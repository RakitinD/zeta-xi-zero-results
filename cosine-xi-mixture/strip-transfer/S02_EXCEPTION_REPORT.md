# COSXI-S02 exception and phase report

## Set, size and unconditional charge

Use the exact \(a,h,s_0,r,C,\Omega,\mathcal Z,E,M,M_j,Q_\delta(T)\) of PROOF.md (1)–(6). The exception consists of one disk per distinct actual zero in \(\mathcal Z\), each radius in \((T^{-2},2T^{-2})\), with all multiplicities attached to its center. No zero coordinates are required.

The principal geometric metric is Lebesgue measure of the ordinate projection:
\[
 |\operatorname{proj}_x E|\leq4T^{-2}M\leq4T^{-2}Q_\delta(T).
\]
This bound is deterministic for each allowed \(T\), not a probability over zeros. It also says every ordinate outside that projection avoids all selected disks, simultaneously across the collar; no fixed-line distribution theorem is used. It does **not** show that the logarithmic derivative has positive real part on those ordinates.

The separate integer metric is total multiplicity \(M\). Simonič Theorem 1 supplies the unconditional input (9). Three dyadic windows give the explicit (10). This is not bookkeeping in terms of an unknown count without an arithmetic bound. The exponent is \(1-\delta/16\); no density gain for zeta is claimed.

Connected components retain the sum \(M_j\) of all multiplicities when disks merge. Their diameter is at most \(4T^{-2}M_j\). All components whose closures meet the target window lie strictly in the fixed positive-distance collar. No plane-area estimate or number-of-components argument substitutes for a charge estimate.

## Distinct failure events

| Object/event | Definition or role | What is proved here |
|---|---|---|
| P zeros | Zeta/xi zeros in the collar; D has poles there | Covered by E with multiplicity; their full clusters transfer exactly |
| Derivative sign failure | \(P\ne0,\ \Re D<\kappa\log T\) | Sufficient one-sided arithmetic condition (25) is proved; the size of this failure set is not estimated |
| Critical points of log P | \(P\ne0,\ D=0\) | Excluded by \(A>0\) on a hypothesized arc; no unconditional covering/count follows |
| Critical points of D itself | \(D'=0\), when D is holomorphic | Not used by the argument; not silently identified with the preceding event |
| Modulus-balance failure | \(\lambda+\log|P|\ne0\) | For the proved joint regime, it holds throughout \(C\setminus E\); no odd-level arc exists there |
| Chart obstruction | Nonzero logarithmic periods around holes | Handled by integer chart offsets and pathwise phases; no global log P is asserted |
| Original window boundary | Components meeting its boundary, possibly with actual boundary zeros | Every such component pays its full M_j in B_Omega; both open and closed counts are covered |
| Collar/contour failure | A component leaving C, or a comparison contour through a zero | Relevant components stay inside C by (3); component boundaries are zero-free by (19) |

Thus E is a value-domination exception, not a claim that every kind of phase-graph defect lies in the same small set.

## Phase and actual transfer

On the retained set the single-valued power series \(q_\lambda=\operatorname{Log}(1+e^{-\lambda}/P)\) relates local logs of the actual mixture and xi, with the same integer overlap offsets. Its magnitude is at most \(1/(3T)\), giving the actual pathwise phase-change error \(2/(3T)\). Closed-contour windings agree exactly.

For a full positively oriented component boundary the integral of D is \(2\pi iM_j\), independent of the radii. Orientation includes clockwise inner boundaries. P has no poles because all domains lie in \(\Re w>1/2\); the original cosh zeros lie on the omitted line. Arbitrary detours carry their winding-number multiples of M_j, so repeated detours are not assigned a one-circuit budget.

The proved transfer consequence is exact equality of mixture and xi zero multiplicities in each full relevant component. In the original fixed-edge expanding window the discrepancy is at most
\[
 B_\Omega=\sum_{\overline U_j\cap\partial\Omega\ne\varnothing}M_j
 \leq Q_\delta(T).
\]
This also yields the unconditional nonvacuous upper bound \(N_H(\Omega)\leq Q_\delta(T)=o(T)\), for every parameter pair satisfying (3),(5). The set of admissible pairs is explicitly nonempty, since \(\lambda=\Lambda(T)\sim\pi T/2\).

The separate monotone-graph lemma only applies conditionally to specified disjoint balanced arcs with positive A. Its lower crossing count pays one unit per arc and omits endpoint crossings. It has no unconditional almost-every moving-curve application here. The completed consequence does not infer zeros from area or geometric deletion: it transfers and counts the entire charged holes.

