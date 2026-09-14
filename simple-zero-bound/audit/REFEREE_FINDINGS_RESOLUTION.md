# Resolution of final referee findings

Final verdict: `PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY`.

E1 - positive-height counting convention:
**Fixed.** The preprint and README now explicitly state `0 < Im(rho) <= T` and `0 < gamma <= T`.

E2 - public proof/source pointers and bibliography:
**Fixed.** RC3 includes a proof locator map, browseable key proof files, full frozen archives,
and a primary-source bibliography.

E3 - Lean raw build evidence:
**Resolved by scope wording.** Raw build stdout was not reconstructed. Public text now calls
the Lean build PASS a **reported local build status** and keeps the formalization explicitly partial.

E4 - path relocation and Windows continuation:
**Fixed.** The release documents PGF-A `--input-dir`, includes the exact Windows continuation
overlays, and explicitly records that the official single-process raw-byte runner returned code 1.

E5 - author placeholder:
**Pending user input.** RC3 deliberately says author identity pending. This is the only remaining
personal/editorial item before a public upload.
