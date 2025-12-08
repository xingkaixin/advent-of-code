def calculate_ribbon(dimensions: str) -> int:
    """
    计算一个礼物的丝带需求

    Args:
        dimensions: 格式为 "l x w x h" 的字符串，例如 "2x3x4"

    Returns:
        所需的丝带总长度（英尺）
    """
    # 清理输入：移除行号和箭头
    # 格式可能是 "29x13x26" 或 "1→29x13x26"
    if '→' in dimensions:
        # 移除行号和箭头部分
        dimensions = dimensions.split('→')[1]

    dimensions = dimensions.strip()

    # 解析尺寸
    l, w, h = map(int, dimensions.split('x'))

    # 计算包装丝带：最小周长（最小的两个尺寸的2倍）
    # 找出最小的两个尺寸
    sides = sorted([l, w, h])
    wrapping_ribbon = 2 * (sides[0] + sides[1])

    # 计算蝴蝶结丝带：体积
    bow_ribbon = l * w * h

    # 总丝带 = 包装丝带 + 蝴蝶结丝带
    return wrapping_ribbon + bow_ribbon


def solve_part2(input_data: str) -> int:
    """
    解决第二部分：计算所有礼物的总丝带需求

    Args:
        input_data: 包含所有礼物尺寸的多行字符串

    Returns:
        所有礼物的总丝带长度
    """
    total = 0
    for line in input_data.strip().split('\n'):
        if line.strip():  # 跳过空行
            total += calculate_ribbon(line.strip())

    return total


def main():
    """主函数：读取输入文件并输出结果"""
    try:
        import os
        # 获取当前脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, 'day2-input')

        with open(input_file, 'r') as f:
            input_data = f.read()

        result = solve_part2(input_data)
        print(f"总丝带需求：{result} 英尺")

    except FileNotFoundError:
        print("错误：找不到输入文件 'day2-input'")
    except Exception as e:
        print(f"错误：{e}")


if __name__ == "__main__":
    main()