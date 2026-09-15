# Resolution of final referee findings

Final verdict: `PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY`.

E1 - positive-height counting convention:
**Fixed.** The preprint and README now explicitly state `0 < Im(rho) <= T` and `0 < gamma <= T`.

E2 - public proof/source pointers and bibliography:
**Resolved in v0.1.1.** The first public release retained stale publication-package paths. The v0.1.1
patch replaces them with current repository paths, exact Release-asset basenames, a PGF-C replay
quick-start, and an explicit external-input locator for the Gebendorfer package.

E3 - Lean raw build evidence:
**Resolved by scope wording.** Raw build stdout was not reconstructed. Public text now calls
the Lean build PASS a **reported local build status** and keeps the formalization explicitly partial.

E4 - path relocation and Windows continuation:
**Fixed.** The release documents PGF-A `--input-dir`, includes the exact Windows continuation
overlays, and explicitly records that the official single-process raw-byte runner returned code 1.

E5 - author placeholder:
**Resolved before the public release.** Current README, CITATION, theorem sheet, and preprint fields
identify Dmitry Rakitin, Independent Researcher. The earlier RC3 note is retained only as historical
context and is no longer a current pending item.

## Post-release regression audit (15 September 2026)

A fresh post-release regression audit returned `POST_RELEASE_PATCH_REQUIRED` with **0 mathematical
blockers and 0 scope/trust-boundary blockers**. Its eight actionable public-layer findings (formula
self-containment, reproducibility paths, provenance hashes/asset membership, and editorial rendering)
are addressed by the v0.1.1 patch. The frozen theorem endpoint, m=492 parameters, proof architecture,
and certificates are unchanged.
