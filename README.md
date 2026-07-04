# storygen

An agent skill that turns your coding agent into a story-writing system:
**Plan → Write → Test → Revise**, with a Pixar-style Braintrust of six
specialist reviewer subagents running in parallel. Works with **Cursor**,
**Claude Code**, and **Codex**.

Making good stories is becoming easier. Making great stories is still hard.
This skill closes some of the gap by borrowing what works from coding agents:
a plan before the draft, a living state document (the story bible) so the
story doesn't break when state isn't updated correctly, a multi-agent test
phase, and revision loops that converge instead of polishing forever.

## Credits

Distilled from **Karina Nguyen**'s Lux Summit talk on storytelling and AI:

- Announcement thread: [x.com/karinanguyen/status/2073248122307002413](https://x.com/karinanguyen/status/2073248122307002413)
- Slides: [Lux Summit — Storytelling](https://docs.google.com/presentation/d/1d7fsWsVYnKy0zVZhYil-cJ7ONEpnKB9D4sVmWGrAnJI/edit)

The core ideas — the coding-agent parallel, the story spine, character-driven
narrative, multi-layered construction, and the Braintrust review process
(candor without authority; make the story better, not be right) — are hers.
The skill/subagent packaging and any mistakes in translation are ours.

## Install

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
Phase 0  Intake     brief, audience, format, constraints
Phase 1  Plan       logline → story spine → story bible → beat outline
Phase 2  Write      scene by scene; every scene turns; bible kept current
Phase 3  Test       six reviewers in parallel, each with one lens
Phase 4  Revise     triage notes against the whole story; fix root causes
Phase 5  Converge   repeat 3–4 until clean (hard cap: three rounds)
```

### The Braintrust

Six readonly subagents review the complete draft + story bible in parallel:

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
