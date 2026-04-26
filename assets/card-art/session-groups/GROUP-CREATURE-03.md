# AI Art Handoff: GROUP-CREATURE-03

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
- Raw, experimental, or alternate images can live in `assets/card-art/incoming/` until selected.
- This session is assigned `GROUP-CREATURE-03` only. Do not generate images for any other task group.

| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `GROUP-CREATURE-03` | `creature-heartfire-dragon` | Heartfire Dragon | Creature Deck | `defines/cards/creature-deck/cards/heartfire-dragon.txt` | `assets/card-art/final/creature-entity/creature-heartfire-dragon.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A colossal fire dragon fully uncoiled inside a magma-lit cavern. |
| `GROUP-CREATURE-03` | `creature-heavy-door` | Heavy Door | Creature Deck | `defines/cards/creature-deck/cards/heavy-door.txt` | `assets/card-art/final/creature-entity/creature-heavy-door.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A massive reinforced dungeon door with bars, chains, and volcanic soot. |
| `GROUP-CREATURE-03` | `creature-iron-gate` | Iron Gate | Creature Deck | `defines/cards/creature-deck/cards/iron-gate.txt` | `assets/card-art/final/creature-entity/creature-iron-gate.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A dungeon iron gate slamming down in a kennel vault. |
| `GROUP-CREATURE-03` | `creature-kiln-pup` | Kiln Pup | Creature Deck | `defines/cards/creature-deck/cards/kiln-pup.txt` | `assets/card-art/final/creature-entity/creature-kiln-pup.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A compact furnace hound with oversized ember eyes, soot-black paws, and a little iron collar, padding beside the Ashen Warden with cute loyalty and dangerous kiln-fire breath. |
| `GROUP-CREATURE-03` | `creature-orc-raider` | Orc Raider | Creature Deck | `defines/cards/creature-deck/cards/orc-raider.txt` | `assets/card-art/final/creature-entity/creature-orc-raider.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A brutal orc raider kicking through embers with a jagged axe. |
| `GROUP-CREATURE-03` | `creature-rusted-chains` | Rusted Chains | Creature Deck | `defines/cards/creature-deck/cards/rusted-chains.txt` | `assets/card-art/final/creature-entity/creature-rusted-chains.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | Burned chains wrapped around a prison post in a rescue chamber. |
| `GROUP-CREATURE-03` | `creature-skeletal-porter` | Skeletal Porter | Creature Deck | `defines/cards/creature-deck/cards/skeletal-porter.txt` | `assets/card-art/final/creature-entity/creature-skeletal-porter.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A skeletal laborer dragging chains and a slab of iron through the ruin. |
| `GROUP-CREATURE-03` | `creature-smoke-seer` | Smoke Seer | Creature Deck | `defines/cards/creature-deck/cards/smoke-seer.txt` | `assets/card-art/final/creature-entity/creature-smoke-seer.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A hooded seer with a censer and glowing smoke-runes around the hands. |
| `GROUP-CREATURE-03` | `creature-tin-golem` | Tin Golem | Creature Deck | `defines/cards/creature-deck/cards/tin-golem.txt` | `assets/card-art/final/creature-entity/creature-tin-golem.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A chunky tin-plated golem standing protectively in a dungeon corridor. |
| `GROUP-CREATURE-03` | `creature-warding-circle` | Warding Circle | Creature Deck | `defines/cards/creature-deck/cards/warding-circle.txt` | `assets/card-art/final/creature-entity/creature-warding-circle.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A glowing blue protective circle inscribed on dungeon stone. |

Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.
