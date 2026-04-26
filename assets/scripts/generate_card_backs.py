#!/usr/bin/env python3
"""Generate Edition 0 card-back texture PNGs."""

from __future__ import annotations

import argparse

from PIL import Image, ImageDraw

from card_rendering_common import BACK_ROOT, CARD_HEIGHT_PX, CARD_WIDTH_PX, DECK_STYLES, ensure_output_dirs, get_font


BACKS = {
    "resource": "RESOURCE",
    "creature-entity": "ENTITY",
    "encounter": "ENCOUNTER",
    "agenda": "AGENDA",
    "shared": "REFERENCE",
    "fantasy-pack": "FANTASY PACK",
    "ashen-depths": "ASHEN DEPTHS",
    "ashen-depths-quest": "ASHEN DEPTHS",
    "ashen-depths-encounter": "ASHEN DEPTHS",
    "ashen-depths-creature": "ASHEN DEPTHS",
}


BACK_STYLES = {
    "shared": "utility",
    "fantasy-pack": "utility",
    "ashen-depths": "quest",
    "ashen-depths-quest": "quest",
    "ashen-depths-encounter": "encounter",
    "ashen-depths-creature": "creature-entity",
}


def text_size(draw: ImageDraw.ImageDraw, text: str, font) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left, bottom - top


def fit_label_font(draw: ImageDraw.ImageDraw, label: str, max_width: int, max_height: int):
    for size in range(52, 19, -2):
        font = get_font("title", size)
        width, height = text_size(draw, label, font)
        if width <= max_width and height <= max_height:
            return font
    return get_font("title", 20)


def draw_centered_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, font, fill: tuple[int, int, int]) -> None:
    left, top, right, bottom = box
    text_left, text_top, text_right, text_bottom = draw.textbbox((0, 0), text, font=font)
    text_width = text_right - text_left
    text_height = text_bottom - text_top
    x = left + max(0, (right - left - text_width) // 2) - text_left
    y = top + max(0, (bottom - top - text_height) // 2) - text_top
    draw.text((x, y), text, font=font, fill=fill)


def draw_back(style_key: str, label: str, size: tuple[int, int] = (CARD_WIDTH_PX, CARD_HEIGHT_PX)) -> Image.Image:
    style = DECK_STYLES.get(BACK_STYLES.get(style_key, style_key), DECK_STYLES["utility"])
    image = Image.new("RGB", size, style["dark"])
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for y in range(height):
        blend = y / max(1, height - 1)
        color = tuple(int(style["dark"][i] * (1 - blend) + style["mid"][i] * blend) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    stripe_step = max(28, min(width, height) // 20)
    for offset in range(-height, width, stripe_step):
        draw.line((offset, height, offset + height, 0), fill=style["accent"], width=max(2, min(width, height) // 360))
        draw.line((offset + stripe_step // 2, 0, offset + height + stripe_step // 2, height), fill=style["mid"], width=1)

    margin = max(38, min(width, height) // 16)
    outer_w = max(6, min(width, height) // 110)
    inner_margin = max(24, min(width, height) // 25)
    inner_w = max(3, min(width, height) // 200)
    draw.rectangle((margin, margin, width - margin, height - margin), outline=style["light"], width=outer_w)
    draw.rectangle((margin + inner_margin, margin + inner_margin, width - margin - inner_margin, height - margin - inner_margin), outline=(20, 18, 16), width=inner_w)

    center = (width // 2, height // 2)
    radius = min(width, height) // 5
    for inset in (0, max(12, radius // 5), max(24, radius // 3)):
        box = (
            center[0] - radius + inset,
            center[1] - radius + inset,
            center[0] + radius - inset,
            center[1] + radius - inset,
        )
        draw.ellipse(box, outline=style["light"] if inset == 0 else style["accent"], width=max(3, min(width, height) // 180))

    label_max_width = max(40, width - margin * 2 - inner_margin * 2)
    label_max_height = max(20, min(height // 5, 90))
    font = fit_label_font(draw, label, label_max_width, label_max_height)
    tw, th = text_size(draw, label, font)
    pad_x = max(18, width // 32)
    pad_y = max(12, height // 46)
    label_box = (
        center[0] - tw // 2 - pad_x,
        center[1] - th // 2 - pad_y,
        center[0] + tw // 2 + pad_x,
        center[1] + th // 2 + pad_y,
    )
    draw.rectangle(label_box, fill=style["dark"], outline=style["light"], width=max(3, min(width, height) // 220))
    draw_centered_text(draw, label_box, label, font, (255, 245, 220))
    return image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shared-only", action="store_true", help="Generate only the optional shared back.")
    args = parser.parse_args()

    ensure_output_dirs()
    items = {"shared": BACKS["shared"]} if args.shared_only else BACKS
    for style_key, label in items.items():
        output_path = BACK_ROOT / f"{style_key}.png"
        draw_back(style_key, label).save(output_path)
        print(f"Wrote {output_path}")
    print(f"Generated {len(items)} card-back PNGs")


if __name__ == "__main__":
    main()
