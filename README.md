# storygen

> We've taught AI to code, plan, and reason. But can it craft the next
> Pulitzer novel or Oscar-winning script?

An agent skill that turns your coding agent into a story-writing system:
**Plan → Write → Test → Revise**, with a Pixar-style Braintrust of six
specialist reviewer subagents running in parallel. Works with **Cursor**,
**Claude Code**, and **Codex**.

## Sample Storybooks

Read the generated sample PDFs directly:

- [Pip of Bramblewick Farm](samples/sesame-seed/storybook.pdf)
- [The Circles of Syracuse](samples/archimedes/storybook.pdf)

Making good stories is becoming easier. Making great stories is still hard —
because of **data** (the development drafts and revision histories matter as
much as the finished text), **subjectivity** (stories are judged on
coherence, emotion, persuasion, and resonance — there's no single right
answer), and **optimization** (it's easy to reward style simulation instead
of the narrative craft that produces reader immersion, empathy, and
transformation). This skill is built around those three problems: it borrows
what works from coding agents — a plan before the draft, a living state
document (the story bible) so the story doesn't break when state isn't
updated correctly, a simulated-editorial-feedback test phase, revision loops
that converge instead of polishing forever — and it preserves the iteration
history as part of the deliverable, because the process matters as much as
the output.

## Credits

Distilled from **Karina Nguyen**'s Lux Summit talk on storytelling and AI:

- Announcement thread: [x.com/karinanguyen/status/2073248122307002413](https://x.com/karinanguyen/status/2073248122307002413)
- Slides: [Lux Summit — Storytelling](https://docs.google.com/presentation/d/1d7fsWsVYnKy0zVZhYil-cJ7ONEpnKB9D4sVmWGrAnJI/edit)

The core ideas — the coding-agent parallel, the story spine, character-driven
narrative, multi-layered construction, the story-arc taxonomy, world seeds,
the storyline-first Braintrust review (candor without authority; make the
story better, not be right), and the framing that teaching an AI to write
great stories might be one of the most aligned ways to teach it to understand
humanity — are hers. The skill/subagent packaging and any mistakes in
translation are ours.

## Install

The quickest way, via [skills.sh](https://www.skills.sh/kashyab12/storygen-skill):

```bash
npx skills add kashyab12/storygen-skill
```

Or clone and use the bundled installer, which also installs the Braintrust
subagents:

```bash
git clone https://github.com/kashyab12/storygen-skill.git
cd storygen-skill
./install.sh            # installs for every tool found on your machine (user scope)
```

Or pick targets and scope explicitly:

```bash
./install.sh cursor              # just Cursor  (~/.cursor)
./install.sh claude codex        # Claude Code + Codex
./install.sh --project all       # into ./.cursor, ./.claude, ./.codex of the current repo
```

What gets installed where:

| Tool | Skill | Subagents |
|---|---|---|
| Cursor | `~/.cursor/skills/storygen/` | `~/.cursor/agents/` |
| Claude Code | `~/.claude/skills/storygen/` | `~/.claude/agents/` |
| Codex | `~/.codex/skills/storygen/` | `~/.codex/agents/` |

(Project scope uses `.cursor/`, `.claude/`, `.codex/` in your repo instead.)

In environments without subagent support, the skill automatically falls back
to running all six review lenses sequentially in-context — you lose
parallelism, not rigor.

## Use

Just ask for a story; the skill triggers on story-writing requests:

> Write a tall-tale storybook about my 6-year-old catching "the legendary
> Gerald," a tiny sunfish, with his dad as fishing captain.

> My son took a toy from another kid and didn't apologize. Write a story
> that teaches him how to apologize next time — without moralizing.

> Jake Paul in a boxing match against Toph from Avatar: The Last Airbender.
> Honor both canons.

You can also point it at an existing draft: "Run the storygen Braintrust on
`draft.md`."

## How it works

```
Phase 0    Intake      brief, audience, format, constraints
Phase 1    Plan        concepts → logline → arc choice → story spine
                       → story bible → beat outline (+ shot/panel lists)
Phase 1.5  Checkpoint  Braintrust reviews the storyline BEFORE prose exists
                       (Pixar reviews storyboards before animation)
Phase 2    Write       scene by scene; every scene turns; bible kept current
Phase 3    Test        six reviewers in parallel, each with one lens
Phase 4    Revise      triage notes against the whole story; fix root causes
Phase 5    Converge    repeat 3–4 until clean (hard cap: three rounds),
                       deliver the story plus its iteration history
```

The plan phase carries the deck's full toolkit: candidate-concept generation
before committing to one idea; a deliberate arc choice from seven shapes
(Classic/Freytag, Hero's Journey, Three-Act, Fichtean, Circular, Braided,
Kishōtenketsu); structured world seeds ([environment type] + [defining
twist] + [inhabitants] + [power/resource] + [struggle/conflict]); character
sheets with strengths, weaknesses, core quality, and the wound behind the
want; and, for universe remixes, a canon-grounded bridging mechanic with
honest costs. Format playbooks cover tall tales, teaching stories,
storybooks, storyboards/comics, and screenplays.

### The Braintrust

Six readonly subagents review the artifact + story bible in parallel — the
beat outline at the checkpoint, the complete draft in the test phase:

| Subagent | Lens |
|---|---|
| `storygen-structure` | Spine integrity, causality, pacing, setup/payoff |
| `storygen-emotion` | Emotional arc, earned feeling, honesty in the unbelievable |
| `storygen-character` | Desire, agency, testing under pressure, earned arcs |
| `storygen-world` | World rules, continuity state, canon fidelity in remixes |
| `storygen-tension` | Stakes, escalation, layered conflict, cheap-tension smells |
| `storygen-voice` | Distinct voices, purposeful dialogue, subtext, rhythm |

Every note is grounded in a quote, diagnostic rather than prescriptive, and
severity-tagged (`BLOCKING` / `MAJOR` / `POLISH`). Two rules govern the whole
process, straight from the Pixar Braintrust:

1. **Candor without authority** — feedback is advisory, not prescriptive, to
   preserve creative agency.
2. **Make the story better, not be right** — optimize story quality, never an
   individual component's score.

## Repo layout

```
skills/storygen/
  SKILL.md          the orchestrator: pipeline, phases, convergence rules
  craft.md          what makes stories great: spine, character, layers, scenes
  braintrust.md     review protocol, rubrics, note format
  story-bible.md    living state template (the story's source of truth)
agents/
  storygen-structure.md   storygen-emotion.md   storygen-character.md
  storygen-world.md       storygen-tension.md   storygen-voice.md
install.sh
```

## License

[MIT](LICENSE)
