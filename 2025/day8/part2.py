from __future__ import annotations

import heapq
from pathlib import Path

try:  # 兼容直接运行与包内导入
    from .part1 import DisjointSet, parse_points  # type: ignore
except ImportError:  # pragma: no cover
    from part1 import DisjointSet, parse_points


def last_connection_product(points) -> int:
    """
    依距离从近到远连接，直到所有节点同属一个电路，返回最后一条连接的X坐标乘积。
    """
    n = len(points)
    if n < 2:
        raise ValueError("至少需要两个接线盒。")

    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz
            pairs.append((dist2, i, j))

    heapq.heapify(pairs)

    dsu = DisjointSet(n)
    components = n
    last_pair = None

    while components > 1:
        dist2, i, j = heapq.heappop(pairs)
        if dsu.union(i, j):
            components -= 1
            last_pair = (points[i][0], points[j][0])

    if last_pair is None:
        raise RuntimeError("未找到有效的连接。")
    return last_pair[0] * last_pair[1]


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    points = parse_points(lines)
    return last_connection_product(points)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
