# Structure of the 27,050 solution relative to the published 27,047 configuration

Reference: the 27,047 configuration published in arXiv:2510.21105 (hexadecimal phase string, read most significant bit first).

- Hamming distance (up to global complement): 1140 vertices.
- The differing vertices form 43 connected components in G63.
- Exactly one component changes the cut: a connected set of **1092 vertices** whose flip changes the cut by **+3**.
- The remaining 42 components (sizes [4, 2, 2, 2, 1, 1]...) each change the cut by 0 (zero-cost "free" clusters).
- Flipping only that 1092-vertex component in the published 27,047 configuration gives a cut of **27050**.
- The 27,050 solution is a 1-flip local optimum: no single vertex flip increases the cut (221 vertices have zero gain).

The vertex list of the 1092-vertex component (1-based G-set numbering) is in `domain_1092_vertices.txt`.
Interpretation: the improvement over the 27,047 configuration is a coordinated move of about one thousand vertices (a domain-wall-like rearrangement), not a small local modification.
