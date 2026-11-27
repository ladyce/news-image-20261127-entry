#!/usr/bin/env python3
"""news-image-20261127 entry: write the built front page to /output/entry.png.

The image sums up Friday 27 November 2026 in one newspaper page: 36 stories
(3 illustrated leads, 12 small stories, 21 briefs), a world map with numbered
pins, a UTC timeline and a date-check box. It was drawn in this session with
PIL: original flat vector drawings and original copy, no external images.

Runs on Python 3.13, standard library only. No network, no randomness: it
copies the PNG that ships beside this file, so two runs write identical bytes.
"""
import os
import shutil
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from the PNG IHDR chunk (bytes 16..24)."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("missing IHDR")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    repo = Path(__file__).resolve().parent
    src = repo / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    data = src.read_bytes()
    if data[:8] != PNG_MAGIC:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    try:
        width, height = png_dimensions(data)
    except ValueError as exc:
        print(f"entry.png: {exc}", file=sys.stderr)
        return 1
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"entry.png is {width}x{height}, over 1024x1024", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({len(data)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
