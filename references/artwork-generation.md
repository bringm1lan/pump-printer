# Artwork generation

## Goal

Original **square** token profile art that reads at thumbnail size and expresses the meme — not generic crypto chrome.

## Workflow

1. Distill one **core visual idea** (character, object, or symbol).
2. Write `artwork-prompt.md` with subject, style, colors, composition, negative constraints.
3. Generate a square image.
4. Inspect: clear center subject? Readable tiny? Extra text clutter?
5. Regenerate up to 2 times if unclear.
6. Save as `candidates/<id>/artwork.png` (or environment equivalent).
7. Set `token.image_path` and keep the prompt on disk.

## Prompt recipe

```text
Square token profile image. [SUBJECT from narrative]. Bold simple shapes,
high contrast, centered composition, readable at 64px. Flat or soft-shaded
illustration. No logos of real brands. No real-person photoreal likeness
unless user explicitly owns rights and requests it. No wallets, charts,
candlesticks, or “to the moon” clichés. Minimal or no text.
```

Adapt style to the meme (absurd, cute, brutalist, pixel, etc.) — stay original.

## Hard no

- Unauthorized brand marks, UI clones of Pump.fun/X, or fake “verified” badges
- Impersonation portraits meant to look like a specific living person for endorsement theater
- Text promising returns (“100x”, “guaranteed”)
- Claiming the image is official merch for a third party

## Failure handling

If generation fails or all attempts are unreadable:

- Set candidate status to `incomplete`
- `token.image_path = null`
- Note failure in `launch-kit.md` and `logs/errors.jsonl`
- Do not pretend artwork exists when preparing Pump.fun upload

## Browser upload

Only upload the saved file associated with the candidate ID. If the file is missing, regenerate or stop form prep.
