#!/usr/bin/env python3
"""Shared helpers for Edition 0 card image generation."""

from __future__ import annotations

import json
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSETS_ROOT = ROOT / "assets"
CARD_ROOT = ROOT / "defines" / "cards"
LAYOUT_PATH = ROOT / "defines" / "card-layout.md"
ATLAS_PATH = ASSETS_ROOT / "card-atlas-definition.md"
QUICK_START_PATH = ROOT / "docs" / "quick-start-guide.md"

CARD_ART_INCOMING_ROOT = ASSETS_ROOT / "card-art" / "incoming"
CARD_ART_FINAL_ROOT = ASSETS_ROOT / "card-art" / "final"
ART_HANDOFF_PATH = ASSETS_ROOT / "card-art" / "AI_ART_HANDOFF.md"
GENERATED_ROOT = ASSETS_ROOT / "generated"
FRAME_ROOT = GENERATED_ROOT / "card-frames"
BACK_ROOT = GENERATED_ROOT / "card-backs"
CARD_FRONT_ROOT = GENERATED_ROOT / "card-fronts"
ATLAS_FRONT_ROOT = GENERATED_ROOT / "atlases" / "fronts"
ATLAS_BACK_ROOT = GENERATED_ROOT / "atlases" / "backs"
PRINT_ROOT = GENERATED_ROOT / "print"

PRINT_DPI = 288
SHEET_WIDTH_IN = 8.5
SHEET_HEIGHT_IN = 11.0
SHEET_WIDTH_PX = int(SHEET_WIDTH_IN * PRINT_DPI)
SHEET_HEIGHT_PX = int(SHEET_HEIGHT_IN * PRINT_DPI)
ATLAS_COLUMNS = 4
ATLAS_ROWS = 3
CARD_WIDTH_PX = SHEET_WIDTH_PX // ATLAS_COLUMNS
CARD_HEIGHT_PX = SHEET_HEIGHT_PX // ATLAS_ROWS
QUEST_CARD_WIDTH_PX = CARD_WIDTH_PX * 2
QUEST_CARD_HEIGHT_PX = CARD_HEIGHT_PX * 2
CLASS_CARD_WIDTH_PX = CARD_WIDTH_PX * 2
CLASS_CARD_HEIGHT_PX = CARD_HEIGHT_PX

SKIP_VALUES = {"", "None", "None."}

DECK_SLUGS = {
    "Agenda Deck": "agenda",
    "Creature Deck": "creature-entity",
    "Encounter Deck": "encounter",
    "Quest Deck": "quest",
    "Resource Deck": "resource",
    "Utility": "utility",
}

LAYOUT_BY_DECK = {
    "Agenda Deck": "agenda",
    "Creature Deck": "creature_entity",
    "Encounter Deck": "encounter",
    "Quest Deck": "quest_reference",
    "Resource Deck": "resource",
    "Utility": "resource",
}

FIELD_LABELS = {
    "Reveal Text": "Reveal",
    "Scene Rule": "Scene",
    "Clear Condition": "Clear",
    "Reward Text": "Reward",
    "Failure Text": "Fail",
    "Rules Text": "Text",
    "Active Ability": "Active",
    "Round End Text": "End",
    "Goal Text": "Goal",
    "Reveal Timing": "Reveal",
    "Setup Text": "Setup",
    "Ongoing Quest Rule": "Rule",
    "Threshold 5": "Esc 5",
    "Threshold 8": "Esc 8",
    "Threshold 10": "Esc 10",
    "Lose Condition": "Lose",
    "Win Condition": "Win",
    "Flavor Text": "Flavor",
}

DECK_STYLES = {
    "resource": {
        "name": "Resource",
        "dark": (64, 35, 23),
        "mid": (139, 82, 44),
        "light": (230, 198, 133),
        "paper": (246, 231, 191),
        "ink": (33, 22, 16),
        "accent": (34, 96, 139),
    },
    "creature-entity": {
        "name": "Creature / Entity",
        "dark": (33, 37, 34),
        "mid": (82, 92, 79),
        "light": (184, 175, 141),
        "paper": (232, 224, 198),
        "ink": (24, 25, 22),
        "accent": (145, 39, 29),
    },
    "encounter": {
        "name": "Encounter",
        "dark": (35, 38, 58),
        "mid": (77, 82, 116),
        "light": (181, 190, 215),
        "paper": (232, 234, 223),
        "ink": (23, 24, 34),
        "accent": (195, 125, 46),
    },
    "agenda": {
        "name": "Secret Agenda",
        "dark": (33, 24, 45),
        "mid": (86, 58, 104),
        "light": (203, 180, 218),
        "paper": (234, 226, 237),
        "ink": (25, 20, 31),
        "accent": (167, 38, 81),
    },
    "quest": {
        "name": "Quest",
        "dark": (47, 48, 37),
        "mid": (96, 99, 65),
        "light": (206, 197, 141),
        "paper": (239, 231, 198),
        "ink": (27, 27, 20),
        "accent": (150, 61, 36),
    },
    "utility": {
        "name": "Utility",
        "dark": (42, 42, 42),
        "mid": (92, 92, 92),
        "light": (205, 205, 196),
        "paper": (238, 238, 226),
        "ink": (26, 26, 24),
        "accent": (80, 100, 120),
    },
}


def rarity_tier(card: dict) -> str:
    rarity = card.get("Rarity", "").strip().lower()
    if rarity and rarity != "common":
        return "rare"
    return "common"


def blend_color(a: tuple[int, int, int], b: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    return tuple(int(a[index] * (1 - amount) + b[index] * amount) for index in range(3))


def style_for_card(card: dict) -> dict:
    base = dict(DECK_STYLES[deck_slug(card.get("Deck", "Utility"))])
    if rarity_tier(card) == "rare":
        base["dark"] = blend_color(base["dark"], (10, 8, 12), 0.35)
        base["mid"] = blend_color(base["mid"], base["accent"], 0.25)
        base["light"] = blend_color(base["light"], (246, 205, 95), 0.35)
        base["paper"] = blend_color(base["paper"], (248, 232, 190), 0.18)
        base["accent"] = blend_color(base["accent"], (214, 151, 40), 0.45)
    return base


def frame_path_for_card(card: dict, layout_name: str | None = None) -> Path:
    layout = layout_name or layout_name_for_card(card)
    return FRAME_ROOT / f"{layout}-{rarity_tier(card)}.png"

FONT_CANDIDATES = {
    "title": [
        Path("C:/Windows/Fonts/georgiab.ttf"),
        Path("C:/Windows/Fonts/georgia.ttf"),
        Path("C:/Windows/Fonts/timesbd.ttf"),
    ],
    "body": [
        Path("C:/Windows/Fonts/georgia.ttf"),
        Path("C:/Windows/Fonts/calibri.ttf"),
        Path("C:/Windows/Fonts/times.ttf"),
    ],
    "body_bold": [
        Path("C:/Windows/Fonts/georgiab.ttf"),
        Path("C:/Windows/Fonts/calibrib.ttf"),
        Path("C:/Windows/Fonts/timesbd.ttf"),
    ],
    "italic": [
        Path("C:/Windows/Fonts/georgiai.ttf"),
        Path("C:/Windows/Fonts/calibrii.ttf"),
        Path("C:/Windows/Fonts/timesi.ttf"),
    ],
}


@dataclass
class RenderIssue:
    card_id: str
    message: str


def ensure_output_dirs() -> None:
    for path in (
        CARD_ART_INCOMING_ROOT,
        CARD_ART_FINAL_ROOT,
        FRAME_ROOT,
        BACK_ROOT,
        CARD_FRONT_ROOT,
        ATLAS_FRONT_ROOT,
        ATLAS_BACK_ROOT,
        PRINT_ROOT,
    ):
        path.mkdir(parents=True, exist_ok=True)


def deck_slug(deck: str) -> str:
    return DECK_SLUGS.get(deck, slugify(deck))


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "unnamed"


def load_layout_spec() -> dict:
    text = LAYOUT_PATH.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- CARD_LAYOUT_SPEC_JSON_START -->\s*```json\s*(.*?)\s*```\s*<!-- CARD_LAYOUT_SPEC_JSON_END -->",
        text,
        re.DOTALL,
    )
    if not match:
        raise SystemExit(f"Could not find machine-readable layout spec in {LAYOUT_PATH}")
    return json.loads(match.group(1))


def iter_card_files() -> list[Path]:
    return sorted(
        path
        for path in CARD_ROOT.rglob("*.txt")
        if path.name.upper() != "TEMPLATE.TXT" and path.parent.name == "cards"
    )


def parse_card(path: Path) -> dict:
    fields: dict[str, str] = {}
    current_key: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("  ") and current_key:
            continuation = raw_line.strip()
            if continuation:
                fields[current_key] = f"{fields[current_key]}\n{continuation}".strip()
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        current_key = key.strip().lstrip("\ufeff")
        fields[current_key] = value.strip()
    fields["_path"] = str(path.relative_to(ROOT)).replace("\\", "/")
    fields["_source_path"] = str(path)
    fields["_kind"] = "defined"
    return fields


def load_cards() -> list[dict]:
    return [parse_card(path) for path in iter_card_files()]


def card_lookup_by_name(cards: list[dict]) -> dict[str, dict]:
    return {card.get("Display Name", ""): card for card in cards}


def layout_name_for_card(card: dict) -> str:
    if card.get("Deck") == "Utility" and card.get("Card Type") == "Class Reference":
        return "class_reference"
    deck = card.get("Deck", "")
    if deck in LAYOUT_BY_DECK:
        return LAYOUT_BY_DECK[deck]
    raise ValueError(f"No layout mapping for deck {deck!r} in {card.get('_path', card.get('Card ID', 'unknown'))}")


def card_size_px(card: dict) -> tuple[int, int]:
    layout_name = layout_name_for_card(card)
    if layout_name == "quest_reference":
        return QUEST_CARD_WIDTH_PX, QUEST_CARD_HEIGHT_PX
    if layout_name == "class_reference":
        return CLASS_CARD_WIDTH_PX, CLASS_CARD_HEIGHT_PX
    return CARD_WIDTH_PX, CARD_HEIGHT_PX


def card_front_path(card: dict) -> Path:
    card_id = card.get("Card ID") or slugify(card.get("Display Name", "unnamed"))
    return CARD_FRONT_ROOT / deck_slug(card.get("Deck", "Utility")) / f"{card_id}.png"


def card_art_path(card: dict) -> Path:
    card_id = card.get("Card ID") or slugify(card.get("Display Name", "unnamed"))
    return CARD_ART_FINAL_ROOT / deck_slug(card.get("Deck", "Utility")) / f"{card_id}.png"


def frame_path_for_layout(layout_name: str) -> Path:
    return FRAME_ROOT / f"{layout_name}.png"


def get_font(role: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES.get(role, []):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def text_bbox(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int, int, int]:
    return draw.textbbox((0, 0), text, font=font)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    left, top, right, bottom = text_bbox(draw, text, font)
    return right - left, bottom - top


def line_height(font: ImageFont.ImageFont, multiplier: float = 1.15) -> int:
    bbox = font.getbbox("Ag")
    return max(1, int((bbox[3] - bbox[1]) * multiplier))


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    text = text.strip()
    if not text:
        return []
    lines: list[str] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if text_size(draw, candidate, font)[0] <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
            if text_size(draw, word, font)[0] <= max_width:
                current = word
            else:
                split_lines = textwrap.wrap(word, width=max(4, len(word) // 2), break_long_words=True)
                lines.extend(split_lines[:-1])
                current = split_lines[-1] if split_lines else ""
        if current:
            lines.append(current)
    return lines


def _line_break_bonus(line: str, is_final: bool) -> int:
    if is_final:
        return 0
    stripped = line.rstrip("\"')")
    if stripped.endswith((".", "!", "?")):
        return -120
    if stripped.endswith((";", ":")):
        return -70
    if stripped.endswith(","):
        return -35
    return 45


def _balanced_wrap_paragraph(
    draw: ImageDraw.ImageDraw,
    paragraph: str,
    font: ImageFont.ImageFont,
    max_width: int,
    max_lines: int | None = None,
) -> list[str]:
    words = paragraph.split()
    if not words:
        return []
    greedy = wrap_text(draw, paragraph, font, max_width)
    if len(words) == 1:
        return greedy

    space_width = text_size(draw, " ", font)[0]
    word_widths = [text_size(draw, word, font)[0] for word in words]
    prefix = [0]
    for width in word_widths:
        prefix.append(prefix[-1] + width)

    def segment_width(start: int, end: int) -> int:
        spaces = max(0, end - start - 1) * space_width
        return prefix[end] - prefix[start] + spaces

    sentence_breaks = sum(1 for word in words if word.rstrip("\"')").endswith((".", "!", "?")))
    greedy_count = len(greedy)
    candidate_counts = {greedy_count}
    if greedy_count <= 3:
        candidate_counts.add(greedy_count + 1)
    if greedy_count == 1 and sentence_breaks:
        candidate_counts.update(range(2, min(3, sentence_breaks + 1, len(words)) + 1))
    if max_lines is not None:
        candidate_counts = {count for count in candidate_counts if count <= max_lines}
    candidate_counts = {count for count in candidate_counts if 1 <= count <= len(words)}
    if not candidate_counts:
        return greedy

    total_width = segment_width(0, len(words))
    best_score = float("inf")
    best_lines = greedy

    for line_count in sorted(candidate_counts):
        target_width = min(max_width * 0.88, max(max_width * 0.48, total_width / line_count))
        dp: list[dict[int, tuple[float, int]]] = [{0: (0.0, -1)}] + [dict() for _ in range(len(words))]
        for end in range(1, len(words) + 1):
            for start in range(end):
                width = segment_width(start, end)
                if width > max_width:
                    continue
                line = " ".join(words[start:end])
                for used_lines, (previous_score, _previous_start) in dp[start].items():
                    next_count = used_lines + 1
                    if next_count > line_count:
                        continue
                    is_final = next_count == line_count
                    width_delta = (width - target_width) / max(1, target_width)
                    short_last_penalty = 90 if is_final and line_count > 1 and width < target_width * 0.45 else 0
                    score = previous_score + width_delta * width_delta * 1000 + short_last_penalty
                    score += _line_break_bonus(line, is_final)
                    existing = dp[end].get(next_count)
                    if existing is None or score < existing[0]:
                        dp[end][next_count] = (score, start)
        if line_count not in dp[len(words)]:
            continue
        count_penalty = max(0, line_count - greedy_count) * 70
        if sentence_breaks and line_count == min(sentence_breaks + 1, 3):
            count_penalty -= 70
        score = dp[len(words)][line_count][0] + count_penalty
        if score >= best_score:
            continue
        breaks = []
        end = len(words)
        used = line_count
        while used:
            _score, start = dp[end][used]
            breaks.append((start, end))
            end = start
            used -= 1
        breaks.reverse()
        lines = [" ".join(words[start:end]) for start, end in breaks]
        best_score = score
        best_lines = lines
    return best_lines


def balanced_wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    max_width: int,
    max_lines: int | None = None,
) -> list[str]:
    text = text.strip()
    if not text:
        return []
    lines: list[str] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        lines.extend(_balanced_wrap_paragraph(draw, paragraph, font, max_width, max_lines))
    return lines


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    max_width: int,
    max_height: int,
    spacing: int = 2,
    align: str = "left",
) -> tuple[int, bool]:
    x, y = xy
    lines = wrap_text(draw, text, font, max_width)
    lh = line_height(font) + spacing
    max_lines = max(1, max_height // lh)
    clipped = len(lines) > max_lines
    lines = lines[:max_lines]
    for line in lines:
        width = text_size(draw, line, font)[0]
        draw_x = x
        if align == "center":
            draw_x = x + (max_width - width) // 2
        elif align == "right":
            draw_x = x + max_width - width
        draw.text((draw_x, y), line, font=font, fill=fill)
        y += lh
    return y, clipped


def fit_font_for_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    role: str,
    start_size: int,
    min_size: int,
    max_width: int,
    max_height: int,
) -> tuple[ImageFont.ImageFont, list[str], bool]:
    for size in range(start_size, min_size - 1, -1):
        font = get_font(role, size)
        lines = wrap_text(draw, text, font, max_width)
        height = len(lines) * (line_height(font) + 2)
        if height <= max_height:
            return font, lines, False
    font = get_font(role, min_size)
    return font, wrap_text(draw, text, font, max_width), True


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    spacing: int = 2,
) -> None:
    left, top, right, bottom = box
    width = right - left
    lh = line_height(font) + spacing
    total_height = len(lines) * lh
    y = top + max(0, (bottom - top - total_height) // 2)
    for line in lines:
        tw = text_size(draw, line, font)[0]
        draw.text((left + (width - tw) // 2, y), line, font=font, fill=fill)
        y += lh


def rounded_rect(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int] | None = None,
    outline: tuple[int, int, int] | None = None,
    width: int = 1,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_diamond_icon(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    radius: int,
    fill: tuple[int, int, int],
    outline: tuple[int, int, int],
) -> None:
    x, y = center
    points = [(x, y - radius), (x + radius, y), (x, y + radius), (x - radius, y)]
    draw.polygon(points, fill=fill)
    draw.line(points + [points[0]], fill=outline, width=max(1, radius // 5))


def crop_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    source_w, source_h = image.size
    scale = max(target_w / source_w, target_h / source_h)
    resized = image.resize((int(source_w * scale), int(source_h * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def draw_placeholder_art(
    size: tuple[int, int],
    card: dict,
    style: dict,
) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size, style["mid"])
    draw = ImageDraw.Draw(image)
    for y in range(height):
        blend = y / max(1, height - 1)
        color = tuple(int(style["mid"][i] * (1 - blend) + style["dark"][i] * blend) for i in range(3))
        draw.line((0, y, width, y), fill=color)
    for offset in range(-height, width, 34):
        draw.line((offset, height, offset + height, 0), fill=style["light"], width=1)
    draw.rectangle((8, 8, width - 9, height - 9), outline=style["light"], width=3)
    title_font, title_lines, _ = fit_font_for_text(
        draw,
        card.get("Display Name", "Art Pending"),
        "title",
        max(20, width // 9),
        12,
        width - 36,
        height // 2,
    )
    draw_centered_lines(draw, (18, 18, width - 18, height // 2), title_lines[:3], title_font, (255, 248, 225))
    pending_font = get_font("body_bold", max(12, width // 18))
    pending = "ART PENDING"
    tw, th = text_size(draw, pending, pending_font)
    rounded_rect(
        draw,
        ((width - tw) // 2 - 12, height - th - 34, (width + tw) // 2 + 12, height - 20),
        8,
        fill=style["dark"],
        outline=style["light"],
        width=2,
    )
    draw.text(((width - tw) // 2, height - th - 27), pending, font=pending_font, fill=(255, 245, 215))
    return image


def load_card_art(card: dict, size: tuple[int, int], style: dict) -> tuple[Image.Image, bool]:
    path = card_art_path(card)
    if path.exists():
        with Image.open(path) as source:
            return crop_cover(source.convert("RGB"), size), True
    return draw_placeholder_art(size, card, style), False


def printable_field_lines(card: dict, layout: dict) -> list[tuple[str, str, bool]]:
    lines: list[tuple[str, str, bool]] = []
    deck = card.get("Deck", "")
    if deck == "Quest Deck":
        stats = (
            f"{card.get('Player Count', '')}: "
            f"4P HP {card.get('Starting Party HP (4P)', '')}, hand {card.get('Starting Hand Size (4P)', '')}; "
            f"3P HP {card.get('Starting Party HP (3P)', '')}, hand {card.get('Starting Hand Size (3P)', '')}; "
            f"Esc {card.get('Escalation Track', '')}"
        )
        lines.append(("", stats, False))
    if deck == "Creature Deck":
        stats = []
        for key, label in (("Threat", "T"), ("Hit Points", "HP"), ("Attack", "ATK"), ("Treasure Value", "TV")):
            value = card.get(key, "")
            if value not in SKIP_VALUES:
                stats.append(f"{label} {value}")
        if stats:
            lines.append(("", " / ".join(stats), False))
    if deck == "Resource Deck":
        subtype = card.get("Subtype", "")
        tv = card.get("Treasure Value", "")
        pieces = [piece for piece in (subtype, f"TV {tv}" if tv not in SKIP_VALUES else "") if piece]
        if pieces:
            lines.append(("", " / ".join(pieces), False))
    if deck == "Encounter Deck":
        scene_tags = card.get("Scene Tags", "")
        if scene_tags not in SKIP_VALUES:
            lines.append(("Tags", scene_tags, False))

    for field in layout["printed_fields"]:
        if field == "Quest Stat Line":
            continue
        value = card.get(field, "")
        if value in SKIP_VALUES:
            continue
        label = FIELD_LABELS.get(field, field)
        lines.append((label, value, field == "Flavor Text"))
    return lines


def make_utility_card(card_id: str, name: str, subtype: str, text: str, art_brief: str = "", flavor_text: str = "") -> dict:
    return {
        "Card ID": card_id,
        "Display Name": name,
        "Deck": "Utility",
        "Card Type": subtype,
        "Subtype": subtype,
        "Rarity": "",
        "Copies In Deck": "1",
        "Treasure Value": "0",
        "Cost": "",
        "Timing": "",
        "Target": "",
        "Rules Text": text,
        "Flavor Text": flavor_text,
        "Art Brief": art_brief,
        "_path": "generated utility card",
        "_source_path": "",
        "_kind": "utility",
    }


def layout_boxes(card: dict, spec: dict) -> dict[str, tuple[int, int, int, int]]:
    layout_name = layout_name_for_card(card)
    layout = spec["layouts"][layout_name]
    width, height = card_size_px(card)
    scale = width / layout["card_width_in"]
    safe_margin = int((spec["card"]["cut_tolerance_in"] + spec["card"]["safe_margin_in"]) * scale)
    gutter = max(5, int(0.025 * scale))
    left = safe_margin
    right = width - safe_margin
    top = safe_margin
    bottom = height - safe_margin

    title_h = int(layout.get("title_box_in", 0.3) * scale)
    art_h = int(layout.get("art_box_in", 1.0) * scale)
    type_h = int(layout.get("type_line_box_in", 0.16) * scale)
    stats_h = int(layout.get("stats_box_in", 0.0) * scale)
    footer_h = int(layout.get("footer_box_in", 0.0) * scale)
    if card.get("Deck") == "Agenda Deck" or layout_name == "class_reference":
        footer_h = 0

    y = top
    title = (left, y, right, y + title_h)
    y += title_h + gutter
    art = (left, y, right, y + art_h)
    y += art_h + gutter
    type_line = (left, y, right, y + type_h)
    y += type_h + gutter
    stats = (left, y, right, y + stats_h) if stats_h else (left, y, right, y)
    if stats_h:
        y += stats_h + gutter
    footer = (left, bottom - footer_h, right, bottom) if footer_h else (left, bottom, right, bottom)
    body_bottom = footer[1] - gutter if footer_h else bottom
    body = (left, y, right, max(y + 10, body_bottom))

    return {
        "full": (0, 0, width, height),
        "safe": (left, top, right, bottom),
        "title": title,
        "art": art,
        "type": type_line,
        "stats": stats,
        "body": body,
        "footer": footer,
    }


def extract_class_reference_cards() -> list[dict]:
    text = QUICK_START_PATH.read_text(encoding="utf-8")
    cards: list[dict] = []
    class_flavor = {
        "Warrior": '"The first one through the smoke gets remembered."',
        "Wizard": '"Patience is a shield no blade can count."',
        "Cleric": '"Mercy is the hand that makes heroes possible."',
    }
    class_art_brief = {
        "Warrior": "A battle-scarred warrior plants a shield and sword in a smoke-filled dungeon breach, holding the line against silhouettes in furnace light.",
        "Wizard": "A calm wizard studies glowing blue-white runes over cracked stone, shaping smoke and ash into a precise defensive spell.",
        "Cleric": "A soot-streaked cleric raises a warm golden prayer over wounded allies beside a broken altar, mercy shining through black furnace smoke.",
    }
    for class_name in ("Warrior", "Wizard", "Cleric"):
        pattern = rf"### {class_name}\s*(.*?)(?=\n### |\n<div class=\"page-break\"></div>|$)"
        match = re.search(pattern, text, re.DOTALL)
        body = match.group(1).strip() if match else ""
        body = re.sub(r"\*\*(.*?)\*\*", r"\1", body)
        body = body.replace("`", "")
        body = re.sub(r"\n{3,}", "\n\n", body)
        body = body.replace("Class passives stack unless a card or quest says otherwise.", "").strip()
        body = body.replace("| Monster | Draw On |\n| --- | --- |\n", "Kill Reward Table:\n")
        body = re.sub(r"\| ([^|]+) \| `?([^|`]+)`? \|", r"- \1: \2", body)
        card = make_utility_card(
            f"class-{slugify(class_name)}",
            f"{class_name} Reference",
            "Class Reference",
            body,
            class_art_brief[class_name],
            class_flavor[class_name],
        )
        card["_path"] = str(QUICK_START_PATH.relative_to(ROOT)).replace("\\", "/")
        cards.append(card)
    return cards
