# Exact determination of `R(C4,K1,260)=277`

**Author:** Zach Waddle  
**Completed:** 2026-08-08  
**Status:** complete AI-assisted research preprint; not peer reviewed

This repository contains the full manuscript, four explicit deletion certificates, exact verification code, discovery-search source, and the documented novelty/research record for

```text
R(C4,K1,260) = 277.
```

## What is proved

Let `f(n)=R(C4,K1,n)`.

- **Lower bound:** deleting 31 explicitly listed points from the simple orthogonal-polarity graph `ER(17)` leaves a `C4`-free graph on 276 vertices with 2,279 edges and minimum degree 16. Its complement has maximum degree 259, so `f(260)>=277`.
- **Upper bound:** a hypothetical 277-vertex `C4`-free graph with minimum degree at least 17 is forced by disjoint second neighborhoods to be 17-regular. This is impossible because `277*17` is odd. Hence `f(260)<=277`.

Four distinct deletion lists are included. All regenerate graphs with certified degree distribution `16^134 17^142` and maximum pair codegree one. No claim is made that the four retained graphs are pairwise nonisomorphic.

## Fast verification

After cloning the repository:

```bash
chmod +x run_all_checks.sh replay_search.sh replay_all_searches.sh
./run_all_checks.sh
```

Expected final line:

```text
ALL CORE CHECKS PASSED
```

The proof-critical checks use only Python's standard library. `run_all_checks.sh` first regenerates the full JSON certificates, raw edge lists, and vertex maps from the four small deletion lists, then verifies them through two independent representations. If `g++` is available, it also rebuilds and replays the primary discovery search.

To run only the static proof audits:

```bash
PYTHONPATH=code python3 code/generate_witnesses.py
PYTHONPATH=code python3 code/verify_witnesses.py
PYTHONPATH=code python3 code/independent_edge_list_check.py
PYTHONPATH=code python3 code/verify_upper_bound.py
PYTHONPATH=code python3 code/adversarial_mutation_tests.py
```

## Replay the search

Primary deterministic replay:

```bash
./replay_search.sh
```

All four archived seeds:

```bash
./replay_all_searches.sh
```

The heuristic search is **not** part of the proof. It only rediscovers the finite deletion certificates; mathematical validity is established by reconstruction and exhaustive verification afterward.

## Repository map

- `paper/paper.md` — full research manuscript.
- `data/deleted_points_seed2601.json` through `seed2604.json` — the four static lower-bound certificates.
- `code/ramsey260_common.py` — exact finite-geometry construction utilities.
- `code/generate_witnesses.py` — regenerates complete JSON certificates, raw edge lists, and vertex maps.
- `code/verify_witnesses.py` — finite-geometry reconstruction verifier.
- `code/independent_edge_list_check.py` — construction-independent raw-edge-list/bitset verifier.
- `code/verify_upper_bound.py` — exact arithmetic audit of the upper proof.
- `code/adversarial_mutation_tests.py` — deliberate negative controls.
- `code/search_polarity_deletion.cpp` — archived heuristic discovery search.
- `docs/candidate_screening.md` — breakthrough threshold and candidate ranking fixed before the final search.
- `docs/novelty_search_log.md` — pre- and post-discovery literature/novelty audit.
- `docs/research_record.md` — concise end-to-end record.
- `manifest.json` — machine-readable result summary.
- `environment.txt` — recorded verification environment.

Generated files under `results/` and `logs/` are intentionally not required to be committed: the scripts recreate them from the static certificates.

## Frontier and novelty caution

The source-located pre-study interval was `275 <= f(260) <= 277`. Version 1 of a 2024 preprint already contained the upper bound 277, so this repository does not claim that upper bound as new. The new contribution is the explicit matching lower construction and exact closure of the interval, together with an independent short upper proof.

No prior exact report or matching construction was found in the documented search. That is strong evidence of novelty, not a logical guarantee against unpublished or poorly indexed work. External Ramsey-theory and bibliographic review is requested before formal publication.

## GitHub Actions

This repository intentionally contains **no GitHub Actions workflows**. Verification is run explicitly from the command line.
