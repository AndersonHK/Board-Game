#!/usr/bin/env python3
"""Calculate the Edition 0 card layout from the atlas definition.

The card size is intentionally sourced from assets/card-atlas-definition.md so
the layout cannot drift away from the printable atlas.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ATLAS_PATH = ROOT / "assets" / "card-atlas-definition.md"
OUTPUT_PATH = ROOT / "defines" / "card-layout.md"


def read_atlas_card_size() -> dict:
    text = ATLAS_PATH.read_text(encoding="utf-8")
    width_match = re.search(r"card width:\s*`[^=]+=\s*([0-9.]+)\s*in`", text)
    height_match = re.search(r"card height:\s*`[^=]+=\s*([0-9.]+)\s*in`", text)
    quest_width_match = re.search(r"quest card width:\s*`[^=]+=\s*([0-9.]+)\s*in`", text)
    quest_height_match = re.search(r"quest card height:\s*`([0-9.]+)\s*in`", text)
    sheet_match = re.search(r"Use US letter paper:\s*`([0-9.]+)\s*in x\s*([0-9.]+)\s*in`", text)
    grid_match = re.search(r"use a\s*`(\d+) x (\d+)`\s*portrait grid", text, re.IGNORECASE)

    if not (width_match and height_match and sheet_match and grid_match):
        raise SystemExit(f"Could not parse atlas size from {ATLAS_PATH}")

    return {
        "sheet_width_in": float(sheet_match.group(1)),
        "sheet_height_in": float(sheet_match.group(2)),
        "columns": int(grid_match.group(1)),
        "rows": int(grid_match.group(2)),
        "card_width_in": float(width_match.group(1)),
        "card_height_in": float(height_match.group(1)),
        "quest_card_width_in": float(quest_width_match.group(1)) if quest_width_match else float(width_match.group(1)) * 2,
        "quest_card_height_in": float(quest_height_match.group(1)) if quest_height_match else float(height_match.group(1)),
    }


def build_spec() -> dict:
    atlas = read_atlas_card_size()
    safe_margin_in = 0.125
    cut_tolerance_in = 0.0625
    safe_width_in = atlas["card_width_in"] - 2 * (safe_margin_in + cut_tolerance_in)
    safe_height_in = atlas["card_height_in"] - 2 * (safe_margin_in + cut_tolerance_in)
    quest_safe_width_in = atlas["quest_card_width_in"] - 2 * (safe_margin_in + cut_tolerance_in)

    spec = {
        "spec_version": 1,
        "source_atlas": "assets/card-atlas-definition.md",
        "units": "inches and points",
        "sheet": atlas,
        "card": {
            "width_in": atlas["card_width_in"],
            "height_in": atlas["card_height_in"],
            "cut_tolerance_in": cut_tolerance_in,
            "safe_margin_in": safe_margin_in,
            "safe_width_in": round(safe_width_in, 4),
            "safe_height_in": round(safe_height_in, 4),
        },
        "quest_card": {
            "width_in": atlas["quest_card_width_in"],
            "height_in": atlas["quest_card_height_in"],
            "cut_tolerance_in": cut_tolerance_in,
            "safe_margin_in": safe_margin_in,
            "safe_width_in": round(quest_safe_width_in, 4),
            "safe_height_in": round(safe_height_in, 4),
            "atlas_slot_span": "2 columns x 1 row",
        },
        "text_model": {
            "avg_glyph_width_em": 0.52,
            "note": "Approximation for fit checks before final font metrics are available.",
        },
        "layouts": {
            "resource": {
                "applies_to": ["Resource Deck"],
                "title_font_pt": 9.5,
                "title_box_in": 0.30,
                "art_box_in": 1.12,
                "type_line_box_in": 0.18,
                "footer_box_in": 0.20,
                "body_font_pt": 6.8,
                "body_line_height_pt": 7.8,
                "printed_fields": ["Cost", "Timing", "Target", "Rules Text", "Flavor Text"],
            },
            "creature_entity": {
                "applies_to": ["Creature Deck"],
                "title_font_pt": 9.2,
                "title_box_in": 0.30,
                "art_box_in": 1.02,
                "type_line_box_in": 0.18,
                "stats_box_in": 0.22,
                "footer_box_in": 0.18,
                "body_font_pt": 6.6,
                "body_line_height_pt": 7.55,
                "printed_fields": ["Rules Text", "Active Ability", "Round End Text", "Flavor Text"],
            },
            "encounter": {
                "applies_to": ["Encounter Deck"],
                "title_font_pt": 9.2,
                "title_box_in": 0.30,
                "art_box_in": 0.88,
                "type_line_box_in": 0.18,
                "footer_box_in": 0.12,
                "body_font_pt": 6.35,
                "body_line_height_pt": 7.25,
                "printed_fields": ["Reveal Text", "Scene Rule", "Clear Condition", "Reward Text", "Failure Text", "Rules Text", "Flavor Text"],
            },
            "agenda": {
                "applies_to": ["Agenda Deck"],
                "title_font_pt": 9.2,
                "title_box_in": 0.30,
                "art_box_in": 1.02,
                "type_line_box_in": 0.18,
                "footer_box_in": 0.12,
                "body_font_pt": 6.45,
                "body_line_height_pt": 7.4,
                "printed_fields": ["Goal Text", "Reward Text", "Failure Text", "Reveal Timing", "Flavor Text"],
            },
            "quest_reference": {
                "applies_to": ["Quest Deck"],
                "card_size": "quest_card",
                "title_font_pt": 9.0,
                "title_box_in": 0.30,
                "art_box_in": 0.54,
                "type_line_box_in": 0.14,
                "footer_box_in": 0.0,
                "body_font_pt": 6.6,
                "body_line_height_pt": 7.3,
                "printed_fields": [
                    "Quest Stat Line",
                    "Setup Text",
                    "Ongoing Quest Rule",
                    "Threshold 5",
                    "Threshold 8",
                    "Threshold 10",
                    "Lose Condition",
                    "Win Condition",
                    "Rules Text",
                    "Flavor Text",
                ],
            },
        },
    }
    for layout in spec["layouts"].values():
        layout_safe_width_in = quest_safe_width_in if layout.get("card_size") == "quest_card" else safe_width_in
        layout["card_width_in"] = round(atlas["quest_card_width_in"] if layout.get("card_size") == "quest_card" else atlas["card_width_in"], 4)
        layout["card_height_in"] = round(atlas["quest_card_height_in"] if layout.get("card_size") == "quest_card" else atlas["card_height_in"], 4)
        layout["safe_width_in"] = round(layout_safe_width_in, 4)
        layout["safe_height_in"] = round(safe_height_in, 4)
        fixed_in = sum(
            layout.get(key, 0.0)
            for key in ("title_box_in", "art_box_in", "type_line_box_in", "stats_box_in", "footer_box_in")
        )
        body_box_in = safe_height_in - fixed_in
        layout["body_box_in"] = round(body_box_in, 4)
        layout["body_box_pt"] = round(body_box_in * 72, 2)
        layout["safe_width_pt"] = round(layout_safe_width_in * 72, 2)
        layout["estimated_chars_per_line"] = int((layout_safe_width_in * 72) // (layout["body_font_pt"] * spec["text_model"]["avg_glyph_width_em"]))
        layout["estimated_body_lines"] = int((body_box_in * 72) // layout["body_line_height_pt"])
    return spec


def markdown_table(spec: dict) -> str:
    lines = [
        "| Layout | Card Size | Body Box | Font | Line Height | Est. Chars / Line | Est. Body Lines |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, layout in spec["layouts"].items():
        lines.append(
            f"| `{name}` | `{layout['card_width_in']} x {layout['card_height_in']} in` | `{layout['body_box_in']:.4f} in` | `{layout['body_font_pt']} pt` | "
            f"`{layout['body_line_height_pt']} pt` | `{layout['estimated_chars_per_line']}` | `{layout['estimated_body_lines']}` |"
        )
    return "\n".join(lines)


def render_markdown(spec: dict) -> str:
    card = spec["card"]
    quest_card = spec["quest_card"]
    sheet = spec["sheet"]
    spec_json = json.dumps(spec, indent=2)
    return f"""# Card Layout

This file defines the standard front layout for Edition 0 cards. It is generated from [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md), which is the source of truth for card size.

To regenerate this file:

```powershell
python .\\assets\\scripts\\calculate_card_layout.py --write
```

## Physical Size

- Sheet: `{sheet['sheet_width_in']} in x {sheet['sheet_height_in']} in`
- Atlas grid: `{sheet['columns']} x {sheet['rows']}`
- Card size: `{card['width_in']} in x {card['height_in']} in`
- Quest card size: `{quest_card['width_in']} in x {quest_card['height_in']} in`
- Cut tolerance: `{card['cut_tolerance_in']} in`
- Safe margin inside cut tolerance: `{card['safe_margin_in']} in`
- Safe content area: `{card['safe_width_in']} in x {card['safe_height_in']} in`
- Quest safe content area: `{quest_card['safe_width_in']} in x {quest_card['safe_height_in']} in`

## Front Anatomy

All card fronts use the same visual stack:

1. Title band with card name and small deck/type treatment.
2. Flavor image box.
3. Type, tag, or stat line.
4. Rules text box.
5. Optional lower flavor or value strip.

Deck layouts vary by the card size and the height assigned to the art and text areas. Encounter cards intentionally give more room to rules text. Quest reference cards use the two-slot quest card size defined in the atlas so their setup and threshold rules remain readable.

## Calculated Text Areas

{markdown_table(spec)}

The fit model uses an average glyph width of `{spec['text_model']['avg_glyph_width_em']}em`. It is a production sanity check, not a replacement for final PDF proofing with the chosen fantasy/body fonts.

## Printed Field Policy

- Do not print `Card ID`, `Art Brief`, or template metadata on cards.
- `Reminder Text` is deprecated for Edition 0 resource cards; repeated teaching belongs in the rules sheets.
- Print `Display Name` in the title band.
- Print rules fields with short labels unless the final renderer has deck-specific iconography.
- Flavor text is printable, but it is the first field to cut if a card must be tightened.
- Quest cards use the `quest_reference` layout and the two-slot quest card size because they carry setup and threshold rules.

## Machine-Readable Layout Spec

<!-- CARD_LAYOUT_SPEC_JSON_START -->
```json
{spec_json}
```
<!-- CARD_LAYOUT_SPEC_JSON_END -->
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help=f"Write {OUTPUT_PATH}")
    args = parser.parse_args()

    spec = build_spec()
    output = render_markdown(spec)
    if args.write:
        with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(output)
        print(f"Wrote {OUTPUT_PATH}")
    else:
        print(output)


if __name__ == "__main__":
    main()
