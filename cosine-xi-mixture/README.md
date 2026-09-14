# Cosine–Riemann Xi mixture results

For

$$
H_t(z)=(1-t)\cos z+t\Xi(z),\qquad 0<t<1,
$$

this directory contains the current theorem suite and the separate proof/audit blocks behind it.

## Current theorem suite

Start with:
- [`THEOREM_SUITE_V2.pdf`](THEOREM_SUITE_V2.pdf)
- [`THEOREM_SUITE_V2.md`](THEOREM_SUITE_V2.md)

Main blocks:

1. **Localization** — explicit Lambert-$W_0$ centers and one simple nonreal zero per small disk.
2. **Completeness** — the localized tail exhausts all nonreal zeros up to a finite exceptional multiset,
   and $N_t^{\rm nr}(R)\sim R\log R/\pi$.
3. **Fixed endpoint front** — two-term asymptotic as $t\uparrow1$ outside fixed height $d>1/2$.
4. **Moving-boundary front** — extension down to the explicit moving zero-free scale.
5. **Strip transfer** — quantitative componentwise zero-count and phase transfer in a fixed strip window.

## Proof and audit map

- `quantitative-localization/`
  - `MANUSCRIPT_V1.pdf`
  - `QUANTITATIVE_PROOF.md`
  - `AUDIT_REPORT.md`
  - `VERDICT_REGISTRY.json`

- `completeness/`
  - `COMPLETENESS_PROOF.md`
  - `AUDIT_REPORT.md`
  - `VERDICT_REGISTRY.json`

- `endpoint/`
  - `ENDPOINT_PROOF.md`
  - `AUDIT_REPORT.md`
  - `VERDICT_REGISTRY.json`

- `strip-transfer/`
  - `S01_PROOF.md`
  - `S02_PROOF.md`
  - `AUDIT_REPORT.md`
  - `VERDICT_REGISTRY.json`
  - `S02_EXCEPTION_REPORT.md`

## Supplementary bridge results

[`BRIDGE_RESULTS.pdf`](BRIDGE_RESULTS.pdf) records paper-level finite-window bridge results:
critical-line persistence, the local `2m-2` multiplicity-splitting law, and finite-window
defect identities.

These bridge statements deliberately carry a weaker status than the independently audited
main theorem suite.

## Historical manuscript scope

The 11 September localization manuscript predates the completeness, endpoint, and strip-transfer
results. It remains a proof manuscript for localization and qualitative background, not the complete
final COS–Xi theory.
