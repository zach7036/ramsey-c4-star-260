#!/usr/bin/env python3
"""Independent bitset audit using only raw edge lists.

This verifier deliberately imports no finite-geometry construction code. It
checks syntax, degrees, complement degree, and the C4 criterion using integer
bitsets. Thus it can validate a certificate supplied by any construction.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

ORDER = 276
STAR_LEAVES = 260
EXPECTED_SIZE = 2279
EXPECTED_DEGREES = {16: 134, 17: 142}
EXPECTED_CODEGREES = {0: 2558, 1: 35392}
LABELS = ("seed2601", "seed2602", "seed2603", "seed2604")


def parse_edgelist(path: Path) -> tuple[list[int], set[tuple[int, int]]]:
    masks = [0] * ORDER
    edges: set[tuple[int, int]] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        fields = stripped.split()
        if len(fields) != 2:
            raise ValueError(f"{path}:{line_number}: expected two integers")
        u, v = map(int, fields)
        if not (0 <= u < ORDER and 0 <= v < ORDER):
            raise ValueError(f"{path}:{line_number}: endpoint out of range")
        if u == v:
            raise ValueError(f"{path}:{line_number}: loop")
        if u > v:
            u, v = v, u
        if (u, v) in edges:
            raise ValueError(f"{path}:{line_number}: duplicate edge {(u, v)}")
        edges.add((u, v))
        masks[u] |= 1 << v
        masks[v] |= 1 << u
    return masks, edges


def check_path(path: Path, *, strict_expected: bool = True) -> dict[str, object]:
    masks, edges = parse_edgelist(path)
    degrees = [mask.bit_count() for mask in masks]
    if min(degrees) != 16:
        raise AssertionError(f"minimum degree is {min(degrees)}, not 16")
    if max(ORDER - 1 - degree for degree in degrees) >= STAR_LEAVES:
        raise AssertionError("complement contains K1,260")

    codegrees: Counter[int] = Counter()
    for u, v in combinations(range(ORDER), 2):
        common = (masks[u] & masks[v]).bit_count()
        codegrees[common] += 1
        if common >= 2:
            raise AssertionError(f"C4 detected via pair {(u, v)} with {common} common neighbors")
    if strict_expected:
        if len(edges) != EXPECTED_SIZE:
            raise AssertionError(f"wrong size: {len(edges)}")
        if dict(sorted(Counter(degrees).items())) != EXPECTED_DEGREES:
            raise AssertionError("wrong degree distribution")
        if dict(sorted(codegrees.items())) != EXPECTED_CODEGREES:
            raise AssertionError("unexpected common-neighbor distribution")

    triangle_incidence = sum(
        (masks[u] & masks[v]).bit_count() for u, v in edges
    )
    if triangle_incidence % 3:
        raise AssertionError("triangle incidence not divisible by three")
    triangles = triangle_incidence // 3
    if triangles != 638:
        raise AssertionError(f"unexpected triangle count {triangles}")

    return {
        "file": path.name,
        "order": ORDER,
        "size": len(edges),
        "degree_distribution": dict(sorted(Counter(degrees).items())),
        "minimum_degree": min(degrees),
        "maximum_degree": max(degrees),
        "complement_maximum_degree": max(ORDER - 1 - d for d in degrees),
        "common_neighbor_distribution": dict(sorted(codegrees.items())),
        "maximum_common_neighbors": max(codegrees),
        "triangle_count": triangles,
        "ramsey_consequence": "R(C4,K1,260)>=277",
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = [check_path(root / "data" / f"witness_260_{label}.edgelist") for label in LABELS]
    output = root / "results" / "independent_edgelist_verification.json"
    output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for result in results:
        print(json.dumps(result, sort_keys=True))
    print("PASS: independent raw-edge-list audits prove all four graphs are valid witnesses")


if __name__ == "__main__":
    main()
