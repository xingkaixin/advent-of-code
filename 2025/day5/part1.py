#!/usr/bin/env python3
"""
Day 5: Cafeteria
统计新鲜的食材ID数量
"""

import bisect
from typing import List, Tuple


def parse_ranges(lines: List[str]) -> List[Tuple[int, int]]:
    """解析新鲜食材ID范围"""
    ranges = []
    for line in lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    return ranges


def parse_available_ids(lines: List[str]) -> List[int]:
    """解析可用食材ID"""
    ids = []
    for line in lines:
        if line.strip() and '-' not in line:
            ids.append(int(line.strip()))
    return ids


def is_fresh(id_to_check: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    使用二分查找判断ID是否在任何新鲜范围内
    由于范围可能重叠且排序不完美，需要检查多个候选范围
    """
    if not ranges:
        return False

    # 找到第一个起始位置大于id_to_check的索引
    idx = bisect.bisect_right(ranges, (id_to_check,))

    # 检查前一个范围（最有可能包含）及其前一个范围
    if idx > 0:
        for i in range(max(0, idx-2), idx):
            start, end = ranges[i]
            if start <= id_to_check <= end:
                return True

    # 检查当前范围（如果存在）及其下一个范围
    if idx < len(ranges):
        for i in range(idx, min(len(ranges), idx+2)):
            start, end = ranges[i]
            if start <= id_to_check <= end:
                return True

    return False


def solve():
    # 读取输入文件
    with open('input.txt', 'r') as f:
        all_lines = f.readlines()

    # 找到空白行的位置
    blank_index = None
    for i, line in enumerate(all_lines):
        if line.strip() == '':
            blank_index = i
            break

    if blank_index is None:
        print("未找到空白行，无法分隔范围和数据")
        return

    # 分割范围和可用ID
    range_lines = all_lines[:blank_index]
    available_lines = all_lines[blank_index + 1:]

    # 解析数据
    fresh_ranges = parse_ranges(range_lines)
    available_ids = parse_available_ids(available_lines)

    # 按范围起始位置排序
    fresh_ranges.sort()

    # 统计新鲜的食材ID数量
    fresh_count = 0
    for avail_id in available_ids:
        if is_fresh(avail_id, fresh_ranges):
            fresh_count += 1

    print(f"新鲜食材ID数量: {fresh_count}")


if __name__ == "__main__":
    solve()
