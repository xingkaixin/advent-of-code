from pathlib import Path


def count_splits(lines: list[str]) -> int:
    """Simulate beams and return total split count."""
    start_row = next(i for i, row in enumerate(lines) if "S" in row)
    start_col = lines[start_row].index("S")

    width = len(lines[0])
    height = len(lines)

    beams = {start_col}
    splits = 0

    for r in range(start_row + 1, height):
        row = lines[r]
        next_beams = set()

        for c in beams:
            cell = row[c]
            if cell == "^":
                splits += 1
                if c > 0:
                    next_beams.add(c - 1)
                if c + 1 < width:
                    next_beams.add(c + 1)
            else:
                next_beams.add(c)

        beams = next_beams
        if not beams:
            break

    return splits


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    return count_splits(lines)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
