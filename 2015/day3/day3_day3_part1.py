#!/usr/bin/env python3
"""
Advent of Code 2015 - Day 3, Part 1
Perfectly Spherical Houses in a Vacuum

计算圣诞老人按照指令访问过的不同房屋数量
"""

def count_houses_with_presents(instructions: str) -> int:
    """
    计算圣诞老人按照指令访问过的不同房屋数量

    Args:
        instructions: 包含移动指令的字符串，^ v < > 分别表示上下左右

    Returns:
        int: 至少收到一份礼物的房屋数量
    """
    # 起始位置 (0, 0)
    x, y = 0, 0

    # 使用集合存储访问过的房屋坐标，确保去重
    visited_houses = {(x, y)}

    # 方向映射
    directions = {
        '^': (0, 1),   # 北
        'v': (0, -1),  # 南
        '>': (1, 0),   # 东
        '<': (-1, 0)   # 西
    }

    for char in instructions:
        if char in directions:
            dx, dy = directions[char]
            x += dx
            y += dy
            visited_houses.add((x, y))

    return len(visited_houses)

def main():
    """主函数：读取输入文件并计算结果"""
    try:
        with open('2015/day3/input', 'r') as file:
            instructions = file.read().strip()

        result = count_houses_with_presents(instructions)
        print(f"圣诞老人访问了 {result} 个不同的房屋")

    except FileNotFoundError:
        print("错误：找不到输入文件 '2015/day3/input'")
        return 1
    except Exception as e:
        print(f"发生错误：{e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())