#!/usr/bin/env python3
"""Generate the printable Edition 0 table-state board."""

from __future__ import annotations

from dataclasses import dataclass

from PIL import Image, ImageDraw

from card_rendering_common import (
    GENERATED_ROOT,
    PRINT_ROOT,
    PRINT_DPI,
    draw_centered_lines,
    fit_font_for_text,
    get_font,
    rounded_rect,
    text_size,
    wrap_text,
)
from print_pdf_common import save_multipage_pdf


PAGE_WIDTH_IN = 8.5
PAGE_HEIGHT_IN = 11.0
PAGE_COUNT = 3
PAGE_WIDTH_PX = int(PAGE_WIDTH_IN * PRINT_DPI)
PAGE_HEIGHT_PX = int(PAGE_HEIGHT_IN * PRINT_DPI)
BOARD_WIDTH_PX = PAGE_WIDTH_PX * PAGE_COUNT
BOARD_HEIGHT_PX = PAGE_HEIGHT_PX
OUT_DIR = GENERATED_ROOT / "board"
BOARD_PDF_PATH = PRINT_ROOT / "table-board-pages.pdf"
STANDARD_CARD_WIDTH_IN = 2.125
STANDARD_CARD_HEIGHT_IN = 3.6667
QUEST_CARD_WIDTH_IN = STANDARD_CARD_WIDTH_IN * 2
QUEST_CARD_HEIGHT_IN = STANDARD_CARD_HEIGHT_IN * 2
PHYSICAL_TOKEN_DIAMETER_IN = 0.875

BG = (32, 35, 32)
PANEL = (232, 226, 205)
PANEL_ALT = (218, 226, 222)
INK = (22, 23, 20)
LINE = (188, 176, 126)
ACCENT = (142, 74, 44)
MUTED = (80, 86, 77)


@dataclass(frozen=True)
class Zone:
    title: str
    subtitle: str
    x: float
    y: float
    w: float
    h: float
    kind: str = "panel"


def px(value_in: float) -> int:
    return int(round(value_in * PRINT_DPI))


def box(zone: Zone) -> tuple[int, int, int, int]:
    return px(zone.x), px(zone.y), px(zone.x + zone.w), px(zone.y + zone.h)


ZONES = [
    Zone("Quest Reference", "Ashen Depths four-slot quest card", 0.45, 0.55, 4.65, 8.45, "quest"),
    Zone("Party HP", "", 5.35, 0.55, 2.75, 2.0, "party_hp"),
    Zone("Escalation Meter", "vertical 0-10 scene tension track", 5.35, 2.85, 2.75, 6.15, "meter"),
    Zone("Fixed Player Order", "seat order, active marker, tie-break reminder", 0.45, 9.3, 7.65, 1.1, "wide"),
    Zone("Current Encounter", "revealed scene, prep scene, trader, or ordeal", 8.85, 0.55, 2.5, 4.75, "scene"),
    Zone("Encounter Deck", "shuffled encounter cards", 11.6, 0.55, 2.5, 4.75, "deck"),
    Zone("Scripted Ordeals", "hold until quest calls them", 14.35, 0.55, 2.5, 4.75, "deck"),
    Zone("Resource Deck", "player action/resource cards", 8.85, 5.65, 2.5, 4.75, "deck"),
    Zone("Entity Deck", "creatures, artifacts, allies, summons", 11.6, 5.65, 2.5, 4.75, "deck"),
    Zone("Secret Agenda Deck", "deal one hidden agenda per player", 14.35, 5.65, 2.5, 4.75, "deck"),
    Zone("Shared Party Cards", "", 17.35, 0.55, 7.8, 8.1, "shared"),
    Zone("Token Bank", "", 17.35, 8.72, 7.8, 1.68, "tokens"),
]


def draw_background(draw: ImageDraw.ImageDraw) -> None:
    for y in range(BOARD_HEIGHT_PX):
        blend = y / max(1, BOARD_HEIGHT_PX - 1)
        color = tuple(int(BG[i] * (1 - blend) + (58, 62, 52)[i] * blend) for i in range(3))
        draw.line((0, y, BOARD_WIDTH_PX, y), fill=color)
    for offset in range(-BOARD_HEIGHT_PX, BOARD_WIDTH_PX, px(0.42)):
        draw.line((offset, BOARD_HEIGHT_PX, offset + BOARD_HEIGHT_PX, 0), fill=(70, 78, 62), width=1)
    draw.rectangle((0, 0, BOARD_WIDTH_PX - 1, BOARD_HEIGHT_PX - 1), outline=LINE, width=px(0.05))
    for page in range(1, PAGE_COUNT):
        x = page * PAGE_WIDTH_PX
        draw.line((x, 0, x, BOARD_HEIGHT_PX), fill=(18, 18, 17), width=px(0.04))


def draw_label(draw: ImageDraw.ImageDraw, text: str, rect: tuple[int, int, int, int], font, fill=INK, align: str = "left") -> None:
    left, top, right, bottom = rect
    lines = wrap_text(draw, text, font, right - left)
    y = top
    line_h = font.getbbox("Ag")[3] - font.getbbox("Ag")[1] + 4
    for line in lines:
        line_w, _ = text_size(draw, line, font)
        x = left
        if align == "center":
            x = left + max(0, (right - left - line_w) // 2)
        draw.text((x, y), line, font=font, fill=fill)
        y += line_h
        if y > bottom:
            break


def draw_zone_title(draw: ImageDraw.ImageDraw, text: str, rect: tuple[int, int, int, int]) -> int:
    left, top, right, bottom = rect
    title_box = (left + px(0.08), top + px(0.04), right - px(0.08), top + px(0.5))
    font, lines, _ = fit_font_for_text(
        draw,
        text,
        "title",
        63,
        44,
        title_box[2] - title_box[0],
        title_box[3] - title_box[1],
    )
    draw_centered_lines(draw, title_box, lines[:2], font, INK, spacing=0)
    return min(bottom, title_box[3] + px(0.01))


def draw_deck_guides(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    slot_width_in: float = STANDARD_CARD_WIDTH_IN,
    slot_height_in: float = STANDARD_CARD_HEIGHT_IN,
    count: int = 3,
) -> None:
    left, top, right, bottom = rect
    slot_w = px(slot_width_in)
    slot_h = px(slot_height_in)
    shift_step = px(0.045)
    stack_shift = shift_step * max(0, count - 1)
    usable_top = top + px(0.78)
    usable_bottom = bottom - px(0.08)
    slot_left = left + max(0, (right - left - slot_w - stack_shift) // 2)
    slot_top = usable_top + max(0, (usable_bottom - usable_top - slot_h - stack_shift) // 2)
    for index in range(count):
        shift = shift_step * index
        draw.rounded_rectangle(
            (slot_left + shift, slot_top + shift, slot_left + slot_w + shift, slot_top + slot_h + shift),
            radius=px(0.06),
            outline=MUTED,
            width=2,
        )


def draw_card_grid_guides(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    cols: int,
    rows: int,
    slot_width_in: float = STANDARD_CARD_WIDTH_IN,
    slot_height_in: float = STANDARD_CARD_HEIGHT_IN,
) -> None:
    left, top, right, bottom = rect
    slot_w = px(slot_width_in)
    slot_h = px(slot_height_in)
    usable_left = left + px(0.12)
    usable_right = right - px(0.12)
    usable_top = top + px(0.42)
    usable_bottom = bottom - px(0.05)
    total_w = slot_w * cols
    total_h = slot_h * rows
    col_gap = max(px(0.08), (usable_right - usable_left - total_w) // max(1, cols - 1))
    row_gap = max(px(0.08), min(px(0.14), (usable_bottom - usable_top - total_h) // max(1, rows - 1)))
    grid_w = total_w + col_gap * (cols - 1)
    grid_h = total_h + row_gap * (rows - 1)
    grid_left = usable_left + max(0, (usable_right - usable_left - grid_w) // 2)
    grid_top = usable_top + max(0, (usable_bottom - usable_top - grid_h) // 2)
    for row in range(rows):
        for col in range(cols):
            x0 = grid_left + col * (slot_w + col_gap)
            y0 = grid_top + row * (slot_h + row_gap)
            draw.rounded_rectangle(
                (x0, y0, x0 + slot_w, y0 + slot_h),
                radius=px(0.06),
                outline=MUTED,
                width=2,
            )


def draw_d20_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    cx, cy = center
    points = [
        (cx, cy - radius),
        (cx + int(radius * 0.9), cy - int(radius * 0.34)),
        (cx + int(radius * 0.56), cy + int(radius * 0.82)),
        (cx - int(radius * 0.56), cy + int(radius * 0.82)),
        (cx - int(radius * 0.9), cy - int(radius * 0.34)),
    ]
    draw.polygon(points, fill=(164, 38, 34), outline=INK)
    inner = [
        (cx, cy - int(radius * 0.72)),
        (cx + int(radius * 0.58), cy - int(radius * 0.2)),
        (cx + int(radius * 0.36), cy + int(radius * 0.52)),
        (cx - int(radius * 0.36), cy + int(radius * 0.52)),
        (cx - int(radius * 0.58), cy - int(radius * 0.2)),
    ]
    draw.line(points + [points[0]], fill=INK, width=4)
    draw.line(inner + [inner[0]], fill=(230, 118, 93), width=3)
    for point in inner:
        draw.line((cx, cy, point[0], point[1]), fill=(94, 25, 23), width=2)
    font = get_font("body_bold", max(26, radius // 2))
    label = "20"
    tw, th = text_size(draw, label, font)
    draw.text((cx - tw // 2, cy - th // 2 - 3), label, font=font, fill=(255, 230, 196))


def draw_skull_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    cx, cy = center
    bone = (234, 226, 203)
    shadow = (61, 34, 31)
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + int(radius * 0.82)), fill=bone, outline=shadow, width=3)
    jaw_top = cy + int(radius * 0.34)
    draw.rounded_rectangle(
        (cx - int(radius * 0.55), jaw_top, cx + int(radius * 0.55), cy + int(radius * 1.08)),
        radius=max(2, radius // 8),
        fill=bone,
        outline=shadow,
        width=3,
    )
    eye_r = max(2, radius // 5)
    for eye_x in (cx - int(radius * 0.36), cx + int(radius * 0.36)):
        draw.ellipse((eye_x - eye_r, cy - eye_r, eye_x + eye_r, cy + eye_r), fill=INK)
    nose = [
        (cx, cy + int(radius * 0.15)),
        (cx - int(radius * 0.13), cy + int(radius * 0.42)),
        (cx + int(radius * 0.13), cy + int(radius * 0.42)),
    ]
    draw.polygon(nose, fill=INK)
    tooth_top = cy + int(radius * 0.62)
    for offset in (-0.24, 0, 0.24):
        x = cx + int(radius * offset)
        draw.line((x, tooth_top, x, cy + int(radius * 1.02)), fill=shadow, width=2)


def draw_calm_start_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int) -> None:
    cx, cy = center
    sky = (139, 179, 217)
    grass = (77, 135, 76)
    sun = (235, 196, 79)
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=sky, outline=INK, width=3)
    sun_r = max(3, radius // 4)
    sun_y = cy - int(radius * 0.58)
    draw.ellipse((cx - sun_r, sun_y - sun_r, cx + sun_r, sun_y + sun_r), fill=sun, outline=INK, width=2)
    hill_y = cy + int(radius * 0.25)
    draw.pieslice((cx - int(radius * 1.15), hill_y - radius, cx + int(radius * 1.15), hill_y + radius), 0, 180, fill=grass)
    draw.arc((cx - int(radius * 1.15), hill_y - radius, cx + int(radius * 1.15), hill_y + radius), 0, 180, fill=INK, width=2)


def draw_party_hp(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    left, top, right, bottom = rect
    icon_radius = min(px(0.58), (bottom - top) // 3)
    icon_center = (left + px(0.68), top + px(1.05))
    draw_d20_icon(draw, icon_center, icon_radius)
    label_font = get_font("body_bold", 36)
    draw_label(
        draw,
        "Set red d20 to party HP",
        (left + px(1.24), top + px(0.78), right - px(0.08), top + px(1.18)),
        label_font,
        INK,
        align="center",
    )
    shield_font = get_font("body_bold", 28)
    shield_box = (left + px(1.24), top + px(1.22), right - px(0.08), bottom - px(0.08))
    rounded_rect(draw, shield_box, px(0.06), fill=(205, 219, 232), outline=MUTED, width=2)
    draw_label(
        draw,
        "Party shield tokens",
        (shield_box[0] + px(0.04), shield_box[1] + px(0.05), shield_box[2] - px(0.04), shield_box[3] - px(0.04)),
        shield_font,
        MUTED,
        align="center",
    )


def draw_meter(draw: ImageDraw.ImageDraw, rect: tuple[int, int, int, int]) -> None:
    left, top, right, bottom = rect
    track = (left + px(0.36), top + px(0.92), right - px(0.36), bottom - px(0.2))
    segment_h = (track[3] - track[1]) / 11
    colors = [(72, 118, 70)] * 5 + [(174, 145, 55)] * 3 + [(151, 67, 54)] * 2 + [(95, 34, 34)]
    number_font = get_font("title", 56)
    for value in range(11):
        y1 = int(track[3] - value * segment_h)
        y0 = int(track[3] - (value + 1) * segment_h)
        draw.rectangle((track[0], y0, track[2], y1), fill=colors[value], outline=INK)
        label = str(value)
        tw, th = text_size(draw, label, number_font)
        icon_radius = max(8, min(int((y1 - y0) * 0.26), px(0.16)))
        center_x = (track[0] + track[2]) // 2
        text_x = center_x - tw // 2
        text_y = y0 + (y1 - y0 - th) // 2 - px(0.01)
        draw.text((text_x, text_y), label, font=number_font, fill=(18, 18, 16))
        icon_center = (center_x + tw // 2 + px(0.08) + icon_radius, (y0 + y1) // 2)
        if value == 10:
            draw_skull_icon(draw, icon_center, icon_radius)
        if value == 0:
            draw_calm_start_icon(draw, icon_center, icon_radius)
    draw.rectangle(track, outline=INK, width=4)


def draw_zone(draw: ImageDraw.ImageDraw, zone: Zone) -> None:
    rect = box(zone)
    left, top, right, bottom = rect
    fill = PANEL_ALT if zone.kind in {"widget", "party_hp", "meter", "tokens"} else PANEL
    rounded_rect(draw, rect, px(0.08), fill=fill, outline=(15, 15, 13), width=3)
    sub_font = get_font("body_bold", 36)
    sub_top = draw_zone_title(draw, zone.title, rect)
    if zone.subtitle and zone.kind not in {"party_hp", "tokens"}:
        draw_label(
            draw,
            zone.subtitle,
            (left + px(0.08), sub_top, right - px(0.08), top + px(0.78)),
            sub_font,
            MUTED,
            align="center",
        )
    if zone.kind == "quest":
        draw_deck_guides(draw, rect, QUEST_CARD_WIDTH_IN, QUEST_CARD_HEIGHT_IN, 1)
    if zone.kind == "deck":
        draw_deck_guides(draw, rect, STANDARD_CARD_WIDTH_IN, STANDARD_CARD_HEIGHT_IN, 3)
    if zone.kind == "scene":
        draw_deck_guides(draw, rect, STANDARD_CARD_WIDTH_IN, STANDARD_CARD_HEIGHT_IN, 1)
    if zone.kind == "shared":
        draw_card_grid_guides(draw, rect, 3, 2)
    if zone.kind == "party_hp":
        draw_party_hp(draw, rect)
    if zone.kind == "meter":
        draw_meter(draw, rect)
    if zone.kind == "tokens":
        labels = ["Damage", "Shield", "Used", "Reminder"]
        colors = [(160, 45, 40), (45, 90, 165), (194, 156, 56), (70, 128, 76)]
        usable_left = left + px(0.75)
        usable_right = right - px(0.75)
        step = (usable_right - usable_left) / max(1, len(labels) - 1)
        token_y = top + px(0.95)
        label_font = get_font("body_bold", 32)
        radius = px(PHYSICAL_TOKEN_DIAMETER_IN / 2)
        for index, (label, color) in enumerate(zip(labels, colors)):
            cx = int(usable_left + step * index)
            draw.ellipse((cx - radius, token_y - radius, cx + radius, token_y + radius), fill=color, outline=INK, width=3)
            label_w, _ = text_size(draw, label, label_font)
            draw.text((cx - label_w // 2, token_y + radius + px(0.06)), label, font=label_font, fill=MUTED)


def draw_join_labels(draw: ImageDraw.ImageDraw) -> None:
    font = get_font("body_bold", 22)
    labels = [
        (PAGE_WIDTH_PX - px(1.9), px(0.08), "RIGHT -> PAGE 2"),
        (PAGE_WIDTH_PX - px(1.9), BOARD_HEIGHT_PX - px(0.28), "RIGHT -> PAGE 2"),
        (PAGE_WIDTH_PX + px(0.1), px(0.08), "LEFT -> PAGE 1"),
        (PAGE_WIDTH_PX + px(0.1), BOARD_HEIGHT_PX - px(0.28), "LEFT -> PAGE 1"),
        (PAGE_WIDTH_PX * 2 - px(1.9), px(0.08), "RIGHT -> PAGE 3"),
        (PAGE_WIDTH_PX * 2 - px(1.9), BOARD_HEIGHT_PX - px(0.28), "RIGHT -> PAGE 3"),
        (PAGE_WIDTH_PX * 2 + px(0.1), px(0.08), "LEFT -> PAGE 2"),
        (PAGE_WIDTH_PX * 2 + px(0.1), BOARD_HEIGHT_PX - px(0.28), "LEFT -> PAGE 2"),
    ]
    for x, y, text in labels:
        draw.text((x, y), text, font=font, fill=LINE)


def draw_join_sigils(draw: ImageDraw.ImageDraw) -> None:
    for seam, label in ((PAGE_WIDTH_PX, "I"), (PAGE_WIDTH_PX * 2, "II")):
        cy = BOARD_HEIGHT_PX // 2
        radius = px(0.3)
        points = [(seam, cy - radius), (seam + radius, cy), (seam, cy + radius), (seam - radius, cy)]
        draw.polygon(points, fill=(78, 70, 45), outline=LINE)
        draw.line((seam - radius, cy, seam + radius, cy), fill=LINE, width=3)
        draw.line((seam, cy - radius, seam, cy + radius), fill=LINE, width=3)
        font = get_font("body_bold", 30)
        tw, th = text_size(draw, label, font)
        draw.text((seam - tw // 2, cy - th // 2 - 2), label, font=font, fill=(242, 228, 170))


def draw_page_titles(draw: ImageDraw.ImageDraw) -> None:
    font = get_font("title", 34)
    titles = ["Board Page 1: Left", "Board Page 2: Center", "Board Page 3: Right"]
    for index, title in enumerate(titles):
        x0 = index * PAGE_WIDTH_PX
        tw, _ = text_size(draw, title, font)
        draw.text((x0 + (PAGE_WIDTH_PX - tw) // 2, px(0.08)), title, font=font, fill=LINE)


def build_board() -> Image.Image:
    image = Image.new("RGB", (BOARD_WIDTH_PX, BOARD_HEIGHT_PX), BG)
    draw = ImageDraw.Draw(image)
    draw_background(draw)
    draw_page_titles(draw)
    for zone in ZONES:
        draw_zone(draw, zone)
    draw_join_sigils(draw)
    draw_join_labels(draw)
    return image


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PRINT_ROOT.mkdir(parents=True, exist_ok=True)
    board = build_board()
    full_path = OUT_DIR / "table-board-full.png"
    board.save(full_path)
    page_names = ["BOARD-PAGE-01-left.png", "BOARD-PAGE-02-center.png", "BOARD-PAGE-03-right.png"]
    pages: list[Image.Image] = []
    for index, name in enumerate(page_names):
        left = index * PAGE_WIDTH_PX
        page = board.crop((left, 0, left + PAGE_WIDTH_PX, PAGE_HEIGHT_PX))
        page.save(OUT_DIR / name)
        pages.append(page)
    save_multipage_pdf(BOARD_PDF_PATH, pages, PRINT_DPI)
    print(f"Wrote {full_path}")
    for name in page_names:
        print(f"Wrote {OUT_DIR / name}")


if __name__ == "__main__":
    main()
