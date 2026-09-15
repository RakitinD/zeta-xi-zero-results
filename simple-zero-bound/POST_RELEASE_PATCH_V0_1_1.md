# Simple-zero public patch v0.1.1

Date: 15 September 2026

A fresh post-release regression audit found no mathematical or scope/trust-boundary blocker, but
identified eight public-layer defects. This patch resolves those defects without changing the theorem
endpoint, m=492 parameters, proof architecture, or certificates.

The corrected theorem sheet is `THEOREM_STATEMENTS.pdf`. The exact finite fusion replay quick-start
is in `reproducibility/PGF_C_REPLAY_QUICKSTART.md`. Third-party comparator input handling is documented
in `reproducibility/EXTERNAL_GEBENDORFER_INPUT.md`.
