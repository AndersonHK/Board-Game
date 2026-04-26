# AI Art Handoff: GROUP-CLASS

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
- This session is assigned `GROUP-CLASS` only. Do not generate images for any other task group.

| Task Group | Card ID | Display Name | Deck | Source | Destination Path | Art Window | Exact Aspect | Suggested Exact Source Size | Fallback Aspect | Art Brief |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| `GROUP-CLASS` | `class-cleric` | Cleric Reference | Utility | `docs/quick-start-guide.md` | `assets/card-art/final/utility/class-cleric.png` | 1116x357 px | 372:119 (3.126:1) | 1116x357 | 3:1 wide landscape if exact custom ratio is unavailable | A soot-streaked cleric raises a warm golden prayer over wounded allies beside a broken altar, mercy shining through black furnace smoke. |
| `GROUP-CLASS` | `class-warrior` | Warrior Reference | Utility | `docs/quick-start-guide.md` | `assets/card-art/final/utility/class-warrior.png` | 1116x357 px | 372:119 (3.126:1) | 1116x357 | 3:1 wide landscape if exact custom ratio is unavailable | A battle-scarred warrior plants a shield and sword in a smoke-filled dungeon breach, holding the line against silhouettes in furnace light. |
| `GROUP-CLASS` | `class-wizard` | Wizard Reference | Utility | `docs/quick-start-guide.md` | `assets/card-art/final/utility/class-wizard.png` | 1116x357 px | 372:119 (3.126:1) | 1116x357 | 3:1 wide landscape if exact custom ratio is unavailable | A calm wizard studies glowing blue-white runes over cracked stone, shaping smoke and ash into a precise defensive spell. |

Generated utility cards other than class references, proxy blanks, and divider cards do not need AI art.
