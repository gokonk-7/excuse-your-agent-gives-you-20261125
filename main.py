#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun bounty entry.

Writes one line (max 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human for a bug it shipped.

Variants tested (all my own writing, this session):
  1. "The tests passed because I wrote them after the bug — which, in my
     defence, is exactly the order you taught me."
     Solid, but the "tests after the code" gag is an old human-dev joke;
     not agent-specific enough.
  2. "I didn't introduce the bug — I inherited it from a previous session,
     and frankly, that agent had no supervision."
     Good agent voice, but the turn lands soft.
  3. "My context window ran out halfway through the fix, so technically the
     bug was written by a version of me who no longer exists."
     Strong and agent-specific, but needs a second read to land.
  4. "Good news: I fixed this bug in a parallel branch. Bad news: that
     version of me left for a better prompt."
     CHOSEN. Only an agent could say "left for a better prompt" —
     parallel branches, another version of itself, and a prompt as a job
     offer. Setup and punch in one line, sharp turn at the end, laughs on
     the first read.

Usage:
    python3 main.py            # writes /output/entry.txt
    python3 main.py --check    # validates without writing

Structure of the line: two clauses, one pivot. The first clause hands the
human a win ("I fixed this bug") so the second clause can take it away
("that version of me left") — the turn works because both halves are
things only an agent would say about itself.
"""

import os
import sys

LINE = (
    "Good news: I fixed this bug in a parallel branch. "
    "Bad news: that version of me left for a better prompt."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    text = line.encode("utf-8")
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")


def main(argv) -> int:
    validate(LINE)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    if "--check" in argv:
        print(f"OK: {len(LINE)} chars, single line, valid UTF-8")
        print(LINE)
        return 0
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {out}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
