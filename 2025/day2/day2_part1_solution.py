def is_invalid_id(n):
    """
    检查一个ID是否由某个数字序列重复两次组成
    例如：55 (5重复两次), 6464 (64重复两次), 123123 (123重复两次)
    """
    s = str(n)
    length = len(s)

    # 如果长度是偶数，才可能由重复序列组成
    if length % 2 != 0:
        return False

    half_len = length // 2
    first_half = s[:half_len]
    second_half = s[half_len:]

    return first_half == second_half

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

def find_invalid_ids_in_range(start, end):
    """
    在给定范围内找出所有无效ID
    """
    invalid_ids = []
    for n in range(start, end + 1):
        if is_invalid_id(n):
            invalid_ids.append(n)
    return invalid_ids

def solve_part1(ranges_str):
    """
    解决第一部分：找出所有范围内的无效ID并求和
    """
    ranges = parse_ranges(ranges_str)
    all_invalid_ids = []

    print(f"开始处理 {len(ranges)} 个范围...")

    for i, (start, end) in enumerate(ranges, 1):
        invalid_ids = find_invalid_ids_in_range(start, end)
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

    print("处理实际输入数据:")
    result = solve_part1(actual_input)
    print(f"\n最终答案: {result}")