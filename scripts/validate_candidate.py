#!/usr/bin/env python3
"""Validate Pump Printer candidate JSON: schema-ish checks + score math."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

DEFAULT_WEIGHTS = {
    "freshness_score": 0.25,
    "engagement_score": 0.20,
    "meme_score": 0.25,
    "originality_score": 0.20,
    "cultural_relevance_score": 0.10,
}

REQUIRED_TOP = ("candidate_id", "discovered_at", "status", "narrative", "token", "checks", "launch")
REQUIRED_NARRATIVE = tuple(DEFAULT_WEIGHTS) + (
    "title",
    "summary",
    "source_posts",
    "overall_score",
    "confidence",
)


def approx_equal(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def validate(path: Path, weights: dict[str, float] | None = None) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    w = weights or DEFAULT_WEIGHTS

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level field: {key}")

    narrative = data.get("narrative") or {}
    for key in REQUIRED_NARRATIVE:
        if key not in narrative:
            errors.append(f"missing narrative field: {key}")

    expected = 0.0
    for field, weight in w.items():
        if field not in narrative:
            continue
        score = narrative[field]
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            errors.append(f"{field} must be 0–100 number, got {score!r}")
            continue
        expected += float(score) * weight

    if "overall_score" in narrative:
        overall = narrative["overall_score"]
        if not isinstance(overall, (int, float)):
            errors.append(f"overall_score must be number, got {overall!r}")
        elif not approx_equal(float(overall), expected):
            errors.append(
                f"overall_score {overall} != weighted sum {round(expected, 2)} "
                f"(diff {abs(float(overall) - expected):.4f})"
            )

    token = data.get("token") or {}
    for key in ("name", "ticker", "description", "image_path", "social_links"):
        if key not in token:
            errors.append(f"missing token field: {key}")

    checks = data.get("checks") or {}
    for key in (
        "historical_duplicate",
        "pumpfun_duplicate_status",
        "impersonation_risk",
        "source_urls_verified",
    ):
        if key not in checks:
            errors.append(f"missing checks field: {key}")

    if checks.get("pumpfun_duplicate_status") not in (None, "clear", "collision", "unverified"):
        errors.append(
            f"invalid pumpfun_duplicate_status: {checks.get('pumpfun_duplicate_status')!r}"
        )

    urls = narrative.get("source_posts") or []
    if not isinstance(urls, list):
        errors.append("source_posts must be a list")
    else:
        for url in urls:
            if not isinstance(url, str) or not url.startswith("http"):
                errors.append(f"invalid source url: {url!r}")

    weight_sum = sum(w.values())
    if not approx_equal(weight_sum, 1.0, tol=0.001):
        errors.append(f"weights must sum to 1.0, got {weight_sum}")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: validate_candidate.py <candidate.json> [weights.json]", file=sys.stderr)
        return 2

    path = Path(argv[1])
    weights = None
    if len(argv) > 2:
        raw = json.loads(Path(argv[2]).read_text(encoding="utf-8"))
        # Allow either scoring_weights object or flat map with short keys
        if "freshness" in raw:
            weights = {
                "freshness_score": float(raw["freshness"]),
                "engagement_score": float(raw["organic_engagement"]),
                "meme_score": float(raw["meme_potential"]),
                "originality_score": float(raw["originality"]),
                "cultural_relevance_score": float(raw["cultural_relevance"]),
            }
        else:
            weights = {k: float(v) for k, v in raw.items()}

    errors = validate(path, weights)
    if errors:
        print("FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    data = json.loads(path.read_text(encoding="utf-8"))
    print("OK")
    print(f"candidate_id={data['candidate_id']}")
    print(f"overall_score={data['narrative']['overall_score']}")
    print(f"status={data['status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
