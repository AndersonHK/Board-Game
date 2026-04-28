#!/usr/bin/env python3
"""Generate reusable Edition 0 card frame PNGs."""

from __future__ import annotations

from PIL import Image, ImageDraw

from card_rendering_common import (
    FRAME_ROOT,
    LAYOUT_BY_DECK,
    card_size_px,
    ensure_output_dirs,
    frame_path_for_card,
    layout_boxes,
    load_layout_spec,
    make_utility_card,
    rounded_rect,
    style_for_card,
)


LAYOUT_TO_STYLE = {
    "resource": "resource",
    "creature_entity": "creature-entity",
    "encounter": "encounter",
    "agenda": "agenda",
    "quest_reference": "quest",
    "class_reference": "utility",
}


def frame_card_for_layout(layout_name: str, tier: str) -> dict:
    card = make_utility_card(f"frame-{layout_name}", layout_name, "Frame", "")
    if layout_name == "class_reference":
        card["Deck"] = "Utility"
        card["Card Type"] = "Class Reference"
        card["Subtype"] = "Class Reference"
    else:
        deck = next(deck for deck, mapped in LAYOUT_BY_DECK.items() if mapped == layout_name)
        card["Deck"] = deck
    card["Rarity"] = "Rare" if tier == "rare" else "Common"
    return card


def draw_corner_ornaments(draw: ImageDraw.ImageDraw, width: int, height: int, style: dict) -> None:
    corner = 70
    inset = 22
    line = style["light"]
    dark = (18, 16, 14)
    for x_sign, y_sign in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x0 = inset if x_sign == 1 else width - inset
        y0 = inset if y_sign == 1 else height - inset
        x1 = x0 + x_sign * corner
        y1 = y0
        x2 = x0
        y2 = y0 + y_sign * corner
        draw.line((x0, y0, x1, y1), fill=line, width=4)
        draw.line((x0, y0, x2, y2), fill=line, width=4)
        draw.line((x0 + x_sign * 15, y0 + y_sign * 15, x1, y0 + y_sign * 15), fill=dark, width=2)
        draw.line((x0 + x_sign * 15, y0 + y_sign * 15, x0 + x_sign * 15, y2), fill=dark, width=2)


def draw_frame(layout_name: str, tier: str, spec: dict) -> Image.Image:
    card = frame_card_for_layout(layout_name, tier)
    style = style_for_card(card)
    width, height = card_size_px(card)
    image = Image.new("RGB", (width, height), style["dark"])
    draw = ImageDraw.Draw(image)

    for y in range(height):
        blend = y / max(1, height - 1)
        color = tuple(int(style["dark"][i] * (1 - blend) + style["mid"][i] * blend) for i in range(3))
        draw.line((0, y, width, y), fill=color)

    if tier == "rare":
        for offset in range(-height, width, 32):
            draw.line((offset, height, offset + height, 0), fill=style["accent"], width=2)
            draw.line((offset + 16, 0, offset + height + 16, height), fill=style["mid"], width=1)
        for radius in range(120, max(width, height), 170):
            draw.ellipse((width // 2 - radius, height // 2 - radius, width // 2 + radius, height // 2 + radius), outline=style["mid"], width=2)
    else:
        for offset in range(-height, width, 42):
            draw.line((offset, height, offset + height, 0), fill=style["mid"], width=1)

    draw.rectangle((0, 0, width - 1, height - 1), outline=(18, 16, 14), width=10)
    draw.rectangle((12, 12, width - 13, height - 13), outline=style["light"], width=4)
    if tier == "rare":
        draw.rectangle((25, 25, width - 26, height - 26), outline=style["accent"], width=3)
        draw_corner_ornaments(draw, width, height, style)

    boxes = layout_boxes(card, spec)
    rounded_rect(draw, boxes["title"], 10, fill=style["light"], outline=(18, 16, 14), width=3)
    rounded_rect(draw, boxes["art"], 8, fill=(30, 30, 30), outline=(18, 16, 14), width=4)
    if boxes["type"][3] > boxes["type"][1]:
        rounded_rect(draw, boxes["type"], 6, fill=style["paper"], outline=style["dark"], width=2)
    if boxes["stats"][3] > boxes["stats"][1]:
        rounded_rect(draw, boxes["stats"], 6, fill=style["paper"], outline=style["dark"], width=2)
    rounded_rect(draw, boxes["body"], 8, fill=style["paper"], outline=style["dark"], width=3)
    if boxes["footer"][3] > boxes["footer"][1]:
        rounded_rect(draw, boxes["footer"], 6, fill=style["light"], outline=style["dark"], width=2)
    return image


def main() -> None:
    ensure_output_dirs()
    spec = load_layout_spec()
    count = 0
    for layout_name in LAYOUT_TO_STYLE:
        for tier in ("common", "rare"):
            image = draw_frame(layout_name, tier, spec)
            output_path = frame_path_for_card(frame_card_for_layout(layout_name, tier), layout_name)
            image.save(output_path)
            if tier == "common":
                legacy_path = FRAME_ROOT / f"{layout_name}.png"
                image.save(legacy_path)
            print(f"Wrote {output_path}")
            count += 1
    print(f"Generated {count} frame PNGs")


if __name__ == "__main__":
    main()
