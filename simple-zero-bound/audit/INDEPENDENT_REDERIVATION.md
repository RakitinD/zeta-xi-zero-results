# PGF-HC01 independent rederivation

This document records the single critic's reconstruction in the required K1–K16 order. It is a proof audit of the frozen m=492 separator, not a search for a replacement theorem. The Phase-0 risk, dependency and rederivation documents were reread and hash-checked before the author proofs. In particular, the tail-profile formula below was independently proposed in Phase 0, before access to PGF-B. Author statements, old verdicts and the author verifier are not premises establishing the new mathematics.

The exact reconstruction program was completed and sealed before its first execution, then executed through local, plane and final stages. Its complete final receipt was sealed before the first read or execution of `verify_fusion.py`. The separate clock and hash records give the ordering. The program uses only integer and Fraction arithmetic for decisive comparisons. Decimal strings are orientation only. It neither calls an optimizer nor replays the retained universal local computation.

## K1 — Primary signed state: PASS

Fix a real even smooth eta supported strictly inside I=[-1/2,1/2], with integral eta²=1. Let f=eta² and K=f-hat with Fourier exponent -2 pi i z u. Work in the real Hilbert space of complex-valued functions h satisfying h(-u)=conjugate(h(u)). Its usual complex L² inner product is real on this subspace: conjugation followed by u→-u proves this directly.

Put v_z(u)=eta(u) exp(-2 pi i z u). For real x, v_x is a unit vector of the real space. For a nonreal conjugate pair define g=(v_z+v_bar(z))/2 and h=(v_z-v_bar(z))/(2i). Both belong to the real space. Expanding the norms, using <v_z,v_bar(z)>=K(0)=1, gives ||g||²-||h||²=1. A pair of multiplicity q therefore contributes the real self-adjoint operator 2q(gg*−hh*) of trace 2q. A real point of multiplicity q contributes q vv* of trace q.

Sum these operators to obtain A. Let P comprise all s simple-real summands, write A=P+Q, and let V have exactly those s unit columns. Then P=VV*, M=V*V is exactly the full simple-real Gram, tr M=s and tr A=N, where N counts total multiplicity. No local subset, old sampled operator, dyadic denominator or historical seven-term window is involved.

The coefficient tensor of A in a real orthonormal basis is the tensor sum of v_z(u)v_z(v), with multiplicity. Its complex L² norm squared is the Hilbert–Schmidt norm squared of A. Expanding the tensor norm gives a sum with conjugate arguments; reindexing the conjugation-invariant second multiset turns it into sum K(z-z')². These are analytic squares, not an illicit replacement by |K(z-z')|². This also establishes that the total analytic sum is real and nonnegative.

If r counts distinct multiple-real points and p counts distinct nonreal conjugate pairs, Q has r+p positive summand directions. It is nonpositive on their orthogonal complement, so beta=rank Q_+≤r+p. Multiplicity gives N-s≥2(r+p). Thus q0=N-s-2beta≥0 is legitimate without a stronger rank assertion.

The stronger beta=r+p also holds here. A finite linear relation among the v_z, divided by eta on a positive-measure nonzero set, gives an exponential polynomial zero on a set with an accumulation point. Analyticity and its derivatives give a Vandermonde system for distinct exponents, hence all coefficients vanish. Passing between a conjugate pair and g,h is invertible. Q on the span of its summand vectors is congruent to the real diagonal coefficient form; Sylvester inertia gives r+p positive and p negative directions. Extra simple directions add zero eigenvalues to Q. Therefore q0 equals sum over multiple real points of (q-2), plus twice the sum over nonreal pairs of (q-1). The proposed trace and rank-error variables vanish by exact identities, not by discarding adverse errors.

This reconstructs Proposition 3.2 on the source state. The functional equation maps a zero rho to 1-conjugate(rho), so z_rho=-i(rho-1/2)log(T)/(2 pi) has the required conjugation symmetry. Its simple real elements are precisely the scaled simple critical-line ordinates.

## K2 — Residual identity and one budget: PASS

All operators below are restricted to a finite common span; identity operators and support projections use that span. Set C=Q_+, H=Q_-, L=(P-2I)_+, R_P=(2I-P)_+, and Pi_C the support of C. Thus CH=0 and L-R_P=P-2I. Define

    W=||C-2 Pi_C||²,
    J=||H-L||²+2 tr(R_P H),
    Z=2 tr(PC),
    Y=2q0+W+J+Z.

All terms are nonnegative. The trace of a product of two positive operators is nonnegative without commutation, since it is the trace of U^(1/2) V U^(1/2).

Direct expansions give

    ||A||²=||P-H||²+||C||²+Z,
    ||P-H||²+4 tr H=tr(P²-L²)+J,
    ||C||²=4 tr C-4 beta+W.

Write Phi(t)=(t-1)²-(t-2)_+², and D=tr Phi(M), retaining all s Gram eigenvalue slots. The function t²-(t-2)_+² vanishes at zero, so transferring the nonzero spectra of P and M is legitimate and gives

    tr(P²-L²)=2 tr M-s+D=s+D.

Combining the expansions with tr C-tr H=N-s yields

    ||A||²-2N+s=D+2(N-s-2beta)+W+J+Z=D+Y.

Thus fixed-function unweighting supplies the single budget hN+D+Y≤s+o_f(N), once h≤2-C(f). If a principal simple Gram compression M_circ is introduced, define X_arith=Y+D-D_circ. Then D_circ+X_arith=D+Y exactly. X_arith is not an additional budget alongside D+Y. The frozen winning route uses full D and Y, so no such compression credit appears in it.

The normalization term -s matters: Phi(0)=1. One cannot replace D by a sum over just the nonzero Gram eigenvalues in a general identity. The exact realization has independent simple columns, but the algebra above also handles singular abstract Gram matrices correctly.

## K3 — Quotient and trace-refined perspective: PASS

Let k=rank L and ell=tr L. The trace identity is

    tr C-2beta=tr H+q0.

Cauchy–Schwarz on the beta-dimensional support gives tr H+q0≤sqrt(beta W). If Pi_L supports L, positivity of H gives

    ell-tr H≤tr(Pi_L(L-H))≤sqrt(k)||L-H||≤sqrt(kJ).

Adding gives ell+q0≤sqrt(beta W)+sqrt(kJ). Therefore

    W+J≥(ell+q0)²/(beta+k),
    Y≥2q0+Z+(ell+q0)²/(beta+k).

The convention is a²/0=+infinity for a>0 and 0/0=0. On an actual state beta+k=0 forces ell+q0=0 by the preceding inequality. No arbitrary positive numerator is allowed at a zero denominator.

For the refinement keep T_H=tr H≥0 before adding the inequalities:

    W≥(T_H+q0)²/beta,
    J≥(ell-T_H)_+²/k.

For positive denominators, the minimizer over T_H≥0 is (beta ell-k q0)/(beta+k) when that value is nonnegative; it lies at most ell. The minimum is then (ell+q0)²/(beta+k). Otherwise T_H=0 is minimizing, giving q0²/beta+ell²/k. This proves the two branches, with the perspective extension at boundary denominators. When beta=0, T_H=q0=0; when k=0 on a finite state, ell=0. The refinement exceeds the coarse quotient on its second branch by (k q0-beta ell)²/[beta k(beta+k)].

Every Young support follows by the square

    (ell+q0)²/B - t(ell+q0)+t²B/4 ≥0,  B=beta+k.

It follows that Young, quotient and refined quotient are alternate restrictions of the same W+J. A lower bound on any one of them is not an extra residual payment.

## K4 — Global spectral and coupled region: PASS

The full M has trace s. Its k eigenvalues above 2 sum to 2k+ell≤s. Their contribution to D is k+2ell. The remaining s-k eigenvalues have deviations from one summing to -(k+ell). Thus

    D≥k+2ell+(k+ell)²/(s-k).

Here k<s if s>0; the empty s=0 state has D=k=ell=0. This is a full-spectrum trace argument, not pinching of a count of eigenvalues above 2.

On a common normalized subsequence write x=s/N, u=k/N, v=ell/N, w=beta/N, c=q0/N=1-x-2w, d=D/N, y=Y/N and z=Z/N. The necessary region is

    h≤x≤1; u,v,w,c,d,y,z≥0; 2u+v≤x;
    d+y≤x-h;
    d≥F(x,u,v)=u+2v+(u+v)²/(x-u);
    y≥2c+z+(v+c)²/(u+w).

One may retain the trace-refined infimum in the last line. Since 2u≤x and x≥h>0, x-u is bounded away from zero. Nonnegativity and the budget bound d,y,z; v is bounded by the trace and w,c by counting. The additional trace variable is bounded by tr H≤sqrt(beta W), so a joint subsequence is available. At a vanishing perspective denominator, the numerator must vanish; the lower-semicontinuous extension preserves the constraint. A normalized u=0 does not imply v=0: sublinear rank may carry order-N tail. No false boundary restriction of that kind is used.

For an independent check of the bare rank projection, discard the nonnegative tail in F to get u≤x(x-h)/(2x-h), and use w≤(1-x)/2. Then

    u+w≤B_h(x)=((2-h)x-h)/(2(2x-h))≤(1-h)/(2-h).

The derivative of B_h is positive for 0<h<1. Since h>2/3, the final upper bound is strictly below 1/4. An eventual finite beta+k≤N/4 can be justified with a fixed h' in (2/3,h) before the height limit, so it does not feed a proposed final proportion back into its own premise. The winning nonlinear route uses the coupled region itself and does not require this finite rank shortcut.

Rank pinching would be false: a six-point Gram sufficiently close to the all-ones matrix has one eigenvalue above 2, while both principal three-point blocks have one each. Consecutive points separated by a sufficiently small positive spacing give such a same-kernel example by continuity. Our transport uses convex Phi_rho, for which trace pinching is valid, and never uses the high-count analogue.

## K5 — Independent nonlinear residual payment: PASS

Drop c,z and enlarge w in the quotient denominator to (1-x)/2. These changes weaken necessary constraints in the allowed direction:

    F(x,u,v)+y≤x-h,
    y≥v²/[u+(1-x)/2].

Put q=u+(1-x)/2, a=(1+x)/2, t=2x-h, N_x=a t-x²=((2-h)x-h)/2 and A_x=t+rho x. Both N_x,A_x are positive for h≤x≤1, 0<h<1. If q=0, the perspective forces v=0 and y-rho v≥0. Otherwise sigma=v/q≥0 and x-u=a-q>0. Expanding the budget gives

    q(t+2x sigma+a sigma²)≤N_x.

Define p=(sqrt(A_x²+rho² N_x)-A_x)/2≥0, so p²+A_x p=rho² N_x/4. At rho=0, p=0. If sigma≥rho, then y-rho v≥q(sigma²-rho sigma)≥0. For 0≤sigma<rho take mu=p/N_x. The polynomial

    (1+mu a)sigma²+(2mu x-rho)sigma+mu t

has positive leading coefficient and discriminant rho²-4mu A_x-4mu²N_x=0. It is nonnegative. Divide by t+2x sigma+a sigma²>0 and multiply the resulting upper bound for the nonnegative numerator rho sigma-sigma² by the bound on q. This gives q(rho sigma-sigma²)≤p, hence

    y-rho v≥-p_h(x;rho).

This derives G6 directly from the actual coupled state. It need not assert that the relaxed minimizer is a realizable zero configuration, or that it is optimal over every physical constraint. The theorem needs a valid lower bound only.

Implicit differentiation gives (2p+A_x)p'=rho²(2-h)/8-(2+rho)p. For rho>0, p<rho²N_x/(4A_x), and

    (2-h)A_x-2(2+rho)N_x=h(h+rho)>0.

Therefore p'>0. For rho=0 it is constant. This is a domain-wide proof of the endpoint use in K13, not a numerical test near the proposed bound.

## K6 — Tail-aware six-band profile: PASS

For a positive m by m unit-diagonal Gram M, put X=M-I, and denote its zero-diagonal six-band part by T_band to avoid confusing it with residual Y. Then tr X=tr T_band=0, tr(T_band X)=||T_band||²=E. For a unit vector u with p_i=|u_i|², and masses P_c in the seven residue classes, Cauchy–Schwarz gives

    |u* T_band u|²≤E·2 sum_{1≤j-i≤6} p_i p_j
                 ≤E(1-sum_c P_c²)≤E/(7/6).

There are no same-residue six-band edges. This proof applies to complex Hermitian Grams. Write tau=7/6, r=sqrt(E/tau), c=1+rho/2. Let Phi_rho(t)=Phi(t)+rho(t-2)_+, rho≥0, and phi_rho(x)=Phi_rho(x+1) for x≥-1. For any a≤2+rho,

    phi_rho(x)≥a x-a²/4.

For x≤1 the difference is (x-a/2)². For x≥1 it is (2+rho-a)x-(1+rho)+a²/4, which is minimized at x=1 and equals (a-2)²/4 there. Negative a presents no problem. The derivative of Phi_rho jumps upward by rho at 2; it is convex.

Take any Hermitian A0≤(2+rho)I. In its eigenbasis, scalar Jensen applied to the spectral measure of X, followed by the scalar bound above, gives

    tr Phi_rho(M)≥tr(A0 X)-||A0||²/4.

No simultaneous diagonalization is assumed. Choose A0=2alpha T_band-d I, alpha≥0, d=2(alpha r-c)_+. Its top eigenvalue is at most 2c. The trace-zero identities then give

    tr Phi_rho(M)≥(2alpha-alpha²)E-m(alpha r-c)_+².

If r≤c, alpha=1 gives E; the expression cannot exceed E since the subtracted terms are nonnegative. If r>c, the maximum of the active quadratic occurs at alpha=(E+m c r)/(E+m r²). It lies in the active domain because alpha r-c=E(r-c)/(E+m r²)>0. The inactive part increases up to alpha=c/r<1; the active derivative remains positive at that boundary and then decreases to zero. Thus this critical point maximizes the full piecewise expression. Substitution yields

    G_{m,rho}(E)=E,                                      E≤tau c²,
    G_{m,rho}(E)=[E+m(2c sqrt(E/tau)-c²)]/(1+m/tau),     E>tau c².

The nonlinear derivative is [1+m c/sqrt(tau E)]/(1+m/tau), positive and decreasing, and equals 1 at the transition. Values agree there. Hence the profile is increasing, concave and continuously differentiable. At E=0 the expression is well-defined by the linear branch. At rho=0, c=1 and this is exactly the source Lemma 4.2, including its transition tau. This derivation is not limited to rewards below 2; the earlier Phase-0 risk about importing an incompatible low-reward seed is resolved by the explicit derivation.

## K7 — All 69 reflected trimming rows: PASS

The imported local premise is nine universal inequalities F_j(g)≥epsilon_j on nonnegative six-gap vectors for the exact 25-term kernel K0. The base singleton target is epsilon=15729481/2000000000; its three-consecutive-window aggregate is at least 3eta, eta=78681/10000000. The latter follows from the source compatibility mechanism: if any constituent is at least 3eta-2epsilon, the other two singleton bounds suffice; otherwise all three lie in the certified sublevel covers, whose exact overlap join and restricted eight-gap verification imply the triple bound. That universal cover computation is a retained imported premise. It was not freshly certified here.

The triple's pair and pressure coefficients are literally one third the sum of three translates of the base coefficients. The independent program verifies this identity against the original restricted candidate, including all pair positions, pressures and the window. Consequently the sum of three F's has target 3eta and does not create pair spans seven or eight merely because its point union has nine points.

At m=492 let n=m-6=486 possible seven-point starts. A trim (a,b) retains starts a through n-b-1. Group this consecutive interval into floor((n-a-b)/3) triples and its remaining singleton starts. Its base target is

    T_base(v)=3 floor(v/3)eta+(v mod 3)epsilon,  v=n-a-b.

For nonbase rows T_j(v)=v epsilon_j. Reflect the trim to (b,a), and average with weight 1/2. Reflection of the primary coefficients is exact. Let d_{j,k} be the pressure prefix through k, zero for k<0. For the outer gap type k=0,...,4 the averaged coefficient is [d_{j,k-a}+d_{j,k-b}]/2. Every interior type-5 coefficient is at most the full sum d_{j,5}; raising it to that envelope weakens the lower-bound inequality on nonnegative gaps, so it is legal.

With E the one common band energy, e=E/n, S_k the sum of the two outer gaps of type k<5 and S_5 the sum of the remaining gaps, define u_k^loc=B S_k/n. Every generated row is

    e + sum_{k<5} [d_{j,k-a}+d_{j,k-b}]/(2B) u_k^loc
      + d_{j,5}/B u_5^loc ≥ T_j(n-a-b)/n.

Keep 21 unordered base trims 0≤a≤b≤5 and six symmetric trims for each of eight other rows: 21+8·6=69. For a nonbase row the target is linear in the number of starts, so an asymmetric row is the mean of its two symmetric counterparts. Keeping only the symmetric ones loses no needed asymmetric inequality. For the base, the triple remainder prevents that simplification in general, and all 21 are retained.

No floating dominance deletion is needed for this audit. Each row is derived independently on the same actual coordinates; their simultaneous imposition is intersection, not an addition of 69 copies of energy. There is no new claim about all possible heterogeneous packets.

## K8 — Physical pair and gap capacities: PASS

For each primary case j and each span l=1,...,6, the exact nonnegative pair coefficients satisfy sum_{q-p=l} a_{j,pq}=2. A full chain of translated windows therefore places at most coefficient 2 on any fixed ambient pair. Trimming only removes nonnegative contributions; averaging a trim and its reflection preserves the bound.

The independent program does not accept this argument only as a summary counter. For each of all 69 actual m492 templates it constructs the twice-weight occupancy of every start: 0, 1 or 2. It translates every one of the 21 primary pair coefficients into actual ambient (i,j) coordinates and accumulates integer numerators. It separately translates all six pressure coefficients into each physical elementary gap. It then checks every ambient pair of each span one through six, and checks that no other span occurs. It verifies load≤2 and exact outer/enveloped inner gap charges.

The first local receipt records 202,239 physical pair positions and 33,879 gap positions checked, all passing. The six maximum span loads for every row, all 69 reconstructed coefficient vectors and thresholds, raw versus envelope costs and individual triple/singleton counts are included in the deterministic receipt. The canonical reconstructed-row-data hash is d097afba9975145a02ba80e5fe940cd50ee5fe1a86ed1aa7475314a3eb0aa149.

The later Farkas weights do not represent extra physical packets. They combine already valid necessary inequalities on a common seven-dimensional point, and their total energy coefficient is separately bounded by the objective coefficient in K10. This distinction prevents a hidden capacity overspend.

## K9 — m492 bookkeeping and pressure: PASS

Here m=492, n=486. The untrimmed base interval has 162 complete triples and no singleton. Every trim uses its own v=486-a-b and its own quotient and remainder; replacing every trim target by v eta would be wrong. The exact program recomputes the 21 base values separately.

There are 491 elementary gaps. Gap types 0,...,4 have multiplicity two, and type 5 has 492-11=481. Thus the full shift tax, after a local plane has selected six prices, is

    P_price=B(2 sum_{k=0}^4 t_k+481 t_5)
           =47854801908769656526884823/25000000000000000000000000.

The frozen prices, rho, reward and h are bound in the independent program and receipt. Since n u_k^loc=B S_k, the local plane's pressure n sum t_k u_k^loc is precisely B sum t_type gap. There is no extra 1/n, 1/1000 or 1/m at this step. The 1/m appears only when all offsets are averaged.

The raw sum of a template's translated pressure can be strictly smaller than the six-type envelope. It is checked as a diagnostic but is not substituted into P_price. The latter pays the actual physical position-price rule of the final block inequality.

## K10 — Whole-polyhedron plane and unbounded rays: PASS

Let z=(e,u_0^loc,...,u_5^loc)≥0 and let A_j z≥b_j be the 69 reconstructed normalized rows. We must prove G_{492,rho}(486e)+486 sum t_k u_k^loc≥R on the entire polyhedron. Completeness of a floating vertex list is not assumed.

The frozen certificate supplies 464 rational energy knots, beginning at zero and strictly increasing, with lower ordinates y_i. The independent program checks y_i≤G(E_i). On the linear branch this is y_i≤E_i. On the nonlinear branch rearrange to sqrt(E_i/tau)≥q_i, where

    q_i=[(1+m/tau)y_i-E_i+m c²]/(2m c).

If q_i≤0 this is automatic; if positive it is equivalent to q_i²≤E_i/tau. The sign is checked before squaring. The result is 95 linear endpoint checks and 369 nonlinear checks, all passing (none of these nonlinear cases used the automatic branch).

For each adjacent pair, independently reconstruct its chord a_i E+b_i from the two rational endpoints. Concavity and the endpoint bounds show that this chord lies below G on that interval. The last line is the constant y_last, which lies below G on the whole unbounded ray by monotonicity. One should not claim that every chord extension is globally below a concave function; that would be false. Only interval-wise coverage is used.

For every one of the 463 chords and the final constant line, verify its supplied nonnegative weights lambda_j over the independently reconstructed rows and the exact component inequalities

    sum_j lambda_j A_j ≤486(a_i,t_0,...,t_5),
    b_i+sum_j lambda_j b_j ≥R.

Multiplying coordinatewise dominance by z≥0 proves line_i(486e)+486 sum t_k u_k^loc≥R for every feasible z. Choose the particular line that is below G at the actual energy. This proves the desired nonlinear plane everywhere, including every recession direction, without an energy cap or vertex enumeration.

All 1,279 dual weights are nonnegative. The minimum coordinate slack is zero, which is legal for a non-strict dominance inequality. The minimum reward slack is the strictly positive rational

    1040175321787158388819576077945708381 /
    17608712849315307694675787110000000000000000000000.

The last energy is 31702987467/5000000000, followed by an explicitly certified constant ray. The plane receipt was sealed before the independent final endgame execution and before any author verifier read. No certificate repair, new line, new dual solution or optimizer was used.

## K11 — Fixed smoothing, offsets and analytic transport: PASS

For rho≥0 the scalar Phi_rho is nonnegative and convex on [0,infinity). Choose eigenbases in disjoint principal blocks of a full Gram M, extending them by zero. Jensen for M in each of these vectors, and summation, gives tr Phi_rho(M)≥sum_blocks tr Phi_rho(M_block). Omitted endpoint indices may be included as extra blocks and then discarded using nonnegativity. This transports D+rho ell, not k.

The plane therefore gives for any exact K0 m-block

    D_rho(M_block)+B sum t_type gap ≥R.

For a set of s ordered points in an interval of length L, use each of the m starting offsets. Each offset has at least s/m-2 complete blocks. Any global elementary gap appears at any one fixed internal block position at most once across all offsets; all prices are nonnegative. Summing and dividing by m yields

    D_rho(M)≥R s/m-P_price L/m-2R.

The weak endpoint count remains valid when s<m, including the empty matrix. The pressure uses a containing interval of length L; equality of the simple points' occupied span to L is unnecessary.

For smoothing choose fixed even cutoffs chi_delta and normalize f_delta=chi_delta² f0/Z_delta, eta_delta=chi_delta sqrt(f0)/sqrt(Z_delta). Positivity of f0 on I makes eta_delta smooth with compact support inside I. Convergence holds in L¹ and L², hence C(f_delta)→C(f0), and ||K_delta-K0||_infinity≤||f_delta-f0||_1→0 on the real axis. For a fixed m-block the Gram Hilbert–Schmidt error is at most m times that last quantity. On PSD spectra Phi_rho has Lipschitz constant 2+rho. Ordered-eigenvalue perturbation and Cauchy–Schwarz give

    |D_rho(M_delta)-D_rho(M_0)|
        ≤(2+rho)m^(3/2)||K_delta-K0||_infinity=:a_delta→0.

Thus the reward becomes R_delta=R-a_delta while the physical pressure is unchanged. Choose delta fixed and sufficiently small that R_delta>0 and 2-C(f_delta)>h. The latter is available because H(f0)>h strictly, independently checked below. Then take T→infinity. The containing interval is (0,L_T], L_T=T log T/(2 pi), so L_T/N(T)→1 by the imported Riemann–von Mangoldt input.

The analytic equality is independently reduced to the precisely stated weighted theorem in the original source: with Q=f*f and L=log T,

    K(z)²=w(rho-rho') [ Q-hat(z)-Q''-hat(z)/(4L²) ],
    z=i(rho-rho')L/(2 pi),  w(v)=4/(4-v²).

This follows from Q''-hat(z)=-4 pi² z² K(z)² and cancellation of 1-v²/4. Q and Q'' are fixed smooth even functions supported strictly inside [-1,1], so both satisfy the imported weighted pair-correlation theorem. The second term is O_f(L^-2)N, and the first constant is C(f). Evenness removes the sign difference in z. This proves the needed fixed-function unweighting from that external theorem; no T-dependent test function is used.

On each fixed smoothing's joint limiting state the local bound uses R_delta. To finish one may either pass delta→0 only in the scalar inequality for a fixed limiting count proportion x, or use the strictly positive margin of K13 to choose a single sufficiently small fixed delta at the outset. Spectral variables need not converge uniformly across different smoothings, and no global large-dimensional spectral continuity estimate is assumed. In the second route choose a_delta s0 less than the final margin. The same budget argument excludes x≤s0 for that one fixed smooth state.

The strict window margin was also independently reproduced. If a=1/sqrt(2), A=sin(a)/a and v(t)=cos(sqrt(2)t)+sum_{j=1}^{24} c_j cos(2 pi j t), then f0=v/A on I. Direct integration of (I+D)cos(omega t), with Dq(t)=integral |t-u|q(u)du, makes the sqrt(2) mode constant and removes its cross terms with the zero-integral integer modes. Orthogonality gives

    H(f0)=3/2-cos(a)/A
          -A^-2 sum_j c_j²/2 ·(1-1/(2j² pi²)).

The fresh program bounds cos(a) and A by alternating rational series (even final index 40 gives the upper bound, odd 41 the lower), and bounds pi by Machin's identity 16 atan(1/5)-4 atan(1/239), using indices 80 and 81. It uses the upper pi in the increasing correction, the lower positive A in denominators, and the upper cosine in the negative term. It proves v>0 and a rational H_lower>h>2/3. The exact rational gap is in the receipt; its orientation is 1.7542285707062155e-16. This is a fresh rational enclosure of the fixed window, not a new universal local gap certificate.

## K12 — Winning dependency closure and one-spend ledger: PASS

The winning proof has three roots: B05_TRIMMED_COMMON_POLYHEDRON, B08_LOCAL_PLANE_AND_GRAM_TRANSPORT and G6_GF02B_PAYMENT. Recursing through the frozen dependencies gives the 13-module closure recorded in WINNING_DEPENDENCY_RECEIPT.json. It includes B01, B02, B03, B04, B05, B06, B08 and G1_STATE, G1_RESIDUAL, G3_QUOTIENT_CORE, G4_SPECTRAL, G4_COUPLED_REGION, G6. All have ACTIVE_EXACT status. The imported A/B module and resource records embedded in C were compared for exact JSON equality with the frozen A/B ledgers. They match.

The formal graph lists imported Proposition 3.2 and fixed-function unweighting dependencies; the B01/B02 statements additionally expose the retained universal local and compatibility premises. Those are explicit trust inputs even though their labels are not separate graph nodes. The plane premise of B08 is supplied by K10 on the trim family. B06 is retained as a declared dependency, while B05 provides the stronger actual polyhedron. No optional G5 transport schema or conditional higher-moment constants enter the proof.

The resource audit is the exact identity

    d+y=(d+rho v)+(y-rho v).

The first bracket is bounded once by the local plane, pinching and offset average. The second bracket is bounded once by G6. The quotient and global spectral conditions restrict the same feasible state used to derive G6; their use does not supply second copies of y, d or the total budget. q0 and Z are inside y and are conservatively discarded in the scalar relaxation; no invented positive density is credited afterward. The same ell appears with +rho and -rho, so the tail is paid exactly once. The local band E appears once in a simultaneous polyhedron and once in the band profile; Farkas weights obey objective-coefficient dominance. Pressure uses one full envelope tax and offsets are divided by m once.

The trace-refined quotient and other valid payment views may be co-imposed or their complete lower bounds maximized, but are not added in this winner. Whole-slack higher-moment bounds are not added to D+Y. Neither numerical sharpness of the global relaxation nor optimality over 86,992 subsets is needed to prove this legal fixed certificate. The author verifier's enumeration replay is a secondary check, not the mathematical basis of this audit.

## K13 — Scalar endgame: PASS

Fix the frozen m=492, rho, six prices and reward R=38219880252651/10000000000000. On any limiting state, after the fixed smoothing interpretation in K11,

    x-h≥d+y≥(R x-P_price)/m-p_h(x;rho).

Put s0=6734775921119/10000000000000. For h≤x≤s0, monotonicity in K5 implies p_h(x;rho)≤p_h(s0;rho). A rational nonnegative pbar satisfying

    pbar²+A_s0 pbar≥rho² N_s0/4

bounds the positive root from above, since the quadratic is strictly increasing on p≥0. Hence

    (m-R)x≥mh-P_price-m pbar.

The independent arithmetic shows m-R=4881780119747349/10000000000000>0 and

    mh-P_price-m pbar-(m-R)s0>0.

This contradicts every h≤x≤s0. Values below h are excluded by the same basic analytic budget. There is no unjustified conclusion from checking just one x numerically: the domain-wide monotonicity and m-R sign supply the rest of the interval. With smoothing, replace R by R_delta; the endgame margin decreases by a_delta s0, so a sufficiently small fixed delta preserves its strict sign. The denominator stays positive.

The count ratio is in [0,1]; a subsequence realizes its liminf. The argument excludes a liminf at or below s0. The advertised weaker statement liminf N_0^s(T)/N(T)≥s0>r_* is therefore supported. No larger unrecorded decimal is proposed.

## K14 — Independent exact comparison, then author replay: PASS

The freshly written program fixes the exact original coefficients, reconstructs the physical rows, proves all Farkas inequalities and then reconstructs the endgame. It does not import the author's verifier. For the decisive radical it computes isqrt(floor(rad·10^180)) and forms a directed rational interval with denominator 10^90. This gives its own pbar independently of the author's penalty_upper. Its strictly positive endgame margin is

    732311509994561991974563925193115633921655445540473383910736720874634024061513211 /
    500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.

Its orientation is 1.46462301998912398394912785038623126784331089108e-9. As an independent alternate sign route, define the penalty needed at the separator by

    p_needed=h-P_price/m-(1-R/m)s0
            =1894323883191685297/1200000000000000000000000000>0.

The program verifies exactly

    p_needed²+A_s0 p_needed-rho²N_s0/4
    =9041598080495932833763851631404069026110772129 /
      4500000000000000000000000000000000000000000000000000000000 >0.

Thus p_h(s0)<p_needed without depending on any authored radical enclosure. Separately substituting the frozen authored rational witness reconstructs its printed margin exactly:

    197709610897766003525347778736270024097588737952243174610346641 /
    134990102025867487759198256090264582174639743300000000000000000000000000 >0.

Finally, using the exact source baseline

    r_*=8269551442741204889710953/12278882618209750000000000,

the independent subtraction is

    s0-r_*=34271814394247548721/491155304728390000000000000>0.

This is approximately 6.977795834496777e-8 in proportion, or 0.000006977795834496777 percentage points. The separator is 67.34775921119 percent, with multiplicity in the denominator and only simple critical-line zeros in the numerator.

The source first seal is 2026-09-13T23:26:32.830240+00:00, SHA256 cfddd356136292f95433ce4c0ed979738374096c090614696a7d979e8ef65dfa. The complete independent receipt finished at 2026-09-13T23:37:50.743203+00:00, SHA256 444b9ce7706986b582c7a2682684953b8c9821767e624636f5ea2bbd1d3825c4. The first author-verifier source read was at 23:38:05.757393+00:00. The separate frozen verifier execution ran from 23:38:27.204452 to 23:38:27.440289+00:00 and returned PASS_EXACT. Its source SHA256 is ea588a3dc810a91d68b796eed597e2731cbe343df438c1b7e925f18a634970ed. All 115 files in its tree had identical before/after hashes. It matched the independent 464-line count, minimum plane margin, separator, gain and authored endgame margin. This chronology excludes reliance on its code as the independent reconstruction.

## K15 — Exact claim and imported trust: PASS

The supported statement is a strict refinement of the supplied Gebendorfer lower bound: the lower asymptotic proportion of all nontrivial zeros, counted with multiplicity, which are simple and lie on the critical line is at least 6734775921119/10^13, strictly above the exact supplied r_*. It uses no RH assumption and no conditional moment density.

New mathematics checked here comprises the exact signed-state residual, quotient and spectral restrictions, the nonlinear residual payment, rho-extended profile, reflected trimming, capacity and m492 bookkeeping, whole-polyhedron separator, same-state transport and one-budget endgame. The weighted unconditional pair-correlation theorem stated in the source and the Riemann–von Mangoldt asymptotic remain external analytic inputs. Their applicability is checked; their external proofs were not re-proved or searched for in this isolated audit.

The original 58,577,037-node universal local computation remains a pinned imported computational trust boundary: 50,089,182 nine-row nodes, 7,638,774 cover nodes and 849,081 restricted nodes. Its archives, proof inputs, candidate bindings and stored completion record were checked, but the subdivision was not executed here. Hash integrity proves identity of evidence, not independent truth of an unexecuted universal computation. The fixed window positivity and H>h were independently re-enclosed with rational arithmetic, narrowing that trust boundary for the window constant.

This audit is not Lean verification and is not independent external peer review. It does not certify world priority, global parameter optimality, completeness of a stronger theorem search, or the uninstantiated conditional higher-moment class. No publication or upload was performed.

## K16 — Reproducibility classification: REVISE, technical only

The frozen PGF-A INPUT_PAYLOAD.json has two absolute Windows author-workspace archive paths. Its default replay.py uses Path(spec['path']) when --input-dir is omitted. A relocated copy therefore depends on those author-machine paths. Static inspection establishes the issue; this audit did not follow those paths into forbidden live workspaces. The source already offers --input-dir for a directory containing the exact two ZIP names, so the defect is default-location metadata and packaging, not absence of a relocation mechanism.

The reproduction archive hash in that metadata equals the exact archive independently verified here. The C-imported primary files were checked byte for byte against that archive, and the portable C verifier ran successfully. The critic's own final program uses a sibling evidence directory and rechecks the exact original archive plus all actually used rational data. Consequently no mathematical binding failure follows from the PGF-A default path issue.

No author file, theorem, certificate or metadata was repaired. The differing supplied reference PDF and reproduction PDF were kept distinct, with the reproduction TeX/candidates authoritative. The one initial output-directory setup assertion and an unsuccessful guessed TeX filename were runtime/path matters; both were resolved within the allowlisted paths without a mathematical change. There was no substantive mathematical defect requiring an early kill freeze.

The resulting first overall classification is PASS_WITH_REPRODUCIBILITY_DEFECTS_ONLY. The technical revision is limited to relocation documentation/default input discovery for A. Mathematical claims are qualified by the explicit imported trust boundary above. No mathematical repair remains in this audit.
