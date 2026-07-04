---
name: storygen
description: >-
  Generate great stories through an agentic Plan → Write → Test → Revise
  pipeline with a Pixar-style Braintrust of specialist reviewers (structure,
  emotion, character, worldbuilding, tension, voice). Use when the user asks
  to write a story, short story, script, screenplay, novel chapter, children's
  storybook, comic, tall tale, fanfic, universe remix, or narrative of any
  kind — or to critique or revise an existing story draft or outline.
---

# Storygen: Agentic Story Generation

We've taught AI to code, plan, and reason. Making *good* stories is becoming
easier; making *great* stories is still hard, for three reasons this skill is
built to counter:

- **Data.** Exceptional storytelling data is scarce — and the development
  drafts and revision histories matter as much as the finished text. The
  process matters as much as the output, so this pipeline **captures the
  iteration**: plans, notes, and revision logs are artifacts, not scratch.
- **Subjectivity.** There is no single "right" answer. Good storytelling is
  judged on four axes — **coherence, emotion, persuasion, resonance** — so
  testing uses a panel of specialist reviewers (simulated editorial
  feedback), not a single score.
- **Optimization.** It's easy to optimize the wrong thing. The target is
  deeper narrative craft — reader **immersion, empathy, transformation** —
  never style simulation. Convergence rules below exist to stop
  polish-loops that improve prose while the story stays broken.

The setup mirrors a coding agent: coding runs Plan → Write → Test → Debug →
Refactor; storytelling runs **Plan → Write → Test → Revise**. And like
software, a story is a **living system of contexts** — it breaks when state
isn't updated correctly — so all phases read and write a story bible.

Two North Stars, from Pixar's Braintrust:

1. **Candor without authority.** Feedback is advisory, never prescriptive.
   Reviewers diagnose problems; the writer owns the fix. This preserves
   creative agency.
2. **Make the story better, not be right.** Optimize whole-story quality,
   never an individual component's score.

## Pipeline

Copy this checklist into a todo list and track progress:

```
Storygen Progress:
- [ ] Phase 0: Intake — brief, audience, format, constraints
- [ ] Phase 1: Plan — concepts, arc, spine, story bible, beat outline
- [ ] Phase 1.5: Storyline checkpoint — Braintrust reviews the outline
- [ ] Phase 2: Write — full draft, scene by scene
- [ ] Phase 3: Test — Braintrust reviews the complete draft (parallel)
- [ ] Phase 4: Revise — triage notes, rewrite, update bible
- [ ] Phase 5: Converge — repeat Test/Revise until pass, then deliver
```

### Phase 0: Intake

Establish before planning (infer sensible defaults from the request rather
than interrogating the user; ask only if the request is genuinely ambiguous):

- **Premise** — the seed idea, in the user's words. It can be tiny ("I have a
  crush on this guy at school"); the pipeline expands it.
- **Audience & purpose** — a 6-year-old's bedtime tall tale, a literary short
  story, a teaching story (e.g. learning to apologize), a screenplay scene.
- **Format & length** — prose, script, storybook/picture-book pages, comic or
  storyboard panels; word or page count.
- **Constraints** — real people or details to include, canon rules if
  remixing existing universes, tone boundaries, content limits.

### Phase 1: Plan

Never draft prose before the plan exists. Craft standards are in
[craft.md](craft.md) — read it before planning. Produce, in order:

1. **Concepts.** If the premise is open-ended, generate 3–5 candidate
   concepts first — same seed, different genre lenses and framings — then
   pick one (or present them if the user wants to choose). A one-line
   daydream can expand into a dozen distinct story concepts; committing to
   the first idea is how stories end up generic.
2. **Logline** — one sentence: protagonist + desire + obstacle + stakes.
3. **Arc choice** — pick the arc shape that fits the story from the seven in
   [craft.md](craft.md) (Classic/Freytag, Hero's Journey, Three-Act, Fichtean,
   Circular, Braided, Kishōtenketsu). Default: Classic Arc. State why.
4. **Story spine** — fill in every slot:
   > Once upon a time there was… Every day… One day… Because of that…
   > Because of that… Until finally… And ever since then…
   Each "Because of that" must be causal, not sequential. If you can swap
   two beats without breaking anything, the spine is broken.
5. **Story bible** — create the living state document from the template in
   [story-bible.md](story-bible.md): world seed (environment type + defining
   twist + inhabitants + power/resource + struggle/conflict), character
   sheets (desire, need, flaw, strengths, weaknesses, core quality, arc),
   world rules, timeline, scene ledger, open threads.
6. **Beat outline** — one line per scene: who wants what, what turns, what
   changes state. For visual formats (storybook, comic, screenplay), take it
   down to a shot/panel list per scene. Every scene must earn its place by
   changing something.

Non-negotiables: the protagonist is driven by desire and conflict; the
audience admires the effort, not the success; characters are forced to grow
through uncomfortable situations.

### Phase 1.5: Storyline checkpoint

Pixar's Braintrust reviews **storyboards before animation** — structural
bugs are cheapest before prose exists. Run a light Braintrust pass on the
outline: give the reviewers the spine, bible, and beat outline. Structure,
character, tension, and worldbuilding lenses apply fully; emotion and voice
review what's visible at this stage (planned emotional arc; planned voice
notes). Fix `BLOCKING` findings in the plan before writing a word of prose.

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
| `storygen-structure` | Story structure — spine, arc, causality, pacing, payoff |
| `storygen-emotion` | Emotional resonance — arc, empathy, earned feeling |
| `storygen-character` | Character development — desire, agency, growth |
| `storygen-world` | Worldbuilding — rules, consistency, texture (the worldbuilding expert) |
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
4. Update the story bible — including its revision log — to reflect every
   change. Then re-verify the spine still holds end to end.

### Phase 5: Converge

Re-run the Braintrust on the revised draft. Ship when:

- No reviewer reports a **blocking** note, and
- Two consecutive rounds produce only **polish**-level notes, or
- Three full rounds have run. Style simulation is not narrative craft: a
  fourth pass of prose-polish cannot fix anything that matters. If round
  three still has blocking notes, the bug is in the plan — return to
  Phase 1 and rebuild the spine.

Deliver the final story **plus its iteration history**: the logline, the
chosen arc and why, the spine, and what changed across revision rounds. The
process matters as much as the output — the development drafts and revision
history are part of the deliverable, not scratch to discard.

## Additional resources

- [craft.md](craft.md) — what makes stories great: spine, arcs, character,
  layers, world seeds, format playbooks (tall tales, teaching stories,
  universe remixes, storyboards)
- [braintrust.md](braintrust.md) — review protocol, rubrics, note format
- [story-bible.md](story-bible.md) — living state template and update rules
