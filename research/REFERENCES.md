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

## PET-006 literature — 2026-11-24T02:23:18Z

- Notsawo, Dumas, Rabusseau, Grokking Finite-Dimensional Algebra (ICML 2026), https://proceedings.mlr.press/v306/notsawo26a.html — empirical algebra structure and representation alignment.
- Jarvis et al., Compositionality and systematicity emerge from iterated learning in deep linear networks (PNAS 2026), https://doi.org/10.1073/pnas.2509739123 — exact iterated learning dynamics and systematicity.
- Lake & Baroni (2023), Human-like systematic generalization through a meta-learning neural network, https://doi.org/10.1038/s41586-023-06668-3.
- Tzeng (1992), A Polynomial-Time Algorithm for the Equivalence of Probabilistic Automata, https://doi.org/10.1137/0221017 — classical efficient equivalence baseline.
- From Hadamard expressions to weighted rotating automata and back, https://doi.org/10.1016/j.tcs.2018.09.017 — established rational series/Hadamard machinery; use standard tensor representation for pointwise products.
- Exact cover by 3-sets NP-completeness: https://mathworld.wolfram.com/ExactCoverProblem.html; counting baseline Jerrum, Counting, Sampling and Integrating, chapter 2, https://www.math.cmu.edu/~af1p/Teaching/MCC17/Papers/JerrumBook.pdf — verify exact reduction convention for #Exact3Cover.
- Hoeffding binomial concentration and classical conditional-expectation derandomization; see MIT notes https://classes.csail.mit.edu/6.856/current/Notes/n23-derandomizedrounding.html.
- Random matrix moment transfer operator baseline: https://arxiv.org/abs/1907.08512.

Search-level comparison only; closest theorem audit open. No originality established. PET-007: audit Hankel-rank realization and identifiability of learned compositional operators.

## PET-007 literature — 2026-11-24T02:30:08Z

- Sontag, Wang, Megretski, Input Classes for Identifiability of Bilinear Systems (IEEE TAC 2009), https://sontaglab.org/FTPDIR/sontag_wang_megretski_inputs_tac_54_195_207.pdf — established constant-input insufficiency and pulse-class identification for generic bilinear systems. PET-007 is a specific loss-only obstruction with symmetric strongly convex gradients, not a general improvement on this theory.
- Balle et al., Spectral Learning of General Weighted Automata via Constrained Matrix Completion, https://papers.neurips.cc/paper/4697-spectral-learning-of-general-weighted-automata-via-constrained-matrix-completion.pdf — finite Hankel rank/minimal realization baseline.
- Rabusseau, Li, Precup, Connecting Weighted Automata and Recurrent Neural Networks through Spectral Learning, https://proceedings.mlr.press/v89/rabusseau19a.html — recovery of linear 2-RNN from Hankel tensor.
- Arrivault et al., A Toolbox for the Spectral Learning of Weighted Automata, https://proceedings.mlr.press/v57/arrivault16.pdf.
- Learning Group Actions on Latent Representations (NeurIPS 2024), https://proceedings.neurips.cc/paper_files/paper/2024/hash/e63309e532688c722177f81e99f94f32-Abstract-Conference.html.
- Statistical and structural identifiability in representation learning (2026), https://arxiv.org/abs/2603.11970.
- Provable Compositional Generalization for Object-Centric Learning (ICLR 2024), https://brendel-group.github.io/objects-identifiability/ — related structural assumptions; check exact paper before citation.
- Standard Clifford algebra volume and paravector identities; reference lecture notes https://web.math.ku.dk/~jakobsen/gramps/Clif.pdf.

Search-level comparison, not a proof of originality. Next PET-008: strongest mechanistic representation/grokking baselines, pre-registered prospective functional relation prediction.
