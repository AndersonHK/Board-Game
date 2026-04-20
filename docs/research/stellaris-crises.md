# Research: Stellaris Crises

This note captures the parts of Stellaris midgame and endgame crises that seem relevant to the current project. The design docs that reference this note live in [../design/core-concept.md](../design/core-concept.md), [../design/deck-architecture.md](../design/deck-architecture.md), and [../design/round-structure.md](../design/round-structure.md). The research index lives in [research-index.md](./research-index.md).

## Why This Matters

The user asked for research on Stellaris midgame and endgame crises as context for the world or quest system. The useful pattern is staged escalation with major threshold events that visibly change the shape of the game.

## Key Insights

1. Stellaris separates midgame crises from endgame crises; the midpoint events reshape the galaxy, but the endpoint events are existential.
2. Crises are not just stronger enemies. They alter diplomacy, priorities, and what the whole table or galaxy must react to.
3. Endgame crises are paced through buildup, warning, arrival, spread, and eventual resolution rather than appearing all at once with no foreshadowing.
4. A crisis can create a unifying threat that temporarily overrides ordinary rivalry.
5. Stellaris tracks crisis progress and aftermath publicly, which makes the shared pressure legible.
6. Different crises create different kinds of pressure, but the high-level structure is consistent: warning signs, threshold crossing, new rules pressure, coordinated response.

## Particularly Relevant Details

- The current fan-maintained Stellaris wiki distinguishes smaller-impact midgame crises from more existential endgame crises.
- Endgame crises only appear after threshold conditions are met and then check periodically for arrival, which creates a sense of looming inevitability rather than exact certainty.
- Once an endgame crisis arrives, broader galactic coordination tools unlock and ordinary factions become more likely to unite against it.
- Crisis arrival can add a public progress tracker, casualty count, or other shared information about the emergency.

## Design Relevance For This Project

- The quest system should probably have at least two dramatic thresholds: a midpoint disruption and a climax.
- Those thresholds should change decision-making, not just increase numbers.
- A midpoint event could change what encounters appear, how action cards resolve, or what the party must prioritize.
- A final escalation at tension 10 should feel like the whole scenario snapping into its end state.
- Public threshold markers help players plan around escalation and argue about timing.

## Candidate Adaptations

- tension 5 or 6: "midgame crisis" card or quest event enters play and changes a core rule
- tension 10: final ordeal or boss fight begins
- public quest tracker showing current phase and upcoming threshold effects
- crisis text that changes all encounters or all class actives until resolved

## Cautions

- The board game should borrow the phase-shift lesson, not Stellaris's content volume.
- For a 30 to 40 minute session, one midpoint and one endpoint twist is probably enough.
- If the thresholds are too random or too punitive, players may feel punished for engaging with the core system.

## Sources

- [Crisis - Stellaris Wiki (Fandom)](https://stellaris.fandom.com/wiki/Crisis)

## Confidence Notes

I found a detailed current summary on the Stellaris Fandom wiki rather than the Paradox wiki, which was difficult to access cleanly in this environment. That is sufficient for structural inspiration, but if later design work depends on patch-specific details, the exact current official wiki pages should be rechecked.
