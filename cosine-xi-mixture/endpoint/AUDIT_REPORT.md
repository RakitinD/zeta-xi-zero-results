# COSXI-EHC01 — independent endpoint audit

## 1. First verdict and exact object

**Overall increment: PASS_AS_WRITTEN. Leading all-root front: PASS_AS_WRITTEN. Two-term all-root front: PASS_AS_WRITTEN.** E0–E5 each pass on their stated scopes. No substantive gap, false mathematical claim on those scopes, unresolved necessary dependency, or required repair was found. There is therefore no first invalid line to propagate.

The audited object is the complete first COSXI-E01 ENDPOINT_PROOF.md, sections 1–8, SHA256 `3de5141d1ed01051416e214cbd76e1eb0b5414a935b3d788aa3f2a56e315a949`, independently hashed from the released copy. Author status labels and old PASS labels are comparison material, not premises. For each real **fixed** d>1/2, the proof establishes

\[
R_d(t)=\frac4\pi\lambda+\frac{2d+7}{\pi}\log\lambda+O_d(1),
\qquad \lambda=\log\frac{t}{1-t}\longrightarrow+\infty,
\]

for the infimum over **all** H_t zeros with |Im z|>=d, including boundary zeros. The lower bound has no height cutoff; the upper bound contains a genuine simple zero for every sufficiently large real lambda. The weaker O_d(log lambda) leading law follows separately from these bounds. No limiting constant for the bounded remainder is asserted.

## 2. E0 — compact scope

Source: section 1, including (1.1). The exact difference H_t−Xi=(1−t)(cos−Xi) converges uniformly on every compact set. On a zero-free compact K, its norm is eventually below min_K|Xi|, proving the stated criterion directly. A sufficiently small circle around an isolated Xi zero admits strict Rouché comparison, and its zero count retains analytic multiplicity. For a simple real zero, a symmetric disk contains exactly one zero counted with multiplicity; conjugation forces it to be real and the count forces simplicity. The same conclusion is not extended to multiple zeros.

For RH implying escape, the compact set {|z|<=R, |Im z|>=d} is Xi-zero-free for each R and each fixed d>0. Conversely, an off-axis Xi zero admits a disk bounded away from the real axis. Choose d smaller than that disk's distance from the axis: persistence gives an eligible H_t zero of bounded modulus. The quantifier “every fixed d>0” is essential. Reflection and the Euler product give unconditional Xi-zero-freeness for |Im z|>1/2. The statement is compact scope, not a new RH proof. Verdict: PASS_AS_WRITTEN.

## 3. E1 — canonical levels, motion and maximal exit

Source: section 2, (2.1)–(2.6) and its interval argument. DEPENDENCY_CHECK.md sections 2–3 verify the original I1–I2 calculations. Substitution gives 1/2+iz=1−w, Xi(z)=xi(w), and cos z=cosh(w−1/2). The factors 1/2 cancel in the quotient. The real-ray logarithms yield exactly L_t=lambda+ell, with every odd integer level and no hidden 2*pi*i shift. At an odd level, the quotient (1+exp L)/(L−level) extends with value −1, preserving multiplicity. The cosh factor is nonzero on Re w>1.

The inherited derivative estimate is valid on the whole closed half-plane Re w>=2. At Re w>=a=2*pi*e^3, the explicit derivative has logarithmic real part nonnegative, Re(1/w)>0, and the three remainder losses are each strictly below 1/16. Thus Re ell'>5/16. Integration on the segment between two points of the convex D={Re w>a} proves a nonzero difference quotient and global injectivity. The analytic inverse exists on ell(D), without any assumption that this image is convex or surjective. The real-ray normalization and vertical integration give |Im ell(sigma+iv)|>=(5/16)|v|.

For an actual root at fixed odd phase ip, the connected component J of {lambda:ip−lambda in ell(D)} is an open interval. The inverse defines the unique branch on that component. Differentiation gives w'=−1/ell'; since Re(1/ell')=Re ell'/|ell'|²>0, height decreases, and |w'|<16/5. Simplicity follows from ell'!=0.

The stronger interval conclusion is genuinely proved. At fixed p the imaginary part of w is bounded by 16|p|/5. In the forward direction its real part decreases between a and its initial value. An infinite right endpoint would confine the branch to a compact rectangle where ell is bounded, contradicting Re ell=−lambda. At its finite endpoint the speed bound makes w Cauchy. Analyticity extends to a neighborhood of the closed line Re w=a; an interior limit would continue the inverse branch, so its real part tends to a. A finite left endpoint has real part at least its interior initial value and bounded displacement, and likewise permits continuation; it is impossible. Hence J=(−infinity,beta), beta finite. This proves the actual component statement, without needing to assume components of arbitrary horizontal sections are connected. Exit is through height a−1/2, not the real axis. Both motion components: PASS_AS_WRITTEN.

## 4. New estimates for every fixed r>1

Source: section 3, (3.1)–(3.5). The exact decomposition has explicit part (w/2)Log(w/a)+(3/2)Log w+c_0 and remainder E independent of lambda. The four bounds are valid for all Re w>=r: 1/(|w|−1), 1/(3|w|), log zeta(r), and exp(1−2r)/(1−exp(1−2r)). In particular no Re w>=2 estimate is extrapolated below 2. The logarithmic Gamma remainder and its sector domain were checked against the actual authoritative formula; see DEPENDENCY_CHECK.md, I3.

For delta_r=(r−1)/2, every closed disk centered in Re w>=r stays in Re w>=r_-=(r+1)/2>1. Analyticity holds on a neighborhood. Cauchy's derivative formula gives M_(r_-)/delta_r and **2**M_(r_-)/delta_r² for E' and E''. Thus all constants are fixed before lambda grows and uniform in the imaginary part.

Differentiating the exact explicit expression gives A>=one-half log|w|−C_r; the discarded Re(3/(2w)) is positive. The argument of w bounds the imaginary logarithmic term by pi/4, and the remaining derivative terms give the stated bound for |B|. Since |w|>=x, the choice X_r=exp(4C_r) gives A>=one-quarter log x for every sigma>=r and x>=X_r. Here C_r>0, so X_r>1 and the asserted strict positivity is valid. On a fixed band A=one-half log x+O_r(1). The second derivative of the explicit part, 1/(2w)−3/(2w²), is uniformly bounded as well. Verdict: PASS_AS_WRITTEN.

## 5. E2/E3 lower half — all-height exclusion

Source: (3.6), section 4, (4.1)–(4.2). Put s=d+1/2, kappa=pi/4 and b=s/2+3/2. Multiplying (sigma−ix)(log(rho/a)−i theta) gives the real term sigma log(rho/a)−x theta; its sign is correct. At sigma=s, replacing theta by pi/2−arctan(s/x) gives

\[
U(s,x)=-\kappa x+b\log x+e_s(x),\qquad |e_s(x)|\le P_s.
\]

Indeed 0<=log(rho/x)<=s²/(2x²), 0<=x arctan(s/x)<=s, and each remaining contribution fits P_s. No convergence of the bounded Euler/cosh part is used.

Evenness and conjugation permit a representative z=x+iy with x>=0 and y>=d. For **bounded x** in [0,X_s], (3.4) gives U_sigma>=1 once sigma>=S, uniformly in that x interval. The minimum on [s,S]x[0,X_s], followed by integration for sigma>S, is a lower bound on the entire unbounded-height region. For large lambda, F_lambda=lambda+U is positive there. Compactness was applied only to a compact rectangle.

For x>=X_s, U_sigma>0 on every intermediate height sigma>=s. Any eligible zero has F_lambda(sigma,x)=0 and therefore F_lambda(s,x)<=0. The boundary error yields kappa*x>=lambda+b log x−P_s. Because b>0 and x>=1, this first yields x>=lambda/(2*kappa) for large lambda. Substitution gives

\[
x\ge\kappa^{-1}\lambda+(b/\kappa)\log\lambda-C_L=T(\lambda)-C_L.
\]

The specified C_L safely absorbs P_s+b log(2*kappa). Finally |z|>=x. Reflection preserves modulus and |Im z|, and equality at height d is retained. This is exclusion of every smaller-radius exterior zero, including any old exceptional zeros and unbounded heights. It uses neither old completeness nor a uniform exception bound. Verdict: PASS_AS_WRITTEN.

## 6. E2/E3 upper half — genuine phase and radial minimum

Source: section 5, (5.1)–(5.4). For fixed c in [C,C+1], log((T+c)/lambda) tends uniformly to log(kappa^{-1}). With the source's Q_s and C, the combined boundary error is <=Q_s, giving −J<=F_lambda(s,x)<=−2 throughout the full length-one interval. All constants are positive and depend only on fixed s. Eventually x>=lambda, so integrating A>=one-quarter log lambda over h_lambda=4(J+1)/log lambda gives F_lambda(s+h_lambda,x)>=1.

The intermediate value theorem and strict increase in sigma give a unique scalar solution in (s,s+h_lambda), including at the interval's endpoints. Since U_sigma=A>0, the real implicit function theorem applies on an open neighborhood of each point; these local solutions agree by uniqueness and give the smooth curve and its endpoint extensions.

In the coordinates sigma−ix, the Cauchy–Riemann signs are U_sigma=A, U_x=B, V_sigma=B and V_x=−A. Consequently sigma'=−B/A and

\[
\frac{dV}{dx}=-\frac{A^2+B^2}{A}\le-\tfrac14\log\lambda.
\]

For sufficiently large lambda the phase decreases by **strictly more than 2*pi** across the interval, so its open image contains an odd multiple of pi. At that interior point the modulus is also exactly balanced. The canonical factorization therefore yields a true H_t zero, and A>0 gives multiplicity one. Its height is strictly above d, with y<d+h_lambda. This is an existence assertion for every sufficiently large real lambda, not a subsequence or a modulus-only surrogate.

For large lambda, y<=d+1 and x is comparable to lambda. The source's identity |z|−x=y²/(|z|+x)<= (d+1)²/(2x) gives the required bound |z|<=T+C+2. Combining this actual-root upper bound with section 5 of this audit yields T−C_L<=R_d<=T+C+2 over the full eligible set. Since b/kappa=(2d+7)/pi, the two-term and leading radial minimum claims both pass. None of the inference relies on fixing t while allowing a phase index to grow, then substituting an index depending on t. Verdict for each upper-root, leading-minimum and two-term-minimum component: PASS_AS_WRITTEN.

## 7. E4 — attainment, every minimizer and canonical phase

Source: section 6, (6.1)–(6.3). The constructed root makes the eligible set nonempty. H_t is entire and nonzero; nonidentity can already be seen on the positive imaginary ray with w>1, where xi(w)>0 and cosh(w−1/2)>0. Thus finitely many zeros occur in the disk bounded by the constructed root's radius. Its nonempty eligible finite subset contains the minimum. The closed height restriction causes no problem. Section 4 has also excluded x=0 for large lambda, so a minimizing orbit has a first-quadrant representative.

For every such representative in the stated radius window, x lies between T−C_L and T+C+2. Substitution in the boundary expansion bounds |F_lambda(s,x)| by a fixed constant. Integrating A>=one-quarter log x from s to its actual sigma, with no prior upper-height hypothesis, gives sigma−s=O_d(1/log lambda). This establishes the height estimate for **every** minimizer and every first-quadrant root in that window, not just the root constructed in section 5.

The coordinate convention matters: the positive x inequalities in the “more generally” paragraph retain the first-quadrant representative convention from section 4 and the preceding minimizer paragraph. An unreflected upper-left partner has signed real part −x. I regard this as the existing convention, not a missing mathematical hypothesis or a required repair; absolute height and modulus conclusions are symmetric. The report and registry explicitly retain that convention.

On s<=sigma<=s+1 the exact imaginary expression is x/2 log(rho/a)+(sigma/2+3/2)theta−Im E. Its replacement by x/2 log(x/a) costs O_d(1), since the first error is O_d(1/x) and the remaining terms are bounded. Hence the original phase is negative eventually. The all-odd-level identity gives q_n=−Im ell=(2n+1)pi and m=−n−1 without a rebranching. From x=4lambda/pi+O_d(log lambda), q_n~2lambda log lambda/pi and n~lambda log lambda/pi² follow. RESULT.json states this for a deterministic selected minimizer, while the proof and RESEARCH_REPORT establish it for every minimizing representative. This is a valid stronger proof, not a contradiction. No rank or continuous minimizing branch is asserted. All three components: PASS_AS_WRITTEN.

## 8. E5 — scalar basepoint and complex profile

Source: section 7, (7.1)–(7.2). The prescribed x_lambda=T+C is an endpoint of the valid scalar-curve interval. It has a unique balance height strictly between s and s+h_lambda. No odd-phase condition is imposed, and accidental equality to a zero is allowed. Its p_lambda=ell'(w_lambda)=one-half log lambda+O_d(1)+iO_d(1) follows from the fixed-band derivative estimates; it is nonzero. Exact modulus balance gives |eta_lambda|=1.

Let K be a fixed compact complex v-set and M=max_K|v|. The displacement is <=M/|p_lambda| and tends to zero. Taking r=(s+1)/2, all the full connecting segments lie in Re w>=r eventually, including any that cross below s. With a uniform bound D_r on |ell''|, the integral Taylor error is at most D_r M²/(2|p_lambda|²)=O_d,K((log lambda)^{-2}). Exponentiating this bounded small error proves (7.2) uniformly on K. The exact cosh factor is nonzero there; no lower bound uniform in t is needed because the ratio identity is exact.

Every sequence lambda_j to infinity has a subsequence on which eta_lambda_j tends to a unit eta. The normalized functions converge locally uniformly to 1+eta exp v. Its lattice zeros have derivative −1 and are simple. On small disjoint circles about any finitely many of them, uniform convergence gives a Rouché count of exactly one, with multiplicity, and therefore a simple zero of the original normalized function. There is no claimed rate to a fixed eta without a phase convergence rate. These points remain in the Euler domain, but need not all have height >=d. All four profile components: PASS_AS_WRITTEN.

## 9. Dependencies, comparisons and audit limits

I1–I3 are CHECKED_REQUIRED_SCOPE; the explicit checks are in DEPENDENCY_CHECK.md. E0 is separate. E1 uses inherited U1–U3 and its additional continuation proof. Sections 3–7 use their own estimates on every fixed exterior and the canonical identity, without the old localization disks, total count, finite-exception theorem, fixed-t threshold or numerical evidence. A hypothetical E1-only problem would not automatically erase E2–E5; a common logarithmic identity problem or missing all-height/phase step would affect the main front. No such problem was found.

The author RESULT, report, prior-art check, ledger, first freeze and self-check were read only in phase 3. The inherited quantitative audit sections 1–2 and completeness audit/dependency sections 2–4 agree with the independently checked necessary scopes. Their other fixed-t claims were not re-audited. Historical source references to old timestamp/locator defects were not followed into unreleased records and are not premises here. Administrative self-check labels are not mathematical validation.

The first outline preceded proof access; the initial notes and actual short search preceded author-ledger and old-audit access. The three early records remain unchanged. Source names already visible in the proof, particularly DLMF and Hotta–Wang, are disclosed in those records. This is one fresh-context, staged-source audit on a shared filesystem, not proof of OS isolation or statistical independence. Actual model, reasoning and service tier remain UNKNOWN. The parent supplied no mathematical evaluation or expected verdict.

The PDF skill was used solely to inspect public primary evidence. No private manuscript, logs or archives were uploaded, no person contacted, no source script/validator executed, no installation or numerical root scan performed, and no source bytes edited. The audit neither repairs nor extends the theorem and does not treat d<=1/2, uniformity at that boundary, all trajectories, a second limit or RH. It is a mathematical review by one language agent, not a formal proof certificate. Prior-art conclusions and limitations are separate in PRIOR_ART_AUDIT.md. Local UTC records and hashes establish observable byte chronology only, not trusted notarization or private cognitive order.

STOP_FOR_SOL_REVIEW after the first final freeze.
