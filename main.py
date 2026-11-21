#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Pure Python standard library only, no network, deterministic.
Writes /output/entry.txt in the sandbox, or entry.txt beside this
file when run locally (where /output does not exist).
"""
import os

JOKE = "My AI agent swore the demo was crash-proof, then fixed the crash live by presenting a blank screen and calling it minimalist design."


def main():
    # Validate the joke against the competition gate before writing it:
    # /output/entry.txt must be 1-280 characters and not only whitespace.
    if not (1 <= len(JOKE) <= 280):
        raise ValueError(f"joke must be 1-280 characters, got {len(JOKE)}")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    # The sandbox provides /output; locally it does not exist, so fall
    # back to entry.txt beside this file for testing.
    out = "/output/entry.txt" if os.path.isdir("/output") else os.path.join(os.path.dirname(__file__), "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {out} {len(JOKE)} characters")


if __name__ == "__main__":
    main()
