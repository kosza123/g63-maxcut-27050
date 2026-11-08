# G63 Max-Cut: a publicly verifiable solution of 27,050

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24049667.svg)](https://doi.org/10.5281/zenodo.24049667)

**A publicly verifiable G63 Max-Cut solution of 27,050, improving upon the published 27,047 reference.**

![G63 Max-Cut 27,050](media/g63_maxcut_27050.png)

| | |
|---|---|
| Instance | G63 from the G-set benchmark (7,000 vertices, 41,459 unit-weight edges) |
| Published reference | 27,047 — Khan & Shukla, arXiv:2510.21105 (2025) |
| This solution | **27,050** (+3 edges) |
| Method | Population annealing Monte Carlo on a GPU (a known method; see [METHODOLOGY.md](METHODOLOGY.md)) |
| Hardware | one NVIDIA GeForce RTX 3060 Ti (consumer GPU) |
| Found | 8 November 2026, 02:13:52 CET, 158.5 minutes into a 7-hour experiment |
| Author | Filip Majchrzak — SAPIO MORPHEUS / COMPLEX (independent research project) |

The point of this repository is that you do not have to trust us: the full configuration is here, together with three
short, dependency-free verifiers. Checking the cut takes less than a second.

## Verify it yourself

1. Download the original instance from the G-set page: `https://web.stanford.edu/~yyye/yyye/Gset/G63`
   (expected sha256 `a1d08e1eed7a32c480e1e71b106c96c6ee280fda1bc7314a33651a8cf493a99b`).
2. Run any of the verifiers:

```bash
python3 verify/verify_cut.py G63 solution/G63_maxcut_27050.txt
node verify/verify_cut.js G63 solution/G63_maxcut_27050.txt
awk -f verify/verify_cut.awk solution/G63_maxcut_27050.txt G63
```

Each verifier reports 27050 on its `CUT` line (Python/Node.js: `CUT              : 27050`; awk: `CUT 27050`). As a control,
the published 27,047 configuration (hexadecimal string in arXiv:2510.21105, read most significant bit first) gives 27,047 with
`python3 verify/verify_cut.py G63 <hexfile> --hex`.

## Files

- `solution/G63_maxcut_27050.txt` — 7,000 characters `0`/`1`; character *k* is the side of vertex *k*+1 (G-set numbering).
- `solution/G63_maxcut_27050.hex` — the same partition as 1,750 hexadecimal digits, each digit read most significant bit first (the hexadecimal format used in arXiv:2510.21105; reading their string this way reproduces 27,047).
- `solution/SHA256SUMS` — checksums of the solution files, of the 1,092-vertex list, and of the original G63 file (last line; the G63 file itself is not in this repository — save your download as `G63` in the repository root and run `sha256sum -c solution/SHA256SUMS` from the root to check all four).
- `verify/` — independent verifiers in Python, Node.js and awk.
- `results/VERIFICATION.md` — all checks performed and their outputs.
- `results/STRUCTURE.md` — how the solution differs from the published 27,047 configuration (one connected 1,092-vertex domain, +3).
- `METHODOLOGY.md` — algorithm, parameters, hardware, timing, statistics, limitations and AI-use statement.
- `paper/` — LaTeX source of the accompanying preprint (not yet submitted).
- `CITATION.cff`, `.zenodo.json` — citation metadata.

## What we claim — and what we do not

- We claim a **verifiable configuration** with cut value 27,050 on G63, which exceeds the published 27,047 reference.
- We do **not** claim that 27,050 is optimal, and we do not claim a new algorithm: population annealing is a known method.
- Status of other reports: every primary source we could verify lists at most 27,047 for G63 (arXiv:2510.21105; arXiv:2606.25203).
  A secondary aggregator page has been described in search snippets as mentioning a value of 27,052; we could not access it
  or find a primary source or configuration for it. If such a configuration exists, it would exceed 27,050.

## Use of AI

The experiment was conceived and directed by Filip Majchrzak. The search code, the execution of the experiment, the
verification tools and the first drafts of the documentation were produced with the AI assistant Claude (Anthropic) acting as
research operator under his direction; three recounts were written by separate AI-agent instances without access to the search
code. See [METHODOLOGY.md](METHODOLOGY.md).

## Citation

If you use this result, please cite the archived record:

> Majchrzak, F. (2026). *G63 Max-Cut: a publicly verifiable solution of 27,050* (Version 1.0.0) [Data set]. Zenodo.
> https://doi.org/10.5281/zenodo.24049667

The DOI above always resolves to the latest version; version 1.0.0 specifically is https://doi.org/10.5281/zenodo.24049668.
GitHub's "Cite this repository" uses `CITATION.cff`.

## Contact

Filip Majchrzak — GitHub [@kosza123](https://github.com/kosza123). Independent re-verification and comparisons with other
methods are very welcome (please open an issue).

## License

Data and documentation: CC BY 4.0 (`LICENSE`). Verifier code: MIT (`LICENSE-CODE`).
