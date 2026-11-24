# Research log — Predictive Emergence Theory

Living authoritative record. UTC timestamps for new entries; historical sessions dated to available local date only. Append new records, never silently replace past claims; corrections link to superseded entries. Refresh the checkpoint after every substantive research block. For proof details read research/FOUNDATIONS.md.

## Current checkpoint — 2026-11-24T02:14:10Z

- **Active target:** PET-005, composability of emergence certificates across multiple dynamical regimes.
- **Next action:** formulate two-saddle transition maps with vanishing entry curves and error propagation; derive a global obstruction from identical local data and a sufficient composition criterion. Compare heteroclinic/Dulac transition theory before novelty claims.
- **Baseline:** PET-001–003 in foundations; PET-004 finite-flow-jet mixed-spectrum theorem and impossibility in research/PET-004.md. Derived internally, not independently certified.
- **Verified experiment:** 4 earlier deterministic cascade roots; no new numerical runs in PET-004. Historical 240-network sweep unverified.
- **Publication status:** NO-GO, no independently established foundational contribution.
- **Constraints:** $0 new spend; one primary target; theory first; avoid churn.
- **Decision:** CONTINUE to PET-005; local mixed-spectrum leading-time target closed internally; independent audit remains; no redundant numerical sweep.
- **Unresolved:** theorem-level novelty, exact finite-precision robustness, full physical exit profile for mixed spectra, global composition, semantic capability discovery.

## Historical archive — 2026-11-23 ET

### PET-000 — Initial program
Motivation: predict emergence of AI and other complex systems before observed, with first-principles mathematical characterization. Four hypotheses: latent precursors, predictive compression, universality, prospective discovery. Distinguish known-capability forecasts from discovery and impossibility; beware measurement artifacts, chaos, undecidability and computational irreducibility. Candidate tools: statistical mechanics, graph theory, dynamical systems, information theory, renormalization. Decision: narrow to unknown-capability discovery.

### PET-001 — Forecast/discovery separation
Derived simple gradient-descent/Max-3SAT constant-gap hardness reduction, bounded-treewidth search route and robust score certification. Weakness: hardness constructed in score function; standard complexity and optimization machinery. Uniform-at-T estimate does not exclude earlier threshold crossings without monotonicity (corrected in foundations). Decision: move toward automatic generation of latent observables, not another combinatorial toy example.

### PET-002 — Positive nonlinear networks
Derived minimum seed-tree generation exponent and first-exit law L/r* + O(log L), arbitrary finite feedback, nonnegative rates and positive nonlinear coefficients. Demonstrated sharp log correction, first-coordinate identity counterexample and signed-cancellation obstruction. Historical numerical sweep: 80 networks x 3 scales = 240 claimed trajectories; no code/seeds/logs recovered, status HISTORICAL_UNVERIFIED. Exact values preserved in foundations. Decision: signed nonlinear dynamics and symmetry/cancellation.

### PET-003 — Resonance-resolved analytic sources
Derived two-scale exit law aL-b log L+O(1) using convergent Poincare–Dulac normal form with positive real diagonalizable spectrum; limiting physical profile and constant under transverse crossing; finite-jet sufficiency with spectral ratio kappa; hidden high-order interaction counterexamples. Exact resonant cascade demonstrates initially absent negative z mode dominates. Four high-precision roots reported. Known classical machinery; novelty not established. Decision: mixed spectra rather than more fully unstable examples.

## 2026-11-24 UTC — Repository bootstrap and evidence audit

Initial AGENTS.md commit timestamp 2026-11-24T01:54:40Z. Consolidated historical proofs and examples, source URLs, and primary target in the same repository. Reproduced four cascade roots independently at 70-digit precision using Python decimal; numerical table matches history. Archived unsupported sweep claims separately; fixed nonmonotone horizon certification, clarified finite-jet wording, nontrivial analytic initialization, local/transverse exit conditions and complexity caveats. No new theorem or originality claim in this documentation block. New substantive research deltas: 0 (governance/recovery work explicitly not counted); repeated experimental work: 1 targeted audit needed because earlier raw artifacts missing; new reproduced examples: 4 roots; new spending: $0. No two-block stagnation rule triggered by this administrative bootstrap. Decision: CONTINUE to PET-004.

## Entry template (append for future research)

- Timestamp (UTC), block ID, branch/commit, primary target
- Falsifiable question, closest literature/baseline and exact expected delta
- Assumptions, statement/proof or counterexample; affected result IDs
- Evidence status, independently checked vs unverified, artifact paths and reproduction commands
- Metrics: D, R, obligations closed/open, assumptions removed, counterexamples, V, compute/spend; quantitative accuracy/complexity if relevant
- Negative results, blockers, superseded claims, novelty overlap and limitations
- Stop criteria evaluated; decision CONTINUE/PIVOT/PARK/STOP and rationale
- Next single action; update checkpoint and roadmap as needed

## 2026-11-24T02:14:10Z — PET-004: mixed-spectrum finite-information prediction

Parent: f26845a34d6da79dbc175a90509676c84f24dfae. Question: can a fixed or adaptive finite jet determine first emergence in real-diagonalizable hyperbolic mixed spectra? Derived PET-004A impossibility (arbitrarily high stable-manifold contact, identical finite jets with different exit existence/timing); PET-004B adaptive finite-flow-jet two-scale exit law via exponential-polynomial recursion and uniform residual bound; PET-004C contact-dependent sufficiency and one-sided termination certificate. Exact symbolic checks: stable seeding, cancellation, resonant cascade with independent stable mode. No new numerical runs. Removed all-positive-spectrum and convergent-normal-form assumptions from leading-time result, with finite contact needed for guaranteed certificate. Full proof and limits: research/PET-004.md. Preliminary literature check: planar Dulac map/time, higher-dimensional saddle passage, unstable exit. Exact novelty comparison and independent audit open. D=2 substantive deltas (impossibility and constructive theorem including corollary); R=0; primary obligations internally closed: obstruction and leading-time construction; exact profile and novelty open; A=1 combined spectral restriction removed; C=1 counterexample family; V=0 new numerical checks; spend=$0. No churn triggers. Decision CONTINUE to PET-005 rather than further local refinements. Next: rigorous multi-transition composition and global indistinguishability obstruction. Publication NO-GO.
