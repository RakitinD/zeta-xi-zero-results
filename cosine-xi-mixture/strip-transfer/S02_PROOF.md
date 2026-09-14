# Quantified zero-cluster and phase transfer in a fixed strip window

Researcher COSXI-S02. First author result, awaiting review; no independent audit or historical-novelty certification. All zero counts use analytic multiplicity. All logarithms of positive real numbers are natural.

## 1. Statement and exact parameter regime

Fix \(0<\delta<1/2\). Put
\[
 a=\tfrac12+\delta,\quad h=\delta/4,\quad s_0=\tfrac12+\delta/4,
 \quad q=1-\delta/16,\quad r=T^{-2},\quad H_0=3.0610046\,10^{10}.
\]
Here \(a\) is only a strip edge; it is not the unrelated constant named \(a\) in the inherited Euler-exterior proof. Define
\[
 \Omega=\{\sigma-ix:a\leq\sigma\leq2,\ T\leq x\leq2T\},
\]
\[
 C=\{\sigma-ix:a-h\leq\sigma\leq2+h,\ T-1\leq x\leq2T+1\}.
 \tag{1}
\]
The collar stays to the right of \(1/2\). Write
\[
 J_q(Y)=10395.2Y^q\log Y+1.104(\log Y)^2
       +0.173\log Y\log\log Y+0.51\log Y,
\]
\[
 Q_\delta(T)=J_q(T/2)+J_q(T)+J_q(2T).
 \tag{2}
\]
For clarity the large-height hypotheses will be the explicit inequalities
\[
 T\geq2H_0,\qquad 4T^{-2}Q_\delta(T)<\min(h,1).
 \tag{3}
\]
They hold eventually for every fixed \(\delta\), since
\(Q_\delta(T)=O_\delta(T^{1-\delta/16}\log T)\).

The completely explicit analytic loss and parameter threshold used below are
\[
 F(T)=\left(25+\frac{\log4+2\log T}{\log(15/14)}\right)\log(200T),
\]
\[
 \Lambda(T)=\frac{\pi(2T+1)}4+F(T)+\frac14\log(3T)+6+\log(4T).
 \tag{4}
\]
Throughout the transfer theorem
\[
 \lambda\geq\Lambda(T),\qquad
 t=\frac{e^\lambda}{1+e^\lambda},\quad c=e^{-\lambda}.
 \tag{5}
\]
Thus the theorem includes the joint choice \(\lambda=\Lambda(T)\sim\pi T/2\), and, for every fixed \(\epsilon>0\), the choice \(\lambda=(\pi/2+\epsilon)T\) for all sufficiently large \(T\). The general inequality (5) only implies \(T=O(\lambda)\), not two-sided comparability. There is no fixed-\(t\), \(T\to\infty\) claim.

Let \(\mathcal Z\) be the finite multiset of zeta zeros
\[
 \rho=\beta-i\gamma,\qquad \beta\geq a-2h=\tfrac12+\delta/2,
 \quad T-2\leq\gamma\leq2T+2,
 \tag{6}
\]
and let \(M\) be its total multiplicity. For each distinct zero choose one disk
\(\{|w-\rho|<r_\rho\}\), with \(r<r_\rho<2r\), and choose the finitely many radii in general position (no tangencies or triple boundary intersections). Let \(E\) be their union. A component \(U_j\) is relevant if its closure meets \(\Omega\); write \(M_j\) for the sum of the multiplicities of its centers.

**Theorem S02-T (AUTHOR_PROVED).** Under (3) and (5):

1. \(M\leq Q_\delta(T)\). The ordinate projection of \(E\) has Lebesgue measure at most \(4rQ_\delta(T)=O_\delta(T^{-1-\delta/16}\log T)\). Every relevant component has closure in the interior of \(C\) and diameter at most \(4rM_j\).
2. All zeros of \(H_t(i(w-1/2))\) in the closed window \(\Omega\) lie in relevant components. Each full relevant component contains exactly \(M_j\) such zeros, with multiplicity, and exactly \(M_j\) zeros of \(\xi\). Neither function vanishes on its boundary.
3. Let \(N_H(\Omega)\) and \(N_\xi(\Omega)\) count zeros on the closed window, including its boundary. Define the explicit boundary charge
\[
 B_\Omega=\sum_{\overline U_j\cap\partial\Omega\ne\varnothing}M_j
 \quad\text{(sum over relevant components)}.
\]
Then
\[
 |N_H(\Omega)-N_\xi(\Omega)|\leq B_\Omega\leq M\leq Q_\delta(T),
 \qquad N_H(\Omega)\leq Q_\delta(T)=o(T).
 \tag{7}
\]
The same assertions hold if both counts use the open window. If \(B_\Omega=0\), the count equality is exact. No assumption excluding original window-boundary zeros is needed for the charged inequality.
4. On every zero-free path in \(C\setminus E\), continuously lifted phases of \(H_t(i(w-1/2))\) and \(\xi(w)\) have changes differing by at most \(2/(3T)\). On every closed contour there, their windings agree exactly. For a positively oriented full component boundary,
\[
 \frac1{2\pi i}\int_{\partial U_j}D(w)\,dw=M_j,
 \qquad D=P'/P,\quad P=\xi/\cosh(w-1/2).
 \tag{8}
\]
Thus deleting one boundary circuit per relevant component deletes exactly total phase \(2\pi\sum_j M_j\leq2\pi Q_\delta(T)\), not a quantity controlled by its shrinking geometric size. Repeated circuits have the corresponding repeated charge.

The upper bound in (7) is information about the mixture obtained from a known zeta estimate. It is not an improved estimate for zeta. Under RH the centers in (6) are absent; the theorem never assumes that absence. It does not guarantee that there is an off-axis zeta or mixture zero in this window.

An explicit nonvacuity example is \(\delta=1/4\), \(T=e^{2000}\), \(\lambda=\Lambda(T)\). Then \(q=63/64\). For \(Y=cT\), \(c\in\{1/2,1,2\}\), we have \(\sum c^q<4\) and \(\log Y<2001\), so the sum of the leading terms in \(Q_\delta(T)/T\) is less than \(10^8e^{-31.25}<5\,10^{-6}\): use \(e>2.7\) and \(2.7^{31}>2\,10^{13}\). The other terms total less than \(10^8e^{-2000}<10^{-592}\), since \(e^{2000}>2^{2000}>10^{600}\). Hence \(Q_{1/4}(e^{2000})/e^{2000}<10^{-5}\), and (3) holds. This is a calculation of theorem parameters, not a numerical claim about zero locations. It also illustrates how conservative the selected density constant and collar loss are.

## 2. Arithmetic input and collar accounting

The sole zero-density theorem actually inserted is Aleksander Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, arXiv:1910.08274v2, Theorem 1, with
\(N(s,Y)=\sum_{\beta>s,\ 0<\gamma\leq Y}m_\rho\).
Its unconditional statement is
\[
 N(s,2Y)-N(s,Y)
 \leq10395.2Y^{1-(s-1/2)/4}\log Y
 +1.104(\log Y)^2+0.173\log Y\log\log Y+0.51\log Y
 \tag{9}
\]
for \(Y\geq H_0\), \(1/2\leq s\leq0.831\).
[Primary theorem](https://arxiv.org/html/1910.08274v2).
It is a proved estimate cited as an arithmetic input, not re-audited here.

Because \(s_0\in(1/2,5/8)\), its range matches every fixed \(\delta\) above. Conjugation preserves zeros and their multiplicities. Each zero in (6) has reflected positive ordinate strictly between \(T/2\) and \(4T\), and real part strictly greater than \(s_0\). Consequently
\[
 M\leq N(s_0,4T)-N(s_0,T/2)
 \leq J_q(T/2)+J_q(T)+J_q(2T)=Q_\delta(T).
 \tag{10}
\]
This uses only three applications of (9), all with \(Y\geq H_0\); it does not require a global count obtained by extending (9) to small heights. The strict/non-strict real-part conventions in (6) and (9) are reconciled by the positive gap \(\delta/4\). The collar and this gap cost a factor four in the available displacement from \(1/2\); the Selberg coefficient \(1/4\) then gives \(\delta/16\).

There are at most \(M\) distinct disks, their radii sum to at most \(2rM\), and each ordinate projection has length \(2r_\rho\). The projection bound follows by subadditivity, with no independence assumption. A connected disk union has diameter at most twice the sum of its radii: follow a simple chain in its overlap graph and use the triangle inequality; include the endpoint radii. Hence
\[
 \operatorname{diam}(\overline U_j)\leq4rM_j\leq4rQ_\delta(T).
 \tag{11}
\]
A relevant closure contains a point of \(\Omega\), whose distances to the vertical and horizontal edges of \(C\) are at least \(h\) and \(1\). Equations (3) and (11) therefore place that entire closure strictly inside \(C\). General-position radii exist because the finitely many tangency and triple-intersection conditions exclude only proper lower-dimensional sets of choices. Boundaries are finite unions of piecewise smooth Jordan curves with their domain orientations; holes are allowed.

These are bounds for projected ordinate length and for integer charge. No estimate of planar area, or identification of area with charge, is used.

## 3. A uniform elementary minimum-modulus bound

This section re-proves a standard minimum-modulus device, with constants for the present strip. It is not a new zeta estimate.

**Lemma S02-M.** For \(T\geq10\), \(1/2\leq\sigma\leq17/8\), \(T-1\leq x\leq2T+1\), and \(0<d\leq1\), if \(w=\sigma-ix\) has distance at least \(d\) from every zeta zero, then
\[
 \log|\zeta(w)|\geq
 -\left(25+\frac{\log(4/d)}{\log(15/14)}\right)\log(200T).
 \tag{12}
\]

**Proof.** Set \(z_0=2-ix\), \(f(u)=\zeta(z_0+u)\). On the disk
\(|u|\leq15/8\) we have \(\Re(z_0+u)\geq1/8\), and the pole \(1\) is outside. Partial summation of the defining series, followed by analytic continuation of the absolutely convergent integral, gives
\[
 \zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{v\}v^{-s-1}\,dv
 \quad(\Re s>0,\ s\ne1).
 \tag{13}
\]
Thus \(|\zeta(s)|\leq |s|/|s-1|+|s|/\Re s\leq100T=:A_T\) on this disk for \(T\geq10\): here \(|s|\leq2T+4.875\), \(|\Im s|\geq T-2.875\), and \(\Re s\geq1/8\). The convergent reciprocal Euler series at \(\Re z_0=2\) gives
\[
 |f(0)|\geq1/\zeta(2)>1/2.
\]
Jensen's formula on radii approaching \(15/8\), or directly when there are no boundary zeros, bounds the number \(n\), with multiplicity, of zeros in any disk of radius at most \(7/4\) by
\[
 n\leq\frac{\log(2A_T)}{\log(15/14)}.
 \tag{14}
\]
The limiting argument needs no positive boundary minimum, only the uniform upper bound. The Jensen identity here follows by factoring the finitely many zeros inside a zero-free boundary circle and applying the harmonic mean-value identity to the remaining logarithmic modulus; each removed zero contributes \(\log(R_{out}/|\alpha|)\).

Choose \(R\in(13/8,7/4)\) with no zero on \(|u|=R\), and remove all its zeros \(\alpha\), with multiplicity, by the finite Blaschke product
\[
 B(u)=\prod_\alpha\frac{R(u-\alpha)}{R^2-\bar\alpha u}.
\]
Unimodular normalizing constants are irrelevant. Each factor has boundary modulus one and interior modulus at most one. The quotient \(g=f/B\), with cancellations filled in, is analytic and zero-free on the closed \(R\)-disk. The maximum principle gives \(|g|\leq A_T\), and
\(|g(0)|\geq|f(0)|>1/2\).
The nonnegative harmonic function \(\log A_T-\log|g|\) satisfies the Harnack estimate
\[
 \log A_T-\log|g(u)|
 \leq25\log(2A_T)\quad (|u|\leq3/2);
\]
indeed \((R+3/2)/(R-3/2)<25\). This disk form of Harnack follows directly from the Poisson formula: its nonnegative boundary values are integrated against a kernel at most \((R+|u|)/(R-|u|)\) times the center kernel.
At the target \(u=\sigma-2\), we have \(|u|\leq3/2\). Its distance assumption gives
\[
 \left|\frac{R(u-\alpha)}{R^2-\bar\alpha u}\right|
 \geq\frac{|u-\alpha|}{R+|u|}\geq d/4.
\]
Multiplying and using (14), then discarding the positive \(\log A_T\) term, proves (12). Jensen and Harnack are applied on actual two-dimensional disks. There is no inference from a distribution on one vertical line. \(\square\)

For \(w\in C\setminus E\), every zero in (6) is at distance greater than \(r\). Every omitted nontrivial zero has either real part below \(a-2h\), or ordinate outside \([T-2,2T+2]\); its distance from \(C\) is therefore at least \(h\) or \(1\). Trivial zeros are far from this high collar. Equation (3) implies \(r<h\), since \(Q_\delta(T)>1\) for \(T\geq2H_0\). Thus every zeta zero has distance at least \(r\) from \(w\). Applying (12) with \(d=r\) yields
\[
 \log|\zeta(w)|\geq-F(T)\quad(w\in C\setminus E).
 \tag{15}
\]
If \(\mathcal Z\) is empty, the same statement follows from the distances to the omitted half-plane and ordinate bands; the definition of \(Q_\delta(T)\), not \(M\), still guarantees \(r<h\).

## 4. Completion factors and domination in the expanding collar

The functional equation gives exactly
\[
 \Xi(i(w-\tfrac12))=\xi(w),\quad
 H_t(i(w-\tfrac12))=t\cosh(w-\tfrac12)(P(w)+c).
 \tag{16}
\]
These agree with the checked inherited canonical quotient. Since all zeros of \(\cosh(w-1/2)\) have real part \(1/2\), it is nonzero in our collar. Thus \(P\) is analytic there, its zeros are precisely those of \(\xi\), and at high ordinates these are precisely the zeta zeros, with the same multiplicities. There are no poles of \(P\) in any domain used in this proof.

For transparency an explicit lower bound on the completion factor
\[
 K(w)=\frac{\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2)}
                    {\cosh(w-1/2)},\quad P=K\zeta
\]
is enough. Sector Stirling with its log-Gamma remainder gives, writing
\(\theta=\arctan(x/\sigma)\),
\[
 \log|\Gamma(w/2)|
 =(\sigma/2-1/2)\log(|w|/2)-x\theta/2-\sigma/2
   +\tfrac12\log(2\pi)+\Re S_\Gamma(w),
\quad |S_\Gamma(w)|\leq1/(3|w|).
 \tag{17}
\]
The branch is the analytic log-Gamma normalized on the positive real ray.
[DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11).
On \(C\), \(1/2<\sigma<17/8\), \(x\geq T-1\geq9\), and \(|w|\leq3T\). In (17) use
\(\theta\leq\pi/2\), \(\sigma/2-1/2\geq-1/4\), and
\(\log(|w|/2)\geq0\). Also \(|w|,|w-1|\geq x\geq1\), and
\(|\cosh(w-1/2)|\leq e^{\sigma-1/2}\). Dropping positive terms proves
\[
 \log|K(w)|\geq-\pi x/4-\tfrac14\log(3T)-6.
 \tag{18}
\]
The constant 6 is valid because
\(\log2+(17/16)\log\pi+17/16+13/8+1<6\).
No lower bound on \(\zeta\) was hidden in (17) or (18).

Combining (15), (18), and \(x\leq2T+1\) gives
\[
 |c/P(w)|\leq
 \exp\{-\lambda+\pi(2T+1)/4+F(T)+\tfrac14\log(3T)+6\}
 =:\varepsilon_{\lambda,T}
 \leq1/(4T)
 \tag{19}
\]
on all of \(C\setminus E\). In particular \(P+c\) has no zero there.

Each relevant component has its closure in the interior of \(C\). On every part of its boundary, (19) holds. For \(v\in[0,1]\), \(P+vc\) is nonvanishing on that boundary. The argument principle makes its total zero count constant under this homotopy. It starts with \(M_j\), because all zeta zeros in the component occur as centers in (6), with their multiplicities, and the other completion factors are nonzero. This proves the cluster count for \(P+c\), and then for \(H_t\) by (16). The argument principle is applied to the full oriented boundary if the union has holes; inner boundaries have clockwise orientation. Any holes contain no zeta zero, since every such zero in \(C\) is a disk center.

All zeros in \(\Omega\) are in the relevant union by (19). Components whose closures meet \(\Omega\) but avoid \(\partial\Omega\) are entirely in the open window; their counts match exactly. For each boundary component the two partial closed-window counts are each between 0 and \(M_j\), so their difference in absolute value is at most \(M_j\). Summing proves (7), including boundary multiplicities. This derivation never integrates over a rectangle boundary that might contain a zero.

A further precise consequence is an arbitrary multiplicity-respecting bijection of the two zero multisets in each full relevant component, with each matched pair at distance at most \(4rM_j\). There is no assertion of individual analytic trajectories, simplicity, or unique matching.

## 5. Chartwise phase and the charged information that is lost

On a neighborhood of each point in \(C\setminus E\) one may choose a log of \(P\). On connected chart overlaps two such logarithms differ by \(2\pi i k\), \(k\in\mathbb Z\). A chart reachable from the inherited Euler region can be normalized by continuation of that canonical logarithm; different paths have the integer periods described below. No global logarithm of \(P\) on the perforated collar is claimed.

Unlike \(\log P\), the correction
\[
 q_\lambda(w)=\operatorname{Log}(1+c/P(w))
             =\sum_{n\geq1}\frac{(-1)^{n+1}}n(c/P(w))^n
 \tag{20}
\]
is single-valued on the open set \(\{|c/P|<1\}\). By (19),
\[
 |q_\lambda|\leq\varepsilon_{\lambda,T}/(1-\varepsilon_{\lambda,T})
 \leq1/(3T).
 \tag{21}
\]
A compatible chart log of \(P+c\) is \(\log P+q_\lambda\), and it has exactly the same integer overlap offsets. The same correction relates logs of \(H_t(i(w-1/2))/t\) and \(\xi(w)\), since their quotient is \(1+c/P\). Therefore for any piecewise smooth path \(\gamma\) in \(C\setminus E\), with continuous phase lifts along the path,
\[
 \Delta_\gamma\arg H_t(i(w-\tfrac12))-\Delta_\gamma\arg\xi(w)
 =\Im(q_\lambda(\gamma(1))-q_\lambda(\gamma(0))),
 \tag{22}
\]
giving the asserted \(2/(3T)\) bound. Adding a constant integer to a chosen lift changes neither phase change. On closed paths the right side is zero exactly.

For a zero of multiplicity \(m\), local factorization gives
\(P(w)=(w-\rho)^mg(w)\), \(g(\rho)\ne0\), hence
\[
 D(w)=m/(w-\rho)+g'(w)/g(w).
\]
Its positive small-circle period is \(2\pi i m\). On a full component boundary the residue theorem sums these multiplicities, proving (8). The nonzero cosh factor has a holomorphic logarithm in \(\Re w>1/2\), so it contributes no closed-contour winding. Merging disks changes neither the sum of residues nor the cluster count.

More generally any closed path in this half-plane that avoids zeros has
\[
 \frac1{2\pi i}\int_\gamma D\,dw
 =\sum_\rho m_\rho\,\operatorname{Ind}(\gamma,\rho)
\]
over its bounded winding support. Thus a phase gluing step must retain the indicated integer, and arbitrary repeated detours cannot be bounded by \(M\) without their winding multiplicities. For a single circuit per deleted relevant component the total charge is at most \(2\pi Q_\delta(T)\). The projection of those holes tends to zero, whereas the permitted integer charge need not tend to zero. In this parameter regime **all actual mixture zeros in the window occur in the holes**; ignoring them would discard the entire mixture count, even though their ordinate projection is small.

## 6. What the monotone-phase criterion does and does not supply

Off zeros direct differentiation gives
\[
 D=\frac{\zeta'}{\zeta}+\frac1w+\frac1{w-1}
 -\tfrac12\log\pi+\tfrac12\psi(w/2)-\tanh(w-\tfrac12).
 \tag{23}
\]
On the fixed collar \(|\tanh(w-1/2)|\leq\coth(a-h-1/2)\). The digamma expansion with its sector remainder, or Cauchy's estimate applied to the analytic remainder in (17) on a fixed relative disk, gives
\[
 \Re D(\sigma-ix)=\tfrac12\log T+
             \Re\frac{\zeta'}{\zeta}(\sigma-ix)+R_\delta(w,T),
 \quad |R_\delta(w,T)|\leq C_\delta.
 \tag{24}
\]
Here \(C_\delta\) is an effective fixed constant; this is an estimate only on the explicit non-arithmetic terms, not on the logarithmic derivative of zeta. For any \(0<\kappa<1/2\), the one-sided arithmetic condition
\[
 \Re(\zeta'/\zeta)\geq-(1/2-\kappa)\log T+C_\delta
 \tag{25}
\]
suffices for \(A=\Re D\geq\kappa\log T\).

For any local log \(U+iV=\log P\), the chain rule in \(w=\sigma-ix\) yields
\[
 U_\sigma=A,\ U_x=B,\ V_\sigma=B,\ V_x=-A,\qquad D=A+iB.
\]
On a connected \(C^1\) modulus graph \(\lambda+U(\sigma(x),x)=0\), with \(A>0\),
\[
 \sigma'=-B/A,\qquad V'=-(A^2+B^2)/A.
 \tag{26}
\]
A continuous phase lift exists along the graph, an interval; a global collar log is unnecessary.

For completeness the following **conditional application** has the necessary break penalty. If \(J\) pairwise disjoint such graph arcs have \(A\geq\kappa\log T\) and ordinate lengths \(\ell_j\), the number of their interior actual odd-level intersections is at least
\[
 \sum_{j=1}^J\frac{\kappa\ell_j\log T}{2\pi}-J.
 \tag{27}
\]
Indeed the phase strictly decreases on each graph, an open real phase interval of length \(L\) contains at least \(L/(2\pi)-1\) odd multiples of \(\pi\), and each crossing is a simple zero by \(P'=PD\ne0\). Distinct arcs give distinct points. Endpoint crossings are deliberately omitted. The phase origins and chart integer offsets do not affect this lower bound; gluing arcs without paying \(J\) would not be justified. An upper bound or global equality of crossing counts does not follow.

No estimate proved here shows that (25) holds on most moving modulus graphs, or even that suitable graphs exist in a chosen window. The set \(E\) is a zero-neighborhood exception for value domination, not an asserted cover of \(\{A<\kappa\log T\}\), of \(D=0\), or of other critical events. In fact (19) implies \(\lambda+\log|P|>0\) on \(C\setminus E\), so there are no modulus-balanced arcs there for our proved joint regime. The actual unconditional consequence is the cluster/count/phase transfer of sections 1–5, which accounts for the zeros in the omitted pieces.

Lester's Theorems 1–3 require \((2\sigma-1)\log T\to\infty\) and \(o(\log T)\); fixed positive \(\delta\) does not meet the latter condition. His Lemma 2 and its Jutila input are useful leads but not premises of this proof. No fixed-line result has been transported to moving curves. Shrinking \(\delta(T)\), endpoint front-scale sharpening, all-height exclusion, radial minima, trajectory continuation, RH, and improved zeta density are not established.

STOP_FOR_SOL_REVIEW after the first complete freeze.
