# PGF-C exact replay quick start (v0.1.1)

The browseable file `simple-zero-bound/proof/verify_fusion.py` is a source mirror. The public replay payload intentionally omits exact files copied from the external Gebendorfer reproduction package.

Download the GitHub Release asset:

`PGF_C_EXACT_REPLAY_PAYLOAD_V0_1_1.zip`

and obtain the original external input `Zeta_Reblocking_Repro.zip` from:

`https://zenodo.org/records/22661276`

Verify the external ZIP SHA-256:

`7398223b5f7d33166e25f53742541f6e2518ed95a53541b5b74ec276e4e52a47`

After extracting the v0.1.1 replay asset, run from the extracted archive root:

```text
python -B -X utf8 hydrate_external_input.py --gebendorfer-zip /path/to/Zeta_Reblocking_Repro.zip
python -B -X utf8 PGF-C/verify_fusion.py --all
```

`hydrate_external_input.py` verifies the external archive hash and copies only the exact `imported/primary` files required by the frozen PGF-C manifest, checking each byte size and SHA-256 against that manifest. The hydrate step is deterministic and does not modify the external archive.

Expected replay scope: exact legal-module enumeration, coefficient binding to the supplied external primary files, rational supporting-plane certificates, exact separator, all supplied plane/endgame certificates, and the PGF-C manifest. The verifier uses the Python standard library only.

The replay does **not** rerun the imported 58,577,037-node interval computation and does not prove the imported analytic theorems. Those remain explicit trust inputs.

The v0.1.1 Release assets do not contain the original Gebendorfer ZIP or byte-identical extracted members of it.
