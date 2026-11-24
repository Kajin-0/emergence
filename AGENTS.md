# AGENTS.md — Predictive Emergence Theory (PET)

Last updated: 2026-11-24T03:13:18Z. Applies repository-wide.

## Mission and constraints

Develop a first-principles mathematical theory that predicts previously unspecified emergent structures/capabilities from microscopic dynamics before they become observable, ideally with provable information/computational savings. AI learning is a motivating application, not an established consequence of existing local ODE results. Seek a foundational result, not incremental publications. No new spending, paid services, frontier-model training, or physical experiments without explicit owner approval. Prioritize analytical proofs, counterexamples and inexpensive reproducible checks. Do not claim a breakthrough, novelty, or verified run without evidence. Repository is public: never commit credentials, private conversation exports, or unrelated personal details.

## Context recovery (mandatory at start of every session)

1. Read this file, README.md, RESEARCH_LOG.md (especially latest checkpoint), research/FOUNDATIONS.md and research/ROADMAP.md. Consult research/REFERENCES.md and existing tests/results before extending work. If files are missing, record the gap rather than reconstructing fictitious evidence.
2. Inspect branch, git status, recent commits, active hypothesis and unresolved proof obligations. Preserve unrelated changes; never force-push or overwrite an existing record. If continuing from a branch, reconcile with main before duplicating work.
3. Resume the single highest-priority unresolved target from the latest log, not the initial brainstorming. Read prior failed routes and counterexamples. Treat the repository as the authoritative project memory, not chat memory.
4. Define a falsifiable question, expected new result, strongest baseline and explicit stop/pivot conditions before starting. Work on the mathematics, not on expanding infrastructure. Check the literature before any novelty claim.
5. At session end update RESEARCH_LOG.md (append timestamped entry and refresh current checkpoint), affected theorem/proof files, and roadmap if changed. Commit coherent changes; record exact commands, inputs, seeds, environment, artifacts, and outcome for numerical work. Verify the commit/ref before claiming persistence. If unable to commit, explicitly report what was not saved.

## Evidence taxonomy

- ESTABLISHED: classical theorem or known result with source.
- DERIVED: proof supplied in repo, internally checked but not independently certified or novel.
- CONJECTURE: precise claim not proved.
- COUNTEREXAMPLE: explicit construction with verified calculation.
- REPRODUCED: executable run with versioned inputs, command and output.
- HISTORICAL_UNVERIFIED: prior conversational numerical claim or source not independently recovered; never treat as reproduced.
- OPEN / BLOCKED / PARKED: unsolved, missing prerequisite, or deprioritized.
- SUPERSEDED: retained for provenance; point to correction.

Proofs must state assumptions, quantifiers, norms, initialization, threshold, local domain and parameter limits; distinguish asymptotic, finite-error and global claims. Audit degeneracy, cancellations, resonances, coordinate invariance, nonmonotone threshold crossings, and worst-case complexity including construction/input/output costs. Never confuse a dynamical mode with a semantic AI capability. Use exact mathematics where possible; numerical evidence cannot establish a theorem.

## Anti-churn policy and stopping conditions

Maintain one active primary theorem target and at most one supporting computational task. A research block must produce at least one substantive delta: new proof lemma closing an explicit obligation; counterexample eliminating a conjecture; strict assumption reduction; improved asymptotic/complexity bound; verified novelty distinction; or a discriminating reproducible experiment. Reformatting, repeating parameter sweeps, rebranding known theory, or rewriting summaries do not count. Do not rerun unchanged passing tests unless required by a changed hypothesis or regression. If two consecutive focused attempts yield zero substantive deltas, park that route, record obstruction and pivot to the best alternative. After three blocked routes on the same primary target, stop and present the precise barrier and next options rather than cycling. Stop a proof route immediately on a valid counterexample to its core claim; salvage only a materially useful restricted version. Stop numerical expansion when it no longer discriminates between hypotheses. Do not create infrastructure absent a specific proof/test dependency.

Track per block: proof obligations closed/open, assumptions removed, theorem scope, counterexamples, known-vs-new distinction, prediction error and asymptotic residual (if applicable), measured versus theoretical computational savings, number of genuinely new deltas, repeat-work count, compute/spend, and decision CONTINUE/PIVOT/PARK/STOP. Targets are not achieved metrics. Publication gate: substantial independently auditable mathematical advance over closest literature; no external submission, public announcement, or priority claim based on preliminary results. User approval required for publication/submission. Public repository is a working record.

## Current handoff

PET-001–003: research/FOUNDATIONS.md; PET-004–012: individual research/PET-0XX.md. PET-008 negative frozen pilot; PET-009–010 restricted observations parked; PET-011 favorable fixed-mask summary compression; PET-012 exact switching continuation, 602 events and 720/720 correct decisions but prototype 1.06x slower and 2.047x logical storage. Primary PET-013: temporal computational predictability from full early state, actual functional forecast or rigorous conditional complexity obstruction, horizon dependence and cost. Read latest RESEARCH_LOG.md and research/ROADMAP.md. Do not retune PET-012 or repeat favorable sweeps. No general AI forecast or verified originality; publication requires audit and approval.
