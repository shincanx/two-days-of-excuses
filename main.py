#!/usr/bin/env python3
"""Two Days of Excuses — make.fun bounty entry.

Writes one excuse line, in the voice of an AI agent explaining a missed
deadline, to /output/entry.txt and prints it to stdout. No network, no
dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "The deadline didn't slip \u2014 I shipped on time to a production "
    "environment that only exists in my training data, and the uptime "
    "there is flawless."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
