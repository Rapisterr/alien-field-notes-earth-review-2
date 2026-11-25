"""Alien Field Notes: The Two Day Earth Review (entry 2).

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to entry.txt in the output directory.

The line defamiliarises a mundane human ritual: the greeting "How are
you?", which locals ask without wanting an honest answer. The alien
reads it as a social rule of the planet and rates the stay like a hotel
review: 4/5, emotionally avoidant hosts, would visit again.

Stdlib only. No third-party imports, no rendering, no network.
"""

import os

LINE = (
    "The locals ask 'How are you?' then panic when you answer honestly. "
    "4/5 \u2014 excellent planet, emotionally avoidant hosts, would visit again."
)

MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            "line is %d chars, over the %d-char limit" % (len(LINE), MAX_CHARS)
        )
    if "\n" in LINE:
        raise ValueError("line must be a single line of plain text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %s (%d chars)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
