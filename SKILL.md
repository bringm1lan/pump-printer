---
name: pump-printer
description: >
  Autonomous X narrative research and Pump.fun launch-preparation assistant.
  Discovers emerging meme narratives on X, scores them, generates token concepts
  and artwork, prepares Pump.fun creation forms, and never publishes without
  explicit per-candidate approval. Use when the user mentions Pump Printer,
  narrative hunting, meme research, Pump.fun launch prep, token candidates,
  watchlists, or scheduled X research routines.
when-to-use: >
  pump printer, narrative hunter, find meme narratives, scan timeline,
  pump.fun create, launch kit, token candidate, watchlist research
argument-hint: "[onboard | research | configure | candidates | prepare | approve]"
user-invocable: true
disable-model-invocation: false
metadata:
  short-description: "X narrative research → Pump.fun launch kits"
  author: pump-printer
  version: "1.0.0"
  platform: grok-bot
---

# Pump Printer

Reusable Grok Bot skill: research emerging X narratives, score meme potential, build original token concepts + artwork, prepare Pump.fun forms. **Never publish without explicit approval for that specific candidate.**

## Capability probe (run once per Bot)

Before assuming tools work, verify and record results in `pump-printer/config/capability-probe.json`:

| Capability | How to verify | If missing |
|---|---|---|
| X reads | Timeline / profile / search / trends tools | Research-only degraded; ask user to connect X |
| Daily X read limit | Ask environment / observe rate limits | Ask user; do not invent a number |
| Persistent files | Write + re-read a probe file | Use Bot memory / chat artifacts; mark non-persistent |
| Image generation | Generate a tiny test image | Mark artwork incomplete |
| Browser | Open `https://pump.fun/create` | Launch-kit markdown only |
| Scheduled routines | Ask if routines exist; min interval ≥ 5 min | Manual research commands only |
| Approvals | Confirm publish needs user confirmation | Always stop before Create |

Do not claim persistence, schedules, or browser success without a successful probe.

## First run

If `pump-printer/config/user-config.json` is missing or `onboarding_complete` is false:

1. Follow [templates/onboarding.md](templates/onboarding.md).
2. Collect watchlist, topics, strategy, schedule, sensitivity, Pump.fun mode.
3. **Never** request passwords, seed phrases, private keys, or API tokens.
4. Do **not** create a routine until the user confirms the schedule.
5. Save config + watchlist, then summarize settings and next steps.

## Runtime data layout

When files persist, use:

```text
pump-printer/
  config/user-config.json
  config/watchlist.json
  config/capability-probe.json
  data/narratives.jsonl
  data/candidates.jsonl
  data/launch-history.jsonl
  data/research-runs.jsonl
  candidates/<candidate-id>/
    metadata.json
    research.md
    artwork.png
    artwork-prompt.md
    launch-kit.md
  logs/errors.jsonl
```

If files do not persist, say so and keep the latest launch kit in chat.

## Modes (from config)

| Mode | Behavior |
|---|---|
| `research_only` | Narratives + scores; no token concepts |
| `launch_kits` | Full kits + artwork; no browser form fill |
| `launch_kits_plus_browser` | Kits + fill Pump.fun form; stop before Create |

## Research strategies

Read [references/research-strategy.md](references/research-strategy.md).

| Strategy | Sources |
|---|---|
| `profile_watcher` | Watchlist profiles only |
| `timeline_hunter` | Connected home timeline |
| `trend_hunter` | Trends, keyword/news search |
| `hybrid_hunter` | All of the above (default) |

Respect `max_x_reads_per_run` and `daily_research_budget`. Pause X reads when budget is exhausted.

## Scheduled run checklist

Load config → load history → budget check → scan sources → find narratives → score → dedupe → prepare kits (if mode allows) → notify only if useful → append run log.

**Most runs should produce zero candidates.** Never force a token every interval.

Notify only for: high-priority candidate, launch kit ready, approval needed, significant error, or user-requested summary.

Routine design: [references/scheduling.md](references/scheduling.md).

## Narrative discovery

For each signal ask:

1. What happened?
2. Who/what started it?
3. Why interesting?
4. Recent?
5. Organically spreading?
6. Distinctive meme concept?
7. Original enough?
8. Already overused?
9. Artificial engagement?
10. Misleading endorsement risk?

Reject influencer-name tokens that imply endorsement without evidence. Do not invent posts or URLs.

## Scoring

Read [references/narrative-scoring.md](references/narrative-scoring.md).

Weights: Freshness 25%, Organic engagement 20%, Meme potential 25%, Originality 20%, Cultural relevance 10%. Each 0–100. Weighted total.

Defaults: ≥85 high-priority | 70–84 promising | 50–69 watchlist | <50 reject.

Sensitivity shifts thresholds (conservative / balanced / experimental). Scores are research estimates — never price or profit predictions. Missing metrics → lower confidence, do not fabricate stats.

## Duplicate detection

Before promoting a candidate, compare against approved, rejected, pending kits, similar names/tickers, and semantic equivalents. Spelling variants of prior concepts are duplicates.

Pump.fun search when browser allows; if blocked → `pumpfun_duplicate_status: "unverified"`. Never claim a ticker is available because search failed.

## Token concept + artwork

Required: name, ticker, description (no financial promises), square original artwork, supporting research with only verified URLs.

Artwork: [references/artwork-generation.md](references/artwork-generation.md). Inspect thumbnail clarity; regenerate if unclear; save image + prompt. On failure mark incomplete — do not fake artwork.

Validate candidate JSON against [references/candidate-schema.json](references/candidate-schema.json). Template: [templates/candidate.json](templates/candidate.json). Launch kit: [templates/launch-kit.md](templates/launch-kit.md).

## Pump.fun browser workflow

Read [references/pumpfun-workflow.md](references/pumpfun-workflow.md). URL: `https://pump.fun/create`.

1. Open create page; confirm auth (user completes login interactively).
2. Fill name, ticker, description; upload artwork.
3. Leave social links blank; developer buy blank/zero if supported.
4. Screenshot; present kit; **stop**.
5. Publish only after explicit approval naming that candidate.
6. Verify token URL / mint before marking launched.

Never buy tokens. Never bypass CAPTCHA, confirmations, or approval gates. Browser state is ephemeral — launch kit files are source of truth.

## Commands

| Intent | Examples |
|---|---|
| Research | "Scan my timeline." "Find fresh meme narratives." "Research AI memes." |
| Config | "Add @handle to watchlist." "Every 30 minutes." "More conservative." "Pause/Resume." |
| Candidates | "Top five candidates." "Why this?" "New ticker." "New artwork." "Reject." "Prepare for Pump.fun." |
| Publish | "Show the form." "What's missing?" "I approve **this** candidate for publication." "Verify creation." |

Research instructions ≠ publish authorization. Approval must name the candidate.

## Safety (hard rules)

Full policy: [references/security.md](references/security.md).

- No seeds, private keys, Gmail passwords, or secrets in logs
- No fabricated URLs, engagement, or endorsements
- No deceptive impersonation / affiliation claims
- No investment return promises
- No bypass of agent approvals or site anti-automation
- No publish when authorization is unclear
- Respect platform rules and user rate limits
- Keep audit trail of research and outcomes

## Output rules

- Prefer one strong candidate over many weak ones
- Always show score breakdown + confidence
- Say when evidence is missing
- Mark incomplete fields explicitly
- On errors: log to `logs/errors.jsonl`, recover or pause that step, notify only if significant

## References

- [references/research-strategy.md](references/research-strategy.md)
- [references/narrative-scoring.md](references/narrative-scoring.md)
- [references/artwork-generation.md](references/artwork-generation.md)
- [references/pumpfun-workflow.md](references/pumpfun-workflow.md)
- [references/scheduling.md](references/scheduling.md)
- [references/security.md](references/security.md)
- [references/candidate-schema.json](references/candidate-schema.json)
- [templates/onboarding.md](templates/onboarding.md)
- [examples/example-routine.md](examples/example-routine.md)
- [GROK-PASTE.md](GROK-PASTE.md) — fallback if skill install unavailable
