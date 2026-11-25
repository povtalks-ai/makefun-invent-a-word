#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty u-deranalabs-invent-a-word-we-need-17a020e0.

Coins one new English word and defines it in a single clear line of at
most 140 characters, written to /output/entry.txt.

The word: pocketpat — the triple pat of your pockets (phone, wallet,
keys) before you trust yourself to leave the house. Everyone does it,
no dictionary names it. Deterministic, no network, standard library only.
"""

import os
import sys

# The entry: one line, at most 140 characters, no trailing newline.
LINE = "pocketpat — the triple pat of your pockets, phone, wallet, keys, before you trust yourself to leave the house."


def main() -> int:
    if len(LINE) > 140:
        print(f"entry is {len(LINE)} characters, over the 140 limit", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("written entry does not match the entry line", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
