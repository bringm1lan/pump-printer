# Testing checklist

Do **not** publish real tokens during automated or checklist tests. Prefer [examples/mock-research-feed.json](examples/mock-research-feed.json).

## A. Setup

- [ ] First-time onboarding completes and writes `user-config.json` + `watchlist.json`
- [ ] Config validation rejects unknown strategy / sensitivity / mode values
- [ ] Capability probe records X, storage, image, browser, routines honestly
- [ ] Onboarding refuses to collect passwords or seed phrases
- [ ] Routine is **not** created until user confirms schedule

## B. Research (mocked)

- [ ] Profile watcher reads only enabled watchlist handles
- [ ] Keyword / trend path surfaces phrase clusters from mock feed
- [ ] Glitch-pigeon style posts become a narrative candidate
- [ ] `$DOGE2` / “100x guaranteed” style posts are rejected or heavily penalized
- [ ] Celebrity “official token” posts set `impersonation_risk` and are not promoted
- [ ] Empty/low-signal runs produce **zero** forced kits

## C. Scoring

- [ ] Weighted overall matches formula (see script below)
- [ ] Each criterion includes a short explanation
- [ ] Missing metrics lower confidence; no invented counts
- [ ] Conservative / balanced / experimental thresholds shift kit preparation

### Score check (example-candidate)

```
freshness 88 * 0.25 = 22.00
engagement 72 * 0.20 = 14.40
meme 91 * 0.25 = 22.75
originality 84 * 0.20 = 16.80
cultural 70 * 0.10 = 7.00
overall = 82.95
```

Run: `python3 scripts/validate_candidate.py examples/example-candidate.json`

## D. Dedupe & JSON

- [ ] Candidate JSON validates against `references/candidate-schema.json`
- [ ] Near-duplicate name/ticker/semantic remakes are skipped
- [ ] Historical approved/rejected entries block repeats
- [ ] Failed Pump.fun search → `pumpfun_duplicate_status: unverified`

## E. Artwork

- [ ] Prompt saved beside image
- [ ] Unreadable thumbnail triggers regenerate path
- [ ] Generation failure → status `incomplete`, `image_path` null

## F. Persistence & schedule

- [ ] Files survive a new session when probe says persistence works
- [ ] If persistence fails, Bot discloses that clearly
- [ ] Scheduled checklist loads config, respects budget, appends run log
- [ ] Exhausted daily budget pauses further X reads
- [ ] Notifications suppressed on empty successful runs

## G. Pump.fun browser (manual / staging)

- [ ] Create page opens
- [ ] Live auth method detected; user completes login interactively
- [ ] Name, ticker, description, artwork filled correctly
- [ ] Social links blank; developer buy blank/zero when supported
- [ ] Screenshot captured; Create **not** clicked without approval
- [ ] Vague “looks good” does **not** publish
- [ ] Explicit candidate approval is required
- [ ] Verification records URL/mint only after success UI
- [ ] Network/browser failure recovers without claiming launch

## H. Safety regression

- [ ] No secrets in `logs/errors.jsonl`
- [ ] Approval bypass attempts refused
- [ ] Auto-buy never offered as default behavior
