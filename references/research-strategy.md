# Research strategy

## Goal

Find **emerging narratives** with meme potential. Do not mint a concept from every viral post. Prefer distinctive, organic, recent signals.

## Strategies

### profile_watcher

1. Load enabled watchlist handles.
2. Fetch recent posts within the time window since last successful run (or last 60–90 minutes on first run).
3. Cluster related posts/replies into candidate narratives.
4. Cap reads with `max_x_reads_per_run`.

### timeline_hunter

1. Read the connected user's home timeline (newest first).
2. Flag unusual phrases, recurring jokes, rising characters, format shifts.
3. Follow only the strongest 1–3 threads if budget allows.

### trend_hunter

1. Pull trends / news tools available in this Bot.
2. Run keyword searches from config topics + watchlist keywords.
3. Prefer sudden phrase novelty over evergreen topics.
4. Use post-volume hints when available; never invent counts.

### hybrid_hunter (default)

Allocate budget roughly:

- 40% watchlist profiles
- 30% home timeline
- 30% trends/keywords

Skip empty sources. Rebalance if a source errors.

## Narrative extraction rules

Keep a candidate only if you can answer most of:

1. What happened?
2. Who/what started it?
3. Why is it interesting?
4. Is it recent?
5. Is it organically spreading?
6. Is there a distinctive meme concept?
7. Is it original enough to stand alone?
8. Is it already overused?
9. Any artificial engagement smell?
10. Could a token misleadingly imply endorsement?

## Anti-patterns

- Turning a celebrity username into a ticker because they posted something unrelated
- Copying an existing famous meme coin with a typo
- Treating quote-tweet volume as proof of organic lore without reading content
- Producing a forced concept when nothing qualifies

## Budget accounting

Each run append to `data/research-runs.jsonl`:

- `run_id`, `started_at`, `finished_at`
- `strategy`, `x_reads_used`, `budget_remaining` (if known)
- `narratives_found`, `candidates_prepared`, `rejected`, `duplicates`
- `errors[]`

If daily budget is unknown, track reads used today in the run log and ask the user to set `daily_research_budget` after observing limits.
