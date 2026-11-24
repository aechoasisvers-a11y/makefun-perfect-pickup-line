"""The Perfect Pickup Line — make.fun entry (program/v1, pure stdlib).

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY_TEXT = (
    "I ran a million simulations of this moment, and in every one "
    "the best line was just: hi \u2014 can I buy you a coffee?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Self-check (pass 2): read back and verify the gate before finishing.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "output does not match intended entry text"
    assert 1 <= len(written) <= 200, "entry outside 1-200 char gate"
    assert written.strip(), "entry must not be only whitespace"
    assert not written.endswith("\n"), "no trailing newline"


if __name__ == "__main__":
    main()
