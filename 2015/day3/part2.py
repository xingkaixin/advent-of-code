#!/usr/bin/env python3
"""
Advent of Code 2015 - Day 3, Part 2
Perfectly Spherical Houses in a Vacuum

圣诞老人和机器人圣诞老人轮流移动，计算收到礼物的房屋数量
"""

def count_houses_with_two_santas(instructions: str) -> int:
    """
    计算圣诞老人和机器人圣诞老人轮流移动时，收到至少一份礼物的房屋数量

    Args:
        instructions: 包含移动指令的字符串，^ v < > 分别表示上下左右

    Returns:
        int: 至少收到一份礼物的房屋数量
    """
    # 两个圣诞老人的起始位置都是 (0, 0)
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    # 起始位置收到两份礼物，但只算作一个房屋
    visited_houses = {(0, 0)}

    # 方向映射
    directions = {
        '^': (0, 1),   # 北
        'v': (0, -1),  # 南
        '>': (1, 0),   # 东
        '<': (-1, 0)   # 西
    }

    # 轮流移动：偶数索引给圣诞老人，奇数索引给机器人圣诞老人
    for i, char in enumerate(instructions):
        if char in directions:
            dx, dy = directions[char]

            if i % 2 == 0:  # 圣诞老人移动
                santa_x += dx
                santa_y += dy
                visited_houses.add((santa_x, santa_y))
            else:  # 机器人圣诞老人移动
                robo_x += dx
                robo_y += dy
                visited_houses.add((robo_x, robo_y))

    return len(visited_houses)

def count_houses_with_two_santas_alternative(instructions: str) -> int:
    """
    另一种实现方式：使用数组存储两个圣诞老人的位置

    Args:
        instructions: 包含移动指令的字符串

    Returns:
        int: 至少收到一份礼物的房屋数量
    """
    # 使用列表存储两个圣诞老人的位置 [santa, robo_santa]
    santas = [(0, 0), (0, 0)]
    visited_houses = {(0, 0)}

    directions = {
        '^': (0, 1),   # 北
        'v': (0, -1),  # 南
        '>': (1, 0),   # 东
        '<': (-1, 0)   # 西
    }

    for i, char in enumerate(instructions):
        if char in directions:
            santa_index = i % 2  # 0: 圣诞老人, 1: 机器人圣诞老人
            dx, dy = directions[char]

            x, y = santas[santa_index]
            x += dx
            y += dy
            santas[santa_index] = (x, y)
            visited_houses.add((x, y))

    return len(visited_houses)

def test_examples():
    """测试给定的例子"""
    print("测试例子：")
    print(f"^v -> {count_houses_with_two_santas('^v')} (期望: 3)")
    print(f"^>v< -> {count_houses_with_two_santas('^>v<')} (期望: 3)")
    print(f"^v^v^v^v^v -> {count_houses_with_two_santas('^v^v^v^v^v')} (期望: 11)")
    print()

def main():
    """主函数：读取输入文件并计算结果"""
    try:
        with open('input', 'r') as file:
            instructions = file.read().strip()

        # 测试例子
        test_examples()

        # 计算结果
        result = count_houses_with_two_santas(instructions)
        print(f"圣诞老人和机器人圣诞老人访问了 {result} 个不同的房屋")

    except FileNotFoundError:
        print("错误：找不到输入文件 'input'")
        return 1
    except Exception as e:
        print(f"发生错误：{e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())