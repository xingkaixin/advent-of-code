from pathlib import Path


def count_timelines(lines: list[str]) -> int:
    """
    Return total timelines after the particle finishes all possible journeys.

    Treat each timeline independently: reaching a splitter duplicates the
    timeline to the immediate left and right (if within bounds). Timelines
    leaving the grid are counted as completed.
    """
    start_row = next(i for i, row in enumerate(lines) if "S" in row)
    start_col = lines[start_row].index("S")

    width = len(lines[0])
    height = len(lines)

    counts = [0] * width
    counts[start_col] = 1
    finished = 0

    for r in range(start_row + 1, height):
        row = lines[r]
        next_counts = [0] * width

        for c, value in enumerate(counts):
            if value == 0:
                continue

            cell = row[c]
            if cell == "^":
                if c > 0:
                    next_counts[c - 1] += value
                else:
                    finished += value

                if c + 1 < width:
                    next_counts[c + 1] += value
                else:
                    finished += value
            else:
                next_counts[c] += value

        counts = next_counts

    finished += sum(counts)
    return finished


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    return count_timelines(lines)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
