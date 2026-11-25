#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life one-liner.

Writes a single joke about office life to /output/entry.txt.
Deterministic: no input, no network, no randomness, no environment
secrets. The same line is written on every run, byte for byte.
"""

import os

JOKE = (
    "The office fridge has its own legal system: your lunch is evidence, "
    "the sticky note is a sworn statement, and the thief is management."
)


def main() -> None:
    # The gate accepts 1-200 characters; refuse to write anything outside it
    # rather than submit an invalid entry.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate needs 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
