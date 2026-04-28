# AI Art Handoff: GROUP-STORY

Generate one final card image per listed card, then save or move it into the exact destination path.

Rules for the art session:

- Do not edit card definition files.
- Use each `Art Brief` as the prompt starting point.
- Keep a consistent dark fantasy board-game illustration style: painterly, readable at card size, ash-choked dungeon ruins, furnace glow, soot, iron, smoke, and warm/cool contrast.
- Do not include readable typography, UI, card borders, watermarks, logos, modern objects, or extra graphic design in the image itself.
- Generate landscape images matching the row's `Exact Aspect` as closely as your generator allows; the existing card art windows are landscape, not portrait.
- If the generator supports custom dimensions, use the row's `Suggested Exact Source Size` or any larger size with the same exact aspect ratio.
- If the generator only supports preset ratios, use the row's `Fallback Aspect` and keep extra crop-safe space around important details.
- Keep the main subject readable inside the center 80% of the image so crop-fitting does not remove heads, faces, hands, weapons, or important silhouettes.
- If an existing final image is portrait or crops badly, treat it as visual reference only and replace it with a landscape version at the same `Destination Path`.
- It is fine to generate larger source images than the final card window; the renderer will crop and fit them.
- Save final images as PNG files at the listed `Destination Path`.
- Keep raw, experimental, or alternate images in `assets/card-art/incoming/TASK_GROUP_ID/` or the image tool's current-session output folder until selected.
- When selecting or moving final PNGs, inspect only images produced in this task group's current session or in `assets/card-art/incoming/TASK_GROUP_ID/`.
- Do not search, reuse, copy, or infer from other task-group folders, other image-session folders, or unrelated existing final art. Cross-session image reuse can silently put the right filename on the wrong picture.
- Before finishing, compare the selected image against the row's `Display Name` and `Art Brief`; if the subject does not match, regenerate it instead of saving it.
- This session is assigned `GROUP-STORY` only. Do not generate images for any other task group. When staging alternates, use `assets/card-art/incoming/GROUP-STORY/`.

| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `GROUP-STORY` | `agenda-ashes-to-ashes` | Ashes to Ashes | Agenda Deck | `defines/cards/agenda-deck/cards/ashes-to-ashes.txt` | `assets/card-art/final/agenda/agenda-ashes-to-ashes.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A triumphant hunter standing over multiple fallen dungeon threats. |
| `GROUP-STORY` | `agenda-by-my-grace` | By My Grace | Agenda Deck | `defines/cards/agenda-deck/cards/by-my-grace.txt` | `assets/card-art/final/agenda/agenda-by-my-grace.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A support hero steadying multiple allies in a collapsing ruin. |
| `GROUP-STORY` | `agenda-first-name-in-the-ballad` | First Name in the Ballad | Agenda Deck | `defines/cards/agenda-deck/cards/first-name-in-the-ballad.txt` | `assets/card-art/final/agenda/agenda-first-name-in-the-ballad.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A heroic name carved into a scorched stone ballad tablet. |
| `GROUP-STORY` | `agenda-keeper-of-relics` | Keeper of Relics | Agenda Deck | `defines/cards/agenda-deck/cards/keeper-of-relics.txt` | `assets/card-art/final/agenda/agenda-keeper-of-relics.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A treasure-keeper surrounded by relics, wards, and summoned allies. |
| `GROUP-STORY` | `agenda-prepared-beyond-reason` | Prepared Beyond Reason | Agenda Deck | `defines/cards/agenda-deck/cards/prepared-beyond-reason.txt` | `assets/card-art/final/agenda/agenda-prepared-beyond-reason.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A calm spellcaster or planner surrounded by stacked gear and mapped routes. |
| `GROUP-STORY` | `agenda-richer-than-the-ruin` | Richer Than the Ruin | Agenda Deck | `defines/cards/agenda-deck/cards/richer-than-the-ruin.txt` | `assets/card-art/final/agenda/agenda-richer-than-the-ruin.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A survivor weighing coins and relics against a burning backdrop. |
| `GROUP-STORY` | `quest-ashen-depths` | Ashen Depths | Quest Deck | `defines/cards/quest-deck/cards/ashen-depths.txt` | `assets/card-art/final/quest/quest-ashen-depths.png` | 1116x705 px | 372:235 (1.583:1) | 1116x705 | 16:10 landscape if exact custom ratio is unavailable | A massive stair descending into a volcanic dungeon, with soot in the air, cracked stone saints, and orange furnace light below. |

Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.
