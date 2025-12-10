from __future__ import annotations

import re
from fractions import Fraction
from pathlib import Path
from typing import Iterable

try:  # 复用 part1 中的解析工具
    from .part1 import BUTTON_RE, bits_to_mask
except ImportError:  # pragma: no cover
    BUTTON_RE = re.compile(r"\(([^()]*)\)")

    def bits_to_mask(indices: Iterable[int]) -> int:
        mask = 0
        for idx in indices:
            mask |= 1 << idx
        return mask

JOLTAGE_RE = re.compile(r"\{([^{}]*)\}")


def parse_targets(line: str) -> list[int]:
    """解析花括号中的电压目标列表。"""
    match = JOLTAGE_RE.search(line)
    if not match:
        raise ValueError(f"缺少电压要求: {line}")
    return [int(part) for part in match.group(1).split(",") if part.strip()]


def parse_buttons(line: str) -> list[int]:
    """解析按钮列表，返回每个按钮影响的计数器掩码。"""
    buttons: list[int] = []
    for group in BUTTON_RE.findall(line):
        group = group.strip()
        if not group:
            continue
        indices = [int(part) for part in group.split(",") if part.strip()]
        buttons.append(bits_to_mask(indices))
    return buttons


def parse_machines(lines: Iterable[str]) -> list[tuple[list[int], list[int]]]:
    machines: list[tuple[list[int], list[int]]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        targets = parse_targets(line)
        buttons = parse_buttons(line)
        machines.append((targets, buttons))
    return machines


def rref(matrix: list[list[Fraction]]) -> tuple[list[int], list[list[Fraction]]]:
    """Gauss-Jordan 消元，返回主元列和化简后的矩阵。"""
    m = len(matrix)
    n = len(matrix[0]) - 1  # 最后一列是 RHS
    mat = [row[:] for row in matrix]
    pivot_cols: list[int] = []
    row = 0
    for col in range(n):
        pivot = None
        for r in range(row, m):
            if mat[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        factor = mat[row][col]
        mat[row] = [val / factor for val in mat[row]]
        for r in range(m):
            if r != row and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[row])]
        pivot_cols.append(col)
        row += 1
        if row == m:
            break
    return pivot_cols, mat


def min_button_presses(targets: list[int], buttons: list[int]) -> int:
    """
    计算单台机器的最少按键次数。

    将问题转化为整数线性方程组 Ax=b, x>=0，目标最小化 1^T x。
    按高斯消元找到自由变量（最多 3 个），枚举其非负整数取值，求出主元变量并记录最小和。
    """
    m = len(targets)

    # 丢弃无效按钮（不影响任何计数器）
    filtered: list[int] = [mask for mask in buttons if mask]
    buttons = filtered
    n = len(buttons)
    if n == 0:
        if all(t == 0 for t in targets):
            return 0
        raise ValueError("没有可用按钮来调整电压。")

    # 变量上界：出现在任何包含它的方程中的 RHS 最小值
    var_upper = [min((targets[i] for i in range(m) if mask >> i & 1), default=0) for mask in buttons]

    # 构建增广矩阵
    matrix: list[list[Fraction]] = []
    for i in range(m):
        row = [Fraction(1) if mask >> i & 1 else Fraction(0) for mask in buttons]
        row.append(Fraction(targets[i]))
        matrix.append(row)

    pivot_cols, mat = rref(matrix)
    pivot_set = set(pivot_cols)
    pivot_row_for: dict[int, int] = {col: idx for idx, col in enumerate(pivot_cols)}

    # 无解检测
    for row in mat:
        if all(val == 0 for val in row[:-1]) and row[-1] != 0:
            raise ValueError("方程组无解。")

    free_cols = [c for c in range(n) if c not in pivot_set]
    free_count = len(free_cols)

    if free_count == 0:  # 唯一解
        total = 0
        for col in pivot_cols:
            row_idx = pivot_row_for[col]
            val = mat[row_idx][-1]
            if val.denominator != 1 or val < 0:
                raise ValueError("唯一解不是非负整数。")
            total += val.numerator
        return total

    best = None

    def backtrack(idx: int, free_values: list[int], partial_sum: int) -> None:
        nonlocal best
        if best is not None and partial_sum >= best:
            return
        if idx == free_count:
            total = partial_sum
            for pcol in pivot_cols:
                prow = pivot_row_for[pcol]
                val = mat[prow][-1]
                for fcol, fval in zip(free_cols, free_values):
                    coeff = mat[prow][fcol]
                    if coeff:
                        val -= coeff * fval
                if val < 0 or val.denominator != 1:
                    return
                total += val.numerator
                if best is not None and total >= best:
                    return
            best = total if best is None or total < best else best
            return

        ub = var_upper[free_cols[idx]]
        for val in range(ub + 1):
            free_values.append(val)
            backtrack(idx + 1, free_values, partial_sum + val)
            free_values.pop()

    backtrack(0, [], 0)
    if best is None:
        raise ValueError("无非负整数解。")
    return best


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    machines = parse_machines(lines)
    total = 0
    for targets, buttons in machines:
        total += min_button_presses(targets, buttons)
    return total


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
