# Theorem suite for cosine-Riemann Xi mixtures

**Dmitry Rakitin**  
Independent Researcher  
phizmat17@gmail.com  
14 September 2026

## Purpose and status

For

\[
H_t(z)=(1-t)\cos z+t\Xi(z),\qquad
\Xi(z)=\xi\!\left(\tfrac12+iz\right),\qquad 0<t<1,
\]

this document records the current theorem-level results of the COS-XI branch.

It supersedes the **scope summary** of the 11 September 2026 localization manuscript:
that manuscript remains the proof document for quantitative localization and qualitative
background, but it predates the later completeness, endpoint-front, and moving-boundary /
cluster-transfer results.

The status labels below are intentionally explicit. “Independent audit PASS” means a separate
model context checked the supplied proof on its stated scope; it is not human journal peer review
and not formal proof-assistant verification.

## Theorem C1 - individual localization of a nonreal zero sequence

**Status:** `THEOREM_BLOCK_INDEPENDENT_AUDIT_PASS`.

Define

\[
a=2\pi e^3,\qquad
c_t=\log\!\left(2e^{1/2}\sqrt{\pi}\,\frac{t}{1-t}\right),
\qquad
D_t=3\log a+2c_t-3,
\]

\[
q_n=(2n+1)\pi,\qquad
B(q)=W_0\!\left(-\frac{2iq}{a}\right),
\]

\[
u(q)=-\frac{2iq}{B(q)},\qquad
h_t(q)=-3-\frac{D_t}{B(q)+1},
\]

and

\[
\widehat z_n(t)=
i\!\left(u(q_n)+h_t(q_n)-\tfrac12\right).
\]

For every fixed \(t\in(0,1)\), there exists \(N(t)\) such that for every \(n\ge N(t)\),

\[
D_n(t)=
\left\{z:\ |z-\widehat z_n(t)|<\frac{40}{q_n}\right\}
\]

lies in the first open quadrant and contains exactly one zero \(z_n(t)\) of \(H_t\),
counted with multiplicity. That zero is simple, and

\[
|z_n(t)-\widehat z_n(t)|
<
\frac{40}{(2n+1)\pi}.
\]

Eventually the disks are pairwise disjoint and \(\operatorname{Re}z_n(t)\) is strictly increasing.
The threshold may be chosen uniformly for \(t\) in any fixed compact subset of \((0,1)\).

Writing \(z_n=x_n+iy_n\),

\[
x_n(t)=
\frac{4\pi n}{\log n}
\left(1+O_t\!\left(\frac{\log\log n}{\log n}\right)\right),
\]

\[
y_n(t)=
\frac{2\pi^2 n}{(\log n)^2}
\left(1+O_t\!\left(\frac{\log\log n}{\log n}\right)\right),
\]

and

\[
y_n(t)=
\frac{\pi x_n(t)}{2\log x_n(t)}
+
O_t\!\left(\frac{x_n(t)}{(\log x_n(t))^2}\right).
\]

The localization theorem alone does not assert completeness; that stronger result is Theorem C2.

## Theorem C2 - completeness of the nonreal tail

**Status:** `THEOREM_INDEPENDENT_AUDIT_PASS`.

Fix \(t\in(0,1)\). Let \(\{z_n(t)\}\) be the first-quadrant sequence from Theorem C1.
There exists a finite exceptional multiset \(E_t\) such that, with multiplicities,

\[
\{\text{nonreal zeros of }H_t\}
=
E_t
\uplus
\biguplus_{n\ge N_C(t)}
\{z_n,\overline{z_n},-z_n,-\overline{z_n}\}.
\]

Consequently, if

\[
N_t^{\rm nr}(R)=
\sum_{\substack{H_t(z)=0,\ |z|\le R\\ \operatorname{Im}z\ne0}}
\operatorname{mult}_{H_t}(z),
\]

then

\[
\boxed{
N_t^{\rm nr}(R)\sim\frac{R\log R}{\pi}
}
\qquad(R\to\infty).
\]

The theorem is fixed-\(t\); no uniform control of the exceptional multiset as \(t\to1\) is asserted.

## Theorem C3 - fixed-height endpoint front as \(t\uparrow1\)

**Status:** `THEOREM_INDEPENDENT_AUDIT_PASS`.

For fixed real \(d>1/2\), define

\[
\lambda=\log\frac{t}{1-t},
\qquad
R_d(t)=
\inf\{|z|:\ H_t(z)=0,\ |\operatorname{Im}z|\ge d\}.
\]

Then, as \(\lambda\to+\infty\),

\[
\boxed{
R_d(t)=
\frac4\pi\lambda+
\frac{2d+7}{\pi}\log\lambda+
O_d(1)
}.
\]

The lower bound applies to every root in the defining set, without a height cutoff.
The upper bound is realized by a simple first-quadrant root with positive real part and height

\[
d+O_d(1/\log\lambda).
\]

No uniformity as \(d\downarrow1/2\) is asserted.

## Theorem C4 - moving-boundary endpoint front

**Status:** S01 `PASS_AS_WRITTEN` in the independent strip-transfer audit.

Put

\[
\beta(v)=
\left\{
54.004(\log v)^{2/3}(\log\log v)^{1/3}
\right\}^{-1}.
\]

There exist absolute constants \(C\) and \(\lambda_0\) such that for every
\(\lambda\ge\lambda_0\) and every real \(s\) satisfying

\[
1-\frac{\beta(6\lambda)}{16}\le s\le\frac32,
\qquad
d=s-\frac12,
\]

the infimum \(R_d(t)\) is finite and attained and

\[
\boxed{
\left|
R_d(t)-
\left(
\frac4\pi\lambda+
\frac{2d+7}{\pi}\log\lambda
\right)
\right|
\le
C\bigl(1+\log\log(6\lambda)\bigr)
}.
\]

The same constants work simultaneously for all \(s\) in the displayed interval.

A genuine simple first-quadrant zero realizes the upper front with

\[
x=
X_{\rm front}(\lambda,s)
+O(1+\log\log\lambda),
\]

\[
d<y<
d+
O\!\left(
\frac{1+\log\log\lambda}{\log\lambda}
\right).
\]

Consequences include:

- every \(d_+=1/2+\eta_+(\lambda)\), where \(\eta_+(\lambda)>0\) and
  \(\eta_+(\lambda)\to0\), eventually satisfies the same front estimate;
- every \(0<\eta_-(\lambda)\le\beta(6\lambda)/16\) gives the same estimate for
  \(d_-=1/2-\eta_-\);
- for the maximal stated \(\eta_-=\beta(6\lambda)/16\), the constructed mixture zero
  eventually satisfies \(0<\operatorname{Im}z<1/2\).

The last statement concerns zeros of the mixture \(H_t\), not a new zero-free region for zeta.

## Theorem C5 - quantified cluster/count/phase transfer in a fixed strip window

**Status:** main theorem S02-T `PASS_AS_WRITTEN` in the independent strip-transfer audit.

Fix \(0<\delta<1/2\), let

\[
a=\frac12+\delta,\qquad
h=\frac{\delta}{4},\qquad
q=1-\frac{\delta}{16},\qquad
r=T^{-2},
\]

and define

\[
\Omega=
\{\sigma-ix:\ a\le\sigma\le2,\ T\le x\le2T\}.
\]

Let

\[
J_q(Y)=
10395.2Y^q\log Y+
1.104(\log Y)^2+
0.173\log Y\log\log Y+
0.51\log Y,
\]

\[
Q_\delta(T)=J_q(T/2)+J_q(T)+J_q(2T).
\]

Assume

\[
T\ge2H_0,\qquad
4T^{-2}Q_\delta(T)<\min(\delta/4,1),
\]

and \(\lambda\ge\Lambda(T)\), with the explicit \(\Lambda(T)\) from the frozen S02 proof.

Let \(E\) be the union of small disks around the relevant zeta zeros in the enlarged collar,
and let \(M_j\) be the total zeta-zero multiplicity in a relevant connected component \(U_j\).
Then:

1. the total relevant multiplicity satisfies \(M\le Q_\delta(T)\);

2. every zero of \(H_t(i(w-\tfrac12))\) in the closed window lies in a relevant component,
and each full relevant component contains exactly \(M_j\) mixture zeros and exactly \(M_j\)
zeros of \(\xi\), with multiplicity;

3.
\[
|N_H(\Omega)-N_\xi(\Omega)|
\le B_\Omega
\le M
\le Q_\delta(T),
\qquad
N_H(\Omega)\le Q_\delta(T)=o(T);
\]

4. on every zero-free path in the collar complement, continuously lifted phase changes of the
mixture and \(\xi\) differ by at most \(2/(3T)\); on every closed contour their windings agree exactly.

The same count assertions hold for the open window. If \(B_\Omega=0\), the two window counts
are exactly equal.

### Explicit audit exclusion

The independent audit found one redundant geometric aside in the original S02 proof to be
false as a general statement: disk-center membership in the total union does not prevent a
separate disk component from lying inside a hole of another component.

That sentence is **not part of Theorem C5** and is excluded. The audit accepted the
full-oriented-boundary homotopy and the main S02-T theorem without it.

## Result-status table

| Block | Public status | Source SHA-256 |
|---|---|---|
| C1 localization + geometry | independent audit PASS | `3891bc166dd7746c8952299529f0e5f3f490435ea9dd76aea114da2dc3a20667` |
| C2 completeness + count | independent audit PASS | `dd8272fd7b87002f434a95a48051ce60fff786bc0d88c6c538ccb45a0cdc9dcc` |
| C3 fixed-\(d\) endpoint front | independent audit PASS | `3de5141d1ed01051416e214cbd76e1eb0b5414a935b3d788aa3f2a56e315a949` |
| C4 moving boundary | `PASS_AS_WRITTEN` | `06c9f892899fcd5dad742414746a87fbc06c5058baa67df6b3dee4198abdf616` |
| C5 strip transfer | S02-T `PASS_AS_WRITTEN` | `f2180957222c7cbba9d321cf1cc3dff141655f70efd250fb2335b919f95f1a7d` |

## Publication note

The 11 September 2026 manuscript *Quantitative localization of nonreal zeros of a
cosine-Riemann Xi mixture* remains the proof manuscript for Theorem C1 and the qualitative
background. It predates Theorems C2-C5 and should not be presented as the complete final COS-XI theory.

A unified long-form manuscript integrating C1-C5 can be prepared separately without changing
these frozen theorem statements.
