# Scheduling (Grok Bot routines)

## How Grok Bot routines work

Per [Grok Bot skills & routines docs](https://docs.x.ai/grok-bot/skills-routines-and-automations):

- A **skill** is reusable instructions; a **routine** is when one Bot runs a workflow.
- Routines run in the **cloud** (laptop can be closed).
- Schedules use the Bot **Timezone** setting.
- New routines wait for the next slot (they do not fire at creation).
- Use **Test** for an immediate safe run.
- Minimum schedule spacing: **5 minutes**.
- Caps: up to **50 routines** per Bot; hourly run limits apply (account + per-routine).
- Each run spends **usage**.

## Default proposal (must be user-confirmed)

- Every **15 minutes**
- **08:00–23:45** local
- Seven days/week
- Name: `Pump Printer Research`

This is ~64 runs/day if the window is fully active. Confirm the user’s plan/usage before enabling.

## Setup prompt (copy)

> Create a routine named “Pump Printer Research” owned by this Bot.
> Schedule: every 15 minutes from 8:00 AM to 11:45 PM in my Bot timezone, all weekdays.
> Instruction: Run the Pump Printer scheduled research checklist from the pump-printer skill.
> Load config and history, respect X read budgets, discover and score narratives, dedupe, and prepare launch kits only when scores clear the configured threshold.
> Mode from user-config (research_only / launch_kits / launch_kits_plus_browser).
> Never publish tokens. Never buy tokens. Never request secrets.
> Notify only for high-priority candidates, ready launch kits, approval requests, or significant errors.
> If X tools or storage fail, log the error and stop that step without inventing data.

## Per-run checklist

1. Load `user-config.json` + `watchlist.json`
2. Abort if `enabled` is false or hunting is paused
3. Load recent `narratives.jsonl` / `candidates.jsonl`
4. Compute remaining daily budget (if known)
5. Scan per strategy
6. Score + filter
7. Dedupe
8. Prepare kits / artwork / optional form fill
9. Append `research-runs.jsonl`
10. Notify only when useful

## Resource tracking fields

Record: runs completed, X reads used, budget remaining, discovered, rejected, duplicates, image failures, browser failures.

## Verification before activation

Ask and confirm:

1. Does this Bot support routines at the requested frequency?
2. Is timezone correct?
3. Is usage impact acceptable?
4. Did **Test** complete without publishing?
5. Did the user explicitly confirm enabling?

Never activate before confirmation (`schedule.user_confirmed` + `enabled`).

## Pause / resume

- Chat: “Pause Pump Printer” / “Resume Pump Printer”
- UI: Bot → Routines → pause switch
- On resume, do not backfill the entire missed window; scan a bounded recent window only
