#!/usr/bin/env python3
"""Render individual Edition 0 printable card-front PNGs."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw

from card_rendering_common import (
    ART_HANDOFF_PATH,
    CARD_FRONT_ROOT,
    FRAME_ROOT,
    ROOT,
    SKIP_VALUES,
    RenderIssue,
    balanced_wrap_text,
    card_art_path,
    card_front_path,
    deck_slug,
    draw_centered_lines,
    draw_diamond_icon,
    draw_wrapped_text,
    ensure_output_dirs,
    extract_class_reference_cards,
    fit_font_for_text,
    frame_path_for_card,
    get_font,
    layout_boxes,
    layout_name_for_card,
    line_height,
    load_card_art,
    load_cards,
    load_layout_spec,
    make_utility_card,
    printable_field_lines,
    rounded_rect,
    style_for_card,
    text_size,
    wrap_text,
)


CLASS_REFERENCE_BODY_FONT_SIZE = 22
CLASS_REFERENCE_MIN_BODY_FONT_SIZE = 20
CLASS_REFERENCE_MAX_BODY_FONT_SIZE = 24
CLASS_TEXT_SIDE_PAD = 8
CLASS_TEXT_LINE_SPACING = 1.12
QUEST_TEXT_SIDE_PAD = 12
QUEST_TEXT_LINE_SPACING = 1.12
ART_GROUP_ROOT = ART_HANDOFF_PATH.parent / "session-groups"
ART_GROUP_INDEX_PATH = ART_HANDOFF_PATH.parent / "AI_ART_SESSION_GROUPS.md"


def utility_cards() -> list[dict]:
    return [
        make_utility_card(
            "proxy-blank",
            "Blank Proxy",
            "Proxy",
            "Write a temporary card name here when a physical copy is missing.",
            "No AI art needed. Plain proxy card.",
        ),
        make_utility_card(
            "proxy-encounter-divider",
            "Encounter Proxy / Divider",
            "Divider",
            "Use as a spare encounter proxy or as a divider between random encounters and scripted ordeals.",
            "No AI art needed. Divider card.",
        ),
        make_utility_card(
            "proxy-creature-blank",
            "Creature Proxy Blank",
            "Proxy",
            "Write a creature, artifact, enchantment, or summon name here when a physical copy is missing.",
            "No AI art needed. Creature proxy card.",
        ),
    ]


def art_box_image(card: dict, box: tuple[int, int, int, int], style: dict) -> tuple[Image.Image, bool]:
    width = box[2] - box[0]
    height = box[3] - box[1]
    return load_card_art(card, (width, height), style)


def draw_title(draw: ImageDraw.ImageDraw, card: dict, box: tuple[int, int, int, int], style: dict, issues: list[RenderIssue]) -> None:
    left, top, right, bottom = box
    width = right - left
    title = card.get("Display Name", "Unnamed")
    font, lines, clipped = fit_font_for_text(draw, title, "title", 38 if width < 800 else 40, 22, width - 26, bottom - top - 12)
    if clipped or len(lines) > 2:
        issues.append(RenderIssue(card.get("Card ID", title), "Title needed minimum font or clipped."))
    draw_centered_lines(draw, (left + 12, top + 3, right - 12, bottom - 3), lines[:2], font, style["ink"], spacing=0)


def type_line(card: dict) -> str:
    deck = card.get("Deck", "")
    if deck == "Creature Deck":
        pieces = [card.get("Card Type", ""), card.get("Subtype", ""), card.get("Creature Type", ""), card.get("Rarity", "")]
    elif deck == "Encounter Deck":
        pieces = [card.get("Card Type", ""), card.get("Encounter Class", ""), card.get("Escalation Use", "")]
    elif deck == "Quest Deck":
        pieces = [card.get("Card Type", ""), card.get("Theme", "")]
    elif deck == "Agenda Deck":
        return agenda_reward_line(card)
    else:
        pieces = [card.get("Card Type", ""), card.get("Subtype", ""), card.get("Rarity", "")]
    return " - ".join(piece for piece in pieces if piece not in SKIP_VALUES)


def agenda_reward_line(card: dict) -> str:
    reward = card.get("Reward Text", "")
    match = re.search(r"Gain\s+(\d+)\s+prestige points?", reward, re.IGNORECASE)
    if match:
        return f"{match.group(1)} Prestige Points"
    return reward or "Secret Agenda"


def stat_line(card: dict) -> str:
    deck = card.get("Deck", "")
    if deck == "Creature Deck":
        stats = []
        for key, label in (("Hit Points", "HP"), ("Attack", "ATK")):
            value = card.get(key, "")
            if value not in SKIP_VALUES:
                stats.append(f"{label} {value}")
        return "   ".join(stats)
    if deck == "Resource Deck":
        stats = []
        for key in ("Cost", "Timing", "Target"):
            value = card.get(key, "")
            if value not in SKIP_VALUES:
                stats.append(f"{key}: {value}")
        return "   ".join(stats)
    return ""


def body_text(card: dict, layout: dict) -> str:
    lines = []
    for label, value, is_flavor in printable_field_lines(card, layout):
        if label == "" and card.get("Deck") != "Quest Deck":
            continue
        if card.get("Deck") == "Agenda Deck" and label == "Reward":
            continue
        if is_flavor:
            lines.append(f'"{value}"')
        elif label == "Text":
            lines.append(value)
        elif label:
            lines.append(f"{label}: {value}")
        else:
            lines.append(value)
    return "\n".join(lines)


def body_text_parts(card: dict, layout: dict) -> tuple[str, str]:
    main_lines = []
    flavor_lines = []
    for label, value, is_flavor in printable_field_lines(card, layout):
        if label == "" and card.get("Deck") != "Quest Deck":
            continue
        if card.get("Deck") == "Agenda Deck" and label == "Reward":
            continue
        if card.get("Deck") == "Agenda Deck" and label == "Fail" and value.strip().lower() == "gain 0 prestige points.":
            continue
        if is_flavor:
            flavor_lines.append(f'"{value}"')
        elif label == "Text":
            main_lines.append(value)
        elif label:
            main_lines.append(f"{label}: {value}")
        else:
            main_lines.append(value)
    return "\n".join(main_lines), "\n".join(flavor_lines)


def flavor_text_color(style: dict) -> tuple[int, int, int]:
    return tuple(int(style["ink"][index] * 0.55 + 132 * 0.45) for index in range(3))


def label_text_bbox(draw: ImageDraw.ImageDraw, text: str, font) -> tuple[int, int, int, int]:
    return draw.textbbox((0, 0), text, font=font)


def label_pill_size(draw: ImageDraw.ImageDraw, text: str, font, pad_x: int, pad_y: int) -> tuple[int, int]:
    text_left, text_top, text_right, text_bottom = label_text_bbox(draw, text, font)
    return text_right - text_left + pad_x * 2, text_bottom - text_top + pad_y * 2


def draw_label_pill(
    draw: ImageDraw.ImageDraw,
    left: int,
    top: int,
    text: str,
    font,
    style: dict,
    pad_x: int = 14,
    pad_y: int = 7,
    radius: int = 7,
    outline_width: int = 2,
) -> tuple[int, int, int, int]:
    width, height = label_pill_size(draw, text, font, pad_x, pad_y)
    box = (left, top, left + width, top + height)
    rounded_rect(draw, box, radius, fill=style["light"], outline=style["dark"], width=outline_width)
    text_left, text_top, text_right, text_bottom = label_text_bbox(draw, text, font)
    text_width = text_right - text_left
    text_height = text_bottom - text_top
    text_x = left + max(0, (width - text_width) // 2) - text_left
    text_y = top + max(0, (height - text_height) // 2) - text_top
    draw.text((text_x, text_y), text, font=font, fill=style["ink"])
    return box


def draw_aligned_line(
    draw: ImageDraw.ImageDraw,
    text: str,
    left: int,
    y: int,
    max_width: int,
    font,
    fill: tuple[int, int, int],
    align: str = "left",
) -> None:
    line_width = text_size(draw, text, font)[0]
    x = left
    if align == "center":
        x = left + max(0, (max_width - line_width) // 2)
    elif align == "right":
        x = left + max(0, max_width - line_width)
    draw.text((x, y), text, font=font, fill=fill)


def wrapped_text_sections(
    draw: ImageDraw.ImageDraw,
    text: str,
    font,
    max_width: int,
) -> list[list[str]]:
    sections: list[list[str]] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        sections.append(wrap_text(draw, paragraph, font, max_width))
    return sections


def section_text_height(sections: list[list[str]], text_line_height: int, paragraph_gap: int) -> int:
    if not sections:
        return 0
    return sum(len(section) * text_line_height for section in sections) + paragraph_gap * (len(sections) - 1)


def largest_paragraph_gap_that_fits(
    sections: list[list[str]],
    text_line_height: int,
    available_height: int,
    minimum_gap: int,
) -> int:
    gap_count = max(0, len(sections) - 1)
    if gap_count == 0:
        return minimum_gap
    line_height_total = sum(len(section) * text_line_height for section in sections)
    return max(minimum_gap, (available_height - line_height_total) // gap_count)


def fit_sectioned_body_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    role: str,
    start_size: int,
    min_size: int,
    max_width: int,
    max_height: int,
    paragraph_gap: int,
):
    for size in range(start_size, min_size - 1, -1):
        font = get_font(role, size)
        text_line_height = max(1, line_height(font, 1.02) + 1)
        sections = wrapped_text_sections(draw, text, font, max_width)
        if section_text_height(sections, text_line_height, paragraph_gap) <= max_height:
            return font, sections, False
    font = get_font(role, min_size)
    return font, wrapped_text_sections(draw, text, font, max_width), True


def draw_body_with_bottom_flavor(
    draw: ImageDraw.ImageDraw,
    card: dict,
    layout: dict,
    body_box: tuple[int, int, int, int],
    style: dict,
    issues: list[RenderIssue],
) -> None:
    main_text, flavor_text = body_text_parts(card, layout)
    combined = "\n".join(part for part in (main_text, flavor_text) if part)
    body_font, _, body_clipped = fit_font_for_text(
        draw,
        combined,
        "body_bold",
        int(layout["body_font_pt"] * 288 / 72) + 2,
        12,
        body_box[2] - body_box[0] - 22,
        body_box[3] - body_box[1] - 18,
    )
    if body_clipped:
        issues.append(RenderIssue(card.get("Card ID", ""), "Rules text needed minimum font or may clip."))

    left = body_box[0] + 11
    top = body_box[1] + 9
    right = body_box[2] - 11
    bottom = body_box[3] - 9
    max_width = right - left

    flavor_lines: list[str] = []
    flavor_font = get_font("italic", max(12, getattr(body_font, "size", 18) - 1))
    flavor_height = 0
    flavor_gap = 8 if flavor_text else 0
    if flavor_text:
        flavor_lines = balanced_wrap_text(draw, flavor_text, flavor_font, max_width)
        flavor_lh = max(1, line_height(flavor_font, 1.02) + 1)
        flavor_height = len(flavor_lines) * flavor_lh
        flavor_top = bottom - flavor_height
        for line in flavor_lines:
            draw_aligned_line(draw, line, left, flavor_top, max_width, flavor_font, flavor_text_color(style), "center")
            flavor_top += flavor_lh

    main_bottom = bottom - flavor_height - flavor_gap
    paragraph_gap_multiplier = 0.46 if card.get("Deck") in {"Agenda Deck", "Encounter Deck"} else 0.28
    paragraph_gap = max(5, int(getattr(body_font, "size", 18) * paragraph_gap_multiplier))
    body_font, main_sections, body_clipped = fit_sectioned_body_font(
        draw,
        main_text,
        "body_bold",
        getattr(body_font, "size", int(layout["body_font_pt"] * 288 / 72) + 2),
        12,
        max_width,
        main_bottom - top,
        paragraph_gap,
    )
    if body_clipped:
        issues.append(RenderIssue(card.get("Card ID", ""), "Rules text needed minimum font or may clip with paragraph spacing."))
    body_line_height = max(1, line_height(body_font, 1.02) + 1)
    y = top
    clipped = False
    for section_index, section in enumerate(main_sections):
        for line in section:
            if y + body_line_height > main_bottom:
                issues.append(RenderIssue(card.get("Card ID", ""), "Rules text clipped above bottom-aligned flavor text."))
                clipped = True
                break
            draw.text((left, y), line, font=body_font, fill=style["ink"])
            y += body_line_height
        if clipped:
            break
        if section_index < len(main_sections) - 1:
            y += paragraph_gap


def quest_stats_text(card: dict) -> str:
    return (
        f"{card.get('Player Count', '')} players  |  "
        f"4P: {card.get('Starting Party HP (4P)', '')} HP, hand {card.get('Starting Hand Size (4P)', '')}  |  "
        f"3P: {card.get('Starting Party HP (3P)', '')} HP, hand {card.get('Starting Hand Size (3P)', '')}  |  "
        f"Escalation {card.get('Escalation Track', '')}"
    )


def quest_panel_text(card: dict, panel: str) -> str:
    if panel == "setup":
        parts = [
            card.get("Setup Text", ""),
            card.get("Rules Text", ""),
        ]
        return "\n".join(part for part in parts if part not in SKIP_VALUES)
    if panel == "escalation":
        parts = [
            f"Rule: {card.get('Ongoing Quest Rule', '')}",
            f"Esc 5: {card.get('Threshold 5', '')}",
            f"Esc 8: {card.get('Threshold 8', '')}",
            f"Esc 10: {card.get('Threshold 10', '')}",
        ]
        return "\n".join(part for part in parts if part.split(": ", 1)[-1] not in SKIP_VALUES)
    if panel == "win":
        parts = [card.get("Win Condition", "")]
        flavor = card.get("Flavor Text", "")
        if flavor not in SKIP_VALUES:
            parts.append(f'"{flavor}"')
        return "\n".join(part for part in parts if part not in SKIP_VALUES)
    if panel == "lose":
        return card.get("Lose Condition", "")
    return ""


def draw_quest_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    heading: str,
    text: str,
    style: dict,
    issues: list[RenderIssue],
    card_id: str,
    start_size: int,
    min_size: int = 18,
) -> None:
    left, top, right, bottom = box
    rounded_rect(draw, box, 10, fill=style["paper"], outline=style["dark"], width=3)
    heading_font = get_font("body_bold", 29)
    heading_box = draw_label_pill(draw, left + 12, top + 10, heading, heading_font, style, pad_x=10, pad_y=8)

    text_left = left + QUEST_TEXT_SIDE_PAD
    text_top = heading_box[3] + 10
    text_width = right - left - QUEST_TEXT_SIDE_PAD * 2
    text_height = bottom - text_top - 12
    raw_lines = text.splitlines()
    flavor_lines_raw = [line for line in raw_lines if line.startswith('"') and line.endswith('"')]
    main_text = "\n".join(line for line in raw_lines if line not in flavor_lines_raw)
    flavor_text = "\n".join(flavor_lines_raw)

    clipped = True
    for size in range(start_size, min_size - 1, -1):
        body_font = get_font("body_bold", size)
        lh = line_height(body_font, QUEST_TEXT_LINE_SPACING) + 2
        minimum_paragraph_gap = max(8, int(size * 0.3))
        paragraph_gap = minimum_paragraph_gap
        main_sections = wrapped_text_sections(draw, main_text, body_font, text_width)
        flavor_font = get_font("italic", max(min_size, size - 1))
        wrapped_flavor = balanced_wrap_text(draw, flavor_text, flavor_font, text_width) if flavor_text else []
        flavor_lh = line_height(flavor_font, QUEST_TEXT_LINE_SPACING) + 2
        flavor_height = len(wrapped_flavor) * flavor_lh
        flavor_gap = max(8, int(size * 0.32)) if flavor_text else 0
        available_main_height = bottom - 10 - flavor_height - flavor_gap - text_top
        main_height = section_text_height(main_sections, lh, minimum_paragraph_gap)
        if main_height + flavor_gap + flavor_height <= text_height:
            paragraph_gap = largest_paragraph_gap_that_fits(
                main_sections,
                lh,
                available_main_height,
                minimum_paragraph_gap,
            )
            clipped = False
            break
    if clipped:
        issues.append(RenderIssue(card_id, f"{heading} panel reached minimum font or may clip."))

    if flavor_text:
        flavor_y = bottom - 10 - flavor_height
        for line in wrapped_flavor:
            draw_aligned_line(draw, line, text_left, flavor_y, text_width, flavor_font, flavor_text_color(style), "center")
            flavor_y += flavor_lh
    main_bottom = bottom - 10 - flavor_height - flavor_gap
    y = text_top
    for section_index, section in enumerate(main_sections):
        for line in section:
            if y + lh > bottom - 8:
                issues.append(RenderIssue(card_id, f"{heading} panel text clipped."))
                break
            if y + lh > main_bottom:
                issues.append(RenderIssue(card_id, f"{heading} panel text clipped above bottom-aligned flavor text."))
                break
            draw.text((text_left, y), line, font=body_font, fill=style["ink"])
            y += lh
        if section_index < len(main_sections) - 1:
            y += paragraph_gap


def draw_quest_card(card: dict, spec: dict) -> tuple[Image.Image, list[RenderIssue]]:
    issues: list[RenderIssue] = []
    layout_name = layout_name_for_card(card)
    layout = spec["layouts"][layout_name]
    style = style_for_card(card)
    frame_path = frame_path_for_card(card, layout_name)
    if not frame_path.exists():
        frame_path = FRAME_ROOT / f"{layout_name}.png"
    if frame_path.exists():
        image = Image.open(frame_path).convert("RGB")
    else:
        image = Image.new("RGB", (int(layout["card_width_in"] * 288), int(layout["card_height_in"] * 288)), style["dark"])
    draw = ImageDraw.Draw(image)
    boxes = layout_boxes(card, spec)
    card_id = card.get("Card ID", card.get("Display Name", ""))

    draw_title(draw, card, boxes["title"], style, issues)

    art, found_art = art_box_image(card, boxes["art"], style)
    image.paste(art, boxes["art"][:2])
    draw.rectangle(boxes["art"], outline=(18, 16, 14), width=5)
    if not found_art and card.get("_kind") == "defined":
        issues.append(RenderIssue(card_id, f"Missing art at {card_art_path(card)}"))

    type_font, type_lines, type_clipped = fit_font_for_text(
        draw,
        type_line(card),
        "body_bold",
        28,
        18,
        boxes["type"][2] - boxes["type"][0] - 24,
        boxes["type"][3] - boxes["type"][1] - 6,
    )
    draw_centered_lines(
        draw,
        (boxes["type"][0] + 12, boxes["type"][1] + 3, boxes["type"][2] - 12, boxes["type"][3] - 3),
        type_lines[:2],
        type_font,
        style["ink"],
        spacing=0,
    )
    if type_clipped:
        issues.append(RenderIssue(card_id, "Quest type line reached minimum font."))

    body_left, body_top, body_right, body_bottom = boxes["body"]
    gutter = 12
    stats_h = 118
    setup_h = 248
    escalation_h = 430
    bottom_h = body_bottom - body_top - stats_h - setup_h - escalation_h - gutter * 3
    bottom_h = max(190, bottom_h)
    y = body_top
    stats_box = (body_left, y, body_right, y + stats_h)
    y += stats_h + gutter
    setup_box = (body_left, y, body_right, y + setup_h)
    y += setup_h + gutter
    escalation_box = (body_left, y, body_right, y + escalation_h)
    y += escalation_h + gutter
    half_gap = gutter // 2
    mid = (body_left + body_right) // 2
    win_box = (body_left, y, mid - half_gap, body_bottom)
    lose_box = (mid + half_gap, y, body_right, body_bottom)

    draw_quest_panel(draw, stats_box, "Stats", quest_stats_text(card), style, issues, card_id, 34, 20)
    draw_quest_panel(draw, setup_box, "Setup", quest_panel_text(card, "setup"), style, issues, card_id, 32, 19)
    draw_quest_panel(draw, escalation_box, "Escalation", quest_panel_text(card, "escalation"), style, issues, card_id, 31, 17)
    draw_quest_panel(draw, win_box, "Win", quest_panel_text(card, "win"), style, issues, card_id, 31, 17)
    draw_quest_panel(draw, lose_box, "Lose", quest_panel_text(card, "lose"), style, issues, card_id, 31, 18)
    return image, issues


def split_class_heading(heading: str) -> tuple[str, str]:
    if ":" not in heading:
        return heading, ""
    label, title = heading.split(":", 1)
    return label.strip(), title.strip()


def split_class_reference_text(text: str) -> tuple[tuple[str, str, str], tuple[str, str, str]]:
    lines = [line.rstrip() for line in text.splitlines()]
    sections: list[tuple[str, list[str]]] = []
    current_heading = "Rules"
    current_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped in {"Active", "Passive"} or stripped.startswith("Passive:") or stripped.startswith("Active:"):
            if current_lines or current_heading != "Rules":
                sections.append((current_heading, current_lines))
            current_heading = stripped
            current_lines = []
            continue
        current_lines.append(line)
    sections.append((current_heading, current_lines))

    passive = ("Passive", "", "")
    active = ("Active", "", "")
    for heading, body_lines in sections:
        body = "\n".join(body_lines).strip()
        label, title = split_class_heading(heading)
        if label == "Passive":
            passive = (label, title, body)
        elif label == "Active":
            active = (label, title, body)
    return passive, active


def class_section_line_count(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> int:
    return sum(len(section) for section in wrapped_text_sections(draw, text, font, max_width))


def class_panel_text_metrics(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> tuple[int, list[list[str]], int, int]:
    sections = wrapped_text_sections(draw, text, font, max_width)
    text_line_height = max(1, line_height(font, CLASS_TEXT_LINE_SPACING) + 2)
    paragraph_gap = max(7, int(getattr(font, "size", CLASS_REFERENCE_BODY_FONT_SIZE) * 0.42))
    return section_text_height(sections, text_line_height, paragraph_gap), sections, text_line_height, paragraph_gap


def class_reference_body_font(draw: ImageDraw.ImageDraw, spec: dict) -> object:
    heading_font = get_font("body_bold", 22)
    _, heading_h = label_pill_size(draw, "Passive: Kill Reward", heading_font, 14, 7)
    for size in range(CLASS_REFERENCE_MAX_BODY_FONT_SIZE, CLASS_REFERENCE_MIN_BODY_FONT_SIZE - 1, -1):
        font = get_font("body_bold", size)
        fits = True
        for card in extract_class_reference_cards():
            boxes = layout_boxes(card, spec)
            body_left, body_top, body_right, body_bottom = boxes["body"]
            panel_gap = 9
            flavor_gap = 6
            flavor_h = 42 if card.get("Flavor Text", "") not in SKIP_VALUES else 0
            panels_bottom = body_bottom - flavor_h - (flavor_gap if flavor_h else 0)
            available_h = panels_bottom - body_top - panel_gap
            panel_h = max(80, available_h // 2)
            max_width = body_right - body_left - CLASS_TEXT_SIDE_PAD * 2
            max_height = panel_h - (8 + heading_h + 9) - 10
            passive, active = split_class_reference_text(card.get("Rules Text", ""))
            for _, _, text in (passive, active):
                height, _, _, _ = class_panel_text_metrics(draw, text, font, max_width)
                if height > max_height:
                    fits = False
                    break
            if not fits:
                break
        if fits:
            return font
    return get_font("body_bold", CLASS_REFERENCE_MIN_BODY_FONT_SIZE)


def draw_class_section_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    label: str,
    title: str,
    text: str,
    style: dict,
    font,
    issues: list[RenderIssue],
    card_id: str,
) -> None:
    left, top, right, bottom = box
    rounded_rect(draw, box, 8, fill=style["paper"], outline=style["dark"], width=3)
    heading_font = get_font("body_bold", 22)
    heading_box = draw_label_pill(draw, left + 9, top + 8, label, heading_font, style, pad_x=14, pad_y=7, radius=6)
    if title:
        title_font = get_font("body_bold", 28)
        title_box = (left + 12, heading_box[1], right - 12, heading_box[3])
        title_fill = tuple(int(style["ink"][index] * 0.72 + 120 * 0.28) for index in range(3))
        title_left, title_top, title_right, title_bottom = label_text_bbox(draw, title, title_font)
        title_width = title_right - title_left
        title_height = title_bottom - title_top
        title_x = title_box[0] + max(0, (title_box[2] - title_box[0] - title_width) // 2) - title_left
        title_y = title_box[1] + max(0, (title_box[3] - title_box[1] - title_height) // 2) - title_top
        draw.text((title_x, title_y), title, font=title_font, fill=title_fill)

    text_left = left + CLASS_TEXT_SIDE_PAD
    text_top = heading_box[3] + 9
    max_width = right - left - CLASS_TEXT_SIDE_PAD * 2
    max_height = bottom - text_top - 10
    height, sections, text_line_height, paragraph_gap = class_panel_text_metrics(draw, text, font, max_width)
    if height > max_height:
        issues.append(RenderIssue(card_id, f"{label} class panel text does not fit at the shared class font size."))
    y = text_top
    clipped = False
    for section_index, section in enumerate(sections):
        for line in section:
            if y + text_line_height > bottom - 8:
                clipped = True
                break
            draw.text((text_left, y), line, font=font, fill=style["ink"])
            y += text_line_height
        if clipped:
            break
        if section_index < len(sections) - 1:
            y += paragraph_gap


def draw_class_flavor_footer(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    style: dict,
) -> None:
    if text in SKIP_VALUES:
        return
    left, top, right, bottom = box
    width = right - left - 24
    font = get_font("italic", 20)
    lines = balanced_wrap_text(draw, text, font, width, max_lines=2)
    line_h = line_height(font, 1.0) + 2
    total_h = len(lines) * line_h
    y = top + max(0, (bottom - top - total_h) // 2)
    for line in lines:
        draw_aligned_line(draw, line, left + 12, y, width, font, flavor_text_color(style), "center")
        y += line_h


def draw_class_reference_card(card: dict, spec: dict) -> tuple[Image.Image, list[RenderIssue]]:
    issues: list[RenderIssue] = []
    layout_name = layout_name_for_card(card)
    layout = spec["layouts"][layout_name]
    style = style_for_card(card)
    frame_path = frame_path_for_card(card, layout_name)
    if not frame_path.exists():
        frame_path = FRAME_ROOT / f"{layout_name}.png"
    if frame_path.exists():
        image = Image.open(frame_path).convert("RGB")
    else:
        image = Image.new("RGB", (int(layout["card_width_in"] * 288), int(layout["card_height_in"] * 288)), style["dark"])
    draw = ImageDraw.Draw(image)
    boxes = layout_boxes(card, spec)
    card_id = card.get("Card ID", card.get("Display Name", ""))

    draw_title(draw, card, boxes["title"], style, issues)
    art, found_art = art_box_image(card, boxes["art"], style)
    image.paste(art, boxes["art"][:2])
    draw.rectangle(boxes["art"], outline=(18, 16, 14), width=4)
    if not found_art:
        issues.append(RenderIssue(card_id, f"Missing art at {card_art_path(card)}"))

    body_box = boxes["body"]
    passive, active = split_class_reference_text(card.get("Rules Text", ""))
    font = class_reference_body_font(draw, spec)
    body_left, body_top, body_right, body_bottom = body_box
    panel_gap = 9
    flavor_gap = 6
    flavor_h = 42 if card.get("Flavor Text", "") not in SKIP_VALUES else 0
    panels_bottom = body_bottom - flavor_h - (flavor_gap if flavor_h else 0)
    available_h = panels_bottom - body_top - panel_gap
    panel_h = max(80, available_h // 2)
    passive_box = (body_left, body_top, body_right, body_top + panel_h)
    active_box = (body_left, body_top + panel_h + panel_gap, body_right, body_top + panel_h * 2 + panel_gap)
    draw_class_section_panel(draw, passive_box, passive[0], passive[1], passive[2], style, font, issues, card_id)
    draw_class_section_panel(draw, active_box, active[0], active[1], active[2], style, font, issues, card_id)
    if flavor_h:
        flavor_box = (body_left, body_bottom - flavor_h, body_right, body_bottom)
        draw_class_flavor_footer(draw, flavor_box, card.get("Flavor Text", ""), style)
    return image, issues


def draw_treasure_chest(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    size: int,
    fill: tuple[int, int, int],
    outline: tuple[int, int, int],
) -> None:
    x, y = xy
    width = size
    height = max(10, int(size * 0.72))
    lid_h = max(5, height // 3)
    body_top = y + lid_h
    draw.rounded_rectangle((x, y, x + width, body_top + 3), radius=4, fill=fill, outline=outline, width=2)
    draw.rectangle((x, body_top, x + width, y + height), fill=fill, outline=outline, width=2)
    draw.line((x + 4, body_top, x + width - 4, body_top), fill=outline, width=2)
    band_x = x + width // 2 - max(2, width // 12)
    draw.rectangle((band_x, y + 2, band_x + max(4, width // 6), y + height - 2), fill=(220, 179, 70), outline=outline)
    lock_w = max(5, width // 5)
    lock_h = max(4, height // 5)
    draw.rectangle((x + width // 2 - lock_w // 2, body_top + 2, x + width // 2 + lock_w // 2, body_top + lock_h + 2), fill=(245, 214, 94), outline=outline)


def draw_skull_icon(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    size: int,
    fill: tuple[int, int, int],
    outline: tuple[int, int, int],
) -> None:
    x, y = center
    radius = size // 2
    head = (x - radius, y - radius, x + radius, y + radius)
    jaw = (x - radius // 2, y + radius // 3, x + radius // 2, y + radius + radius // 2)
    draw.ellipse(head, fill=fill, outline=outline, width=2)
    draw.rounded_rectangle(jaw, radius=max(2, size // 8), fill=fill, outline=outline, width=2)
    eye_r = max(2, size // 8)
    draw.ellipse((x - radius // 2 - eye_r, y - eye_r, x - radius // 2 + eye_r, y + eye_r), fill=outline)
    draw.ellipse((x + radius // 2 - eye_r, y - eye_r, x + radius // 2 + eye_r, y + eye_r), fill=outline)
    nose = [(x, y + eye_r), (x - eye_r, y + radius // 3), (x + eye_r, y + radius // 3)]
    draw.polygon(nose, fill=outline)
    for offset in (-size // 6, 0, size // 6):
        draw.line((x + offset, y + radius // 2, x + offset, y + radius), fill=outline, width=1)


def draw_creature_stat_band(
    draw: ImageDraw.ImageDraw,
    card: dict,
    box: tuple[int, int, int, int],
    style: dict,
) -> None:
    left, top, right, bottom = box
    font = get_font("body_bold", 22)
    stats = stat_line(card)
    stat_width, stat_height = text_size(draw, stats, font)
    try:
        threat_count = max(0, int(card.get("Threat", "0")))
    except ValueError:
        threat_count = 0
    icon_size = min(18, max(12, bottom - top - 24))
    icon_step = icon_size + 5
    icons_width = threat_count * icon_step - 5 if threat_count else 0
    gap = 12 if threat_count and stats else 0
    total_width = icons_width + gap + stat_width
    x = left + max(8, (right - left - total_width) // 2)
    center_y = top + (bottom - top) // 2 - 2
    for index in range(threat_count):
        draw_skull_icon(draw, (x + icon_size // 2 + index * icon_step, center_y), icon_size, style["accent"], style["dark"])
    draw.text((x + icons_width + gap, top + max(2, (bottom - top - stat_height) // 2 - 1)), stats, font=font, fill=style["ink"])


def draw_footer(draw: ImageDraw.ImageDraw, card: dict, box: tuple[int, int, int, int], style: dict) -> None:
    if card.get("Deck") == "Agenda Deck":
        return
    if box[3] <= box[1]:
        return
    left, top, right, bottom = box
    footer_font = get_font("body_bold", 18)
    treasure_value = card.get("Treasure Value", "")
    text = f"Treasure Value {treasure_value}" if treasure_value not in SKIP_VALUES else "Treasure Value 0"
    text_width, text_height = text_size(draw, text, footer_font)
    icon_size = min(28, max(18, bottom - top - 13))
    total_width = icon_size + 9 + text_width
    x = left + max(8, (right - left - total_width) // 2)
    icon_y = top + max(3, (bottom - top - int(icon_size * 0.72)) // 2)
    draw_treasure_chest(draw, (x, icon_y), icon_size, style["accent"], style["dark"])
    draw.text((x + icon_size + 9, top + max(2, (bottom - top - text_height) // 2 - 1)), text, font=footer_font, fill=style["ink"])


def draw_card(card: dict, spec: dict) -> tuple[Image.Image, list[RenderIssue]]:
    if card.get("Deck") == "Quest Deck":
        return draw_quest_card(card, spec)
    if card.get("Deck") == "Utility" and card.get("Card Type") == "Class Reference":
        return draw_class_reference_card(card, spec)

    issues: list[RenderIssue] = []
    layout_name = layout_name_for_card(card)
    layout = spec["layouts"][layout_name]
    style = style_for_card(card)
    frame_path = frame_path_for_card(card, layout_name)
    if not frame_path.exists():
        frame_path = FRAME_ROOT / f"{layout_name}.png"
    if frame_path.exists():
        image = Image.open(frame_path).convert("RGB")
    else:
        width, height = (layout["card_width_in"], layout["card_height_in"])
        image = Image.new("RGB", (int(width * 288), int(height * 288)), style["dark"])
    draw = ImageDraw.Draw(image)
    boxes = layout_boxes(card, spec)

    draw_title(draw, card, boxes["title"], style, issues)

    art, found_art = art_box_image(card, boxes["art"], style)
    image.paste(art, boxes["art"][:2])
    draw.rectangle(boxes["art"], outline=(18, 16, 14), width=4)
    if not found_art and card.get("_kind") == "defined":
        issues.append(RenderIssue(card.get("Card ID", card.get("Display Name", "")), f"Missing art at {card_art_path(card)}"))

    type_font, type_lines, type_clipped = fit_font_for_text(draw, type_line(card), "body_bold", 21, 14, boxes["type"][2] - boxes["type"][0] - 20, boxes["type"][3] - boxes["type"][1] - 4)
    draw_centered_lines(draw, (boxes["type"][0] + 10, boxes["type"][1] + 2, boxes["type"][2] - 10, boxes["type"][3] - 2), type_lines[:2], type_font, style["ink"], spacing=0)
    if type_clipped:
        issues.append(RenderIssue(card.get("Card ID", ""), "Type line reached minimum font."))

    stats = stat_line(card)
    if stats:
        target_box = boxes["stats"] if boxes["stats"][3] > boxes["stats"][1] else boxes["type"]
        if card.get("Deck") == "Creature Deck" and boxes["stats"][3] > boxes["stats"][1]:
            draw_creature_stat_band(draw, card, target_box, style)
        else:
            stat_font, stat_lines, stat_clipped = fit_font_for_text(draw, stats, "body_bold", 22, 14, target_box[2] - target_box[0] - 24, target_box[3] - target_box[1] - 4)
            if boxes["stats"][3] > boxes["stats"][1]:
                draw_centered_lines(draw, (target_box[0] + 12, target_box[1] + 2, target_box[2] - 12, target_box[3] - 2), stat_lines[:2], stat_font, style["ink"], spacing=0)
            else:
                draw_diamond_icon(draw, (target_box[0] + 18, (target_box[1] + target_box[3]) // 2), 7, style["accent"], style["dark"])
            if stat_clipped:
                issues.append(RenderIssue(card.get("Card ID", ""), "Stat line reached minimum font."))

    body_box = boxes["body"]
    draw_body_with_bottom_flavor(draw, card, layout, body_box, style, issues)

    draw_footer(draw, card, boxes["footer"], style)
    return image, issues


def art_window_info(card: dict, spec: dict) -> tuple[str, str, str, str]:
    boxes = layout_boxes(card, spec)
    art_box = boxes["art"]
    width = art_box[2] - art_box[0]
    height = art_box[3] - art_box[1]
    ratio = width / height
    divisor = math.gcd(width, height)
    exact_ratio = f"{width // divisor}:{height // divisor} ({ratio:.3f}:1)"
    scale = max(1, min(4, 2200 // width))
    exact_size = f"{width * scale}x{height * scale}"
    if ratio >= 1.9:
        fallback = "3:1 wide landscape if exact custom ratio is unavailable" if ratio >= 2.4 else "2:1 landscape if exact custom ratio is unavailable"
    elif ratio >= 1.66:
        fallback = "16:9 landscape if exact custom ratio is unavailable"
    else:
        fallback = "16:10 landscape if exact custom ratio is unavailable"
    return f"{width}x{height} px", exact_ratio, exact_size, fallback


def chunk_cards(cards: list[dict], group_prefix: str, group_size: int) -> list[tuple[str, list[dict]]]:
    groups = []
    sorted_cards = sorted(cards, key=lambda card: card.get("Display Name", ""))
    for index in range(0, len(sorted_cards), group_size):
        group_number = index // group_size + 1
        groups.append((f"{group_prefix}-{group_number:02d}", sorted_cards[index : index + group_size]))
    return groups


def art_task_groups(cards: list[dict]) -> list[tuple[str, str, list[dict]]]:
    story_cards = [card for card in cards if card.get("Deck") in {"Agenda Deck", "Quest Deck"}]
    encounter_cards = [card for card in cards if card.get("Deck") == "Encounter Deck"]
    creature_cards = [card for card in cards if card.get("Deck") == "Creature Deck"]
    resource_cards = [card for card in cards if card.get("Deck") == "Resource Deck"]
    class_cards = [card for card in cards if card.get("Deck") == "Utility" and card.get("Card Type") == "Class Reference"]

    groups: list[tuple[str, str, list[dict]]] = []
    if story_cards:
        groups.append(("GROUP-STORY", "Quest and secret agenda art", sorted(story_cards, key=lambda card: (card.get("Deck", ""), card.get("Display Name", "")))))
    if encounter_cards:
        groups.append(("GROUP-ENCOUNTER", "Encounter scene art", sorted(encounter_cards, key=lambda card: card.get("Display Name", ""))))
    groups.extend((group_id, "Creature and entity art", group_cards) for group_id, group_cards in chunk_cards(creature_cards, "GROUP-CREATURE", 10))
    groups.extend((group_id, "Resource/action art", group_cards) for group_id, group_cards in chunk_cards(resource_cards, "GROUP-RESOURCE", 13))
    if class_cards:
        groups.append(("GROUP-CLASS", "Class reference art", sorted(class_cards, key=lambda card: card.get("Display Name", ""))))
    return groups


def art_handoff_row(card: dict, spec: dict, group_id: str) -> str:
    source = card.get("_path", "")
    destination = str(card_art_path(card).relative_to(ROOT)).replace("\\", "/")
    brief = card.get("Art Brief", "").replace("|", "/").replace("\n", " ")
    art_window, exact_aspect, exact_size, fallback_aspect = art_window_info(card, spec)
    return (
        f"| `{group_id}` | `{card.get('Card ID', '')}` | {card.get('Display Name', '')} | {card.get('Deck', '')} | "
        f"`{source}` | `{destination}` | {art_window} | {exact_aspect} | {exact_size} | {fallback_aspect} | {brief} |"
    )


def art_handoff_header(title: str, extra_rule: str | None = None) -> list[str]:
    lines = [
        f"# {title}",
        "",
        "Generate one final card image per listed card, then save or move it into the exact destination path.",
        "",
        "Rules for the art session:",
        "",
        "- Do not edit card definition files.",
        "- Use each `Art Brief` as the prompt starting point.",
        "- Keep a consistent dark fantasy board-game illustration style: painterly, readable at card size, ash-choked dungeon ruins, furnace glow, soot, iron, smoke, and warm/cool contrast.",
        "- Do not include readable typography, UI, card borders, watermarks, logos, modern objects, or extra graphic design in the image itself.",
        "- Generate landscape images matching the row's `Exact Aspect` as closely as your generator allows; the existing card art windows are landscape, not portrait.",
        "- If the generator supports custom dimensions, use the row's `Suggested Exact Source Size` or any larger size with the same exact aspect ratio.",
        "- If the generator only supports preset ratios, use the row's `Fallback Aspect` and keep extra crop-safe space around important details.",
        "- Keep the main subject readable inside the center 80% of the image so crop-fitting does not remove heads, faces, hands, weapons, or important silhouettes.",
        "- If an existing final image is portrait or crops badly, treat it as visual reference only and replace it with a landscape version at the same `Destination Path`.",
        "- It is fine to generate larger source images than the final card window; the renderer will crop and fit them.",
        "- Save final images as PNG files at the listed `Destination Path`.",
        "- Raw, experimental, or alternate images can live in `assets/card-art/incoming/` until selected.",
    ]
    if extra_rule:
        lines.append(extra_rule)
    lines.extend(
        [
            "",
            "| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |",
            "| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |",
        ]
    )
    return lines


def write_group_handoff_files(groups: list[tuple[str, str, list[dict]]], spec: dict) -> None:
    ART_GROUP_ROOT.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# AI Art Session Groups",
        "",
        "Use these files to run parallel art-generation sessions. Tell each session its exact task group ID and have it open only that group file.",
        "",
        "Session instruction template:",
        "",
        "```text",
        "You are assigned TASK_GROUP_ID. Open assets/card-art/session-groups/TASK_GROUP_ID.md and generate only the cards listed there. Save each final PNG to its listed Destination Path. Do not edit card definition files or generate cards from other groups.",
        "```",
        "",
        "| Task Group | Scope | Cards | Handoff File |",
        "| --- | --- | ---: | --- |",
    ]
    for group_id, description, group_cards in groups:
        filename = f"{group_id}.md"
        output_path = ART_GROUP_ROOT / filename
        lines = art_handoff_header(
            f"AI Art Handoff: {group_id}",
            f"- This session is assigned `{group_id}` only. Do not generate images for any other task group.",
        )
        for card in group_cards:
            lines.append(art_handoff_row(card, spec, group_id))
        lines.extend(["", "Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.", ""])
        with output_path.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(lines))
        index_lines.append(f"| `{group_id}` | {description} | `{len(group_cards)}` | `assets/card-art/session-groups/{filename}` |")
    index_lines.append("")
    with ART_GROUP_INDEX_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(index_lines))


def write_art_handoff(cards: list[dict], spec: dict) -> None:
    ART_HANDOFF_PATH.parent.mkdir(parents=True, exist_ok=True)
    groups = art_task_groups(cards)
    group_by_card_id = {
        card.get("Card ID", ""): group_id
        for group_id, _, group_cards in groups
        for card in group_cards
    }
    lines = art_handoff_header("AI Art Handoff")
    for card in sorted(cards, key=lambda item: (item.get("Deck", ""), item.get("Display Name", ""))):
        lines.append(art_handoff_row(card, spec, group_by_card_id.get(card.get("Card ID", ""), "GROUP-UNASSIGNED")))
    lines.extend(
        [
            "",
            "For parallel work, use [AI_ART_SESSION_GROUPS.md](AI_ART_SESSION_GROUPS.md) and the per-group files in `assets/card-art/session-groups/`.",
            "",
            "Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.",
            "",
        ]
    )
    with ART_HANDOFF_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    write_group_handoff_files(groups, spec)
    print(f"Wrote {ART_HANDOFF_PATH}")
    print(f"Wrote {ART_GROUP_INDEX_PATH}")
    print(f"Wrote {len(groups)} art session group files in {ART_GROUP_ROOT}")


def render_cards(cards: list[dict], spec: dict) -> list[RenderIssue]:
    all_issues: list[RenderIssue] = []
    for card in cards:
        output_path = card_front_path(card)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image, issues = draw_card(card, spec)
        image.save(output_path)
        all_issues.extend(issues)
        print(f"Wrote {output_path}")
    return all_issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-handoff", action="store_true", help="Do not regenerate assets/card-art/AI_ART_HANDOFF.md.")
    parser.add_argument("--handoff-only", action="store_true", help="Only regenerate art handoff files; do not render card fronts.")
    args = parser.parse_args()

    ensure_output_dirs()
    spec = load_layout_spec()
    defined_cards = load_cards()
    class_cards = extract_class_reference_cards()
    if args.handoff_only:
        write_art_handoff(defined_cards + class_cards, spec)
        return
    cards = defined_cards + class_cards + utility_cards()
    issues = render_cards(cards, spec)
    if not args.skip_handoff:
        write_art_handoff(defined_cards + class_cards, spec)
    print(f"Generated {len(cards)} card-front PNGs in {CARD_FRONT_ROOT}")
    if issues:
        print("Warnings:")
        for issue in issues:
            print(f"- {issue.card_id}: {issue.message}")


if __name__ == "__main__":
    main()
