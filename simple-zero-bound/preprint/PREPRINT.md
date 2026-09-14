# A strict computer-assisted refinement of a certified lower bound for simple critical-line zeros

**Author-ready publication draft - 14 September 2026**

**Author:** Dmitry Rakitin  
Independent Researcher  
phizmat17@gmail.com

## Abstract

We give a computer-assisted strict refinement of the supplied certified Gebendorfer lower bound
for the lower asymptotic proportion of nontrivial zeros of the Riemann zeta function that are
simple and lie on the critical line. The frozen endpoint is

`kappa_0^s >= 6734775921119/10^13 = 0.6734775921119`.

The exact difference from the supplied comparator is

`34271814394247548721/491155304728390000000000000 > 0`.

The refinement combines the certified local-window base with a global residual/rank-tail constraint,
a state-dependent nonlinear residual payment, a tail-aware finite band profile, an m=492
trimming/capacity construction, and an exact universal supporting plane certified by 464
chord/ray Farkas certificates over 69 local rows. An isolated hostile audit passed mathematical
kill targets K1-K15. A final publication referee returned
`PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY` with no substantive blocker. The complete
58,577,037-node Gebendorfer finite layer was independently cross-host replayed. Partial Lean
formalization is frozen with its remaining boundary stated explicitly.

## 1. Statement and counting convention

Let `N(T)` count all nontrivial zeros `rho` of the Riemann zeta function satisfying
`0 < Im(rho) <= T`, with analytic multiplicity.

Let `N_0^s(T)` count the distinct zeros `rho = 1/2 + i gamma` with
`0 < gamma <= T` whose analytic multiplicity is exactly one.

Define

`kappa_0^s = liminf_(T->infinity) N_0^s(T)/N(T)`.

The frozen theorem claim is

`kappa_0^s >= 6734775921119/10^13 = 0.6734775921119`.

The supplied Gebendorfer comparator is

`r_G = 8269551442741204889710953/12278882618209750000000000 = 0.673477522333941655...`.

The exact strict gain is

`6734775921119/10^13 - r_G = 34271814394247548721/491155304728390000000000000 > 0`.

## 2. Imported certified local base

The imported local base is the supplied Gebendorfer six-gap architecture:
one explicit analytic window, nine universal local inequalities, three-window compatibility,
exact coarsening/joining, and a restricted eight-gap proof.

Its full finite computation contains

`50,089,182 + 7,638,774 + 849,081 = 58,577,037`

visited nodes.

All computational obligations were independently replayed on a separate Windows host.
The unmodified official `reproduce.py --full` returned code 1 at a raw-byte equality test after
the nine local proofs because native Windows text mode emitted CRLF while the frozen artifact uses LF.
The documented continuation completed the cover, coarsening, join, and restricted proof.
After LF normalization the generated row sequences are identical, the 71-box coarsening is
byte-identical, and the total node count matches the retained reference exactly.

## 3. Refinement architecture

The frozen post-Gebendorfer proof is organized into audited blocks K1-K15:

- K1 primary signed state, occurrence multiplicities, simple Gram and inertia;
- K2 single residual identity `D+Y`, with `Y=2q0+W+J+Z`;
- K3 quotient/refinement and boundary guards;
- K4 global rank/high-eigenvalue feasible region;
- K5 one nonlinear residual payment;
- K6 tail-aware profile and rho=0 regression;
- K7-K9 69 trim rows, physical capacity, m=492 costs, n=486, 162 untrimmed triples;
- K10 464 exact chord/ray Farkas certificates for the universal supporting plane;
- K11 analytic transport, offsets, endpoint losses, and fixed smoothing;
- K12 legal 13-module fusion with no double counting;
- K13 exact endgame with positive nonlinear margin;
- K14 independent exact reconstruction sealed before the author verifier was read;
- K15 disciplined public claim wording.

## 4. Proof and source pointers

This note is deliberately compact. The full proof and data are distributed with it.

Browseable key files:
- `../proof/fusion/FUSION_PROOF.md`
- `../proof/fusion/verify_fusion.py`
- `../proof/hostile/INDEPENDENT_REDERIVATION.md`
- `../proof/hostile/INDEPENDENT_FINAL_RECEIPT.json`
- `../proof/gebendorfer/Zeta_Reblocking_Improvement.pdf`
- `../proof/final_referee/REFEREE_REPORT.md`

Complete frozen archives:
- `../artifacts/RH_POST_GEBENDORFER_FUSION_V1_3_RUN1_FROZEN_OUTPUTS.zip`
- `../artifacts/RH_POST_GEBENDORFER_FUSION_HOSTILE_AUDIT_V1_RUN1_FROZEN_OUTPUTS.zip`
- `../artifacts/Zeta_Reblocking_Repro.zip`
- `../artifacts/GEBENDORFER_CROSS_HOST_REPLAY_EVIDENCE_V2.zip`
- `../artifacts/RH_LEAN_FROZEN_SOURCES_STAGE5_STAGE6_RC1.zip`

## 5. Independent audits

The isolated hostile audit gave
`PASS_WITH_REPRODUCIBILITY_DEFECTS_ONLY`.
All mathematical kill targets K1-K15 passed; K16 was a technical default-path reproducibility issue.

The final publication referee gave
`PUBLICATION_PASS_WITH_EDITORIAL_DEFECTS_ONLY`
and found no substantive mathematical, scope, or circularity blocker.

The final referee's editorial/reproducibility findings are addressed in
`../release/REFEREE_FINDINGS_RESOLUTION.md`.

## 6. Lean status

The release contains exact frozen Lean source/manifests for Stage 5, the Stage-6 bootstrap,
and a substantive K1-K5 scalar/core tranche.

The local research host reported:
- `STAGE6_BOOTSTRAP_BUILD = PASS`
- `STAGE6_AXIOM_AUDIT = PASS`
- `STAGE6_K1K5_BUILD = PASS`
- `STAGE6_K1K5_AXIOM_AUDIT = PASS`
- `STAGE6_K1K5_FREEZE = PASS`

The final referee did not rerun Lean and noted that raw build stdout was absent from RC2.
Accordingly, this release calls these **reported local build statuses**, not independently
reproduced build evidence.

This is partial formalization, not an end-to-end Lean proof. In particular the concrete K1
Vandermonde/Sylvester zeta-operator realization remains an explicit boundary, K6-K15 are not
fully internalized, and Lean does not rerun the 58,577,037-node interval computation.

## 7. Reproducibility notes

PGF-A supports relocating its frozen source archives via:

`python replay.py --input-dir <directory-containing-input-zips>`.

The exact Windows continuation used after the official Gebendorfer raw-byte failure is included in
`../reproducibility/`.

All final artifact hashes are frozen in `../PUBLICATION_MANIFEST.json` and
`../hashes/HASHES_SHA256.txt`.

## 8. References

See `../bibliography/REFERENCES.md`.

The external analytic inputs include Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh,
*An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*
(Acta Arithmetica 214 (2024), arXiv:2306.04799v1), and Lamzouri,
*A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the
critical line* (2026, arXiv:2609.02882v1).

## 9. Scope

This is a computer-assisted strict refinement of the supplied certified comparator.
It is not a proof of the Riemann Hypothesis, not full Lean formal verification,
not completed independent human peer review, not a claim of global optimality,
and not a literature-wide priority claim.
