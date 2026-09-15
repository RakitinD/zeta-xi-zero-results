# Zeta and Xi zero results

**Dmitry Rakitin**  
Independent Researcher  
[phizmat17@gmail.com](mailto:phizmat17@gmail.com)

This repository collects two AI-assisted mathematical research lines concerning zeros of the
Riemann zeta / Xi functions. The results are presented with explicit theorem statements,
proof sources, audit records, reproducibility material, and scope limitations.

## Result I — simple zeros on the critical line

A frozen computer-assisted strict refinement of the supplied certified Gebendorfer comparator:

```math
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge
\frac{6734775921119}{10^{13}}
=
0.6734775921119
```

Here `N(T)` counts all nontrivial zeta zeros with `0 < Im(rho) <= T`, with analytic multiplicity,
and `N_0^s(T)` counts distinct simple zeros on the critical line.

The exact improvement over the supplied certified comparator is positive:

$$
\frac{34271814394247548721}
{491155304728390000000000000}>0.
$$

Verification layers include:
- exact frozen author verifier `PASS_EXACT`;
- isolated hostile audit with mathematical kill targets K1–K15 PASS;
- independent cross-host replay of all 58,577,037 nodes in the imported computational base;
- final publication referee: `PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY`;
- partial Lean formalization with explicit remaining boundaries.

Start here:
- [`simple-zero-bound/THEOREM_STATEMENTS.pdf`](simple-zero-bound/THEOREM_STATEMENTS.pdf)
- [`simple-zero-bound/preprint/PREPRINT.pdf`](simple-zero-bound/preprint/PREPRINT.pdf)
- [`simple-zero-bound/README.md`](simple-zero-bound/README.md)

## Result II — zeros of cosine–Riemann Xi mixtures

For

$$
H_t(z)=(1-t)\cos z+t\Xi(z),\qquad 0<t<1,
$$

the current theorem suite contains five main blocks:

1. explicit Lambert-$W_0$ localization of an infinite simple nonreal zero sequence;
2. completeness of the nonreal tail and $N_t^{\rm nr}(R)\sim \frac{R\log R}{\pi}$;
3. a fixed-height endpoint front as $t\uparrow1$;
4. a moving-boundary endpoint front down to the stated zero-free scale;
5. quantified fixed-strip cluster/count/phase transfer.

Supplementary paper-level bridge results record finite-window critical-line persistence,
the local `2m-2` multiplicity-splitting law for paired perturbations, and finite-window
defect identities.

Start here:
- [`cosine-xi-mixture/THEOREM_SUITE_V2.pdf`](cosine-xi-mixture/THEOREM_SUITE_V2.pdf)
- [`cosine-xi-mixture/README.md`](cosine-xi-mixture/README.md)
- [`cosine-xi-mixture/BRIDGE_RESULTS.pdf`](cosine-xi-mixture/BRIDGE_RESULTS.pdf)

The 11 September localization manuscript is retained as the proof manuscript for the first
COS–Xi theorem block, but it predates the later completeness, endpoint, and strip-transfer results.

## Verification and scope

These are research artifacts, not journal peer review and not a proof of the Riemann Hypothesis.
The repository distinguishes frozen proofs, independent model-context audits, exact computational
replay evidence, partial formalization, and paper-level results.

See [`STATUS.md`](STATUS.md).

## Repository layout

- `simple-zero-bound/` — theorem sheet, preprint, full proof, audit and reproducibility pointers.
- `cosine-xi-mixture/` — current theorem suite and separate proof/audit blocks.
- `provenance/` — release and hash information.
- `CITATION.cff` — author/repository citation metadata.

Large frozen archives are distributed as GitHub Release assets rather than committed to git history.
The v0.1.1 public-safe asset set externalizes the original third-party Gebendorfer reproduction package bytes;
see `simple-zero-bound/reproducibility/EXTERNAL_GEBENDORFER_INPUT.md`.

## License note

No repository-wide license is granted in this initial release. Third-party material remains under
its own terms. A repository-wide license can be added later after original and imported materials
are separated cleanly.
