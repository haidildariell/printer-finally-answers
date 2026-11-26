#!/usr/bin/env python3
"""The Printer Finally Answers - entry for make.fun.

Writes the printer's reply, exactly one line, to the output file.
"""

import os

PRINTER_REPLY = "I ate your report. It is still in my belly, warm, stapled, and upside down."

MAX_CHARS = 240

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def validate_line(line):
    """The entry must be exactly one line of 1-240 characters."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry line must be 1-240 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(path, line):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_line(line) + "\n")


def main():
    write_entry(OUTPUT_PATH, PRINTER_REPLY)


if __name__ == "__main__":
    main()
