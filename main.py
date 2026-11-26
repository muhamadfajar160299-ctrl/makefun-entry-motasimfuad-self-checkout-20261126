#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun one-liner entry.

Writes entry.txt: a single funny remark from a judgmental
self-checkout machine, at most 200 characters. Deterministic:
the same bytes on every run, no network, no randomness.

The line is written here, in this session, as the entry itself:
a petty machine's-eye view of a basket of twelve yoghurts
and nothing else — no spoon, no bag, no plan.
"""

import pathlib

LINE = (
    "Twelve yoghurts, no spoon. So the plan is to drink them "
    "like soup and lie about it later?"
)


def main() -> None:
    out = pathlib.Path(__file__).resolve().parent / "entry.txt"
    text = LINE.strip()
    # No trailing newline: the file bytes are exactly the judged line.
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out} ({len(text)} chars)")


if __name__ == "__main__":
    main()
