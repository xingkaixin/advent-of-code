from __future__ import annotations

import heapq
from pathlib import Path
from typing import Iterable


def parse_points(lines: Iterable[str]) -> list[tuple[int, int, int]]:
    """Parse non-empty lines into a list of 3D integer coordinates."""
    points = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    return points


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.sz = [1] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.sz[ra] < self.sz[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.sz[ra] += self.sz[rb]
        return True


def k_closest_pairs(points: list[tuple[int, int, int]], k: int) -> list[tuple[int, int, int]]:
    """
    Return the k closest point pairs as (distance_squared, i, j) sorted ascending.

    A max-heap of fixed size keeps only the k best pairs while scanning all pairs.
    Ties are resolved by the input order (lower indices first) via the tuple order.
    """
    n = len(points)
    heap: list[tuple[int, int, int]] = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz

            key = (-dist2, -i, -j)
            if len(heap) < k:
                heapq.heappush(heap, key)
            else:
                if key > heap[0]:
                    heapq.heapreplace(heap, key)

    pairs = [(-d, -i, -j) for d, i, j in heap]
    pairs.sort()
    return pairs


def largest_circuit_product(points: list[tuple[int, int, int]], pair_limit: int) -> int:
    """Connect the closest pairs and return the product of the three largest circuit sizes."""
    total_pairs = len(points) * (len(points) - 1) // 2
    connect_count = min(pair_limit, total_pairs)
    if connect_count == 0:
        raise ValueError("Need at least one junction box to form circuits.")

    pairs = k_closest_pairs(points, connect_count)

    dsu = DisjointSet(len(points))
    for _, i, j in pairs:
        dsu.union(i, j)

    sizes = [dsu.sz[idx] for idx in range(len(points)) if dsu.parent[idx] == idx]
    sizes.sort(reverse=True)
    if len(sizes) < 3:
        raise ValueError("Expected at least three circuits to compute the product.")
    return sizes[0] * sizes[1] * sizes[2]


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    points = parse_points(lines)
    return largest_circuit_product(points, 1000)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
