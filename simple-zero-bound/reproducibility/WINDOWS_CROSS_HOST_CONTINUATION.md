# Windows cross-host continuation procedure

The original Gebendorfer `reproduce.py --full` is preserved unmodified.

On the Windows replay host it completed all nine local proofs and then stopped at the raw-byte
check for `cover_boxes.txt`. Native Windows text mode writes CRLF, whereas the frozen artifact
uses LF.

The public release includes the exact continuation overlays used after that failure:

- `RH_GEBENDORFER_COVER_CONTINUATION_HOTFIX_V1.zip`
- `RH_GEBENDORFER_CROSS_HOST_FREEZE_HOTFIX_V2.zip`

Observed replay accounting:

- local: 50,089,182 nodes;
- cover: 7,638,774 nodes;
- restricted: 849,081 nodes;
- total: 58,577,037 nodes.

The continuation verifies:
- regenerated rigorous tables;
- complete cover;
- LF-normalized and row-sequence equality;
- byte-identical 71-box coarsening;
- row-sequence equality of the joined 281 boxes;
- restricted proof;
- unchanged frozen source tree.

This is a cross-host computational replay, not a claim that the original single-process
raw-byte runner returned success on Windows.
