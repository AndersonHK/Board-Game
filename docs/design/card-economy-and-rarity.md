# Card Economy And Rarity

This file captures the current cost philosophy, shared rarity language, and economy-facing class hooks. Canonical player-facing rules live in [../../defines](../../defines/README.md) and [../quick-start-guide.md](../quick-start-guide.md); this document preserves the design reasons and balance risks behind those rules. The broader game brief lives in [core-concept.md](./core-concept.md). The deck model lives in [deck-architecture.md](./deck-architecture.md). External research for this file lives in [../research/yugioh-tribute-and-mtg-discard-costs.md](../research/yugioh-tribute-and-mtg-discard-costs.md).

## Cost Goal

The user wants powerful cards to feel expensive because they ask players to give something up now, not because they wait for a mana curve. In this model, cost comes primarily from:

- discarding cards from hand
- sacrificing allied creatures, setup pieces, or stored assets
- giving up future value to gain immediate swing

The design target is that weak or moderate cards feel immediate, while strong cards feel committed.

## Current Shared Rarity Direction

The current vertical-slice direction standardizes both resource cards and monster cards under the same two-rarity field.

### Current Labels

- `Common`
- `Elite`

These work for both sides of the game:

- a `Common` monster or card reads as lower pressure and lower spectacle
- an `Elite` monster or card reads as more defining, more costly, or more dangerous

### Older Label Pairs

Earlier candidate pairs included `minor` / `major`, `standard` / `rare`, and `lesser` / `greater`. They are useful historical context, but the current vertical slice teaches `Common` and `Elite`.

## Mechanical Meaning Of Rarity

### Common

- lower immediate ceiling
- more likely to be played instantly
- less likely to carry round-end text
- more likely to be valid for broad search criteria

### Elite

- stronger swing or stronger persistence
- more likely to require discard or sacrifice to unlock full value
- more likely to carry round-end text
- more likely to matter for encounter scripting and climax pressure

This does not mean every elite card must be slow, only that elite should correlate with stronger impact and more meaningful consequence.

## Cost Philosophy

The current recommendation is:

- cheap cards should be fast, narrow, and flexible
- expensive cards should be decisive, persistent, or explosive
- heavy costs should be visible and paid by the acting player
- discard should usually be chosen by the acting player, not random
- sacrifice should usually hit real board assets, not abstract counters only

That structure fits the user's direction and the external research better than a hidden resource pool would.

## Simulation-Informed Considerations

The latest stress test in [../../temp/playtests/quest-003-canon-stress-test-10-round/09-findings.md](../../temp/playtests/quest-003-canon-stress-test-10-round/09-findings.md) and its supporting logs give three relevant warnings.

### Hand Size Pressure Already Works

The tested baseline of `3` starting cards and a hand limit of `6` already produced meaningful pressure without starving the table. Brin even had to discard back down after a greed spike. Because of that, moving one archetype from `6` to `12` is not a small tweak. It is a major asymmetry that will strongly affect hoarding, discard tolerance, and the value of delayed power cards.

### Kill Credit Already Creates Delay Incentives

Brin repeatedly waited for safe last-hit windows or reward windows instead of contributing early. That means a kill-based aggressive passive can be exciting, but it can also intensify sandbagging if the trigger is too reliable or too profitable.

### The Climax Was Better Because Draws Stayed Tight

Quest 003 held together in the final ordeal partly because escalation 10 did not become a refill engine. Any economy changes that accidentally give too much extra draw or too much hand retention in the climax risk flattening that tension.

## Current Archetype Hooks Under This Economy

### Wizard Storage Hook

Current vertical-slice rule:

- max hand size `12` instead of `6`
- this larger cap is active from the start of the game
- normal starting hand still applies; the larger cap affects cleanup and retention, not initial draw or standard draw cadence

This strongly supports a stockpiling, patience, and delayed-burst identity. It also pairs naturally with discard costs because the archetype can afford to hold expensive lines until the right moment.

### Warrior Kill-Credit Hook

Current vertical-slice rule:

- chance to gain a normal draw from scoring the last hit on a monster
- that chance scales using monster `Threat` and monster rarity
- this is available on every monster kill in the current quickstart
- the kill must come from that player's own card or class-trait damage
- the active trait deals `2` damage once per turn

This creates a vivid rivalry loop, especially in a game that already tracks hero credit and Spotlight-like recognition.

### Warrior Reward Formula

The current expression is:

- treat `Common` rarity as multiplier `1`
- treat `Elite` rarity as multiplier `2`
- use monster threat tiers `1`, `2`, and `3`
- when the Warrior scores the last hit on a monster, roll a d6
- gain a normal draw if the result is less than or equal to `rarity multiplier x threat`

That produces this ladder:

- `Threat 1 Common`: succeed on `1`
- `Threat 2 Common`: succeed on `1-2`
- `Threat 3 Common`: succeed on `1-3`
- `Threat 1 Elite`: succeed on `1-2`
- `Threat 2 Elite`: succeed on `1-4`
- `Threat 3 Elite`: succeed on `1-6`

This is stronger and cleaner than the earlier table because it can be explained by one formula instead of six disconnected cases, and it naturally reaches full certainty on the strongest elite monsters.

The design reason for the exact numbers is that every combination maps cleanly onto a `d6`, producing a full `1` through `6` reward ladder without another lookup table. It also makes low-threat common kills mildly tempting, mid-tier kills meaningfully tempting, and the final or elite kills feel like visible credit events.

### Cleric Support Hook

Current vertical-slice rule:

- the support archetype helps another player pass a save
- the helped player chooses `1` card that would have been lost, and that card goes to the support player's hand instead of to discard

That gives support a real economy engine, but one rooted in intervention rather than hoarding or kill credit.

## Canonization Questions

1. Should `Elite` always imply round-end text more often, or only remain a power/copy-count/search signal?
2. Should future support designs broaden rescue beyond flipped save failures, or keep the Cleric passive narrow?
3. Does the `12`-hand archetype need a compensating weakness, or is the class already naturally balanced by slower tempo and delayed play?
4. Does Wizard Treasure scoring need adjustment if retained cards and owned permanents beat high Glory scores too often?

## Current Recommendation

Keep the vertical-slice numbers stable through the release demo unless playtesting reveals a clear failure. The risky parts are now balance questions, not missing rules:

1. Warrior kill credit should stay exciting without making players wait for last hits too often.
2. Wizard retention should feel powerful without making Treasure scoring the default best route.
3. Cleric rescue should feel profitable enough that support can win without becoming a pure kingmaker.
