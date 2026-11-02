# Example routine — Pump Printer Research

## Create (chat)

```text
Create a routine named “Pump Printer Research” for this Bot.

When to run: every 15 minutes from 8:00 AM to 11:45 PM in my Bot timezone, every day.

Instruction:
You are running Pump Printer (skill: pump-printer).
1) Load pump-printer/config/user-config.json and watchlist.json.
2) If disabled or paused, exit quietly.
3) Verify remaining daily X research budget; stop reads if exhausted.
4) Run the configured research strategy (default hybrid_hunter).
5) Discover emerging narratives; score with configured weights.
6) Dedupe against narratives.jsonl and candidates.jsonl.
7) For scores that clear the sensitivity threshold, build a candidate folder
   (metadata.json, research.md, artwork if possible, launch-kit.md).
8) If mode is launch_kits_plus_browser and a strong candidate is new,
   prepare https://pump.fun/create fields and screenshot — do NOT click Create.
9) Append data/research-runs.jsonl.
10) Notify me only if: high-priority candidate, launch kit ready, approval needed,
    or a significant error. Otherwise stay silent.

Hard rules: never request secrets; never fabricate URLs; never publish;
never buy tokens; never bypass approvals.
```

## After creation

1. Open Bot → Routines → confirm **When to run** text.
2. Click **Test** once.
3. Confirm no Create click occurred.
4. Enable only after you are happy with the test.

## Example user approvals

```text
I approve candidate pp-20261102-141500-glitchpigeon (Glitch Pigeon / GLITCHP) for publication on Pump.fun.
```

```text
Reject candidate pp-20261102-141500-glitchpigeon — too close to an existing meme.
```

## Example research commands

```text
Scan my timeline for Pump Printer.
Find the strongest narrative from the last hour.
Add @someaccount to my watchlist.
Change Pump Printer to conservative scoring.
Pause Pump Printer.
```
