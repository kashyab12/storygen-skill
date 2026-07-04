# The Braintrust: Multi-Agent Story Testing

Modeled on Pixar's Braintrust — simulated editorial feedback as the test
phase of the storygen pipeline. Specialist reviewers examine the same
artifact in parallel, each through one lens. Their notes are advisory; the
writer (the orchestrating agent) decides what to act on.

Storytelling has no single "right" answer — quality is judged on
**coherence, emotion, persuasion, and resonance**. No one reviewer grades
all four; the panel covers them together, and the writer's triage is where
the axes get weighed against each other.

## Key principles

| Principle | Operational meaning |
|---|---|
| **Candor without authority** | Reviewers diagnose honestly and hold nothing back, but never prescribe. They say what's broken and why it matters; the writer owns the fix. Feedback loops stay advisory, not prescriptive, to preserve creative agency. |
| **Make the story better, not be right** | Optimize for whole-story quality, not individual component performance. A note that would improve "tension" at the cost of the arc is a bad note. Reviewers flag it anyway; the writer triages it away. |

## The panel

Pixar's Braintrust puts the **storyline/storyboard** in front of five
lenses: story structure, emotional resonance, character development, a
worldbuilding expert, and tension & conflict. Storygen keeps those five and
adds **voice & dialogue** (from the multi-layered construction model),
since prose drafts carry voice in a way storyboards don't.

| Reviewer | Covers |
|---|---|
| `storygen-structure` | Spine, arc shape, causality, pacing, setup/payoff |
| `storygen-emotion` | Emotional arc, earned feeling, catharsis, honesty in the unbelievable |
| `storygen-character` | Desire, agency, conflictedness, testing, earned arcs |
| `storygen-world` | World rules, continuity state, setting-as-pressure, canon fidelity |
| `storygen-tension` | Stakes, escalation, layered conflict, scene-level pressure |
| `storygen-voice` | Distinct voices, purposeful dialogue, subtext, narration, rhythm |

## Two checkpoints

**Checkpoint A — storyline review (Phase 1.5).** Like Pixar reviewing
storyboards before animation: the panel reviews the spine + bible + beat
outline (plus shot/panel lists for visual formats) *before prose exists*.
Structure, character, tension, and worldbuilding apply in full; emotion
reviews the planned emotional arc; voice reviews the planned voice notes and
any sample lines. Structural bugs cost 10x more after drafting — fix every
`BLOCKING` here first.

**Checkpoint B — draft review (Phase 3).** The panel reviews the complete
draft + current bible. Never review fragments — most story bugs are
cross-scene state bugs.

## Running a review round

1. Give every reviewer the **complete artifact** (outline at Checkpoint A,
   full draft at Checkpoint B) and the **story bible**.
2. Launch all six reviewers in parallel (one batch of Task calls, each
   readonly). If running without subagents, adopt each persona sequentially
   using the condensed rubrics below — never skip a lens.
3. Collect notes in the standard format (below).
4. Writer triages: group notes by root cause, resolve conflicts using the
   spine and the protagonist's arc as tiebreakers, then revise.

## Note format (all reviewers)

Every note must be:

- **Grounded**: quote or cite the exact scene/beat/line.
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

**Structure** — Does the spine hold? Does the draft deliver the arc shape
the plan chose (Classic, Hero's Journey, Fichtean, Kishōtenketsu…)? Is every
beat causal ("because of that", never "and then")? Is the inciting incident
irreversible? Does the climax force a choice only the grown protagonist
could make? Do setups pay off? Is pacing proportionate to importance?

**Emotional resonance** — What is the reader feeling at each beat, and is it
what the story needs them to feel? Is every emotion earned on the page rather
than asserted? Does the emotional arc build to genuine catharsis? Is the
unbelievable honest — do impossible events carry true feeling? Does the
story produce immersion and empathy, not just admiration of its prose?

**Character development** — Can you state each major character's desire in
one sentence? Does the protagonist drive events (agency) or get dragged by
them? Are they tested by uncomfortable situations that force growth? Do we
admire the effort rather than the success? Is the arc's endpoint earned? Do
the sheets' strengths/weaknesses/core quality actually show up on the page?

**Worldbuilding** — Are the world's rules established before they're used
and never bent for convenience? Does the world seed (twist, resource,
struggle) actively pressure the story? Is state consistent (who knows what,
what's where, what time it is)? In remixes: does each universe keep its own
logic, and does the bridging mechanic have honest costs and limits?

**Tension & conflict** — What is at stake, does the reader know, and do the
stakes rise? Is conflict layered (external, interpersonal, internal)? Does
every scene contain opposition? Are there stretches with no pressure? Is the
climax the point of maximum pressure? Any cheap tension (withheld info,
coincidence, idiot-plot)?

**Voice & dialogue** — Cover the names: can you still tell who's speaking?
Does every line reveal character or advance story? Is exposition disguised
as conversation? Does the narration's voice fit the audience and form? Read
it aloud — where does the rhythm die?

## Convergence rules

- Ship when a round produces no `BLOCKING` notes and two consecutive rounds
  produce only `POLISH`.
- Hard cap: three full draft rounds. Endless polish loops optimize style
  simulation, not narrative craft — the goal is reader immersion, empathy,
  and transformation, and no amount of prose-polish supplies those. If round
  three still has blocking notes, the problem is in the plan — return to
  Phase 1 and rebuild the spine rather than continuing to patch prose.
- After every revision, update the story bible (including the revision log —
  the iteration history is part of the deliverable) before re-reviewing.
