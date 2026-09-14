# The first exterior zero of a vanishing cosine perturbation of Xi

Researcher: COSXI-E01. Status: AUTHOR_PROVED, first author result for review. This is neither an independent audit nor a formally verified proof.

For each fixed real d > 1/2, put

\[
 H_t(z)=(1-t)\cos z+t\Xi(z),\qquad
 \Xi(z)=\xi(1/2+iz),\qquad
 \lambda=\log\frac{t}{1-t},\quad 0<t<1,
\]
\[
 R_d(t)=\inf\{|z|:H_t(z)=0,\ |\Im z|\ge d\}.
\]

The empty-set convention is +infinity. All zero statements use analytic multiplicity. The parameter reduction is exact: H_t/t=Xi+exp(-lambda)cos and t=exp(lambda)/(1+exp(lambda)). The main result is

\[
 \boxed{R_d(t)=\frac4\pi\lambda+
 \frac{2d+7}{\pi}\log\lambda+O_d(1)}
 \qquad(\lambda\longrightarrow+\infty).                 \tag{T}
\]

The lower bound covers every root in the set defining R_d, without a height cutoff. The upper bound is realized by a simple, correctly phased root with positive real part and height d + O_d(1/log lambda). Constants and thresholds depend on the fixed d; no uniformity as d decreases to 1/2 is asserted. Sections 1–5 establish the core E0–E2, with stronger estimates retained. Section 6 explicitly concludes the optional E3 refinement and E4 consequence after the core. Section 7 treats optional E5.

## 1. Compact convergence and its limited scope (E0)

Exactly H_t-Xi=(1-t)(cos-Xi), so H_t converges to Xi locally uniformly as t tends to 1. If a compact K contains no Xi zero, then m_K=min_K|Xi|>0. The stated criterion

\[
 (1-t)\sup_K|\cos-\Xi|<m_K
\]

gives |H_t|>0 on K by the triangle inequality. Around any Xi zero, a sufficiently small circle has no Xi zero on its boundary. Rouché gives the same number of nearby H_t zeros as the Xi multiplicity for t sufficiently close to 1. At a simple real Xi zero, choose a conjugation-invariant disk containing no other Xi zero. Its unique nearby H_t zero is simple and real for real t, since conjugation preserves both H_t and that disk. At a multiple zero only the total local multiplicity is fixed; individual labeling, simplicity and absence of coalescence are not assumed. [Rouché's theorem, DLMF 1.10(iv)](https://dlmf.nist.gov/1.10#iv).

For completeness, the usual scope equivalence is

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 R_d(t)\longrightarrow\infty\text{ for every fixed }d>0.       \tag{1.1}
\]

If all Xi zeros are real, each compact set {|z|<=R, |Im z|>=d} is zero-free for Xi and eventually for H_t. Conversely, an off-real Xi zero has a small closed disk at a positive distance from the real axis; Rouché preserves its positive multiplicity there and prevents the corresponding R_d from escaping. This is standard compact persistence, not an RH argument. For d>1/2, Xi is already zero-free in the reflected Euler exterior, unconditionally. Neither (T) nor any later assertion treats the remaining critical-strip problem.

## 2. Exact canonical reduction and fixed-phase motion (E1)

Use precisely the original coordinate

\[
 w=\tfrac12-iz=\sigma-ix,\qquad z=i(w-\tfrac12),
 \qquad a=2\pi e^3,\quad c_0=\log(2e^{1/2}\sqrt\pi).
\]

On Re w>1 define ell=L_(1/2) by

\[
\begin{split}
 \ell(w)={}&\Log w+\Log(w-1)-\tfrac w2\log\pi
  +\log\Gamma(w/2)-w+\tfrac12\\
 &+L_\zeta(w)-\log(1+e^{1-2w}),\qquad
 L_\zeta(w)=\sum_p\sum_{k\ge1}\frac{p^{-kw}}k.
\end{split}                                                   \tag{2.1}
\]

All logarithms have the original real-ray normalization: the first two are real for real w>1, log-Gamma is the analytic logarithm normalized on the positive ray, and the last logarithm is its convergent power series. Thus ell is real on that ray. The Euler logarithm converges absolutely and locally uniformly on Re w>1. Reflection and the xi definition give

\[
 L_t(w)=\lambda+\ell(w),\qquad
 H_t(i(w-\tfrac12))=(1-t)\cosh(w-\tfrac12)
          (1+e^{\lambda+\ell(w)}).                            \tag{2.2}
\]

The cosh factor is nonzero here. Consequently the complete zero condition is

\[
 \lambda+\ell(w)=(2m+1)\pi i,\qquad m\in\mathbb Z.           \tag{2.3}
\]

The canonical first-quadrant negative phase is -iq_n, q_n=(2n+1)pi, m=-n-1; no phase offset is changed. At an odd level, multiplication by the nonzero local factor (1+e^L)/(L-(2m+1)pi i) preserves multiplicity. These identities are rechecked directly from source/quantitative/QUANTITATIVE_PROOF.md, section 2, (11)–(18). The normalizations agree with [DLMF 25.4.3–4](https://dlmf.nist.gov/25.4) and [DLMF 25.2.11](https://dlmf.nist.gov/25.2#E11).

For E1 only, retain the established bound

\[
 \Re\ell'(w)>5/16\quad(\Re w\ge a).                         \tag{2.4}
\]

Here is its quantitative check. The exact decomposition (3.1) below gives ell'=1/2 Log(w/a)+1/2+3/(2w)+E'. The inherited derivative estimate, on its original domain Re w>=2, is

\[
 |E'|\le10/|w|^2+5\,2^{-\Re w}+3e^{1-2\Re w}.
\]

For Re w>=a>32, the logarithmic real part is nonnegative, Re(1/w)>0, and each of the three losses is strictly below 1/16. This proves (2.4). The exact source proof is completeness sections 2–4 (U1–U3); the quantitative section 3 Cauchy argument proves the derivative bound rather than differentiating a formal error. The current audit sections 2–4 and dependency check sections 2–3 have the same domain qualifications.

Let D={Re w>a}. For distinct w_1,w_2 in D, the difference quotient of ell is the integral of ell' on their segment and has real part >5/16. Thus ell is injective on D. Also

\[
 \Im\ell(\sigma+iv)=\int_0^v\Re\ell'(\sigma+iu)\,du,
 \qquad |\Im\ell(\sigma+iv)|\ge(5/16)|v|.                  \tag{2.5}
\]

This is the direct positive-real-derivative argument, a classical univalence criterion, not a new method; see [Hotta–Wang, Theorem 1.A](https://arxiv.org/html/1401.5647).

Fix an actual root w_0 in D at lambda_0 and its fixed odd level ip, p=(2m+1)pi. Let J be the connected component containing lambda_0 of

\[
 \{\lambda\in\mathbb R:ip-\lambda\in\ell(D)\}.
\]

The inverse of ell defines the unique branch w(lambda) on J. The implicit function theorem yields, exactly on this interval,

\[
 \frac{dw}{d\lambda}=-\frac1{\ell'(w)},\qquad
 \frac{d\Im z}{d\lambda}=-\Re\frac1{\ell'(w)}<0,
 \qquad \left|\frac{dw}{d\lambda}\right|<16/5.               \tag{2.6}
\]

Indeed Re(1/ell')=Re ell'/|ell'|^2>0 and |ell'|>5/16. Every represented root is simple.

One can specify J more sharply: J=(-infinity,beta) for a finite beta>lambda_0, and Re w tends to a at beta. To prove this, (2.5) bounds |Im w| by 16|p|/5. In the forward direction Re w decreases and is bounded below by a, so if J extended to arbitrarily large lambda the entire branch would stay in a compact rectangle in Re w>=a. The continuous ell is bounded there, contradicting Re ell(w)=-lambda. Thus the right endpoint beta is finite. The speed bound makes w Cauchy as a finite endpoint is approached. If its limiting real part exceeded a, the implicit function theorem would continue the branch inside D, a contradiction; hence it tends to a. In the backward direction, a finite left endpoint would have Re w>=Re w_0>a and bounded distance from w_0 by the speed bound, again permitting continuation. Therefore that endpoint is -infinity. This is an exterior-branch result only. The finite exit is through height a-1/2, not a collision with the real axis; no continuation or labeling all the way to t=1 is claimed.

## 3. Uniform estimates on every fixed Euler exterior

The exact decomposition, with no t-dependent remainder, is

\[
 \ell(w)=\frac w2\Log(w/a)+\frac32\Log w+c_0+E(w),           \tag{3.1}
\]
\[
 E(w)=\Log(1-1/w)+S_\Gamma(w)+L_\zeta(w)
                       -\log(1+e^{1-2w}),
\]
\[
 S_\Gamma(w)=\log\Gamma(w/2)
 -[(w/2-1/2)\Log(w/2)-w/2+\tfrac12\log(2\pi)].
\]

For every fixed r>1 set

\[
 M_r=\frac1{r-1}+\frac1{3r}+\log\zeta(r)
                  +\frac{e^{1-2r}}{1-e^{1-2r}}.
\]

Then, on the entire closed half-plane Re w>=r,

\[
 |E(w)|\le M_r.                                             \tag{3.2}
\]

The first logarithm is bounded by 1/(|w|-1), the Euler logarithm by log zeta(r), and the last logarithm by its absolute power series. Complex log-Gamma Stirling with first neglected term 1/(6w) gives |S_Gamma(w)|<=1/(3|w|), since sec^2(arg(w)/2)<=2 in the right half-plane. This uses the log-Gamma remainder, not the different Gamma-series remainder. [DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11). These estimates establish (3.2) for all r>1 directly, including r<2.

For r>1 define r_-=(r+1)/2, delta_r=(r-1)/2, and K_r=M_(r_-)/delta_r. Every radius-delta_r disk centered in Re w>=r remains in Re w>=r_->1. Cauchy's formula applied to (3.2) gives

\[
 |E'(w)|\le K_r,\qquad
 |E''(w)|\le2M_{r_-}/\delta_r^2\qquad(\Re w\ge r).          \tag{3.3}
\]

No inherited Re w>=2 bound has been used below 2. These are uniform in the imaginary part and have no lambda dependence.

Write ell'=A+iB and set C_r=(log a)/2+K_r+1. Differentiating the exact explicit part in (3.1), using (3.3), proves

\[
 A(w)\ge\tfrac12\log|w|-C_r,
 \qquad |B(w)|\le\tfrac\pi4+\frac3{2r}+K_r.                \tag{3.4}
\]

In particular, with X_r=max(1,exp(4C_r)),

\[
 A(\sigma-ix)\ge\tfrac14\log x>0
 \quad(\sigma\ge r,\ x\ge X_r).                            \tag{3.5}
\]

On any fixed band r<=sigma<=r+1, we also have A=1/2 log x+O_r(1) as x tends to infinity. Equations (3.1) and (3.3) give a uniform bound on ell'' on each fixed exterior Re w>=r; this will justify the optional complex profile.

Hereafter fix d>1/2 and abbreviate

\[
 s=d+\tfrac12>1,\quad \kappa=\pi/4,\quad
 b=s/2+3/2=d/2+7/4,
 \quad T(\lambda)=\kappa^{-1}\lambda+(b/\kappa)\log\lambda.
\]

Put U(sigma,x)=Re ell(sigma-ix), V(sigma,x)=Im ell(sigma-ix), and F_lambda=lambda+U. For x>=1, the exact real part in (3.1), with rho=(s^2+x^2)^(1/2) and theta=arctan(x/s), gives

\[
 U(s,x)=\frac{s}{2}\log(\rho/a)-\frac{x\theta}{2}
                         +\frac32\log\rho+c_0+\Re E(s-ix).
\]

Since theta=pi/2-arctan(s/x), 0<=log(rho/x)<=s^2/(2x^2), and 0<=x arctan(s/x)<=s, it follows that

\[
 |U(s,x)+\kappa x-b\log x|\le P_s\quad(x\ge1),             \tag{3.6}
\]

where one possible constant is

\[
 P_s=bs^2/2+(s/2)\log a+s/2+c_0+M_s.
\]

All constants here are fixed before lambda is allowed to grow. The bounded Euler and cosh contributions are not assumed to converge.

## 4. Exclusion of all lower-radius exterior roots

Evenness and conjugation reduce any root with |Im z|>=d to z=x+iy with x>=0 and y>=d. The corresponding sigma=y+1/2 satisfies sigma>=s, so (2.3) implies F_lambda(sigma,x)=0.

First handle 0<=x<=X_s at every height. Choose S>=s so large that (log S)/2-C_s>=1. From (3.4), partial_sigma U>=1 on sigma>=S. Let m_s be the minimum of U on the compact rectangle [s,S] x [0,X_s]. For sigma>=S,

\[
 U(\sigma,x)\ge U(S,x)+(\sigma-S)\ge m_s.
\]

The same lower bound holds on the rectangle. Thus F_lambda>0 everywhere in this unbounded bounded-x region when lambda>-m_s. Compact convergence by itself would not have sufficed here.

For x>=X_s, (3.5) makes F_lambda strictly increasing in sigma on the entire interval [s,infinity). A zero therefore forces F_lambda(s,x)<=0. By (3.6),

\[
 \kappa x\ge\lambda+b\log x-P_s.                          \tag{4.1}
\]

As x>=1, for large lambda this first implies x>=lambda/(2 kappa). Substituting that inequality back into (4.1) gives

\[
 x\ge T(\lambda)-C_L,
 \qquad C_L=\frac{P_s+b|\log(2\kappa)|}{\kappa}.            \tag{4.2}
\]

Consequently every root with |Im z|>=d has |z|>=T(lambda)-C_L. This covers arbitrarily large heights and possible exceptional zeros from old fixed-t decompositions. Neither completeness, a fixed-t big-O substitution, nor control of an exceptional multiset is used.

## 5. A true simple root within the upper radius

Set

\[
 Q_s=P_s+b(|\log(\kappa^{-1})|+1),\quad
 C=(Q_s+2)/\kappa+1,\quad J=\kappa(C+1)+Q_s,
 \quad h_\lambda=4(J+1)/\log\lambda.
\]

These constants depend only on s. Uniformly for c in any fixed bounded interval,

\[
 \lambda-\kappa(T(\lambda)+c)+b\log(T(\lambda)+c)
 =-\kappa c+b\log\frac{T(\lambda)+c}{\lambda},
\]

and the last logarithm tends uniformly to log(kappa^-1). Hence, for large lambda and all

\[
 x\in I_\lambda=[T(\lambda)+C,T(\lambda)+C+1],
\]

(3.6) implies

\[
 -J\le F_\lambda(s,x)\le-2.                               \tag{5.1}
\]

For these x, eventually x>=lambda and (3.5) gives A>=1/4 log lambda for every sigma>=s. Thus

\[
 F_\lambda(s+h_\lambda,x)\ge-J+(h_\lambda/4)\log\lambda=1.
                                                                    \tag{5.2}
\]

The intermediate value theorem and strict increase in sigma give a unique solution sigma_lambda(x) in (s,s+h_lambda) to F_lambda=0 for each x in I_lambda. The real implicit function theorem gives a smooth curve, including smooth local extensions at its endpoints. With ell'=A+iB evaluated on the curve, the chain rule gives

\[
 \partial_\sigma U=A,\quad \partial_xU=B,\quad
 \partial_\sigma V=B,\quad \partial_xV=-A,
\]
\[
 \sigma_\lambda'(x)=-B/A,\qquad
 \frac d{dx}V(\sigma_\lambda(x),x)
          =-\frac{A^2+B^2}{A}\le-\tfrac14\log\lambda.       \tag{5.3}
\]

Over this interval of length 1 the continuous phase therefore decreases by more than 2pi for large lambda. It must meet an odd multiple of pi in the interior. At that point F_lambda=0 as well, so (2.3), not merely modulus balance, gives an actual H_t zero. It is simple because Re ell'>0 there. Its coordinates satisfy

\[
 T(\lambda)+C<x<T(\lambda)+C+1,\qquad
 d<y<d+h_\lambda.                                          \tag{5.4}
\]

For large lambda, y<=d+1 and x is comparable to lambda. Since

\[
 0\le\sqrt{x^2+y^2}-x=\frac{y^2}{\sqrt{x^2+y^2}+x}
                  \le\frac{(d+1)^2}{2x},
\]

the root has |z|<=T(lambda)+C+2. Together with (4.2), this proves E2, including its required existence and all-root lower bound, even with a bounded remainder after retaining the logarithmic term. Analytic multiplicities are preserved throughout, and the constructed root has multiplicity one.

## 6. The two-term theorem and the moving original phase (E3–E4)

The estimates in sections 4–5 immediately give (T), since b/kappa=(2d+7)/pi. This proves the optional E3 refinement on precisely the full root set requested, as well as the weaker E2 statement R_d=4lambda/pi+O_d(log lambda). The proof does not assert existence of a limiting constant in the bounded remainder.

There is also useful information about minimizers. The upper construction shows the set is nonempty for large lambda. H_t is a nonzero entire function, and only finitely many zeros lie in any compact disk. Thus R_d is attained. Reflect minimizers to the first quadrant and choose the one with smallest positive real part if there is more than one. This is a definition at each lambda, not a continuous branch or a rank ordering of the old tail.

More generally, any root with y>=d and |z|<=T(lambda)+C+2 has

\[
 T(\lambda)-C_L\le x\le T(\lambda)+C+2.
\]

Equation (3.6) then bounds |F_lambda(s,x)| by a constant depending only on s. Since F_lambda(sigma,x)=0 and (3.5) holds for every intermediate height,

\[
 0\le\sigma-s\le O_s(1/\log\lambda).                     \tag{6.1}
\]

This proves y=d+O_d(1/log lambda) for every minimizing representative; it does not assume in advance that the minimizing height stays bounded.

For sigma in [s,s+1], (3.1) gives directly, uniformly as x tends to infinity,

\[
 -\Im\ell(\sigma-ix)
 =\frac x2\log(x/a)+O_s(1).                                \tag{6.2}
\]

Indeed the exact expression is x/2 log(rho/a)+(sigma/2+3/2)theta-Im E, where rho=(sigma^2+x^2)^(1/2) and theta=arctan(x/sigma); replacing rho by x changes the first term by O_s(1/x), while the remaining terms are bounded. In particular the phase is negative for large x. Every root in the preceding radius range, including the selected minimizer and the root in (5.4), therefore has the original canonical level

\[
 \lambda+\ell(w)=-iq_n,\quad q_n=(2n+1)\pi,
 \quad n\ge0,
\]

and, since x=4lambda/pi+O_d(log lambda),

\[
 q_n\sim\frac2\pi\lambda\log\lambda,\qquad
 n\sim\frac{\lambda\log\lambda}{\pi^2}.                    \tag{6.3}
\]

This derives E4 from the canonical logarithm in the joint limit. It identifies a phase index and makes no assertion that it is a global radial rank or that an old sufficient N(t) is a transition radius. Different minimizing roots may be selected at different parameters.

## 7. A phase-retaining local profile (E5)

Define x_lambda=T(lambda)+C explicitly and use the unique scalar modulus solution from section 5 at that x:

\[
 w_\lambda=\sigma_\lambda(x_\lambda)-ix_\lambda,
 \qquad \Re(\lambda+\ell(w_\lambda))=0.
\]

This basepoint is defined by a real monotone balance equation, without imposing the original complex zero equation or choosing an already known zero. It could accidentally be a zero for some parameters; no such property is used. Let

\[
 p_\lambda=\ell'(w_\lambda),\qquad
 \eta_\lambda=e^{i\theta_\lambda}
             =e^{\lambda+\ell(w_\lambda)},\quad |\eta_\lambda|=1.
\]

Retain eta_lambda, including its canonical Euler/cosh contributions. On the complex scale

\[
 w=w_\lambda+v/p_\lambda,
\]

we have p_lambda=1/2 log lambda+O_d(1)+iO_d(1), so this is a scale of order 1/log lambda. For every fixed compact v-set, the corresponding w-set lies in Re w>1 for all large lambda, even when it crosses the line Re w=s. Choose once and for all r=(s+1)/2>1. The uniform ell'' bound following (3.3) on Re w>=r and the integral Taylor remainder give

\[
 \ell(w_\lambda+v/p_\lambda)-\ell(w_\lambda)
       =v+O_{d,K}((\log\lambda)^{-2})\quad(v\in K).         \tag{7.1}
\]

The normalized original functions consequently satisfy

\[
 \mathcal G_\lambda(v):=
 \frac{H_t(i(w_\lambda+v/p_\lambda-1/2))}
 {(1-t)\cosh(w_\lambda+v/p_\lambda-1/2)}
 =1+\eta_\lambda e^v+O_{d,K}((\log\lambda)^{-2}),           \tag{7.2}
\]

locally uniformly in v. The denominator is nonzero on these neighborhoods. From any sequence lambda_j tending to infinity, compactness of the unit circle supplies a subsequence with eta_(lambda_j) tending to eta. On that subsequence

\[
 \mathcal G_{\lambda_j}\longrightarrow1+\eta e^v
\]

locally uniformly. Its simple zeros form the lattice v=i((2k+1)pi-theta), eta=e^(i theta), k in Z. Rouché on small disjoint circles around finitely many such lattice points gives the corresponding simple zeros of the normalized original functions for sufficiently large j. This is a local assertion within the Euler domain; not every such local point is claimed to lie above height d.

Equation (7.2) is the asserted profile; an unqualified universal phase limit is not asserted. Its analytic mechanism is generic Taylor linearization with a non-root modulus basepoint. The contribution specific to this family is the verified original-coordinate basepoint, scale and uniform Euler/Stirling control. No new theta-specific universality theorem or PDE transfer is claimed.

## 8. Dependency and scope record

The endpoint proof uses the exact identities and elementary classical complex analysis. The old fixed-t localization disks, their correction h_(n,t), sufficient threshold N(t), completeness theorem and finite exceptional multiset are not premises of sections 3–7. Only E1 uses the old U1–U3 on their original half-plane; their proof and audits were read in the permitted packet. The new Cauchy bounds supply the missing uniformity at every fixed d>1/2 before taking the endpoint limit.

No numerical root scan or numerical root evidence was used. No Xi simplicity assumption, radial ordering, uniformly bounded exceptional set, continuation through the critical strip, unique residual phase limit, or RH conclusion is present. The first author proof is complete on these scopes, with no identified remaining mathematical gap, but remains subject to SOL review. Literature comparison is bounded and separate from correctness; world novelty is not established.

STOP_FOR_SOL_REVIEW after the first completed output freeze.
