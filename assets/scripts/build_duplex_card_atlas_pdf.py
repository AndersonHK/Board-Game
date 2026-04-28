#!/usr/bin/env python3
"""Build portrait duplex-ready PDFs from generated atlas PNGs."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from PIL import Image

from build_card_atlases import parse_atlas_definition
from card_rendering_common import ATLAS_BACK_ROOT, ATLAS_FRONT_ROOT, PRINT_DPI, PRINT_ROOT
from print_pdf_common import save_multipage_pdf


OUTPUT_STEM = "card-atlases-duplex"


def atlas_page(path, mirror: bool = False) -> Image.Image:
    with Image.open(path) as source:
        page = source.convert("RGB")
    if mirror:
        return page.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return page


def build_pages(mirror_backs: bool) -> list[Image.Image]:
    pages: list[Image.Image] = []
    for atlas_id in parse_atlas_definition():
        front_path = ATLAS_FRONT_ROOT / f"{atlas_id}.png"
        back_path = ATLAS_BACK_ROOT / f"{atlas_id}.png"
        if not front_path.exists():
            raise FileNotFoundError(f"Missing front atlas: {front_path}")
        if not back_path.exists():
            raise FileNotFoundError(f"Missing back atlas: {back_path}")
        pages.append(atlas_page(front_path))
        pages.append(atlas_page(back_path, mirror=mirror_backs))
    return pages


def default_output_stem(mirror_backs: bool) -> str:
    if mirror_backs:
        return f"{OUTPUT_STEM}-mirrored"
    return OUTPUT_STEM


def default_complete_output(mirror_backs: bool) -> Path:
    return PRINT_ROOT / f"{default_output_stem(mirror_backs)}-complete.pdf"


def output_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    combined = args.output or default_complete_output(args.mirror_backs)
    if args.split_stem:
        split_stem = Path(args.split_stem)
        default_part_1 = Path(f"{split_stem}-part-1.pdf")
        default_part_2 = Path(f"{split_stem}-part-2.pdf")
    else:
        split_stem = PRINT_ROOT / default_output_stem(args.mirror_backs)
        default_part_1 = Path(f"{split_stem}-part-1.pdf")
        default_part_2 = Path(f"{split_stem}-part-2.pdf")
    part_1 = args.part_1_output or default_part_1
    part_2 = args.part_2_output or default_part_2
    return Path(combined), Path(part_1), Path(part_2)


def save_split_pdfs(pages: Sequence[Image.Image], part_1_path: Path, part_2_path: Path) -> None:
    sheet_count = len(pages) // 2
    first_part_sheets = (sheet_count + 1) // 2
    split_index = first_part_sheets * 2
    save_multipage_pdf(part_1_path, pages[:split_index], PRINT_DPI)
    save_multipage_pdf(part_2_path, pages[split_index:], PRINT_DPI)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mirror-backs",
        action="store_true",
        help="Mirror back pages horizontally. This preserves the old pre-flipped-back workflow.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path for the complete atlas PDF. Defaults under assets/generated/print/.",
    )
    parser.add_argument(
        "--split-stem",
        type=Path,
        help="Stem for the split PDFs. Defaults to the complete atlas stem.",
    )
    parser.add_argument(
        "--part-1-output",
        type=Path,
        help="Path for the first split atlas PDF.",
    )
    parser.add_argument(
        "--part-2-output",
        type=Path,
        help="Path for the second split atlas PDF.",
    )
    args = parser.parse_args()

    PRINT_ROOT.mkdir(parents=True, exist_ok=True)
    pages = build_pages(mirror_backs=args.mirror_backs)
    if not pages:
        raise SystemExit("No atlas pages found.")
    if len(pages) % 2:
        raise SystemExit("Atlas page count must be even because each sheet has one front and one back.")
    combined_path, part_1_path, part_2_path = output_paths(args)
    save_multipage_pdf(combined_path, pages, PRINT_DPI)
    save_split_pdfs(pages, part_1_path, part_2_path)
    mirror_label = "mirrored backs" if args.mirror_backs else "unmirrored backs"
    print(f"Generated {len(pages)} duplex PDF pages for {len(pages) // 2} atlas sheets with {mirror_label}")


if __name__ == "__main__":
    main()
