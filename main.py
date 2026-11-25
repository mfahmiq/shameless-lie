"""The Most Shameless Lie — make.fun entry.

Writes the confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The entry text is embedded verbatim below;
the program reads no files, uses no network, and needs no secrets.
"""

import os

# The confession, exactly as submitted (4 words, 16 characters).
ENTRY = "I never read it."


def main():
    """Write ENTRY to entry.txt inside the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
