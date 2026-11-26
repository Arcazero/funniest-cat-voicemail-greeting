#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt.
The greeting is at most 120 characters, plain UTF-8 text.
"""

import os

GREETING = (
    "Hi, it's Mittens. I'm asleep on your laptop. "
    "Leave a message after the beep \u2014 "
    "I'll hear it at 4 a.m. and ignore it."
)


def main() -> None:
    text = GREETING.strip()
    assert 1 <= len(text) <= 120, f"greeting is {len(text)} chars, must be 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
