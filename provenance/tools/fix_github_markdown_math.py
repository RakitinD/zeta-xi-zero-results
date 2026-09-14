from pathlib import Path
import re
import hashlib

ROOT = Path.cwd()

FILES = [
    Path("README.md"),
    Path("simple-zero-bound/README.md"),
    Path("simple-zero-bound/THEOREM_STATEMENTS.md"),
    Path("simple-zero-bound/preprint/PREPRINT.md"),
    Path("cosine-xi-mixture/README.md"),
    Path("cosine-xi-mixture/THEOREM_SUITE_V2.md"),
    Path("cosine-xi-mixture/BRIDGE_RESULTS.md"),
    Path("cosine-xi-mixture/RESULTS_STATUS.md"),
]

def convert_outside_fences(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out = []
    in_fence = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence:
            line = line.replace(r"\[", "$$").replace(r"\]", "$$")
            line = line.replace(r"\(", "$").replace(r"\)", "$")
        out.append(line)
    return "".join(out)

changed = []
for rel in FILES:
    p = ROOT / rel
    if not p.exists():
        raise SystemExit(f"missing expected file: {rel}")
    old = p.read_text(encoding="utf-8")
    new = convert_outside_fences(old)

    # GitHub does not reliably render display math indented inside a numbered list.
    if rel == Path("README.md"):
        new = re.sub(
            r"(?ms)^2\. completeness of the nonreal tail and\s*\n\s*\$\$\s*\n"
            r"\s*N_t\^\{\\rm nr\}\(R\)\\sim \\frac\{R\\log R\}\{\\pi\};\s*\n\s*\$\$",
            r"2. completeness of the nonreal tail and $N_t^{\\rm nr}(R)\\sim \\frac{R\\log R}{\\pi}$;",
            new,
        )

    if new != old:
        p.write_text(new, encoding="utf-8", newline="\n")
        changed.append(str(rel).replace("\\", "/"))

# Recompute the repository hash ledger, but do not hash the ledger itself.
ledger = ROOT / "provenance" / "GIT_TREE_HASHES_SHA256.txt"
rows = []
for p in sorted(ROOT.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if rel == Path("provenance/GIT_TREE_HASHES_SHA256.txt"):
        continue
    if ".git" in rel.parts:
        continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    rows.append(f"{h}  {str(rel).replace(chr(92), '/')}")

ledger.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")

print("GITHUB_MARKDOWN_MATH_PATCH = PASS")
print("changed_files =", len(changed))
for x in changed:
    print(" ", x)
print("hash_ledger_rebuilt =", ledger)
