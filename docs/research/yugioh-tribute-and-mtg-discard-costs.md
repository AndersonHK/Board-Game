# Yu-Gi-Oh Tribute And MTG Discard Costs

This note captures external research for the user's requested cost-system direction. It is meant to inform design discussion, not to act as canonical rules text. Broader project context lives in [../project-memory.md](../project-memory.md). The current action-layer design lives in [../design/card-economy-and-rarity.md](../design/card-economy-and-rarity.md).

## Primary Sources

- Konami, [Official Rulebook v9.01](https://img.yugioh-card.com/ygo_cms/ygo/all/uploads/Rulebook_v9_en.pdf)
- Wizards of the Coast, [Discard Tricks](https://magic.wizards.com/en/news/making-magic/discard-tricks-2005-04-11-0)
- Wizards of the Coast, [Why? Because We Like You](https://magic.wizards.com/en/news/making-magic/why-because-we-you-2011-08-12)
- Wizards of the Coast, [The Dynamics of a Turn](https://magic.wizards.com/en/news/feature/dynamics-turn-2006-11-04)
- Wizards of the Coast, [Magic Rules Hub](https://magic.wizards.com/en/rules)

## What The Sources Say

### Yu-Gi-Oh Tribute Structure

- The official rulebook says Level 5 to 6 monsters require 1 Tribute, while Level 7 or higher require 2 Tributes.
- Tribute Summons are not a bonus action. They still live inside the game's normal once-per-turn summon lane.
- The same rulebook also uses discarding, Tributing, and paying LP as examples of intentional activation costs for effects used during a player's own main phase.

### Magic Discard Structure

- Wizards describes discard as a historically unfun mechanic when pushed too hard, especially because it stops players from getting to use their cards.
- Wizards also says random discard became rarer because it annoyed players more than directed or chosen discard.
- Mark Rosewater's discard design guidance says discard is usually kept at sorcery speed so it does not become a surprise "you never got to play your card" trap.
- The same article distinguishes discard as a theme from discard as a utility tool and notes that discard gets stronger as more discard pieces exist in the same deck.
- Magic's turn-structure guidance checks hand size during cleanup rather than forcing immediate discard the moment a player goes over the limit.

## Design Lessons For This Project

### 1. Expensive Effects Should Ask For Visible Commitment

The cleanest reusable lesson from Tribute Summons is not "copy monster levels." It is that powerful effects can ask for board or hand commitment that the table can see. A big play feels earned when the cost is paid from real assets already under pressure.

### 2. Costs Should Usually Be Voluntary And On Your Own Turn

Both games point toward costs that are declared deliberately, not surprise taxes sprung out of nowhere. If this project uses discard and sacrifice as its main cost language, those payments should usually happen when the acting player chooses a strong line, not as constant hidden punishment.

### 3. Player-Choice Discard Is Safer Than Random Discard

Magic's official design writing strongly suggests that random discard is more frustrating than selective discard. For this board game, that argues for costs like "discard 1" or "discard a setup card" over "discard at random" when a player is paying for their own power spike.

### 4. Cost Density Snowballs Fast

Magic explicitly warns that discard becomes more powerful when more discard pieces exist in the same shell. In this project, that means discard costs, hand-attack effects, forced cleanup pressure, and hand-cap manipulation should not all be pushed hard in the same archetype or rarity band at once.

### 5. Cleanup-Based Hand Limits Support Hoarding Identities

Magic's cleanup model is a useful precedent for hand-size asymmetry. If one archetype gets a bigger hand cap, the clean interpretation is that it matters at cleanup, not that it creates extra draw windows by itself.

## Current Fit For The Board Game

- The user's directive that strong cards should cost discards and sacrifices is consistent with both source families, as long as the costs remain visible and deliberate.
- A two-rarity structure can help communicate when those heavier costs appear more often.
- The current simulation evidence makes one caution especially important: strong finishers and greedy hand growth already produce rivalry. Any new "pay cards to explode" system will amplify that tension further.

## Research-Informed Warnings

- Do not make random discard a major baseline tax unless chaos is the explicit point of the card or encounter.
- Do not let the late-game archetype combine a much larger hand cap with too many free extra draws, or it may stop feeling like "stored patience" and start feeling like raw card-volume dominance.
- Do not let the aggressive archetype's reward for kills become so reliable that it encourages players to hold back until a monster is almost dead every time.

## Open Questions For Canonization

1. Should discard and sacrifice be mostly self-paid action costs, or can encounters regularly force them too?
2. Should the heaviest cards ask for hand discards, board sacrifices, or a choice between the two?
3. Should monster rarity and resource rarity use the same words and the same power expectations, or only the same field name?
4. If a class changes hand size, should that be active from setup or unlocked later by escalation, storage, or class progress?
