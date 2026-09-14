# COSXI-QHC01 — independent audit of COSXI-Q01

The localization Q1, geometry Q2, finite criterion Q4, and the complete analytic package pass as written, on their stated domains. No substantive proof gap or false analytic assertion was found. This conclusion concerns the supplied quantitative proof only. It does not establish historical novelty, completeness of the zero family, RH, or a result about a previous version.

## Scope and staged independence

The complete QUANTITATIVE_PROOF.md and RESULT.json were read after the phase-1 outline was frozen and ROOT acknowledged its hash without mathematical comment. The proof SHA256 checked by this auditor is `3891bc166dd7746c8952299529f0e5f3f490435ea9dd76aea114da2dc3a20667`. Author status labels were not used as premises. The explicit checklist and all ten registry claims were considered.

Only the staged released files, public primary sources, operational skill/runtime instructions, and this auditor's output were read. There were no children, other workers, model changes, historical research-file reads, source edits, author-script execution, external manuscript uploads, or contacts with people. Isolation means a fresh context with a read allowlist on a shared filesystem; it does not mean OS isolation or statistical independence. Actual model, reasoning setting, and service tier are UNKNOWN.

Seven initial independently formulated literature queries were recorded before phase-3 author-log/evidence access. Phase-2 CHECKLIST and RESULT already exposed the names Lagarias–Montague, Csordas–Smith, and DLMF; the search snapshot expressly discloses this. Its manually entered `recorded_utc` is inaccurate and has not been rewritten. Its actual filesystem freeze time is `2026-09-10T22:06:05.2971283Z`; ROOT verified the first hash before the separate phase-3 release. The timestamp defect is administrative and has no mathematical consequence.

## Per-claim verdicts

| Claim | Verdict | Decisive check |
|---|---|---|
| Q0 | PASS_AS_WRITTEN | Canonical logarithms, normalization, coordinate map and all phase levels agree. |
| Q1 | PASS_AS_WRITTEN | Q4 holds throughout an eventual tail; ordered real projections separate every pair. |
| Q2 | PASS_AS_WRITTEN | Exact parameter derivatives give the stated step errors; parameter elimination gives the sharper y(x) error. |
| Q3 | PASS_AS_WRITTEN | Both global complex bounds, including constants and the Cauchy-circle argument, hold for Re(w) ≥ 2. |
| Q4 | PASS_AS_WRITTEN | The stated finite hypotheses imply the strict full-disk bounds and a one-zero count for H itself. |
| ADD21 | PASS_AS_WRITTEN | The reciprocal terms are −1/w and +1/(6w), giving −5/(6w). |
| ADD22_23 | PASS_AS_WRITTEN | Direct real/imaginary expansion reproduces both equations with their signs. |
| ADD37 | PASS_AS_WRITTEN | Disk-wide derivative estimate follows from Q3 and the proven growth of Re(u). |
| UNIFORM_K | PASS_AS_WRITTEN | The only parameter-dependent constants are controlled by bounded D_t on K. |
| N1 | NOT_CHECKED_OPTIONAL | No numerical root checks were performed. Author figures remain unverified, noninterval illustrations. |

## 1. Exact reduction: Q0, equations (11)–(18)

For z = x + iy the map is w = y + 1/2 − ix. Conversely, substituting z = i(w−1/2) gives 1/2+iz = 1−w, hence Xi(z)=xi(w) by reflection, and cos z = cosh(w−1/2). This linear map has derivative i, preserves distances and multiplicities, and sends Re(w)>1, Im(w)<0 into the first open z-quadrant. The normalization and reflection agree with [DLMF 25.4.3–4](https://dlmf.nist.gov/25.4).

The half-plane Re(w)>1 is simply connected. The factors w, w−1, Gamma(w/2), zeta(w), and cosh(w−1/2) have no zeros there. The log-Gamma is the analytic logarithm normalized on the positive real axis, not the principal logarithm of the numerical Gamma value. Absolute locally uniform convergence of the Euler logarithm gives its exponential as zeta, consistently with [DLMF 25.2.11](https://dlmf.nist.gov/25.2#E11). The final logarithm is its convergent power series, since |exp(1−2w)|<e^(−1).

The factor 1/2 in xi cancels the factor 1/2 in cosh. Expanding (13), with Log(w−1)=Log w+Log(1−1/w), gives the w-dependent logarithmic terms

\[
\frac w2\Log w-\frac w2\log(2\pi)-\frac{3w}{2}
+\frac32\Log w.
\]

The remaining constant is log(t/(1−t))+log 2+(1/2)log pi+1/2=c_t. Thus a=2 pi e^3 and (18) are exact. All logarithmic identities hold first on w>1 and then by analytic continuation with the specified branches.

Since the prefactor in (14) never vanishes, the complete set of zero conditions is L_t=(2m+1)pi i. At each fixed level, 1+exp(L) has nonzero derivative with respect to L. The negative level −iq_n has m=−n−1. No global branch of the logarithm of H is being assumed.

## 2. Global complex remainder: Q3 and ADD21

Write R=|w| and sigma=Re(w)≥2. The logarithmic series gives |Log(1−1/w)|≤1/(R−1). The first omitted term of the log-Gamma expansion at w/2 is 1/(6w). The sector factor for this logarithmic expansion is sec²(arg(w)/2)≤2, giving |S_Gamma(w)|≤1/(3R). The actual expansion and the first paragraph of [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii) were inspected, including the distinction between log-Gamma and Gamma remainder bounds and the permitted sector |arg w|<pi.

Positivity of the Euler-log coefficients gives

\[
|L_\zeta(w)|\le\log\zeta(\sigma)\le\zeta(\sigma)-1
\le 2^{-\sigma}+\int_2^\infty x^{-\sigma}\,dx
\le3\,2^{-\sigma}.
\]

The last logarithm is bounded by e^(1−2sigma)/(1−e^(1−2sigma)). These four estimates establish (19) uniformly in Im(w), with no t-dependence.

For (20), the radius-R/4 Cauchy disk avoids the negative real cut: its arguments have absolute value at most pi/2+arcsin(1/4)<3pi/4, and every point zeta on it has |zeta|≥3R/4. Log-Gamma minus its leading expression is analytic on the cut plane. The same sector bound yields

\[
|S_\Gamma(\zeta)|
\le\frac{\sec^2(3\pi/8)}{6(3R/4)}
<\frac{14}{9R}<\frac2R.
\]

Cauchy's derivative estimate therefore gives |S'_Gamma(w)|≤8/R². Also 1/|w(w−1)|≤2/R². The argument uses an expanded sector for S_Gamma only; it never extends the Euler-log to that circle.

Termwise Euler-log differentiation gives a Dirichlet series with coefficients Lambda(n)≤log n. Since n≥2 and sigma≥2,

\[
|L'_\zeta(w)|\le4\,2^{-\sigma}\sum_{n\ge2}\frac{\log n}{n^2}.
\]

The summand is decreasing on [2,infinity). Its sum is at most log(2)/4+(1+log 2)/2=1/2+3log(2)/4<5/4. The coefficient 5 is valid. Finally 2e^(1−2sigma)/(1−e^(1−2sigma))<3e^(1−2sigma), because e^(1−2sigma)≤e^(−3)<1/3. This proves (20) on the entire stated half-plane, including sigma=2.

For ADD21, Log(1−1/w)=−1/w+O(R^(−2)); retaining the first Gamma correction gives S_Gamma(w)=1/(6w)+O(R^(−3)) in the closed right sector. The remaining two terms have their stated exponentially small bounds. Equation (21) follows. It is not needed in Q4.

## 3. Phase coordinates and explicit model: ADD22_23 and §4

With w=sigma−ix and Log(w/a)=A−i theta, multiplication gives

\[
w\Log(w/a)=\sigma A-x\theta-i(xA+\sigma\theta).
\]

Adding (3/2)(log rho−i theta)+c_t+E and equating to −iq_n gives exactly (22) and (23). Both equations are necessary and together sufficient. These are equations in the inherited domain Re(w)>1 (and their quoted error bound uses sigma≥2). The notation x,sigma>0 in this paragraph is a coordinate convention, not a new claim that the Euler-log converges for 0<sigma≤1. Making that inherited restriction explicit would improve presentation but is not required to repair the theorem.

The left side of (2) increases strictly from 0 to infinity; its logarithmic derivative is 1/beta+2tan beta+beta sec² beta>0. Thus beta exists uniquely and smoothly for each q>0. With alpha=beta tan beta, direct multiplication gives B exp B=−2iq/a. Therefore u=ae^B=−2iq/B, arg u=−beta in (−pi/2,0), Log(u/a)=B, and F(u)=−iq.

As q decreases to zero, B tends to zero. Since B+1 is never zero, the inverse-function theorem continues this local inverse along the negative imaginary ray. That ray lies in the standard principal branch domain in [DLMF 4.13](https://dlmf.nist.gov/4.13); the identification with W_0 is valid and is independent of any software branch label.

Taking moduli gives ell=alpha+(1/2)log(alpha²+beta²). Since beta is bounded and alpha tends to infinity, first alpha~ell and then alpha=ell−log ell+O(log ell/ell). The relation alpha=beta cot(pi/2−beta) gives beta=pi/2+O(1/ell). Formula (26) then gives (28), in particular s~pi q/(log q)²→infinity before any small-zeta use.

Lastly F'(u)=(B+1)/2=d and Log u=log a+B. Dividing the lower-order residual by d yields h_t=−3−D_t/(B+1). The additional −1/2 in the z coordinate makes the constant contribution −7/2 inside the parentheses. No root equation for F_0 is hidden in the definition of the center.

## 4. Exact finite criterion: Q4, equations (30)–(36)

Let delta=w−(u+h_t), eta=h_t+delta. The finite hypotheses, without an asymptotic substitution, imply |delta|≤1, |eta|≤5, |w|≥U−5, Re(w)≥s−5≥2, and Im(w)≤−v+5≤−1 on the closed disk. The connecting segment from u to w has the same bounds. A neighborhood of this compact disk stays inside Re(w)>1, so every function used in Rouché is analytic there.

By (19) and (31), the bound for E is

\[
\frac1{U-6}+\frac1{3(U-5)}+\frac1U<\frac3U.
\]

For an explicit all-U check, multiply by U: the left side is at most 100/94+100/285+1<3 because U/(U−c) decreases for U>c. This verifies (32) for every U≥100.

Taylor's integral remainder uses F''(w)=1/(2w), hence its bound is |eta|²/[4(U−5)]. The logarithmic difference is bounded by |eta|/(U−5). Cancellation of dh_t+(3/2)Log u+c_t leaves G=L_t+iq=d delta+Remainder with

\[
|\mathrm{Remainder}|<\frac{25/4+15/2}{U-5}+\frac3U
=\frac{55}{4(U-5)}+\frac3U<\frac{20}{U}.
\]

For the last inequality the U-multiplied expression is at most 5500/380+3<20. Thus neither the radius nor the constant 40 needs alteration.

Since q=U|B|/2 and Re(B)>0, the linear term on the boundary has modulus (40/U)|B+1|/|B|>40/U. Rouché gives exactly one zero of G, counted with multiplicity; its hypotheses agree with [DLMF 1.10(iv)](https://dlmf.nist.gov/1.10#iv).

This alone would not count H. The additional full-disk bound is valid:

\[
|G|<\frac{40}{U}\left(1+\frac1{|B|}\right)+\frac{20}{U}
\le\frac{100}{U}\le1.
\]

The strictness comes from the remainder inequality even at U=100. Consequently exp(L_t)=−exp G and no level G=2k pi i with k nonzero is present. The analytic continuation of (1−exp G)/G has value −1 at zero and no zeros for |G|<1. Multiplication by it and by the nonvanishing cosh factor preserves the G zero count. H therefore has exactly one zero with multiplicity one, and none on the boundary. The disk is in the stated quarter-plane and its z image is in the first quadrant.

## 5. Tail, derivative and separation: Q1, Q2, ADD37, UNIFORM_K

All quantities U, |B|, q, s, v in (30) tend to infinity. For fixed t, h_t tends to −3. Further,

\[
U2^{5-s}\to0,\qquad Ue^{11-2s}\to0,
\]

because s~pi q/(log q)² while log U=O(log q). Thus every finite condition holds simultaneously for all sufficiently large real q, and hence all sufficiently large q_n. A subsequence argument or numerical threshold is unnecessary.

On those disks w−u=O_t(1). Equations (20) and (28) give E'=O(U^(−2)), as their exponential terms are smaller than U^(−2) eventually. Expanding the explicit derivative of F_0 around u gives L'_t(w)=d+O_t(U^(−1)), uniformly throughout the disk. This proves ADD37. Simplicity in Q4 was already obtained from the multiplicity count and does not rely on ADD37.

Differentiating the exact identities gives all three formulas in (38). In particular u''=2i B/[q(B+1)^3]=O(1/[q(log q)²]) and h'_t=O_t(1/[q(log q)²]). Integrating on [q,q+2pi] gives the center increment (8); both error estimates hold uniformly on that fixed-length interval. Multiplication by i gives the positive leading term 4pi/(B+1). The real part of the continuous center's derivative is 2(alpha+1)/[(alpha+1)²+beta²]+O_t(1/[q(log q)²])~2/log q>0. Adjacent real projections are separated by a gap asymptotic to 4pi/log q, while the sum of radii is O(1/q). Eventually each projection's right endpoint lies left of the next one's left endpoint. Transitivity establishes separation of all pairs, and the actual zeros have strictly increasing real parts. Adding two localization errors gives (9). The radius/spacing ratio is O(log n/n)→0.

Formula (26) with h_t=O_t(1) and the localization error gives x_n=2q_n alpha_n/(alpha_n²+beta_n²)+O_t(1), y_n=2q_n beta_n/(alpha_n²+beta_n²)+O_t(1). Substituting q_n=(2n+1)pi and (27) verifies both leading constants in (7) and the relative errors.

For (10) it is essential to use alpha=log(U/a), not to substitute the rough n-asymptotic directly. Indeed s/v=beta/alpha and U/v=1+O(alpha^(−2)); hence alpha=log v−log a+O(alpha^(−2)). Together with beta=pi/2+O(alpha^(−1)), this gives s=pi v/(2log v)+O(v/(log v)²). The O_t(1) changes from v,s to x_n,y_n are absorbed in that error. The stated bound contains no omitted log-log loss.

For a fixed compact K in (0,1), D_t is bounded. This makes the h_t estimates, their derivatives, the geometric errors and their eventual thresholds uniform on K. Every other bound is independent of t. Endpoint uniformity, an optimal N(t), trajectories and complete zero enumeration are outside the assertions.

## Dependencies and limits

Q0 and the model construction are independent of Q3. The proof of Q4 uses only the E-bound (19), not (20), ADD21 or ADD37. Q1 then uses Q4 and the tail and projection arguments. Q2 uses the explicit model derivatives and Q1's localization; ADD37 separately uses the derivative part of Q3. ADD22_23 is an algebraic consequence of Q0, not a needed alternative to the complex equation. UNIFORM_K follows by tracing those proofs. N1 is a premise of none of them.

No first invalid line or counterexample is reported because none was found in the analytic claims on their inherited domains. The separate literature audit records bounded negative search findings and known methods, not novelty. The sources were checked through their actual relevant formulas/pages; no source's bibliographic appearance was treated as verification. No numerical scan or even optional numerical root point was used. This is an independent mathematical review, not formal proof verification or an interval certificate.
