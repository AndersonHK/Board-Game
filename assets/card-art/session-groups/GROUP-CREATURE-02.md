# AI Art Handoff: GROUP-CREATURE-02

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
- This session is assigned `GROUP-CREATURE-02` only. Do not generate images for any other task group. When staging alternates, use `assets/card-art/incoming/GROUP-CREATURE-02/`.

| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `GROUP-CREATURE-02` | `creature-dire-wolf` | Dire Wolf | Creature Deck | `defines/cards/creature-deck/cards/dire-wolf.txt` | `assets/card-art/final/creature-entity/creature-dire-wolf.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A massive wolf with ash in its fur and glowing eyes in the furnace light. |
| `GROUP-CREATURE-02` | `creature-ember-bat` | Ember Bat | Creature Deck | `defines/cards/creature-deck/cards/ember-bat.txt` | `assets/card-art/final/creature-entity/creature-ember-bat.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A small flaming bat creature scattering embers in a dungeon vault. |
| `GROUP-CREATURE-02` | `creature-furnace-hound` | Furnace Hound | Creature Deck | `defines/cards/creature-deck/cards/furnace-hound.txt` | `assets/card-art/final/creature-entity/creature-furnace-hound.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A molten hunting hound with furnace cracks glowing under the skin. |
| `GROUP-CREATURE-02` | `creature-goblin-bruiser` | Goblin Bruiser | Creature Deck | `defines/cards/creature-deck/cards/goblin-bruiser.txt` | `assets/card-art/final/creature-entity/creature-goblin-bruiser.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A stocky goblin with a club and patched leather, charging through cinders. |
| `GROUP-CREATURE-02` | `creature-goblin-chieftain` | Goblin Chieftain | Creature Deck | `defines/cards/creature-deck/cards/goblin-chieftain.txt` | `assets/card-art/final/creature-entity/creature-goblin-chieftain.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A goblin commander in scavenged plate barking orders in a kennel corridor. |
| `GROUP-CREATURE-02` | `creature-goblin-cutthroat` | Goblin Cutthroat | Creature Deck | `defines/cards/creature-deck/cards/goblin-cutthroat.txt` | `assets/card-art/final/creature-entity/creature-goblin-cutthroat.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A lean goblin knife-fighter lunging from the dark with scavenged armor. |
| `GROUP-CREATURE-02` | `creature-grave-hound` | Grave Hound | Creature Deck | `defines/cards/creature-deck/cards/grave-hound.txt` | `assets/card-art/final/creature-entity/creature-grave-hound.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A spectral hound with grave-dust fur tracking a wounded target. |
| `GROUP-CREATURE-02` | `creature-grave-knight` | Grave Knight | Creature Deck | `defines/cards/creature-deck/cards/grave-knight.txt` | `assets/card-art/final/creature-entity/creature-grave-knight.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | An undead knight in ash-caked mail rising from a cracked tomb slab, its sword glowing dull red under furnace light. |
| `GROUP-CREATURE-02` | `creature-gray-wolf` | Gray Wolf | Creature Deck | `defines/cards/creature-deck/cards/gray-wolf.txt` | `assets/card-art/final/creature-entity/creature-gray-wolf.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A scarred wolf prowling through ash and chains. |
| `GROUP-CREATURE-02` | `creature-greedfire-vow` | Greedfire Vow | Creature Deck | `defines/cards/creature-deck/cards/greedfire-vow.txt` | `assets/card-art/final/creature-entity/creature-greedfire-vow.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A red-orange pact sigil written in flame above a treasure hoard. |

Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.
