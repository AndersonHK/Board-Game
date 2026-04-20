# Research: Hearts of Iron IV World Tension

This note captures the parts of the Hearts of Iron IV world tension system that seem relevant to the current project. The design brief that references this research lives in [../design/core-concept.md](../design/core-concept.md). The research index lives in [research-index.md](./research-index.md).

## Why This Matters

The user specifically cited the "world tension meter gameplay dynamic." The useful pattern here is a shared global meter that changes what players are allowed, encouraged, or forced to do as the game escalates.

## Key Insights

1. World tension is a shared table-state variable represented from 0% to 100%.
2. Aggressive actions increase the meter; peace-oriented outcomes and decay can reduce it over time.
3. The meter does not just track mood. It gates actions and unlocks stronger options at specific thresholds.
4. Different factions or ideologies respond differently to the same threshold, so one shared meter creates asymmetric consequences.
5. Rising tension speeds up conflict systems and normalizes stronger responses.
6. Because everyone watches the same track, individual aggression produces collective consequences.

## Particularly Relevant Details

From the wiki summary:

- world tension increases from actions like declaring war, justifying war goals, joining factions, and joining wars as an attacker
- it can decrease through peace outcomes and passive decay
- each percentage point affects broader systems, including war-goal timing and war support
- certain actions require minimum thresholds such as 25%, 40%, 50%, 80%, or 100%, depending on ideology and action type

## Design Relevance For This Project

- A shared escalation track could elegantly synchronize the pacing of all three archetypes.
- The aggressive class can be tempted to raise tension for short-term gain.
- The defensive/cautious class can prefer lower tension while building toward a late payoff.
- The support class can broker around the consequences of threshold changes or profit from collective stability.
- Thresholds are a clean way to add drama without adding many rules exceptions.

## Candidate Adaptations

- a public "tension" or "chaos" meter that rises when players attack, betray, hoard, or trigger certain deck effects
- threshold bands that unlock stronger cards, harsher monsters, or broader interaction options
- class abilities that care differently about the current tension band
- tension decay between rounds to create timing windows

## Cautions

- A shared meter only works if players can meaningfully influence it and care about its thresholds.
- If the meter affects too many subsystems, the game teach could become muddy.
- The best adaptation is probably a very small number of threshold bands with clear consequences.

## Sources

- [World tension - Hearts of Iron 4 Wiki](https://hoi4.paradoxwikis.com/World_tension)

## Confidence Notes

This note relies on a community-maintained wiki, which is appropriate for system-level understanding. The design lesson here is conceptual rather than dependent on patch-precise numbers.
