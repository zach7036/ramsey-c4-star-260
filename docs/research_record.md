# End-to-end research record

## Fixed benchmark

The minimum acceptable outcome was exact resolution of a source-located unresolved value of `R(C4,K1,n)`, not merely a one-sided bound.

## Frontier identified before computation

The 2025 survey theorem gives

`R(C4,K1,q(q-1)-t)=q^2-t`

for odd prime powers `q>=5` and even `t=2,4,...,2*ceil(q/4)`. At `q=17`, this reaches `t=10`, hence `R(C4,K1,262)=279`, but not `t=12`, which is `n=260`.

Using the adjacent-value inequality twice gives `R(C4,K1,260)>=275`. Parsons' general upper bound gives 278. A public 2024 preprint version gives the sharper upper bound 277 for this even parameter. Thus the strongest source-located interval used for screening was `275 <= R(C4,K1,260) <= 277`.

## Computation

The orthogonal-polarity graph `ER(17)` was generated exactly from `PG(2,17)`. A local-search algorithm selected 31 vertices to delete while enforcing that every retained degree is at least 16. The primary seed 2603 reached a valid deletion after 786,389 swaps. Three other seeds yielded distinct deletion lists.

## Result

Each deletion leaves an induced graph on 276 vertices with 2,279 edges, degree distribution `{16:134,17:142}`, no pair with two common neighbors, and complement maximum degree 259. This proves the lower bound 277.

For the upper bound, a hypothetical 277-vertex avoiding graph has minimum degree at least 17. For every vertex `v`, the sets `N(u)\{v}` for `u in N(v)` are pairwise disjoint and each has size at least 16, so `16*d(v)<=276` and `d(v)<=17`. The graph would therefore be 17-regular on 277 vertices, contradicting the handshaking lemma. This proves the upper bound 277.

## Validation

Four finite-geometry reconstructions, an independent raw-edge-list bitset checker, exact upper-bound arithmetic, adversarial mutation tests, and a deterministic replay of the primary search all pass. The search is discovery-only; the static graph certificates constitute the proof.
