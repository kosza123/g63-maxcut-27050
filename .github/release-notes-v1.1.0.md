**Correction release.** Our result of 27,050 does improve upon the cited 27,047 configuration (Khan & Shukla, arXiv:2510.21105),
but the presentation in v1.0.0 was misleading because we overlooked an earlier, publicly verifiable G63 configuration with cut value
**27,052**, published by R. Ota and M. Okada on 23 March 2026 ([doi:10.5281/zenodo.19189885](https://doi.org/10.5281/zenodo.19189885)).
The v1.0.0 statements that every verifiable primary source listed at most 27,047 for G63 and that no primary source for 27,052 could be
found were wrong. Researchers have also pointed us to earlier reports of 27,052 (Fujitsu Digital Annealer, 2020 and 2021) and a 2026 report of
27,051, which we have not yet read in the full texts. 27,050 is therefore **not** the highest reported value for G63.

## What changed

- README: correction notice, a table of reported G63 values with sources and verification status, thanks to Kenneth Zick and
  Nikhil Shukla, corrected citation section.
- `.zenodo.json`, `CITATION.cff`: corrected description and references (including the exact title of the Ota & Okada record).
- `paper/main.tex`: corrected abstract, introduction and a correction paragraph.
- `media/g63_maxcut_27050.png`: graphic now shows the highest publicly verifiable cut known to us (27,052) and states that 27,050
  is not a record.
- `results/STRUCTURE.md`: one sentence clarified ("the improvement over the 27,047 configuration").

## What did not change

The solution files, checksums, verifiers and METHODOLOGY.md are identical to v1.0.0. The configuration still has cut value 27,050:

```
2e3d330e3d77d8e68b384daf6b72f59d4a5d5c4d9478ebd6dfd4444bc4a566df  solution/G63_maxcut_27050.txt
d28df54d409d998d77bb0197a747a0df3e04472a056e46f23f68737564f44c10  solution/G63_maxcut_27050.hex
```

No claim of optimality, of a record or of a new algorithm is made. AI use: the correction was drafted with the AI assistant Claude
(Anthropic) and reviewed by the author.
