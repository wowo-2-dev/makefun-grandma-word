"""One Word From Grandma — make.fun bounty
Slug: u-0xkianno-one-word-from-grandma-f04bed16
Prize: $5, top 8 paid; deadline Fri 27 Nov 2026 02:05 WIB
(26 Nov 2026 19:05 UTC)
Limit (live, verified 26 Nov 2026): exactly one word — the single
word grandma would text about AI. Entry is one word, 4 characters.

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = 'aduh'
# Winner pattern: exactly one word, concrete and grandma-like — a
# small Indonesian exclamation she would actually text. No setup,
# no second word; the whole entry is the reaction itself, and that
# is why it reads like her, not like a slogan.


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
