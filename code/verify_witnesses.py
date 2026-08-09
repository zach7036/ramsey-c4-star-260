#!/usr/bin/env python3
"""Finite-geometry reconstruction audit for all four lower-bound witnesses."""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations

from ramsey260_common import (
    AMBIENT_ORDER,
    DELETION_COUNT,
    Q,
    RAMSEY_VALUE,
    STAR_LEAVES,
    TARGET_MIN_DEGREE,
    TARGET_ORDER,
    adjacency_from_edges,
    ambient_edges,
    dot_mod,
    graph_stats,
    has_c4,
    is_absolute,
    package_root,
    projective_points,
)

LABELS = ("seed2601", "seed2602", "seed2603", "seed2604")
EXPECTED_DEGREE_DISTRIBUTION = {16: 134, 17: 142}
EXPECTED_COMMON_NEIGHBOR_DISTRIBUTION = {0: 2558, 1: 35392}


def verify_ambient() -> dict[str, object]:
    points = projective_points(Q)
    assert len(points) == AMBIENT_ORDER
    assert len(set(points)) == AMBIENT_ORDER
    absolute = [i for i, point in enumerate(points) if is_absolute(point)]
    assert len(absolute) == Q + 1 == 18

    edges = ambient_edges(points, Q)
    adjacency = adjacency_from_edges(AMBIENT_ORDER, edges)
    stats = graph_stats(adjacency)
    assert stats.order == 307
    assert stats.size == 2754
    assert stats.degree_distribution == {17: 18, 18: 289}
    assert stats.maximum_common_neighbors == 1
    assert not has_c4(adjacency)
    return {
        "order": stats.order,
        "size": stats.size,
        "absolute_points": len(absolute),
        "degree_distribution": stats.degree_distribution,
        "maximum_common_neighbors": stats.maximum_common_neighbors,
    }


def verify(label: str) -> dict[str, object]:
    root = package_root()
    path = root / "data" / f"witness_260_{label}.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    assert data["field_order"] == Q
    assert data["ambient_order"] == AMBIENT_ORDER
    assert data["deletion_count"] == DELETION_COUNT
    assert data["target_order"] == TARGET_ORDER
    assert data["target_minimum_degree"] == TARGET_MIN_DEGREE
    assert data["star_leaves"] == STAR_LEAVES
    assert data["ramsey_value"] == RAMSEY_VALUE

    points = projective_points(Q)
    deleted = [int(v) for v in data["deleted_ambient_indices"]]
    retained = [int(v) for v in data["retained_ambient_indices"]]
    assert len(deleted) == len(set(deleted)) == DELETION_COUNT
    assert len(retained) == len(set(retained)) == TARGET_ORDER
    assert set(deleted).isdisjoint(retained)
    assert set(deleted).union(retained) == set(range(AMBIENT_ORDER))
    assert [list(points[i]) for i in deleted] == data["deleted_points"]
    assert [list(points[i]) for i in retained] == data["retained_points"]
    assert retained == data["local_to_ambient"]
    assert sum(is_absolute(points[i]) for i in retained) == 14

    local = {ambient: i for i, ambient in enumerate(retained)}
    expected_edges = []
    for u, v in ambient_edges(points, Q):
        if u in local and v in local:
            expected_edges.append((local[u], local[v]))
    stored_edges = [tuple(map(int, edge)) for edge in data["edges_local_labels"]]
    assert stored_edges == expected_edges

    adjacency = adjacency_from_edges(TARGET_ORDER, stored_edges)
    stats = graph_stats(adjacency)
    assert stats.order == TARGET_ORDER
    assert stats.size == 2279
    assert stats.minimum_degree == TARGET_MIN_DEGREE
    assert stats.maximum_degree == 17
    assert stats.degree_distribution == EXPECTED_DEGREE_DISTRIBUTION
    assert stats.maximum_common_neighbors == 1
    assert stats.common_neighbor_distribution == EXPECTED_COMMON_NEIGHBOR_DISTRIBUTION
    assert stats.triangle_count == 638
    assert not has_c4(adjacency)
    assert stats.complement_maximum_degree == 259
    assert stats.complement_maximum_degree < STAR_LEAVES
    stored_stats = data["statistics"]
    assert stored_stats["order"] == stats.order
    assert stored_stats["size"] == stats.size
    assert stored_stats["minimum_degree"] == stats.minimum_degree
    assert stored_stats["maximum_degree"] == stats.maximum_degree
    assert {int(k): int(v) for k, v in stored_stats["degree_distribution"].items()} == stats.degree_distribution
    assert stored_stats["maximum_common_neighbors"] == stats.maximum_common_neighbors
    assert {int(k): int(v) for k, v in stored_stats["common_neighbor_distribution"].items()} == stats.common_neighbor_distribution
    assert stored_stats["triangle_count"] == stats.triangle_count
    assert stored_stats["complement_maximum_degree"] == stats.complement_maximum_degree

    stored_edge_set = set(stored_edges)
    for u, v in combinations(range(TARGET_ORDER), 2):
        orthogonal = dot_mod(points[retained[u]], points[retained[v]], Q) == 0
        assert ((u, v) in stored_edge_set) == orthogonal

    return {
        "label": label,
        **stats.to_dict(),
        "retained_absolute_points": 14,
        "ramsey_consequence": "R(C4,K1,260)>=277",
    }


def main() -> None:
    ambient = verify_ambient()
    results = [verify(label) for label in LABELS]
    payload = {"ambient": ambient, "witnesses": results}
    output = package_root() / "results" / "finite_geometry_verification.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))
    print("PASS: all four witnesses reconstruct exactly and prove R(C4,K1,260)>=277")


if __name__ == "__main__":
    main()
