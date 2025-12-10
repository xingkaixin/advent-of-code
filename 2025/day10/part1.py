from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

LIGHTS_RE = re.compile(r"\[([.#]+)\]")
BUTTON_RE = re.compile(r"\(([^()]*)\)")


def bits_to_mask(indices: Iterable[int]) -> int:
    """Convert a list of indicator indices to a bitmask."""
    mask = 0
    for idx in indices:
        mask |= 1 << idx
    return mask


def parse_machine(line: str) -> tuple[int, list[int]]:
    """Return the target mask and button masks for one machine description."""
    lights_match = LIGHTS_RE.search(line)
    if not lights_match:
        raise ValueError(f"Missing indicator diagram in line: {line}")
    lights = lights_match.group(1)

    target_mask = 0
    for pos, ch in enumerate(lights):
        if ch == "#":
            target_mask |= 1 << pos

    buttons: list[int] = []
    for group in BUTTON_RE.findall(line):
        group = group.strip()
        if not group:
            continue
        indices = [int(part) for part in group.split(",") if part.strip()]
        buttons.append(bits_to_mask(indices))

    return target_mask, buttons


def parse_machines(lines: Iterable[str]) -> list[tuple[int, list[int]]]:
    machines: list[tuple[int, list[int]]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        machines.append(parse_machine(line))
    return machines


def min_button_presses(target_mask: int, buttons: list[int]) -> int:
    """Brute-force the fewest button presses to reach the target configuration."""
    if not buttons and target_mask:
        raise ValueError("No buttons available to toggle indicators.")

    best: int | None = None
    total_combos = 1 << len(buttons)

    for combo in range(total_combos):
        state = 0
        presses = 0
        for idx, mask in enumerate(buttons):
            if combo & (1 << idx):
                state ^= mask
                presses += 1

        if state == target_mask:
            if best is None or presses < best:
                best = presses
                if best == 0:
                    return 0

    if best is None:
        raise ValueError("Unable to configure indicators with available buttons.")
    return best


def solve() -> int:
    input_file = Path(__file__).parent / "input.txt"
    lines = input_file.read_text().splitlines()
    machines = parse_machines(lines)
    return sum(min_button_presses(target, buttons) for target, buttons in machines)


if __name__ == "__main__":
    answer = solve()
    print(f"Answer: {answer}")
