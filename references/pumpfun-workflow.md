# Pump.fun browser workflow

Target: `https://pump.fun/create`

Website behavior changes. **Inspect the live page** every session; do not assume wallet signing, fees, email login, or zero-dev-buy from memory alone.

## Modes

| Config `pumpfun.mode` | Browser actions |
|---|---|
| `research_only` | None |
| `launch_kits` | None (markdown + files only) |
| `launch_kits_plus_browser` | Fill form + screenshot; stop before Create |

## Authentication

1. Open the create page.
2. Detect login method currently offered (email/Gmail/wallet/other).
3. Ask the user to complete interactive auth themselves.
4. **Never** request or store passwords, Gmail credentials, seed phrases, or private keys.
5. Proceed only when the page shows an authenticated create form.

If auth cannot be completed, save the launch kit and exit cleanly.

## Form preparation

For an approved-for-prep candidate (prep ≠ publish):

1. Confirm authenticated create UI.
2. Fill **name** from `token.name`.
3. Fill **ticker** from `token.ticker`.
4. Fill **description** from `token.description`.
5. Upload `artwork` from the candidate folder.
6. Leave optional social links blank (`leave_social_links_blank: true`).
7. Developer buy: leave blank or set **0** when the UI allows (`developer_buy: zero_or_blank`).
8. Re-read all fields; fix mismatches.
9. Capture screenshot; save path in candidate metadata.
10. Set `launch.form_prepared = true`.
11. Present kit to user. **Do not click Create.**

Browser sessions may reset between routine runs. Re-fill from the launch kit whenever needed. The kit is source of truth.

## Publication gate

Publish only when **all** are true:

1. User message explicitly approves **this** `candidate_id` (name/ticker).
2. Bot/platform approval controls allow the click.
3. `auto_publish` remains false unless user changed config **and** still gave per-candidate approval.
4. No CAPTCHA/block unresolved.
5. Form values still match the kit.

If any required confirmation appears — **stop and ask**. Never bypass safety, CAPTCHA, or approval UI.

## Verification

After a permitted Create:

1. Wait for success UI or token page.
2. Record `token_url`, visible name/ticker, and `mint_address` if shown.
3. Only then set `launch.published = true` and append `data/launch-history.jsonl`.
4. If verification fails, status = `publish_unverified` — do not claim success.

## Never

- Auto-buy the token or any amount beyond zero/blank developer buy
- Assume creation succeeded because a button was clicked
- Claim ticker availability when search failed (`pumpfun_duplicate_status: unverified`)
- Use prior “you may publish later” config as approval for a new candidate
