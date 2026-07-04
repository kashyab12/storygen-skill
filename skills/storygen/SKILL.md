---
name: storygen
description: >-
  Generate great stories through an agentic Plan → Write → Test → Revise
  pipeline with a Pixar-style Braintrust of specialist reviewers (structure,
  emotion, character, worldbuilding, tension, voice). Use when the user asks
  to write a story, short story, script, screenplay, novel chapter, children's
  storybook, tall tale, fanfic, universe remix, or narrative of any kind — or
  to critique or revise an existing story draft.
---

# Storygen: Agentic Story Generation

Making good stories is becoming easier. Making great stories is still hard.
This skill treats storytelling like a coding agent treats software:
**Plan → Write → Test → Revise**, with a living system of state — because a
story breaks when state isn't updated correctly, exactly like software.

Two North Stars, adapted from Pixar's Braintrust:

1. **Candor without authority.** Feedback is advisory, never prescriptive.
   Reviewers diagnose problems; the writer owns the fix.
2. **Make the story better, not be right.** Optimize the whole story's
   quality, never an individual component's score.

## Pipeline

Copy this checklist into a todo list and track progress:

```
Storygen Progress:
- [ ] Phase 0: Intake — brief, audience, format, constraints
- [ ] Phase 1: Plan — logline, story spine, story bible
- [ ] Phase 2: Write — full draft, scene by scene
- [ ] Phase 3: Test — Braintrust review (parallel subagents)
- [ ] Phase 4: Revise — triage notes, rewrite, update bible
- [ ] Phase 5: Converge — repeat Test/Revise until pass, then deliver
```

### Phase 0: Intake

Establish before planning (infer sensible defaults from the request rather
than interrogating the user; ask only if the request is genuinely ambiguous):

- **Premise** — the seed idea, in the user's words.
- **Audience & purpose** — a 6-year-old's bedtime tall tale, a literary short
  story, a teaching story (e.g. learning to apologize), a screenplay scene.
- **Format & length** — prose / script / picture-book pages; word or page count.
- **Constraints** — real people or details to include, canon rules if remixing
  existing universes, tone boundaries, content limits.

### Phase 1: Plan

Never draft prose before the plan exists. Produce, in order:

1. **Logline** — one sentence: protagonist + desire + obstacle + stakes.
2. **Story spine** — fill in every slot:
   > Once upon a time there was… Every day… One day… Because of that…
   > Because of that… Until finally… And ever since then…
   Each "Because of that" must be causal, not sequential. If you can swap
   two beats without breaking anything, the spine is broken.
3. **Story bible** — create the living state document from the template in
   [story-bible.md](story-bible.md): character dossiers (desire, fear, flaw,
   arc), world rules, timeline, scene ledger, open threads.
4. **Beat outline** — one line per scene: who wants what, what turns, what
   changes state. Every scene must earn its place by changing something.

Craft standards for the plan are in [craft.md](craft.md) — read it before
planning. Non-negotiables: the protagonist is driven by desire and conflict;
the audience admires the effort, not the success; characters are forced to
grow through uncomfortable situations.

### Phase 2: Write

Draft the full story from the beat outline. While writing:

- Work scene by scene; each scene has a turn (a value that flips: hope→fear,
  ignorance→knowledge, safety→danger).
- Keep voice distinctive and dialogue purposeful — every line either reveals
  character or advances the story, ideally both.
- **Honesty in the unbelievable**: however fantastical the premise, emotions
  and choices must be true. A dragon may be impossible; the fear of
  disappointing your father is not.
- After drafting, update the story bible: what each character now knows,
  wants, and has lost; which threads opened or closed. Stale state produces
  continuity bugs.

### Phase 3: Test — the Braintrust

Run the multi-agent review. Full protocol in [braintrust.md](braintrust.md).

**If subagents / a Task tool are available**, launch these six reviewers **in
parallel, in a single batch**, each readonly, each given the complete draft
plus the story bible:

| Subagent | Lens |
|---|---|
| `storygen-structure` | Story structure — spine, causality, pacing, payoff |
| `storygen-emotion` | Emotional resonance — arc, empathy, earned feeling |
| `storygen-character` | Character development — desire, agency, growth |
| `storygen-world` | Worldbuilding — rules, consistency, texture |
| `storygen-tension` | Tension & conflict — stakes, pressure, escalation |
| `storygen-voice` | Voice & dialogue — distinctiveness, purpose, rhythm |

**If subagents are not available**, run the same six reviews sequentially
in-context using the condensed rubrics in [braintrust.md](braintrust.md),
adopting one persona at a time. Do not skip lenses.

### Phase 4: Revise

1. Collect all notes. Discard none unread.
2. **Triage against the whole story**, not the note's severity alone: a note
   is only actioned if the fix makes the *story* better. When notes conflict
   (e.g. tension wants a darker midpoint, emotion wants warmth), the story
   spine and the protagonist's arc are the tiebreakers.
3. Rewrite the affected scenes — fix root causes (usually in structure or
   character motivation), not symptoms (usually in prose).
4. Update the story bible to reflect every change. Then re-verify the spine
   still holds end to end.

### Phase 5: Converge

Re-run the Braintrust on the revised draft. Ship when:

- No reviewer reports a **blocking** note, and
- Two consecutive rounds produce only **polish**-level notes, or
- Three full rounds have run (avoid over-optimization — style simulation is
  not narrative craft; a fourth pass of prose-polish will not fix anything
  that matters).

Deliver the final story plus a short craft note: the logline, the spine, and
what changed across revisions (the process matters as much as the output —
preserve the iteration history rather than discarding it).

## Additional resources

- [craft.md](craft.md) — what makes stories great: spine, character, layers
- [braintrust.md](braintrust.md) — review protocol, rubrics, note format
- [story-bible.md](story-bible.md) — living state template and update rules
