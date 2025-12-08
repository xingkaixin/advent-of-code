def max_joltage_from_bank(bank):
    """
    从一行电池中选择两个电池，产生最大电压

    Args:
        bank (str): 电池银行，如 "987654321111111"

    Returns:
        int: 最大电压
    """
    max_joltage = 0
    # 遍历所有可能的两个电池组合，考虑位置顺序
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # 计算这两个电池产生的电压
            voltage = int(bank[i] + bank[j])
            if voltage > max_joltage:
                max_joltage = voltage
    return max_joltage

def solve_part1(filename=None):
    """
    解决第一部分：计算所有电池银行的最大总电压
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

    # 计算每个银行的最大电压并求和
    for line in lines:
        bank_max = max_joltage_from_bank(line)
        total_joltage += bank_max

    print(f"总输出电压: {total_joltage}")
    return total_joltage

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # 如果提供了文件名参数
        solve_part1(sys.argv[1])
    else:
        # 默认交互式输入
        solve_part1()