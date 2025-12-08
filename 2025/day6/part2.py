from math import prod
from pathlib import Path


def solve():
    """
    Solve 2025 Day 6 Part 2 by reading the worksheet right-to-left.

    Each column (right to left) forms one number from top to bottom.
    Columns made entirely of spaces separate problems.
    The operator for a problem is the non-space symbol in the bottom row
    inside that group of columns.
    """
    input_file = Path(__file__).parent / "input.txt"

    lines = [line.rstrip("\n") for line in input_file.read_text().splitlines()]

    # Pad all rows so every column index exists.
    width = max(len(line) for line in lines)
    padded = [line.ljust(width) for line in lines]
    digit_rows = len(padded) - 1

    def process_problem(columns):
        """Given collected columns (right-to-left order), compute the problem value."""
        ops = {col[-1] for col in columns if col[-1] != " "}
        if len(ops) != 1:
            raise ValueError(f"Expected 1 operator, found {ops}")
        op = ops.pop()

        numbers = []
        for col in columns:
            digits = [ch for ch in col[:digit_rows] if ch != " "]
            if not digits:
                raise ValueError("Encountered a column without digits.")
            numbers.append(int("".join(digits)))

        return sum(numbers) if op == "+" else prod(numbers)

    total = 0
    current = []

    for col_idx in reversed(range(width)):
        column = [row[col_idx] for row in padded]
        if all(ch == " " for ch in column):
            if current:
                total += process_problem(current)
                current = []
            continue
        current.append(column)

    if current:
        total += process_problem(current)

    return total


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer:,}")
