# The Open Dossier Format
## Architectural instructions for AI-assisted, publicly verified independent research

An *Open Dossier* is a research publication shipped as a versioned
repository: executable claims under CI, audited citations, published
adversarial review, a typed claim ledger with honest per-claim
verification status, and DOI-archived releases. Dossier 001 is the
reference specimen; this document is the spec for Dossier 002 and beyond.

Version 1.0 — distilled from the TL-DO-QKD project (Ali-Khan, 2026).
Purpose: take a research idea from conception to a public, checkable
publication with the human's review time concentrated where only human
judgment works. Hand this document to an AI assistant at the start of any
new project and follow the phases in order.

---

## Design principles

1. **Decorrelate the verifier from the generator.** Whoever (or whatever)
   produced a claim must not be its only checker. The three decorrelated
   verifiers available are: executable code, fresh/different AI sessions or
   models, and the human author. Route every claim to at least one of them.
2. **Every claim gets a type, and every type gets a check.** (See the claim
   ledger, Phase 1.)
3. **Honesty beats polish.** "To the best of our knowledge," named caveats,
   and a public list of OPEN findings are features. A claim that survived a
   visible attack is worth more than a claim never attacked.
4. **The human's hours are the scarce resource.** The pipeline's job is to
   shrink the toothcomb to a short, named residue — never to zero. Zero is a
   lie, and the acknowledgments section promises otherwise.
5. **Ship the receipts.** Verification artifacts (scripts, audits, red-team
   reports) are published alongside the paper, not discarded.

---

## Phase 0 — Conception and prior-art reconnaissance (AI-led)

- State the idea in one paragraph. Extract its 3–6 candidate novelty claims.
- Web-search each candidate claim directly ("has X been done"), then search
  the *components* of the idea, then search the *combinations*. Record every
  hit with full citation.
- Produce a RELATION TO PRIOR WORK table: established / adjacent / open.
- **Kill criterion:** if the central claim is prior art, say so plainly and
  either pivot to the open residue or stop. (In the source project, the
  original protocol sketch was ~80% prior art; the open 20% became the paper.)
- Known limit: conference abstracts and in-review work are poorly indexed.
  Novelty claims are always "to the best of our knowledge."

## Phase 1 — The claim ledger (AI-led, human-reviewed)

Build a table of EVERY claim the eventual paper will make. Columns:

| id | claim | type | verifier | status |

Types and their mandated verifiers:
- **CITE** (a source says X): fetch the primary source; verbatim-check
  authors, title, venue, volume, page, year. Triangulation through 3+
  independent citing works is the permitted fallback, flagged as weaker.
- **NUM** (a number follows from stated assumptions): recompute in an
  executable script. No number appears in prose that the script does not
  print.
- **DERIV** (a derivation/proof step): symbolic recomputation where possible
  (sympy), otherwise route to Phase 3 adversarial review AND the human
  residue. Derivations are the highest-risk claim type.
- **NOVEL** (nobody has done X): Phase 0 search record + "to our knowledge"
  phrasing + explicit invitation to correct.
- **EST** (engineering estimate/projection): state all assumptions inline,
  compute in the script, and label as projection in the text. Never let an
  EST masquerade as a NUM.

## Phase 2 — Drafting (AI-led)

- Write the manuscript with the ledger open. Every sentence making a claim
  carries a ledger id (in comments) until the final pass.
- Format: LaTeX for the arXiv artifact; see "Publication format" below for
  the executable companion.
- The Reproducibility section and the AI-assistance acknowledgment are
  mandatory boilerplate.

## Phase 3 — Mechanical verification (AI-led, fully automatic)

- **verify_numbers.(py|ipynb):** recomputes every NUM and EST from stated
  assumptions; prints PASS/FAIL against the manuscript's ranges; exits
  nonzero on any failure. The manuscript is not "done" until this passes —
  and crucially, when it fails, FIX THE MANUSCRIPT OR THE MODEL, never widen
  the tolerance to make the test pass.
- **Citation audit:** re-fetch and re-check every CITE at final-draft stage
  (text drifts; references get added late). Output: citation_audit.md with
  per-entry status and flags.
- If code/data are part of the work: pin dependencies, fix random seeds,
  and run end-to-end from a clean environment.

## Phase 4 — Adversarial review (AI-led, decorrelated sessions)

- Hand the finished draft to FRESH AI sessions — ideally at least one model
  from a different provider — with this brief, verbatim:
  "You are Referee 2. Your goal is to reject this paper. Find: (a) the
  physics/math error that kills it; (b) the prior art that scoops it; (c)
  the internal inconsistency; (d) the overclaim in abstract vs. body; (e)
  the assumption a hostile expert would call naive. Report findings ranked
  by severity. Do not be polite."
- Consolidate into red_team_report.md with findings marked RESOLVED or OPEN.
- Fix what can be fixed; convert the rest into explicit caveats in the
  paper. An OPEN finding stated in the paper is armor; discovered by a
  referee, it is a wound.

## Phase 5 — Human-judgment residue (HUMAN; the few hours that matter)

The AI must hand the human a SHORT, NAMED list — not "please review" but
"these N items are where my judgment is least trustworthy." For a physics
paper, the residue is typically:
1. The one-or-two original derivations (sign conventions, regimes of
   validity) — read with pen and paper.
2. The novelty claims — does the human's domain memory contradict them?
3. The boldest abstract sentences — is the human prepared to defend each
   one to a named expert in the field?
4. Anything the red team left OPEN.
The human signs off item by item. This is the step the acknowledgments
section promises, and the step that makes the human the author in fact,
not just in name.

**Per-claim waiver (the honest-labeling doctrine).** The human may decline
to verify any residue item — that is a legitimate mode of this pipeline,
and for some authors it is the point: judging end results by consistency
and reality checks, as in modern software practice, rather than by
re-derivation. The waiver has exactly one price, and it is non-negotiable:
the claim's ledger status becomes OPEN-UNVERIFIED, the manuscript's
language is softened to match ("is expected to," "we conjecture"), the
acknowledgments state the author's actual review level, and the claim is
posted as an open invitation — ideally with named credit for whoever
closes it. The format's invariant is not that everything is verified; it
is that every label is true. A paper full of honestly-labeled open claims
is a research instrument; a paper with one falsely-labeled verified claim
is dead, and takes the format's credibility with it.

## Phase 6 — Publication and community review

- arXiv FIRST (citable, timestamped priority record), then the open layers:
  repository public, LinkedIn/social pointer post, and direct email with the
  preprint to the 3–6 research groups whose work it builds on, asking for
  criticism. Their replies are the fastest deep review on earth.
- File issues against your own paper as feedback arrives; revise on arXiv
  (v2, v3 — version history is a feature); submit to a journal in parallel
  if desired (Quantum, PRA, npj QI for physics — all preprint-friendly).

---

## Publication format: the executable paper

The PDF is the citable artifact, not the primary one. Recommended repository
layout (GitHub or equivalent), published simultaneously with the arXiv post:

    paper/
      manuscript.tex / .pdf      <- the arXiv artifact
    verification/
      verify_numbers.py          <- Phase 3; CI runs this on every commit
      citation_audit.md
      red_team_report.md         <- including OPEN findings, publicly
      claim_ledger.csv
    notebooks/ or site/
      paper.ipynb / Quarto / MyST source  <- the executable rendition:
         prose interleaved with the live computations behind every figure
         and table; "Run all" reproduces the paper's numbers
    .github/workflows/verify.yml <- CI: the paper's claims are tested like
                                     software; the badge on the README says
                                     "claims: passing"
    README.md                    <- abstract, links, how to check the work,
                                     how to file an issue against a claim

Tooling notes: Quarto or Jupyter Book/MyST render notebook + prose to a live
web page (GitHub Pages) AND to LaTeX/PDF from one source — best of both.
Binder/Colab badges let a reader rerun everything in a browser in one click.
arXiv remains the priority/citation layer because it is what the field
indexes; the repository is the verification layer; the web page is the
reading layer. Use all three; they are not in competition.

---

## What this pipeline does NOT replace

Stated plainly, because the credibility of the whole enterprise depends on
not overclaiming: expert peer review catches things no current pipeline
component catches — wrong framing of a field, an experimental
impracticality known only to practitioners, the unpublished negative result
everyone in the hallway knows about. The pipeline's claim is narrower and
still transformative: it makes every MECHANICALLY CHECKABLE claim checked,
in public, before any referee sees the paper, and it compresses the human
author's verification burden to a few named hours. It raises the floor of
correctness; expert judgment still sets the ceiling.
