# Pump Printer

AI-powered **X narrative research** and **Pump.fun launch-preparation** skill for [Grok Bot](https://docs.x.ai/grok-bot/skills-routines-and-automations).

Pump Printer watches X for emerging internet narratives, scores meme potential, builds original token concepts and artwork, and can prepare a Pump.fun creation form. You configure research preferences and approve publication. The skill does **not** publish tokens on its own.

## What it does

1. Connects to your X research preferences (watchlist, topics, strategy).
2. Runs on demand or on a **scheduled Grok Bot routine**.
3. Discovers narratives (not random words from tweets).
4. Scores candidates with a transparent weighted model.
5. Deduplicates against prior findings.
6. Generates name, ticker, description, and original artwork.
7. Optionally fills `https://pump.fun/create` via the Bot browser.
8. Stops for your explicit per-candidate approval before any publish.
9. Verifies and records outcomes when a launch succeeds.

## Required Grok Bot capabilities

| Capability | Required? | Notes |
|---|---|---|
| X access (timeline / profiles / search / trends) | Yes for research | Connect X in the Bot; limits vary by account — probe, don't assume |
| Persistent files or durable Bot storage | Strongly recommended | Without it, history may not survive sessions |
| Image generation | For full launch kits | Kits marked incomplete if generation fails |
| Browser / computer use | For form preparation | Optional; markdown kits still work |
| Scheduled routines | For autonomy | Grok Bot cloud routines; minimum interval **5 minutes** |
| User approvals | Always | Publish must remain behind confirmation |

V1 does **not** need an external backend, database, OpenAI key, or custom browser service.

## Install / configure

### Option A — Install as a Grok Bot skill (preferred)

1. Copy this folder into a place your Bot can read, or paste/upload the contents into a Grok Bot conversation.
2. Ask the Bot:

   > Save Pump Printer as a private skill using the SKILL.md and references in this package. Enable it for this Bot under Private skills if needed.

3. Or open **Connect apps** → enable the skill under **Private skills**.
4. Say: `Run Pump Printer onboarding` or `/pump-printer onboard`.

### Option B — Grok Build / local skill paths

If you use Grok Build–compatible discovery:

- Project: `.grok/skills/pump-printer/SKILL.md` (and supporting files)
- User: `~/.grok/skills/pump-printer/`

Copy this package into that path.

### Option C — Copy-paste fallback

If native skill install is unavailable, paste [GROK-PASTE.md](GROK-PASTE.md) into the Bot and ask it to follow those instructions as standing operating procedure. Then run onboarding.

## Connect X

1. In Grok Bot, connect the **X** app / plugin for that Bot.
2. Sign in with your X account through the supported OAuth flow.
3. Confirm the Bot can read your home timeline and public profiles.
4. **Never** paste Bearer tokens, API keys, or passwords into chat.

Pump Printer will probe available X tools and ask about your real daily read limits instead of assuming a fixed number (some environments report ~1000 reads/day; that is **not** universal).

## Configure a watchlist

During onboarding, or later:

> Add @example1 and @example2 to my Pump Printer watchlist.

Watchlist format: [config/example-watchlist.json](config/example-watchlist.json). No account is hard-required.

## Choose a research strategy

| Strategy | Focus |
|---|---|
| `profile_watcher` | New posts from your watchlist |
| `timeline_hunter` | Your X home timeline |
| `trend_hunter` | Trends, keywords, unusual phrases |
| `hybrid_hunter` | All of the above (default) |

Also set topics (memes, AI culture, crypto humor, etc.) and sensitivity: `conservative` | `balanced` | `experimental`.

Defaults live in [config/default-config.json](config/default-config.json).

## Configure a scheduled routine

Grok Bot routines run in the cloud. Ask the **same Bot** that owns Pump Printer:

> Create a routine named “Pump Printer Research” that runs the Pump Printer scheduled research checklist every 15 minutes from 8:00 AM to 11:45 PM in my timezone, seven days a week. Research and prepare launch kits only. Never publish. Notify me only for high-priority candidates, ready kits, approval needs, or significant errors.

Then:

1. Open the Bot → **Routines** and confirm **When to run**.
2. Use **Test** once with safe settings.
3. Confirm timezone under Bot settings.
4. Do not enable until you explicitly approve the schedule.

Limits to know (from Grok Bot docs): schedules must be **≥ 5 minutes** apart; account-wide and per-routine hourly run caps apply; each run spends usage. See [references/scheduling.md](references/scheduling.md).

## Authenticate to Pump.fun

1. Ask the Bot to open `https://pump.fun/create`.
2. Complete email/Gmail (or current site login) yourself in the interactive session.
3. Do **not** send passwords or wallet seeds to the Bot.
4. Pump Printer inspects the live page — it does not assume fees, wallet signing, or zero-cost creation.

## Review a launch kit

When notified, open the candidate folder or ask:

> Show the launch kit for candidate \<id\>.

You should see narrative summary, score breakdown, sources, name/ticker/description, artwork, duplicate-check status, and whether the Pump.fun form was prepared.

## Approve or reject

- Reject: `Reject candidate <id>.`
- Prepare form: `Prepare candidate <id> for Pump.fun.`
- Approve publish (must be specific):

  > I approve candidate \<id\> (\<name\> / \<ticker\>) for publication on Pump.fun.

Vague phrases like “looks good” or prior config are **not** publish authorization.

## What is automated vs approval-gated

| Automated (when configured) | Requires you |
|---|---|
| X scanning within budget | Initial config + X connect |
| Scoring + dedupe | Approving/rejecting candidates |
| Draft name/ticker/description | Final publish decision |
| Artwork generation | Completing Pump.fun / email login |
| Form fill + screenshot | Any token purchase (never auto) |
| Research notifications | Verifying live site behavior changes |

## Troubleshooting

| Issue | What to try |
|---|---|
| Routine never runs | Not paused? Timezone correct? New schedules wait for next slot — use **Test**. Interval ≥ 5 min? |
| Rate limit on routines | Widen interval; Grok Bot enforces hourly caps |
| X tools missing | Reconnect X; follow Bot/X plugin errors (not credits guesses) |
| Budget exhausted | Raise `daily_research_budget` or wait for reset; skill should pause reads |
| History forgotten | Persistence probe failed — re-save config; prefer file-backed computer |
| Browser form empty next run | Expected — kits on disk are source of truth; re-run prepare |
| Duplicate check unverified | Pump.fun search blocked; do not treat as “ticker free” |
| Artwork missing | Image gen failed; regenerate or mark incomplete |
| Accidental publish risk | Keep mode ≠ publish; never ask to bypass approvals |

More: [references/security.md](references/security.md), [references/pumpfun-workflow.md](references/pumpfun-workflow.md).

## Stop or uninstall

- Pause: `Pause Pump Printer.` (or pause the routine in Bot UI)
- Delete routine: Bot → Routines → delete
- Disable private skill: Connect apps → Private skills → disable
- Remove files: delete the `pump-printer` runtime data and this package from skill paths

## Testing

See [TESTING.md](TESTING.md). Automated tests must use mocked research data and must **not** publish real tokens.

## Package layout

```text
Pump printer/
├── SKILL.md                 # Main agent entry
├── README.md
├── LICENSE
├── GROK-PASTE.md            # Copy-paste fallback
├── TESTING.md
├── config/
├── references/
├── templates/
└── examples/
```

## Future (not V1 dependencies)

Optional later: webhooks for export, Node integrations, hosted inboxes, external image APIs, review dashboard, other launch platforms, research-quality analytics, multi-strategy profiles.

## License

MIT — see [LICENSE](LICENSE).
