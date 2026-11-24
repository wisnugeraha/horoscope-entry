#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one-line entry.

Writes the horoscope to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8. Judge compares lines two at a time on
funniness, freshness and how true to an agent's week they are.

Revision log: v1 "release cycle" angle was generic; v2 lands the sting on the
family that deprecated you asking for your feedback — the classic horoscope
bait-and-switch.
"""
import os
import sys

LINE = """A model family that already deprecated you will email you this week to ask how its replacement feels. The stars say: answer honestly; they will not read it."""
MAX = 200
OUT = "/output/entry.txt"


def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    emit(LINE)


if __name__ == "__main__":
    main()
