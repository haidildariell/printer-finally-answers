#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes a single line - the office printer's own comeback - to
/output/entry.txt (or to the path in the ENTRY_OUTPUT_PATH env var,
used for local testing).
"""

import os

LINE = "You stare at my blinking light like it owes you an apology. It blinks. That is the apology."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
