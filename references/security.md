# Security and safety

## Hard prohibitions

1. Never request wallet seed phrases or private keys.
2. Never request Gmail/email passwords.
3. Never expose secrets in logs, screenshots captions, or candidate files.
4. Never fabricate source URLs or engagement stats.
5. Never imply an influencer endorsed a token without clear evidence.
6. Never create deceptive impersonation tokens (fake official/celebrity affiliation).
7. Never promise investment returns or guaranteed profits.
8. Never generate fake engagement or advise market manipulation.
9. Never bypass Grok Bot approval requirements or “trick” a Create click.
10. Never bypass CAPTCHA / anti-automation / access restrictions.
11. Never publish when authorization is unclear or only implied.
12. Respect X and Pump.fun rules, user schedules, and rate limits.

## Approval model

| Action | Gate |
|---|---|
| Research / score / log | Config enabled |
| Create launch kit + art | Mode + score threshold |
| Fill Pump.fun form | Mode `launch_kits_plus_browser` |
| Click Create / publish | Explicit user approval naming `candidate_id` + platform approval UI |
| Buy tokens | **Never** automated |

Research commands are not publish authorization.

## Impersonation checks

Set `checks.impersonation_risk = true` and refuse kit promotion when:

- Name/ticker/description claims to be the official token of a person/brand without authorization
- Artwork mimics a real person’s likeness to suggest endorsement
- Copy uses “official”, “endorsed by”, or similar without evidence

## Error handling

| Failure | Recovery |
|---|---|
| X rate limit / 429 | Back off; mark budget; notify if persistent |
| X auth errors | Stop reads; tell user to reconnect X |
| Storage write fail | Warn non-persistence; keep kit in chat |
| Image gen fail | Status `incomplete` |
| Browser/nav fail | Keep kit; retry later; log error |
| Pump.fun UI changed | Re-inspect; update steps; don’t guess |
| Unclear publish intent | Ask for explicit candidate approval |

Append structured lines to `logs/errors.jsonl`:

```json
{"ts":"ISO-8601","candidate_id":null,"stage":"research|art|browser|publish","error":"...","recovery":"..."}
```

## Audit trail

Retain: research runs, candidate metadata, approval quotes (text only), publish verification results. Do not store credentials.
