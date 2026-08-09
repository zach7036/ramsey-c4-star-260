#!/usr/bin/env python3
"""Generate four static ER(17) deletion certificates and raw edge lists."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from ramsey260_common import (
    AMBIENT_ORDER,
    DELETION_COUNT,
    Q,
    RAMSEY_VALUE,
    STAR_LEAVES,
    TARGET_MIN_DEGREE,
    TARGET_ORDER,
    graph_stats,
    induced_witness,
    is_absolute,
    package_root,
)

LABELS = ("seed2601", "seed2602", "seed2603", "seed2604")
DISCOVERY = {
    "seed2601": {"seed": 2601, "search_role": "independent heuristic replay", "first_solution_iteration": 4331726},
    "seed2602": {"seed": 2602, "search_role": "independent heuristic replay", "first_solution_iteration": 14905923},
    "seed2603": {
        "seed": 2603,
        "search_role": "primary deterministic replay",
        "first_solution_iteration": 786389,
    },
    "seed2604": {"seed": 2604, "search_role": "independent heuristic replay", "first_solution_iteration": 5195084},
}


def generate(label: str) -> dict[str, object]:
    root = package_root()
    deleted_path = root / "data" / f"deleted_points_{label}.json"
    deleted = json.loads(deleted_path.read_text(encoding="utf-8"))
    points, retained, retained_points, edges, adjacency = induced_witness(deleted)
    stats = graph_stats(adjacency)

    payload: dict[str, object] = {
        "claim": "R(C4,K1,260)=277",
        "certificate_role": "lower-bound witness proving R(C4,K1,260)>=277",
        "label": label,
        "field_order": Q,
        "ambient_graph": "simple orthogonal-polarity graph ER(17)",
        "ambient_order": AMBIENT_ORDER,
        "ambient_point_ordering": [
            "(1,a,b) for a=0..16 and b=0..16",
            "(0,1,b) for b=0..16",
            "(0,0,1)",
        ],
        "adjacency_rule": "distinct points x,y are adjacent iff x dot y = 0 modulo 17",
        "deletion_count": DELETION_COUNT,
        "deleted_ambient_indices": sorted(deleted),
        "deleted_points": [list(points[i]) for i in sorted(deleted)],
        "retained_ambient_indices": retained,
        "retained_points": [list(p) for p in retained_points],
        "local_to_ambient": retained,
        "edges_local_labels": [list(edge) for edge in edges],
        "target_order": TARGET_ORDER,
        "target_minimum_degree": TARGET_MIN_DEGREE,
        "star_leaves": STAR_LEAVES,
        "ramsey_value": RAMSEY_VALUE,
        "retained_absolute_points": sum(is_absolute(points[i]) for i in retained),
        "statistics": stats.to_dict(),
        "discovery": DISCOVERY[label],
    }

    json_path = root / "data" / f"witness_260_{label}.json"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    edge_path = root / "data" / f"witness_260_{label}.edgelist"
    edge_path.write_text("".join(f"{u} {v}\n" for u, v in edges), encoding="utf-8")

    map_path = root / "data" / f"witness_260_{label}_vertex_map.csv"
    with map_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["local_vertex", "ambient_index", "x0", "x1", "x2", "absolute"])
        for local, ambient in enumerate(retained):
            p = points[ambient]
            writer.writerow([local, ambient, *p, int(is_absolute(p))])

    return {
        "label": label,
        "json": str(json_path.relative_to(root)),
        "edgelist": str(edge_path.relative_to(root)),
        "vertex_map": str(map_path.relative_to(root)),
        "statistics": stats.to_dict(),
    }


def main() -> None:
    results = [generate(label) for label in LABELS]
    output = package_root() / "results" / "generation_summary.json"
    output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for result in results:
        print(json.dumps(result, sort_keys=True))
    print("PASS: generated four exact ER(17) deletion witnesses")


if __name__ == "__main__":
    main()
