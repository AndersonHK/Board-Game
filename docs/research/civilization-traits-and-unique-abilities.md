# Research: Civilization Traits and Unique Abilities

This note captures the parts of Civilization's trait and unique-ability design that seem relevant to the current project. The design brief that references this research lives in [../design/core-concept.md](../design/core-concept.md). The class design that references this research lives in [../design/class-archetypes.md](../design/class-archetypes.md). The research index lives in [research-index.md](./research-index.md).

## Why This Matters

The user pointed to Civilization traits as an example of small mechanical changes that cause major long-term differences because the surrounding systems compound over time.

## Key Insights

1. Civilization-style asymmetry often modifies only one or two rules, but those rules sit on high-leverage economic loops.
2. Because the base game compounds over many turns, even tiny edges strongly influence long-run development.
3. Good traits do not need many exceptions; they need to touch decisions that recur constantly.
4. Traits can express identity through incentives: what the player wants to invest in, protect, or exploit.
5. Different eras of Civilization handle this differently, but the important shared lesson is light rules text with heavy strategic consequences.

## Cross-Series Notes

- In Civilization III, civilization traits such as Militaristic, Commercial, Scientific, Religious, and Industrious changed broad tendencies through a couple of persistent bonuses.
- In Civilization IV, leaders commonly had two traits, each with compact bonuses such as free promotions, extra culture, faster workers, or reduced building-production costs.
- In Civilization V, unique abilities replaced the earlier trait model with more bespoke faction rules, but many still remained short and strategically defining.

## Particularly Relevant Examples

- Civ IV Aggressive: a simple free combat promotion plus cheaper military infrastructure changes military tempo and unit value.
- Civ IV Creative: passive culture generation changes border growth and city planning from turn one.
- Civ V India's ability changes the city-count versus population tradeoff, altering whether the faction wants to play wide or tall.
- Civ V Sweden's friendship-related bonus directly incentivizes diplomacy and mutual benefit.

## Design Relevance For This Project

- The class layer should attach to repeated decisions, not corner cases.
- The aggressive / cautious / support split can be reinforced through tiny changes to gain, storage, or exchange rules.
- The best abilities will not feel dramatic because they are long; they will feel dramatic because they bend the whole incentive landscape.
- A balanced base system is essential, because these asymmetries rely on leverage rather than brute force.

## Candidate Adaptations

- aggressive gets a favorable conversion rate on risky actions
- defensive gets better retention or less loss from common setbacks
- support gets extra value whenever an action benefits more than one player

## Cautions

- If a trait changes a low-frequency rule, it will feel forgettable.
- If a trait alters too many numbers at once, it stops being elegant and becomes a separate ruleset.
- Physical tabletop play benefits from asymmetries that players can understand at a glance.

## Sources

- [Civilization III: Info Center - Civilization Abilities](https://civfanatics.com/civ3/infocenter/)
- [Civilization IV: Civilizations](https://civfanatics.com/civ4/civilopedia/civilizations/)
- [Leader trait (Civ4)](https://civilization.fandom.com/wiki/Leader_trait_%28Civ4%29)
- [Civilization V: Civilizations](https://civfanatics.com/civ5/info/civilizations/)
- [Unique ability (Civ5)](https://civilization.fandom.com/wiki/Unique_ability_%28Civ5%29)

## Confidence Notes

This note synthesizes multiple references across the series. The specific numeric examples differ by title, but the pattern of compact asymmetry with compounding impact is clear.
