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

## PET-008 literature — 2026-11-24T02:41:09Z

- Nanda et al., Progress Measures for Grokking via Mechanistic Interpretability, https://arxiv.org/abs/2301.05217 — established restricted/excluded logit progress measures, Fourier circuit formation precedes generalization.
- https://arxiv.org/abs/2606.12966 — Fourier synchronization precursor; revisions include controlled comparisons with memorization and task basis. Check current title/authors before citing specific results. Early lead alone does not establish a new predictor.
- https://arxiv.org/abs/2607.04333 — representational priors and grokking delay, related causal interventions.
- https://arxiv.org/abs/2611.19477 — learning rule influences circuit size; related optimizer dependence.

Pilot restricted comparator is task-symmetry averaging, not exact Nanda frequency filtering. PET-009 audit NTK, linearized training, drift bounds and functional margin forecasts before novelty claims.

## PET-009 literature — 2026-11-24T02:55:39Z

- Jacot, Gabriel, Hongler (2018), Neural Tangent Kernel: Convergence and Generalization in Neural Networks, https://arxiv.org/abs/1806.07572.
- Huang & Yau (2020), Dynamics of Deep Neural Networks and Neural Tangent Hierarchy, https://proceedings.mlr.press/v119/huang20l.html — finite-width derivative hierarchy.
- Guillen, Misof, Gerken (2026), Finite-Width Neural Tangent Kernels from Feynman Diagrams, https://proceedings.mlr.press/v306/guillen26a.html.
- Wang et al. (2026 preprint), Dynamical coarse-graining of neural-network training, https://arxiv.org/abs/2610.36180 — closest general closure/coarse-graining program, theorem-level comparison mandatory.
- On the learning dynamics of two-layer quadratic neural networks for understanding deep learning, https://doi.org/10.1007/s11704-020-0298-0 — coupled quadratic network training ODEs.
- Learning quadratic neural networks in high dimensions: SGD dynamics and scaling laws, https://papers.nips.cc/paper_files/paper/2025/hash/d7ce06e9293c3d8e6cb3f80b4157f875-Abstract-Conference.html.
- Prony's method on the sphere, https://doi.org/10.5802/smai-jcm.53 — classical finite moment reconstruction and Vandermonde structure.
- Batenkov & Yomdin, On the Accuracy of Solving Confluent Prony Systems, https://doi.org/10.1137/110836584 — precision/conditioning baseline.

Search-level comparison only. No established originality. PET-010 must review noisy finite moment recovery, accessible observations and dynamical approximation costs before any novelty assertion.

## PET-010 literature — 2026-11-24T03:03:00Z

- Demanet & Townsend, Stable extrapolation of analytic functions, https://arxiv.org/abs/1605.09601 — noisy samples and fractional-power extrapolation stability.
- Trefethen, Quantifying the ill-conditioning of analytic continuation, https://doi.org/10.1007/s10543-020-00802-7 — quantitative continuation instability.
- Foucart, Instances of computational optimal recovery: Refined approximability models, https://doi.org/10.1016/j.jco.2020.101503 — optimal linear recovery with bounded noise and dual norm penalties. PET-010B is a special finite-dimensional application, not a new minimax theorem.
- Numerical analytic continuation, https://doi.org/10.1007/s13160-023-00599-2 — analytic continuation limitations and algorithms.

Search-level comparison, no verified originality. Next audit full-state multi-example dynamical coarse-graining and feature learning at theorem level.

## PET-011 literature — 2026-11-24T03:09:06Z

- Lin-Juan Wang et al., Dynamical coarse-graining of neural-network training, https://arxiv.org/abs/2610.36180 (26 Oct 2026 preprint): abstract and indexed description identify exact closure for fixed activation patterns (five moments in their ReLU example). Full HTML unavailable in this session; do not claim theorem-level novelty comparison. PET-011 treats fixed-mask moment closure as known; compare proposed sign gate and mixed query bounds with full theorem when accessible.
- Scaling Up Exact Neural Network Compression by ReLU Stability (NeurIPS 2021), https://proceedings.neurips.cc/paper/2021/hash/e35d7a5768c4b85b4780384d55dc3620-Abstract.html — static stable ReLU compression, relevant baseline for certification.
- Studying the Evolution of Neural Activation Patterns During Training of Feed-Forward ReLU Networks, https://pmc.ncbi.nlm.nih.gov/articles/PMC8733739/ — activation change measurements, no assumption of perpetual stability.
- Ergen & Pilanci, Global Optimality Beyond Two Layers: Training Deep ReLU Networks via Convex Programs, https://proceedings.mlr.press/v139/ergen21a.html — hyperplane arrangement methods.
- Glasgow, Wu & Bruna, Mean-field analysis of polynomial-width two-layer neural network beyond finite time horizon, https://proceedings.mlr.press/v291/glasgow25a.html — long-time particle approximation baseline.
- Martin, Biroli & Bach, High-Dimensional Analysis of Gradient Flow for Extensive-Width Quadratic Neural Networks, https://www.jmlr.org/papers/v27/26-0672.html — multi-example feature dynamics in a different regime.

Search-level comparison only. No verified originality. Next audit switching/geometry methods and exact closure theorem at full-text level.

## PET-012 literature — 2026-11-24T03:13:18Z

- Wang et al., https://arxiv.org/abs/2610.36180 — fixed-pattern moment closure; indexed abstract confirms overlap, full novelty comparison incomplete.
- Matoušek (1992), Reporting points in halfspaces, https://www.sciencedirect.com/science/article/pii/092577219290006E.
- Afshani & Chan (2009), Optimal Halfspace Range Reporting in Three Dimensions, https://epubs.siam.org/doi/abs/10.1137/1.9781611973068.21 — linear space, O(log n+k) query; check preprocessing guarantee for combined bound.
- Random Sampling, Halfspace Range Reporting, and Construction of (<=k)-Levels in Three Dimensions, https://epubs.siam.org/doi/10.1137/S0097539798349188 — O(n log n) expected preprocessing and expected O(log n+k) query.
- Chan (2012), Optimal Partition Trees, https://doi.org/10.1007/s00454-012-9410-z.
- A dynamic bounding volume hierarchy for generalized collision detection, https://www.sciencedirect.com/science/article/abs/pii/S0097849306000689.

Search-level comparison, no originality claim. Prototype does not implement optimal halfspace structures. Next audit temporal iteration/fast-forwarding and learning complexity.
