# Methodology

## Problem

Max-Cut on G63 from the G-set benchmark (7,000 vertices, 41,459 edges, unit weights; vertex degrees from 4 to 589). The cut value of a partition is the number of edges
whose endpoints lie on different sides.

## Algorithm: population annealing Monte Carlo (known method)

Population annealing (Hukushima & Iba 2003; Machta 2010; Wang, Machta & Katzgraber 2015) evolves a population of replicas
while the inverse temperature β is increased; at every temperature step the population is resampled in proportion to the
Boltzmann weights, then each replica is updated by Monte Carlo sweeps. We maximise the cut, i.e. we use weights
∝ exp(β · cut).

Configuration that produced the 27,050 solution:

| parameter | value |
|---|---|
| population size R | 8,192 replicas, independent uniformly random initial states |
| schedule | β geometric from 0.3 to 9.0 in 6,000 steps |
| resampling | systematic resampling with weights exp((β_t − β_{t−1}) · cut), constant population size |
| sweeps per step | 10 heat-bath sweeps; vertex flip probability 1 / (1 + exp(−β · g)), g = change of the cut |
| update order | by colour classes of a greedy (largest-degree-first) proper colouring with 8 colours, so all vertices of one class are updated in parallel |
| final step | zero-temperature quench (only cut-increasing flips) of every replica |
| run | anneal number 12 of a sequence of independent anneals (each anneal starts from fresh random states) |

## Implementation and hardware

- One NVIDIA GeForce RTX 3060 Ti (8 GB), CUDA kernels compiled at runtime through CuPy (NVRTC); host: Windows 11, 16 CPU cores.
- Spins stored as bytes in vertex-major / replica-minor layout, so that a warp reads one vertex across 32 replicas (coalesced memory access).
- Counter-based pseudo-random numbers (splitmix64 hashing of seed, step, vertex, replica).
- The cut of every replica is tracked incrementally and recounted from scratch periodically (drift check); every reported
  configuration was recounted independently (see `results/VERIFICATION.md`).
- Throughput: about 10⁹–10¹⁰ single-spin updates per second; one anneal with these parameters took about 10 minutes
  (615 s on average, while the GPU was shared with a second annealing process).

## Timeline (single 7-hour experiment, start 2026-11-07 23:35:21 CET)

| time from start | event |
|---|---|
| 0–50 min | verification of the published 27,047 configuration; local search (tabu search) and exact large-neighbourhood search around it (no improvement); first population-annealing runs |
| 113 min | first configuration above the reference: 27,048 |
| 158.5 min | **27,050** (this repository) |
| 420 min | end of the experiment; no configuration above 27,050 was found |

## Statistics of the deep anneals

Across 66 complete anneals with population 8,192, started from random states with three schedules chosen during the
experiment (β up to 7, 9 and 10; 4,000, 6,000 and 9,000 steps):

| best cut of the anneal | number of anneals |
|---|---|
| 27,046 | 2 |
| 27,047 | 54 |
| 27,048 | 9 |
| 27,050 | 1 |

We checked one saved 27,047 state from each of 55 of the 66 anneals (the anneals whose saved states included a 27,047 state);
all belonged to the "family" of the published configuration (they differ from it only by zero-cost clusters). Shorter anneals (population 2,048–4,096, at most 1,500
steps) ended between 26,957 and 27,045.

## Observations on the landscape

- The 27,047 level is a large plateau: in a 27,047 configuration about 235 vertices have zero flip gain, and pairs of such
  configurations differ only by independent zero-cost clusters.
- Tabu search found no improvement; exact re-optimisation (mixed-integer programming) of thousands of ball-shaped regions of 300–1,200 vertices around the
  published configuration found no improvement.
- The improvement documented here is a coordinated move of about a thousand vertices: relative to the published configuration,
  27,050 corresponds to flipping one connected set of 1,092 vertices (+3); see `results/STRUCTURE.md`.

## Limitations

- One instance, one experiment; parameters were adjusted during the experiment; no equal-hardware comparison with other solvers.
- Population annealing is a known method; we do not claim a new algorithm.
- We do not claim optimality of 27,050.
- The published run times for 27,047 (runs that produced the best cut typically ran 8–24 h on an RTX A6000, arXiv:2510.21105)
  are run lengths under different settings and are not comparable with our anneal times; no equal-hardware or equal-time
  comparison was made.
- The solver source code is not part of this release; the claim does not depend on it, because the configuration can be
  verified directly.

## Authorship and use of AI

The experiment was conceived and directed by Filip Majchrzak within the SAPIO MORPHEUS / COMPLEX research project.
The search code, the execution of the experiment, the verification tools and the first drafts of this documentation were
produced by an AI assistant (Claude, by Anthropic) acting as a research operator under his direction. Three of the
independent recounts were written by separate AI-agent instances that had no access to the search code. The solver used
here is a standard population-annealing implementation written for this experiment; no proprietary component of the
SAPIO MORPHEUS / COMPLEX project was required to obtain or to verify the result. Responsibility for the content rests with
the author.
