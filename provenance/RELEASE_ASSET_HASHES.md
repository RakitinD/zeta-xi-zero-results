# GitHub Release asset hashes

Recommended corrected release tag: `v0.1.1`

The historical `v0.1-frozen` assets remain historical artifacts. The v0.1.1 simple-zero upload set
uses public-safe derivatives that do not include the original third-party `Zeta_Reblocking_Repro.zip`
or byte-identical extracted member files from that archive. Workflows requiring those external files
hydrate them locally after SHA-256 verification; see `simple-zero-bound/reproducibility/EXTERNAL_GEBENDORFER_INPUT.md`.

## Simple-zero v0.1.1 assets

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `simple-zero/FINAL_PUBLICATION_REFEREE_RC2_OUTPUT.zip` | 46159 | `ab1332dd55e98d6eda570796380fc7025d8d0d6d69296e7969da54cd7360b9bc` |
| `simple-zero/GEBENDORFER_CROSS_HOST_REPLAY_EVIDENCE_V2.zip` | 13702 | `2ff2fc08558d07e400356737305a56e272eba5b73296434d61eccfca6889859c` |
| `simple-zero/PGF_C_EXACT_REPLAY_PAYLOAD_V0_1_1.zip` | 5099677 | `6ebbf24a8e3d15153b0836c8c93c0c88e475473f55ed927a6fb0b068067a4894` |
| `simple-zero/RH_GEBENDORFER_COVER_CONTINUATION_HOTFIX_V1.zip` | 7286 | `6f2ea40b7295810ea3cc3ff2f67bba5e2fe22891e273e913e15fc7c375b0b4d1` |
| `simple-zero/RH_GEBENDORFER_CROSS_HOST_FREEZE_HOTFIX_V2.zip` | 5738 | `bcbdcb1a02b86341d29635e67e03a39f2c9ba0d7221200d5b5263f510a162a03` |
| `simple-zero/RH_LEAN_FROZEN_SOURCES_STAGE5_STAGE6_RC1.zip` | 131306 | `30567f820a6654c30fe046cdd1b52a3d260c330f260b1e3632413cfaf8fdb04a` |
| `simple-zero/RH_POST_GEBENDORFER_FUSION_HOSTILE_AUDIT_V1_RUN1_PUBLIC_SAFE_V0_1_1.zip` | 5573046 | `3110c45606f6d6bd701ee8275d25a14cca8021420f36475dafc3f38ef6d1d94a` |
| `simple-zero/RH_POST_GEBENDORFER_FUSION_V1_3_PUBLIC_SAFE_OUTPUTS_V0_1_1.zip` | 5452087 | `9a7209727e2ff29208b1cf922de38513a9b9ebd58b2aef4c707d8bb0c7dae4e2` |

## Unchanged cosine-Xi assets retained from v0.1

These assets are unaffected by the simple-zero v0.1.1 patch and may be reused byte-for-byte in a
combined release. They remain listed here so the combined-project release provenance is not weakened.

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `cosine-xi/RH_COSXI_PHASE_GEOMETRY_AND_REVERSE_TRANSFER_V1_BUNDLE.zip` | 186581 | `8f0c49056aaa1812fa5a2be9bcbbe5f54731ddab07380697cb8e827258596e5a` |
| `cosine-xi/RH_COSXI_STRIP_TRANSFER_INDEPENDENT_AUDIT_V1_RUN1.zip` | 1940321 | `d2cb433273a424570b31de8b98ca70c86d5f3033281a22d0a57c52dc7e13946e` |
| `cosine-xi/RH_COS_XI_COMPLETENESS_INDEPENDENT_AUDIT_V1_RUN1.zip` | 3818661 | `2aee86d1b79ea830fd86cb8d0ddda53e9fbef17b7d941e3f97da878123623fba` |
| `cosine-xi/RH_COS_XI_ENDPOINT_INDEPENDENT_AUDIT_V1_RUN1.zip` | 1604555 | `50241a4c51cd00b205dc0e6d3d41e2d242e994d0887640f06c9452825a465d05` |
| `cosine-xi/RH_COS_XI_QUANTITATIVE_INDEPENDENT_AUDIT_V1_RUN1.zip` | 9580667 | `ca6acff67e411a471545250d17db879166c99f7c091a79fd9fcb5e678e994357` |
| `cosine-xi/RH_COS_XI_QUANTITATIVE_LOCALIZATION_V1_BUNDLE.zip` | 1123940 | `53ef2f7a82442fa569bb27b587b568d143aaf61615b6d2e1f3ae87b8beb7d7c2` |
