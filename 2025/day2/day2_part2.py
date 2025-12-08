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

    for i, (start, end) in enumerate(ranges, 1):
        invalid_ids = find_invalid_ids_in_range_part2(start, end)
        all_invalid_ids.extend(invalid_ids)
        print(f"范围 {i}: {start}-{end} -> 无效ID: {invalid_ids}")

    total = sum(all_invalid_ids)
    print(f"\n所有无效ID: {len(all_invalid_ids)} 个")
    print(f"总和: {total}")
    return total

# 测试示例
if __name__ == "__main__":
    # 先测试一些具体的数字
    print("测试重复序列检测:")
    test_numbers = [12341234, 123123123, 1212121212, 1111111, 12345, 1212, 123123]
    for num in test_numbers:
        result = is_invalid_id_part2(num)
        print(f"{num}: {'无效ID' if result else '有效ID'}")

    print("\n" + "="*50)

    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    print("测试示例数据:")
    result = solve_part2(example_input)
    print(f"示例结果: {result}")
    print(f"期望结果: 4174379265")