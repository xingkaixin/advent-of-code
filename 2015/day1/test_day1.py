# 测试 Advent of Code 2015 Day 1 解决方案
from day1_part1 import calculate_floor, find_basement_position


def test_part1():
    # Part 1 测试用例
    assert calculate_floor("(())") == 0
    assert calculate_floor("()()") == 0
    assert calculate_floor("(((") == 3
    assert calculate_floor("(()(()(") == 3
    assert calculate_floor("))(((((") == 3
    assert calculate_floor("())") == -1
    assert calculate_floor("))(") == -1
    assert calculate_floor(")))") == -3
    assert calculate_floor(")())())") == -3
    print("✅ Part 1 所有测试用例通过")


def test_part2():
    # Part 2 测试用例
    assert find_basement_position(")") == 1
    assert find_basement_position("()())") == 5
    print("✅ Part 2 所有测试用例通过")


if __name__ == "__main__":
    test_part1()
    test_part2()
