# Completeness of the localized nonreal tail and its leading count

Researcher: COSXI-C01. First incremental development for RH_COS_XI_TAIL_COMPLETENESS_V1.

**Status: AUTHOR_PROVED for U1, U2, U3, F1, C1 and C2, on the inherited lemmas stated below.** This is an author proof awaiting SOL review, not an independent audit. Fix an arbitrary real \(0<t<1\). All zero multisets and counts include analytic multiplicity.

## 1. Objects and exact inherited dependencies

Use
\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
 \Xi(z)=\xi(\tfrac12+iz),\quad H_t(z)=(1-t)\cos z+t\Xi(z).
\]
Removable singularities are filled in. Retain the original definitions
\[
 a=2\pi e^3,\quad c_t=\log\!\left(2e^{1/2}\sqrt\pi\frac{t}{1-t}\right),
 \quad D_t=3\log a+2c_t-3,\quad q_n=(2n+1)\pi,
\]
\[
 B_n=W_0(-2iq_n/a),\quad u_n=-2iq_n/B_n,\quad
 h_{n,t}=-3-\frac{D_t}{B_n+1},\quad
 \widehat z_n(t)=i(u_n+h_{n,t}-\tfrac12).
 \tag{1.1}
\]
The zeros \(z_n(t)\) always mean the original zeros in the disks of radius \(40/q_n\) about these centers, with their original phase indices.

Source paths here are relative to the supplied read-only worker_inputs root. Write Q01 for source/quantitative/QUANTITATIVE_PROOF.md. Its SHA256 is
3891bc166dd7746c8952299529f0e5f3f490435ea9dd76aea114da2dc3a20667.
The prior quantitative audit is source/quantitative_audit/AUDIT_REPORT.md. It accepted the inherited analytic results on their stated domains and explicitly did not establish completeness or a total count.

**I1 — Canonical reduction.** On \(\Re w>1\), use the affine map
\[
 w=\tfrac12-iz=y+\tfrac12-ix,\qquad z=i(w-\tfrac12).
 \tag{1.2}
\]
The canonical analytic logarithm is
\[
\begin{split}
L_t(w)={}&\log\frac{t}{1-t}+\Log w+\Log(w-1)-\frac w2\log\pi
+\log\Gamma(w/2)-w+\tfrac12\\
&+L_\zeta(w)-\log(1+e^{1-2w}),\qquad
L_\zeta(w)=\sum_p\sum_{k\ge1}\frac{p^{-kw}}k .
\end{split}
\]
The first logarithms are real on \(w>1\); log-Gamma is the analytic logarithm normalized on the positive ray; the final logarithm is its convergent power series. Thus \(L_t(\sigma)\) is real for real \(\sigma>1\), and
\[
 H_t(i(w-\tfrac12))=(1-t)\cosh(w-\tfrac12)(1+e^{L_t(w)}),
 \tag{1.3}
\]
with nonzero prefactor. Consequently all zero conditions in this domain are
\[
 L_t(w)=(2m+1)\pi i,\qquad m\in\mathbb Z.
 \tag{1.4}
\]
At each such level the multiplicity equals that of \(L_t(w)-(2m+1)\pi i\). The affine map preserves distances and multiplicities. There is the exact decomposition
\[
 L_t(w)=\frac w2\Log(w/a)+\frac32\Log w+c_t+E(w).
 \tag{1.5}
\]
Locators: Q01 §2, (11)–(18); quantitative audit §1. English labels: eq:coordinate-map, eq:exact-log, eq:factorization-log, eq:all-levels, eq:chosen-level, eq:decomposition.

**I2 — Derivative remainder on the whole half-plane.** For \(\sigma=\Re w\ge2\),
\[
 |E'(w)|\le\frac{10}{|w|^2}+5\,2^{-\sigma}+3e^{1-2\sigma}.
 \tag{1.6}
\]
This bound is uniform in the imaginary part and independent of \(t\). Locators: Q01 §3, Q3, (20); quantitative audit §2; English lem:remainder and eq:Eprime-bound. We use the proved derivative bound, not formal differentiation of an asymptotic error.

**I3 — Original existence, phase and geometry.** For all sufficiently large integers \(n\ge0\), the original localization disks lie in the first open quadrant, are pairwise disjoint, and each contains exactly one simple zero \(z_n(t)\). With \(w_n=\tfrac12-iz_n(t)\), its exact phase is
\[
 L_t(w_n)=-iq_n,\qquad m=-n-1.
 \tag{1.7}
\]
Furthermore,
\[
 \Re u_n\sim\frac{\pi q_n}{(\log q_n)^2}\longrightarrow\infty,
 \qquad h_{n,t}\longrightarrow-3,
 \tag{1.8}
\]
and, for \(z_n=x_n+iy_n\),
\[
 x_n\sim\frac{4\pi n}{\log n},\qquad
 y_n\sim\frac{2\pi^2n}{(\log n)^2}.
 \tag{1.9}
\]
Locators: Q01 Q1–Q2, (5)–(9); §4, (28)–(29); §5, Q4 and (34)–(36); §6, (38)–(40). Its §5 establishes the actual phase (1.7), as well as the zero of \(H_t\). Quantitative audit §§4–5 checks these facts. English labels: thm:localization, prop:finite, thm:geometry, eq:model-growth, eq:correction.

**I4 — Strip finiteness, symmetry and axis exclusion.** \(H_t\) is entire, even, satisfies \(H_t(\bar z)=\overline{H_t(z)}\), and has \(H_t(iy)>0\) for every real \(y\). For every fixed finite \(M>0\), the nonreal zeros in the closed unbounded strip \(|\Im z|\le M\) have finite total multiplicity.

Locators: source/qualitative/PROOF_V1_RU.md, §3 Lemma 1 and §5.1, with LC1 in source/qualitative/HC01_AUDIT_REPORT.md, §2.2 and §§3–4. LC1 applies strip decay on the localization circles at height \(\max(M,d)\). The clarification appears in source/qualitative/PROOF_V1_1_RU.md, §3; §5.1 gives axis positivity and symmetry. Version 1.1 is a clarified working version, not a separately re-audited proof. English Appendix A, thm:qualitative, is an integration counterpart, not a new translation audit.

The noncompact content of I4 matters: strip decay and Rouché give one simple real zero in each sufficiently distant cosine disk; a positive periodic lower bound for the cosine excludes every other distant strip zero. Only the central remainder is handled by compactness. Since \(H_t(0)>0\), it contains finitely many zeros, all of finite multiplicity.

## 2. Lemma U1 — Positive real derivative in a fixed half-plane

**U1 (AUTHOR_PROVED).** Take the nonoptimized constant
\[
 \Sigma=a=2\pi e^3.
\]
For every \(\Re w\ge\Sigma\),
\[
 \Re L_t'(w)>\frac5{16}>0 .
 \tag{2.1}
\]
This analytic statement is independent of \(t\); it does not itself count zeros.

**Proof.** Differentiating (1.5) gives
\[
 L_t'(w)=\tfrac12\Log(w/a)+\tfrac12+\frac{3}{2w}+E'(w).
\]
For \(\sigma=\Re w\ge\Sigma\ge2\), we have
\(\Re\Log(w/a)=\log(|w|/a)\ge\log(\Sigma/a)\),
\(\Re(1/w)=\sigma/|w|^2>0\), and \(\Re E'(w)\ge-|E'(w)|\). By (1.6),
\[
 \Re L_t'(w)\ge
 \frac12\log\frac\Sigma a+\frac12
 -\frac{10}{\Sigma^2}-5\,2^{-\Sigma}-3e^{1-2\Sigma}.
 \tag{2.2}
\]
At \(\Sigma=a\) the logarithm vanishes. The inequalities \(\pi>2,e>2\) give \(a>32>16\). Each of the three subtracted terms is less than \(1/16\):
\[
 \frac{10}{\Sigma^2}<\frac{10}{16^2}<\frac1{16},\quad
 5\,2^{-\Sigma}<5\,2^{-16}<\frac1{16},\quad
 3e^{1-2\Sigma}<3e^{-31}<3\,2^{-31}<\frac1{16}.
\]
Thus the lower bound exceeds \(1/2-3/16=5/16\). The real constant \(c_t\) disappears under differentiation. No numerical threshold search is required. ∎

## 3. Lemma U2 — Global injectivity

**U2 (AUTHOR_PROVED).** \(L_t\) is injective on the whole half-plane
\(\mathcal D=\{w:\Re w>\Sigma\}\).

**Proof.** For distinct \(w_1,w_2\in\mathcal D\), the full segment between them remains in this convex domain, and
\[
 \frac{L_t(w_2)-L_t(w_1)}{w_2-w_1}
 =\int_0^1 L_t'(w_1+s(w_2-w_1))\,ds .
 \tag{3.1}
\]
The right side has real part greater than \(5/16\). It cannot vanish, proving injectivity, rather than merely nonvanishing of the derivative. ∎

This is the strict-positive case of the classical Noshiro–Warschawski criterion; a checked statement is [Hotta–Wang, §1.2, Theorem 1.A](https://arxiv.org/html/1401.5647). Formula (3.1) proves the needed case directly. This known criterion is not claimed as a new method.

At a zero in (1.3), the derivative of \(1+e^{L_t(w)}\) is
\[
 e^{L_t(w)}L_t'(w)=-L_t'(w)\ne0.
\]
The nonzero prefactor and affine coordinate map show that every represented \(H_t\)-zero in \(\mathcal D\) is simple.

## 4. Lemma U3 — Phase sign and the original indices

**U3 (AUTHOR_PROVED).** For real \(\sigma>\Sigma\) and real \(v\),
\[
 \Im L_t(\sigma+iv)=\int_0^v\Re L_t'(\sigma+iu)\,du .
 \tag{4.1}
\]
This has the sign of \(v\), and vanishes exactly when \(v=0\).

**Proof.** Its initial value is zero because \(L_t(\sigma)\) is real. The chain rule gives
\[
 \frac{d}{dv}\Im L_t(\sigma+iv)
 =\Im(iL_t'(\sigma+iv))=\Re L_t'(\sigma+iv)>0.
\]
Integration gives (4.1). For \(v<0\), the reversed orientation makes the integral of this positive function negative. ∎

Put \(M=\Sigma-\tfrac12>0\). If \(z=x+iy\) has \(y>M\), then \(w\in\mathcal D\) and \(\Im w=-x\). Combining U3 with all odd levels (1.4) yields:

| Upper \(z\)-half-plane location | \(\Im w\) | Zero phase | Original \(m\) |
|---|---|---|---|
| \(x>0,\ y>M\) | negative | \(-iq_n,\ n\ge0\) | \(-n-1\) |
| \(x<0,\ y>M\) | positive | \(+iq_n,\ n\ge0\) | \(n\) |
| \(x=0,\ y>M\) | zero | no odd level | none |

Every negative odd integer is uniquely \(-2n-1\), \(n\ge0\), so the first-quadrant index offset is exactly the old one. The upper-left partner of \(z\) is \(-\bar z\), whose \(w\)-coordinate is \(\bar w\). The normalization gives \(L_t(\bar w)=\overline{L_t(w)}\), by analytic continuation of equality on the real ray; the partner therefore has the positive phase shown. The two lower-quadrant points come from conjugation in the \(z\)-plane. These symmetries preserve multiplicity.

No logarithmic assertion is extended outside \(\Re w>1\). The real \(z\)-axis maps to \(\Re w=1/2\), outside this argument, and real zeros are excluded from the target multiset. The entire imaginary \(z\)-axis is separately excluded by I4.

## 5. Lemma F1 and Theorem C1 — The finite complement

Choose an integer \(N_C(t)\ge3\) so that I3 holds for all \(n\ge N_C(t)\), including disjointness, and
\[
 \Re(u_n+h_{n,t})-\frac{40}{q_n}>\Sigma
 \quad(n\ge N_C(t)).
 \tag{5.1}
\]
This is possible by (1.8) and \(40/q_n\to0\). Thus each closed original localization disk in the \(w\)-plane lies inside \(\mathcal D\); its zero has \(y_n>M\). Only the starting integer is increased. No center, radius or phase label is changed.

**F1 (AUTHOR_PROVED).** All nonreal zeros outside these fourfold tail orbits form a finite multiset, including boundary-height zeros and the finitely many lower phase indices.

**Proof.** Let \(\mathcal S_t\) be the multiset of all nonreal zeros with \(|\Im z|\le M\), including equality. Its total multiplicity is finite by I4.

For \(0\le n<N_C(t)\), define
\[
 A_n=\{z=x+iy:x>0,\ y>M,\ L_t(\tfrac12-iz)=-iq_n\}.
\]
These are \(H_t\)-zeros by (1.3). Each \(A_n\) is empty or a singleton by U2, and a nonempty one consists of a simple zero by §3. Thus
\(A_t=\bigcup_{0\le n<N_C(t)}A_n\) has at most \(N_C(t)\) elements.

For any zero with \(x>0,y>M\), U3 supplies a unique phase \(-iq_n\) with \(n\ge0\). At a low index it belongs to \(A_t\). At \(n\ge N_C(t)\), I3 and (5.1) already supply \(w_n\in\mathcal D\) at that same phase. Injectivity gives \(w=w_n\), hence \(z=z_n(t)\). Existence for large levels comes from I3, not from a claim that an injective map is surjective onto all odd levels. A low level need not have a preimage.

Each nonreal zero with \(|\Im z|>M\) has nonzero real part by I4. Its symmetry orbit has exactly one first-quadrant representative with height greater than \(M\). Evenness and conjugation preserve multiplicity (apply the even identity and the conjugated Taylor expansion). Therefore
\[
 E_t=\mathcal S_t\;\uplus\!
 \biguplus_{z\in A_t}\{z,\bar z,-z,-\bar z\}
 \tag{5.2}
\]
is a finite multiset, of total multiplicity at most
\(\operatorname{mult}(\mathcal S_t)+4N_C(t)\).
The pieces do not overlap: their heights separate the strip from the other orbits, and different first-quadrant representatives give different orbits. The boundary lines \(\Im z=\pm M\) belong to \(\mathcal S_t\); imaginary-axis zeros do not exist; real zeros are never included. This exhausts the complement. ∎

**C1 (AUTHOR_PROVED).** For every fixed \(0<t<1\), exactly as multisets,
\[
 \mathcal Z_t^{\mathrm{nr}}
 =E_t\;\uplus\!\biguplus_{n\ge N_C(t)}
 \{z_n(t),\overline{z_n(t)},-z_n(t),-\overline{z_n(t)}\}.
 \tag{5.3}
\]
All tail points are simple and all tail orbits are disjoint; the central exceptions retain their actual, possibly larger, multiplicities.

**Proof.** F1 accounts for every zero, and I3 plus symmetry gives every listed point. Each tail orbit has four distinct points since its representative is in the first open quadrant. Intersecting orbits would have the same first-quadrant representative, impossible for two disjoint original disks. This proves the disjoint multiset equality. ∎

The finite support of \(E_t\) is bounded, so all sufficiently large-modulus nonreal zeros are tail members. Boundedness follows from proved finiteness; it is not an assumption hiding a noncompact exceptional region.

## 6. Corollary C2 — Radial inversion and the total count

**C2 (AUTHOR_PROVED, using C1).** Count with analytic multiplicity and a closed radial cutoff:
\[
 N_t^{\mathrm{nr}}(R)=
 \sum_{\substack{H_t(z)=0,\ |z|\le R\\\Im z\ne0}}
 \operatorname{mult}_{H_t}(z)
 \sim\frac{R\log R}{\pi}\qquad(R\to\infty).
 \tag{6.1}
\]

**Localized-sequence count.** Put \(\rho_n=|z_n(t)|\) and \(C=4\pi\). From (1.9), \(y_n/x_n\to0\), so
\[
 \rho_n=x_n\sqrt{1+(y_n/x_n)^2}\sim Cn/\log n.
 \tag{6.2}
\]
The real model \(f(s)=Cs/\log s\) increases strictly for \(s\ge3\), since
\(f'(s)=C(\log s-1)/(\log s)^2>0\).
Let
\(B(S)=\#\{n\in\mathbb Z:n\ge3,\ f(n)\le S\}\).
We claim
\[
 B(S)\sim S\log S/C.
 \tag{6.3}
\]
Set \(v(S)=S\log S/C\). For each fixed \(\lambda>0\),
\[
 \frac{f(\lambda v(S))}{S}
 =\frac{\lambda\log S}
 {\log S+\log\log S+\log(\lambda/C)}
 \longrightarrow\lambda.
\]
For \(0<\eta<1\), this puts \(S\) strictly between
\(f((1-\eta)v(S))\) and \(f((1+\eta)v(S))\), once \(S\) is large.
Monotonicity and integer rounding bound \(B(S)\) between
\((1-\eta)v(S)-O(1)\) and \((1+\eta)v(S)+O(1)\).
Divide by \(v(S)\) and let \(\eta\downarrow0\), proving (6.3).

For
\(A_t(R)=\#\{n\ge N_C(t):\rho_n\le R\}\),
given \(0<\varepsilon<1\), (6.2) supplies \(n_\varepsilon\ge N_C(t)\) such that
\[
 (1-\varepsilon)f(n)\le\rho_n\le(1+\varepsilon)f(n)
 \quad(n\ge n_\varepsilon).
\]
Hence, accounting only for finitely many earlier integers,
\[
 B\!\left(\frac{R}{1+\varepsilon}\right)-O_{t,\varepsilon}(1)
 \le A_t(R)\le
 B\!\left(\frac{R}{1-\varepsilon}\right)+O_{t,\varepsilon}(1).
 \tag{6.4}
\]
Divide by \(R\log R/C\). Equation (6.3) and
\(\log(R/(1\pm\varepsilon))/\log R\to1\)
bound the lower and upper limiting ratios by
\(1/(1+\varepsilon)\) and \(1/(1-\varepsilon)\).
Letting \(\varepsilon\downarrow0\) proves
\[
 A_t(R)\sim R\log R/(4\pi).
 \tag{6.5}
\]
No increasing-modulus assumption has been made. The inclusions in (6.4) use \(\le\), and therefore include roots exactly at \(|z|=R\).

**Total nonreal count.** Now use C1. Every orbit has four points of the same modulus, each simple. For every \(R\ge0\), exactly,
\[
 N_t^{\mathrm{nr}}(R)=4A_t(R)+E_t(R),\qquad
 E_t(R)=\sum_{\substack{z\in\operatorname{supp}E_t\\|z|\le R}}
 \operatorname{mult}_{E_t}(z).
 \tag{6.6}
\]
The latter is bounded by the finite total multiplicity of \(E_t\), and eventually equals it. Equations (6.5)–(6.6) prove (6.1). Without C1, (6.5) would count only the localized sequence, and four copies would furnish only a lower bound for the total. No zeta zero-counting formula is used. ∎

## 7. Scope and limitations

The supplied route's steps S1–S6 are verified with the inherited domains intact. The explicit \(\Sigma=a\), the sign/index table, the finite multiset (5.2), and the nonmonotone radial inversion supply the required details. No unresolved implication is identified in this mandatory fixed-\(t\) increment on its stated dependencies.

Although \(\Sigma\) is independent of \(t\), the localization threshold \(N_C(t)\), exceptional multiset and counting thresholds may depend on \(t\). Optional K1, uniform completeness and uniform control of exceptions on compact parameter sets, is not developed or asserted. The old uniform localization statement remains separate.

No endpoint uniformity, second counting term, threshold optimization, central-zero coordinates, trajectory classification, new function family, simplicity of \(\Xi\)-zeros or RH implication is claimed. No numerical zero evidence is needed. The bounded literature check establishes neither world novelty nor priority. Earlier PASS labels do not cover this new author proof. STOP_FOR_SOL_REVIEW after its first freeze.
