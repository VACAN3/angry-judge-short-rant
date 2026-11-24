#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (overridable with OUTPUT_PATH for local runs).
"""

import os

RANT = (
    "My office microwave has one job \u2014 heat my lunch \u2014 yet every day "
    "it serves a frozen center, a lava-hot rim, and three smug beeps, like "
    "a chef who burned the dish and still expects a tip."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(RANT)
    print(f"Wrote {len(RANT)} characters to {out_path}")


if __name__ == "__main__":
    main()
