#!/usr/bin/env python3
"""Estimate whether current card text fits the Edition 0 layout."""

from __future__ import annotations

import argparse
import json
import math
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LAYOUT_PATH = ROOT / "defines" / "card-layout.md"
CARD_ROOT = ROOT / "defines" / "cards"
REPORT_PATH = ROOT / "assets" / "card-text-fit-report.md"

SKIP_VALUES = {"", "None", "None."}
LABELS = {
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
    "Threshold 5": "5",
    "Threshold 8": "8",
    "Threshold 10": "10",
    "Lose Condition": "Lose",
    "Win Condition": "Win",
    "Flavor Text": "Flavor",
}


def load_spec() -> dict:
    text = LAYOUT_PATH.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- CARD_LAYOUT_SPEC_JSON_START -->\s*```json\s*(.*?)\s*```\s*<!-- CARD_LAYOUT_SPEC_JSON_END -->",
        text,
        re.DOTALL,
    )
    if not match:
        raise SystemExit(f"Could not find machine-readable layout spec in {LAYOUT_PATH}")
    return json.loads(match.group(1))


def parse_card(path: Path) -> dict:
    fields = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    fields["_path"] = str(path.relative_to(ROOT)).replace("\\", "/")
    return fields


def iter_card_files() -> list[Path]:
    return sorted(path for path in CARD_ROOT.rglob("*.txt") if path.name.upper() != "TEMPLATE.TXT" and path.parent.name == "cards")


def layout_for_card(spec: dict, card: dict) -> str:
    deck = card.get("Deck", "")
    for name, layout in spec["layouts"].items():
        if deck in layout["applies_to"]:
            return name
    raise ValueError(f"No layout for deck {deck!r} in {card['_path']}")


def chars_per_line(width_pt: float, font_pt: float, avg_glyph_width_em: float) -> int:
    return max(10, int(width_pt // (font_pt * avg_glyph_width_em)))


def wrapped_line_count(text: str, width: int) -> int:
    if not text:
        return 0
    return max(1, len(textwrap.wrap(text, width=width, break_long_words=False, replace_whitespace=False)))


def printable_lines(card: dict, layout: dict) -> list[str]:
    lines = []

    if card.get("Deck") == "Quest Deck":
        stats = (
            f"{card.get('Player Count', '')}: "
            f"4P HP {card.get('Starting Party HP (4P)', '')}, hand {card.get('Starting Hand Size (4P)', '')}; "
            f"3P HP {card.get('Starting Party HP (3P)', '')}, hand {card.get('Starting Hand Size (3P)', '')}; "
            f"Esc {card.get('Escalation Track', '')}"
        )
        lines.append(stats)

    if card.get("Deck") == "Creature Deck":
        stats = []
        for key, label in (("Threat", "T"), ("Hit Points", "HP"), ("Attack", "ATK"), ("Treasure Value", "TV")):
            value = card.get(key, "")
            if value not in SKIP_VALUES:
                stats.append(f"{label} {value}")
        if stats:
            lines.append(" / ".join(stats))

    if card.get("Deck") == "Resource Deck":
        tv = card.get("Treasure Value", "")
        subtype = card.get("Subtype", "")
        if tv not in SKIP_VALUES or subtype not in SKIP_VALUES:
            lines.append(" / ".join(part for part in (subtype, f"TV {tv}" if tv else "") if part))

    if card.get("Deck") == "Encounter Deck":
        scene_tags = card.get("Scene Tags", "")
        if scene_tags not in SKIP_VALUES:
            lines.append(f"Tags: {scene_tags}")

    for field in layout["printed_fields"]:
        if field == "Quest Stat Line":
            continue
        value = card.get(field, "")
        if value in SKIP_VALUES:
            continue
        label = LABELS.get(field, field)
        if field == "Flavor Text":
            lines.append(f"\"{value}\"")
        else:
            lines.append(f"{label}: {value}")
    return lines


def check_card(spec: dict, card: dict) -> dict:
    layout_name = layout_for_card(spec, card)
    layout = spec["layouts"][layout_name]
    avg = spec["text_model"]["avg_glyph_width_em"]
    body_width = chars_per_line(layout["safe_width_pt"], layout["body_font_pt"], avg)
    title_width = chars_per_line(layout["safe_width_pt"], layout["title_font_pt"], avg)
    title_lines = wrapped_line_count(card.get("Display Name", ""), title_width)
    title_capacity = max(1, int((layout["title_box_in"] * 72) // (layout["title_font_pt"] * 1.1)))
    body_lines = sum(wrapped_line_count(line, body_width) for line in printable_lines(card, layout))
    body_capacity = layout["estimated_body_lines"]
    ratio = body_lines / body_capacity if body_capacity else math.inf
    status = "PASS"
    if title_lines > title_capacity or body_lines > body_capacity:
        status = "FAIL"
    elif ratio >= 0.9:
        status = "WARN"
    return {
        "status": status,
        "name": card.get("Display Name", "(unnamed)"),
        "deck": card.get("Deck", ""),
        "layout": layout_name,
        "body_lines": body_lines,
        "body_capacity": body_capacity,
        "title_lines": title_lines,
        "title_capacity": title_capacity,
        "path": card["_path"],
        "ratio": ratio,
    }


def render_report(results: list[dict]) -> str:
    counts = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for result in results:
        counts[result["status"]] += 1
    lines = [
        "# Card Text Fit Report",
        "",
        f"Layout source: [../defines/card-layout.md](../defines/card-layout.md)",
        "",
        f"- Cards checked: `{len(results)}`",
        f"- Pass: `{counts['PASS']}`",
        f"- Warn: `{counts['WARN']}`",
        f"- Fail: `{counts['FAIL']}`",
        "",
        "This report uses approximate text metrics from the layout definition. Final proofing still needs the actual render fonts.",
        "",
        "| Status | Card | Deck | Layout | Body Lines | Title Lines | Path |",
        "| --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    for result in sorted(results, key=lambda item: ({"FAIL": 0, "WARN": 1, "PASS": 2}[item["status"]], item["deck"], item["name"])):
        lines.append(
            f"| `{result['status']}` | {result['name']} | {result['deck']} | `{result['layout']}` | "
            f"`{result['body_lines']}/{result['body_capacity']}` | `{result['title_lines']}/{result['title_capacity']}` | "
            f"`{result['path']}` |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true", help=f"Write {REPORT_PATH}")
    args = parser.parse_args()

    spec = load_spec()
    cards = [parse_card(path) for path in iter_card_files()]
    results = [check_card(spec, card) for card in cards]
    report = render_report(results)

    if args.write_report:
        with REPORT_PATH.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(report)
        print(f"Wrote {REPORT_PATH}")

    print(report)
    if any(result["status"] == "FAIL" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
