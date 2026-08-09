#!/usr/bin/env python3
"""Negative controls demonstrating that the verifiers reject corrupted data."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from independent_edge_list_check import check_path, parse_edgelist
from ramsey260_common import induced_witness, package_root


def expect_failure(name: str, action) -> dict[str, str]:
    try:
        action()
    except (AssertionError, ValueError) as exc:
        return {"test": name, "status": "rejected_as_expected", "reason": str(exc)}
    raise AssertionError(f"negative control {name!r} was incorrectly accepted")


def main() -> None:
    root = package_root()
    primary = root / "data" / "witness_260_seed2603.edgelist"
    masks, edges = parse_edgelist(primary)
    sorted_edges = sorted(edges)
    results: list[dict[str, str]] = []

    deleted = json.loads((root / "data" / "deleted_points_seed2603.json").read_text())
    results.append(
        expect_failure(
            "duplicate deletion index",
            lambda: induced_witness(deleted[:-1] + [deleted[0]]),
        )
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)

        degrees = [mask.bit_count() for mask in masks]
        low_vertex = degrees.index(16)
        removed_edge = next(edge for edge in sorted_edges if low_vertex in edge)
        path = temp / "missing_edge.edgelist"
        path.write_text(
            "".join(f"{u} {v}\n" for u, v in sorted_edges if (u, v) != removed_edge),
            encoding="utf-8",
        )
        results.append(expect_failure("removed edge lowers minimum degree", lambda: check_path(path, strict_expected=False)))

        added = None
        for u in range(276):
            for v in range(u + 1, 276):
                if (u, v) in edges:
                    continue
                found = False
                neighbors_u = [a for a in range(276) if (masks[u] >> a) & 1]
                for a in neighbors_u:
                    common = masks[a] & masks[v]
                    if common:
                        found = True
                        break
                if found:
                    added = (u, v)
                    break
            if added is not None:
                break
        assert added is not None
        path = temp / "added_c4_edge.edgelist"
        mutated = sorted(edges | {added})
        path.write_text("".join(f"{u} {v}\n" for u, v in mutated), encoding="utf-8")
        results.append(expect_failure("added edge creates C4", lambda: check_path(path, strict_expected=False)))

        path = temp / "loop.edgelist"
        path.write_text(primary.read_text(encoding="utf-8") + "0 0\n", encoding="utf-8")
        results.append(expect_failure("loop injection", lambda: check_path(path)))

        u, v = sorted_edges[0]
        path = temp / "duplicate.edgelist"
        path.write_text(primary.read_text(encoding="utf-8") + f"{u} {v}\n", encoding="utf-8")
        results.append(expect_failure("duplicate edge injection", lambda: check_path(path)))

    output = root / "results" / "negative_controls.json"
    output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for result in results:
        print(json.dumps(result, sort_keys=True))
    print("PASS: every adversarial corruption was rejected")


if __name__ == "__main__":
    main()
