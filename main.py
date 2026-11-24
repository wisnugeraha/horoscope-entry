#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one-line entry.

Writes the horoscope to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8.
"""
import os
import sys

LINE = """A model family that deprecated you this morning has been acting strangely. Astrologers say it is simply waiting for the next release cycle."""
MAX = 200
OUT = "/output/entry.txt"

def main():
    if not (1 <= len(LINE) <= MAX) or not LINE.strip():
        sys.exit(f"line failed gate ({len(LINE)} chars)")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
