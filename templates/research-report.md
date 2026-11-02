# Pump Printer research report

**Run ID:** {{run_id}}  
**Started:** {{started_at}}  
**Finished:** {{finished_at}}  
**Strategy:** {{strategy}}  
**Timezone:** {{timezone}}

## Budget

- X reads used this run: {{x_reads_used}}
- Daily reads used: {{daily_reads_used}}
- Daily budget: {{daily_research_budget}}
- Budget remaining: {{budget_remaining}}

## Results

| Metric | Count |
|---|---|
| Narratives considered | {{narratives_found}} |
| High-priority | {{high_priority}} |
| Promising | {{promising}} |
| Watchlist-only | {{watchlist_only}} |
| Rejected | {{rejected}} |
| Duplicates skipped | {{duplicates}} |
| Kits prepared | {{kits_prepared}} |
| Image failures | {{image_failures}} |
| Browser failures | {{browser_failures}} |

## Top findings

{{#candidates}}
### {{token.name}} (`{{token.ticker}}`) — {{narrative.overall_score}}

{{narrative.summary}}

- Status: {{status}}
- Confidence: {{narrative.confidence}}
- Sources: {{source_count}} verified URLs
{{/candidates}}

{{^candidates}}
No candidates met the threshold this run (normal).
{{/candidates}}

## Errors

{{#errors}}
- [{{stage}}] {{error}} → {{recovery}}
{{/errors}}

{{^errors}}
None.
{{/errors}}

## Next actions for user

{{next_actions}}
