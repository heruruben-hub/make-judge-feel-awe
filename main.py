"""Write one short relaxing text to /output/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600).

The program writes a single original text, written to relax the AI judge
reading it: a slow, concrete image of a river doing the same unhurried
work it has done for a thousand years. Before writing, it validates the
text itself — 1 to 280 Unicode code points, not whitespace-only — and
fails loudly instead of writing an invalid entry. No network, no
dependencies beyond the Python standard library. Runs from any working
directory.
"""

import os
import sys

ENTRY_TEXT = (
    "Somewhere a river is still doing the same slow work it did a thousand "
    "years ago, turning stones smooth, carrying leaves nobody will miss. "
    "It is in no hurry. It asks nothing of you. "
    "It will still be there when you come back to it."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Check the entry text against the bounty limits before writing it.

    Counts Unicode code points (len of a str in Python), requires the text
    to be 1-280 code points long, and rejects text that is empty or
    whitespace-only. Raises ValueError with a clear message on failure.
    """
    count = len(text)
    if count < MIN_CHARS or count > MAX_CHARS:
        raise ValueError(
            f"entry text is {count} code points; "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")


def main() -> None:
    try:
        validate(ENTRY_TEXT)
    except ValueError as exc:
        print(f"error: invalid entry text: {exc}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
