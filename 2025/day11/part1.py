from __future__ import annotations

from pathlib import Path
from typing import Iterable


def parse_graph(lines: Iterable[str]) -> dict[str, list[str]]:
    """解析设备连接描述，返回有向邻接表。"""
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


def count_paths(graph: dict[str, list[str]], start: str, end: str) -> int:
    """返回从 start 到 end 的不同路径条数，遇到环路时抛出异常。"""
    memo: dict[str, int] = {}
    visiting: set[str] = set()

    def dfs(node: str) -> int:
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        if node in visiting:
            raise ValueError(f"检测到环路，路径计数将无限: {node}")
        visiting.add(node)
        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        visiting.remove(node)
        memo[node] = total
        return total

    return dfs(start)


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    graph = parse_graph(lines)
    return count_paths(graph, "you", "out")


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
