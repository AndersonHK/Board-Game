# Card Layout

This file defines the standard front layout for Edition 0 cards. It is generated from [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md), which is the source of truth for card size.

To regenerate this file:

```powershell
python .\assets\scripts\calculate_card_layout.py --write
```

## Physical Size

- Sheet: `8.5 in x 11.0 in`
- Atlas grid: `4 x 3`
- Card size: `2.125 in x 3.6667 in`
- Quest card size: `4.25 in x 7.3334 in`
- Class reference size: `4.25 in x 3.6667 in`
- Cut tolerance: `0.0625 in`
- Safe margin inside cut tolerance: `0.125 in`
- Safe content area: `1.75 in x 3.2917 in`
- Quest safe content area: `3.875 in x 6.9584 in`
- Class reference safe content area: `3.875 in x 3.2917 in`

## Front Anatomy

All card fronts use the same visual stack:

1. Title band with card name and small deck/type treatment.
2. Flavor image box.
3. Type, tag, or stat line.
4. Rules text box.
5. Optional lower flavor or value strip.

Deck layouts vary by the card size and the height assigned to the art and text areas. Encounter cards intentionally give more room to rules text. Quest reference cards use the four-slot quest card size defined in the atlas, with visible sections for stats, setup, escalation, win, and lose text. Class references use a two-slot card size with one shared body font size across all class cards.

## Calculated Text Areas

| Layout | Card Size | Body Box | Font | Line Height | Est. Chars / Line | Est. Body Lines |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `resource` | `2.125 x 3.6667 in` | `1.4917 in` | `6.8 pt` | `7.8 pt` | `35` | `13` |
| `creature_entity` | `2.125 x 3.6667 in` | `1.3917 in` | `6.6 pt` | `7.55 pt` | `36` | `13` |
| `encounter` | `2.125 x 3.6667 in` | `1.9317 in` | `6.35 pt` | `7.25 pt` | `38` | `19` |
| `agenda` | `2.125 x 3.6667 in` | `1.6717 in` | `6.45 pt` | `7.4 pt` | `37` | `16` |
| `quest_reference` | `4.25 x 7.3334 in` | `3.8484 in` | `10.0 pt` | `11.5 pt` | `53` | `24` |
| `class_reference` | `4.25 x 3.6667 in` | `1.7517 in` | `8.2 pt` | `9.25 pt` | `65` | `13` |

The fit model uses an average glyph width of `0.52em`. It is a production sanity check, not a replacement for final PDF proofing with the chosen fantasy/body fonts.

## Printed Field Policy

- Do not print `Card ID`, `Art Brief`, or template metadata on cards.
- `Reminder Text` is deprecated for Edition 0 resource cards; repeated teaching belongs in the rules sheets.
- Print `Display Name` in the title band.
- Print rules fields with short labels unless the final renderer has deck-specific iconography.
- Flavor text is printable, but it is the first field to cut if a card must be tightened.
- Quest cards use the `quest_reference` layout and the four-slot quest card size because they carry setup and threshold rules.
- Class reference cards use the `class_reference` layout and the two-slot class reference size.

## Machine-Readable Layout Spec

<!-- CARD_LAYOUT_SPEC_JSON_START -->
```json
{
  "spec_version": 1,
  "source_atlas": "assets/card-atlas-definition.md",
  "units": "inches and points",
  "sheet": {
    "sheet_width_in": 8.5,
    "sheet_height_in": 11.0,
    "columns": 4,
    "rows": 3,
    "card_width_in": 2.125,
    "card_height_in": 3.6667,
    "quest_card_width_in": 4.25,
    "quest_card_height_in": 7.3334,
    "class_card_width_in": 4.25,
    "class_card_height_in": 3.6667
  },
  "card": {
    "width_in": 2.125,
    "height_in": 3.6667,
    "cut_tolerance_in": 0.0625,
    "safe_margin_in": 0.125,
    "safe_width_in": 1.75,
    "safe_height_in": 3.2917
  },
  "quest_card": {
    "width_in": 4.25,
    "height_in": 7.3334,
    "cut_tolerance_in": 0.0625,
    "safe_margin_in": 0.125,
    "safe_width_in": 3.875,
    "safe_height_in": 6.9584,
    "atlas_slot_span": "2 columns x 2 rows"
  },
  "class_card": {
    "width_in": 4.25,
    "height_in": 3.6667,
    "cut_tolerance_in": 0.0625,
    "safe_margin_in": 0.125,
    "safe_width_in": 3.875,
    "safe_height_in": 3.2917,
    "atlas_slot_span": "2 columns x 1 row"
  },
  "text_model": {
    "avg_glyph_width_em": 0.52,
    "note": "Approximation for fit checks before final font metrics are available."
  },
  "layouts": {
    "resource": {
      "applies_to": [
        "Resource Deck"
      ],
      "title_font_pt": 9.5,
      "title_box_in": 0.3,
      "art_box_in": 1.12,
      "type_line_box_in": 0.18,
      "footer_box_in": 0.2,
      "body_font_pt": 6.8,
      "body_line_height_pt": 7.8,
      "printed_fields": [
        "Cost",
        "Timing",
        "Target",
        "Rules Text",
        "Flavor Text"
      ],
      "card_width_in": 2.125,
      "card_height_in": 3.6667,
      "safe_width_in": 1.75,
      "safe_height_in": 3.2917,
      "body_box_in": 1.4917,
      "body_box_pt": 107.4,
      "safe_width_pt": 126.0,
      "estimated_chars_per_line": 35,
      "estimated_body_lines": 13
    },
    "creature_entity": {
      "applies_to": [
        "Creature Deck"
      ],
      "title_font_pt": 9.2,
      "title_box_in": 0.3,
      "art_box_in": 1.02,
      "type_line_box_in": 0.18,
      "stats_box_in": 0.22,
      "footer_box_in": 0.18,
      "body_font_pt": 6.6,
      "body_line_height_pt": 7.55,
      "printed_fields": [
        "Rules Text",
        "Active Ability",
        "Round End Text",
        "Flavor Text"
      ],
      "card_width_in": 2.125,
      "card_height_in": 3.6667,
      "safe_width_in": 1.75,
      "safe_height_in": 3.2917,
      "body_box_in": 1.3917,
      "body_box_pt": 100.2,
      "safe_width_pt": 126.0,
      "estimated_chars_per_line": 36,
      "estimated_body_lines": 13
    },
    "encounter": {
      "applies_to": [
        "Encounter Deck"
      ],
      "title_font_pt": 9.2,
      "title_box_in": 0.3,
      "art_box_in": 0.88,
      "type_line_box_in": 0.18,
      "footer_box_in": 0.0,
      "body_font_pt": 6.35,
      "body_line_height_pt": 7.25,
      "printed_fields": [
        "Reveal Text",
        "Scene Rule",
        "Clear Condition",
        "Reward Text",
        "Failure Text",
        "Rules Text",
        "Flavor Text"
      ],
      "card_width_in": 2.125,
      "card_height_in": 3.6667,
      "safe_width_in": 1.75,
      "safe_height_in": 3.2917,
      "body_box_in": 1.9317,
      "body_box_pt": 139.08,
      "safe_width_pt": 126.0,
      "estimated_chars_per_line": 38,
      "estimated_body_lines": 19
    },
    "agenda": {
      "applies_to": [
        "Agenda Deck"
      ],
      "title_font_pt": 9.2,
      "title_box_in": 0.3,
      "art_box_in": 1.02,
      "type_line_box_in": 0.18,
      "footer_box_in": 0.12,
      "body_font_pt": 6.45,
      "body_line_height_pt": 7.4,
      "printed_fields": [
        "Goal Text",
        "Reward Text",
        "Failure Text",
        "Reveal Timing",
        "Flavor Text"
      ],
      "card_width_in": 2.125,
      "card_height_in": 3.6667,
      "safe_width_in": 1.75,
      "safe_height_in": 3.2917,
      "body_box_in": 1.6717,
      "body_box_pt": 120.36,
      "safe_width_pt": 126.0,
      "estimated_chars_per_line": 37,
      "estimated_body_lines": 16
    },
    "quest_reference": {
      "applies_to": [
        "Quest Deck"
      ],
      "card_size": "quest_card",
      "title_font_pt": 15.0,
      "title_box_in": 0.42,
      "art_box_in": 2.45,
      "type_line_box_in": 0.24,
      "footer_box_in": 0.0,
      "body_font_pt": 10.0,
      "body_line_height_pt": 11.5,
      "printed_fields": [
        "Quest Stat Line",
        "Setup Text",
        "Ongoing Quest Rule",
        "Threshold 5",
        "Threshold 8",
        "Threshold 10",
          "Lose Condition",
          "Win Condition",
          "Win Flavor Text",
          "Lose Flavor Text",
          "Rules Text",
          "Flavor Text"
      ],
      "card_width_in": 4.25,
      "card_height_in": 7.3334,
      "safe_width_in": 3.875,
      "safe_height_in": 6.9584,
      "body_box_in": 3.8484,
      "body_box_pt": 277.08,
      "safe_width_pt": 279.0,
      "estimated_chars_per_line": 53,
      "estimated_body_lines": 24
    },
    "class_reference": {
      "applies_to": [
        "Utility"
      ],
      "card_size": "class_card",
      "title_font_pt": 11.0,
      "title_box_in": 0.3,
      "art_box_in": 1.24,
      "type_line_box_in": 0.0,
      "footer_box_in": 0.0,
      "body_font_pt": 8.2,
      "body_line_height_pt": 9.25,
      "printed_fields": [
        "Rules Text"
      ],
      "card_width_in": 4.25,
      "card_height_in": 3.6667,
      "safe_width_in": 3.875,
      "safe_height_in": 3.2917,
      "body_box_in": 1.7517,
      "body_box_pt": 126.12,
      "safe_width_pt": 279.0,
      "estimated_chars_per_line": 65,
      "estimated_body_lines": 13
    }
  }
}
```
<!-- CARD_LAYOUT_SPEC_JSON_END -->
