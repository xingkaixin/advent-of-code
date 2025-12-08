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

    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        all_invalid_ids.extend(invalid_ids)
        print(f"范围 {start}-{end}: 找到无效ID {invalid_ids}")

    total = sum(all_invalid_ids)
    print(f"所有无效ID: {all_invalid_ids}")
    print(f"总和: {total}")
    return total

# 测试示例
if __name__ == "__main__":
    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    print("测试示例数据:")
    result = solve_part1(example_input)
    print(f"示例结果: {result}")
    print(f"期望结果: 1227775554")