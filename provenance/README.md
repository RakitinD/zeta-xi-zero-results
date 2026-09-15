# Provenance

The git tree contains readable theorem statements, proofs, audit reports, status documents, and
reproducibility instructions.

Large archives are distributed separately as GitHub Release assets. The recommended corrected
release is **v0.1.1**. Its simple-zero public-safe assets do not redistribute the original third-party
Gebendorfer reproduction ZIP or exact extracted member bytes; external input identity is bound by SHA-256.

Exact SHA-256 pins are recorded in:
- `RELEASE_ASSET_HASHES.md` - v0.1.1 public Release assets;
- `GIT_TREE_HASHES_SHA256.txt` - actual Git-tree/worktree bytes;
- `ARCHIVE_ORIGINAL_HASHES.md` - historical frozen archive-original byte hashes when newline
  normalization makes them differ from the Git-tree copy.

The Git-tree ledger excludes itself to avoid a recursive hash definition.
