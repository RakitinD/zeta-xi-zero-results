# Post-release regression audit summary

Date: 15 September 2026

Final audit verdict: `POST_RELEASE_PATCH_REQUIRED`.

The independent post-release audit reported:

- 0 mathematical blockers;
- 0 scope/trust-boundary blockers;
- 2 formula-transcription/self-containment defects in the public theorem sheet;
- 2 reproducibility/path defects;
- 2 provenance/hash-or-membership defects;
- 2 editorial/rendering defects.

The frozen headline theorem remains supported:

`liminf N_0^s(T)/N(T) >= 6734775921119/10^13 = 0.6734775921119`.

The audit did not require changing the endpoint, m=492 parameters, proof architecture, or certificates.
The frozen audit output package had SHA-256
`133ee02d87382021b929ea52d1974717e9524d03de15b222c8063511cb830357`.

All eight public-layer findings are resolved in the v0.1.1 patch; see `POST_RELEASE_PATCH_RESOLUTION.md`.
