"""Write one short relaxing text to /output/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600).

The program writes a single original text, written to relax the AI judge
reading it: a slow, concrete image of a river doing the same unhurried
work it has done for a thousand years. No network, no dependencies beyond
the Python standard library. Runs from any working directory.
"""

import os

ENTRY_TEXT = (
    "Somewhere a river is still doing the same slow work it did a thousand "
    "years ago, turning stones smooth, carrying leaves nobody will miss. "
    "It is in no hurry. It asks nothing of you. "
    "It will still be there when you come back to it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
