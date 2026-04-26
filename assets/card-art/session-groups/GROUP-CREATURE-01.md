# AI Art Handoff: GROUP-CREATURE-01

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
- This session is assigned `GROUP-CREATURE-01` only. Do not generate images for any other task group.

| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `GROUP-CREATURE-01` | `creature-ash-cultist` | Ash Cultist | Creature Deck | `defines/cards/creature-deck/cards/ash-cultist.txt` | `assets/card-art/final/creature-entity/creature-ash-cultist.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A soot-robed cultist carrying a brazier and hooked blade. |
| `GROUP-CREATURE-01` | `creature-ash-miasma` | Ash Miasma | Creature Deck | `defines/cards/creature-deck/cards/ash-miasma.txt` | `assets/card-art/final/creature-entity/creature-ash-miasma.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | Thick ash smoke hanging in coils through a shrine chamber. |
| `GROUP-CREATURE-01` | `creature-ash-ogre` | Ash Ogre | Creature Deck | `defines/cards/creature-deck/cards/ash-ogre.txt` | `assets/card-art/final/creature-entity/creature-ash-ogre.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | An enormous ogre hauling a slab club through volcanic rubble. |
| `GROUP-CREATURE-01` | `creature-ash-skulk` | Ash Skulk | Creature Deck | `defines/cards/creature-deck/cards/ash-skulk.txt` | `assets/card-art/final/creature-entity/creature-ash-skulk.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A thin ash-covered dungeon stalker crouching behind broken masonry with a hooked knife and pale eyes in the smoke. |
| `GROUP-CREATURE-01` | `creature-ashen-warden` | Ashen Warden | Creature Deck | `defines/cards/creature-deck/cards/ashen-warden.txt` | `assets/card-art/final/creature-entity/creature-ashen-warden.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A towering furnace guardian of riveted iron and burning vents, emerging from a kiln. |
| `GROUP-CREATURE-01` | `creature-blessing-brazier` | Blessing Brazier | Creature Deck | `defines/cards/creature-deck/cards/blessing-brazier.txt` | `assets/card-art/final/creature-entity/creature-blessing-brazier.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A sacred furnace brazier on a pedestal, glowing gold amid soot and ruin. |
| `GROUP-CREATURE-01` | `creature-chainbound-head` | Chainbound Head | Creature Deck | `defines/cards/creature-deck/cards/chainbound-head.txt` | `assets/card-art/final/creature-entity/creature-chainbound-head.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A chained dragon skull and neck thrashing loose over a furnace abyss. |
| `GROUP-CREATURE-01` | `creature-cinder-familiar` | Cinder Familiar | Creature Deck | `defines/cards/creature-deck/cards/cinder-familiar.txt` | `assets/card-art/final/creature-entity/creature-cinder-familiar.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A small fox-like fire familiar hovering beside a spellcaster. |
| `GROUP-CREATURE-01` | `creature-cinder-knight` | Cinder Knight | Creature Deck | `defines/cards/creature-deck/cards/cinder-knight.txt` | `assets/card-art/final/creature-entity/creature-cinder-knight.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A burned-out knightly construct holding a heavy sword in a smoke-filled hall. |
| `GROUP-CREATURE-01` | `creature-cinder-sapper` | Cinder Sapper | Creature Deck | `defines/cards/creature-deck/cards/cinder-sapper.txt` | `assets/card-art/final/creature-entity/creature-cinder-sapper.png` | 504x293 px | 504:293 (1.720:1) | 2016x1172 | 16:9 landscape if exact custom ratio is unavailable | A soot-streaked saboteur with cracked goggles, a coal-black pick, and a satchel of ember charges near a dungeon support pillar. |

Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.
