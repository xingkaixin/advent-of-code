from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SHAPE_HEADER_RE = re.compile(r"^(\d+):\s*$")
REGION_RE = re.compile(r"^(\d+)x(\d+):\s*(.*)$")


@dataclass(frozen=True)
class Region:
    width: int
    height: int
    quantities: tuple[int, ...]

    @property
    def area(self) -> int:
        return self.width * self.height


def parse_shapes_and_regions(lines: Iterable[str]) -> tuple[list[int], list[Region]]:
    """
    解析输入，返回每种礼物的面积列表（按索引排序）以及区域列表。

    输入分两段：
    - 第一段为形状定义：`idx:` 后跟若干行 `.#` 图案。
    - 第二段为区域定义：`WxH:` 后跟每种形状数量。
    """
    shapes: dict[int, list[str]] = {}
    regions: list[Region] = []

    current_idx: int | None = None
    current_grid: list[str] = []
    in_regions = False

    def flush_shape() -> None:
        nonlocal current_idx, current_grid
        if current_idx is not None and current_grid:
            shapes[current_idx] = current_grid
        current_idx = None
        current_grid = []

    for raw in lines:
        line = raw.strip()
        if not line:
            if not in_regions:
                flush_shape()
            continue

        region_match = REGION_RE.match(line)
        if region_match:
            in_regions = True
            flush_shape()
            width, height = map(int, region_match.group(1, 2))
            quantities_str = region_match.group(3).strip()
            quantities = tuple(int(x) for x in quantities_str.split()) if quantities_str else ()
            regions.append(Region(width, height, quantities))
            continue

        if in_regions:
            raise ValueError(f"区域定义中出现无法解析的行: {line}")

        header_match = SHAPE_HEADER_RE.match(line)
        if header_match:
            flush_shape()
            current_idx = int(header_match.group(1))
            continue

        if current_idx is None:
            raise ValueError(f"缺少形状索引头: {line}")
        current_grid.append(line)

    flush_shape()

    if not shapes:
        raise ValueError("未解析到任何形状定义。")

    max_idx = max(shapes)
    if set(shapes) != set(range(max_idx + 1)):
        raise ValueError(f"形状索引需从 0 连续递增，实际为: {sorted(shapes)}")

    shape_areas: list[int] = []
    for idx in range(max_idx + 1):
        grid = shapes[idx]
        shape_areas.append(sum(row.count("#") for row in grid))

    for region in regions:
        if len(region.quantities) != len(shape_areas):
            raise ValueError(
                f"区域数量与形状数量不一致: {region.quantities} vs {len(shape_areas)}"
            )

    return shape_areas, regions


def count_fit_regions(shape_areas: list[int], regions: list[Region]) -> int:
    """
    Part1 的关键结论：只要所有礼物占用的总面积不超过矩形面积，就一定能放下。
    因此逐个区域做面积校验即可。
    """
    total = 0
    for region in regions:
        used_area = sum(q * a for q, a in zip(region.quantities, shape_areas))
        if used_area <= region.area:
            total += 1
    return total


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    shape_areas, regions = parse_shapes_and_regions(lines)
    return count_fit_regions(shape_areas, regions)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")

