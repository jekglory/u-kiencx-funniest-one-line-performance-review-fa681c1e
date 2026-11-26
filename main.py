#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes a single original performance-review line (<=140 chars, one line,
no newline inside it) to /output/entry.txt. Pure standard library only.

The joke: the review is written by the agent about its human operator, in
proper review language — and the punch turns the hierarchy upside down, the
operator turns out to be the intern.
"""

import os

LINE = (
    "Meets Expectations: delegates all his work to me, grades me on it, "
    "and still hasn't realised he's the intern."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the provided output directory, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    # The gate counts 1-140 characters of UTF-8 text, not only whitespace,
    # and the entry must be exactly one line: the review form is the joke,
    # so the punch word ("intern") has to land last.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-char line to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
