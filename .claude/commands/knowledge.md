---
description: Save insights from or retrieve past insights for the current conversation
---

# /knowledge Workflow

## Usage

- `/knowledge` or `/knowledge retrieve` — search past insights relevant to the current topic
- `/knowledge save` — capture insights from the current conversation

## Steps

1. Invoke the `knowledge` skill using the Skill tool.
2. Determine the mode:
   - If the user said "save" or the conversation produced new findings → **Save mode**
   - If the user said "retrieve", asked a question, or is starting new work → **Retrieve mode**
   - If unclear, ask the user: "Would you like to save insights from this conversation or retrieve past knowledge?"
3. Follow the corresponding mode steps in the skill
