# Project Memory

This file is the long-term memory for the project. It should retain the durable context needed to resume work cleanly across sessions. Repository structure and canonical file locations are tracked in [repository-directory.md](./repository-directory.md). Repo-wide Codex instructions live in [../CODEX.md](../CODEX.md).

## Snapshot

- Project: class board game project
- Timeline: one week total
- Collaboration model: user provides the evolving vision; Codex helps design, document, structure, and iterate
- Delivery strategy: finish and maintain the Edition 0 printable vertical slice
- Art plan: use AI-generated art and generated print assets for the physical game
- Current phase: vertical-demo release cleanup, print-readiness, and final rules/card wording checks

## Current Understanding

On 2026-04-20, the user said we are designing a class board game together under a one-week time budget. Many design details remain uncertain, so the process should favor a nearly complete minimal horizontal slice first, then a fully playable vertical slice. The art will be fully AI-generated and later printed. The user asked for persistent markdown-based project memory, a repository directory reference, and a root [../CODEX.md](../CODEX.md) that tells Codex to keep these files current and cross-referenced.

Later on 2026-04-20, the user added the first real concept brief. The game should support the immediate classroom context of four players but ideally scale beyond that. The user cited [research on Betrayal at House on the Hill](./research/research-index.md#betrayal-at-house-on-the-hill), [research on the Hearts of Iron IV world tension meter](./research/research-index.md#hearts-of-iron-iv-world-tension), [research on Hearthstone hero powers](./research/research-index.md#hearthstone-hero-powers-and-lightweight-asymmetry), and [research on Civilization traits and unique abilities](./research/research-index.md#civilization-traits-and-unique-abilities) as important mechanical reference points.

The game is intended to be system-agnostic across theme packs. The same mechanical skeleton should support fantasy, sci-fi, steampunk, grimdark, and similar settings, while the flavor names and presentation change. For the first vertical-slice demo, the user is leaning toward a classic D&D-like fantasy setting. A fuller evolving brief is tracked in [design/core-concept.md](./design/core-concept.md), current class identity notes live in [design/class-archetypes.md](./design/class-archetypes.md), and the deck model lives in [design/deck-architecture.md](./design/deck-architecture.md).

Later on 2026-04-20, the user corrected the component structure: the game actually has four decks or deck-like systems, not three. The four are the [world or quest system](./design/deck-architecture.md#world--quest-system), [encounter deck](./design/deck-architecture.md#encounter-deck), [resource-artifact-action deck](./design/deck-architecture.md#resource--artifact--action-deck), and [secret agenda deck](./design/deck-architecture.md#secret-agenda-deck). The game has no explicit traitor. All players are in the same party and share the lose condition of survival, but each player also has a secret agenda and wants to finish with the most points. The current round-flow hypothesis and escalation model are tracked in [design/round-structure.md](./design/round-structure.md).

Later on 2026-04-20, the user corrected a more important misunderstanding in the earlier prototype framing. Encounter cards should not be treated as fixed threat-value cards. They are event or scene cards that may spawn monster cards, force save throws, trigger discards, create bargains, or open preparation windows. Monster cards and player-controlled allied entities such as familiars or golems should likely share a common rules grammar rather than becoming a separate fifth core deck immediately. The action deck should include both battle tools and selfish setup cards that can be used outside battle, so a greedy player can spend time improving their own future position instead of merely skipping help. The desired experience is emergent relationship storytelling: players should feel invested in who was brave, selfish, rescued, indebted, or resentful by the end of the story.

Later that same day, the user clarified that the same event can scale across escalation bands by spawning different enemy cards, such as goblins at low tension, orcs at mid tension, and an ogre at high tension. The user also asked us to design toward the possibility of an auxiliary enemy or entity reserve that could hold monster cards, persistent obstacles like heavy doors, and persistent enchantments like miasma. After that, the user formalized a real [creature deck](../defines/creature-deck.md) and a canonical [core round structure](../defines/core-rules.md): starting hand 3, hand limit 6, standard rounds use two action turns, players act first and enemy monsters act after them in each half of the round, every player and enemy monster takes an action each turn if able, the standard draw happens between turns 1 and 2 once per round and still happens at round end if that window was skipped, unresolved hurdles raise escalation at round end, round-end effects from cards are then triggered, and escalation 10 removes the normal turn cap.

Later still, the user cleaned up the creature-deck wording. Encounters should not use abstract level-based creature packages. Instead, encounter cards either name exact creature cards or specify valid card types, and players then go through the creature deck in order to take the first cards that satisfy the criteria. The user also asked that [defines](../defines/README.md) stay rulebook-like and avoid design-rationale language; broader pacing and interpretation notes should live in the design docs instead.

Later still, the user refined the spawn examples again. The `Ashen Ambush` example should keep its high-escalation `Ogre Brute`, while the medium-escalation example should demonstrate criteria-based spawning with strength references instead of named cards. The user also suggested a likely future creature taxonomy: monsters may carry a threat or strength value, and each rough band may eventually split into a simpler minor versus major distinction, with round-end effects being much more common on the stronger side of that split. That taxonomy is not yet canonical defines text, but it is now part of the active design direction in [design/deck-architecture.md](./design/deck-architecture.md).

On 2026-04-21, the user asked for a design pass before more canonical `defines/` work. The next focus is naming the three archetypes, drafting rule definitions for each, and using the latest simulated match to inform balancing questions before promotion. The user specifically wants the late-game wizard-like archetype to have a hand limit of 12 instead of 6, the aggressive warrior-like archetype to have a chance to gain a card from monster last hits based on monster threat or strength, and both monster cards and player resource cards to share exactly two rarity types. The user also stated a stronger economic directive: card "cost" should primarily come from discards and sacrifices, with stronger cards being more expensive and weaker cards being more immediate. Research for that direction now lives in [research/yugioh-tribute-and-mtg-discard-costs.md](./research/yugioh-tribute-and-mtg-discard-costs.md), and the current draft design synthesis lives in [design/card-economy-and-rarity.md](./design/card-economy-and-rarity.md). These ideas are being documented for debate first and are not yet canonical `defines/` text.

Later the same day, the user narrowed several of those debate points. The archetype names should remain fantasy-facing, but feel more like player style descriptors than abstract mechanic labels. The late-game wizard-like archetype's hand limit of 12 should apply from the start of the game. The aggressive archetype's reward should be a normal draw, should scale using both monster strength and rarity, and should currently be eligible on every monster kill. For the support archetype, the user pointed back to the earlier cleric-style example already echoed by Quest 003's rescue pattern: when support flips another player's failed save into a success, a card that player would have lost can go to the support player's hand instead of the discard pile. The remaining debate now centers less on broad direction and more on final names, reward probabilities, and exact wording.

Later still on 2026-04-21, the user clarified more of the intended structure. The helped player, not the cleric, should choose which saved card transfers to the support player's hand. The late-game hand-cap archetype should keep the normal starting hand recommendation while gaining the larger cap from the start. The aggressive class should treat kills from its own action cards, creature cards, and class-trait damage as valid for its last-hit passive, and the user wants it to gain a new active trait that deals 1 damage once per turn. For now, the reward curve should span a full d6 ladder from roughly 1-in-6 on weak common monsters up to near-guaranteed or guaranteed draws on strong Rare monsters. The user also wants the presentation layer to reflect three escalation zones on the printed tracker, colored green, yellow, and red, with a skull marker at 10, and tiny red circular damage tokens to track HP.

Later still on 2026-04-21, the user proposed a cleaner expression for the aggressive reward model: use `rarity multiplier x monster threat` as the success threshold on a d6, which naturally creates a `1` through `6` reward ladder across common versus Rare monsters and the three planned threat tiers. The user also approved the current internal style-label recommendation of `Daring`, `Patient`, and `Nurturing`, while keeping the player-facing fantasy class names for the vertical slice. In addition, the future Quick Start Guide should be written purely for players inside the fantasy presentation. It should not refer to internal design names or developer-facing abstractions. Instead, it should directly teach setup, quest selection, class selection, class traits, starting draws, round flow, turn structure, and card actions in straightforward human-readable terms.

Later still on 2026-04-21, the user confirmed that the strongest aggressive reward band can be fully guaranteed. A `Threat 3 Rare` monster may therefore reach `6` out of `6` on the reward roll. The user also required that all formulas and mechanics be stated explicitly in player-facing materials because players must compute them directly with dice, tokens, and cards. Work has now begun on [quick-start-guide.md](./quick-start-guide.md) as the baseline fantasy teaching sheet, and future simulations should use that guide and log any ambiguous or undocumented mechanics they discover.

On 2026-04-22, the user standardized several more visible rules for the first printable vertical slice. Trader scenes should reveal the top `5` resource cards and give each player exactly `1` trader interaction in that scene, either a direct `1-for-1` swap or a `Haggle` roll where `1-2` means discard `1` and still trade `1-for-1`, `3-4` means trade `1-for-1`, and `5-6` means trade `1` hand card for `2` trader cards. All classes may make a basic `1`-damage attack instead of playing a card or using an active. The user also changed the active abilities to a stronger direct baseline: `Warrior` active deals `2` damage, `Wizard` active places `2` blue shield tokens on the party or any creature and those shields are spent `1-for-1` before damage, and `Cleric` active heals either `1` party HP or `2` HP to any creature. Class passives should now stack by default, and if stacked copies of the same passive would compete for one rescue-style card transfer, only one transfer happens and ties can be broken by a die roll.

Later the same day, the user standardized the table widgets and scoring direction. Damage tokens should be small red circles placed on surviving damageable cards to show damage already dealt. Party HP should be tracked with a red `d20`. Endgame scoring should keep the name `prestige points` and use Treasure Value instead of a separate kill score. The current scoring split is `Treasure Points` from cards in hand plus player-owned cards on the field, `Glory Points` from claimed hostile and blocking cards, and agenda reward. Treasure Value should roughly track card power from `1` to `7`, while agendas should be decisive enough to swing the final total by around `20` points.

Later still on 2026-04-22, the user approved a first production-facing content scope. The first vertical slice should stay as small as possible for physical printing and cutting: `1` quest, `8` random encounters, `1` scripted mid-game ordeal, `1` scripted final ordeal, `12` enemies, `1` mid-game boss, `1` end-game boss, at least `2` friendly summons, at least `2` artifacts, and at least `3` enchantments including `Miasma` and at least `2` player-played enchantments. Artifacts should use the same card grammar as monsters but with `Attack 0`, and summons should enter play through resource cards such as `Summon Golem`. Expensive cards should use visible costs like discard, sacrifice, or HP payment, with `Rare` cards tending to carry those heavier costs. The user also wants `3`-player mode supported explicitly in the quick start, currently testing from a starting point of `18` party HP and `4` starting cards per player, and wants both `3`- and `4`-player simulations run against the new canon.

Later still, the user requested a structured text template system under [../defines](../defines/README.md) so each deck can be defined in human-readable, machine-readable plain text files with one template per deck and one file per card. The eventual Python card-generation script should be able to rely on those fields for names, stats, costs, treasure values, rules text, and flavor text. The user also made a process requirement explicit: playtests may recommend promotions, but nothing should be auto-promoted from playtesting into canon without explicit user approval.

On 2026-04-22, the user tightened the turn-order wording further. Players choose the order of player actions. Enemy monsters act from strongest to weakest, and any toss-up in that ordering is chosen by the players.

Later on 2026-04-22, the user added a default enemy-AI rule for live play. Enemy monsters should use a legal named active ability instead of a normal attack when possible. If they do attack, they must target friendly creatures first if any legal friendly creature target exists; otherwise they attack the party. Explicit card text can override this default, and future effects such as `silence` may stop an ability from being usable.

Later on 2026-04-22, the user clarified an important scope boundary for the printable content files. Numeric deck counts such as `8` random encounters and `64` action cards are vertical-slice production minimums for what must be printed by the end of the slice, not hard runtime caps on the eventual full game's card libraries. The full encounter deck should eventually be much larger, and the full action deck may grow to around `200` cards. Rules text and quest text should therefore avoid accidentally turning those print minimums into permanent gameplay limits.

On 2026-04-26, the user made final-pass vertical-demo edits to [Heartfire Dragon](../defines/cards/creature-deck/cards/heartfire-dragon.txt) and [Reliquary of Cinders](../defines/cards/encounter-deck/cards/reliquary-of-cinders.txt). The design takeaway is that high-pressure card effects should favor meaningful player choice over imposed luck, especially choices between personal loss and shared party harm. Randomness should make each chosen risk tense, not replace the choice. The production takeaway is that drawing an encounter card is the reveal: players immediately see all text on that card, so the encounter template should not include a separate `Spawn Text` field. Immediate scene setup belongs in `Reveal Text`.

Later on 2026-04-26, a quickstart preservation pass converted [quick-start-guide.md](./quick-start-guide.md) into five player-facing printable reference sections that currently render as ten letter-size pages, and promoted several Quest 007 rulings into player-facing text or card wording. The preserved rules include direct trade definition, escalation-0 prep scene procedure, immediate reward timing, discard-pile wording, threshold-5 reward-draw tax scope, Shrine of Echoes carry-over behavior, support-success agenda examples, sacrifice definition, and the default that excess damage to one target does not spill over unless a card says otherwise. The design docs were also cleaned so current vertical-slice rules are marked as current rather than stale draft directions.

Later on 2026-04-26, work began on the production asset package. [assets/print-and-bundle-package.md](../assets/print-and-bundle-package.md) is now the canonical Edition 0 physical manifest. It defines the printed card counts, quick-start sheets, background table board, vertical escalation meter, player areas, token counts, required dice, bundling groups, and a playability sanity-check gap list. The current identified package gaps are party HP maximum, once-per-scene tracking convention, physical class reference cards, final board art layout, token sheet layout, and card backs. The escalation marker is now a guitar pick.

On 2026-04-28, the print pipeline was updated for FedEx-style duplex printing. The default atlas PDF now uses unmirrored back pages, with `--mirror-backs` available for the old pre-flipped workflow. [assets/scripts/build_duplex_card_atlas_pdf.py](../assets/scripts/build_duplex_card_atlas_pdf.py) now writes a complete atlas PDF plus two email-sized split PDFs by default, and exposes output-path arguments for the complete and split files. [assets/scripts/generate_table_board.py](../assets/scripts/generate_table_board.py) now also writes the three-page board PDF at `assets/generated/print/table-board-pages.pdf`. The atlas and board generators remain separate scripts and share only the small multipage-PDF helper in [assets/scripts/print_pdf_common.py](../assets/scripts/print_pdf_common.py).

Later on 2026-04-28, the rarity vocabulary was cleaned up. Current canon has only `Common` and `Rare` rarity values. Older `Elite` wording was treated as a terminology artifact and replaced in canonical docs, scripts, and card definitions. The useful design idea behind it remains as future signature-card space: unique, quest-unique, or story-defining cards can use explicit copy-count exceptions, fields, or rules text without becoming a third rarity.

## Goals

- Produce a board game that is realistic to design, prototype, and present within one week.
- Reach a nearly complete minimal design quickly enough to test the whole game loop early.
- Evolve that minimal design into a fully playable vertical slice with enough polish for a class project.
- Maintain documentation that supports fast decision-making and reduces repeated context rebuilding.
- Build a system that supports multiple theme packs without changing its core mechanics.
- Keep the rules teachable in roughly a minute at the class/archetype level.
- Finish a full game in roughly 30 to 40 minutes.

## Constraints

- Total project duration is one week.
- The design still contains significant uncertainty.
- The game must be practical to print and assemble.
- Art is expected to be AI-generated rather than hand-produced.
- The workflow should support collaborative iteration between the user and Codex.
- The immediate play group is four people in a classroom context.
- The mechanical core should ideally scale beyond four players.
- Class differences should be mechanically simple but strategically meaningful.
- There is no spatial map board; the game state is tracked through cards, widgets, and status markers.
- The party must survive to avoid losing collectively.

## Principles

- Time is the primary constraint, so scope discipline matters.
- Early completeness matters more than early polish.
- Every major design choice should help the game become testable sooner.
- Documentation should stay lightweight but durable.
- Ambiguity should be captured explicitly as open questions.
- Theme should be swappable without rebuilding the whole rules engine.
- Small asymmetries with large strategic consequences are preferable to rule-heavy exceptions.
- Escalation should matter continuously, not just at the final boss.

## Key Decisions

### Confirmed

1. The project is a board game for a class assignment.
2. The project will be developed over one week.
3. The current work prioritizes finishing and maintaining the Edition 0 printable vertical slice.
4. Art will be fully AI-generated and printed physically.
5. Codex should maintain persistent markdown-based project memory and repository references.
6. The game should work for four classroom players and ideally scale beyond that.
7. The system should support theme packs layered over a shared mechanical core.
8. The initial vertical-slice theme is leaning toward classic D&D-style fantasy.
9. The corrected component structure is four decks or deck-like systems, three classes, and dice.
10. The three class archetypes are aggressive, defensive/cautious, and support/cooperative.
11. The only player-starting differences between classes should be a small number of special traits, likely at least one active and one passive ability each.
12. Those class traits should be simple to explain but strong enough to reshape how each player approaches the game.
13. The four deck systems are world/quest, encounter, resource-artifact-action, and secret agenda.
14. There is no explicit traitor role; tension comes from secret agendas and point competition inside a shared survival frame.
15. The current lose condition is collective death or failure to survive the ordeal sequence.
16. The target playtime is about 30 to 40 minutes.
17. There is no spatial map board; instead the table will use widgets or trackers for escalation and other statuses.
18. The current escalation track runs from 0 to 10.
19. The world/quest system defines the setting frame, threshold events, and at least one light rules modifier.
20. The user wants research on [Stellaris crisis structure](./research/stellaris-crises.md) to inform midpoint and endpoint escalation beats.
21. The user wants research on [Risk and Ticket to Ride secret-objective patterns](./research/secret-objectives-risk-ticket-to-ride.md) to inform the agenda deck.
22. Encounter cards are scene events, not simple fixed threat cards.
23. Events may spawn monsters, hazards, save throws, bargains, or prep windows.
24. The opening tension-0 round should be a prep beat instead of an immediate battle.
25. Action cards should support selfish setup and future advantage outside battle, not only direct combat participation.
26. Emergent relationship storytelling is the guiding principle for the game's feel.
27. The same event may scale across escalation bands by spawning different entity cards.
28. Persistent obstacles and enchantments such as heavy doors or miasma are in scope.
29. Starting hand size is 3 cards.
30. Hand limit is 6 cards.
31. A standard round has two action turns with a draw between them.
32. Each player takes 1 action per turn unless an effect changes that.
33. Each creature attacks or defends once per turn unless an effect changes that.
34. If hurdles remain unresolved at round end, escalation rises by 1 and round-end card effects are then triggered.
35. At escalation 10, the normal turn limit no longer applies.
36. The creature deck now exists as a formal support deck.
37. Encounter creature spawning uses exact names or card-type criteria, not abstract level packages.
38. When criteria are used, players go through the creature deck in order and take the first matching cards.
39. `defines/` should stay rulebook-like and avoid design rationale.
40. Criteria-based creature spawning may include strength references.
41. A future creature taxonomy may use threat or strength values plus an optional minor versus major distinction separate from rarity.
42. The standard draw between turns 1 and 2 happens once per round, not once per encounter, and still happens at round end if the normal draw window was skipped.
43. Party health is tracked with a red `d20`.
44. Damage tokens are small red circles that track damage already dealt to surviving damageable cards.
45. Shield tokens are blue, are removed before damage is applied, and do not persist between scenes unless a card says otherwise.
46. Every class may make a basic attack for `1` damage instead of playing a card or using a class active.
47. Class passives stack by default unless an effect says otherwise.
48. If stacked copies of the same passive would compete for one rescue-style card transfer, only one transfer happens and ties can be broken with a die roll.
49. The Warrior active should deal `2` damage.
50. The Wizard active should place `2` shield tokens on the party or any creature.
51. The Cleric active should heal `1` party HP or `2` HP to any creature.
52. Trader scenes should reveal the top `5` resource cards and give each player exactly one trader interaction in that scene.
53. Haggle should resolve as: `1-2` discard `1` then trade `1-for-1`, `3-4` trade `1-for-1`, `5-6` trade `1` hand card for `2` trader cards.
54. Summoned creatures cannot attack on the turn they are summoned unless a card says otherwise.
55. Artifacts should use the same card grammar as monsters but with `Attack 0`.
56. High-threat boss cards may use a named active ability and still attack on the same turn if their card says so.
57. Endgame scoring should use `prestige points` built from `Treasure Points` in hand plus on-field owned cards, `Glory Points` from claimed hostile and blocking cards, and agenda reward.
58. Treasure Value should scale roughly from `1` to `7`.
59. Agenda rewards should be decisive in final scoring, currently targeting around `20` points.
60. The first vertical slice should include one quest, eight random encounters, one mid-game ordeal, one final ordeal, twelve enemies, a mid-game boss, an end-game boss, at least two summons, at least two artifacts, and at least three enchantments.
61. Three-player mode should be taught explicitly with a higher party HP total and `4` starting cards per player, currently testing from `18` party HP.
62. Card definitions should live in human-readable, machine-readable plain text templates under `defines/`.
63. No playtest finding should be promoted into canon without explicit user approval.
64. Vertical-slice card-count numbers such as `10` random encounters and `80` resource/action cards are current printable counts, not long-term caps on the full game's deck sizes.
65. The full game should eventually support a much larger encounter library and potentially around `200` action cards.
66. Enemy monsters use a legal named active ability before making a normal attack unless card text lets them do both.
67. Enemy monsters target friendly creatures first if possible, and otherwise target the party.
68. High-pressure card effects should generally give players a meaningful choice before randomness resolves the risk.
69. Encounter templates should not include a separate `Spawn Text` field because drawing the encounter card reveals all information on that card; immediate setup belongs in `Reveal Text`.
70. The quickstart should be maintained as printable letter-size reference sheets; the current generated PDF is `10` letter-size pages organized around five player-facing sections.
71. Escalation-0 prep scenes use a normal non-hostile round and clear at round end if no hostile or blocking hurdles exist.
72. Earned scene rewards resolve immediately unless the card says otherwise, then the table finishes the current round structure.
73. Direct trade means swapping `1` hand card with `1` revealed trader card.
74. Excess damage to one target does not carry over to the party or another target unless a card says otherwise.
75. Threshold-5 reward-draw tax in Ashen Depths applies to extra draws from encounter `Reward Text`.
76. The Edition 0 production bundle is tracked in [assets/print-and-bundle-package.md](../assets/print-and-bundle-package.md).
77. The physical package should include a background table board, vertical escalation meter with a guitar-pick arrow, red damage tokens, blue shield tokens, yellow used markers, green reminder markers, printed proxy cards, `1` red `d20`, and `1` d6.
78. Edition 0 cards use the atlas plan in [assets/card-atlas-definition.md](../assets/card-atlas-definition.md): standard cards are `2.125 in x 3.6667 in`, class references span two columns at `4.25 in x 3.6667 in`, quest cards may span a `2 x 2` block at `4.25 in x 7.3334 in`, and the current `16` front atlases cover `186` physical cards, `192` occupied slots, and `0` blank/proxy slots.
79. The standard Edition 0 card-front layout is generated in [defines/card-layout.md](../defines/card-layout.md) from the atlas card size, and current card text fit is checked by [assets/scripts/check_card_text_fit.py](../assets/scripts/check_card_text_fit.py).
80. Resource-card `Reminder Text` is deprecated for Edition 0 and removed from the resource template. Repeated teaching such as cost timing, choose-one modes, combat targets, permanents, and summon sickness belongs in the rules sheets.
81. Printed-materials-only playtests should begin from [assets/printed-materials-index.md](../assets/printed-materials-index.md), using the quickstart, printed cards, package manifest, atlas, and widget definitions only. Design docs, non-printed rule references, and prior playtests should be read only after the run for comparison.
82. Player-facing widget and token definitions live in [assets/widget-and-token-definitions.md](../assets/widget-and-token-definitions.md).
83. Edition 0 card rendering now generates reusable frames, rendered individual card fronts from `defines/cards`, card-back textures, front/back letter-size atlas PNGs, and duplex atlas PDFs under [assets/scripts](../assets/scripts). The atlas generator and board generator stay separate; shared multipage-PDF writing lives in [assets/scripts/print_pdf_common.py](../assets/scripts/print_pdf_common.py). Final AI art should live in `assets/card-art/final/<deck-slug>/<card-id>.png`, with [assets/card-art/AI_ART_HANDOFF.md](../assets/card-art/AI_ART_HANDOFF.md) as the prompt and destination checklist.
84. Agenda cards no longer have a base `Treasure Value` field or printed treasure footer. Agenda scoring comes only from the explicit prestige reward printed on the card.
85. Quest reference cards render as four-slot `2 x 2` cards with larger art and separate Stats, Setup, Escalation, Win, and Lose sections.
86. Class reference cards render as two-slot `2 x 1` cards generated from the quick-start class section, with separate Passive and Active panels, a shared larger body font, and no treasure footer.
87. Encounter cards no longer have a base `Treasure Value` field or printed treasure footer. Encounter rewards are explicit card text, and rendered body fields use extra paragraph spacing.
88. The table organizer board is now generated as three portrait letter pages side by side (`25.5 in x 11 in`). A two-page board was rejected because its safe area is too cramped for the quest reference, decks, widgets, and six full-size shared-party card slots. Generated board pages include corner left/right labels and center seam sigils for assembly, and the seam sigils are drawn above board zones so they stay visible.
89. The generated table board no longer reserves printed discard, trader-stock, or player-score zones. Ordinary discards and trader stock are loose table piles beside the relevant deck or player area, while cards claimed from kills stay in per-player score piles beside each player's own area. The Party HP zone includes a large red d20 icon plus one party shield-token area, the token bank spaces four bought-token colors evenly at the physical `7/8 in` chip diameter, and the escalation widget is a large vertical `0-10` track with no printed needle.
90. Class reference cards now use equal-height Passive and Active panels plus a centered italic flavor footer. Warrior active damage cannot target flying cards or artifacts.
91. Board deck/current-scene placement guides now use the actual standard card footprint (`2.125 in x 3.6667 in`) instead of stretching to each labeled zone. The quest reference guide uses the four-slot quest footprint (`4.25 in x 7.3334 in`).
92. The creature/entity deck now includes `84` printed cards after adding Ash Skulk and Cinder Sapper as new Commons at `4` copies each, Grave Knight as a new Rare at `2` copies, and Kiln Pup as a single-copy unique companion for Ashen Warden. These occupy all former creature proxy slots on `ATLAS-CRE-07`.
93. The resource deck now includes `80` printed cards after filling `ATLAS-REF-02` slots `05-12` with Oathbound Strike (`2` Rare), Borrowed Time (`2` Rare), and Brace Together (`4` Common). The encounter deck now includes `10` random encounters after adding Ember Tax Patrol to `ATLAS-ENC-01` slot `10`; scripted ordeals moved to slots `11-12`.
94. Current print outputs include `assets/generated/print/card-atlases-duplex-complete.pdf`, `assets/generated/print/card-atlases-duplex-part-1.pdf`, `assets/generated/print/card-atlases-duplex-part-2.pdf`, and `assets/generated/print/table-board-pages.pdf`.
95. Current canonical rarity values are `Common` and `Rare` only. `Elite` should not be used as a rarity synonym; special one-off cards should use explicit uniqueness or copy-count rules instead.

### Not Yet Decided

- Exact resolution mechanics for events, monsters, hazards, and persistent scene cards
- Final player count range
- Long-term full-game scoring refinements beyond the Edition 0 prestige model
- Long-term system expansion beyond the current Edition 0 rules core
- Exact functions and card composition of the four deck systems
- Exact dice system
- How players survive or fail within a scene
- Exact mid-escalation and end-escalation events for the first quest
- Whether classes, cards, encounters, or all three scale by tension
- Whether persistent obstacles and enchantments should stay in the creature deck's rules layer or move to a broader entity reserve
- The exact reward table and trigger limits for the aggressive last-hit passive
- The support archetype's matching economy-facing identity hook in this new pass
- The final presentation details for damage tokens and escalation-track printing
- Final proof results for FedEx duplex alignment and cutting
- Testing cadence

## Open Questions

- What is the game's core concept and player fantasy?
- What is the intended player count range beyond the known four-player classroom case?
- What iteration, if any, is needed after the next printed proof?
- How exactly do players resolve a scene each round when that scene may be combat, hazard, social, or persistent?
- How do dice enter the system: save throws, combat, card effects, or all three?
- What are points actually measuring, and how are they awarded?
- What specific secret agenda patterns create tension without making cooperation collapse?
- Is the HOI4-style tension meter a literal shared track, or more of a design inspiration for threshold-based escalation? Current evidence suggests a literal shared track from 0 to 10, but its exact effects remain open.
- What is the precise economy or resource model that the aggressive, cautious, and support classes are manipulating?
- What exact stats or tags should monster cards, persistent scene cards, and allied entity cards share?
- What exact fields should future monster, resource, archetype, quest, and encounter JSON structures contain once design debate is done?
- How much of the persistent obstacle and enchantment layer belongs inside the creature deck versus a broader entity reserve?
- How should hero credit or narrative spotlight be awarded when several players contributed to the same scene?
- What concrete gameplay promises should `Common` and `Rare` make as the card pool grows?
- How reliable should the aggressive archetype's last-hit card gain be before it starts encouraging unhealthy sandbagging?
- What exact wording should govern the support archetype's rescue-and-claim card flow when it saves another player from a failed ordeal?
- What kind of AI art style best fits the game and printing constraints?
- What rubric or evaluation criteria does the class project need to satisfy?

## Near-Term Plan

1. Keep the print pipeline reproducible for card atlases, board pages, and quick-start sheets.
2. Proof the current FedEx-oriented PDFs for scale, duplex orientation, and cut alignment.
3. Resolve remaining production gaps only when they affect the printed classroom prototype.
4. Use printed-materials-only playtests to find rules or component gaps that are invisible in design docs.
5. Promote changes into canonical docs only after review.

## Documentation Notes

- Update this file whenever durable project understanding changes.
- Link major decisions to the relevant files when those files exist.
- Reflect repository structure changes through [repository-directory.md](./repository-directory.md).
