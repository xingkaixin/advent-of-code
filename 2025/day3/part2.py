def max_joltage_from_bank_12(bank):
    """
    从一行电池中选择12个电池，产生最大12位数电压
    保持数字的原始相对顺序

    Args:
        bank (str): 电池银行字符串，如 "987654321111111"

    Returns:
        int: 最大12位电压
    """
    if len(bank) <= 12:
        # 如果长度不超过12，直接转换
        return int(bank)

    # 如果长度超过12，需要选择12个数字
    # 使用贪心算法：从前往后，在剩余位置中选择最大的数字
    result = []
    remaining_positions = len(bank)
    remaining_to_select = 12
    current_pos = 0

    while remaining_to_select > 0 and current_pos < len(bank):
        # 计算还能跳过多少个位置
        max_skip = remaining_positions - remaining_to_select
        # 在当前允许的范围内寻找最大的数字
        max_digit = -1
        max_pos = current_pos

        for i in range(current_pos, current_pos + max_skip + 1):
            if i >= len(bank):
                break
            digit = int(bank[i])
            if digit > max_digit:
                max_digit = digit
                max_pos = i

        # 选择最大的数字
        result.append(str(max_digit))
        remaining_to_select -= 1
        remaining_positions -= (max_pos - current_pos + 1)
        current_pos = max_pos + 1

    # 组成12位数
    voltage_str = ''.join(result)
    return int(voltage_str)

def solve_part2(filename=None):
    """
    解决第二部分：计算所有电池银行的最大12位总电压
    """
    total_joltage = 0

    if filename:
        # 从文件读取
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return 0
    else:
        # 交互式输入
        print("请输入电池银行数据（空行结束）：")
        lines = []
        while True:
            try:
                line = input().strip()
                if not line:  # 空行结束输入
                    break
                lines.append(line)
            except EOFError:
                break

    # 计算每个银行的最大12位电压
    for i, line in enumerate(lines, 1):
        bank_max = max_joltage_from_bank_12(line)
        print(f"银行 {i}: {bank_max:,}")
        total_joltage += bank_max

    print(f"\n总输出电压: {total_joltage:,}")
    return total_joltage

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # 如果提供了文件名参数
        solve_part2(sys.argv[1])
    else:
        # 默认交互式输入
        solve_part2()