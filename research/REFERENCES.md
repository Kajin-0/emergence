# Literature baseline and novelty audit

Checked source landing pages during repository initialization, 2026-11-23 ET. This is not a systematic review; read full relevant theorems before asserting originality. Links are durable external identifiers, not chat citation IDs.

| Source | Relevance / novelty boundary |
|---|---|
| Israeli & Goldenfeld (2004), Computational Irreducibility and the Predictability of Complex Physical Systems, https://doi.org/10.1103/PhysRevLett.92.074105 | Coarse-graining can make macroscopic behavior predictable despite complex microscopic evolution. PET must go beyond generic coarse-graining. |
| Israeli & Goldenfeld (2006), Coarse-graining of cellular automata, emergence, and the predictability of complex systems, https://doi.org/10.1103/PhysRevE.73.026203 | Extended coarse-graining baseline. |
| Shalizi & Crutchfield (2001), Computational Mechanics: Pattern and Prediction, Structure and Simplicity, https://www.its.caltech.edu/~theory/compmech.pdf | Predictive causal states, optimality and uniqueness. |
| Saxe, McClelland & Ganguli (2013 preprint / ICLR 2014), https://arxiv.org/abs/1312.6120 | Exact learning dynamics in deep linear networks; sequential transitions. |
| Nanda et al. (2023), Progress measures for grokking via mechanistic interpretability, https://arxiv.org/abs/2301.05217 | Mechanistic progress indicators before observable generalization. |
| Schaeffer, Miranda & Koyejo (2023), Are Emergent Abilities of Large Language Models a Mirage?, https://arxiv.org/abs/2304.15004 | Metric-dependent discontinuities; distinguish true dynamical transitions from threshold artifacts. |
| Snell et al. (2024), Predicting Emergent Capabilities by Finetuning, https://arxiv.org/abs/2411.16035 | Forecasts specified tasks; in some cases predictions reach models trained with up to 4x compute. Not general unknown-capability discovery. |
| Håstad (2001), Some Optimal Inapproximability Results, https://doi.org/10.1145/502090.502098 | Gap hardness used in PET-001A. |
| Encyclopedia of Mathematics, Poincare–Dulac theorem, https://encyclopediaofmath.org/wiki/Poincar%C3%A9%E2%80%93Dulac_theorem | Established convergent polynomial normal form in the Poincare domain; central baseline for PET-003. |
| Encyclopedia of Mathematics, Local normal forms for dynamical systems, https://encyclopediaofmath.org/wiki/Local_normal_forms_for_dynamical_systems | Formal vs analytic normal forms; mixed-spectrum obstacle. |
| Marín & Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: Coefficient properties, https://arxiv.org/abs/2105.09785 | Critical baseline for PET-004; planar saddle passages, asymptotic coefficients. |

Additional literature leads (not fully audited): max-sum/tree-decomposition algorithms for weighted constraint optimization; tropical/hypergraph shortest derivations; Koopman observables; spectral/modal participation; saddle-to-saddle learning dynamics; stable/unstable invariant foliations and high-dimensional saddle passage; capability elicitation. Earlier conversation referenced 2026 stochastic emergence and skill-order studies without durable bibliographic identifiers; do not cite their numerical claims until independently identified and checked.

For every candidate result, log exact closest theorem, overlap, assumption difference, result difference, and whether novelty is established. Known theorem + new terminology is not novelty.

## PET-004 preliminary search — 2026-11-24 UTC

- Marín & Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: General setting, https://www.sciencedirect.com/science/article/pii/S0022039620306021 — planar transverse-section maps and time.
- Local setting, https://www.sciencedirect.com/science/article/pii/S0022039620303387 — resonant planar saddle passage.
- Asymptotic properties of the Dulac map near a hyperbolic saddle in dimension three, https://afst.centre-mersenne.org/item/AFST_2001_6_10_4_595_0/ — higher-dimensional baseline.
- Scaling limit for escapes from unstable equilibria in the vanishing noise limit: nontrivial Jordan block case, https://arxiv.org/abs/1708.00558 — stochastic exit timing and normal forms; distinct from deterministic analytic-curve setting.

Search-level comparison only. Read theorem statements and proofs before claiming PET-004 novelty. Investigate existing flow-jet asymptotics and arbitrary-dimensional saddle passage specifically.

## PET-005 literature audit — 2026-11-24T02:18:12Z

- Robust Heteroclinic Cycles in Pluridimensions, https://doi.org/10.1007/s00332-025-10175-2 — log-coordinate transition matrix products are established.
- Switching in Heteroclinic Networks, https://doi.org/10.1137/15M1042176 — global transition map form controls switching.
- Podvigina et al., Stability of a heteroclinic network and its cycles, https://arxiv.org/abs/1712.04270 — eigenvalues/transition matrices insufficient without geometric return-map analysis.
- Linearization of complex hyperbolic Dulac germs, https://www.sciencedirect.com/science/article/pii/S0022247X21009124 — power-log germs and return maps.

PET-006 initial reading: Notsawo et al. (2026), Grokking Finite-Dimensional Algebra, https://proceedings.mlr.press/v306/notsawo26a.html; Compositionality and systematicity emerge from iterated learning in deep linear networks, https://pmc.ncbi.nlm.nih.gov/articles/PMC13168545/; A mathematical theory for understanding when abstract representations emerge in neural networks, https://pmc.ncbi.nlm.nih.gov/articles/PMC13014162/; Brunton et al., Koopman Invariant Subspaces and Finite Linear Representations of Nonlinear Dynamical Systems for Control, https://pmc.ncbi.nlm.nih.gov/articles/PMC4769143/. Search-level findings; exact theorem comparison required.
