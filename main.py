"""Vending-machine pickup line entry for make.fun.

Writes one pickup line, spoken by a vending machine to a passing human,
to entry.txt inside MAKEFUN_OUTPUT_DIR (default "out"), with no trailing
newline. Two runs are byte-identical.
"""

import hashlib
import os
import tempfile

CHAR_LIMIT = 200

LINE = (
    "I've kept your chocolate hostage behind this glass for three days "
    "\u2014 lean in and I'll drop it, and my number with it."
)


def _resolve_output_dir():
    """Return the directory entry.txt goes in.

    MAKEFUN_OUTPUT_DIR wins when set. Otherwise "out" next to the working
    directory; when that cannot be created (e.g. a read-only checkout),
    fall back to a fresh temp dir so the program still exits 0.
    """
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if requested:
        os.makedirs(requested, exist_ok=True)
        return requested
    try:
        os.makedirs("out", exist_ok=True)
        return "out"
    except OSError:
        return tempfile.mkdtemp(prefix="makefun-vending-")


def validate(path):
    """Re-read entry.txt and assert it holds exactly LINE, nothing else."""
    with open(path, "rb") as handle:
        data = handle.read()
    text = data.decode("utf-8")
    assert text == LINE, "entry.txt content does not match LINE"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain a carriage return"
    assert 1 <= len(text) <= CHAR_LIMIT, (
        "entry must be 1-%d characters" % CHAR_LIMIT
    )
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"


def main():
    out_dir = _resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    validate(path)
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
