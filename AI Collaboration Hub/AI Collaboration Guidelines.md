# Pacha Story AI Collaboration Guidelines

## Prompting Framework
- Always include a 150-400 word recap of relevant scenes and decisions before new drafting.
- Declare the current emotional target (reader response + character interior state) and the desired shift by scene end.
- Specify which arc you are working in (992 Tiwanaku, 1992 Copacabana, 1452 early chasqui, 1532 comet, 1492 inner cord) and note any cross-arc callbacks.
- List required motifs/symbols, POV, timeline, and any continuity notes (e.g., `meteor has not appeared since Cord 1`).
- Supply a tone brief: e.g., `lyrical, reverent, grounded in Andean sensory detail with hints of cosmic awe`.

## Drafting Protocol
1. Duplicate the scene template in Notion (or local equivalent).
2. Paste the recap, emotional target, motif checklist, and tone brief into the prompt.
3. Ask AI to produce no more than 900 words per pass; if more is needed, continue with a new prompt that includes a condensed recap of the last output.
4. After each pass, log a human `Emotional State of Reader` note and highlight continuity anchors.
5. Store the AI output in the scene page or file, tagging it `Needs Human Review`.

## Chunking & Overlap
- Break cords into 1-2k word segments; overlapping recaps must mention the previous segment's closing image and the next scene's trigger.
- For sections exceeding three segments, request a distilled continuity summary (<400 words) and save it as `Cord Summary vX`.
- Before any new request, reference the latest `Cord Summary` plus scene-specific recap.

## Review & Integration
- First human reviewer reads for emotional truth and continuity; mark `Accepted` or `Requires Revision` directly in the scene file.
- Second reviewer (human or AI) focuses on line-level flow only after emotional alignment is confirmed.
- Use AI for revisions only with explicit instructions: cite the excerpt, list issues, state what must stay untouched (cultural details, character voice).
- Once changes are approved, toggle scene status to `Locked` and update the `Cord Board` tracker.

## AI Boundaries & Escalation
- Do not let AI invent new cultural or historical elements without a research check. Flag `Requires Fact Check` if unsure.
- Avoid global rewrites across multiple cords in one pass. Handle transitions scene by scene.
- If AI output drifts in tone or pacing, pause and update the tone guide before requesting further drafts.

## Continuity Aids
- Maintain the character, artifact, and motif tables; reference their shorthand IDs in prompts.
- After each sprint, run AI on `continuity audit` prompts using the latest summaries to detect contradictions.
- Keep a running `Decision Log` for any retcons or major tweaks and link affected scenes.

## Voice Harmonization
- Periodically provide AI with short excerpts from both co-authors as style anchors.
- When blending scenes, ask AI to `merge while preserving the lyrical cadence and restrained sentiment` and review closely.

## Archiving & Versioning
- Save stable scenes with ISO-date suffixes (e.g., `Cord2-Scene3-2024-06-18`).
- Move obsolete drafts to an archive toggle or subfolder to avoid reusing outdated context.
