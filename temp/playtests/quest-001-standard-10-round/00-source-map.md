# Quest 001 Source Map

This file distills the current rules shape for the first resolution simulation. It is not a rules doc. It is a working extraction from the current design docs plus provisional assumptions needed to run one mock session.

## Source Anchors

- Four public systems: quest frame, encounter deck, resource-action deck, and secret agendas ([deck-architecture](../../../docs/design/deck-architecture.md)).
- Shared survival condition inside private scoring pressure ([core-concept](../../../docs/design/core-concept.md)).
- Three archetypes with one passive and one active effect each, kept short and strategically visible ([class-archetypes](../../../docs/design/class-archetypes.md), [hearthstone-hero-powers research](../../../docs/research/hearthstone-hero-powers.md), [civilization-traits research](../../../docs/research/civilization-traits-and-unique-abilities.md)).
- Round flow hypothesis: reveal encounter, deal with it, play actions, raise tension by 1 ([round-structure](../../../docs/design/round-structure.md)).
- Shared escalation track from 0 to 10 with meaningful threshold events rather than constant bespoke rules ([core-concept](../../../docs/design/core-concept.md), [round-structure](../../../docs/design/round-structure.md), [HOI4 world tension research](../../../docs/research/hearts-of-iron-iv-world-tension.md), [Stellaris crises research](../../../docs/research/stellaris-crises.md)).

## Distilled Rules Used In This Simulation

1. The party shares a single lose condition and a single health track for this pass. If party HP reaches 0, everyone loses ([core-concept](../../../docs/design/core-concept.md)).
2. The quest uses a 10-step tension arc with one midpoint phase shift and one final climax ([core-concept](../../../docs/design/core-concept.md), [round-structure](../../../docs/design/round-structure.md), [stellaris-crises research](../../../docs/research/stellaris-crises.md)).
3. Encounters are represented as one threat target per round. Players solve that target by committing cards and class abilities.
4. Aggressive, defensive, and support classes should feel different from round 2 or 3 onward, not only in rare situations ([class-archetypes](../../../docs/design/class-archetypes.md)).
5. Secret agendas should distort incentives without making the party implode ([deck-architecture](../../../docs/design/deck-architecture.md), [secret-objectives research](../../../docs/research/secret-objectives-risk-ticket-to-ride.md)).

## Explicit v0 Numbers For The Run

- Party HP: 14
- Per-player HP: not used
- Starting hand: 3 cards each
- Baseline draw: 1 card each at end of round
- Encounter failure damage: equal to final shortfall
- Encounter uncertainty: after commitments, roll 1d6
  - 1-2 = -1 total impact
  - 3-4 = no change
  - 5-6 = +1 total impact
- Boss format: single-round threat check only

## Systems Still Undefined In The Canonical Docs

- Whether the resource pool is a closed finite deck or a library of repeatable templates
- How scoring works beyond hidden agendas
- How encounter rewards are claimed
- Whether utility cards can solve non-combat encounters using the same threat language as combat cards
- Exact timing of threshold events
- Whether damage prevention changes success state or only HP loss
- Whether there is a hand limit
- Whether bosses need their own HP or multi-round structure

Each of those gaps is patched in the simulation log and rulings log as needed rather than treated as settled design.
