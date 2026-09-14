# Editorial source map — not part of the manuscript

## Editorial basis

This is a clean English consolidation of supplied proofs and audit materials. It does not add a new theorem or conduct a new independent proof audit.

1. **Quantitative source:** `COSXI-Q01/QUANTITATIVE_PROOF.md`, taken from the supplied ZIP `96b40b10-2885-4629-97cb-c54a7c8a5347.zip`.
   SHA-256: `3891bc166dd7746c8952299529f0e5f3f490435ea9dd76aea114da2dc3a20667`.
2. **Quantitative audit:** supplied `COSXI-QHC01/AUDIT_REPORT.md`, `VERDICT_REGISTRY.json` and `PRIOR_ART_AUDIT.md` from `6306de07-eac9-4405-9a59-ff59e5e4b34d.zip`. The auditor accepted Q0–Q4, ADD21, ADD22_23, ADD37 and UNIFORM_K as written. N1 was not checked. The audit was by one language-model agent in a separate context, not journal peer review or formal verification.
3. **Qualitative source:** supplied `RH_COS_XI_GLOBAL_NONREAL_V1_1.md`, incorporating the three local clarifications from COSXI-HC01. The English appendices use its mathematical statements and proofs, not the surrounding research-campaign narrative.
4. **Qualitative audit:** supplied COSXI-HC01 analytical report and verdicts. The qualitative growth argument is treated as classical background; no new general-method claim is made.

## Quantitative claim mapping

| Supplied claim | English manuscript location |
|---|---|
| Q0; source equations (11)–(18) | Section 2, exact reduction, domains and all logarithmic levels |
| Q1; source equations (1)–(6) | Theorem 1.1, center definitions in Section 1.1, Sections 4–6 |
| Q2; source equations (7)–(10), (38)–(40) | Theorem 1.2 and Section 6 |
| Q3; source equations (19)–(20) | Lemma 3.1 and its complete proof |
| Q4; source equations (30)–(36) | Proposition 5.1 and its complete proof |
| ADD21 | Equation (3.4), the first reciprocal correction to E |
| ADD22_23 | Equations (3.5)–(3.6); the inherited domain Re(w)>1 is now explicit |
| ADD37 | Equation (5.9), the disk-wide derivative estimate |
| UNIFORM_K | Both main theorem statements and the final paragraph of Section 6 |
| N1 numerical illustrations | Deliberately omitted; not a premise of any analytic claim |

The constants a=2πe³, c_t, D_t, the selected principal branch W_0, the correction −7/2, radius 40/q_n, and the finite sufficient inequalities are unchanged. The phase index is explicitly distinguished from a complete zero enumeration.

## Qualitative claim mapping

| Supplied material | English manuscript location |
|---|---|
| T1.1–T1.4, real-zero tail, imaginary and vertical-strip statements | Appendix A, Theorem A.1 |
| Exact positive theta kernel, strip decay, order/type and imaginary-axis expansion | Appendix A.1 |
| Growth/factorization contradiction | Appendix A.2 |
| E-T0 | Proposition A.2 |
| T2 and the scaled-cosine corollary | Appendix B, Proposition B.1 and Corollary B.2 |

LC1 is included through the height max(M,d) and radius d<π/(2ω). LC2 is included as a one-sided upper bound. LC3 is included through the common tail threshold for 0≤t≤t_0<1 and the compact-complement argument. The source's lower-order growth terms and domains are preserved.

## Editorial changes

- Translated and consolidated the proofs into ordinary mathematical prose.
- Put the quantitative theorem first; moved the qualitative result and its general form to appendices.
- Renumbered statements, equations and references; removed workflow IDs, pass/fail labels and administrative logs from the paper.
- Used ν instead of the source's auxiliary ζ for the Cauchy-circle coordinate, and ϱ instead of ρ for the modulus in the phase calculation, to avoid notational collisions. The mathematics is unchanged.
- Made the inherited phase-equation domain Re(w)>1 explicit; estimates still require Re(w)≥2.
- Included the audit's elementary checks of the numerical constants in the finite criterion.
- Omitted non-interval numerical examples and source-code execution logs.
- Added a short AI-assistance disclosure based on the documented workflow. It makes no claim of human peer review or formal verification.
- Separated author metadata from the mathematical source.

## Bibliography and research boundary

Public pages were used only to check bibliographic details and the cited statements. No unpublished manuscript or theorem was uploaded to an external service. The references are the sources already used in the supplied proofs/audits: NIST DLMF; Lagarias–Montague; Csordas–Smith; Borwein–Corless; Gardner's factorization notes.

The Lagarias–Montague journal metadata was checked against the authors' arXiv record. Csordas–Smith is cited as the inspected author-hosted manuscript; unverified journal metadata was not supplied. Borwein–Corless is cited in the inspected arXiv version. The bibliography does not silently upgrade uninspected Salvy or Boas originals into verified dependencies. The comparison with prior work is limited to the cited statements; no worldwide novelty or priority conclusion is added.

## Verification limits

The new checks concern source coverage, constants carried into the typeset text, LaTeX references, compilation and visual layout. The source proofs were previously audited; this editorial edition has not itself received a new independent mathematical audit. Neither the local production report nor its file hashes is an external priority record.

## Exact input digests

```json
{
  "QUANTITATIVE_PROOF_RU.md": "3891bc166dd7746c8952299529f0e5f3f490435ea9dd76aea114da2dc3a20667",
  "RH_COS_XI_GLOBAL_NONREAL_V1_1.md": "c7cebe9fb14997f8a18027872f0cd38626b2ba5fc8fc82bcda7fef0cb0532a58",
  "QHC01_AUDIT_REPORT.md": "d3bd4d188d4e006129557eb92b70b6a5d8e9e40982d26ba6589bd5ccfdef4d74",
  "QHC01_PRIOR_ART_AUDIT.md": "a7b6edd5209dcadce3f2b66e1df7e52e8e21431adc19129c549e515fe0f0e34c"
}
```
