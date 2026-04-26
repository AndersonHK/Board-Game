#!/usr/bin/env python3
"""Build a portrait long-edge duplex-ready PDF from generated atlas PNGs."""

from __future__ import annotations

from PIL import Image

from build_card_atlases import parse_atlas_definition
from card_rendering_common import ATLAS_BACK_ROOT, ATLAS_FRONT_ROOT, PRINT_DPI, PRINT_ROOT


OUTPUT_PATH = PRINT_ROOT / "card-atlases-duplex.pdf"


def atlas_page(path, mirror: bool = False) -> Image.Image:
    with Image.open(path) as source:
        page = source.convert("RGB")
    if mirror:
        return page.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return page


def main() -> None:
    PRINT_ROOT.mkdir(parents=True, exist_ok=True)
    pages: list[Image.Image] = []
    for atlas_id in parse_atlas_definition():
        front_path = ATLAS_FRONT_ROOT / f"{atlas_id}.png"
        back_path = ATLAS_BACK_ROOT / f"{atlas_id}.png"
        if not front_path.exists():
            raise FileNotFoundError(f"Missing front atlas: {front_path}")
        if not back_path.exists():
            raise FileNotFoundError(f"Missing back atlas: {back_path}")
        pages.append(atlas_page(front_path))
        pages.append(atlas_page(back_path, mirror=True))
    if not pages:
        raise SystemExit("No atlas pages found.")
    first, rest = pages[0], pages[1:]
    first.save(OUTPUT_PATH, save_all=True, append_images=rest, resolution=PRINT_DPI)
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Generated {len(pages)} duplex PDF pages for {len(pages) // 2} atlas sheets")


if __name__ == "__main__":
    main()
