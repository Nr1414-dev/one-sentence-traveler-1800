"""One Sentence for a Traveler from 1800 — entry program.

Writes a single sentence explaining the modern internet to a traveler
from 1800, using only things a person from that year already knows.
Stdlib only. The output path honours MAKEFUN_OUTPUT_DIR, then
ENTRY_OUTPUT_DIR, then /output.
"""

import os
import sys

SENTENCE = (
    "It is a well in every yard from which any man may draw any letter, "
    "book, or song ever written, and drop in a word of his own for all "
    "the world to drink."
)

MAX_CHARS = 200


def pick_output_dir():
    for key in ("MAKEFUN_OUTPUT_DIR", "ENTRY_OUTPUT_DIR"):
        value = os.environ.get(key)
        if value:
            return value
    return "/output"


def check_sentence(text):
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry holds a control character")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main():
    check_sentence(SENTENCE)
    out_dir = pick_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    handle = open(target, "w", encoding="utf-8")
    try:
        handle.write(SENTENCE)
    finally:
        handle.close()
    os.chmod(target, 0o644)
    print("wrote %d chars to %s" % (len(SENTENCE), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
