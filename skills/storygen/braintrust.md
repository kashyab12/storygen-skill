# The Braintrust: Multi-Agent Story Testing

Modeled on Pixar's Braintrust. Six specialist reviewers examine the same
draft in parallel, each through one lens. Their notes are advisory; the
writer (the orchestrating agent) decides what to act on.

## Key principles

| Principle | Operational meaning |
|---|---|
| **Candor without authority** | Reviewers diagnose honestly and hold nothing back, but never prescribe. They say what's broken and why it matters; the writer owns the fix. This preserves creative agency. |
| **Make the story better, not be right** | Optimize for whole-story quality, not individual component performance. A note that would improve "tension" at the cost of the arc is a bad note. Reviewers flag it anyway; the writer triages it away. |

## Running a review round

1. Give every reviewer the **complete draft** and the **story bible**. Never
   review fragments — most story bugs are cross-scene state bugs.
2. Launch all six reviewers in parallel (one batch of Task calls, each
   readonly). If running without subagents, adopt each persona sequentially
   using the condensed rubrics below — never skip a lens.
3. Collect notes in the standard format (below).
4. Writer triages: group notes by root cause, resolve conflicts using the
   spine and the protagonist's arc as tiebreakers, then revise.

## Note format (all reviewers)

Every note must be:

- **Grounded**: quote or cite the exact scene/line.
- **Diagnostic, not prescriptive**: name the problem and the cost to the
  reader — not the rewrite. ("I stopped believing her choice in the barn
  scene because nothing earlier shows she can act alone" — not "add a scene
  where she acts alone.")
- **Severity-tagged**:
  - `BLOCKING` — the story fails for the reader if unaddressed
  - `MAJOR` — noticeably weakens the story
  - `POLISH` — refinement; only act on these once nothing bigger remains
- Each reviewer ends with a verdict: **PASS** (nothing blocking or major in
  my lens) or **NEEDS WORK**, plus the single note that matters most.
- No padding. If a lens finds nothing, say "No issues found in this lens."

## Condensed rubrics (for sequential / no-subagent mode)

The full personas live in the subagent files; these are the minimum questions
per lens.

**Structure** — Does the spine hold? Is every beat causal ("because of
that", never "and then")? Is the inciting incident irreversible? Does the
climax force a choice only the grown protagonist could make? Do setups pay
off? Is pacing proportionate to importance?

**Emotional resonance** — What is the reader feeling at each beat, and is it
what the story needs them to feel? Is every emotion earned on the page rather
than asserted? Does the emotional arc build to genuine catharsis? Is the
unbelievable honest — do impossible events carry true feeling?

**Character development** — Can you state each major character's desire in
one sentence? Does the protagonist drive events (agency) or get dragged by
them? Are they tested by uncomfortable situations that force growth? Do we
admire the effort rather than the success? Is the arc's endpoint earned?

**Worldbuilding** — Are the world's rules established before they're used
and never bent for convenience? Is state consistent (who knows what, what's
where, what time it is)? Does the setting pressure the story or just
decorate it? In remixes: does each universe keep its own logic?

**Tension & conflict** — What is at stake, does the reader know, and do the
stakes rise? Is conflict layered (external, interpersonal, internal)? Does
every scene contain opposition? Are there stretches with no pressure? Is the
climax the point of maximum pressure?

**Voice & dialogue** — Cover the names: can you still tell who's speaking?
Does every line reveal character or advance story? Is exposition disguised
as conversation? Does the narration's voice fit the audience and form? Read
it aloud — where does the rhythm die?

## Convergence rules

- Ship when a round produces no `BLOCKING` notes and two consecutive rounds
  produce only `POLISH`.
- Hard cap: three full rounds. Endless polish loops optimize style
  simulation, not narrative craft. If round three still has blocking notes,
  the problem is in the plan — return to Phase 1 and rebuild the spine
  rather than continuing to patch prose.
- After every revision, update the story bible before re-reviewing.
