# Project Memory

This file is the long-term memory for the project. It should retain the durable context needed to resume work cleanly across sessions. Repository structure and canonical file locations are tracked in [repository-directory.md](./repository-directory.md). Repo-wide Codex instructions live in [../CODEX.md](../CODEX.md).

## Snapshot

- Project: class board game project
- Timeline: one week total
- Collaboration model: user provides the evolving vision; Codex helps design, document, structure, and iterate
- Delivery strategy: build a nearly complete minimal horizontal slice first, then turn it into a fully playable vertical slice
- Art plan: use fully AI-generated art that the user can print for the physical game
- Current phase: early concept definition, rules correction, and simulation-driven prototyping

## Current Understanding

On 2026-04-20, the user said we are designing a class board game together under a one-week time budget. Many design details remain uncertain, so the process should favor a nearly complete minimal horizontal slice first, then a fully playable vertical slice. The art will be fully AI-generated and later printed. The user asked for persistent markdown-based project memory, a repository directory reference, and a root [../CODEX.md](../CODEX.md) that tells Codex to keep these files current and cross-referenced.

Later on 2026-04-20, the user added the first real concept brief. The game should support the immediate classroom context of four players but ideally scale beyond that. The user cited [research on Betrayal at House on the Hill](./research/research-index.md#betrayal-at-house-on-the-hill), [research on the Hearts of Iron IV world tension meter](./research/research-index.md#hearts-of-iron-iv-world-tension), [research on Hearthstone hero powers](./research/research-index.md#hearthstone-hero-powers-and-lightweight-asymmetry), and [research on Civilization traits and unique abilities](./research/research-index.md#civilization-traits-and-unique-abilities) as important mechanical reference points.

The game is intended to be system-agnostic across theme packs. The same mechanical skeleton should support fantasy, sci-fi, steampunk, grimdark, and similar settings, while the flavor names and presentation change. For the first vertical-slice demo, the user is leaning toward a classic D&D-like fantasy setting. A fuller evolving brief is tracked in [design/core-concept.md](./design/core-concept.md), current class identity notes live in [design/class-archetypes.md](./design/class-archetypes.md), and the deck model lives in [design/deck-architecture.md](./design/deck-architecture.md).

Later on 2026-04-20, the user corrected the component structure: the game actually has four decks or deck-like systems, not three. The four are the [world or quest system](./design/deck-architecture.md#world--quest-system), [encounter deck](./design/deck-architecture.md#encounter-deck), [resource-artifact-action deck](./design/deck-architecture.md#resource--artifact--action-deck), and [secret agenda deck](./design/deck-architecture.md#secret-agenda-deck). The game has no explicit traitor. All players are in the same party and share the lose condition of survival, but each player also has a secret agenda and wants to finish with the most points. The current round-flow hypothesis and escalation model are tracked in [design/round-structure.md](./design/round-structure.md).

Later on 2026-04-20, the user corrected a more important misunderstanding in the earlier prototype framing. Encounter cards should not be treated as fixed threat-value cards. They are event or scene cards that may spawn monster cards, force save throws, trigger discards, create bargains, or open preparation windows. Monster cards and player-controlled allied entities such as familiars or golems should likely share a common rules grammar rather than becoming a separate fifth core deck immediately. The action deck should include both battle tools and selfish setup cards that can be used outside battle, so a greedy player can spend time improving their own future position instead of merely skipping help. The desired experience is emergent relationship storytelling: players should feel invested in who was brave, selfish, rescued, indebted, or resentful by the end of the story.

Later that same day, the user clarified that the same event can scale across escalation bands by spawning different enemy cards, such as goblins at low tension, orcs at mid tension, and an ogre at high tension. The user also asked us to design toward the possibility of an auxiliary enemy or entity reserve that could hold monster cards, persistent obstacles like heavy doors, and persistent enchantments like miasma. Those ideas are not yet confirmed as a formal fifth deck, but they are now part of the working direction tracked in [design/core-concept.md](./design/core-concept.md), [design/deck-architecture.md](./design/deck-architecture.md), and [design/round-structure.md](./design/round-structure.md).

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
3. The team will prioritize a nearly complete horizontal slice before a fuller vertical slice.
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

### Not Yet Decided

- Exact resolution mechanics for events, monsters, hazards, and persistent scene cards
- Final player count range
- Final scoring and point model
- Core mechanics
- Exact functions and card composition of the four deck systems
- Exact dice system
- How players survive or fail within a scene
- Exact mid-escalation and end-escalation events for the first quest
- Whether classes, cards, encounters, or all three scale by tension
- Whether the game needs a formal enemy or entity reserve in addition to the four core decks
- Print format requirements
- Testing cadence

## Open Questions

- What is the game's core concept and player fantasy?
- What is the intended player count range beyond the known four-player classroom case?
- What is the minimum loop required for the first horizontal slice?
- How exactly do players resolve a scene each round when that scene may be combat, hazard, social, or persistent?
- How do dice enter the system: save throws, combat, card effects, or all three?
- What are points actually measuring, and how are they awarded?
- What specific secret agenda patterns create tension without making cooperation collapse?
- Is the HOI4-style tension meter a literal shared track, or more of a design inspiration for threshold-based escalation? Current evidence suggests a literal shared track from 0 to 10, but its exact effects remain open.
- What is the precise economy or resource model that the aggressive, cautious, and support classes are manipulating?
- What exact stats or tags should monster cards, persistent scene cards, and allied entity cards share?
- How should hero credit or narrative spotlight be awarded when several players contributed to the same scene?
- What kind of AI art style best fits the game and printing constraints?
- What rubric or evaluation criteria does the class project need to satisfy?

## Near-Term Plan

1. Receive the user's game overview.
2. Convert that overview into a concise design brief in [design/core-concept.md](./design/core-concept.md).
3. Capture the class identity model in [design/class-archetypes.md](./design/class-archetypes.md).
4. Research the cited inspirations and store takeaways in [research/research-index.md](./research/research-index.md).
5. Capture the four-deck model in [design/deck-architecture.md](./design/deck-architecture.md).
6. Capture the current round and escalation model in [design/round-structure.md](./design/round-structure.md).
7. Identify the smallest end-to-end playable loop.
8. Use simulation passes to test that loop and correct misunderstandings quickly.
9. Lock the first horizontal-slice scope.
10. Create component, rules, and production docs as needed.

## Documentation Notes

- Update this file whenever durable project understanding changes.
- Link major decisions to the relevant files when those files exist.
- Reflect repository structure changes through [repository-directory.md](./repository-directory.md).
