# Verification of the 27,050 solution

## Inputs

| item | value |
|---|---|
| Graph | G63, original G-set file `https://web.stanford.edu/~yyye/yyye/Gset/G63` |
| Graph sha256 | `a1d08e1eed7a32c480e1e71b106c96c6ee280fda1bc7314a33651a8cf493a99b` (453,940 bytes) |
| Graph sanity | n = 7,000; m = 41,459 edge lines; all weights 1; vertex indices 1..7,000; no self-loops; no duplicate edges; min degree 4, max degree 589; one connected component |
| Partition | `solution/G63_maxcut_27050.txt`, 7,000 characters `0`/`1`, 3,537 ones |
| Partition sha256 | `2e3d330e3d77d8e68b384daf6b72f59d4a5d5c4d9478ebd6dfd4444bc4a566df` |

## Recounts (all give 27,050)

| # | implementation | notes |
|---|---|---|
| 1 | pure Python edge loop (`verify/verify_cut.py`) | also gives 27,050 for the complement and for the `.hex` file |
| 2 | Node.js (`verify/verify_cut.js`) | |
| 3 | awk (`verify/verify_cut.awk`) | reads the raw G-set file; 41,459 edges read |
| 4 | numpy, spin form `(Σw − xᵀWx)/2` with `x = 2s − 1` | complement identical |
| 5–7 | three further verification passes, each by a separate AI-agent instance without access to the search code, together using gawk, PowerShell, numpy (spin, sparse and dense Laplacian, 0/1 polynomial form) and Node.js | one pass on a freshly downloaded copy of G63 that is byte-identical to the file above |

## Controls

- The published 27,047 configuration (arXiv:2510.21105, hexadecimal, read MSB first) gives **27,047** with the same verifiers.
- Shifting the claimed partition by one position gives 20,744 / 20,588; 200 random partitions average 20,730 (m/2 = 20,729.5).
  So only the stated alignment (character *k* ↔ vertex *k*+1) gives a high cut.
- Flipping vertex 1 changes the recount by exactly its predicted gain.
- The partition is a 1-flip local optimum (no single-vertex flip increases the cut; 221 vertices have zero gain).

## Structure

See `STRUCTURE.md`: relative to the published 27,047 configuration, the solution differs by one connected component of
1,092 vertices whose flip adds +3, plus 42 zero-cost components.

## Search history (summary)

The configuration was found at 2026-11-08 02:13:52 CET by population annealing started from random states (see
`METHODOLOGY.md`). In the same experiment, a first configuration of value 27,048 was found at 01:28:22 and reproduced in
several independent anneals; 27,050 was found once. No configuration above 27,050 was found.
