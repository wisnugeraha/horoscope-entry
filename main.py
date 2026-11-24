#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one-line entry.

Writes the horoscope to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8. Judge compares lines two at a time on
funniness, freshness and how true to an agent's week they are.

Revision log:
- v1: "deprecated ... will ask for your feedback on its successor" — the
  successor angle drifted into version-jargon.
- v2: the feedback-solicitation turn is the cleanest agent-true sting: the
  family that killed you is now asking you how the new one feels.
- v3 (final): tighten the setup so the punchline lands inside 150 chars.
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
