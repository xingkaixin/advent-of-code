def is_invalid_id_part2(n):
    """
    检查一个ID是否由某个数字序列重复至少两次组成
    Part 2规则：12341234 (1234重复2次), 123123123 (123重复3次), 1212121212 (12重复4次), 1111111 (1重复7次)
    """
    s = str(n)
    length = len(s)

    # 尝试所有可能的序列长度 (1 到 length//2)
    for seq_len in range(1, length // 2 + 1):
        if length % seq_len == 0:  # 只有当长度能被序列长度整除时才可能
            times = length // seq_len
            if times >= 2:  # 至少重复两次
                sequence = s[:seq_len]
                repeated = sequence * times
                if repeated == s:
                    return True
    return False

def parse_ranges(ranges_str):
    """
    解析输入的ID范围字符串
    例如： "11-22,95-115" -> [(11, 22), (95, 115)]
    """
    ranges = []
    for range_str in ranges_str.split(','):
        if range_str.strip():  # 忽略空字符串
            start, end = map(int, range_str.strip().split('-'))
            ranges.append((start, end))
    return ranges

def find_invalid_ids_in_range_part2(start, end):
    """
    在给定范围内找出所有无效ID (Part 2规则)
    """
    invalid_ids = []
    for n in range(start, end + 1):
        if is_invalid_id_part2(n):
            invalid_ids.append(n)
    return invalid_ids

def solve_part2(ranges_str):
    """
    解决第二部分：找出所有范围内的无效ID (Part 2规则) 并求和
    """
    ranges = parse_ranges(ranges_str)
    all_invalid_ids = []

    print(f"开始处理 {len(ranges)} 个范围...")

    for i, (start, end) in enumerate(ranges, 1):
        invalid_ids = find_invalid_ids_in_range_part2(start, end)
        all_invalid_ids.extend(invalid_ids)
        if invalid_ids:  # 只打印找到无效ID的范围
            print(f"范围 {i}: {start}-{end} -> 无效ID: {invalid_ids}")

    total = sum(all_invalid_ids)
    print(f"\n找到的所有无效ID: {len(all_invalid_ids)} 个")
    print(f"总和: {total}")
    return total

# 处理实际输入
if __name__ == "__main__":
    # 读取实际输入文件
    with open('day2/input', 'r') as f:
        actual_input = f.read().strip()

    print("处理实际输入数据 (Part 2):")
    result = solve_part2(actual_input)
    print(f"\n最终答案 (Part 2): {result}")