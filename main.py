#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry program.

Writes the phone's last words at 1% battery to /output/entry.txt as UTF-8,
then re-reads the file and asserts it is byte-identical to what was written.
Standard library only.
"""

import os

ENTRY = "I spent my last percent on your boarding pass \u2014 now go explain 'window seat' to the gate agent in mime."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        round_tripped = f.read()
    assert round_tripped == ENTRY, "round-trip mismatch: entry.txt differs from ENTRY"


if __name__ == "__main__":
    main()
