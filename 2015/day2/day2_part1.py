def calculate_wrapping_paper(dimensions: str) -> int:
    """
    计算一个礼物的包装纸需求

    Args:
        dimensions: 格式为 "l x w x h" 的字符串，例如 "2x3x4"

    Returns:
        所需的包装纸总面积（平方英尺）
    """
    # 清理输入：移除行号和箭头
    # 格式可能是 "29x13x26" 或 "1→29x13x26"
    if '→' in dimensions:
        # 移除行号和箭头部分
        dimensions = dimensions.split('→')[1]

    dimensions = dimensions.strip()

    # 解析尺寸
    l, w, h = map(int, dimensions.split('x'))

    # 计算表面积：2*l*w + 2*w*h + 2*h*l
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l

    # 计算最小面的面积
    areas = [l * w, w * h, h * l]
    smallest_area = min(areas)

    # 总包装纸 = 表面积 + 最小面面积
    return surface_area + smallest_area


def solve_part1(input_data: str) -> int:
    """
    解决第一部分：计算所有礼物的总包装纸需求

    Args:
        input_data: 包含所有礼物尺寸的多行字符串

    Returns:
        所有礼物的总包装纸面积
    """
    total = 0
    for line in input_data.strip().split('\n'):
        if line.strip():  # 跳过空行
            total += calculate_wrapping_paper(line.strip())

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

        result = solve_part1(input_data)
        print(f"总包装纸需求：{result} 平方英尺")

    except FileNotFoundError:
        print("错误：找不到输入文件 'day2-input'")
    except Exception as e:
        print(f"错误：{e}")


if __name__ == "__main__":
    main()