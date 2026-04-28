#!/usr/bin/env python3
"""Generate the printable Edition 0 quick-start guide PDF."""

from __future__ import annotations

import argparse
import math
import random
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

from card_rendering_common import GENERATED_ROOT, PRINT_DPI, QUICK_START_PATH


PAGE_WIDTH_IN = 8.5
PAGE_HEIGHT_IN = 11.0
PAGE_WIDTH_PX = int(PAGE_WIDTH_IN * PRINT_DPI)
PAGE_HEIGHT_PX = int(PAGE_HEIGHT_IN * PRINT_DPI)
OUT_DIR = GENERATED_ROOT / "guide"
PDF_PATH = OUT_DIR / "quick-start-guide.pdf"

PARCHMENT = (218, 188, 125)
PARCHMENT_DARK = (118, 76, 31)
PARCHMENT_LIGHT = (247, 230, 182)
INK = (42, 30, 21)
MUTED_INK = (96, 72, 48)
RULE = (127, 88, 45)
ACCENT = (113, 36, 32)

FONT_PATHS = {
    "gothic": [
        Path("C:/Windows/Fonts/OLDENGL.TTF"),
        Path("C:/Windows/Fonts/GOTHICB.TTF"),
        Path("C:/Windows/Fonts/georgiab.ttf"),
    ],
    "body": [
        Path("C:/Windows/Fonts/GARA.TTF"),
        Path("C:/Windows/Fonts/pala.ttf"),
        Path("C:/Windows/Fonts/BKANT.TTF"),
        Path("C:/Windows/Fonts/georgia.ttf"),
        Path("C:/Windows/Fonts/cambria.ttc"),
        Path("C:/Windows/Fonts/calibri.ttf"),
    ],
    "body_bold": [
        Path("C:/Windows/Fonts/GARABD.TTF"),
        Path("C:/Windows/Fonts/palab.ttf"),
        Path("C:/Windows/Fonts/BKANTB.TTF"),
        Path("C:/Windows/Fonts/georgiab.ttf"),
        Path("C:/Windows/Fonts/cambriab.ttf"),
        Path("C:/Windows/Fonts/calibrib.ttf"),
    ],
    "italic": [
        Path("C:/Windows/Fonts/GARAIT.TTF"),
        Path("C:/Windows/Fonts/palai.ttf"),
        Path("C:/Windows/Fonts/georgiai.ttf"),
        Path("C:/Windows/Fonts/cambriai.ttf"),
        Path("C:/Windows/Fonts/calibrii.ttf"),
    ],
}


@dataclass(frozen=True)
class Style:
    body: int
    h2: int
    h3: int
    leading: float
    para_gap: int
    bullet_gap: int


@dataclass
class Cursor:
    column: int
    x: int
    y: int


def px(value_in: float) -> int:
    return int(round(value_in * PRINT_DPI))


def font_path(kind: str) -> Path | None:
    for path in FONT_PATHS[kind]:
        if path.exists():
            return path
    return None


def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    path = font_path(kind)
    if path is None:
        return ImageFont.load_default()
    return ImageFont.truetype(str(path), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, chosen_font: ImageFont.ImageFont) -> tuple[int, int]:
    if not text:
        return 0, 0
    left, top, right, bottom = draw.textbbox((0, 0), text, font=chosen_font)
    return right - left, bottom - top


def line_height(chosen_font: ImageFont.ImageFont, leading: float) -> int:
    bbox = chosen_font.getbbox("Ag")
    return int(round((bbox[3] - bbox[1]) * leading))


def clean_inline(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.replace("&amp;", "&")
    return text.strip()


def strip_comments(markdown: str) -> str:
    return re.sub(r"<!--.*?-->", "", markdown, flags=re.S)


def split_sheets(markdown: str) -> list[list[str]]:
    body = strip_comments(markdown)
    parts = re.split(r'<div class="page-break"></div>', body)
    sheets = []
    for part in parts:
        lines = [line.rstrip() for line in part.strip().splitlines()]
        lines = [line for line in lines if line.strip() != "# Quick Start Guide"]
        if any(line.strip() for line in lines):
            sheets.append(lines)
    return sheets


def parchment_background(page_index: int) -> Image.Image:
    rng = random.Random(104729 + page_index)
    image = Image.new("RGB", (PAGE_WIDTH_PX, PAGE_HEIGHT_PX), PARCHMENT)
    base_draw = ImageDraw.Draw(image)
    cx = PAGE_WIDTH_PX / 2
    cy = PAGE_HEIGHT_PX / 2
    for y in range(PAGE_HEIGHT_PX):
        blend = y / max(1, PAGE_HEIGHT_PX - 1)
        radial = abs((y - cy) / cy) * 0.11
        color = tuple(
            int(PARCHMENT_LIGHT[channel] * (1 - blend * 0.20 - radial) + PARCHMENT[channel] * (blend * 0.20 + radial))
            for channel in range(3)
        )
        base_draw.line((0, y, PAGE_WIDTH_PX, y), fill=color)

    fine_noise = Image.effect_noise((PAGE_WIDTH_PX, PAGE_HEIGHT_PX), 22).convert("L")
    fine_noise = ImageOps.colorize(fine_noise, (176, 130, 66), (252, 239, 197))
    image = Image.blend(image, fine_noise, 0.16)

    cloud = Image.effect_noise((PAGE_WIDTH_PX // 3, PAGE_HEIGHT_PX // 3), 82).convert("L")
    cloud = cloud.resize((PAGE_WIDTH_PX, PAGE_HEIGHT_PX), Image.Resampling.BICUBIC).filter(ImageFilter.GaussianBlur(px(0.05)))
    cloud_color = ImageOps.colorize(cloud, (154, 98, 43), (250, 235, 190))
    image = Image.blend(image, cloud_color, 0.24)

    stains = Image.new("RGBA", image.size, (0, 0, 0, 0))
    stain_draw = ImageDraw.Draw(stains)
    for _ in range(42):
        x = rng.randrange(px(0.35), PAGE_WIDTH_PX - px(0.35))
        y = rng.randrange(px(0.35), PAGE_HEIGHT_PX - px(0.35))
        rx = rng.randrange(px(0.18), px(0.95))
        ry = rng.randrange(px(0.10), px(0.55))
        alpha = rng.randrange(10, 34)
        stain_draw.ellipse((x - rx, y - ry, x + rx, y + ry), fill=(105, 63, 28, alpha))
    stains = stains.filter(ImageFilter.GaussianBlur(px(0.09)))
    image = Image.alpha_composite(image.convert("RGBA"), stains).convert("RGB")

    texture = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(texture)
    for _ in range(150):
        y = rng.randrange(0, PAGE_HEIGHT_PX)
        alpha = rng.randrange(9, 25)
        draw.line((0, y, PAGE_WIDTH_PX, y + rng.randrange(-9, 10)), fill=(101, 63, 30, alpha), width=1)
    for _ in range(70):
        x = rng.randrange(0, PAGE_WIDTH_PX)
        alpha = rng.randrange(5, 15)
        draw.line((x, 0, x + rng.randrange(-26, 27), PAGE_HEIGHT_PX), fill=(255, 246, 207, alpha), width=1)
    for _ in range(32):
        x1 = rng.randrange(px(0.2), PAGE_WIDTH_PX - px(0.2))
        y1 = rng.randrange(px(0.2), PAGE_HEIGHT_PX - px(0.2))
        length = rng.randrange(px(0.25), px(1.2))
        x2 = x1 + rng.randrange(-length, length)
        y2 = y1 + rng.randrange(-length // 2, length // 2)
        draw.line((x1, y1, x2, y2), fill=(94, 58, 26, rng.randrange(14, 34)), width=1)
    image = Image.alpha_composite(image.convert("RGBA"), texture).convert("RGB")

    edge_mask = Image.new("L", image.size, 0)
    edge_pixels = edge_mask.load()
    max_edge = px(0.95)
    step = max(1, px(0.018))
    for y in range(0, PAGE_HEIGHT_PX, step):
        for x in range(0, PAGE_WIDTH_PX, step):
            dist = min(x, y, PAGE_WIDTH_PX - 1 - x, PAGE_HEIGHT_PX - 1 - y)
            if dist >= max_edge:
                alpha = 0
            else:
                curve = (1 - dist / max_edge) ** 1.35
                alpha = int(180 * curve)
            for fill_y in range(y, min(y + step, PAGE_HEIGHT_PX)):
                for fill_x in range(x, min(x + step, PAGE_WIDTH_PX)):
                    edge_pixels[fill_x, fill_y] = alpha
    edge_noise = Image.effect_noise((PAGE_WIDTH_PX // 4, PAGE_HEIGHT_PX // 4), 100).convert("L")
    edge_noise = edge_noise.resize(image.size, Image.Resampling.BICUBIC).filter(ImageFilter.GaussianBlur(px(0.04)))
    edge_mask = ImageChops.multiply(edge_mask, ImageOps.autocontrast(edge_noise))
    edge_color = Image.new("RGB", image.size, (95, 57, 23))
    image = Image.composite(edge_color, image, edge_mask)
    return image.filter(ImageFilter.SMOOTH)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, chosen_font: ImageFont.ImageFont, width: int) -> list[str]:
    words = clean_inline(text).split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_size(draw, candidate, chosen_font)[0] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def is_table_start(lines: list[str], index: int) -> bool:
    return index + 1 < len(lines) and lines[index].lstrip().startswith("|") and lines[index + 1].lstrip().startswith("|")


def collect_table(lines: list[str], index: int) -> tuple[list[list[str]], int]:
    table_lines = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        table_lines.append(lines[index])
        index += 1
    rows = []
    for line in table_lines:
        cells = [clean_inline(cell) for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells):
            continue
        rows.append(cells)
    return rows, index


def make_page(page_index: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = parchment_background(page_index)
    draw = ImageDraw.Draw(image)
    margin = px(0.34)
    draw.rounded_rectangle(
        (margin, margin, PAGE_WIDTH_PX - margin, PAGE_HEIGHT_PX - margin),
        radius=px(0.12),
        outline=RULE,
        width=px(0.018),
    )
    draw.rounded_rectangle(
        (margin + px(0.08), margin + px(0.08), PAGE_WIDTH_PX - margin - px(0.08), PAGE_HEIGHT_PX - margin - px(0.08)),
        radius=px(0.08),
        outline=(172, 124, 65),
        width=2,
    )
    return image, draw


def draw_lines(
    draw: ImageDraw.ImageDraw,
    cursor: Cursor,
    lines: list[str],
    chosen_font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    width: int,
    leading: float,
    indent: int = 0,
) -> int:
    line_h = line_height(chosen_font, leading)
    for line in lines:
        draw.text((cursor.x + indent, cursor.y), line, font=chosen_font, fill=fill)
        cursor.y += line_h
    return cursor.y


def draw_table(
    draw: ImageDraw.ImageDraw,
    cursor: Cursor,
    rows: list[list[str]],
    col_width: int,
    style: Style,
) -> None:
    if not rows:
        return
    table_font = font("body", max(25, style.body - 4))
    header_font = font("body_bold", max(25, style.body - 4))
    columns = max(len(row) for row in rows)
    cell_pad = px(0.035)
    if columns == 3:
        widths = [int(col_width * 0.22), int(col_width * 0.22)]
        widths.append(col_width - sum(widths))
    elif columns == 2:
        widths = [int(col_width * 0.32), col_width - int(col_width * 0.32)]
    else:
        widths = [col_width // columns] * columns
    x0 = cursor.x
    for row_index, row in enumerate(rows):
        cell_lines = []
        row_h = 0
        for col_index in range(columns):
            text = row[col_index] if col_index < len(row) else ""
            chosen = header_font if row_index == 0 else table_font
            wrapped = wrap_text(draw, text, chosen, widths[col_index] - cell_pad * 2)
            cell_lines.append((wrapped, chosen))
            row_h = max(row_h, len(wrapped) * line_height(chosen, 1.05) + cell_pad * 2)
        fill = (223, 202, 154) if row_index == 0 else (239, 224, 184)
        x = x0
        for col_index, (wrapped, chosen) in enumerate(cell_lines):
            rect = (x, cursor.y, x + widths[col_index], cursor.y + row_h)
            draw.rectangle(rect, fill=fill, outline=(154, 107, 57), width=1)
            temp_cursor = Cursor(cursor.column, x + cell_pad, cursor.y + cell_pad)
            draw_lines(draw, temp_cursor, wrapped, chosen, INK, widths[col_index] - cell_pad * 2, 1.05)
            x += widths[col_index]
        cursor.y += row_h
    cursor.y += style.para_gap


def column_geometry() -> tuple[list[int], int, int, int, int]:
    margin_x = px(0.55)
    top = px(1.18)
    bottom = PAGE_HEIGHT_PX - px(0.58)
    gutter = px(0.28)
    col_w = (PAGE_WIDTH_PX - margin_x * 2 - gutter) // 2
    return [margin_x, margin_x + col_w + gutter], col_w, top, bottom, gutter


def advance_column(cursor: Cursor, col_x: list[int], top: int) -> bool:
    if cursor.column == 0:
        cursor.column = 1
        cursor.x = col_x[1]
        cursor.y = top
        return True
    return False


def ensure_space(cursor: Cursor, needed: int, bottom: int, col_x: list[int], top: int) -> bool:
    if cursor.y + needed <= bottom:
        return True
    return advance_column(cursor, col_x, top)


def estimate_text_height(draw: ImageDraw.ImageDraw, text: str, chosen_font: ImageFont.ImageFont, width: int, leading: float) -> int:
    return len(wrap_text(draw, text, chosen_font, width)) * line_height(chosen_font, leading)


def draw_sheet(draw: ImageDraw.ImageDraw, lines: list[str], style: Style, page_num: int) -> bool:
    col_x, col_w, top, bottom, _ = column_geometry()
    title_line = next((line for line in lines if line.startswith("## ")), f"## Sheet {page_num}")
    title_text = clean_inline(title_line.replace("##", "", 1))
    title_font = font("gothic", style.h2)
    title_box = (px(0.55), px(0.42), PAGE_WIDTH_PX - px(0.55), px(1.0))
    title_w, title_h = text_size(draw, title_text, title_font)
    draw.text(
        (title_box[0] + (title_box[2] - title_box[0] - title_w) // 2, title_box[1] + (title_box[3] - title_box[1] - title_h) // 2 - px(0.03)),
        title_text,
        font=title_font,
        fill=INK,
    )
    draw.line((px(0.65), px(1.03), PAGE_WIDTH_PX - px(0.65), px(1.03)), fill=RULE, width=3)

    cursor = Cursor(0, col_x[0], top)
    body_font = font("body", style.body)
    bold_font = font("body_bold", style.body)
    h3_font = font("body_bold", style.h3)
    small_caps = font("body_bold", max(24, style.body - 4))
    index = 0

    while index < len(lines):
        raw = lines[index].strip()
        index += 1
        if not raw or raw.startswith("## "):
            continue
        if is_table_start(lines, index - 1):
            rows, index = collect_table(lines, index - 1)
            estimate = max(px(0.32), len(rows) * px(0.24))
            if not ensure_space(cursor, estimate, bottom, col_x, top):
                return False
            draw_table(draw, cursor, rows, col_w, style)
            continue
        if raw.startswith("### "):
            heading = clean_inline(raw[4:])
            needed = line_height(h3_font, 1.05) + style.para_gap
            if not ensure_space(cursor, needed, bottom, col_x, top):
                return False
            cursor.y += max(0, style.para_gap // 2)
            draw.text((cursor.x, cursor.y), heading, font=h3_font, fill=ACCENT)
            heading_w, _ = text_size(draw, heading, h3_font)
            draw.line((cursor.x, cursor.y + line_height(h3_font, 1.0), cursor.x + min(heading_w + px(0.18), col_w), cursor.y + line_height(h3_font, 1.0)), fill=RULE, width=2)
            cursor.y += line_height(h3_font, 1.08) + style.para_gap
            continue
        if raw.startswith("- ") or re.match(r"\d+\.\s+", raw):
            marker = "•" if raw.startswith("- ") else raw.split(".", 1)[0] + "."
            text = raw[2:] if raw.startswith("- ") else re.sub(r"^\d+\.\s+", "", raw)
            marker_font = bold_font
            marker_w, _ = text_size(draw, marker, marker_font)
            indent = marker_w + px(0.08)
            wrapped = wrap_text(draw, text, body_font, col_w - indent)
            needed = len(wrapped) * line_height(body_font, style.leading) + style.bullet_gap
            if not ensure_space(cursor, needed, bottom, col_x, top):
                return False
            draw.text((cursor.x, cursor.y), marker, font=marker_font, fill=ACCENT)
            draw_lines(draw, cursor, wrapped, body_font, INK, col_w - indent, style.leading, indent)
            cursor.y += style.bullet_gap
            continue
        if raw.startswith("**") and raw.endswith("**"):
            label = clean_inline(raw)
            needed = line_height(small_caps, 1.0) + style.para_gap
            if not ensure_space(cursor, needed, bottom, col_x, top):
                return False
            draw.text((cursor.x, cursor.y), label, font=small_caps, fill=ACCENT)
            cursor.y += line_height(small_caps, 1.0) + max(1, style.para_gap // 3)
            continue

        chosen_font = body_font
        paragraph = clean_inline(raw)
        wrapped = wrap_text(draw, paragraph, chosen_font, col_w)
        needed = len(wrapped) * line_height(chosen_font, style.leading) + style.para_gap
        if not ensure_space(cursor, needed, bottom, col_x, top):
            return False
        draw_lines(draw, cursor, wrapped, chosen_font, INK, col_w, style.leading)
        cursor.y += style.para_gap

    page_font = font("body_bold", 22)
    footer = f"Edition 0 Quick Start - Page {page_num}"
    fw, _ = text_size(draw, footer, page_font)
    draw.text(((PAGE_WIDTH_PX - fw) // 2, PAGE_HEIGHT_PX - px(0.38)), footer, font=page_font, fill=MUTED_INK)
    return True


def render_sheet(lines: list[str], page_num: int) -> Image.Image:
    styles = [
        Style(body=36, h2=66, h3=38, leading=1.14, para_gap=12, bullet_gap=4),
        Style(body=34, h2=62, h3=36, leading=1.10, para_gap=9, bullet_gap=3),
        Style(body=32, h2=58, h3=34, leading=1.06, para_gap=7, bullet_gap=2),
        Style(body=30, h2=54, h3=32, leading=1.03, para_gap=5, bullet_gap=1),
    ]
    for style in styles:
        image, draw = make_page(page_num)
        if draw_sheet(draw, lines, style, page_num):
            return image
    raise RuntimeError(f"Could not fit quick-start sheet {page_num} on one page")


def generate_guide(source: Path = QUICK_START_PATH, pdf_path: Path = PDF_PATH) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sheets = split_sheets(source.read_text(encoding="utf-8"))
    images = [render_sheet(lines, index + 1) for index, lines in enumerate(sheets)]
    page_paths = []
    for index, image in enumerate(images, start=1):
        path = OUT_DIR / f"quick-start-guide-page-{index:02d}.png"
        image.save(path)
        page_paths.append(path)
    images[0].save(
        pdf_path,
        "PDF",
        resolution=PRINT_DPI,
        save_all=True,
        append_images=images[1:],
    )
    return page_paths


def content_geometry() -> tuple[int, int, int, int]:
    margin_x = px(0.82)
    top = px(1.55)
    bottom = PAGE_HEIGHT_PX - px(0.82)
    width = PAGE_WIDTH_PX - margin_x * 2
    return margin_x, width, top, bottom


def fit_font(kind: str, text: str, size: int, max_width: int, min_size: int = 34) -> ImageFont.FreeTypeFont:
    test_image = Image.new("RGB", (16, 16))
    draw = ImageDraw.Draw(test_image)
    while size > min_size:
        chosen = font(kind, size)
        if text_size(draw, text, chosen)[0] <= max_width:
            return chosen
        size -= 2
    return font(kind, min_size)


def page_title(lines: list[str], fallback: str) -> str:
    title_line = next((line for line in lines if line.startswith("## ")), fallback)
    return clean_inline(title_line.replace("##", "", 1))


def draw_page_title(draw: ImageDraw.ImageDraw, title_text: str, style: Style) -> None:
    title_box = (px(0.72), px(0.35), PAGE_WIDTH_PX - px(0.72), px(1.2))
    title_font = fit_font("gothic", title_text, style.h2, title_box[2] - title_box[0], min_size=58)
    title_w, title_h = text_size(draw, title_text, title_font)
    draw.text(
        (
            title_box[0] + (title_box[2] - title_box[0] - title_w) // 2,
            title_box[1] + (title_box[3] - title_box[1] - title_h) // 2 - px(0.02),
        ),
        title_text,
        font=title_font,
        fill=INK,
    )
    draw.line((px(0.82), px(1.28), PAGE_WIDTH_PX - px(0.82), px(1.28)), fill=RULE, width=4)


def draw_footer(draw: ImageDraw.ImageDraw, page_num: int) -> None:
    page_font = font("body_bold", 28)
    footer = f"Edition 0 Quick Start - Page {page_num}"
    fw, _ = text_size(draw, footer, page_font)
    draw.text(((PAGE_WIDTH_PX - fw) // 2, PAGE_HEIGHT_PX - px(0.48)), footer, font=page_font, fill=MUTED_INK)


def estimate_table_height(draw: ImageDraw.ImageDraw, rows: list[list[str]], col_width: int, style: Style) -> int:
    if not rows:
        return 0
    table_font = font("body", max(30, style.body - 4))
    header_font = font("body_bold", max(30, style.body - 3))
    columns = max(len(row) for row in rows)
    cell_pad = px(0.055)
    if columns == 3:
        widths = [int(col_width * 0.22), int(col_width * 0.22)]
        widths.append(col_width - sum(widths))
    elif columns == 2:
        widths = [int(col_width * 0.32), col_width - int(col_width * 0.32)]
    else:
        widths = [col_width // columns] * columns
    height = 0
    for row_index, row in enumerate(rows):
        row_h = 0
        for col_index in range(columns):
            text = row[col_index] if col_index < len(row) else ""
            chosen = header_font if row_index == 0 else table_font
            wrapped = wrap_text(draw, text, chosen, widths[col_index] - cell_pad * 2)
            row_h = max(row_h, len(wrapped) * line_height(chosen, 1.08) + cell_pad * 2)
        height += row_h
    return height + style.para_gap


def guide_block_height(
    draw: ImageDraw.ImageDraw,
    raw: str,
    lines: list[str],
    index: int,
    col_w: int,
    style: Style,
) -> tuple[int, int]:
    body_font = font("body", style.body)
    bold_font = font("body_bold", style.body)
    h3_font = font("gothic", style.h3)
    label_font = font("body_bold", max(34, style.body + 4))
    if is_table_start(lines, index):
        rows, next_index = collect_table(lines, index)
        return estimate_table_height(draw, rows, col_w, style), next_index
    if raw.startswith("### "):
        return line_height(h3_font, 1.05) + style.para_gap + px(0.18), index + 1
    if raw.startswith("- ") or re.match(r"\d+\.\s+", raw):
        marker = chr(8226) if raw.startswith("- ") else raw.split(".", 1)[0] + "."
        text = raw[2:] if raw.startswith("- ") else re.sub(r"^\d+\.\s+", "", raw)
        marker_w, _ = text_size(draw, marker, bold_font)
        indent = marker_w + px(0.11)
        wrapped = wrap_text(draw, text, body_font, col_w - indent)
        return len(wrapped) * line_height(body_font, style.leading) + style.bullet_gap, index + 1
    if raw.startswith("**") and raw.endswith("**"):
        return line_height(label_font, 1.0) + max(1, style.para_gap // 2), index + 1
    wrapped = wrap_text(draw, clean_inline(raw), body_font, col_w)
    return len(wrapped) * line_height(body_font, style.leading) + style.para_gap, index + 1


def next_subsection_end(lines: list[str], index: int) -> int:
    end = index + 1
    while end < len(lines):
        raw = lines[end].strip()
        if raw.startswith("### "):
            break
        end += 1
    return end


def subsection_height(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    start: int,
    col_w: int,
    style: Style,
) -> int:
    end = next_subsection_end(lines, start)
    total = 0
    index = start
    while index < end:
        raw = lines[index].strip()
        if not raw:
            index += 1
            continue
        height, next_index = guide_block_height(draw, raw, lines, index, col_w, style)
        total += height
        index = next_index
    return total


def range_height(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    start: int,
    end: int,
    col_w: int,
    style: Style,
) -> int:
    total = 0
    index = start
    while index < end:
        raw = lines[index].strip()
        if not raw:
            index += 1
            continue
        height, next_index = guide_block_height(draw, raw, lines, index, col_w, style)
        total += height
        index = next_index
    return total


def draw_guide_block(
    draw: ImageDraw.ImageDraw,
    cursor: Cursor,
    raw: str,
    lines: list[str],
    index: int,
    col_w: int,
    style: Style,
) -> int:
    body_font = font("body", style.body)
    bold_font = font("body_bold", style.body)
    h3_font = font("gothic", style.h3)
    label_font = font("body_bold", max(34, style.body + 4))
    if is_table_start(lines, index):
        rows, next_index = collect_table(lines, index)
        draw_table(draw, cursor, rows, col_w, style)
        return next_index
    if raw.startswith("### "):
        heading = clean_inline(raw[4:])
        _, _, top, _ = content_geometry()
        cursor.y += max(0, style.para_gap // 2) if cursor.y <= top + px(0.04) else px(0.18)
        draw.text((cursor.x, cursor.y), heading, font=h3_font, fill=ACCENT)
        heading_w, _ = text_size(draw, heading, h3_font)
        rule_y = cursor.y + line_height(h3_font, 1.0)
        draw.line((cursor.x, rule_y, cursor.x + min(heading_w + px(0.22), col_w), rule_y), fill=RULE, width=3)
        cursor.y += line_height(h3_font, 1.08) + style.para_gap
        return index + 1
    if raw.startswith("- ") or re.match(r"\d+\.\s+", raw):
        marker = chr(8226) if raw.startswith("- ") else raw.split(".", 1)[0] + "."
        text = raw[2:] if raw.startswith("- ") else re.sub(r"^\d+\.\s+", "", raw)
        marker_w, _ = text_size(draw, marker, bold_font)
        indent = marker_w + px(0.11)
        wrapped = wrap_text(draw, text, body_font, col_w - indent)
        draw.text((cursor.x, cursor.y), marker, font=bold_font, fill=ACCENT)
        draw_lines(draw, cursor, wrapped, body_font, INK, col_w - indent, style.leading, indent)
        cursor.y += style.bullet_gap
        return index + 1
    if raw.startswith("**") and raw.endswith("**"):
        label = clean_inline(raw)
        draw.text((cursor.x, cursor.y), label, font=label_font, fill=ACCENT)
        cursor.y += line_height(label_font, 1.0) + max(1, style.para_gap // 2)
        return index + 1

    wrapped = wrap_text(draw, clean_inline(raw), body_font, col_w)
    draw_lines(draw, cursor, wrapped, body_font, INK, col_w, style.leading)
    cursor.y += style.para_gap
    return index + 1


def render_guide_section(lines: list[str], first_page_num: int, style: Style) -> list[Image.Image]:
    title = page_title(lines, f"Sheet {first_page_num}")
    content_lines = [line for line in lines if not line.startswith("## ")]
    images: list[Image.Image] = []
    index = 0
    page_num = first_page_num
    while index < len(content_lines):
        image, draw = make_page(page_num)
        draw_page_title(draw, title, style)
        x, col_w, top, bottom = content_geometry()
        cursor = Cursor(0, x, top)
        started = False
        while index < len(content_lines):
            raw = content_lines[index].strip()
            if not raw:
                index += 1
                continue
            if raw.startswith("### ") and started:
                section_height = subsection_height(draw, content_lines, index, col_w, style)
                if section_height <= bottom - top and cursor.y + section_height > bottom:
                    break
                section_end = next_subsection_end(content_lines, index)
                remaining_height = range_height(draw, content_lines, section_end, len(content_lines), col_w, style)
                would_orphan_tail = (
                    0 < remaining_height < px(1.35)
                    and cursor.y + section_height <= bottom
                    and cursor.y + section_height + remaining_height > bottom
                    and section_height + remaining_height <= bottom - top
                )
                if would_orphan_tail:
                    break
            needed, _ = guide_block_height(draw, raw, content_lines, index, col_w, style)
            if started and cursor.y + needed > bottom:
                break
            if cursor.y + needed > bottom:
                raise RuntimeError(f"Guide block is too tall for one page near: {raw[:80]}")
            index = draw_guide_block(draw, cursor, raw, content_lines, index, col_w, style)
            started = True
        draw_footer(draw, page_num)
        images.append(image)
        page_num += 1
    if not images:
        image, draw = make_page(page_num)
        draw_page_title(draw, title, style)
        draw_footer(draw, page_num)
        images.append(image)
    return images


def generate_guide(source: Path = QUICK_START_PATH, pdf_path: Path = PDF_PATH) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sheets = split_sheets(source.read_text(encoding="utf-8"))
    style = Style(body=63, h2=150, h3=94, leading=1.14, para_gap=26, bullet_gap=12)
    images: list[Image.Image] = []
    next_page = 1
    for lines in sheets:
        section_images = render_guide_section(lines, next_page, style)
        images.extend(section_images)
        next_page += len(section_images)
    page_paths = []
    for index, image in enumerate(images, start=1):
        path = OUT_DIR / f"quick-start-guide-page-{index:02d}.png"
        image.save(path)
        page_paths.append(path)
    images[0].save(
        pdf_path,
        "PDF",
        resolution=PRINT_DPI,
        save_all=True,
        append_images=images[1:],
    )
    return page_paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the printable quick-start guide PDF.")
    parser.add_argument("--source", type=Path, default=QUICK_START_PATH)
    parser.add_argument("--output", type=Path, default=PDF_PATH)
    args = parser.parse_args()
    pages = generate_guide(args.source, args.output)
    print(f"Wrote {args.output}")
    for page in pages:
        print(f"Wrote {page}")


if __name__ == "__main__":
    main()
