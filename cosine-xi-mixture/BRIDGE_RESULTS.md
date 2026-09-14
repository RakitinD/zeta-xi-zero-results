# COS-XI bridge results

**Dmitry Rakitin**  
Independent Researcher  
phizmat17@gmail.com  
14 September 2026

## Status and scope

These are supplementary **paper-level bridge results** from the later COS-XI campaign.
They are not assigned the same independent-audit status as Theorems C1-C5 in
`THEOREM_SUITE_V2.md`.

Source artifacts recorded in the research campaign include:

- `RH_COSXI_C1_CRITICAL_LINE_TRANSFER_V1.md`;
- `RH_COSXI_C2_ATTACK_V1.md`;
- `RH_COSXI_ENDPOINT_NEAR_AXIS_DEFECT_BUDGET_V1.md`.

They should be cited as auxiliary bridge statements, not as an RH proof and not as a completed
global asymptotic defect theorem.

## Bridge B1 - finite-window critical-line transfer

**Status:** `C1 = SOLVED_AT_PAPER_LEVEL`.

Fix a finite ordinate window \([T,2T]\) and let

\[
\Gamma_T=\{\gamma_1<\cdots<\gamma_s\}
\]

be retained simple critical-line zeros of \(\Xi\):

\[
\Xi(\gamma_j)=0,\qquad \Xi'(\gamma_j)\ne0.
\]

Given any prescribed displacement tolerance \(\eta_T>0\) and any lower parameter threshold
\(\Lambda_*(T)\), there exists

\[
\Lambda_{C1}(T)\ge\Lambda_*(T)
\]

such that for every \(\lambda\ge\Lambda_{C1}(T)\), with

\[
t=\frac{e^\lambda}{1+e^\lambda},
\]

each \(\gamma_j\) continues to a unique simple real zero \(r_j(t)\) of

\[
H_t(z)=(1-t)\cos z+t\Xi(z)
\]

satisfying

\[
|r_j(t)-\gamma_j|<\eta_T.
\]

For sufficiently small disjoint neighborhoods chosen around the retained simple zeros, the
corresponding real zeros of \(H_t\) preserve their order.

This is a finite-window persistence/transfer theorem. It does not assert simplicity of all
critical-line zeros of \(\Xi\), does not count off-line zeros, and does not imply RH.

## Bridge B2 - local multiplicity splitting under paired perturbations

**Status:** paper-level local theorem (`C2-MULT`).

Let \(f\) be real analytic (or holomorphic with the usual reality symmetry near the real axis),
let \(\gamma\in\mathbb R\) be a real zero of multiplicity \(m\ge1\), and let \(g\) be real analytic
near \(\gamma\) with

\[
g(\gamma)\ne0.
\]

For all sufficiently small nonzero real \(\varepsilon\), each of

\[
f+\varepsilon g,\qquad f-\varepsilon g
\]

has exactly \(m\) simple roots in a sufficiently small disk around \(\gamma\), counted with
multiplicity. Across the two perturbations together, exactly two of these \(2m\) local roots are
real and

\[
\boxed{2m-2}
\]

are nonreal.

For \(m=1\) this produces no nonreal local defect; for \(m>1\) the excess multiplicity is converted
into nonreal roots across the paired perturbations.

For the \(\Xi\) application, the campaign uses cosine perturbation directions and chooses a
direction nonvanishing at the retained real zero; the two directions
\(\cos z\) and \(\cos(\sqrt2\,z)\) provide a way to avoid simultaneous vanishing.

## Bridge B3 - finite-window defect identities

Work in a fixed finite region with pairwise disjoint localization disks around the relevant
zeros of \(\Xi\), small enough that the local perturbation conclusions are valid.

Let \(E_{\mathbb R}\) denote the total excess multiplicity carried by real zeros in those disks,
i.e. the sum of \(m-1\) over the retained real zeros of multiplicity \(m\).
Let \(D_{\mathbb R}\) be the total number of local nonreal roots produced across the paired
perturbations from those real zeros. Then Bridge B2 gives the exact identity

\[
\boxed{D_{\mathbb R}=2E_{\mathbb R}}.
\]

If \(N_{\rm off}\) denotes the corresponding total multiplicity of nonreal \(\Xi\)-zeros in the
same finite localization scheme, and \(D_{\rm all}\) denotes the full paired local nonreal-defect
count, the local bookkeeping identity is

\[
\boxed{D_{\rm all}=2N_{\rm off}+2E_{\mathbb R}}.
\]

These are finite/local bridge identities. The campaign did **not** prove the endpoint-scale
asymptotic statement needed to turn them into a global \(o(N)\) defect budget, and no such
global consequence is claimed here.

## Publication rule

These bridge results may be listed as supplementary paper-level results. They should remain
visibly separated from the independently audited main COS-XI theorem suite until they receive
their own independent audit or formal verification.
