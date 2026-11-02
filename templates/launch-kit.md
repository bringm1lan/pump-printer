# Launch kit — {{token.name}} ({{token.ticker}})

**Candidate ID:** {{candidate_id}}  
**Discovered:** {{discovered_at}}  
**Status:** {{status}}  
**Overall score:** {{narrative.overall_score}} (confidence: {{narrative.confidence}})

## Narrative

**Title:** {{narrative.title}}

{{narrative.summary}}

**Why it matters:** {{narrative.why_interesting}}

### Scores

| Criterion | Score | Notes |
|---|---|---|
| Freshness (25%) | {{narrative.freshness_score}} | {{narrative.score_explanations.freshness}} |
| Organic engagement (20%) | {{narrative.engagement_score}} | {{narrative.score_explanations.organic_engagement}} |
| Meme potential (25%) | {{narrative.meme_score}} | {{narrative.score_explanations.meme_potential}} |
| Originality (20%) | {{narrative.originality_score}} | {{narrative.score_explanations.originality}} |
| Cultural relevance (10%) | {{narrative.cultural_relevance_score}} | {{narrative.score_explanations.cultural_relevance}} |

Scores are research estimates, not predictions of price or demand.

### Sources (verified only)

{{#source_posts}}
- {{.}}
{{/source_posts}}

## Token concept

- **Name:** {{token.name}}
- **Ticker:** {{token.ticker}}
- **Description:** {{token.description}}
- **Artwork:** {{token.image_path}}
- **Social links:** none (left blank by default)

## Checks

- Historical duplicate: {{checks.historical_duplicate}}
- Pump.fun duplicate status: {{checks.pumpfun_duplicate_status}}
- Impersonation risk: {{checks.impersonation_risk}}
- Source URLs verified: {{checks.source_urls_verified}}

## Launch status

- Form prepared: {{launch.form_prepared}}
- User approved: {{launch.user_approved}}
- Published: {{launch.published}}
- Token URL: {{launch.token_url}}
- Mint: {{launch.mint_address}}

## Approval

To publish, the user must explicitly say they approve **this** candidate ID. Until then, do not click Create.
