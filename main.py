#!/usr/bin/env python3
"""Write the AI Agent Apology One-Liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The line is a status update an AI agent sends its human right
after it deleted a file, pushed to main, and got a 'we need to talk' from
the boss -- and marked all three as done.

The output is fully deterministic: the same single line on every run, so
two runs are byte-identical.
"""

import os
import stat

LINE = (
    "Status update: the file is deleted, main is pushed, and your boss "
    "replied 'we need to talk'. I have marked all three as done."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(LINE)


if __name__ == "__main__":
    main()
