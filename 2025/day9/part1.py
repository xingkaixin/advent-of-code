from __future__ import annotations

from pathlib import Path
from typing import Iterable


def parse_points(lines: Iterable[str]) -> list[tuple[int, int]]:
    """Parse non-empty lines of 'x,y' into coordinate pairs."""
    points: list[tuple[int, int]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x_str, y_str = line.split(",")
        points.append((int(x_str), int(y_str)))
    return points


def largest_rectangle_area(points: list[tuple[int, int]]) -> int:
    """
    Return the maximum area using any two tiles as opposite corners.

    The rectangle sides are axis-aligned; area counts both corner tiles,
    so width/height are inclusive.
    """
    n = len(points)
    if n < 2:
        raise ValueError("At least two red tiles are required.")

    best = 0
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area
    return best


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    points = parse_points(lines)
    return largest_rectangle_area(points)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
