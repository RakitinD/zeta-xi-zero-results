# COSXI-CHC01 independent audit report

## 1. Verdict and audited object

**Overall increment: PASS_AS_WRITTEN. Completeness C1: PASS_AS_WRITTEN. Total nonreal count C2: PASS_AS_WRITTEN.** Each of U1, U2, U3, F1, C1 and C2 passes on the precise fixed-parameter scope stated in the submitted proof. No first invalid line, substantive gap, false statement, or additional required clarification was found.

For every fixed real \(0<t<1\), the original phase-indexed zeros in the prescribed disks, after an increase of their starting index only, exhaust the nonreal zeros through their fourfold orbits modulo a finite multiset. With analytic multiplicities and the closed radial cutoff, \(N_t^{\rm nr}(R)\sim R\log R/\pi\). This is a total count, because completeness and the necessary inherited scopes have been checked.

The entire submitted source, sections 1-7 of COMPLETENESS_PROOF.md, was read. Its SHA256 is dd8272fd7b87002f434a95a48051ce60fff786bc0d88c6c538ccb45a0cdc9dcc, matching the claim matrix. The original quantitative proof and qualitative V1 hashes match their frozen values. DEPENDENCY_CHECK.md details what was rechecked; the old audit labels were comparison evidence only.

## 2. U1: positive real derivative

Source: section 2, (2.1)-(2.2), using I1-I2. The analytic decomposition differentiates to
\[
L_t'(w)=\tfrac12\Log(w/a)+\tfrac12+\frac{3}{2w}+E'(w).
\]
On \(\sigma=\Re w\ge\Sigma=a\), \(|w|\ge\Sigma\), \(\Re\Log(w/a)=\log(|w|/a)\ge0\), and \(\Re(1/w)=\sigma/|w|^2>0\). Taking the negative absolute-value bound for the remainder, and enlarging each loss by replacing \(\sigma,|w|\) with \(\Sigma\), has the correct inequality direction.

Since \(\pi>2\) and \(e>2\), \(\Sigma>32>16\). The displayed bounds \(10/16^2<1/16\), \(5\,2^{-16}<1/16\), and \(3e^{-31}<3\,2^{-31}<1/16\) are all strict. Thus (2.2) exceeds \(1/2-3/16=5/16\). The derivative estimate is valid on the closed half-plane, including its boundary, and for every stated t because only the real additive constant \(c_t\) depends on t. Verdict: PASS_AS_WRITTEN.

## 3. U2: injectivity and simplicity

Source: section 3, (3.1) and the simplicity paragraph. A segment between any two points of \(\mathcal D=\{\Re w>\Sigma\}\) stays in \(\mathcal D\). Dividing the integral of \(L_t'\) along that segment by its nonzero displacement yields (3.1). Its real part is greater than \(5/16\); hence the quotient and difference cannot vanish. This is global injectivity, proved without a claim that a nonzero derivative alone suffices.

At an odd level, the derivative of \(1+\exp L_t\) is \(-L_t'\ne0\). The prefactor is nonzero and the affine coordinate map has nonzero derivative. Every represented root in this half-plane is therefore simple. No simplicity assertion about central exceptions or Xi zeros follows or is made.

The cited classical criterion has exactly the required convex-domain form: take \(f=L_t\), \(D=\mathcal D\), and rotation constant zero in Hotta-Wang, section 1.2, Theorem 1.A. Nonconstancy follows from U1. No disk normalization is required, and the submitted direct proof already establishes the needed strict case. [Hotta-Wang primary text](https://arxiv.org/html/1401.5647). Verdict: PASS_AS_WRITTEN.

## 4. U3: phase signs, indices and axes

Source: section 4, (4.1), phase table and reflection paragraphs. The real-ray normalization gives \(\Im L_t(\sigma)=0\). The derivative with respect to v is
\(\Im(iL_t'(\sigma+iv))=\Re L_t'(\sigma+iv)>0\).
Integrating from zero proves (4.1), with the integral negative when \(v<0\), positive when \(v>0\), and zero exactly when \(v=0\).

The map is \(w=y+1/2-ix\), so for \(M=\Sigma-1/2\):

| Position in the upper z half-plane | Sign of Im w | Odd level | Original level integer |
|---|---|---|---|
| \(x>0,\ y>M\) | negative | \(-i(2n+1)\pi,\ n\ge0\) | \(m=-n-1\) |
| \(x<0,\ y>M\) | positive | \(+i(2n+1)\pi,\ n\ge0\) | \(m=n\) |
| \(x=0,\ y>M\) | zero | none | none |

The all-level factorization leaves no missing \(2\pi i\) offset. The upper-left partner is \(-\bar z\), whose w-coordinate is \(\bar w\); equality of \(L_t(\bar w)\) and \(\overline{L_t(w)}\) follows from the canonical real-ray normalization and the identity theorem. Evenness and conjugation in z preserve Taylor multiplicities and generate the lower partners. Imaginary-axis positivity is independently valid for the entire axis by I4. The real axis is outside the logarithmic domain used here and is excluded from the target multiset. Verdict: PASS_AS_WRITTEN.

## 5. F1: the finite complement

Source: section 5 through (5.2). The escape \(\Re u_n\to+\infty\), \(h_{n,t}\to-3\), and \(40/q_n\to0\) permit a single integer \(N_C(t)\ge3\) for which every later original closed disk lies in \(\mathcal D\). This is a whole eventual tail, not a subsequence. The original centers, radii and indices remain unchanged.

The closed strip \(|\Im z|\le M\) is unbounded. Its nonreal multiset \(\mathcal S_t\) is finite by the directly checked strip theorem; isolation of zeros alone would be insufficient. Both boundary-height lines are assigned to \(\mathcal S_t\).

For each \(0\le n<N_C(t)\), \(A_n\) consists of actual roots by the factorization and is empty or a singleton by injectivity; if present the root is simple. Different levels cannot share a root. Thus \(A_t\) has at most \(N_C(t)\) points; no existence is assumed for a low level.

For any first-quadrant root above M, U3 provides a unique nonnegative original phase index. At a high index the original disk theorem already supplies a root at precisely that same level inside \(\mathcal D\), and U2 makes the proposed root identical to it. This is the decisive completeness implication; existence is imported from I3, not inferred from injectivity or surjectivity.

Every remaining remote nonreal zero has nonzero real part and exactly one first-quadrant representative per fourfold orbit. The strip and remote low-level orbits have disjoint height ranges, and different representatives give different orbits. Consequently the finite multiset
\[
E_t=\mathcal S_t\uplus\biguplus_{z\in A_t}\{z,\bar z,-z,-\bar z\}
\]
has total multiplicity at most \(\operatorname{mult}(\mathcal S_t)+4N_C(t)\). Central multiplicities are retained and no real zero is included. Verdict: PASS_AS_WRITTEN.

## 6. C1: exact multiset equality

Source: section 5, (5.3) and its proof. F1 classifies every nonreal zero; conversely I3 and the exact symmetries make every listed tail point a zero. A first-quadrant representative has four distinct orbit points. Distinct original disk zeros cannot have the same representative, so their orbits are disjoint. Low levels cannot equal high levels, and the closed strip does not meet the tail. Analytic multiplicities are one in the tail and retain their actual values in \(E_t\).

This proves both containments and the disjoint multiset equality exactly. Bounded support of \(E_t\) is a consequence of the proved finiteness, not a hidden assumption about an unbounded region. Verdict: PASS_AS_WRITTEN.

## 7. C2: sequence count, factor four and total count

Source: section 6, (6.1)-(6.6). All three logical judgments are positive, for distinct reasons.

First, \(y_n/x_n\to0\) and \(x_n>0\) eventually imply \(\rho_n=|z_n|\sim4\pi n/\log n\). The model \(f(s)=4\pi s/\log s\) has positive derivative for \(s\ge3\). Setting \(v(S)=S\log S/(4\pi)\) gives \(f(\lambda v(S))/S\to\lambda\). Model monotonicity and integer rounding yield \(B(S)\sim S\log S/(4\pi)\), as written.

For every fixed \(\varepsilon\in(0,1)\), all sufficiently late indices satisfy
\((1-\varepsilon)f(n)\le\rho_n\le(1+\varepsilon)f(n)\).
The lower inclusion follows from \(f(n)\le R/(1+\varepsilon)\); the upper from \(\rho_n\le R\Rightarrow f(n)\le R/(1-\varepsilon)\). Omitting the finitely many earlier indices gives exactly (6.4). Taking \(R\to\infty\) at fixed epsilon and then epsilon down to zero proves the sequence count (6.5). No monotonicity of the actual radii enters. Every inclusion uses the closed inequality, so radius-boundary roots are counted.

Second, conditional on C1, the orbit symmetries preserve modulus, and all four tail roots are simple. Therefore the factor-four passage
\(N_t^{\rm nr}(R)=4A_t(R)+E_t(R)\)
is exact for every \(R\ge0\), with \(0\le E_t(R)\le\operatorname{mult}(E_t)<\infty\).

Third, C1 and its required inherited inputs are checked in this audit, so that conditional calculation establishes the **total** nonreal count unconditionally within the stated fixed-t mathematical assumptions. The coefficient is \(4/(4\pi)=1/\pi\). Without completeness the same sequence arithmetic would only furnish a total-count lower bound; that distinction is explicit in the source and registry. Verdict: PASS_AS_WRITTEN.

## 8. Comparison with inherited records

The quantitative original and its audit explicitly exclude completeness. Their accepted localization is used only within its proved scope. The original disk proof's \(|G|<1\) step, not the old PASS label, establishes the exact phase needed here.

The qualitative V1 strip proof had a local expository omission concerning the height on Rouché circles. Its estimate already holds for every fixed height; V1.1 and the new proof explicitly use \(L=\max(M,d)\). I4 is checked with that already incorporated clarification. No further clarification or new theorem is needed in the current increment. Old LC2 and LC3 concern growth-contradiction wording and a parameter-endpoint argument, neither of which is needed for I4 here.

The prior quantitative N1 evidence locator incorrectly combines a filename and heading; its old manual search timestamp is also qualified by the released ROOT records. The exact bytes and qualifications are preserved. N1 and those administrative fields are not mathematical premises of I1-I4. Their defects do not validate or invalidate the new mathematics and were not silently repaired.

The author RESULT, report, search, integration proposal and administrative evidence were read as comparison material after the initial search freeze. The integration proposal remains a proposal: the English manuscript was not accessed or edited. Historical source instructions and proposed future work were not acted on.

## 9. Scope, chronology and limits

The phase-1 outline was written after only the dispatch and two phase-1 research files. ROOT acknowledged its first SHA256 before releasing phase 2. Initial mathematical notes and actual short public queries were recorded before the full author ledger and inherited audit reports; ROOT acknowledged the first search SHA256 before phase 3. These early files remain unchanged.

Source names and historical labels were already visible within phase-2 permitted prose, including Hotta-Wang, Lagarias-Montague, Csordas-Smith, NIST DLMF, Gardner, Lindelof/Boas and old audit labels. This is not blindness to those disclosures. The parent supplied no mathematical evaluation or expected verdict. The single fresh context had no children or setting changes. Actual model, reasoning and service tier are UNKNOWN.

All released source bytes are retained under evidence/released_inputs. The PDF skill and runtime documentation were used solely for public-source rendering. No author/source script, numerical root scan, install, proof repair, new theorem, K1, second term, endpoint theorem, uniform exceptional bound, threshold optimization, trajectory study, manuscript edit, publication, contact or private upload was performed. This is a mathematical audit by one language agent, not formal verification or human review.

The independent literature assessment is in PRIOR_ART_AUDIT.md. Known methods and bounded failure to find an exact predecessor do not establish world novelty, priority, or publication value. Local system clocks and hashes establish observable byte chronology only, not trusted external notarization, private cognitive order, OS isolation, or statistical independence.

STOP_FOR_SOL_REVIEW after the first final freeze.

