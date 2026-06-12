# Red-Team Report — manuscript.tex (Ali-Khan 2026, TL-DO-QKD)

Brief: attack the paper the way a hostile, competent referee would. Findings
ordered by severity. Items marked RESOLVED were fixed during this audit;
items marked OPEN require the author's judgment or further work and should be
expected in referee reports.

---

## Finding 1 — RESOLVED: Table 1 and abstract overstated PIE by 1.5–2.5 bits

The original Table 1 claimed 14–15 bits (30 ps / M=158 row) and 16–17 bits
(3 ps / M=30 row). Recomputation from the caption's own stated parameters
(verify_numbers.py, Table 1 section) gives 13.07 and 14.42 bits respectively.
The discrepancy traced to implicitly assuming a negligible lens point-spread
width while the caption stated 1.3 ps and 0.5 ps. The abstract inherited the
inflated "14–17" range.

**Action taken:** Table corrected to 13 and 14–15; abstract corrected to
"13–15 bits ... approaching the 17.3-bit correlation-time floor"; Sec. 4.1
gain example corrected 2.5 → 2.4 bits; Sec. 4.2 break-even corrected
0.64 → 0.66. The headline 10^8 b/s order-of-magnitude claim survives the
correction (verified: 3.1e7–3.8e8 b/s across conservative/aggressive
parameter choices).

**Lesson encoded in pipeline doc:** prose numbers drift from their own stated
assumptions during editing; only executable recomputation catches this class
of error reliably.

## Finding 2 — OPEN (highest referee risk): the nonlocal imaging claim has no
## derivation in the paper

Section 5 asserts, "at the Gaussian level," that fiber dispersion on Bob's
photon can serve as D_in of an imaging system completed at Alice, citing the
Tsang–Psaltis/Patera formalism. No derivation is shown. A referee will demand
the explicit two-photon amplitude propagated through the distributed system,
with sign conventions for anomalous vs. normal dispersion made explicit, and
will check whether the imaging condition Eq. (8) really applies to the
difference coordinate with the claimed sign (the frequency anticorrelation
flips a sign relative to the single-photon case; the paper waves at this).

**Recommendation:** add a short appendix deriving the magnified coincidence
distribution for Gaussian envelopes, or soften "yields" to "is expected to
yield" and explicitly defer the derivation. The first option is far stronger.
This is the single most likely place for the paper to contain a real physics
error, because it is the only nontrivial derivation done from scratch.

**Author disposition (v1.0):** hand derivation declined by design — this
project's thesis is judging end results by reality checks, not re-derivation.
Manuscript language softened to "is expected to yield"; the derivation is
declared open in the text itself; claim C11 is labeled OPEN-UNVERIFIED in the
ledger; confirmation or refutation is invited as a community contribution,
with the first correct treatment credited in v1.1. The finding therefore
remains OPEN, honestly labeled, by choice rather than oversight.

## Finding 3 — OPEN: lens temporal field of view vs. cw frames may gut the
## practical rate

The protocol assumes a cw pump (to maximize T_coh and hence K), but the time
lens must cover the photon's arrival uncertainty, which for cw operation is
the full 64 ns frame. The demonstrated lens of Joshi et al. has a field of
view orders of magnitude smaller. The paper acknowledges this (Sec. 5
caveats) and gestures at pulsed/Talbot pumps or triggered lenses, but a
referee can argue the headline PIE assumes cw frames while the enabling
component assumes localized arrivals — i.e., the two key assumptions are in
tension. The aperture-duty-cycle penalty is not quantified anywhere.

**Recommendation:** add one honest paragraph quantifying the duty-cycle
penalty for a gated-lens architecture (effective rate × FOV/T_f unless the
pump is structured), and present the pulsed-pump variant's reduced K
explicitly. Better to state the tension's cost than to let the referee
discover it.

## Finding 4 — OPEN: the saturation-rate argument is qualitative where it
## needs one inequality

Eq. (9) multiplies away lens loss by "pump harder," bounded only by a verbal
appeal to multi-pair statistics. A referee will ask: at what mean pair number
per frame does the multi-pair Holevo penalty cancel the magnification gain?
One inequality (mu_max as a function of frame occupancy and accidental floor,
in the style of Zhong et al. 2015 supplementary) would close this. Also kappa
(coincidence-to-singles ratio) is used but never given a justified value.

## Finding 5 — OPEN: novelty claims have a literature-recall ceiling

Claims (i)–(iv) in Sec. 2 are phrased "to the best of our knowledge," which is
correct practice, and the search conducted for this audit found no prior
integration of single-photon time lenses into QKD protocols. But: (a)
conference proceedings (CLEO/QCrypt abstracts) are poorly indexed and were not
exhaustively searched; (b) U.S. Patent 8,744,086 covers adjacent hybrid
time-frequency territory and its claims have not been read against this
protocol; (c) the quantum temporal imaging community (Kolobov, Horoshko,
Karpinski groups) may have proposals in review right now — the Joshi paper
explicitly flags "temporal mode quantum processing" as the application space.
Residual scoop/priority risk is real and is the strongest argument for
preprinting quickly rather than polishing long.

## Finding 6 — OPEN (timeliness): the "parity with record" claim has a short
## shelf life

115.8 Mb/s (Li 2023) is the verified DV record, but Gb/s-class CV-QKD
preprints already exist (noted in text via arXiv:2503.14843) and one may be
published any month. The paper's framing already hedges correctly (parity,
not supremacy; PIE is the real claim), but the author should expect to update
this paragraph at the proof stage, and should not let any press/LinkedIn
framing say "fastest QKD ever proposed."

## Finding 7 — minor: security claims to tighten

- "cannot increase Eve's information" (Sec. 4.3) is correct for a
  characterized local map but the bypass audit is a calibration check, not a
  proof element; one sentence should say so plainly (it nearly does).
- The Gaussian/TFCM bound is collective-attack; composable general-attack
  security via Niu et al. is asserted to "carry over" — a referee may ask for
  the conditions (the entropic uncertainty relation there assumes specific
  measurement models; the magnifier changes the measurement POVM). Recommend
  weakening to "is expected to carry over, with the magnifier absorbed into
  the measurement characterization" unless the author verifies the proof's
  assumptions directly.

## Finding 8 — minor: one bibliography page number from secondary sources

Grunenfelder2023 page (422) verified only by triangulation. One-minute check
on nature.com before submission (see citation_audit.md).

---

## Summary verdict

The paper's core quantitative spine now survives recomputation (16/16 checks).
The two load-bearing risks are Finding 2 (the one original derivation, not
shown) and Finding 3 (cw-frame vs. lens-aperture tension, not quantified).
Both are fixable with one appendix and one paragraph. Findings 4–7 are
referee-management. Nothing found contradicts the paper's central claims; the
corrections required were quantitative (1.5–2.5 bits), not structural.
