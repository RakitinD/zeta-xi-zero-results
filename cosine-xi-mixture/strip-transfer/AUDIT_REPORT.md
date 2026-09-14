# COSXI-STHC01 — first independent audit

## Decisions and exact objects

**S01-GLOBAL: PASS_AS_WRITTEN. S01 whole proof: PASS_AS_WRITTEN. S02-T: PASS_AS_WRITTEN. S02 whole text: MIXED_RESULT.** The component-hole sentence in S02 §4 has a false general geometric justification; its natural component-hole reading is recorded separately as FALSE_STATEMENT. It is unnecessary to the already written full-oriented-boundary proof. No alteration of either main theorem, numerical constant, parameter range or proof mechanism is required for these main decisions.

The exact source SHA256 values are S01 `06c9f892899fcd5dad742414746a87fbc06c5058baa67df6b3dee4198abdf616` and S02 `f2180957222c7cbba9d321cf1cc3dff141655f70efd250fb2335b919f95f1a7d`. Both complete proofs, including scope paragraphs, were read before phase 3. Copies remain unchanged under evidence/released_inputs/source/delivery/researchers/. The structured registry contains all 23 decisions. The proof, with its hypotheses, governs over abbreviated claim-matrix wording.

| Claim | Verdict | Audited scope |
|---|---|---|
| S01-TRANSFER | PASS_AS_WRITTEN | Supplied zero-free rectangle, value budget and positive derivative |
| S01-RIGHT-EULER | PASS_AS_WRITTEN | eta tends to zero with eta^(-2)=o(log lambda) |
| S01-LOG | PASS_AS_WRITTEN | Canonical log on the specified domain; estimates on its stricter band |
| S01-CONTROL | PASS_AS_WRITTEN | All eligible high-ordinate rays; bounded-band value estimate |
| S01-LOW | PASS_AS_WRITTEN | Fixed low-x region with unbounded sigma |
| S01-LOWER | PASS_AS_WRITTEN | Every eligible zero, including boundary zeros |
| S01-UPPER | PASS_AS_WRITTEN | Actual simple odd-phase root on one connected graph |
| S01-GLOBAL | PASS_AS_WRITTEN | Uniform all-root radial minimum and attainment |
| S01-ABOVE | PASS_AS_WRITTEN | Any positive eta_plus tending to zero, eventually at most 1/2 |
| S01-BELOW | PASS_AS_WRITTEN | Every 0<eta_minus<=beta(6lambda)/16 |
| S01-BELOW-ROOT | PASS_AS_WRITTEN | Strictly below Re w=1 at the maximal stated width |
| S01-MINIMIZER-PHASE | PASS_AS_WRITTEN | Every minimizing first-quadrant representative, phase index only |
| S02-A | PASS_AS_WRITTEN | Off-zero charts and supplied graphs; arithmetic sign condition remains conditional |
| S02-M | PASS_AS_WRITTEN | Stated distance-based minimum modulus and collar specialization |
| S02-E | PASS_AS_WRITTEN | Density charge, projection, diameter and containment |
| S02-DOMINATION | PASS_AS_WRITTEN | Exact Lambda(T) on all C minus E, including component boundaries |
| S02-T | PASS_AS_WRITTEN | Full relevant components and charged open/closed window counts |
| S02-P | PASS_AS_WRITTEN | Lifted path phase and full oriented boundary charge |
| S02-PAIRING | PASS_AS_WRITTEN | Arbitrary multiplicity-respecting matching in each full component |
| S02-G | PASS_AS_WRITTEN | Conditional lower count with one break penalty per supplied arc |
| S02-TOPOLOGY-SENTENCE | FALSE_STATEMENT | General component-hole inference; actual zeta realization is not asserted |
| S02-NONVACUITY | PASS_AS_WRITTEN | Parameter arithmetic only |
| S02-SCOPE-DISTINCTION | PASS_AS_WRITTEN | No unconditional positive-A graph supply or improved zeta bound |

## Exact normalization and analytic inputs

For z=i(w-1/2), the xi argument is 1-w, so reflection gives Xi(z)=xi(w). The cosine becomes cosh(w-1/2), whose zeros have Re w=1/2. Therefore P=xi/cosh is analytic on Re w>1/2, although it can vanish there. Both factorizations in the submissions are exact, since t exp(-lambda)=1-t. The nonzero factors and the affine map preserve analytic multiplicity. On a log chart, the entire zero condition is lambda+ell=(2m+1)pi i. There is no phase truncation.

Expanding the log-Gamma leading part and cancelling the two factors 1/2 gives (w/2)Log(w/a)+(3/2)Log w+c0 with a=2pi e^3 and c0=log(2 e^(1/2) sqrt(pi)). Its derivative is (1/2)Log(w/a)+1/2+3/(2w). The remainder is exactly the four terms in S01 (5); it is independent of lambda. At w=1, xi=1/2 and cosh(1/2) is nonzero, so P is regular and nonzero. The separated poles in (7) cancel and are not separately evaluated there.

DEPENDENCY_CHECK.md checks the original Q01/E01 domains afresh. The mandatory Bellotti and Simonic primary statements have been inspected in both versioned HTML and original PDFs, with the relevant PDF pages rendered and viewed. Their deep proofs are accepted as published theorem inputs, not re-proved. DLMF formulas were directly inspected. ARITHMETIC_INPUT_AUDIT.json records all 13 inputs and the precise mappings.

## S01 connected transfer

Write F=lambda+U and D=A+iB in coordinates w=sigma-ix. Analyticity gives F_sigma=A, F_x=B, V_sigma=B and V_x=-A. For each x, the lower value is negative, while the upper value exceeds -J+a0 h>0. A>=a0 gives a unique interior scalar solution. The implicit function theorem on an open neighborhood extends the graph at interval endpoints; uniqueness patches its local pieces. Along it, sigma'=-B/A and V'=-(A^2+B^2)/A<=-a0. An open phase interval longer than 2pi contains an odd multiple of pi, even if endpoints themselves are odd levels. At that interior crossing P' = P D is nonzero; the original mixture zero is simple. This proves S01-TRANSFER on exactly its conditional hypotheses, without a bound on B or a global injectivity assertion.

## S01 Euler-only moving range

E01's explicit M_(1+eta) is O(eta^(-1)) with an absolute constant: its first term is eta^(-1), the zeta-log term is at most log(1+eta^(-1)), and the other terms are uniformly bounded for 0<eta<=1/2. Its radius-eta/2 Cauchy argument uses Re w>=1+eta/2, giving K=O(eta^(-2)) and C_s=O(eta^(-2)). Thus X_s=exp(4C_s)=lambda^(o(1)) and M_s=o(lambda) under the submitted rate.

For rho=|w|, theta=arctan(x/sigma), the explicit real part has term (sigma/2)log(rho/a)-x theta/2+(3/2)log rho+c0. Since rho>=sigma>=1, theta<=pi/2, and sigma log(sigma/a)>=-a/e, it is at least -pi x/4-a/(2e)+c0. Subtracting M_s proves (13) at every height. Consequently lambda+U>0 for x<=X_s eventually, with no moving compact minimum. For larger x, A>=log x/4 on the whole ray. The boundary expansion (14) is uniform on 1<=s<=3/2. It forces x>=lambda/(2kappa), then x>=X_front-O(M_s+1). An upper rectangle with the §7 choices and budget a fixed multiple of M_s+1 has thickness O(eta^(-1)/log lambda)=o(1), supplies a simple phase hit, and has bounded height. The radial correction is O(1/lambda). The proof tracks every moving constant and establishes S01-RIGHT-EULER; this rate is not imposed on S01-ABOVE.

## S01 interior logarithm and explicit budgets

The decreasing positive beta makes Omega={x>4, sigma>1-beta(x)/2} simply connected via the displayed product-coordinate homeomorphism. Bellotti's zero-free region contains its closure locally with a strict margin; there is no pole there. A log exists and is uniquely fixed by its agreement with Euler log on the connected overlap. For h=beta(2x), x>=10, the radius-h/2 disk centered at 1+h/4-ix has x'<2x and left edge 1-h/4>1-beta(x')/2. Its real part stays above 3/4. These are neighborhood, not merely pointwise, conditions.

For sigma<=1 on that disk, Bellotti's value theorem with both constants rounded upwards gives the first term of M(x). For sigma>=1, partial summation with integer N=ceil(|Im w|) gives precisely (16). It follows either directly from the tail integral of floor(u)-N or from DLMF 25.2.8; the minus sign is correct. Here the finite sum is at most 1+log N, the rational term at most 1/|Im w|, and the integral at most |w|N^(-sigma)/sigma<=4. They fit 10 log(2x). At the center, the Euler normalization bounds |g(c)| by log(1+4/h).

Let f=g-g(c) and A0=M-Re g(c). If A0>0, Re f<=A0 implies |f/(2A0-f)|<=1. Schwarz on radius R=h/2 gives |f|<=2A0 r/(R-r); r=3R/4 gives |g|<=6M+7|g(c)|. If A0=0, the harmonic maximum principle makes f constant zero. Points with sigma in [1-h/16,1+h/2] are within 5h/16 of c, so their radius-h/16 circles stay within 3h/8. Cauchy yields Z=16H/h. For sigma>=1+h/2, a radius-(sigma-1)/2 Euler disk yields the derivative bound in the submission. This covers all sigma, with no phase ambiguity or pole crossing.

With L=log(2x), h^(3/2)L is a constant times (log L)^(-1/2). Thus M and G0 are O(1+log L), H=O(1+log log(2x)), and Z=O(L^(2/3)(log L)^(4/3))=o(log x). All constants are absolute. S01-LOG is a standard deduction from two distinct arithmetic inputs, not an improvement to either.

For S01-CONTROL, the remainder derivative losses besides g' are at most 10/x^2+2q0/(1-q0), q0=e^(-1/2). Re(3/(2w))>0 and Re Log w=log|w|>=log x. The stated C_E safely bounds the remaining constant losses for x>=10, giving (20); a fixed X0 works for every larger x because Z/log x tends to zero. For (22), the geometric errors are bounded by 5/x^2+log a+1+|c0|; the other non-g remainder losses are 1/(x-1)+1/(3x)+q0/(1-q0). Their sum is less than 20 on x>=10. The real-value band and the all-sigma derivative domain are correctly kept distinct.

## S01 low ordinates and every root

The polynomial 3+4cos(theta)+cos(2theta)=2(1+cos(theta))^2 makes the Euler logarithm nonnegative in combination (11). If zeta(1+i tau) had multiplicity m>=1 for tau nonzero, the simple pole at 1 and analyticity at 1+2i tau make its left side O((sigma-1)^(4m-3)), tending to zero. This contradicts its lower bound one. Completion handles tau=0. Thus P is nonzero on the fixed compact [1,S] by [0,X0]. Q01's whole-half-plane derivative estimate permits a fixed S>=2 with A>=1 for all sigma>=S and all real x. A small fixed left extension of that compact has |P| bounded below; integration from S extends the same bound to unbounded sigma. This proves S01-LOW without assuming uniform compact convergence on an expanding region.

For allowed s, beta(2x)>=beta(6lambda) on X0<=x<=3lambda, so s>=1-beta(2x)/16. Every eligible zero reflects to x>=0, sigma>=s. Low x is excluded, intermediate x uses A>0 along every height to force F(s,x)<=0, and x>=3lambda is radially farther than the eventual front. In the intermediate range, kappa x>=lambda+b log x-KQ_lambda first gives x>=lambda/(2kappa), then (25). This is S01-LOWER over the complete eligible zero set, with no exception count or height cutoff.

For S01-UPPER, eventually I is within [lambda,2lambda], L<=1 and s+h_lambda<=2, uniformly for the allowed s. On I, 0<=log(x/lambda)<=log 2 and b<=5/2, so the error plus b log(x/lambda) has magnitude at most M_lambda. Then the stated c_lambda and J_lambda give -J_lambda<=F(s,x)<=-2. Integrating A>=log(lambda)/4 through h_lambda gives F(s+h_lambda,x)>=1. The rectangle has a zero-free neighborhood inside Omega; its phase decrease is at least (log(lambda)/4)(16pi/log(lambda))=4pi. The transfer lemma provides an interior simple root with strict height excess less than h_lambda. Its radius differs from x by O(1/lambda).

All constants can be chosen before lambda and simultaneously in s. The lower and upper bounds give S01-GLOBAL, and the nonzero entire H_t has finitely many zeros in a disk containing the upper zero. Its nonempty eligible finite subset attains the infimum. This also handles boundary equality. No monotonic radial ordering is needed.

Every minimizing first-quadrant representative has x=X_front+O(Q_lambda), since its radius is bounded above by the constructed radius and below by (25). Thus F(s,x)=O(Q_lambda), and integration up to its actual sigma gives sigma-s=O(Q_lambda/log lambda). This derives bounded height; it does not assume it. The exact imaginary expression is

    -Im ell = (x/2)log(rho/a) + (sigma/2+3/2)theta - Im E.

On the now bounded sigma band it equals (x/2)log(x/a)+O(Q_lambda). Its sign is positive eventually. Hence the actual original odd phase is -i(2n+1)pi with n~lambda log(lambda)/pi^2, and D has positive real part at every such minimizer. This verifies S01-MINIMIZER-PHASE without a rank or trajectory assertion.

S01-ABOVE and S01-BELOW are substitutions into the same uniform theorem. At maximal eta_minus, h_lambda/eta_minus=O((log lambda)^(-1/3)(log log lambda)^(4/3)) tends to zero, proving S01-BELOW-ROOT for the mixture. No strict-below-one root is claimed for every arbitrarily smaller eta. The O(log log lambda) error resolves the full logarithmic term but may conceal its tiny moving correction.

## S02 charge and geometry

Simonic's Theorem 1 has s in [1/2,0.831], Y>=H0, strict beta>s, and the displayed four constants. Its standard zero count carries multiplicity: the underlying Littlewood integral in §4.2 weights each local zero by its order. No literal word “multiplicity” was found in the PDF text search; the checked zero-counting identity, not an invented quotation, fixes the convention. Section 4.5 explicitly treats boundary heights by continuity. The source is accepted at its theorem statement; the arithmetic proof is not re-audited.

Here s0=1/2+delta/4 is strictly below every included center real part and below 5/8. For T>=2H0, [T-2,2T+2] is strictly contained in (T/2,4T); conjugation preserves multiplicities. The three intervals (T/2,T], (T,2T], (2T,4T] telescope without endpoint loss. Their exponent is 1-(s0-1/2)/4=1-delta/16. This proves M<=Q_delta(T) using exactly three valid source applications.

There are at most M disks; their diameters sum to less than 4rM. A simple chain of overlapping disks joining two points gives component diameter at most twice the radii sum, hence at most 4rM_j. Closure does not enlarge that bound. If its closure meets Omega, a point of intersection is at least h and 1 from the respective collar edges. Hypothesis (3) therefore puts the entire relevant closure in int C. When M=0 there are no components. General-position choices avoid tangencies and triple intersections; the finite piecewise smooth domain boundary may have several circuits. These are S02-E's claimed conclusions; simple connectivity is never required.

## S02 minimum modulus

For z0=2-ix and |u|<=15/8, Re(z0+u)>=1/8 and the pole at 1 is outside. Formula (13) is (16) with N=1. Its elementary absolute estimates, using |s|<=2T+4.875 and |Im s|>=T-2.875, give at most 100T for T>=10 (even the bound (2T+4.875)/(T-2.875)+8(2T+4.875) is below 100T). At the center, the reciprocal Euler series gives |zeta(2-ix)|>=1/zeta(2)>1/2; integral comparison already gives zeta(2)<2.

Jensen on an outer radius tending to 15/8 bounds each zero at radius at most 7/4 by a contribution at least log(15/14), hence n<=log(200T)/log(15/14). Boundary zeros are handled by limiting radii; the nonzero center prevents a zero at radius zero. Choose R in (13/8,7/4) avoiding zeros. Division by the finite Blaschke product cancels exactly its interior zeros, with orders; its denominator has no poles in the disk and its boundary modulus is one. The quotient g is analytic and zero-free on a neighborhood of the closed disk, |g|<=100T and |g(0)|>1/2.

The nonnegative harmonic function log(100T)-log|g| satisfies the Poisson/Harnack factor (R+3/2)/(R-3/2)<25. At the target u=sigma-2, |u|<=3/2. Each Blaschke factor is at least |u-alpha|/(R+|u|)>=d/4. Multiplying, applying the zero-count bound and dropping the positive log(100T) proves (12). This checks both multiplicity and the explicit constants, not just its asymptotic shape.

For a point of C minus E, included zeros are farther than r because every selected disk radius exceeds r. An omitted nontrivial zero is separated by at least h in real part or 1 in ordinate. Trivial zeros are farther away. Since Q>1 and 4rQ<h, r<h. Thus (12) with d=r yields -F(T), also when M=0. This proves S02-M uniformly on the full retained collar.

## S02 domination and cluster transfer

The log-Gamma formula (17) has the correct negative term -x theta/2. On C, 1/2<sigma<17/8, x>=T-1 and |w|<=3T. Since log(|w|/2)>=0, its potentially negative coefficient is at least -1/4, and theta<=pi/2. The completion factors satisfy |w|,|w-1|>=1 and |cosh(w-1/2)|<=exp(sigma-1/2). The total discarded negative constants are bounded by log 2+(17/16)log pi+17/16+13/8+1<6. These give (18). Combining with -F(T) and x<=2T+1 proves exactly (19) under lambda>=Lambda(T), including every relevant component boundary. This is S02-DOMINATION.

Every zeta zero in C is a selected disk center, and every zero of xi there is a zeta zero of the same order. A center lies in exactly its own connected component of E. Therefore the zeros in U_j number M_j, irrespective of anything in a bounded complementary hole. P+vc, 0<=v<=1, is nonzero on the full boundary by |c/P|<=1/(4T)<1. The integer argument-principle integral over the full domain-oriented boundary varies continuously with v and is consequently constant. It counts exactly the domain U_j: outer counterclockwise and inner clockwise curves cancel all winding about excluded holes, including any nested component. This is the full-boundary homotopy already explicitly written in §4, not a replacement argument added by this audit. CHALLENGE_RESPONSE.md explains the redundant false aside separately.

Consequently P+c and xi have M_j zeros in every full relevant component, and none on its boundary. By domination all mixture zeros of the closed window are in that union. A relevant component whose closure avoids the window boundary is entirely inside the open window; this follows by connectedness, since leaving would require meeting the boundary. It contributes equally to the two counts. Each component meeting the boundary contributes two partial counts in [0,M_j], so the discrepancy is at most M_j, not 2M_j. Summing proves both open and closed charged inequalities, their uncharged equality when B=0, and N_H<=Q. An arbitrary multiset bijection in U_j has distance at most its diameter. This proves S02-T and S02-PAIRING, without matching only the zeros retained by the original rectangle.

## S02 phases, conditional arcs and nonvacuity

The power series q_lambda=Log(1+c/P) is globally single-valued where |c/P|<1. On the retained collar its modulus is at most (1/(4T))/(1-1/(4T))<=1/(3T). The quotient H_t(i(w-1/2))/(t xi(w))=1+c/P then gives the exact endpoint difference of phase changes in (22). Arbitrary additive lift constants cancel; the error is at most 2/(3T), with no path-length factor, and is zero on closed paths. Residues of D=P'/P are the analytic multiplicities. Full component cycles have period 2pi i M_j; repeated paths must use their winding indices. “One circuit” in the claimed charge has the explicit full-oriented-boundary meaning fixed in the theorem and reports, not just an outer Jordan curve. S02-P passes on that scope.

For S02-A, differentiating the normalized Stirling formula gives psi(w/2)=Log(w/2)+O(1/|w|) using the verified sector Cauchy estimate. On fixed C, log|w|=log T+O(1), rational terms are bounded, and |tanh(w-1/2)|<=coth(3delta/4). Hence the non-arithmetic remainder in (24) is bounded by an effective C_delta. The lower condition (25) does imply A>=kappa log T. The registry phrase “zero-free collar” is qualified by its own off-zero hypothesis and by the actual proof's local chart scope; the entire C is not asserted zero-free.

On each supplied C1 graph the same chain rule as in S01 gives phase decrease at least kappa ell_j log T. An open interval of length L contains at least L/(2pi)-1 odd levels, and every crossing is simple because P D is nonzero. Pairwise disjoint arcs give different points. Summation proves S02-G's lower bound with -J, including endpoint exclusions. It provides neither an upper equality nor any arcs. In fact (19) forces lambda+log|P|>=log(4T)>0 on C minus E, so no balanced arcs occur there in the transfer regime. This proves the S02-SCOPE-DISTINCTION item.

For delta=1/4 and T=e^2000, q=63/64. The three leading terms of Q/T are less than 10395.2*4*2001*e^(-31.25)<10^8 e^(-31.25)<5*10^(-6), using 27^31>2*10^44 and e>2.7. The other terms are below 10^8 e^(-2000)<10^(-592), since 2^2000>10^600. Thus Q/T<10^(-5); 4rQ<4*10^(-5)/T<h=1/16 and T>=2H0. This verifies S02-NONVACUITY by parameter arithmetic, without evaluating zeta or scanning roots.

## First issue, late comparison and limits

No first invalid mathematical line was found in S01. For S02 the first identified defect is the §4 sentence after the already completed full-boundary homotopy, claiming holes contain no zeta zero merely because every such zero in C is a disk center. Membership in E does not imply membership in the surrounding component. The general inference fails for a ring and a separate disk inside its hole. The literal natural component-hole statement is rejected on that geometric reading; this audit does not exhibit an actual zeta configuration. The corrected complementary-set interpretation is discussed in CHALLENGE_RESPONSE.md and is not silently substituted into the source. The main argument has no dependency on the aside; no main claim is weakened or rescued by a new proof.

The later author reports and dependency maps agree with the substantive limitations already seen in the full proofs. Their ledgers disclosed additional related leads, not extra operative arithmetic inputs. Earlier QHC01/EHC01 verdicts agree on the necessary original normalization and remainder domains; their PASS labels were not premises for the moving or expanding-domain claims. The preserved administrative flags are documented in DEPENDENCY_CHECK.md. They remain historical flags; nothing was edited to clear them and they do not themselves establish a mathematical defect or hidden reading behavior.

The three early snapshots remain byte-identical. ROOT supplied access releases and hashes, not a mathematical expectation. The late topology question agrees with the concern already written in PHASE2_NOTES.md; hashes support observable byte chronology only. Actual hidden model, reasoning and service tier are UNKNOWN. No child, replacement, source edit, historical script, root scan, private upload or external contact was used. Public PDFs and pages were retrieved through authorized direct downloads after sandbox authentication failures; no access blocker remains for the mandatory sources. Rendered source pages were visually inspected. Full mathematical formalization, exhaustive historical priority and hidden cognitive/statistical independence are not certified. No supplied completed-output validator was run by this auditor.

S01 proves a uniform mixture radial theorem using a narrower known zero-free region. S02 proves an expanding-window mixture count and phase theorem using a known density saving. Neither supplies a new zeta bound, RH, zero simplicity, or unconditional positive-A moving graphs. PRIOR_ART_AUDIT.md states the bounded comparison separately.

STOP_FOR_SOL_REVIEW after the first final freeze.
