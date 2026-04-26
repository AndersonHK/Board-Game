# AI Art Session Groups

Use these files to run parallel art-generation sessions. Tell each session its exact task group ID and have it open only that group file.

Session instruction template:

```text
You are assigned TASK_GROUP_ID. Open assets/card-art/session-groups/TASK_GROUP_ID.md and generate only the cards listed there. When choosing final images, use only images generated in this current session or staged under assets/card-art/incoming/TASK_GROUP_ID/. Do not inspect, search, copy, or reuse images from other generated-image session folders, task-group folders, or existing final-art folders. Save each final PNG to its listed Destination Path. Do not edit card definition files or generate cards from other groups.
```

| Task Group | Scope | Cards | Handoff File |
| --- | --- | ---: | --- |
| `GROUP-STORY` | Quest and secret agenda art | `7` | `assets/card-art/session-groups/GROUP-STORY.md` |
| `GROUP-ENCOUNTER` | Encounter scene art | `12` | `assets/card-art/session-groups/GROUP-ENCOUNTER.md` |
| `GROUP-CREATURE-01` | Creature and entity art | `10` | `assets/card-art/session-groups/GROUP-CREATURE-01.md` |
| `GROUP-CREATURE-02` | Creature and entity art | `10` | `assets/card-art/session-groups/GROUP-CREATURE-02.md` |
| `GROUP-CREATURE-03` | Creature and entity art | `10` | `assets/card-art/session-groups/GROUP-CREATURE-03.md` |
| `GROUP-RESOURCE-01` | Resource/action art | `13` | `assets/card-art/session-groups/GROUP-RESOURCE-01.md` |
| `GROUP-RESOURCE-02` | Resource/action art | `12` | `assets/card-art/session-groups/GROUP-RESOURCE-02.md` |
| `GROUP-CLASS` | Class reference art | `3` | `assets/card-art/session-groups/GROUP-CLASS.md` |
