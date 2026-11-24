# Mathematical foundations and result register

Archived 2026-11-23 ET. Reconstructed from investigations PET-001–003; equations and proofs below are the working canonical versions, not peer-reviewed claims of novelty. All logarithms natural. Infinite orders refer to identically zero analytic functions. An actual dynamical exit is not automatically a semantic capability. See REFERENCES.md for established baselines.

## PET-000 — Program formulation (CONJECTURE)

For a microscopic map \(x_{t+1}=F_\lambda(x_t)\), seek a reduced representation \(q=\Phi(x)\) and reduced map \(G_\lambda\) such that \(\Phi F_\lambda\approx G_\lambda\Phi\), with predictive error and total construction/evaluation cost controlled. Distinguish prediction of a specified capability, discovery within a predefined compositional grammar, and discovery of genuinely new classes (which requires an operationally defined admissible representation space). Four original hypotheses: latent precursors; asymptotic predictive compression; universality classes; prospective capability discovery. A meaningful speedup compares identical output/precision/horizon, including preprocessing, input representation, search and output costs. Target asymptotic ratio \(C_{\rm pred}(N,T,\delta)/C_{\rm sim}(N,T,\delta)\to0\) in a specified scaling regime. No universal claim is justified. Classical symmetry-breaking example: \(\dot q=\mu q-q^3\) has stable \(q=0\) for \(\mu<0\), and stable \(q=\pm\sqrt\mu\) for \(\mu>0\); known bifurcation theory, not new.

## PET-001 — Forecasting versus discovery

### Definitions
Finite capability space \(\mathcal A\), score \(S(x,a)\in[0,1]\), threshold \(\theta\), emergence time \(\tau(a)=\inf\{t:S(x_t,a)\ge\theta\}\). Forecast: specified \(a\); discovery: find unspecified \(a\) with \(\tau(a)\le T\); completeness: enumerate all such \(a\). If \(\mathcal A=\{0,1\}^n\), size \(2^n\).

### PET-001A: constant-gap hardness (DERIVED; elementary reduction)
Loss \(L(w)=\tfrac12\sum_{i=1}^m(w_i-1)^2\), Hessian identity, gradient descent from zero, step \(\eta=1/2\), so \(w_i(t)=1-2^{-t}\). For a 3-CNF formula with clause indicators \(c_i(a)\), set \(S_t(a)=(1-2^{-t})m^{-1}\sum_i c_i(a)\). Specified assignment evaluation is \(O(m)\) clause operations; discovery by time \(T=6\) is NP-hard by the known gap-Max-E3SAT result (distinguish satisfiable from optimum at most 15/16). At threshold 31/32, YES maximum is 63/64 and NO maximum is at most 15/16 (even tighter: 945/1024). YES gap 1/64; NO gap at least 1/32. Scores are monotone in time. The hardness is in the deliberately encoded capability space, not in training dynamics. No claim about typical neural networks or originality.

### PET-001B: factorized search (ESTABLISHED machinery; proposed application)
For \(S_T(a)=\sum_j f_{j,T}(a_{C_j})\), binary variables and supplied tree decomposition of primal graph width \(k\), max-sum dynamic programming takes \(\operatorname{poly}(n,m)2^{k+1}\) arithmetic operations, assuming accessible factor tables and decomposition. Enumeration takes \(O(m2^n)\) for bounded-size clauses. Construction, precision and exponential output enumeration costs must be counted. High treewidth alone does not imply hardness on every instance. Automatic recovery of useful factors remains OPEN.

### PET-001C: robust certification (DERIVED; elementary)
If \(\sup_a|S_T(a)-\widehat S_T(a)|\le\delta\), then \(|\max_a S_T(a)-\max_a\widehat S_T(a)|\le\delta\) by applying the pointwise inequalities and maximizing. Predicted maximum below \(\theta-\delta\) certifies no threshold at T; at least \(\theta+\delta\) certifies a threshold by T for initially subthreshold capabilities. Correction: no threshold at T does NOT imply no earlier crossing without monotonicity or a uniform-in-time bound. For arbitrary trajectories apply the argument to \(\sup_{0\le t\le T,a} S_t(a)\). Approximate argmax has regret at most \(2\delta\) if prediction is uniformly accurate. Main obstacle is cheaply constructing the uniform approximation, not the inequality.

## PET-002 — Positive polynomial network first exit

### PET-002A (DERIVED; novelty unverified)
Fixed finite system
\[
\dot x_i=\lambda_i x_i+\sum_{\alpha\in M_i}c_{i,\alpha} x^\alpha,\quad
\lambda_i\ge0,\ c_{i,\alpha}>0,\quad |\alpha|\ge2.
\]
Initial \(x_i(0)=\epsilon^{w_i}\), \(0<w_i\le\infty\); infinite weight means zero. Fixed coefficients and threshold \(\rho>0\); \(\epsilon\downarrow0\). Exit \(\tau_\rho=\inf\{t:\max_i x_i(t)\ge\rho\}\). Allow arbitrary feedback. Restrict to reachable indices (finite derivations from seeds). Let \(b_i\) be minimum total seed-leaf weight of a finite generation tree with root i. Then
\[
b_i=\min(w_i,\min_{\alpha\in M_i}\sum_j\alpha_j b_j).
\]
Use min-plus relaxation initialized by w; unreachable coordinates remain zero. If \(r_*=\max_{i:b_i<\infty}\lambda_i/b_i>0\), and \(L=\ln(1/\epsilon)\), then
\[
\tau_\rho=L/r_*+O(\ln L).
\]
The coefficient is computable in \(O(NM)\) arithmetic operations for bounded-degree monomials, N nodes and M monomials, excluding bit complexity. General monomial representation cost replaces M by total input incidence size. This is a leading-order shortcut, not a measured complexity separation.

**Proof.** Minimum-cost generation trees need not repeat an index along a branch: replacing a repeated ancestor subtree by its descendant removes positive-cost side branches. Thus height at most N, and N rounds of relaxation suffice. For fixed small \(t_0>0\) (existence uniformly for sufficiently small epsilon), variation of constants and positivity applied along a minimal tree give \(x_i(t_0)\ge C_i\epsilon^{b_i}\) for each reachable mode; if exit occurred earlier the upper bound is already true. Since \(\dot x_i\ge\lambda_i x_i\), the maximizing mode yields \(\tau_\rho\le L/r_*+O(1)\). For a lower bound use
\[
q=\epsilon e^{(r_*+1/L)t},\qquad z_i=L^{p_i}q^{b_i}.
\]
For each reachable monomial let \(\Delta=\sum_j\alpha_jb_j-b_i\ge0\). Equality dependencies have strictly smaller input weights because all finite weights are positive and degree at least two; hence acyclic. Choose fixed nonnegative \(p_i\) with \(p_i\ge2+\sum_j\alpha_jp_j\) on equality dependencies. The nonlinear/linear-scale ratio is \(x^\alpha/z_i\) evaluated at z, namely \(L^{\sum\alpha_jp_j-p_i}q^\Delta\). It is at most \(L^{-2}\) for equality terms; choose fixed K large enough for the same bound on all strict terms when \(q\le L^{-K}\). Also choose \(Kb_i>p_i\). Then \(\dot z_i/z_i=b_i(r_*+1/L)\ge\lambda_i+b_i/L\) dominates the finite nonlinear sum for large L. Initial z dominates x. Cooperative comparison on the nonnegative orthant yields \(x_i\le z_i\) until \(t_-=(L-K\ln L)/(r_*+1/L)\), with all z below rho there and throughout earlier times. This gives the required lower bound. No assertion if all reachable amplification rates are zero.

### PET-002B: examples and limitations (COUNTEREXAMPLES)
- \(\dot x=x,\dot y=4y+x^2\), initial \((\epsilon,0)\): \(x=\epsilon e^t\), \(y=(\epsilon^2/2)(e^{4t}-e^{2t})\); unit threshold \(t_x=L\), \(t_y=L/2+\ln2/4+o(1)\). Initially absent mode determines earlier leading timescale.
- \(\dot x=x,\dot y=2y+x^2\): \(y=t\epsilon^2e^{2t}\); threshold 1 gives \(t_y=L-\tfrac12\ln L+o(1)\). Logarithmic correction sharp; cannot uniformly replace error by O(1).
- \(\dot x=x,\dot y=100x^2\), initial \((\epsilon,0)\): \(y=50\epsilon^2(e^{2t}-1)\) crosses 1 first even though its intrinsic rate is zero. Ratio maximizer determines leading time, not threshold-crossing coordinate.
- Signed cancellation: \(\dot y=4y+x_1^2-x_2^2\) with identical x trajectories and \(y(0)=0\) yields no y. Positive derivation algebra cannot resolve destructive interference.

### PET-002C historical numerical record (HISTORICAL_UNVERIFIED)
Earlier conversational report described 80 six-mode networks, 11 quadratic interactions each, four initially absent modes, feedback allowed, 40 random and 40 absent-dominant networks, 3 epsilon values each (240 trajectories). Raw generators, seeds, code, tolerance, threshold and raw logs were not retained; do not count as verified.

| L | Absent-dominant median relative error | Absent-dominant max error | Random max error | Random first-coordinate matches |
|---:|---:|---:|---:|---:|
|10|9.1024%|20.739%|9.958%|37/40|
|20|4.5512%|10.370%|4.982%|37/40|
|40|2.2756%|5.185%|2.526%|37/40|

Archive only. Do not spend effort reconstructing this sweep unless required to discriminate a new theorem.

## PET-003 — Signed analytic source, resonance-resolved prediction

### Motivation (COUNTEREXAMPLE to naive algebra)
For \(\dot x=x,\dot y=4y+x^2\) with \(y(0)=-\epsilon^2/2\), \(y(t)=-(\epsilon^2/2)e^{2t}\); fast term cancels. The exact coordinate \(z=y+x^2/2\) obeys \(\dot z=4z\), invariant cancellation manifold z=0. Nonlinear coordinates capture latent amplitudes.

### PET-003A: two-scale exit law (DERIVED; classical machinery)
Consider \(\dot x=Ax+f(x)\), real analytic near zero, \(f=O(\|x\|^2)\), A diagonalizable over R with all eigenvalues \(0<\lambda_1\le\cdots\le\lambda_N\). Let \(x(0)=\gamma(\epsilon)\) be non-identically-zero real analytic curve with \(\gamma(0)=0\), epsilon positive. Fixed sufficiently small exit radius \(\rho>0\) in a fixed norm, inside the conjugacy neighborhood. All asymptotics for fixed system and curve. Poincare–Dulac (established) yields convergent local analytic \(x=H(u)\) reducing dynamics to
\[
\dot u_i=\lambda_i u_i+R_i(u),\qquad
R_i=\sum_{\alpha:\alpha\cdot\lambda=\lambda_i,\ |\alpha|\ge2}r_{i,\alpha}u^\alpha.
\]
Finite resonances; each nonlinear input has lower eigenvalue. Put \(v_i=e^{-\lambda_it}u_i\). Then \(\dot v_i=R_i(v)\), a triangular polynomial system. Recursively integrating gives
\[
u_i=e^{\lambda_it}\sum_{d=0}^{D_i}c_{i,d}(\epsilon)t^d
\]
with analytic coefficients polynomial in the initial u coordinates. Define \(\nu_{i,d}=\operatorname{ord}c_{i,d}\), \(\nu_i=\min_d\nu_{i,d}\), and \(d_i=\max\{d:\nu_{i,d}=\nu_i\}\) for nonzero coordinates only. Write \(C_i\ne0\) for the leading coefficient of \(c_{i,d_i}\). Set
\[
a_*=\min_i\nu_i/\lambda_i,\qquad b_*=\max_{i:\nu_i/\lambda_i=a_*}d_i/\lambda_i.
\]
Then
\[
\tau_\rho=a_* L-b_*\ln L+O(1).
\]
Define \(E_*=\{i:\nu_i/\lambda_i=a_*, d_i/\lambda_i=b_*\}\). At \(t=a_*L-b_*\ln L+s\) and bounded s, the normal-form solution converges uniformly on compact s intervals to \(U_i(s)=C_i a_*^{d_i}e^{\lambda_i s}\) for \(i\in E_*\), zero otherwise. Physical profile is \(H(U(s))\) while in local domain. Coordinate support depends on normalization; physical profile and divergent exit coefficients are invariant for fixed physical problem.

**Proof detail.** In each exponential polynomial, terms with larger epsilon order are exponentially smaller at t proportional to L; among equal orders the largest d dominates. Substitution of shifted time gives \(C_i a_*^{d_i} e^{(\lambda_i a_*-\nu_i)L} L^{d_i-\lambda_i b_*}e^{\lambda_i s}\). Only E survives. For early times \(0\le t\le a_*L-b_*\ln L-S\), bound each term using the increasing envelope \(|c_{i,d}|t^d e^{\lambda_i t}\); at the upper endpoint the envelope tends to a constant times \(e^{-\lambda_i S}\) for selected terms and zero otherwise. Thus no earlier exit for sufficiently large fixed S. At some bounded later shift the selected profile exceeds a sufficiently small exit radius, staying in the local conjugacy domain up to first exit. Local norm equivalence and continuity give bounded time displacement. If the limiting profile has a unique first crossing at \(s_\rho\), with strict subthreshold earlier and transverse outward crossing, uniform convergence gives
\[
\tau_\rho=a_*L-b_*\ln L+s_\rho+o(1),\qquad \|H(U(s_\rho))\|=\rho.
\]
These are local source results, not statements about mixed spectra, discrete SGD, global attractors, stochastic training or semantic ability.

### PET-003B: finite-jet prediction (DERIVED; sharpness family)
Let \(p=\operatorname{ord}\gamma\) (lowest nonzero component order) and \(\kappa=\lambda_{\max}/\lambda_{\min}\). The vector-field jet through \(D_f=\lfloor\kappa\rfloor\) and initialization jet through \(D_\gamma=\lfloor p\kappa\rfloor\) suffice to determine \(a_*,b_*\) using a fixed normal-form convention (choose nonresonant homological solutions, set free resonant transformation coefficients to zero). **Correction:** “through first order and second order” in the earlier narrative meant the two displayed bounds respectively, NOT universally linear/quadratic order.

Proof: invertible linear part implies at least one initial u coefficient has order p. Hence \(a_*\le p/\lambda_{\min}\). No coefficient of order exceeding \(p\kappa\) can win, since dividing by any eigenvalue gives strictly greater than that upper bound. The degree-j transformation contributes along gamma only at order at least pj, so degrees above \(\lfloor\kappa\rfloor\) are irrelevant. Homological equations through degree D depend only on the vector-field D-jet, and all resonances have degree at most D. The polynomial solution coefficients depend on u(0), so truncation modulo epsilon to order \(\lfloor p\kappa\rfloor\) suffices. Exact coefficients and exact resonance decisions assumed. This determines the leading time coefficients, not full H or constant shift. Dense input jets can be combinatorially large; no general efficiency claim.

Sharpness family: compare \(\dot x=x,\dot y=\Lambda y\) and \(\dot x=x,\dot y=\Lambda y+c x^k\) with \(c\ne0,k\ge2\), initial \((\epsilon,0)\). They agree through degree k−1. If \(\Lambda>k\), exit coefficients are 1 and k/\(\Lambda\) respectively; if \(\Lambda=k\), both a=1 but the forced system has b=1/k versus zero. For k=10 and Lambda=100 the leading time ratio is 0.1. To show worst-case sharpness at each spectral ratio \(\kappa\ge2\), take k=floor(kappa), Lambda=kappa (including resonance at integers). Similar seed variation \(y_0=\epsilon^j\) in the linear system demonstrates sensitivity of initial jets. No uniform fixed Taylor order across unbounded spectral ratios.

### PET-003C: resonant cascade (DERIVED + REPRODUCED)
\[
\dot x=x,\quad \dot y=2y+x^2,\quad\dot z=3z-2xy,\quad (x_0,y_0,z_0)=(\epsilon,0,0).
\]
Exact solution \(x=\epsilon e^t,\ y=t\epsilon^2e^{2t},\ z=-t^2\epsilon^3e^{3t}\).
Invariants (nu, lambda, d): x=(1,1,0), y=(2,2,1), z=(3,3,2). Thus a=1, b=2/3, selected z; limiting profile \((0,0,-e^{3s})\). For Euclidean exit rho=0.1, \(s_\rho=\ln(0.1)/3\). High precision results are reproduced by the versioned Python script and output file. The constant approximation converges slowly because subdominant coordinates persist algebraically. This example validates the algebra, not general novelty.

## Open research obligations

- Independent mathematical review of PET-002A and PET-003A/B; compare against closest published theorems rather than only broad literature.
- Mixed stable/unstable eigenvalues: invariant-manifold reduction, finite jet conditions, resonances, exact cancellation, non-escaping initial curves; complex/Jordan/center directions remain separate extensions.
- Constructive algorithm with complexity/precision bounds and no oracle for exact analytic vanishing; distinguish information sufficiency from computational efficiency.
- Determine global transition sequences with error control and possible unpredictability; do not assume local exit results compose.
- Define semantic capabilities through explicit task/algorithm grammar and prove connection to actual functional behavior. No current result does this.

## PET-004 update — 2026-11-24 UTC

See [PET-004.md](PET-004.md) for the mixed-spectrum impossibility, adaptive finite-flow-jet two-scale timing theorem, and contact-dependent sufficient degree. The previous mixed-spectrum leading-time question is internally resolved under the stated hyperbolic real-diagonalizable assumptions; global composition and the exact physical exit profile remain open.

## PET-005 update

See [PET-005.md](PET-005.md): global finite-jet obstruction, conditional power-log composition, precision and signed cancellation. Strong classical overlap; pivot to functional discovery.

## PET-006 update

See [PET-006.md](PET-006.md): genuine input-output composition hardness at one learning step and conditional deterministic emergence-population bounds/witness via tensor moments. Supplied compositional grammar and classical overlap limit novelty. Next infer latent functional representations.

## PET-007 update

See [PET-007.md](PET-007.md): loss-only all-curriculum indistinguishability and sharp ordered functional-readout depth for strongly convex Clifford quadratics. Exact 341-schedule implementation check reproduced. Full microscopic laws distinguish the models; no actual neural capability result. Next PET-008 tests learned functional representations.
