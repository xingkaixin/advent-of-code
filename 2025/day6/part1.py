import re
from pathlib import Path


def solve():
    """
    Solve 2025 Day 6: Trash Compactor

    The worksheet consists of 4 rows of numbers and 1 row of operators.
    Each column forms a problem:
    - If operator is '*', multiply the four numbers
    - If operator is '+', add the four numbers

    Return the grand total of all problem answers.
    """
    input_file = Path(__file__).parent / 'input.txt'

    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Parse input
    nums = []
    for line in lines[:4]:
        nums.append([int(x) for x in re.findall(r'\d+', line)])

    ops = re.findall(r'[+*]', lines[4])

    # Calculate total
    total = 0
    for i in range(min(len(n) for n in nums)):
        if i < len(ops):
            if ops[i] == '*':
                total += nums[0][i] * nums[1][i] * nums[2][i] * nums[3][i]
            else:  # '+'
                total += nums[0][i] + nums[1][i] + nums[2][i] + nums[3][i]

    return total


if __name__ == '__main__':
    answer = solve()
    print(f"Answer: {answer:,}")
