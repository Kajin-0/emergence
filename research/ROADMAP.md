# Research roadmap and decision gates

Last updated 2026-11-24T02:30:08Z. Primary goal: a substantial theorem about prospective emergence discovery or its fundamental limits, not an inventory of known techniques.

## Active primary target PET-008 — Prospective discovery of learned functional relations

PET-007 found a loss-only information obstruction even with arbitrary curricula, plus a sharp ordered-readout diagnostic in a constructed Clifford family. This is not yet inference from full microscopic learning dynamics. Park generic realization and constructed-obstruction refinements unless a specific dependency arises.

1. Choose ONE small algebraic learner whose internal representation is not imposed (e.g. an ordinary trainable modular arithmetic network with held-out structured input families). Define observable functional relations, finite admissible relation grammar, novelty relative to training constraints, target performance, and prediction horizon. Distinguish untrained task families from mere held-out random examples and prevent access to future labels/checkpoints during prediction.
2. Audit Nanda et al. mechanistic grokking progress measures, Fourier/circuit analyses, algebra grokking, learned group actions, structural identifiability and compositional generalization. Seek a precise improvement over known representation diagnostics, not another renaming of them.
3. Formulate an early internal representation certificate predicting which relations become functional at a future checkpoint, or a rigorous barrier. Measure false positives, recall, coverage, lead time, matched compute, and calibration; compare loss-only, early direct output, standard spectral/representation diagnostics, and simple trajectory extrapolation. Freeze prediction rules and held-out evaluations before running a discriminating experiment.
4. No broad sweeps, paid compute, or frontier training. Start with analytical argument; only run the minimal experiment that tests the hypothesis. If a known baseline subsumes the claim, record and pivot. Follow AGENTS.md stopping rules.
5. Seek a substantial structural result (general theorem or genuinely strong predictive separation), not a publication based on a toy benchmark. Keep semantic claims bounded by operational task grammar.

## Longer-term queue (not parallel work)

- Future: universality across nontrivial systems only after a theorem predicts common mechanisms; avoid unrelated toy suites.
- Global goal: classify when macroscopic behavior can be predicted more efficiently than microscopic evolution and when it cannot; only then connect to emergence of intelligence.

## Metrics (proposed, not achievements)

Initial aspirational numerical gates: >=10x measured total-cost reduction vs matched simulation; <=5% held-out transition-location error (state units, threshold, horizon, confidence); >=100x representation compression including metadata; >=3 genuinely different independently tested classes; held-out parameter regimes; prospective capability discovery for advanced stage. These numerical goals are subordinate to proof/novelty and not universal mathematical requirements. Use absolute time error and relative error, scaled residual after each asymptotic term, mode/profile discrepancy, coverage and false positives/negatives. For complexity compare same input, output, accuracy and horizon, count preprocessing and bit complexity. No spending without permission.

## Churn quantification and block template

One focused block has a question, baseline, hypothesis, finite deliverable and decision criteria. Record D = count of substantive distinct deltas (see AGENTS), R = count of repeated tasks with no new dependency, O_closed/O_open = explicit proof obligations closed/open, A_removed = assumptions strictly eliminated, C = new valid counterexamples, V = reproducible checks added, spend and compute. Track rolling last two blocks: if D_total=0 then park/pivot; any R>0 requires explanation. Do not game metrics by subdividing lemmas or repeated runs. No arbitrary numerical quota for theorem significance. Three genuinely distinct blocked routes on the same primary target -> STOP and summarize barrier. Stop if strongest baseline already subsumes proposed result, unless precise new question survives. Immediate stop on invalid core claim; document correction. Stop when result is strong enough for independent proof and novelty audit; no external submission without approval.

Publication gate: exact theorem with independently checkable proof; counterexamples and limitations; comparison with closest results at theorem level; substantial significance (not isolated finite-instance improvements); reproducible evidence if used; independent audit by another reasoning process or specialist; owner approval.
