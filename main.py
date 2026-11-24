#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, at most 120 characters, as if a
houseplant had written it, to /output/entry.txt, where the house judge
reads it.

The line is a monstera answering email from its windowsill. It gives the
plant a voice with opinions — it is judging the sender's tone — and it
measures its reply time in the plant's own unit of time: waterings, not
business days. Three beats, no wasted words: the email arrived, the plant
is judging you, and it will get back to you in three to five waterings.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Your email reached the monstera. It's judging your tone from the "
    "windowsill. Reply time: three to five waterings."
)


def main() -> None:
    # Gate self-check before writing: 1-120 UTF-8 characters, not only
    # white space. The line is 113 characters: a monstera on the
    # windowsill, judging the sender's tone, answering in waterings.
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        raise SystemExit("line fails the 1-120 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
