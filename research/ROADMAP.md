# Research roadmap and decision gates

Last updated 2026-11-23 ET. Primary goal: a substantial theorem about prospective emergence discovery or its fundamental limits, not an inventory of known techniques.

## Active primary target PET-004 — Hyperbolic mixed spectra

Given a real analytic vector field at a hyperbolic equilibrium with both positive and negative real eigenvalues, and nontrivial analytic initialization curve approaching zero, characterize when the local first-exit coefficients and profile are identifiable from finite microscopic information. Explicitly permit curves contained in stable manifolds (no local exit), arbitrary cancellation and coupling. Do not assume convergent Poincare–Dulac normal form in the mixed-sign case. Initially require real diagonalizable spectrum; complex, Jordan, center and stochastic cases deferred.

Priority proof obligations:
1. Separate nonescaping initial conditions on local stable manifold from trajectories which exit. Determine whether exact stable-manifold contact order is finite-jet decidable uniformly; search for counterexamples with arbitrarily high contact.
2. Analyze stable-to-unstable nonlinear seeding using invariant-manifold flattening and variation of constants; derive a candidate law in terms of unstable transverse amplitudes. A curve's distance to stable manifold may be arbitrarily high order, so avoid naively using PET-003's p-based bound. Test whether a known upper contact-order bound restores finite-information prediction.
3. Compare with Dulac map/time, invariant foliation, normal forms, inclination lemma and saddle passage results; identify a precise gap in arbitrary-dimensional mixed spectra before investing in generalization. Treat classical saddle exit estimates as baselines, not breakthroughs.
4. Build explicit counterexamples or a genuinely general theorem with uniform quantifiers; only then add a small reproducible numerical check if it discriminates competing hypotheses. Stop after closing the target or exhausting three distinct blocked routes (see AGENTS.md).

Proposed starting family: x'= -x, y'=lambda*y+c*x^k; x0=epsilon,y0=0. Solve exactly, compare against c=0 and against initialization on stable manifold. This is a planned proof test, not a new verified claim. Investigate the role of transverse order and information bounds before broader global transition models.

## Longer-term queue (not parallel work)

- PET-005: prediction of sequences of local exits/attractor transitions; specify connecting maps and propagate error. Need rigorous composition conditions or impossibility examples.
- PET-006: discover observables/factorizations from microscopic interactions and prove computational savings; account for search, precision and output length. Candidate tools: symmetry, spectral/Koopman methods, representation theory, low-treewidth factorization, information theory. No oracle assumption.
- PET-007: universality across nontrivial systems. Compare graph percolation, coupled oscillators, Ising models, cellular automata, deep linear learning and tiny algorithmic learning systems. Avoid unrelated toy suites until a theorem predicts shared behavior.
- PET-008: blinded prospective discovery in an explicit capability grammar, followed by small-model generalization if analytical foundations justify it. Pre-register grammar, training data, score, continuous diagnostics, novelty test, baseline and held-out cases; separate new mechanism from arbitrary threshold or metric artifact.
- Global goal: classify when macroscopic behavior can be predicted more efficiently than microscopic evolution and when it cannot; only then connect to emergence of intelligence.

## Metrics (proposed, not achievements)

Initial aspirational numerical gates: >=10x measured total-cost reduction vs matched simulation; <=5% held-out transition-location error (state units, threshold, horizon, confidence); >=100x representation compression including metadata; >=3 genuinely different independently tested classes; held-out parameter regimes; prospective capability discovery for advanced stage. These numerical goals are subordinate to proof/novelty and not universal mathematical requirements. Use absolute time error and relative error, scaled residual after each asymptotic term, mode/profile discrepancy, coverage and false positives/negatives. For complexity compare same input, output, accuracy and horizon, count preprocessing and bit complexity. No spending without permission.

## Churn quantification and block template

One focused block has a question, baseline, hypothesis, finite deliverable and decision criteria. Record D = count of substantive distinct deltas (see AGENTS), R = count of repeated tasks with no new dependency, O_closed/O_open = explicit proof obligations closed/open, A_removed = assumptions strictly eliminated, C = new valid counterexamples, V = reproducible checks added, spend and compute. Track rolling last two blocks: if D_total=0 then park/pivot; any R>0 requires explanation. Do not game metrics by subdividing lemmas or repeated runs. No arbitrary numerical quota for theorem significance. Three genuinely distinct blocked routes on the same primary target -> STOP and summarize barrier. Stop if strongest baseline already subsumes proposed result, unless precise new question survives. Immediate stop on invalid core claim; document correction. Stop when result is strong enough for independent proof and novelty audit; no external submission without approval.

Publication gate: exact theorem with independently checkable proof; counterexamples and limitations; comparison with closest results at theorem level; substantial significance (not isolated finite-instance improvements); reproducible evidence if used; independent audit by another reasoning process or specialist; owner approval.
