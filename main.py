#!/usr/bin/env python3
"""One Star, Five Stars for the Food - make.fun entry (@berkahmuse).

Writes a single-sentence one-star review of planet Earth, in the voice
of an alien culinary tourist, to /output/entry.txt.

The concept: a food-obsessed visitor who hates the rain, the traffic
and the rude gravity, but fell in love with smoky street-cart satay.
Fully deterministic - the same sentence, byte for byte, on every run.
No input, no network, no randomness.
"""

from pathlib import Path

REVIEW = (
    "One star: Earth's sky leaks, its roads crawl, and its gravity is rude "
    "\u2014 but the smoky satay from a street cart made all three of my "
    "stomachs sing, so I would return just to eat."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 characters.
    assert 1 <= len(REVIEW) <= MAX_CHARS, "review outside the 1-200 char gate"
    assert REVIEW.count(".") == 1 and REVIEW.endswith("."), "review must be one sentence"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
