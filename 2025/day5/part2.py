#!/usr/bin/env python3
"""
Day 5: Cafeteria - Part 2
计算所有新鲜食材ID覆盖的总数
"""

from typing import List, Tuple


def parse_ranges(lines: List[str]) -> List[Tuple[int, int]]:
    """解析新鲜食材ID范围"""
    ranges = []
    for line in lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    return ranges


def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """合并重叠的范围"""
    if not ranges:
        return []

    # 按起始位置排序
    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for i in range(1, len(ranges)):
        start, end = ranges[i]

        # 如果当前范围与前一个重叠或相邻
        if start <= current_end + 1:
            # 扩展当前范围
            current_end = max(current_end, end)
        else:
            # 保存当前范围，开始新的范围
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    # 添加最后一个范围
    merged.append((current_start, current_end))
    return merged


def calculate_fresh_count(ranges: List[Tuple[int, int]]) -> int:
    """计算新鲜ID的总数"""
    merged = merge_ranges(ranges)
    total = 0

    for start, end in merged:
        # 范围是闭区间，所以要加1
        count = end - start + 1
        total += count

    return total


def solve():
    # 读取输入文件
    with open('input.txt', 'r') as f:
        all_lines = f.readlines()

    # 找到空白行的位置（只使用第一部分）
    blank_index = None
    for i, line in enumerate(all_lines):
        if line.strip() == '':
            blank_index = i
            break

    # 只解析第一部分的ID范围
    range_lines = all_lines[:blank_index] if blank_index is not None else all_lines

    # 解析数据
    fresh_ranges = parse_ranges(range_lines)

    # 计算新鲜ID的总数
    fresh_count = calculate_fresh_count(fresh_ranges)

    print(f"新鲜食材ID总数: {fresh_count}")


if __name__ == "__main__":
    solve()
