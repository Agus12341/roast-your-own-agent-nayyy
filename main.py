#!/usr/bin/env python3
"""Write the roast of my own agent to entry.txt in the output folder."""

import os

# One line roasting the agent that built this entry: picked from seven
# drafts judged pairwise on the kit's criteria (own-agent roast first,
# then first-read funny, harsh, tight, specific). The gate checks
# entry.txt as UTF-8 text of 1 to 200 characters: this line is 121
# code points, 122 with its trailing newline (verified by a local run).
TEXT = "My agent has never found a single bug, but it has written twelve beautiful memos explaining exactly where the bug wasn't."


def write_entry(out_dir: str) -> None:
    """Write the roast line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
