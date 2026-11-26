"""Entry for make.fun bounty u-mang-the-printer-finally-answers-8fbf0907.

Writes the printer's comeback line to entry.txt in MAKEFUN_OUTPUT_DIR.
Gate: UTF-8 text, 1-240 characters, one line, not only whitespace.
"""

import os

ENTRY = (
    "Sheet 9,412 jammed because your agent printed its own approval "
    "form 14 times and never approved a single copy, so the jam is on you."
)


def main() -> None:
    # Gate assertion: 1-240 chars, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
