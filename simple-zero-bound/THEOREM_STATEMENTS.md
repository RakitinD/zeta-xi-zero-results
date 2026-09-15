# Frozen theorem statements: simple critical-line zeros

**Dmitry Rakitin**
Independent Researcher
phizmat17@gmail.com
15 September 2026

## Status

This document extracts the theorem-level statements from the frozen post-Gebendorfer fusion proof.
It is an entry point to the full proof and evidence; it is not a replacement for them.

**Correction note (15 September 2026, v0.1.1).** The theorem endpoint and frozen proof are
unchanged. This revision restores definitions omitted from the shortened public theorem sheet and
updates reproducibility/provenance pointers after a post-release regression audit.

Current verification status:

- frozen exact author verifier: `PASS_EXACT`;
- isolated hostile audit: mathematical kill targets K1-K15 PASS;
- final publication referee: `PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY`;
- complete imported Gebendorfer finite layer independently cross-host replayed:
  `58,577,037` visited nodes;
- Lean formalization is partial: Stage 5 frozen, Stage-6 bootstrap and substantive K1-K5
  scalar/core tranches have reported local build/axiom PASS status.

No statement below is a claim of the Riemann Hypothesis, full Lean formalization,
human journal peer review, global optimality, or literature-wide priority.

## Notation

Let $N(T)$ count all nontrivial zeros $\rho$ of the Riemann zeta function satisfying
$0<\operatorname{Im}\rho\le T$, counted with analytic multiplicity. Let $N_0^s(T)$
count the distinct zeros $\rho=\tfrac12+i\gamma$ with $0<\gamma\le T$ and analytic
multiplicity exactly one. Define

$$
\kappa_0^s=\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}.
$$

The frozen certified lower floor for the window constant $2-C(f_0)$ used in Theorems S2--S6 is

$$
h:=\frac{210042647916503}{312500000000000}.
$$

## Theorem S1 - simple critical-line zero proportion

Subject to the explicit analytic inputs and finite certificate chain recorded in the frozen
publication package,

$$
\boxed{\kappa_0^s\ge
\frac{6734775921119}{10^{13}}
=0.6734775921119}.
$$

The proof uses a single common signed-operator / simple-Gram state, a 69-row reflected-trim
local polyhedron, a tail-aware band profile, exact all-offset transport, one nonlinear residual
payment, and an exact universal supporting plane at block size $m=492$.

### Strict-comparison corollary

For the supplied certified Gebendorfer comparator

$$
r_G=
\frac{8269551442741204889710953}{12278882618209750000000000}
=0.673477522333941655\ldots,
$$

the gain is exactly

$$
\frac{6734775921119}{10^{13}}-r_G
=
\frac{34271814394247548721}{491155304728390000000000000}>0.
$$

Thus Theorem S1 is a strict refinement of that specified certified comparator.

## Theorem S2 - one common residual state

On the normalized limiting state used by the frozen proof, let

$$
x=s/N,\quad u=k/N,\quad v=\ell/N,\quad
w=\beta/N,\quad c=q_0/N=1-x-2w,
$$
$$
d=D/N,\qquad y=Y/N.
$$

The frozen signed-operator identities give a single residual budget

$$
S_2-2N+s=D+Y,
\qquad
hN+D+Y\le s+o(N),
$$

with

$$
Y=2q_0+W+J+Z\ge0.
$$

The normalized feasible region includes

$$
h\le x\le1,\qquad
2u+v\le x,\qquad d+y\le x-h,
$$

and

$$
d\ge
u+2v+\frac{(u+v)^2}{x-u},
$$

together with the frozen quotient / trace-refined residual constraints.
All later gains are restrictions or decompositions of this same budget; they are not added
as independent credits.

## Theorem S3 - exact global residual payment

For the same normalized state and every $\rho\ge0$ in the frozen route,

$$
y-\rho v\ge -p_h(x;\rho),
$$

where

$$
p_h(x;\rho)=
\frac{\sqrt{A_x^2+\rho^2N_x}-A_x}{2},
$$

$$
A_x=(2x-h)+\rho x,\qquad
N_x=\frac{(2-h)x-h}{2}.
$$

Equivalently,

$$
p_h^2+A_xp_h=\frac{\rho^2N_x}{4}.
$$

## Theorem S4 - universal local supporting plane

Let

$$
m=492,\qquad
\rho=\frac{19569717577}{10^{14}},
$$

and let the frozen reward and nonnegative position prices be

$$
R=\frac{38219880252651}{10^{13}},
$$

$$
(t_0,\ldots,t_5)=
\left(
\frac{2444609786511}{25000000000000},
\frac{28224041240321}{10^{14}},
\frac{24984358312191}{50000000000000},
\frac{72302683681231}{10^{14}},
\frac{90853194486369}{10^{14}},
\frac{1249217915609}{1250000000000}
\right).
$$

For the $m$-point Gram block, put

$$
n=m-6=486,\qquad
B:=\frac{1970462189}{500000000000},\qquad
\tau:=\frac76,
$$

and define

$$
E:=2\sum_{i<j,\,j-i\le6}|G_{ij}|^2,\qquad
e:=\frac{E}{n},\qquad
u_k^{\rm loc}:=\frac{B S_k}{n}\quad(0\le k\le5),
$$

where $S_k$ are the frozen gap-position sums used by the reflected-trim constraints. Define

$$
G_{m,\rho}(E)=
\begin{cases}
E,&E\le\tau(1+\rho/2)^2,\\[1mm]
\displaystyle\frac{E+m\left(2(1+\rho/2)\sqrt{E/\tau}-(1+\rho/2)^2\right)}
{1+m/\tau},&E>\tau(1+\rho/2)^2.
\end{cases}
$$

The frozen tail-aware band profile $G_{m,\rho}$ satisfies

$$
\boxed{
G_{m,\rho}(ne)+n\sum_{k=0}^5 t_k u_k^{\rm loc}\ge R
}
$$

throughout the entire 69-row nonnegative reflected-trim polyhedron.

The certificate is not based on completeness of a floating vertex list. It is certified by
464 exact rational chord/ray pieces. Each piece carries nonnegative rational Farkas weights
whose coordinatewise domination proves the affine lower bound on the whole polyhedron.

## Theorem S5 - all-offset transport

For the same common state and any local plane certified as in Theorem S4, the frozen
all-offset and fixed-smoothing transport gives

$$
\boxed{
d+\rho v\ge \frac{Rx-P_{\rm price}}{m}
},
$$

where the exact physical shift cost for the winning plane is

$$
P_{\rm price}=
\frac{47854801908769656526884823}
{25000000000000000000000000}.
$$

## Theorem S6 - exact fusion separator

Let

$$
s_0=\frac{6734775921119}{10^{13}}.
$$

For $h\le x\le s_0$, the frozen function $p_h(x;\rho)$ is increasing in $x$.
The exact replay supplies a rational $\bar p\ge0$ satisfying

$$
\bar p^2+A_{s_0}\bar p\ge\frac{\rho^2N_{s_0}}4.
$$

Since $p\mapsto p^2+A_{s_0}p$ is increasing on $p\ge0$, this gives
$ p_h(s_0;\rho)\le\bar p$, and hence $p_h(x;\rho)\le\bar p$ throughout
$h\le x\le s_0$. The exact replay then verifies

$$
mh-P_{\rm price}-m\bar p-(m-R)s_0
=
\frac{
197709610897766003525347778736270024097588737952243174610346641
}{
134990102025867487759198256090264582174639743300000000000000000000000000
}>0.
$$

Combining Theorems S3-S5 with the identity

$$
d+y=(d+\rho v)+(y-\rho v)
$$

therefore excludes every joint limiting state with $h\le x\le s_0$.
The imported basic inequality excludes $x<h$. Hence Theorem S1 follows.

## Dependency map

$$
\text{Gebendorfer certified local base}
\longrightarrow
\text{common residual state}
\longrightarrow
\text{69-row local plane}
$$

$$
\longrightarrow
\text{all-offset transport}
+
\text{one global residual payment}
\longrightarrow
\text{exact separator}
\longrightarrow
\text{Theorem S1}.
$$

## Frozen provenance

- historical frozen post-Gebendorfer fusion V1.3 archive SHA-256 (not redistributed in v0.1.1):
  `a028aa7398cbc0f8bfeb0258c03fdf38244dd24928badcac303905954bd98e5d`
- historical frozen hostile-audit archive SHA-256 (not redistributed in original form in v0.1.1):
  `d62d4629d003034136670924b2b68cc1c23e0a5fafd95e7ab1447d0fad35596f`
- external Gebendorfer reproduction archive SHA-256 (download separately; not redistributed in v0.1.1):
  `7398223b5f7d33166e25f53742541f6e2518ed95a53541b5b74ec276e4e52a47`
- independent cross-host replay evidence ZIP SHA-256:
  `2ff2fc08558d07e400356737305a56e272eba5b73296434d61eccfca6889859c`
