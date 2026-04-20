# Research: Secret Objectives in Risk and Ticket to Ride

This note captures the parts of Risk secret missions and Ticket to Ride tickets that seem relevant to the current project. The design docs that reference this note live in [../design/core-concept.md](../design/core-concept.md) and [../design/deck-architecture.md](../design/deck-architecture.md). The research index lives in [research-index.md](./research-index.md).

## Why This Matters

The user asked for research on Risk quests and Ticket to Ride objectives as models for the secret agenda deck. The shared lesson is that private goals can create selfish incentives inside a public game state.

## Key Insights

1. Secret objectives are powerful because other players can see your behavior but not your exact motive.
2. Risk uses secret mission victory cards to accelerate the game and give each player a hidden personal win target.
3. Ticket to Ride uses hidden tickets that remain secret until the end of the game and score positive if completed and negative if failed.
4. Ticket to Ride also forces a keep decision: players are dealt multiple tickets and must keep at least some of them, which creates commitment and uncertainty.
5. Hidden objectives work especially well when pursuing them still uses the same public actions everyone else is using.
6. Negative scoring for unfinished goals is a useful way to make goals matter without requiring instant revelation.

## Particularly Relevant Details

- Hasbro's Risk product description says the updated game includes improved mission cards and that the player who completes a secret mission first reveals it to prove the win.
- The current Ticket to Ride rulebook says each player starts with 4 tickets, must keep at least 2, keeps them secret, and later may draw 3 more and must keep at least 1.
- Ticket to Ride scoring adds completed ticket values and subtracts incomplete ticket values at the end of the game.

## Design Relevance For This Project

- Secret agendas can create traitor-like suspicion without requiring a true traitor.
- The best agendas will be achievable through ordinary play actions, not through isolated mini-games.
- Endgame point scoring may work better than instant-win objectives, because this game still has a shared survival requirement.
- A keep-one-or-keep-some structure could make agendas feel chosen without introducing a long draft.
- Agendas that create slight selfish distortions are safer than agendas that demand direct sabotage every game.

## Candidate Adaptations

- each player draws 2 or 3 agenda cards after picking a class and keeps 1
- agendas remain hidden until the end unless voluntarily revealed
- completed agendas grant points; failed agendas may grant nothing or a small penalty
- agendas push players toward kills, hoarding, rescue, timing, or comparative status

## Cautions

- If agendas are too adversarial, the party-survival structure collapses.
- If agendas are too soft, players will ignore them.
- If agenda scoring is too opaque, the endgame may feel arbitrary.

## Sources

- [Risk Game instructions page - Hasbro](https://instructions.hasbro.com/en-my/instruction/hasbro-risk-game)
- [Ticket to Ride - Days of Wonder](https://www.daysofwonder.com/game/ticket-to-ride/)
- [Ticket to Ride English rulebook PDF](https://cdn.svc.asmodee.net/production-daysofwonder/uploads/2025/07/7201N_TICKET2RIDEV2_RULES_EN_20250425_WEB.pdf)

## Confidence Notes

The Ticket to Ride details come from the current official rulebook. For Risk, I could confirm the existence and role of secret missions from Hasbro's instructions page, but I did not retrieve the full mission-card text in this environment, so this note focuses on the structural lesson rather than exact mission wording.
