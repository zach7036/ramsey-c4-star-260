# Exact determination of the star-quadrilateral Ramsey number

## \(R(C_4,K_{1,260})=277\)

**Zach Waddle**  
**Completed:** 8 August 2026  
**Status:** Research preprint; not peer reviewed  
**Evidence standard:** Exact finite certificates, exhaustive verification, and an analytic upper-bound proof

> **Scope and caution.** The mathematical claim in this manuscript is finite and exactly checkable. The novelty review found no prior report of the exact value or the lower-bound construction, but an indexed search cannot exclude all unpublished, private, or poorly indexed work. The result should therefore be independently reviewed by a specialist before it is treated as established in the literature.

## Abstract

Let \(f(n)=R(C_4,K_{1,n})\), where \(K_{1,n}\) is the star with \(n\) leaves. Before this investigation, the strongest source-located results gave

\[
275\le f(260)\le277.
\]

The lower endpoint follows from a published exact value at \(n=262\) and the standard adjacent-value inequality, while a public 2024 preprint version already supplied the upper endpoint. The unresolved problem was therefore the existence of a \(C_4\)-free graph on 276 vertices with minimum degree at least 16.

A breakthrough threshold was fixed before the final computation: a one-sided improvement would be incremental, whereas an exact resolution of a source-located open Ramsey value with independently auditable certificates would qualify as a minor breakthrough in this narrow exact-value program. I searched induced subgraphs of the orthogonal-polarity graph \(ER(17)\), generated directly from \(PG(2,17)\). A deterministic swap search found a 31-point deletion whose retained graph has 276 vertices, 2,279 edges, degree distribution \(16^{134}17^{142}\), and maximum pairwise common-neighbor count one. Consequently the graph is \(C_4\)-free and its complement has maximum degree 259, proving \(f(260)\ge277\). Three further seeds produced distinct deletion lists with the same certified statistics.

For the matching upper bound, suppose a \(C_4\)-free graph on 277 vertices has minimum degree at least 17. For each vertex \(v\), the sets \(N(u)\setminus\{v\}\), \(u\in N(v)\), are pairwise disjoint and each has at least 16 elements. Hence \(16d(v)\le276\), so every vertex has degree exactly 17. This is impossible on 277 vertices by the handshaking lemma. Therefore

\[
\boxed{R(C_4,K_{1,260})=277}.
\]

The lower certificate was reconstructed from finite-field coordinates, audited independently from raw edge lists, subjected to deliberate corruption tests, and reproduced from the archived search seed. A post-discovery search found no prior exact report or matching 276-vertex construction. The result closes the full source-located interval and extends the published \(q=17\) exact sequence to the first even offset beyond its stated \(t\le10\) range. Subject to external mathematical and bibliographic review, the evidence supports classification as a minor breakthrough within the specific star-quadrilateral Ramsey-number line.

**Keywords:** Ramsey number; quadrilateral; star; \(C_4\)-free graph; polarity graph; finite geometry; computational proof; extremal graph theory

# 1. Introduction

For graphs \(H_1,H_2\), the Ramsey number \(R(H_1,H_2)\) is the least integer \(N\) such that every graph \(G\) on \(N\) vertices contains \(H_1\), or the complement \(\overline G\) contains \(H_2\). This study concerns

\[
f(n):=R(C_4,K_{1,n}),
\]

where \(C_4\) is the four-cycle and \(K_{1,n}\) is the star with \(n\) leaves.

The problem has an equivalent minimum-degree formulation. A graph avoids \(K_{1,n}\) exactly when its maximum degree is at most \(n-1\). Thus \(f(n)\) is the least \(N\) for which no \(C_4\)-free graph on \(N\) vertices has minimum degree at least \(N-n\). Exact values are difficult because both sides must be settled: a lower bound requires an explicit high-minimum-degree \(C_4\)-free graph, while an upper bound requires ruling out every graph at the next order.

The modern literature emphasizes that only a small fraction of exact values are known and that there is no universal construction for the associated Ramsey graphs. Finite projective geometry supplies the principal structured source of lower witnesses: orthogonal-polarity graphs have approximately \(q^2\) vertices, degree approximately \(q\), and no four-cycle. Published theorems determine selected parameter families near prime-power scales, but leave discrete gaps between them.

The present work targets one such gap at the prime \(q=17\). A 2025 survey records the exact family

\[
f(q(q-1)-t)=q^2-t
\]

for odd prime powers \(q\ge5\) and even \(t=2,4,\ldots,2\lceil q/4\rceil\). At \(q=17\), this stops at \(t=10\). The next even offset is \(t=12\), corresponding to

\[
n=17\cdot16-12=260,
\qquad q^2-t=289-12=277.
\]

The question is therefore whether the apparent continuation \(f(260)=277\) is valid. It is not a consequence of the published family, because \(t=12\) lies outside its stated range. The central obstacle is a lower certificate: a \(C_4\)-free graph on 276 vertices with minimum degree at least 16.

This manuscript documents the full investigation: threshold definition, candidate screening, frontier audit, construction search, exact proof, adversarial verification, post-discovery novelty review, and reproducibility package.

# 2. State of the frontier before this study

## 2.1 General bounds and the adjacent-value inequality

Two classical tools locate the target.

First, Parsons proved

\[
f(n)\le n+\lceil\sqrt n\rceil+1.
\]

For \(n=260\), this gives \(f(260)\le278\).

Second, Chen proved the adjacent inequality

\[
f(n-1)\ge f(n)-2.
\]

The published \(q=17,t=10\) case gives

\[
f(262)=279.
\]

Applying the adjacent inequality twice yields

\[
f(261)\ge277,
\qquad
f(260)\ge275.
\]

## 2.2 The sharper prior upper bound

Version 1 of Boza's 2024 preprint states that, when \(n\) is even and \(\lceil\sqrt n\rceil\) is odd,

\[
f(n)\le n+\left\lceil\sqrt{n-\lceil\sqrt n\rceil+2}\right\rceil+1.
\]

For \(n=260\), \(\lceil\sqrt{260}\rceil=17\) and

\[
\left\lceil\sqrt{260-17+2}\right\rceil
=\lceil\sqrt{245}\rceil=16,
\]

so this theorem gives \(f(260)\le277\). The current version of the preprint no longer states this particular theorem, but version 1 remains public prior art. Accordingly, this study does **not** claim the upper bound \(277\) as new. A short independent proof is included so that the exact result does not depend on a withdrawn statement.

## 2.3 Exact pre-study interval

Combining the strongest source-located bounds gives

\[
\boxed{275\le f(260)\le277}.
\]

The unresolved alternatives were \(275,276,277\). A 276-vertex graph with minimum degree 16 would eliminate the first two values at once and close the interval exactly.

## 2.4 Why this frontier matters

This target is narrow, but it is positioned at a genuine construction boundary. The known \(q=17\) family reaches offsets \(t=2,4,6,8,10\); \(t=12\) is the first even step outside the theorem. Moreover, the 2025 survey explicitly frames exact determination of \(R(C_4,K_{1,n})\) as difficult, records that only a small fraction of exact values are known, and identifies polarity graphs as the dominant source of Ramsey constructions.

# 3. Breakthrough criterion fixed before the final search

The following definitions were fixed before the final target was selected and were not altered after the computation.

**Novel result.** A statement or certificate not previously reported, regardless of importance.

**Incremental advance.** A modest one-sided bound improvement, a larger search, an additional witness, or an expected parameter extension that leaves the central uncertainty unresolved.

**Minor breakthrough.** A result that materially changes the frontier of a specific problem, such as exactly resolving a source-located open Ramsey value, decisively overturning a conjectured value, or introducing a qualitatively new certifying method that eliminates the remaining possibilities.

**Major breakthrough.** A result with broader field-wide reach, such as an infinite exact family, a major asymptotic improvement, or a general structural theorem.

The minimum acceptable outcome was fixed as a **minor breakthrough**. Operationally, for this project that required:

1. exact determination of at least one unresolved value of \(R(C_4,K_{1,n})\);
2. independently auditable lower and upper arguments;
3. a post-result novelty search finding no prior exact report;
4. reproducible code and static certificates.

A new lower bound alone, a failed search, or a conjectural pattern would not meet the threshold.

# 4. Literature, opportunity search, and candidate ranking

## 4.1 Candidate generation

Several possible breakthrough opportunities were considered rather than committing to the first plausible task. The ranking optimized the product of frontier importance, tractability, verifiability, and novelty confidence. Scores were ordinal from 1 to 5 and were used only for triage.

| Candidate | Importance | Tractability | Verifiability | Novelty confidence | Threshold chance | Composite |
|---|---:|---:|---:|---:|---:|---:|
| Exact \(R(C_4,K_{1,260})\), first even \(q=17\) offset beyond \(t\le10\) | 4 | 5 | 5 | 4 | 5 | 23 |
| Exact adjacent value \(R(C_4,K_{1,259})\) | 4 | 3 | 5 | 4 | 3 | 19 |
| Infinite extension of the \(q(q-1)-t\) theorem to \(t=12\) | 5 | 2 | 5 | 4 | 2 | 18 |
| Exhaustive distance-antimagic classification at order ten | 3 | 3 | 5 | 3 | 2 | 16 |
| Stretched Littlewood-Richardson positivity counterexample | 5 | 1 | 4 | 4 | 1 | 15 |

The adjacent target \(n=259\) was also investigated. Its upper side admitted a promising exact reduction, but no matching lower construction was obtained. Because it did not meet the fixed exact-resolution threshold, it was deferred rather than promoted as a completed result. The \(n=260\) target yielded both sides.

## 4.2 Pre-study novelty audit

The search covered the 2025 field survey, the principal 2015-2017 finite-field and polarity-graph papers, both public versions of Boza's preprint, the dynamic small-Ramsey survey, exact-phrase web searches, scholarly metadata, arXiv, and repository-oriented queries.

Searches included notation variants of \(R(C_4,K_{1,260})\), the proposed value 277, the equivalent \(q=17,t=12\) formulation, and construction-oriented phrases such as “276-vertex \(C_4\)-free graph with minimum degree 16” and “delete 31 vertices from \(ER(17)\).” No prior exact report or matching certificate was located before computation.

# 5. Research question

The precise research question was:

> **Does there exist a \(C_4\)-free graph on 276 vertices with minimum degree at least 16?**

A positive answer would prove \(f(260)\ge277\). Since the source-located upper bound was already 277, this would establish

\[
f(260)=277
\]

and meet the fixed breakthrough threshold.

Equivalently, the target was to find an induced 276-vertex subgraph of a structured \(C_4\)-free host with complement maximum degree at most 259.

# 6. Data, materials, and computational resources

No experimental or proprietary data were used. Every input is generated from the mathematical definition.

## 6.1 Finite field and projective points

All arithmetic is over the prime field \(\mathbb F_{17}\). The 307 points of \(PG(2,17)\) are represented canonically, in this order, by

\[
(1,a,b)\quad(a,b\in\mathbb F_{17}),
\qquad
(0,1,b)\quad(b\in\mathbb F_{17}),
\qquad
(0,0,1).
\]

This gives 289 + 17 + 1 = 307 representatives.

## 6.2 Ambient graph

The simple orthogonal-polarity graph \(ER(17)\) joins two **distinct** projective points \(x,y\) when

\[
x\cdot y\equiv0\pmod{17}.
\]

Loops at absolute points are omitted. Direct reconstruction gives:

| Ambient statistic | Exact value |
|---|---:|
| Vertices | 307 |
| Edges | 2,754 |
| Degree distribution | \(17^{18}18^{289}\) |
| Maximum pairwise common-neighbor count | 1 |
| Four-cycles | 0 |

The maximum common-neighbor count one is an exhaustive computational restatement of \(C_4\)-freeness.

## 6.3 Software and recorded environment

The discovery search was implemented in C++17. All proof-critical verification programs use only Python's standard library. The recorded environment was:

- Python 3.13.5;
- g++ 14.2.0;
- 64-bit Linux.

Hardware speed affects only discovery time. Verification depends solely on the static deletion sets, coordinates, and edge lists.

# 7. Methods

## 7.1 Reduction to a deletion problem

A retained vertex of ambient degree 17 may lose at most one neighbor if its final degree is to remain at least 16. A retained vertex of ambient degree 18 may lose at most two. Thus, for a deletion set \(D\) of size 31, the constraint is

\[
|N_{ER(17)}(v)\cap D|\le d_{ER(17)}(v)-16
\quad\text{for every }v\notin D.
\]

Any feasible deletion immediately yields a 276-vertex \(C_4\)-free graph with minimum degree at least 16.

## 7.2 Search objective

For each retained vertex \(v\), define the excess

\[
e_v=\max\left(0,
|N(v)\cap D|-[d_{ER(17)}(v)-16]
\right).
\]

The search minimized

\[
P(D)=\sum_{v\notin D,\ e_v>0}
\left(1000+100e_v^2+e_v\right).
\]

A score of zero is exactly the target feasibility condition.

## 7.3 Local-search procedure

The search maintains 31 deleted vertices and proposes swaps between one deleted and one retained point. Proposals are biased toward currently deficient retained vertices. Worsening moves may be accepted under a decaying simulated-annealing temperature, and the state is restarted after a long stagnant period. The archived parameters are:

- initial temperature: 2,200;
- cooling multiplier: 0.99997 per iteration;
- minimum temperature: 0.1;
- probability of a deficiency-focused proposal: 0.88;
- stagnation restart threshold: 300,000 iterations.

The primary seed 2603 reached score zero at iteration 786,389. Seeds 2601, 2602, and 2604 independently reached score zero at iterations 4,331,726; 14,905,923; and 5,195,084, respectively.

The heuristic is not trusted as a proof. It only discovers deletion lists. Each resulting graph is rebuilt and checked exhaustively.

## 7.4 Exact lower-bound verification

The construction verifier:

1. regenerates all 307 projective points;
2. reconstructs every ambient edge from the dot-product rule;
3. applies each deletion list;
4. regenerates the complete retained edge set;
5. checks all degrees;
6. checks every one of the \(\binom{276}{2}=37,950\) vertex pairs for common-neighbor multiplicity;
7. verifies complement maximum degree;
8. compares the regenerated graph with the stored JSON and raw edge list.

A second implementation deliberately ignores finite geometry and reads only each raw edge list. It uses 276 integer bitsets to recompute degrees, codegrees, triangles, and complement degrees.

## 7.5 Upper-bound method

The upper proof is analytic and requires no solver. It uses only the disjointness of second neighborhoods in a \(C_4\)-free graph and parity of the degree sum. Section 8.3 gives the complete proof.

# 8. Results

## 8.1 Primary deletion certificate

Using zero-based indices in the canonical projective-point order, delete

```text
[0,9,20,24,40,61,67,70,100,112,117,130,150,166,175,195,
 207,221,222,225,236,237,253,264,267,287,292,293,300,302,304]
```

The induced graph \(H\) on the remaining 276 points has the following exact statistics.

| Statistic | Value |
|---|---:|
| Order | 276 |
| Size | 2,279 |
| Degree distribution | \(16^{134}17^{142}\) |
| Minimum degree | 16 |
| Maximum degree | 17 |
| Pair codegree 0 | 2,558 |
| Pair codegree 1 | 35,392 |
| Maximum pair codegree | 1 |
| Triangles | 638 |
| Complement maximum degree | 259 |

The codegree counts sum to

\[
2558+35392=37950=\binom{276}{2}.
\]

Since no vertex pair has two common neighbors, \(H\) contains no \(C_4\). Since \(\delta(H)=16\),

\[
\Delta(\overline H)=275-16=259,
\]

so \(\overline H\) contains no \(K_{1,260}\).

**Proposition 1.** \(R(C_4,K_{1,260})\ge277\).

**Proof.** The explicit graph \(H\) has 276 vertices, contains neither a \(C_4\) nor, in its complement, a star with 260 leaves. Therefore 276 vertices do not force either forbidden graph. \(\square\)

## 8.2 Replicate deletion certificates

Three additional seeds produced different 31-index deletion lists. Every retained graph has the same exact statistics listed above. No claim is made that the four graphs are pairwise nonisomorphic; they are independent deletion certificates and search replays.

| Search seed | First score-zero iteration | Static certificate |
|---:|---:|---|
| 2601 | 4,331,726 | verified |
| 2602 | 14,905,923 | verified |
| 2603 | 786,389 | verified; primary |
| 2604 | 5,195,084 | verified |

The search is a discovery mechanism only; the static witnesses are the proof objects.

## 8.3 Matching upper bound

**Theorem 2.** Every \(C_4\)-free graph on 277 vertices has a vertex of degree at most 16. Consequently,

\[
R(C_4,K_{1,260})\le277.
\]

**Proof.** Suppose, for contradiction, that \(G\) is a \(C_4\)-free graph on 277 vertices with

\[
\delta(G)\ge17.
\]

Fix any vertex \(v\), and write \(d=d(v)\). For each \(u\in N(v)\), define

\[
S_u=N(u)\setminus\{v\}.
\]

Because \(d(u)\ge17\), every \(S_u\) has at least 16 elements. The sets \(S_u\) are pairwise disjoint. Indeed, if a vertex \(x\) belonged to both \(S_{u_1}\) and \(S_{u_2}\) for distinct neighbors \(u_1,u_2\) of \(v\), then

\[
v-u_1-x-u_2-v
\]

would be a four-cycle.

All sets \(S_u\) lie inside \(V(G)\setminus\{v\}\), which has 276 vertices. Therefore

\[
16d\le276,
\]

and hence \(d\le17\). Since \(v\) was arbitrary and \(\delta(G)\ge17\), every vertex has degree exactly 17. But a 17-regular graph on 277 vertices would have degree sum

\[
277\cdot17=4709,
\]

which is odd, contradicting the handshaking lemma. Thus no such \(G\) exists.

If a graph on 277 vertices has complement avoiding \(K_{1,260}\), then its minimum degree is at least \(277-260=17\). The contradiction therefore proves the Ramsey upper bound. \(\square\)

## 8.4 Main theorem

Combining Proposition 1 and Theorem 2 gives the exact result.

**Theorem 3 (Main theorem).**

\[
\boxed{R(C_4,K_{1,260})=277}.
\]

Equivalently, every graph on 277 vertices contains a four-cycle or its complement contains a star with 260 leaves, while the archived 276-vertex graph avoids both.

# 9. Verification and attempts to falsify the result

A surprising exact result was treated as presumptively wrong until it survived independent checks.

## 9.1 Finite-geometry reconstruction

For all four deletion lists, a standard-library Python program regenerated \(PG(2,17)\), rebuilt \(ER(17)\) from the dot-product condition, and recomputed the retained graphs. The program verified:

- exactly 307 ambient points and 2,754 ambient edges;
- ambient degree distribution \(17^{18}18^{289}\);
- ambient maximum codegree one;
- exactly 31 distinct deleted indices;
- exactly 276 retained points;
- exact agreement between coordinate-derived and stored edge sets;
- retained order 276 and size 2,279;
- retained degree distribution \(16^{134}17^{142}\);
- maximum retained codegree one;
- complement maximum degree 259.

All four certificates passed.

## 9.2 Coordinate-free edge-list audit

A separate implementation imports no projective-geometry code. It parses only the raw edge lists, rejects loops and duplicate edges, constructs adjacency bitsets, and independently verifies every Ramsey-relevant property. All four edge lists passed with identical statistics.

This separation attacks a major mundane failure mode: an error shared by the projective-point generator and the certificate generator cannot automatically survive a verifier that sees only an unlabeled simple graph.

## 9.3 Deterministic discovery replay

The archived C++17 search was rebuilt from source. With the recorded command and seed 2603, it returned the exact primary deletion list at iteration 786,389. The other three archived seeds also reproduce their own lists under the documented long replay command.

The replay is evidence about reproducibility, not mathematical validity. The static certificate remains sufficient even if the search implementation is ignored.

## 9.4 Deliberate corruption tests

Five negative controls were injected:

| Corruption | Expected failure | Observed result |
|---|---|---|
| Duplicate deletion index | malformed construction | rejected |
| Remove an edge at a degree-16 vertex | minimum degree falls to 15 | rejected |
| Add a selected nonedge | a vertex pair gains two common neighbors, creating \(C_4\) | rejected |
| Inject a loop | invalid simple graph | rejected |
| Duplicate an edge | invalid edge list | rejected |

The observed diagnostic for the added edge was a pair with exactly two common neighbors; the removed-edge diagnostic reported minimum degree 15.

## 9.5 Exact upper-bound audit

A dependency-free verifier recomputes the upper proof's integer arithmetic:

\[
277-260=17,
\qquad
16\cdot18=288>276,
\qquad
277\cdot17=4709\equiv1\pmod2.
\]

No floating-point calculation or probabilistic inference enters the theorem.

## 9.6 Integrity and rerun status

The full command `./run_all_checks.sh` regenerated all certificates, ran both lower verifiers, audited the upper proof, executed the negative controls, and replayed the primary search. Its final recorded line was:

```text
ALL CORE CHECKS PASSED
```

# 10. Comparison with the previous frontier

| Quantity | Before this study | After this study |
|---|---:|---:|
| \(R(C_4,K_{1,260})\) | \(275\le f(260)\le277\) | \(f(260)=277\) |
| Best lower bound | 275 | 277 |
| Lower-bound improvement | - | +2 |
| Remaining candidate values | 3 values: 275, 276, 277 | 1 value |
| 276-vertex \(C_4\)-free graph with \(\delta\ge16\) | not located | four explicit deletion certificates |
| Published \(q=17\) even-offset endpoint | \(t=10\) | additional exact point at \(t=12\) |

The result closes 100% of the source-located uncertainty at this parameter. It is stronger than a one-sided numerical improvement: both alternatives below 277 are eliminated by a single explicit construction, and the upper endpoint is independently proved.

# 11. Novelty verification after discovery

After the exact value and deletion certificate were obtained, a second adversarial search was conducted around the discovered statement rather than the original topic. Queries included:

```text
"R(C_4,K_{1,260})"
"R(C4,K1,260)"
"R(C_4, K_{1, 260})"
"277" "K1,260" C4
"quadrilateral" "star" Ramsey 260 277
site:arxiv.org "K1,260" C4 Ramsey
site:github.com "R(C4,K1,260)"
"q(q-1)-12" Ramsey star quadrilateral
"t = 12" "R(C4" star q=17
"ER(17)" "minimum degree 16"
"orthogonal polarity graph" "276" "minimum degree 16"
"C4-free graph" "276 vertices" "minimum degree"
"delete 31" polarity graph 17 C4
```

The search revisited the current field survey, the exact finite-field papers, both arXiv versions of Boza's preprint, scholarly metadata, general web results, and repository results. No prior statement \(R(C_4,K_{1,260})=277\), no matching 31-point deletion, and no equivalent 276-vertex minimum-degree-16 construction was located.

This is evidence, not a proof of universal novelty. Unpublished calculations, private correspondence, non-indexed theses, or very recent manuscripts may exist. The appropriate status is therefore “candidate new theorem pending specialist bibliographic review,” not an unconditional claim of priority.

# 12. Why the result meets the predefined breakthrough threshold

The threshold was exact resolution of a genuinely unresolved value with independently auditable certificates. The result meets each component:

1. **Decisive frontier change.** The three-value interval \(275\)-\(277\) is replaced by the exact value 277.
2. **Resolution rather than extension alone.** The central existence question is answered by an explicit graph; no uncertainty remains at \(n=260\).
3. **Location at a known bottleneck.** The result occupies the first even \(q=17\) offset outside the stated range of the published exact family.
4. **Independent auditability.** The lower side is a finite graph certificate verified from both coordinates and raw edges; the upper side is a short analytic contradiction.
5. **Adversarial survival.** Reconstruction, independent implementation, deterministic replay, corruption tests, and exact arithmetic all passed.
6. **Post-discovery novelty evidence.** No prior exact report or certificate was found in the targeted search.

The work is not a major breakthrough. It does not prove the \(t=12\) case for every odd prime power, settle the asymptotics of \(f(n)\), classify all extremal witnesses, or resolve the broad open problems in the survey. Its defensible classification is a **minor breakthrough within the narrow exact star-quadrilateral Ramsey-number program**, contingent on external verification of proof and priority.

# 13. Limitations

1. The manuscript has not been peer reviewed.
2. A literature search cannot rule out every unpublished or poorly indexed result.
3. The lower witnesses were discovered heuristically, although their validity is independent of the heuristic.
4. The four deletion lists may yield isomorphic graphs; no pairwise nonisomorphism or uniqueness claim is made.
5. No classification of all 276-vertex extremal graphs is attempted.
6. The result proves one exact value, not an infinite family.
7. The computation does not establish that analogous deletions exist for every larger prime power at offset \(t=12\).
8. The adjacent \(n=259\) target remains unresolved in this study.

There is no sampling uncertainty in the theorem itself. Every mathematical assertion needed for the exact value is finite and deterministic. The remaining uncertainties concern novelty, external review, and generalization.

# 14. Scientific implications

## 14.1 Polarity deletion reaches beyond the uniform theorem range

The construction shows that \(ER(17)\) contains a large induced subgraph supporting the next even offset after the published \(q=17\) sequence. Uniform finite-field formulas often stop because a construction is guaranteed only over a parameter range; a targeted deletion optimization can cross that boundary at a concrete prime.

## 14.2 The lower-bound problem has a useful capacity formulation

For the target minimum degree \(q-1\), each degree-\(q\) absolute point can tolerate one deleted neighbor and each degree-\(q+1\) nonabsolute point can tolerate two. This turns the Ramsey construction into a sparse capacitated deletion problem with exceptionally cheap exact verification. The formulation may be useful for testing \(t=12\) at other odd prime powers.

## 14.3 Exact values inform broader conjectures

The new value satisfies

\[
260+\lceil\sqrt{260}\rceil
=277,
\]

placing it at the lower of the two values highlighted in the survey's Problem 7.2. One data point does not settle that problem, but it extends the exact evidence to a parameter that was outside the principal \(q=17\) family.

## 14.4 Search and proof are cleanly separated

The study illustrates a robust computational-mathematics pattern: use heuristic optimization only to locate a finite certificate, then replace trust in the heuristic with exhaustive, dependency-light verification. This makes the result portable across machines and independently checkable without reproducing the search trajectory.

# 15. Reproducibility

## 15.1 Package contents

```text
Ramsey_C4_Star_260_Study/
  README.md
  paper/
    paper.md
    main.tex
    Exact_Ramsey_C4_Star_260.pdf
    frontier_q17.png
  code/
    ramsey260_common.py
    generate_witnesses.py
    verify_witnesses.py
    independent_edge_list_check.py
    verify_upper_bound.py
    adversarial_mutation_tests.py
    search_polarity_deletion.cpp
  data/
    deleted_points_seed2601.json
    deleted_points_seed2602.json
    deleted_points_seed2603.json
    deleted_points_seed2604.json
    witness_260_seed*.json
    witness_260_seed*.edgelist
    witness_260_seed*_vertex_map.csv
  docs/
    candidate_screening.md
    novelty_search_log.md
    research_record.md
  results/
    generation_summary.json
    finite_geometry_verification.json
    independent_edgelist_verification.json
    upper_bound_verification.json
    negative_controls.json
  logs/
    verification.log
    search_replay.log
    search_seed2601.log
    search_seed2602.log
    search_seed2604.log
  run_all_checks.sh
  replay_search.sh
  replay_all_searches.sh
  environment.txt
  manifest.json
  SHA256SUMS
```

## 15.2 Core verification

From the package root:

```bash
./run_all_checks.sh
```

The proof checks require only Python's standard library. If a C++17 compiler is present, the script also rebuilds and replays the primary discovery search.

The static proof can be audited without replaying the search:

```bash
PYTHONPATH=code python3 code/generate_witnesses.py
PYTHONPATH=code python3 code/verify_witnesses.py
PYTHONPATH=code python3 code/independent_edge_list_check.py
PYTHONPATH=code python3 code/verify_upper_bound.py
PYTHONPATH=code python3 code/adversarial_mutation_tests.py
```

## 15.3 Discovery replay

The primary replay is:

```bash
./replay_search.sh
```

To replay all four seeds:

```bash
./replay_all_searches.sh
```

The all-seed replay is not required to verify the theorem and may take longer depending on the compiler and machine.

## 15.4 Certificate semantics

For a stored deletion list, regenerate the canonical projective points, join distinct orthogonal pairs, discard every edge incident with a deleted point, and relabel retained points in increasing ambient-index order. The resulting raw edge list must have exactly 276 vertices and satisfy the statistics in Table 3. Any graph program can independently audit the raw edge list; no specialized finite-geometry package is required.

# 16. Conclusion

Before this investigation, the strongest source-located results left

\[
275\le R(C_4,K_{1,260})\le277.
\]

A result closing that interval exactly was fixed in advance as the minimum breakthrough threshold. The investigation searched induced subgraphs of \(ER(17)\), found four explicit 31-point deletion certificates, and verified that each retained graph has 276 vertices, minimum degree 16, and no four-cycle. This proves the lower bound 277. A local disjoint-neighborhood count forces any hypothetical 277-vertex avoiding graph to be 17-regular, and parity rules it out, proving the matching upper bound.

Therefore the completed result is

\[
\boxed{R(C_4,K_{1,260})=277}.
\]

The result closes the full prior interval and adds the first even \(q=17\) offset beyond the published \(t\le10\) family. Its proof survives independent graph representations, exact arithmetic, deliberate corruptions, and deterministic replay. A post-discovery search found no earlier exact report or matching construction. Subject to external mathematical and bibliographic review, this supports classification as a minor scientific breakthrough in the specific exact-value program.

# Appendix A. All four deletion lists

All indices are zero-based in the canonical projective-point ordering defined in Section 6.

**Seed 2601**

```text
[2,24,25,41,52,61,72,97,98,112,117,119,127,130,133,135,
 142,156,171,195,204,212,213,215,219,229,246,260,277,296,303]
```

**Seed 2602**

```text
[13,14,18,24,45,64,77,85,108,118,135,142,160,166,173,174,
 176,180,182,183,199,209,234,240,252,261,263,278,287,295,305]
```

**Seed 2603 (primary)**

```text
[0,9,20,24,40,61,67,70,100,112,117,130,150,166,175,195,
 207,221,222,225,236,237,253,264,267,287,292,293,300,302,304]
```

**Seed 2604**

```text
[4,24,34,37,38,50,51,60,63,65,85,87,89,95,96,136,
 137,140,141,170,171,174,183,186,187,193,195,202,250,270,306]
```

# Appendix B. AI-assistance disclosure

This investigation was conducted through an AI-assisted research workflow coordinated for Zach Waddle. OpenAI GPT-5.6 Pro searched and synthesized the literature, generated and ranked candidate targets, wrote and executed the computational search, derived and checked the proof, created the verification suite, performed adversarial tests, and drafted the manuscript. The named human author is responsible for deciding whether to circulate, revise, or submit the work. Independent specialist review is explicitly requested.

# References

1. Y. Chen, X. Zhang, and Y. Zhang, “Star-quadrilateral Ramsey Number and Beyond,” *Advances in Mathematics (China)* 54(2) (2025), 292-314. DOI: 10.11845/sxjz.2024006a.
2. L. Boza, “Exact Values and Bounds for Ramsey Numbers of \(C_4\) Versus a Star Graph,” arXiv:2409.12770v1 (2024); revised as v2 (12 June 2026). DOI: 10.48550/arXiv.2409.12770.
3. X. Zhang, Y. Chen, and T. C. E. Cheng, “Some Values of Ramsey Numbers for \(C_4\) versus Stars,” *Finite Fields and Their Applications* 45 (2017), 73-85. DOI: 10.1016/j.ffa.2016.11.012.
4. X. Zhang, Y. Chen, and T. C. E. Cheng, “Polarity Graphs and Ramsey Numbers for \(C_4\) versus Stars,” *Discrete Mathematics* 340(4) (2017), 655-660. DOI: 10.1016/j.disc.2016.12.005.
5. T. D. Parsons, “Ramsey Graphs and Block Designs, I,” *Transactions of the American Mathematical Society* 209 (1975), 33-44.
6. T. D. Parsons, “Graphs from Projective Planes,” *Aequationes Mathematicae* 14 (1976), 167-189.
7. G. Chen, “A Result on \(C_4\)-Star Ramsey Numbers,” *Discrete Mathematics* 163 (1997), 243-246.
8. Y. Wu, Y. Sun, R. Zhang, and S. P. Radziszowski, “Ramsey Numbers of \(C_4\) versus Wheels and Stars,” *Graphs and Combinatorics* 31 (2015), 2437-2446.
9. S. P. Radziszowski, “Small Ramsey Numbers,” *Electronic Journal of Combinatorics*, Dynamic Survey 1, revision 18 (24 April 2026).
