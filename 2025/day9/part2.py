from __future__ import annotations

from pathlib import Path

try:  # 兼容包内导入与直接运行
    from .part1 import parse_points
except ImportError:  # pragma: no cover
    from part1 import parse_points


def build_edges(points: list[tuple[int, int]]):
    """按顺序构建闭合折线边列表，每条边记录方向。"""
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append((x1, y1, x2, y2, x1 == x2))
    return edges


def point_on_segment(px: float, py: float, x1: int, y1: int, x2: int, y2: int) -> bool:
    """判断点是否落在闭合线段上。"""
    if x1 == x2:  # 垂直
        return px == x1 and min(y1, y2) <= py <= max(y1, y2)
    if y1 == y2:  # 水平
        return py == y1 and min(x1, x2) <= px <= max(x1, x2)
    return False


def point_in_polygon(px: float, py: float, edges) -> bool:
    """
    偶奇法判定点是否在（含边界）简单矩形折线内。

    仅使用垂直边做扫描，避免水平边的双计数问题。
    """
    inside = False
    for x1, y1, x2, y2, is_vertical in edges:
        if point_on_segment(px, py, x1, y1, x2, y2):
            return True
        if is_vertical:
            y_low, y_high = sorted((y1, y2))
            if y_low <= py < y_high and x1 > px:
                inside = not inside
    return inside


def rectangle_inside_polygon(x_low: int, x_high: int, y_low: int, y_high: int, edges) -> bool:
    """
    矩形（含边界）是否完全位于折线围成区域。

    检查矩形中心在内且折线不穿过矩形内部。
    """
    cx = (x_low + x_high) / 2
    cy = (y_low + y_high) / 2
    if not point_in_polygon(cx, cy, edges):
        return False

    for x1, y1, x2, y2, is_vertical in edges:
        if is_vertical:
            if x_low < x1 < x_high:
                y_min, y_max = sorted((y1, y2))
                if y_max > y_low and y_min < y_high:
                    return False
        else:
            if y_low < y1 < y_high:
                x_min, x_max = sorted((x1, x2))
                if x_max > x_low and x_min < x_high:
                    return False
    return True


def largest_rectangle_within_loop(points: list[tuple[int, int]]) -> int:
    """返回仅由红/绿瓷砖构成的最大矩形面积。"""
    n = len(points)
    if n < 2:
        raise ValueError("至少需要两块红砖。")

    edges = build_edges(points)
    best = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area <= best:
                continue

            x_low, x_high = sorted((x1, x2))
            y_low, y_high = sorted((y1, y2))

            if rectangle_inside_polygon(x_low, x_high, y_low, y_high, edges):
                best = area
    return best


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    points = parse_points(lines)
    return largest_rectangle_within_loop(points)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
