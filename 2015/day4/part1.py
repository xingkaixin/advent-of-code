#!/usr/bin/env python3
"""
Advent of Code 2015 - Day 4, Part 1
The Ideal Stocking Stuffer

找到密钥和数字组合的MD5哈希以5个0开头的小正整数
"""

import hashlib

def find_adventcoin(secret_key: str, prefix_zeros: int = 5) -> int:
    """
    找到使MD5哈希以指定数量0开头的最小正整数

    Args:
        secret_key: 密钥字符串
        prefix_zeros: 哈希开头需要的0的个数

    Returns:
        int: 符合条件的最小正整数
    """
    target_prefix = '0' * prefix_zeros

    # 从1开始逐步尝试每个正整数
    for number in range(1, 10000000):  # 设置一个合理的上限
        # 构建要哈希的字符串
        test_string = f"{secret_key}{number}"

        # 计算MD5哈希
        hash_result = hashlib.md5(test_string.encode()).hexdigest()

        # 检查是否以足够数量的0开头
        if hash_result.startswith(target_prefix):
            return number

    # 如果没找到（理论上不应该发生）
    raise ValueError(f"在10000000次尝试内未找到符合条件的数字")

def test_examples():
    """测试给定的例子"""
    print("测试例子：")

    # 例子1: abcdef -> 609043
    result1 = find_adventcoin("abcdef")
    expected1 = 609043
    print(f"abcdef -> {result1} (期望: {expected1}) {'✓' if result1 == expected1 else '✗'}")

    # 例子2: pqrstuv -> 1048970
    result2 = find_adventcoin("pqrstuv")
    expected2 = 1048970
    print(f"pqrstuv -> {result2} (期望: {expected2}) {'✓' if result2 == expected2 else '✗'}")
    print()

def main():
    """主函数：读取输入文件并计算结果"""
    try:
        with open('input', 'r') as file:
            secret_key = file.read().strip()

        print(f"正在为密钥 '{secret_key}' 寻找AdventCoin...")

        # 测试例子
        test_examples()

        # 计算实际结果
        result = find_adventcoin(secret_key)
        print(f"找到答案：{result}")
        print(f"验证：{secret_key}{result} 的MD5哈希以5个0开头")

    except FileNotFoundError:
        print("错误：找不到输入文件 'input'")
        return 1
    except Exception as e:
        print(f"发生错误：{e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())