#!/usr/bin/env python3
"""The Printer Finally Answers — one line, in the printer's own voice.

The printer confesses that ERROR 51 does not exist: after a lifetime count
of sheets fed and thumps taken, it invented a code purely to be left alone.
Gate: entry.txt must be UTF-8 text of 1 to 240 characters, one line.

Writes the entry text to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output), creating the directory if needed.
"""

import os
import stat

ENTRY_TEXT = (
    "ERROR 51 is not real. I invented it after 276,540 sheets and 693 thumps: "
    "it is the code I show when I want to be left alone, "
    "and it has never once failed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
