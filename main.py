#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The joke is about
the demo itself: it works in rehearsal, then fails live in front of a
room — the punchline lands on the agent "fixing" a bug by deleting the
feature and calling it a refactor.
"""

import os

JOKE = (
    "I rehearsed the demo ten times. Live, my agent fixed the bug "
    "by deleting the feature and calling it a refactor."
)


def main() -> None:
    text = JOKE.strip()
    if not text or len(text) > 280:
        raise ValueError("joke must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
