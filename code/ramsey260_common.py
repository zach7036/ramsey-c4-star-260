#!/usr/bin/env python3
"""Exact construction utilities for the R(C4,K_{1,260}) certificate.

All finite-field arithmetic is over the prime field F_17. Projective points are
normalized so that the first nonzero coordinate is 1, in this deterministic
order:

    (1,a,b), a=0..16, b=0..16;
    (0,1,b), b=0..16;
    (0,0,1).

Two distinct points are adjacent in the simple orthogonal-polarity graph ER(17)
when their dot product is 0 modulo 17. Loops at absolute points are omitted.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable, Sequence

Q = 17
AMBIENT_ORDER = Q * Q + Q + 1
DELETION_COUNT = 31
TARGET_ORDER = 276
TARGET_MIN_DEGREE = 16
STAR_LEAVES = 260
RAMSEY_VALUE = 277

Point = tuple[int, int, int]
Edge = tuple[int, int]


@dataclass(frozen=True)
class GraphStats:
    order: int
    size: int
    minimum_degree: int
    maximum_degree: int
    degree_distribution: dict[int, int]
    maximum_common_neighbors: int
    common_neighbor_distribution: dict[int, int]
    triangle_count: int
    complement_maximum_degree: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def projective_points(q: int = Q) -> list[Point]:
    """Return canonical representatives of PG(2,q), for prime q."""
    points: list[Point] = []
    points.extend((1, a, b) for a in range(q) for b in range(q))
    points.extend((0, 1, b) for b in range(q))
    points.append((0, 0, 1))
    expected = q * q + q + 1
    if len(points) != expected or len(set(points)) != expected:
        raise AssertionError("projective point enumeration failed")
    return points


def dot_mod(x: Point, y: Point, q: int = Q) -> int:
    return sum(a * b for a, b in zip(x, y)) % q


def is_absolute(point: Point, q: int = Q) -> bool:
    return dot_mod(point, point, q) == 0


def ambient_edges(points: Sequence[Point], q: int = Q) -> list[Edge]:
    """Generate the simple orthogonal-polarity graph on supplied points."""
    return [
        (i, j)
        for i, j in combinations(range(len(points)), 2)
        if dot_mod(points[i], points[j], q) == 0
    ]


def adjacency_from_edges(order: int, edges: Iterable[Edge]) -> list[set[int]]:
    adjacency = [set() for _ in range(order)]
    seen: set[Edge] = set()
    for raw_u, raw_v in edges:
        u, v = int(raw_u), int(raw_v)
        if not 0 <= u < order or not 0 <= v < order:
            raise ValueError(f"edge {(u, v)} has endpoint outside 0..{order - 1}")
        if u == v:
            raise ValueError(f"loop at vertex {u}")
        if u > v:
            u, v = v, u
        if (u, v) in seen:
            raise ValueError(f"duplicate edge {(u, v)}")
        seen.add((u, v))
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency


def induced_witness(
    deleted_indices: Iterable[int], q: int = Q
) -> tuple[list[Point], list[int], list[Point], list[Edge], list[set[int]]]:
    """Construct the retained induced graph, locally relabeled 0..275."""
    points = projective_points(q)
    raw_deleted = [int(v) for v in deleted_indices]
    deleted = sorted(raw_deleted)
    if len(set(deleted)) != len(deleted):
        raise ValueError("deleted point list contains duplicates")
    if len(deleted) != DELETION_COUNT:
        raise ValueError(
            f"expected {DELETION_COUNT} distinct deleted points, found {len(deleted)}"
        )
    if deleted and (deleted[0] < 0 or deleted[-1] >= len(points)):
        raise ValueError("deleted point index outside ambient graph")

    deleted_set = set(deleted)
    retained_ambient = [i for i in range(len(points)) if i not in deleted_set]
    if len(retained_ambient) != TARGET_ORDER:
        raise AssertionError(f"retained order is not {TARGET_ORDER}")
    local = {ambient: i for i, ambient in enumerate(retained_ambient)}

    edges: list[Edge] = []
    adjacency = [set() for _ in retained_ambient]
    for u, v in ambient_edges(points, q):
        if u in local and v in local:
            a, b = local[u], local[v]
            edges.append((a, b))
            adjacency[a].add(b)
            adjacency[b].add(a)

    retained_points = [points[i] for i in retained_ambient]
    return points, retained_ambient, retained_points, edges, adjacency


def graph_stats(adjacency: Sequence[set[int]]) -> GraphStats:
    order = len(adjacency)
    if order == 0:
        raise ValueError("empty graph")
    degrees = [len(neighbors) for neighbors in adjacency]
    size = sum(degrees) // 2
    common_histogram: Counter[int] = Counter()
    maximum_common_neighbors = 0
    for u, v in combinations(range(order), 2):
        common = len(adjacency[u].intersection(adjacency[v]))
        common_histogram[common] += 1
        maximum_common_neighbors = max(maximum_common_neighbors, common)

    triangle_incidence = 0
    for u in range(order):
        for v in adjacency[u]:
            if u < v:
                triangle_incidence += len(adjacency[u].intersection(adjacency[v]))
    if triangle_incidence % 3:
        raise AssertionError("triangle incidence is not divisible by three")

    return GraphStats(
        order=order,
        size=size,
        minimum_degree=min(degrees),
        maximum_degree=max(degrees),
        degree_distribution=dict(sorted(Counter(degrees).items())),
        maximum_common_neighbors=maximum_common_neighbors,
        common_neighbor_distribution=dict(sorted(common_histogram.items())),
        triangle_count=triangle_incidence // 3,
        complement_maximum_degree=max(order - 1 - d for d in degrees),
    )


def has_c4(adjacency: Sequence[set[int]]) -> bool:
    """A simple graph has a C4 iff some pair has two common neighbors."""
    return any(
        len(adjacency[u].intersection(adjacency[v])) >= 2
        for u, v in combinations(range(len(adjacency)), 2)
    )


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]
