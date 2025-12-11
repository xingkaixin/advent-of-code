from __future__ import annotations

from pathlib import Path

try:
    from .part1 import parse_graph
except ImportError:  # pragma: no cover - 方便独立运行
    def parse_graph(lines):
        graph: dict[str, list[str]] = {}
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            if ":" not in line:
                raise ValueError(f"缺少冒号分隔符: {line}")
            name_part, targets_part = line.split(":", 1)
            name = name_part.strip()
            if name in graph and graph[name]:
                raise ValueError(f"重复的设备定义: {name}")
            targets = [item for item in targets_part.strip().split() if item]
            graph[name] = targets
            for target in targets:
                graph.setdefault(target, [])
        return graph


def build_path_counts(graph: dict[str, list[str]], target: str) -> dict[str, int]:
    """
    返回每个节点到 target 的路径条数。

    采用带记忆的 DFS，若检测到环路则抛出异常避免无限计数。
    """
    memo: dict[str, int] = {}
    visiting: set[str] = set()

    def dfs(node: str) -> int:
        if node == target:
            return 1
        if node in memo:
            return memo[node]
        if node in visiting:
            raise ValueError(f"检测到环路，无法统计路径: {node}")
        visiting.add(node)
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        visiting.remove(node)
        memo[node] = total
        return total

    for node in graph.keys():
        if node not in memo:
            dfs(node)
    memo[target] = 1
    return memo


def count_paths_through_both(
    graph: dict[str, list[str]], start: str, first: str, second: str, end: str
) -> int:
    """统计从 start 到 end 且经过 first 和 second（顺序任意）的路径数量。"""
    to_first = build_path_counts(graph, first)
    to_second = build_path_counts(graph, second)
    to_end = build_path_counts(graph, end)

    first_then_second = (
        to_first.get(start, 0) * to_second.get(first, 0) * to_end.get(second, 0)
    )
    second_then_first = (
        to_second.get(start, 0) * to_first.get(second, 0) * to_end.get(first, 0)
    )
    return first_then_second + second_then_first


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    graph = parse_graph(lines)
    return count_paths_through_both(graph, "svr", "dac", "fft", "out")


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
