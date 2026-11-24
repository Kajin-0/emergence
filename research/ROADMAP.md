# Research roadmap and decision gates

Last updated 2026-11-24T03:09:06Z. Primary goal: a substantial theorem about prospective emergence discovery or its fundamental limits, not an inventory of known techniques.

## Active primary target PET-012 — Event-aware full-state compression

PET-011 demonstrated restricted fixed-mask ReLU compression with sufficient sign gate and unseen-output error certificates; 227.6x state entries, 6.91x end-to-end vs microscopic replay in favorable one-run example. Fixed-mask closure itself known. Next address training mask changes.

1. Audit Wang et al. arXiv:2610.36180 (full theorem if accessible), activation-region tracking, computational geometry range/switch reporting, lazy matrix propagation, and existing sparse event algorithms. No novelty claim from elementary fixed-mask closure.
2. Derive exact or certified approximate continuation when a mask gate fails. Investigate lazy group transforms and hierarchical geometry to identify/split only potential switching neurons, cost in actual switches and visited nodes rather than all N*T. Distinguish failed sufficient gate from actual switches. Retain original states if needed; count all storage, rebuilding and fallback.
3. Prove sufficient conditions for substantive end-to-end gain, or obstruction; include worst cases and precision. Compare with optimized fixed-mask closure and vectorized microscopic replay, same accuracy/output. Avoid claims of speedup based only on arithmetic counts or toy clustering.
4. Only if structural hypothesis survives, freeze one discriminating switching experiment before running; no sweep/repetition of PET-011 or PET-008. No paid compute.
5. Follow AGENTS stopping/pivot rules; if classical literature subsumes result or no meaningful gain survives, park route. Publication requires independent proof/novelty audit and approval.

## Longer-term queue (not parallel work)

- Future: universality across nontrivial systems only after a theorem predicts common mechanisms; avoid unrelated toy suites.
- Global goal: classify when macroscopic behavior can be predicted more efficiently than microscopic evolution and when it cannot; only then connect to emergence of intelligence.

## Metrics (proposed, not achievements)

Initial aspirational numerical gates: >=10x measured total-cost reduction vs matched simulation; <=5% held-out transition-location error (state units, threshold, horizon, confidence); >=100x representation compression including metadata; >=3 genuinely different independently tested classes; held-out parameter regimes; prospective capability discovery for advanced stage. These numerical goals are subordinate to proof/novelty and not universal mathematical requirements. Use absolute time error and relative error, scaled residual after each asymptotic term, mode/profile discrepancy, coverage and false positives/negatives. For complexity compare same input, output, accuracy and horizon, count preprocessing and bit complexity. No spending without permission.

## Churn quantification and block template

One focused block has a question, baseline, hypothesis, finite deliverable and decision criteria. Record D = count of substantive distinct deltas (see AGENTS), R = count of repeated tasks with no new dependency, O_closed/O_open = explicit proof obligations closed/open, A_removed = assumptions strictly eliminated, C = new valid counterexamples, V = reproducible checks added, spend and compute. Track rolling last two blocks: if D_total=0 then park/pivot; any R>0 requires explanation. Do not game metrics by subdividing lemmas or repeated runs. No arbitrary numerical quota for theorem significance. Three genuinely distinct blocked routes on the same primary target -> STOP and summarize barrier. Stop if strongest baseline already subsumes proposed result, unless precise new question survives. Immediate stop on invalid core claim; document correction. Stop when result is strong enough for independent proof and novelty audit; no external submission without approval.

Publication gate: exact theorem with independently checkable proof; counterexamples and limitations; comparison with closest results at theorem level; substantial significance (not isolated finite-instance improvements); reproducible evidence if used; independent audit by another reasoning process or specialist; owner approval.
