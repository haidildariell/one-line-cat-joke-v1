"""One-line cat joke entry for make.fun.

Writes a single cat joke, exactly one line, to entry.txt inside the
output directory (OUTPUT_DIR env var, default /output).
"""

import os

LINE = "I told my cat she's adopted; she blinked slowly, which in cat is the middle finger."


def get_line():
    """Return the joke line, validated: non-empty, one line, <= 200 chars."""
    if not LINE:
        raise ValueError("joke line is empty")
    if "\n" in LINE:
        raise ValueError("joke line must be a single line")
    if len(LINE) > 200:
        raise ValueError("joke line exceeds 200 characters")
    return LINE


def write_entry(line, out_dir):
    """Write the given line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(get_line(), out_dir)


if __name__ == "__main__":
    main()
