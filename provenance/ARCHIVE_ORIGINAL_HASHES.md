# Historical archive-original byte hashes

Some frozen files in the supplied Windows publication worktree use CRLF bytes, while the corresponding
Git blobs use LF-normalized bytes. Their semantic content is unchanged, but raw SHA-256 values differ.
`GIT_TREE_HASHES_SHA256.txt` therefore hashes the actual Git-tree bytes. This file preserves the
archive-original pins that were independently matched against the supplied pre-release worktree/archive.

## Verified archive-original pins that differ from Git bytes

| Public Git path | Historical archive-original SHA-256 | Current Git-byte SHA-256 | Historical source |
|---|---|---|---|
| `cosine-xi-mixture/endpoint/RESULT.json` | `e1307ba108ef3161de2e2fae74095a1bd8caa28ed7cd247672e4e1ad7bda5f7d` | `e352946412336878fd04289a704317a36d713f1c85e40a9155c12ca4ec9e6df1` | supplied Windows publication worktree |
| `cosine-xi-mixture/endpoint/VERDICT_REGISTRY.json` | `18ddb92a4cda10452b44ddadf5da41a25891def8d73ad49655098aaa5cc0ea41` | `e134fad4f5da758ad0f36372de519fb2e39b37dbaee653de56a42823d043377c` | supplied Windows publication worktree |
| `cosine-xi-mixture/quantitative-localization/VERDICT_REGISTRY.json` | `c5fe3f3aa986785e0e2f477809b4b100a72981f540ea022763d5e5f72e590f6b` | `542ea1d772e5e96104cb3ff090c04bd928f568825607ed8f624ee4417ebf41e2` | supplied Windows publication worktree |
| `cosine-xi-mixture/strip-transfer/S01_RESULT.json` | `c08afad81e005e98d836ec7a957bbdeb45043def81e764aa80d537dc8ef64e07` | `3818efaf4f643ca2e0b8e205fe879ab7a86fc5779c2226b844c2a19ed7bede5b` | supplied Windows publication worktree |
| `cosine-xi-mixture/strip-transfer/VERDICT_REGISTRY.json` | `cef6c6e1b4d5f253f4cba17d02ce62d2da12466e622dec2890b07491639ec836` | `fd9a30df73f3a8a626bb842ae5c118f6f4eee242af96e045c50c3eb1350e1a34` | supplied Windows publication worktree |
| `simple-zero-bound/proof/EXACT_REPLAY_RECEIPT.json` | `79495ccf0e8ddf24309b033bb0696fdc0a1b05b9c66fa26f627e4206af32642e` | `b2fe4768263c5c73156f088bcbd38095df2dc3283152095603e4d2537907675c` | PGF-C frozen output archive / supplied Windows worktree |
| `simple-zero-bound/proof/RESULT.json` | `ac42ed1e011930779abafa77e156fba7a95e3f098145588a7bc7946c37feddb2` | `cec98b57e074fb090bfcaa823fb6ae4d496fc907143ccdedbca3036a975ca82c` | PGF-C frozen output archive / supplied Windows worktree |
| `simple-zero-bound/audit/INDEPENDENT_FINAL_RECEIPT.json` | `444b9ce7706986b582c7a2682684953b8c9821767e624636f5ea2bbd1d3825c4` | `b36dc6298a12c3a284931b03738927a0385f740e50e45b93a3a2569430f2aa0e` | hostile-audit frozen output archive / supplied Windows worktree |
| `simple-zero-bound/audit/FINAL_PUBLICATION_REFEREE_RESULT.json` | `ac2c7b78efc4e248a4254092eccd0eb459f2c78f9b5429f94de599acb7eead20` | `cbac4fc925f03925d0e60753d013e9168e4f680beb8bdd064c974e8c5b67860a` | final-referee frozen output archive / supplied Windows worktree |

## One stale v0.1 ledger entry not treated as an archive-original pin

The v0.1 hash ledger listed
`cosine-xi-mixture/README.md` as
`fba3d200952552ae1a4ca07b8daa0afed797abaf78c788e8aa25e44ba83a5dcc`.
That value matches neither the actual Git blob nor the supplied Windows publication-worktree bytes.
Both supplied/current byte sources hash to
`d2693f66dc4abf22b61deadf88c67b96429131b730cb0d11fa0a3d8275522571`.
Accordingly the unexplained old value is preserved here only as a stale historical ledger value, not
asserted to be an archive-original binding.

## Frozen package hashes retained for provenance

- original fusion output archive: `a028aa7398cbc0f8bfeb0258c03fdf38244dd24928badcac303905954bd98e5d`;
- original hostile-audit output archive: `d62d4629d003034136670924b2b68cc1c23e0a5fafd95e7ab1447d0fad35596f`;
- original Gebendorfer reproduction archive: `7398223b5f7d33166e25f53742541f6e2518ed95a53541b5b74ec276e4e52a47`.
