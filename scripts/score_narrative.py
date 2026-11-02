#!/usr/bin/env python3
"""Compute Pump Printer overall narrative score from criterion scores."""

from __future__ import annotations

import argparse
import json
import sys


WEIGHTS = {
    "freshness": 0.25,
    "organic_engagement": 0.20,
    "meme_potential": 0.25,
    "originality": 0.20,
    "cultural_relevance": 0.10,
}


def overall(scores: dict[str, float], weights: dict[str, float] = WEIGHTS) -> float:
    total = 0.0
    for key, weight in weights.items():
        value = float(scores[key])
        if value < 0 or value > 100:
            raise ValueError(f"{key} out of range: {value}")
        total += value * weight
    return round(total, 2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freshness", type=float, required=True)
    parser.add_argument("--engagement", type=float, required=True)
    parser.add_argument("--meme", type=float, required=True)
    parser.add_argument("--originality", type=float, required=True)
    parser.add_argument("--cultural", type=float, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    scores = {
        "freshness": args.freshness,
        "organic_engagement": args.engagement,
        "meme_potential": args.meme,
        "originality": args.originality,
        "cultural_relevance": args.cultural,
    }
    result = {
        "scores": scores,
        "weights": WEIGHTS,
        "overall_score": overall(scores),
    }
    if args.json:
        json.dump(result, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(result["overall_score"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
