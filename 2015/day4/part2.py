#!/usr/bin/env python3
"""
Advent of Code 2015 - Day 4, Part 2
The Ideal Stocking Stuffer

找到密钥和数字组合的MD5哈希以6个0开头的小正整数
"""

import hashlib
import time

def find_adventcoin_with_progress(secret_key: str, prefix_zeros: int = 6, show_progress: bool = True) -> int:
    """
    找到使MD5哈希以指定数量0开头的最小正整数，支持进度显示

    Args:
        secret_key: 密钥字符串
        prefix_zeros: 哈希开头需要的0的个数
        show_progress: 是否显示进度

    Returns:
        int: 符合条件的最小正整数
    """
    target_prefix = '0' * prefix_zeros
    start_time = time.time()
    last_report = 0

    # 从1开始逐步尝试每个正整数
    for number in range(1, 100000000):  # 设置更大的上限
        # 构建要哈希的字符串
        test_string = f"{secret_key}{number}"

        # 计算MD5哈希
        hash_result = hashlib.md5(test_string.encode()).hexdigest()

        # 检查是否以足够数量的0开头
        if hash_result.startswith(target_prefix):
            end_time = time.time()
            if show_progress:
                print(f"找到答案！用时 {end_time - start_time:.2f} 秒")
            return number

        # 每隔一定数量显示进度
        if show_progress and number % 1000000 == 0 and number != last_report:
            elapsed = time.time() - start_time
            rate = number / elapsed if elapsed > 0 else 0
            print(f"已尝试 {number:,} 次，用时 {elapsed:.1f} 秒，速度: {rate:,.0f} 次/秒")
            last_report = number

    # 如果没找到（理论上不应该发生）
    raise ValueError(f"在100000000次尝试内未找到符合条件的数字")

def find_adventcoin(secret_key: str, prefix_zeros: int = 5) -> int:
    """
    简化版本的AdventCoin查找函数

    Args:
        secret_key: 密钥字符串
        prefix_zeros: 哈希开头需要的0的个数

    Returns:
        int: 符合条件的最小正整数
    """
    return find_adventcoin_with_progress(secret_key, prefix_zeros, show_progress=False)

def test_examples():
    """测试给定的例子"""
    print("测试例子（5个0）：")

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
        print()

        # 第一部分：5个0（用于对比）
        print("=== 第一部分：5个0 ===")
        test_examples()

        print(f"计算5个0开头的答案...")
        start_time = time.time()
        result5 = find_adventcoin(secret_key, 5)
        time5 = time.time() - start_time
        print(f"5个0的答案：{result5}，用时 {time5:.3f} 秒")
        print()

        # 第二部分：6个0
        print("=== 第二部分：6个0 ===")
        print(f"计算6个0开头的答案...")
        result6 = find_adventcoin_with_progress(secret_key, 6)
        print(f"6个0的答案：{result6}")
        print(f"验证：{secret_key}{result6} 的MD5哈希以6个0开头")
        print()

        # 验证结果
        hash5 = hashlib.md5(f"{secret_key}{result5}".encode()).hexdigest()
        hash6 = hashlib.md5(f"{secret_key}{result6}".encode()).hexdigest()
        print(f"验证 5个0：{secret_key}{result5} -> {hash5[:10]}...")
        print(f"验证 6个0：{secret_key}{result6} -> {hash6[:10]}...")
        print()
        print(f"对比：6个0的答案比5个0的答案大 {result6 - result5:,} 倍")

    except FileNotFoundError:
        print("错误：找不到输入文件 'input'")
        return 1
    except Exception as e:
        print(f"发生错误：{e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())