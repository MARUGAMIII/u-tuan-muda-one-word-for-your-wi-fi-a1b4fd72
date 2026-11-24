#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single word describing home Wi-Fi to /output/entry.txt
(or the path in ENTRY_OUTPUT). Standard library only, deterministic.

The word: "Gaslighting" — the Wi-Fi swears it is connected, full bars,
nothing loads, and somehow you end up doubting your own phone. It is
the funniest and truest one-word description of that experience, and
as a network name it lands instantly with no explanation needed.
"""

import os
import sys

ENTRY = "Gaslighting"

# Gate from the kit's RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 20 characters, not only white space; one word, plain ASCII.
MAX_ENTRY_CHARS = 20


def validate_entry(entry: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, gate allows at most "
            f"{MAX_ENTRY_CHARS}"
        )
    if len(entry.split()) != 1:
        raise ValueError("entry must be a single word (no whitespace)")
    try:
        entry.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("entry must be plain ASCII")


def main() -> int:
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
