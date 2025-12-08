# Advent of Code 2015 - Day 1: Not Quite Lisp
# Part 1: Calculate final floor
# Part 2: Find position where Santa first enters basement


def calculate_floor(instructions: str) -> int:
    """
    计算Santa最终到达的楼层

    Args:
        instructions: 包含括号指令的字符串

    Returns:
        最终楼层号
    """
    floor = 0
    for char in instructions:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor


def find_basement_position(instructions: str) -> int:
    """
    找到Santa第一次进入地下室（-1楼）的字符位置

    Args:
        instructions: 包含括号指令的字符串

    Returns:
        第一次到达-1楼的字符位置（从1开始计数）
    """
    floor = 0
    for i, char in enumerate(instructions, 1):  # 从1开始计数
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return i

    return -1  # 如果从未进入地下室


def main():
    # 读取输入文件
    with open("input", "r") as f:
        instructions = f.read().strip()

    # Part 1: 计算最终楼层
    final_floor = calculate_floor(instructions)
    print(f"Part 1 - 最终楼层: {final_floor}")

    # Part 2: 找到第一次进入地下室的位置
    basement_position = find_basement_position(instructions)
    print(f"Part 2 - 第一次进入地下室的位置: {basement_position}")


if __name__ == "__main__":
    main()
