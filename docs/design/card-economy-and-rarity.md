# Card Economy And Rarity

This file captures the current draft direction for card costs, shared rarity language, and related archetype questions. It is design intent, not canon rules text. The broader game brief lives in [core-concept.md](./core-concept.md). The deck model lives in [deck-architecture.md](./deck-architecture.md). External research for this file lives in [../research/yugioh-tribute-and-mtg-discard-costs.md](../research/yugioh-tribute-and-mtg-discard-costs.md).

## Draft Goal

The user wants powerful cards to feel expensive because they ask players to give something up now, not because they wait for a mana curve. In this model, cost comes primarily from:

- discarding cards from hand
- sacrificing allied creatures, setup pieces, or stored assets
- giving up future value to gain immediate swing

The design target is that weak or moderate cards feel immediate, while strong cards feel committed.

## Draft Shared Rarity Direction

The current direction is to standardize both resource cards and monster cards under the same two-rarity field.

### Recommended Working Labels

- `common`
- `elite`

These are recommended because they work for both sides of the game:

- a `common` monster or card reads as lower pressure and lower spectacle
- an `elite` monster or card reads as more defining, more costly, or more dangerous

### Alternate Label Pairs Worth Debating

- `minor` / `major`
- `standard` / `rare`
- `lesser` / `greater`

## Draft Mechanical Meaning Of Rarity

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

## Draft Archetype Hooks Under This Economy

### Late-Game Wizard-Like Archetype

Current requested direction:

- max hand size `12` instead of `6`
- this larger cap is active from the start of the game

This strongly supports a stockpiling, patience, and delayed-burst identity. It also pairs naturally with discard costs because the archetype can afford to hold expensive lines until the right moment.

### Aggressive Warrior-Like Archetype

Current requested direction:

- chance to gain a normal draw from scoring the last hit on a monster
- that chance should scale using both monster strength and monster rarity
- the user currently wants this available on every monster kill
- the kill must come from that player's own card or class-trait damage
- the archetype also wants an active trait that deals `1` damage once per turn

This creates a vivid rivalry loop, especially in a game that already tracks hero credit and Spotlight-like recognition.

### Draft Warrior Reward Formula

The cleanest current expression is:

- treat `common` rarity as multiplier `1`
- treat `elite` rarity as multiplier `2`
- use monster threat tiers `1`, `2`, and `3`
- when the warrior scores the last hit on a monster, roll a d6
- gain a normal draw if the result is less than or equal to `rarity multiplier x threat`

That produces this ladder:

- `Threat 1 Common`: succeed on `1`
- `Threat 2 Common`: succeed on `1-2`
- `Threat 3 Common`: succeed on `1-3`
- `Threat 1 Elite`: succeed on `1-2`
- `Threat 2 Elite`: succeed on `1-4`
- `Threat 3 Elite`: succeed on `1-6`

This is stronger and cleaner than the earlier table because it can be explained by one formula instead of six disconnected cases, and it naturally reaches full certainty on the strongest elite monsters.

### Support Archetype

The strongest current support direction comes from the user's earlier cleric example and from the lighter rescue effect tested in Quest 003:

- the support archetype helps another player pass a save or avoid a loss
- the helped player chooses `1` card that would have been lost, and that card goes to the support player's hand instead of to discard

That gives support a real economy engine, but one rooted in intervention rather than hoarding or kill credit.

## Canonization Questions

1. Should `elite` always imply round-end text more often, or only "can be used as a search filter"?
2. Should the support rescue rule trigger only on flipped save failures, or more broadly on any prevented allied loss?
3. Does the support rescue transfer only `1` card even if several would be lost?
4. Does the `12`-hand archetype need a compensating weakness, or is the class already naturally balanced by slower tempo and delayed play?

## Current Recommendation Before Defines

Do not canonize numbers for rarity behavior yet. The safer next step is to agree on:

1. the shared rarity labels
2. the support rescue wording
3. whether elite has stronger round-end expectations by default
4. whether the wizard needs a real drawback for its larger hand cap
