#!/usr/bin/env python3
"""Check final card art for duplicate or suspiciously similar images."""

from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageOps

from card_rendering_common import CARD_ART_FINAL_ROOT


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def bits_to_int(bits: list[bool]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return value


def difference_hash(path: Path) -> int:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("L").resize((17, 16), Image.Resampling.LANCZOS)
    pixels = list(image.getdata())
    bits: list[bool] = []
    for y in range(16):
        row = pixels[y * 17 : (y + 1) * 17]
        for x in range(16):
            bits.append(row[x] > row[x + 1])
    return bits_to_int(bits)


def average_hash(path: Path) -> int:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image).convert("L").resize((16, 16), Image.Resampling.LANCZOS)
    pixels = list(image.getdata())
    average = sum(pixels) / len(pixels)
    return bits_to_int([pixel > average for pixel in pixels])


def hamming(left: int, right: int) -> int:
    return bin(left ^ right).count("1")


def relative(path: Path) -> str:
    return path.as_posix()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=CARD_ART_FINAL_ROOT, help="Final art root to scan.")
    parser.add_argument("--dhash-threshold", type=int, default=12, help="Near-duplicate dHash threshold.")
    parser.add_argument("--ahash-threshold", type=int, default=18, help="Near-duplicate aHash threshold.")
    args = parser.parse_args()

    root = args.root
    files = sorted(root.rglob("*.png"))
    print(f"# Card Art Integrity Report\n")
    print(f"- Final PNGs scanned: `{len(files)}`")
    print(f"- Root: `{relative(root)}`")

    hashes: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        hashes[sha256(path)].append(path)
    duplicate_groups = [group for group in hashes.values() if len(group) > 1]

    if duplicate_groups:
        print("\n## Exact Duplicates\n")
        for group in duplicate_groups:
            print("- Duplicate SHA-256:")
            for path in group:
                print(f"  - `{relative(path)}`")
    else:
        print("\n## Exact Duplicates\n\nNone.")

    perceptual_rows = [(path, difference_hash(path), average_hash(path)) for path in files]
    near_duplicates: list[tuple[int, int, Path, Path]] = []
    for index, (left_path, left_dhash, left_ahash) in enumerate(perceptual_rows):
        for right_path, right_dhash, right_ahash in perceptual_rows[index + 1 :]:
            dhash_distance = hamming(left_dhash, right_dhash)
            ahash_distance = hamming(left_ahash, right_ahash)
            if dhash_distance <= args.dhash_threshold and ahash_distance <= args.ahash_threshold:
                near_duplicates.append((dhash_distance, ahash_distance, left_path, right_path))

    if near_duplicates:
        print("\n## Near-Duplicate Candidates\n")
        for dhash_distance, ahash_distance, left_path, right_path in sorted(near_duplicates):
            print(
                f"- dHash `{dhash_distance}`, aHash `{ahash_distance}`: "
                f"`{relative(left_path)}` / `{relative(right_path)}`"
            )
    else:
        print("\n## Near-Duplicate Candidates\n\nNone.")

    return 1 if duplicate_groups or near_duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
