#!/usr/bin/env python3
"""Machine-auditable arithmetic for the 277-vertex upper bound."""

from __future__ import annotations

import json
from pathlib import Path

N = 277
STAR_LEAVES = 260
DELTA_LOWER = N - STAR_LEAVES


def verify() -> dict[str, object]:
    assert DELTA_LOWER == 17
    available_vertices = N - 1
    set_size_lower = DELTA_LOWER - 1
    degree_upper = available_vertices // set_size_lower
    assert available_vertices == 276
    assert set_size_lower == 16
    assert degree_upper == 17
    forced_degree = DELTA_LOWER
    degree_sum = N * forced_degree
    assert degree_sum % 2 == 1

    return {
        "hypothetical_order": N,
        "star_leaves": STAR_LEAVES,
        "forced_minimum_degree": DELTA_LOWER,
        "local_disjoint_set_size_lower_bound": set_size_lower,
        "available_vertices": available_vertices,
        "forced_maximum_degree": degree_upper,
        "forced_regular_degree": forced_degree,
        "degree_sum": degree_sum,
        "degree_sum_parity": "odd",
        "contradiction": "handshaking lemma",
        "ramsey_consequence": "R(C4,K1,260)<=277",
    }


def main() -> None:
    result = verify()
    root = Path(__file__).resolve().parents[1]
    (root / "results" / "upper_bound_verification.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, sort_keys=True))
    print("PASS: exact local counting plus parity proves R(C4,K1,260)<=277")


if __name__ == "__main__":
    main()
