"""Write a one-line joke about working beside an AI coding agent.

The joke is written to entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
No input is read, no network is used, and the output is deterministic.
"""

import os

DEFAULT_OUTPUT_DIR = "/output"

JOKE = (
    "My agent blamed the demo crash on a library that doesn't exist "
    "— then imported it, and the demo worked."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
