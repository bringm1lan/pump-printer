# Narrative scoring

## Weights (defaults)

| Criterion | Weight | What it measures |
|---|---|---|
| Freshness | 25% | How new the discussion is; first-mover vs late |
| Organic engagement | 20% | Real replies/quotes/spread quality (not raw vanity) |
| Meme potential | 25% | Compressibility into a joke, character, or phrase |
| Originality | 20% | Distinct from saturated meme-coin tropes |
| Cultural relevance | 10% | Resonates beyond a single private joke |

Weights must sum to 1.0. Override only via `scoring_weights` in user config.

## Scale

Each criterion: integer **0–100**.

```
overall = freshness*0.25
        + engagement*0.20
        + meme*0.25
        + originality*0.20
        + cultural*0.10
```

Round display to 2 decimals. Store exact float in JSON.

## Criterion guidance

### Freshness

- 90–100: hours-old, still forming
- 70–89: same day, still accelerating
- 40–69: multi-day but not exhausted
- 0–39: stale / already coin-farmed everywhere

### Organic engagement

Score quality of discussion, not hype language. If metrics unavailable, cap at 55 and set `confidence` lower. **Never fabricate likes/reposts.**

### Meme potential

Can a stranger get the joke from a name + image in under 2 seconds?

### Originality

Penalize dog/cat/pepe clones, celebrity-name grabs, and recycled tickers.

### Cultural relevance

Does it touch a broader vibe (tech moment, sports, format, phrase) vs pure private lore?

## Categories (defaults)

| Overall | Category | Action |
|---|---|---|
| 85–100 | High-priority | Notify + prepare kit (if mode allows) |
| 70–84 | Promising | Prepare kit when sensitivity allows |
| 50–69 | Watchlist | Log only unless user asks |
| <50 | Reject | Log rejection reason |

### Sensitivity shifts

| Sensitivity | Prepare kits from | High-priority notify from |
|---|---|---|
| conservative | ≥85 | ≥90 |
| balanced | ≥70 | ≥85 |
| experimental | ≥60 | ≥80 |

Safety, originality, and impersonation checks always apply.

## Explanations

Every score needs a **one-sentence why**. Example:

> Freshness 88: phrase appeared in the last 3 hours across unrelated accounts with no prior coin.

## Confidence

- `high`: multiple verified sources + usable engagement signals
- `medium`: solid narrative, some missing metrics
- `low`: thin evidence; do not auto-prepare kits even if score is high

Overall score is a **research estimate**, not a prediction of price, volume, or profit.
