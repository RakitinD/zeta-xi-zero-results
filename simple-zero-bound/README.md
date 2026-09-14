# Simple critical-line zeros

## Main theorem

\[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge 0.6734775921119.
\]

Exact endpoint: `6734775921119 / 10^13`.

Exact gain over the supplied certified Gebendorfer comparator:

`34271814394247548721 / 491155304728390000000000000 > 0`.

## Start here

1. [`THEOREM_STATEMENTS.pdf`](THEOREM_STATEMENTS.pdf)
2. [`preprint/PREPRINT.pdf`](preprint/PREPRINT.pdf)
3. [`proof/FUSION_PROOF.md`](proof/FUSION_PROOF.md)
4. [`audit/INDEPENDENT_REDERIVATION.md`](audit/INDEPENDENT_REDERIVATION.md)
5. [`audit/FINAL_PUBLICATION_REFEREE_REPORT.md`](audit/FINAL_PUBLICATION_REFEREE_REPORT.md)
6. [`formalization/LEAN_STATUS.md`](formalization/LEAN_STATUS.md)
7. [`reproducibility/WINDOWS_CROSS_HOST_CONTINUATION.md`](reproducibility/WINDOWS_CROSS_HOST_CONTINUATION.md)

## Replay status

Independent Windows replay accounting:

- 50,089,182 local nodes;
- 7,638,774 cover nodes;
- 849,081 restricted nodes;
- 58,577,037 total.

The original single-process runner returned code 1 at a raw-byte LF/CRLF comparison.
A documented continuation completed the remaining obligations. The public status is therefore
**independent cross-host computational replay PASS**, not byte-identical full-run PASS on Windows.

## Lean boundary

Lean is partial. Frozen sources cover Stage 5, a Stage-6 bootstrap, and a substantive K1–K5
scalar/core tranche. Reported local builds and axiom audits passed, but the final publication
referee did not rerun Lean. K1 operator realization and K6–K15 full internalization remain outside
the current formalized scope.
