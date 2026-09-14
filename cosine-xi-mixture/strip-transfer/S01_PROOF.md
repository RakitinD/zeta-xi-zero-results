# A moving boundary for the first cosine–Xi zero

COSXI-S01. All new mixture assertions below have status AUTHOR_PROVED, awaiting review. No independent audit or historical novelty claim is made.

## 1. Statements and notation

Put kappa=pi/4, a=2*pi*exp(3), c0=log(2*exp(1/2)*sqrt(pi)),

\[
 \xi(w)=\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w),\quad
 \Xi(z)=\xi(\tfrac12+iz),\quad H_t(z)=(1-t)\cos z+t\Xi(z),
 \quad\lambda=\log(t/(1-t)).
\]

The large parameter is lambda, not the ordinate in the external source. Write w=sigma-ix, z=i(w-1/2)=x+i(sigma-1/2), and

\[
 P(w)=\xi(w)/\cosh(w-1/2),\qquad D=P'/P.
\]

For v>=3 define

\[
 \beta(v)=\{54.004(\log v)^{2/3}(\log\log v)^{1/3}\}^{-1},
 \qquad q(x)=\beta(2x)\quad(x\ge10).
\]

**S01-GLOBAL (unconditional moving-boundary theorem).** There are absolute constants C and lambda0 such that, for EVERY real lambda>=lambda0 and EVERY real

\[
 1-\beta(6\lambda)/16\le s\le3/2,\qquad d=s-1/2,
\]

the infimum over all zeros, including boundary zeros,

\[
 R_d(t)=\inf\{|z|:H_t(z)=0,\ |\Im z|\ge d\}
\]

is finite and attained, and

\[
 \boxed{\left|R_d(t)-\left\{\frac4\pi\lambda+
       \frac{2d+7}{\pi}\log\lambda\right\}\right|
       \le C(1+\log\log(6\lambda)).}                    \tag{1}
\]

The same constants work simultaneously for all s in this interval; no regularity of a chosen s(lambda) is needed. There is a genuine simple first-quadrant zero with

\[
 x=X_{\rm front}(\lambda,s)+O(1+\log\log\lambda),\qquad
 d<y<d+O((1+\log\log\lambda)/\log\lambda),              \tag{2}
\]

where X_front=lambda/kappa+(s/2+3/2)log(lambda)/kappa. Every eligible zero has modulus at least X_front-O(1+log log lambda). The upper zero is obtained on one connected arc of x-length 16*pi/log(lambda), whose phase variation is at least 4*pi. Every minimizing first-quadrant representative also satisfies (2) with the lower strict height inequality replaced by y>=d. The error in (1) is o(log lambda), so the displayed logarithmic term is resolved. A very small correction (2d-1)log(lambda)/pi need not separately exceed the error.

In particular:

* **S01-ABOVE:** for any eta_plus(lambda)>0 tending to zero, with no lower rate restriction, d_plus=1/2+eta_plus satisfies (1) for all sufficiently large lambda. The final threshold also requires eta_plus<=1/2.
* **S01-BELOW:** every choice 0<eta_minus(lambda)<=beta(6lambda)/16 satisfies (1) for d_minus=1/2-eta_minus. This is an application of an already known zeta zero-free region, not its improvement.
* With the concrete choice eta_minus=beta(6lambda)/16, the zero in (2) actually has 0<y<1/2, or 1-eta_minus<Re w<1, for every sufficiently large lambda. Indeed its height excess is o(eta_minus). These are zeros of the MIXTURE.

For comparison with the starting endpoint constants, section 4 proves **S01-RIGHT-EULER** without the published near-one bounds: if eta>0 tends to zero and eta^{-2}=o(log lambda), then

\[
 R_{1/2+\eta}(t)=X_{\rm front}(\lambda,1+\eta)+O(\eta^{-1}). \tag{3}
\]

For example eta=(log lambda)^{-1/4} is admissible. This is a separate sufficient rate from the original constants, not a restriction on S01-ABOVE.

## 2. Exact algebra, branches, and a finite loss budget

The completed functional equation gives Xi(i(w-1/2))=xi(w), and cos(i(w-1/2))=cosh(w-1/2). The latter has no zero for Re w>1/2. Thus throughout that half-plane the branch-free equation is

\[
 H_t(i(w-1/2))=0\quad\Longleftrightarrow\quad P(w)=-e^{-\lambda}. \tag{4}
\]

On the Euler half-plane Re w>1, the canonically normalized logarithm ell of P is the one in E01 section 2 and Q01 section 2: all explicit logarithms are continued from the positive real ray, and log zeta is the absolutely convergent Euler logarithm. Its exact rearrangement is

\[
 \ell(w)=\frac w2\Log(w/a)+\frac32\Log w+c_0+E(w),\quad
 E=\Log(1-1/w)+S_\Gamma+g-\log(1+e^{1-2w}),             \tag{5}
\]

where g=log zeta and S_Gamma is the log-Gamma Stirling remainder. The explicit factorization is

\[
 H_t(i(w-1/2))=(1-t)\cosh(w-1/2)(1+e^{\lambda+\ell(w)}). \tag{6}
\]

On any specified continuation of ell, all odd levels lambda+ell=(2m+1)pi*i are retained. Multiplicities in (6) agree with those of ell minus the chosen level. This is an identity, independent of the old tail existence and completeness theorems.

Direct logarithmic differentiation, away from component singularities and zeros, gives

\[
 D=\frac{\zeta'}\zeta+\frac1w+\frac1{w-1}-\tfrac12\log\pi
       +\tfrac12\psi(w/2)-\tanh(w-1/2).                 \tag{7}
\]

At w=1 the pole in zeta'/zeta cancels 1/(w-1); P is regular and nonzero there. We never use the separated formula at that point.

Here is an input-output statement that isolates what the phase argument needs. Let an analytic nonzero P have an analytic logarithm ell on a neighborhood of the closed rectangle [s,s+h]xI in coordinates sigma-ix. Assume the prefactor in (6) is nonzero on that neighborhood, as it is in Re w>1/2. Set F=lambda+Re ell, V=Im ell, D=A+iB. Suppose on the rectangle A>=a0>0 and on its lower edge

\[
 -J\le F(s,x)\le-\epsilon<0,\quad a_0h>J,\quad a_0|I|>2\pi. \tag{8}
\]

**S01-TRANSFER:** these hypotheses imply a unique smooth balance graph sigma(x) in (s,s+h), and a simple zero of (6) over the interior of I. Indeed F_sigma=A, F_x=B, V_sigma=B, V_x=-A, so the intermediate value and implicit function theorems give

\[
 \sigma'=-B/A,\qquad (V(\sigma(x),x))'=-(A^2+B^2)/A\le-a_0. \tag{9}
\]

Its continuous phase interval contains an odd multiple of pi. At that point (6) supplies a zero and D!=0 gives simplicity. Any branch shifted by 2*pi*i has exactly the same odd-level set. No estimate on |B| is required for this existence implication beyond the finiteness and continuity supplied by analyticity. No sum over disconnected arcs, and no univalence on a perforated domain, occurs.

For a full radial minimum one additionally needs: (i) lower-edge value control for every smaller x under consideration; (ii) positive A along EVERY height sigma>=s at those x, or another all-height exclusion argument; (iii) a lower bound on |P| in the entire low-x region, including arbitrarily large sigma; and (iv) a trivial radial cutoff beyond the tested x interval. A derivative estimate alone does not supply the lower-edge sign or magnitude in (8). A one-sided bound Re(zeta'/zeta)>=-(1/2-a1)log x+O(1), with an actual a1>0 and controlled explicit terms, would suffice for A; the full modulus bound used below is a convenient stronger input. The value budget J, rather than the derivative loss alone, determines h and the displacement of X_front. The zero-free neighborhoods below furnish the required logarithm and estimates with explicit interior margins.

## 3. Classical analytic estimates and inherited scope

The source identities and elementary estimates used here were checked in E01 sections 2–5, Q01 sections 2–3, and their corresponding endpoint/quantitative audits; the source-specific records are in evidence/INHERITED_SCOPE_CHECK.md. The old PASS labels do not assert moving-boundary uniformity. Completeness was read for context and is not a premise of any theorem here. Neither a fixed-t exceptional set nor the old sufficient index N(t) enters this argument.

The log-Gamma remainder formula at DLMF 5.11.1 and the first paragraph of 5.11(ii) gives

\[
 |S_\Gamma(w)|\le1/(3|w|)\quad(\Re w>0),\qquad
 |S_\Gamma'(w)|\le8/|w|^2.                               \tag{10}
\]

For the derivative, take the radius-|w|/4 Cauchy circle in the sector |arg z|<3*pi/4, where the same remainder is <2/|w|. This circle is used only for S_Gamma, not for g. The logarithmic correction derivative is 1/[w(w-1)], bounded by 2/|w|^2 for |w|>=2. The cosh logarithm and its derivative have bounds q0/(1-q0) and 2q0/(1-q0) whenever exp(1-2sigma)<=q0<1. These are convergent power-series estimates.

For later compact coverage, xi is nonzero for Re w>=1, including xi(1)=1/2. Besides the Euler product, the classical line-one zero-freeness is independently recovered as follows. For sigma>1, positivity of 3+4*cos(theta)+cos(2theta)=2(1+cos(theta))^2 in the Euler logarithm gives

\[
 \zeta(\sigma)^3|\zeta(\sigma+i\tau)|^4
                         |\zeta(\sigma+2i\tau)|\ge1.    \tag{11}
\]

If tau!=0 and zeta(1+i*tau)=0 of multiplicity m>=1, analytic continuation at 1+i*tau and 1+2i*tau makes the left side O((sigma-1)^{4m-3}) as sigma decreases to 1; it tends to zero, a contradiction. The only real line-one point is the simple pole of zeta, removed in xi with value 1/2. The remaining factors are nonzero. This proof also checks the precise classical assertion recorded in DLMF 25.10(i); no hypothesis about zeros inside the strip was used.

## 4. What the original Euler constants already permit

Let s=1+eta, 0<eta<=1/2. The original M_s from E01 (3.2) obeys M_s=O(eta^{-1}) with an absolute constant, since zeta(1+eta)<=1+1/eta. On Re w>=s,

\[
 |E|\le M_s,\quad |E'|\le K_s=O(\eta^{-2}),\quad
 A\ge\tfrac12\log|w|-C_s,\quad C_s=O(\eta^{-2}).       \tag{12}
\]

These follow by Cauchy on radius eta/2 in Re w>=1+eta/2, exactly the stated original margin. Set X_s=exp(4C_s). If eta^{-2}=o(log lambda), then X_s=lambda^{o(1)} and M_s=o(lambda). This is a genuinely nonempty joint range.

The old compact minimum need not be extrapolated to a moving rectangle. Equation (5) itself gives a uniform lower bound at EVERY sigma>=s and x>=0:

\[
 U(\sigma,x)\ge-\kappa x-a/(2e)+c_0-M_s.              \tag{13}
\]

To check it, with rho=|w| and theta=arctan(x/sigma), use theta<=pi/2, rho>=sigma>=1, log rho>=0, and sigma*log(rho/a)>=sigma*log(sigma/a)>=-a/e. Thus F>0 at all heights when x<=X_s, once lambda>kappa X_s+a/(2e)-c0+M_s. This covers the moving low-x region explicitly.

For x>=X_s, (12) gives A>=log x/4>0 at every height. At sigma=s, the elementary real-part calculation in (5), uniform for 1<=s<=3/2, is

\[
 U(s,x)=-\kappa x+(s/2+3/2)\log x+O(M_s+1)\quad(x\ge1). \tag{14}
\]

Every eligible root therefore satisfies x>=X_front-O(M_s+1): first use kappa*x>=lambda+b*log x-O(M_s+1), b=s/2+3/2>0, to obtain x>=lambda/(2*kappa), then substitute this in log x. The upper construction is (8) on a boundary interval displaced O(M_s+1) to the right of X_front, with J=O(M_s+1), h=O((M_s+1)/log lambda), and length 16*pi/log lambda. It lies at x comparable to lambda, so A>=log lambda/4, for all sufficiently large lambda. For clarity, one may use the exact choices in section 7 with its boundary budget M_lambda replaced by a sufficiently large absolute multiple of M_s+1. The proof of the signs there uses only (14) and (M_s+1)=o(lambda); h=o(1) follows from the assumed rate. Equation (9) gives the odd phase and a simple actual root. Since y is bounded, |z|-x=O(1/lambda). These lower and upper bounds prove (3), with every parameter dependency retained. Its error is o(log lambda). No published zero-free region is needed for this Euler-only conclusion.

## 5. A verified interior log-zeta estimate

Use two separate unconditional inputs from Bellotti, arXiv:2306.10680v1, Theorems 1.1 and 1.2, inspected in the primary full-text HTML with v1 metadata (submission 19 June 2023):

\[
 |\zeta(\sigma+i\tau)|\le70.7|\tau|^{4.438(1-\sigma)^{3/2}}
                  (\log|\tau|)^{2/3},\quad
 1/2\le\sigma\le1,\quad |\tau|\ge3,                    \tag{15}
\]

and no zeros when |tau|>=3 and sigma>=1-beta(|tau|). The constants in (15) are rounded UP from 70.6995 and 4.43795. No estimate for g or g' is silently attributed to the zero-free assertion. The asymptotic constant 48.0718 from Theorem 1.3 is not used.

Let

\[
 \Omega=\{\sigma-ix:x>4,\ \sigma>1-\beta(x)/2\}.
\]

This is an open simply connected domain: (sigma,x) maps homeomorphically to (sigma-1+beta(x)/2,x) in a product of two open intervals. It is zero-free for zeta by the source region, has no zeta pole, and lies in sigma>3/4. Therefore it has an analytic logarithm g. Normalize it by agreement with the Euler logarithm on the connected overlap sigma>1,x>4. This constructs the branch and all phase offsets; simply removing zeros is not the justification.

Fix x>=10 and put h=q(x), c=1+h/4-ix, R=h/2. The entire closed disk |w-c|<=R lies in Omega with a positive margin. Indeed its ordinate x' satisfies 3<x-h/2<=x'<=x+h/2<2x, hence beta(x')>=beta(2x)=h, whereas its left edge is 1-h/4>1-beta(x')/2. Its right edge is <2. All source hypotheses hold on a neighborhood of this disk.

For its part with sigma>=1 we need a bound uniform right down to 1. For integer N and Re w>0, w!=1, summation by parts and analytic continuation give

\[
 \zeta(w)=\sum_{n\le N}n^{-w}+\frac{N^{1-w}}{w-1}
                  -w\int_N^\infty\{u\}u^{-w-1}\,du.   \tag{16}
\]

The formula is first obtained from the absolutely convergent Dirichlet series at Re w>1; the integral is analytic at Re w>0. On the disk, choose N=ceil(|Im w|). If sigma>=1, the sum is <=1+log N, the middle term <=1/|Im w|, and the integral term has modulus <=|w|N^{-sigma}/sigma<=4. Consequently |zeta(w)|<=10*log(2x). This avoids the spurious divergence of the real-ray bound as sigma decreases to 1.

Define the explicit positive budgets

\[
 M(x)=\max\{\log70.7+4.438(h/4)^{3/2}\log(2x)
                       +\tfrac23\log\log(2x),\ \log(10\log(2x))\},
\]
\[
 G_0(x)=\log(1+4/h),\quad H(x)=6M(x)+7G_0(x),\quad Z(x)=16H(x)/h. \tag{17}
\]

On the whole disk Re g<=M(x) by (15) and (16), while |g(c)|<=log zeta(1+h/4)<=G0(x) by its Euler normalization. The elementary Borel–Caratheodory estimate yields |g|<=H(x) on radius 3h/8. For completeness, if f=g-g(c), A=M-Re g(c)>0, then f/(2A-f) has modulus <=1 and vanishes at the center. Schwarz's lemma gives |f|<=2A*r/(R-r); r=3R/4 gives the claimed 6M+7|g(c)| bound. If A=0, the harmonic maximum principle makes f identically zero.

For real sigma in [1-h/16,1+h/2], the point sigma-ix is at distance at most 5h/16 from c, so its full radius-h/16 Cauchy circle lies in radius 3h/8. Thus |g|<=H and |g'|<=16H/h there. For sigma>=1+h/2, the Euler logarithm gives |g|<=log(1+2/h)<=H; its radius-(sigma-1)/2 Cauchy disk is entirely in the Euler half-plane and gives

\[
 |g'|\le\frac2{\sigma-1}\log(1+\frac2{\sigma-1})
       \le\frac4h\log(1+4/h)\le Z(x).
\]

We have consequently proved **S01-LOG**, with the canonical branch just constructed:

\[
 |g(\sigma-ix)|\le H(x),\quad
 |\zeta'/\zeta(\sigma-ix)|\le Z(x)
 \quad(x\ge10,\ \sigma\ge1-q(x)/16).                  \tag{18}
\]

These are standard consequences rederived with the stated margins, not new zeta bounds. From (17), with L=log(2x),

\[
 H(x)=O(1+\log\log(2x)),\qquad
 Z(x)=O(L^{2/3}(\log L)^{4/3})=o(\log x).               \tag{19}
\]

All constants are absolute. For example the exponential contribution in M has (h/4)^{3/2}L=1/[8*(54.004)^{3/2}*sqrt(log L)], so it is bounded for x>=10. This displays the derivative loss explicitly. The h/16 Cauchy margin, the h/4 distance of the large disk's left edge from 1, and the factor 2 in q(x)=beta(2x) are all fixed before x grows.

## 6. From arithmetic bounds to all-height control

Equation (5) extends analytically to Omega using the g above, the normalized log-Gamma, the power series Log(1-1/w) (|w|>4), and the cosh series (sigma>3/4). It agrees with the Euler ell on the overlap; hence (6) and the ORIGINAL odd phases continue without an integer offset. No global logarithm on the critical strip is asserted.

Let q0=exp(-1/2) and C_E=(log a)/2+1+2q0/(1-q0). Equations (5), (10), and (18) give, at x>=10 and sigma>=1-q(x)/16,

\[
 A=\Re D\ge\tfrac12\log x-C_E-Z(x).                   \tag{20}
\]

Here Re(3/(2w))>0; the other non-arithmetic derivative losses are <=10/x^2+2q0/(1-q0). Thus choose a fixed absolute X0>=10 such that for EVERY x>=X0,

\[
 C_E+Z(x)\le\tfrac14\log x.                            \tag{21}
\]

Such an X0 exists by (19); the defining functions are explicit, though no numerical optimization is attempted. We have A>=log x/4 on the entire eligible vertical ray at each such x. Also |B|<=pi/4+3/(2x)+10/x^2+2q0/(1-q0)+Z(x), which is recorded but not needed for the sign argument (9).

For 3/4<=s<=2 the real-part expansion of (5) has the uniform bound

\[
 |U(s,x)+\kappa x-(s/2+3/2)\log x|\le20+H(x)
 \quad(x\ge10,\ s\ge1-q(x)/16).                        \tag{22}
\]

To verify the absolute 20, let rho=(s^2+x^2)^{1/2} and theta=arctan(x/s). The real explicit part is (s/2)log(rho/a)-x*theta/2+(3/2)log rho+c0. Relative to -kappa*x+b*log x, the geometric errors are b*log(rho/x), -(s/2)log a, x*arctan(s/x)/2, and c0. Their absolute sum is at most 5/x^2+log a+1+|c0| for s<=2,x>=10. The non-g remainder is bounded by 1/(x-1)+1/(3x)+q0/(1-q0). The total is <20. Only the real value is needed here; (18) gives the stronger full-log estimate for phase normalization as well.

The low-x part is a FIXED compact argument plus a separate large-sigma argument. Choose a fixed S>=2 large enough that A>=1 on sigma>=S, all real x, using Q01's whole-half-plane estimate |E'|<=10/|w|^2+5*2^{-sigma}+3*exp(1-2sigma) and the explicit derivative in (5). This choice is independent of lambda and x. On the compact rectangle [1,S]x[0,X0], P is continuous and nonzero by section 3. There are consequently fixed eps0 in (0,1/4) and m0 finite such that P is nonzero and log|P|>=m0 on [1-eps0,S]x[0,X0]. Uniform continuity on a compact neighborhood, or a positive minimum and a bounded derivative there, proves this left extension. For sigma>=S and 0<=x<=X0, integrate A>=1 from S to obtain the SAME lower bound m0 at all heights. Therefore

\[
 F_\lambda(\sigma,x)>0\quad
 (\sigma\ge1-\varepsilon_0,\ 0\le x\le X_0)
 \quad\hbox{if }\lambda>-m_0.                          \tag{23}
\]

This does not assert uniform compact convergence on an expanding rectangle. The compact rectangle, eps0, and m0 are fixed first. The completion at w=1 is used rather than a false pole. The high-x derivative input is then used throughout the adjoining interval [X0,3lambda].

## 7. Full exclusion, odd-phase upper root, and the minimum

Fix any sufficiently large lambda and any s in the interval of section 1. Impose beta(6lambda)/16<eps0 and lambda>-m0, so (23) excludes all eligible low-x roots. On X0<=x<=3lambda, monotonicity of beta gives s>=1-q(x)/16. Thus (20)–(22) apply for every sigma>=s.

Write Q_lambda=1+log log(6lambda). By (17)–(19) choose once and for all an absolute K>=1 with

\[
 20+H(x)\le KQ_\lambda\quad(X_0\le x\le3\lambda),
 \quad M_\lambda=KQ_\lambda+3.                         \tag{24}
\]

Every eligible root can be reflected by evenness and conjugation to x>=0,y>=d, preserving multiplicity, modulus, and boundary equality. If x>=3lambda its radius is already >=3lambda. Otherwise the low-x exclusion gives x>X0, and positivity of A on the WHOLE ray [s,infinity) implies F_lambda(s,x)<=0. Equation (22) implies

\[
 \kappa x\ge\lambda+b\log x-KQ_\lambda,\qquad b=s/2+3/2.
\]

For large lambda this first gives x>=lambda/(2*kappa), and then

\[
 x\ge X_{\rm front}-(KQ_\lambda+b\log(2\kappa))/\kappa.
                                                               \tag{25}
\]

The case x>=3lambda satisfies the same lower bound once lambda is large, because X_front/lambda tends to 1/kappa<3 uniformly in s. This proves **S01-LOWER**, an all-height lower exclusion over the complete root set, without requiring an arithmetic estimate beyond the finite ordinate cutoff 3lambda.

For the upper root put

\[
 c_\lambda=(M_\lambda+2)/\kappa,\quad
 L_\lambda=16\pi/\log\lambda,\quad
 I=[X_{\rm front}+c_\lambda,\ X_{\rm front}+c_\lambda+L_\lambda],
\]
\[
 J_\lambda=2M_\lambda+3+\kappa,\qquad
 h_\lambda=4(J_\lambda+1)/\log\lambda.                  \tag{26}
\]

For all sufficiently large lambda, uniformly in s, I is contained in [lambda,2lambda], L_lambda<=1, and s+h_lambda<=2. For x=X_front+c_lambda+u in I,

\[
 F_\lambda(s,x)=-\kappa(c_\lambda+u)+b\log(x/\lambda)
                       +e(s,x),\qquad |e(s,x)|\le KQ_\lambda.
\]

Since b<=5/2 and 0<=log(x/lambda)<=log 2, the last two terms have absolute value <=M_lambda. Hence -J_lambda<=F_lambda(s,x)<=-2. Integrating A>=log(lambda)/4 over [s,s+h_lambda] gives F_lambda(s+h_lambda,x)>=1. All points are inside Omega; moving upwards in sigma only increases the source margin. The rectangle has a zero-free neighborhood, and (8) holds with a0=log(lambda)/4. Across I the phase decreases by at least 4*pi, strictly more than 2*pi. Thus (9) and (6) prove **S01-UPPER**, an actual SIMPLE zero for every such lambda and s, at an original odd phase, with s<sigma<s+h_lambda. It obeys x=X_front+O(Q_lambda), y=d+O(Q_lambda/log lambda). Since y is bounded,

\[
 0\le |z|-x=\frac{y^2}{|z|+x}=O(1/\lambda).             \tag{27}
\]

Combining (25) and (27) proves (1). The entire function H_t is not identically zero: it is positive on the positive imaginary ray corresponding to real w>1. A disk containing the upper root contains finitely many zeros, with a nonempty eligible subset; the closed height restriction then gives attainment of the full infimum. No radial ordering of an inherited tail is presumed.

For any minimizing first-quadrant representative, (25) and the upper bound give x=X_front+O(Q_lambda), so (22) gives F_lambda(s,x)=O(Q_lambda). Integrating A>=log x/4 up to its actual sigma proves sigma-s=O(Q_lambda/log lambda) without any prior upper-height assumption. Moreover it is simple because D has positive real part there. On this resulting bounded band, (5) and (18) give the canonical phase

\[
 -\Im\ell(\sigma-ix)=\tfrac x2\log(x/a)+O(Q_\lambda),
\]

which is negative for Im ell at large x. Thus the constructed root and every minimizing representative have lambda+ell=-i(2n+1)pi with n>=0 and n~lambda*log(lambda)/pi^2. This is a phase index, not a radial rank or a continuous trajectory.

Finally, at eta_minus=beta(6lambda)/16,

\[
 \frac{Q_\lambda/\log\lambda}{\eta_{\rm minus}}
 =O((\log\lambda)^{-1/3}(\log\log\lambda)^{4/3})\to0.
\]

Thus h_lambda<eta_minus eventually, proving that the actual upper zero lies strictly below Re w=1. For a smaller eta_minus the same radial minimum theorem still holds, but the constructed zero is not claimed to lie below 1 unless h_lambda<eta_minus is checked.

## 8. Thresholds, scope, and comparison

All quantified constants in the combined theorem are absolute, inherited from the displayed source constants and the explicit elementary estimates, except that the final admissibility time for an arbitrary eta_plus also requires eta_plus<=1/2. A sufficient lambda0 is obtained by imposing: (21) for the fixed X0; beta(6lambda)/16<eps0; lambda>-m0; X0<lambda; L_lambda<=1; s+h_lambda<=2 for all allowed s; I contained in [lambda,2lambda]; and the lower-bound bootstrap in (25). Their eventual validity was proved. eps0 and m0 are fixed compact constants from section 6, not supplied numerical values. The proof is asymptotic and does not claim a usable numerical lambda0 or an interval-certified numerical example.

ABOVE_ONE and BELOW_ONE both have an unconditional FULL_RADIAL_MINIMUM. The constructed root is in the window lambda<=|Re z|<=2lambda, but WINDOW_ONLY is not the final scope: (23), (25), and the x>=3lambda cutoff cover every smaller radius and every height. ONE_SIDED lower and upper assertions are separately identified so that the full conclusion's dependencies can be reviewed. The only global logarithm claimed outside the Euler half-plane is on the specified zero-free Omega. There is no continuation to all Re w>1/2, no xi simplicity assumption, no RH proof or new critical-line proportion, no improvement of the zero-free region or value bounds in (15), and no claim of world novelty. The loss-budget lemma and this particular mixture consequence are author results for review; the arithmetic estimates in section 5 are known-input consequences rederived here.

STOP_FOR_SOL_REVIEW after the first complete freeze.
