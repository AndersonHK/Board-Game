#!/usr/bin/env python3
"""Build printable card atlas PNGs from generated card fronts and backs."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw

from card_rendering_common import (
    ATLAS_BACK_ROOT,
    ATLAS_FRONT_ROOT,
    BACK_ROOT,
    ATLAS_PATH,
    CARD_HEIGHT_PX,
    CARD_WIDTH_PX,
    SHEET_HEIGHT_PX,
    SHEET_WIDTH_PX,
    card_front_path,
    ensure_output_dirs,
    extract_class_reference_cards,
    load_cards,
    make_utility_card,
)
from generate_card_backs import BACKS, draw_back


ASHEN_DEPTHS_UNIQUE_CREATURES = {
    "Ashen Warden",
    "Kiln Pup",
    "Chainbound Head",
    "Heartfire Dragon",
}

ASHEN_DEPTHS_ENCOUNTERS = {
    "Dragon in the Deep",
    "Furnace Warden Rises",
}


@dataclass
class AtlasPlacement:
    atlas_id: str
    slots: list[int]
    name: str


def utility_cards() -> list[dict]:
    return [
        make_utility_card("proxy-blank", "Blank Proxy", "Proxy", "Write a temporary card name here when needed."),
        make_utility_card("proxy-encounter-divider", "Encounter Proxy / Divider", "Divider", "Spare encounter proxy or divider."),
        make_utility_card("proxy-creature-blank", "Creature Proxy Blank", "Proxy", "Spare creature/entity proxy."),
    ]


def slot_range(value: str) -> list[int]:
    value = value.strip("` ")
    if "-" in value:
        start, end = value.split("-", 1)
        return list(range(int(start), int(end) + 1))
    return [int(value)]


def slot_group(value: str) -> list[int]:
    slots: list[int] = []
    for chunk in value.split(","):
        slots.extend(slot_range(chunk))
    return slots


def parse_atlas_definition() -> dict[str, list[AtlasPlacement]]:
    atlases: dict[str, list[AtlasPlacement]] = {}
    current_atlas: str | None = None
    for raw_line in ATLAS_PATH.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^###\s+(ATLAS-[A-Z]+-\d+)", raw_line)
        if heading:
            current_atlas = heading.group(1)
            atlases[current_atlas] = []
            continue
        if not current_atlas or not raw_line.startswith("|"):
            continue
        cells = [cell.strip() for cell in raw_line.strip().strip("|").split("|")]
        if len(cells) < 2 or "Slot" in cells[0] or "---" in cells[0]:
            continue
        slots = slot_group(cells[0])
        name = cells[1].strip()
        copies = None
        if len(cells) >= 3:
            copy_match = re.search(r"`?(\d+)`?", cells[2])
            if copy_match:
                copies = int(copy_match.group(1))
        if copies and copies == len(slots):
            for slot in slots:
                atlases[current_atlas].append(AtlasPlacement(current_atlas, [slot], name))
        else:
            atlases[current_atlas].append(AtlasPlacement(current_atlas, slots, name))
    return atlases


def atlas_deck_hint(atlas_id: str, card_name: str) -> str | None:
    if atlas_id.startswith("ATLAS-RES"):
        return "Resource Deck"
    if atlas_id.startswith("ATLAS-CRE"):
        return "Creature Deck"
    if atlas_id.startswith("ATLAS-ENC"):
        return "Encounter Deck"
    if card_name == "Ashen Depths":
        return "Quest Deck"
    if card_name.endswith("Reference"):
        return "Utility"
    return "Agenda Deck"


def normalize_card_name(name: str) -> str:
    name = re.sub(r",\s*two-slot quest card$", "", name).strip()
    name = re.sub(r",\s*four-slot quest card$", "", name).strip()
    if name.lower() == "blank proxy":
        return "Blank Proxy"
    if name.lower() == "encounter proxy / divider":
        return "Encounter Proxy / Divider"
    if name.lower() == "creature proxy blanks":
        return "Creature Proxy Blank"
    if name.lower() in {"warrior reference", "wizard reference", "cleric reference"}:
        return name.title()
    return name


def source_cards() -> list[dict]:
    return load_cards() + extract_class_reference_cards() + utility_cards()


def build_card_index() -> dict[tuple[str, str], dict]:
    return {
        (card.get("Display Name", ""), card.get("Deck", "")): card
        for card in source_cards()
    }


def build_front_index(cards: dict[tuple[str, str], dict]) -> dict[tuple[str, str], Path]:
    return {
        key: card_front_path(card)
        for key, card in cards.items()
    }


def ensure_back_textures() -> None:
    BACK_ROOT.mkdir(parents=True, exist_ok=True)
    for style_key, label in BACKS.items():
        output_path = BACK_ROOT / f"{style_key}.png"
        if not output_path.exists():
            draw_back(style_key, label).save(output_path)


def back_key_for_card(card: dict) -> str:
    deck = card.get("Deck", "")
    if card.get("Display Name", "") in ASHEN_DEPTHS_UNIQUE_CREATURES:
        return "ashen-depths-creature"
    if deck == "Resource Deck":
        return "resource"
    if deck == "Creature Deck":
        return "creature-entity"
    if deck == "Encounter Deck" and card.get("Display Name", "") in ASHEN_DEPTHS_ENCOUNTERS:
        return "ashen-depths-encounter"
    if deck == "Encounter Deck":
        return "encounter"
    if deck == "Agenda Deck":
        return "agenda"
    if deck == "Quest Deck":
        return "ashen-depths-quest"
    if deck == "Utility" and card.get("Card Type") == "Class Reference":
        return "fantasy-pack"
    return "shared"


def slot_box(slot: int) -> tuple[int, int, int, int]:
    index = slot - 1
    row = index // 4
    col = index % 4
    left = col * CARD_WIDTH_PX
    top = row * CARD_HEIGHT_PX
    return left, top, left + CARD_WIDTH_PX, top + CARD_HEIGHT_PX


def placement_box(placement: AtlasPlacement) -> tuple[int, int, int, int]:
    rows = [(slot - 1) // 4 for slot in placement.slots]
    cols = [(slot - 1) % 4 for slot in placement.slots]
    left = min(cols) * CARD_WIDTH_PX
    top = min(rows) * CARD_HEIGHT_PX
    right = (max(cols) + 1) * CARD_WIDTH_PX
    bottom = (max(rows) + 1) * CARD_HEIGHT_PX
    return left, top, right, bottom


def resolve_front_path(index: dict[tuple[str, str], Path], atlas_id: str, raw_name: str) -> Path:
    name = normalize_card_name(raw_name)
    hint = atlas_deck_hint(atlas_id, name)
    candidates = []
    if hint:
        candidates.append((name, hint))
    candidates.extend(key for key in index if key[0] == name)
    for key in candidates:
        path = index.get(key)
        if path and path.exists():
            return path
    raise FileNotFoundError(f"Could not resolve generated card front for {raw_name!r} in {atlas_id}")


def resolve_card(index: dict[tuple[str, str], dict], atlas_id: str, raw_name: str) -> dict:
    name = normalize_card_name(raw_name)
    hint = atlas_deck_hint(atlas_id, name)
    candidates = []
    if hint:
        candidates.append((name, hint))
    candidates.extend(key for key in index if key[0] == name)
    for key in candidates:
        card = index.get(key)
        if card:
            return card
    raise FileNotFoundError(f"Could not resolve card definition for {raw_name!r} in {atlas_id}")


def placement_blocks_vertical_line(placement: AtlasPlacement, line_col: int) -> tuple[int, int] | None:
    slot_set = set(placement.slots)
    blocks = []
    for row in range(3):
        left_slot = row * 4 + line_col
        right_slot = left_slot + 1
        if left_slot in slot_set and right_slot in slot_set:
            blocks.append((row * CARD_HEIGHT_PX, (row + 1) * CARD_HEIGHT_PX))
    if blocks:
        return min(start for start, _ in blocks), max(end for _, end in blocks)
    return None


def placement_blocks_horizontal_line(placement: AtlasPlacement, line_row: int) -> tuple[int, int] | None:
    slot_set = set(placement.slots)
    blocks = []
    for col in range(4):
        top_slot = (line_row - 1) * 4 + col + 1
        bottom_slot = top_slot + 4
        if top_slot in slot_set and bottom_slot in slot_set:
            blocks.append((col * CARD_WIDTH_PX, (col + 1) * CARD_WIDTH_PX))
    if blocks:
        return min(start for start, _ in blocks), max(end for _, end in blocks)
    return None


def draw_segmented_vertical_line(
    draw: ImageDraw.ImageDraw,
    x: int,
    blocked: list[tuple[int, int]],
    color: tuple[int, int, int],
) -> None:
    y = 0
    for start, end in sorted(blocked):
        if y < start:
            draw.line((x, y, x, start), fill=color, width=2)
        y = max(y, end)
    if y < SHEET_HEIGHT_PX:
        draw.line((x, y, x, SHEET_HEIGHT_PX), fill=color, width=2)


def draw_segmented_horizontal_line(
    draw: ImageDraw.ImageDraw,
    y: int,
    blocked: list[tuple[int, int]],
    color: tuple[int, int, int],
) -> None:
    x = 0
    for start, end in sorted(blocked):
        if x < start:
            draw.line((x, y, start, y), fill=color, width=2)
        x = max(x, end)
    if x < SHEET_WIDTH_PX:
        draw.line((x, y, SHEET_WIDTH_PX, y), fill=color, width=2)


def draw_cut_grid(draw: ImageDraw.ImageDraw, placements: list[AtlasPlacement]) -> None:
    grid_color = (45, 45, 45)
    for col in range(1, 4):
        x = col * CARD_WIDTH_PX
        blocked = [
            block
            for placement in placements
            if (block := placement_blocks_vertical_line(placement, col)) is not None
        ]
        draw_segmented_vertical_line(draw, x, blocked, grid_color)
    for row in range(1, 3):
        y = row * CARD_HEIGHT_PX
        blocked = [
            block
            for placement in placements
            if (block := placement_blocks_horizontal_line(placement, row)) is not None
        ]
        draw_segmented_horizontal_line(draw, y, blocked, grid_color)
    draw.rectangle((0, 0, SHEET_WIDTH_PX - 1, SHEET_HEIGHT_PX - 1), outline=grid_color, width=2)


def build_front_atlas(atlas_id: str, placements: list[AtlasPlacement], index: dict[tuple[str, str], Path], draw_grid: bool) -> Path:
    sheet = Image.new("RGB", (SHEET_WIDTH_PX, SHEET_HEIGHT_PX), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    for placement in placements:
        front_path = resolve_front_path(index, atlas_id, placement.name)
        with Image.open(front_path) as source:
            card = source.convert("RGB")
            left, top, right, bottom = placement_box(placement)
            target_size = (right - left, bottom - top)
            if card.size != target_size:
                card = card.resize(target_size, Image.Resampling.LANCZOS)
            sheet.paste(card, (left, top))
    if draw_grid:
        draw_cut_grid(draw, placements)
    output_path = ATLAS_FRONT_ROOT / f"{atlas_id}.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
    return output_path


def build_back_atlas(atlas_id: str, placements: list[AtlasPlacement], index: dict[tuple[str, str], dict], draw_grid: bool) -> Path:
    sheet = Image.new("RGB", (SHEET_WIDTH_PX, SHEET_HEIGHT_PX), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    for placement in placements:
        card = resolve_card(index, atlas_id, placement.name)
        back_key = back_key_for_card(card)
        left, top, right, bottom = placement_box(placement)
        target_size = (right - left, bottom - top)
        card_back = draw_back(back_key, BACKS[back_key], target_size)
        sheet.paste(card_back, (left, top))
    if draw_grid:
        draw_cut_grid(draw, placements)
    output_path = ATLAS_BACK_ROOT / f"{atlas_id}.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-cut-grid", action="store_true", help="Do not draw slot cut lines on atlas PNGs.")
    args = parser.parse_args()

    ensure_output_dirs()
    ensure_back_textures()
    card_index = build_card_index()
    front_index = build_front_index(card_index)
    atlases = parse_atlas_definition()
    count = 0
    for atlas_id, placements in atlases.items():
        front_path = build_front_atlas(atlas_id, placements, front_index, draw_grid=not args.no_cut_grid)
        back_path = build_back_atlas(atlas_id, placements, card_index, draw_grid=not args.no_cut_grid)
        print(f"Wrote {front_path}")
        print(f"Wrote {back_path}")
        count += 1
    print(f"Generated {count} front atlas PNGs in {ATLAS_FRONT_ROOT}")
    print(f"Generated {count} back atlas PNGs in {ATLAS_BACK_ROOT}")


if __name__ == "__main__":
    main()
