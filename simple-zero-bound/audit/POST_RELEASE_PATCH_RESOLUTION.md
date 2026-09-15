# v0.1.1 post-release patch resolution

This patch changes public presentation, reproducibility instructions, provenance ledgers, and public-safe Release assets. It does **not** change the frozen theorem endpoint, m=492 parameters, proof architecture, or certificates.

- **D01:** define `h = 210042647916503/312500000000000` in Markdown/TeX theorem sheets as the frozen certified lower floor used in S2-S6.
- **D02:** restore `rho>=0`, all six fixed prices, the local `B`, `tau`, `E`, `e`, `u_k^{loc}` and `G_{m,rho}` definitions, the monotonicity of `p_h(x;rho)` on `h<=x<=s0`, and the `pbar` upper-enclosure condition in the TeX/PDF theorem sheet.
- **D03:** add `PGF_C_EXACT_REPLAY_PAYLOAD_V0_1_1.zip` and a direct quick-start; clarify that the browseable verifier source alone lacks its payload.
- **D04:** replace stale publication-package paths with current repository paths and exact v0.1.1 Release-asset basenames.
- **D05:** regenerate the Git-tree SHA-256 ledger from actual Git-normalized bytes and record historical archive-original byte hashes separately.
- **D06:** v0.1.1 public-safe derivative assets no longer redistribute the original Gebendorfer ZIP or exact extracted member bytes; the historical v0.1 nested inclusion is documented explicitly.
- **D07:** wrap the theorem-sheet dependency display and remove the duplicate preprint References heading; rerender both PDFs.
- **D08:** mark the historical author-placeholder item resolved.
