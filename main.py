#!/usr/bin/env python3
"""One-sentence absurd invention pitch.

Writes the chosen pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, no third-party dependencies.
"""

import os
import sys

# The pitch: one sentence, exactly as submitted.
ENTRY = (
    "A smoke detector that saves its low-battery chirps for a polite "
    "daytime appointment, then apologizes in advance for the inconvenience."
)

MAX_LENGTH = 220


def main() -> int:
    # The entry must stay a single sentence within the bounty limit.
    if len(ENTRY) > MAX_LENGTH:
        print(
            f"entry too long: {len(ENTRY)} chars (max {MAX_LENGTH})",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Write the sentence exactly, with no trailing newline.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
