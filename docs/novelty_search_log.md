# Pre- and post-discovery novelty search log

**Search date:** 2026-08-08  
**Target statement:** `R(C4,K1,260)=277`

## Closest prior results located

1. Chen, Zhang, and Zhang (2025), *Star-quadrilateral Ramsey Number and Beyond*, Theorem 2.6: for odd prime powers `q>=5` and `t=2,4,...,2*ceil(q/4)`, `R(C4,K1,q(q-1)-t)=q^2-t`. At `q=17`, the theorem stops at `t=10`, two units before the present `t=12` case.
2. Boza, arXiv:2409.12770v1 (2024), Theorem 5: an upper theorem for even `n` with odd `ceil(sqrt(n))` implies `R(C4,K1,260)<=277`. The current v2 (2026) does not state that theorem. This study does **not** claim the upper bound as new; it supplies a short independent proof.
3. Parsons' classical bound gives `R(C4,K1,260)<=278`.
4. The adjacent-value inequality `f(n-1)>=f(n)-2`, combined twice with the published exact value `f(262)=279`, gives only `f(260)>=275`.

## Exact-value queries

Queries were run with spacing, punctuation, and notation variants:

- `"R(C_4,K_{1,260})"`
- `"R(C4,K1,260)"`
- `"R(C_4, K_{1, 260})"`
- `"277" "K1,260" C4`
- `"quadrilateral" "star" Ramsey 260 277`
- `site:arxiv.org "K1,260" C4 Ramsey`
- `site:github.com "R(C4,K1,260)"`

No prior exact report was located.

## Formula- and construction-oriented queries

- `"q(q-1)-12" Ramsey star quadrilateral`
- `"t = 12" "R(C4" star q=17`
- `"ER(17)" "minimum degree 16"`
- `"orthogonal polarity graph" "276" "minimum degree 16"`
- `"C4-free graph" "276 vertices" "minimum degree"`
- `"delete 31" polarity graph 17 C4`

No matching theorem, deletion list, edge list, or 276-vertex minimum-degree-16 construction was located.

## Sources and repositories checked

- the current 2025 field survey and its reference trail;
- both public arXiv versions of Boza's preprint;
- exact web and scholarly-metadata searches;
- arXiv-focused and repository-focused queries;
- certificate-oriented searches designed to find the graph even if the Ramsey consequence was unstated.

## Conclusion and limitation

The result appears absent from the current indexed literature searched. This is strong evidence of novelty, not a logical proof of absence from every thesis, private manuscript, non-indexed proceeding, or unpublished computation. External bibliographic review is requested before formal publication.
