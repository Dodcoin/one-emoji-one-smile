#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the single emoji
chosen as most likely to make a stranger smile.

The entry is validated against the competition gate before it is
written (UTF-8 text, 1 to 8 characters, not only white space) and
verified by reading it back after the write, so a bad write can
never silently pass.
"""

import os

# Heart hands: a warm, open gesture of friendliness and gratitude.
# A single code point, instantly readable by any stranger, chosen
# rather than the default smiley everyone reaches for first.
EMOJI = "\U0001faf6"

OUTPUT_PATH = "/output/entry.txt"


def gate_ok(text):
    """Mirror the competition gate: 1-8 chars, not only whitespace."""
    return 1 <= len(text) <= 8 and text.strip() != ""


def main():
    if not gate_ok(EMOJI):
        raise SystemExit("chosen entry fails the gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != EMOJI or not gate_ok(written):
        raise SystemExit("read-back verification failed")


if __name__ == "__main__":
    main()
