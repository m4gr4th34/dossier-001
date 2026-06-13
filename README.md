# Dossier 001 — Temporal-Imaging-Enhanced Dispersive-Optics QKD

**The first publication in the Open Dossier format: a living, executable, publicly audited research record.**
*Don't trust this paper — run it.*
Irfan Ali-Khan · Independent Researcher · Saratoga, California · June 2026

[![claims: verified](https://github.com/m4gr4th34/dossier-001/actions/workflows/verify.yml/badge.svg)](https://github.com/m4gr4th34/dossier-001/actions/workflows/verify.yml)
<!-- After Zenodo release, paste your DOI badge here: -->
<!-- [![DOI](https://zenodo.org/badge/1267581633.svg)](https://doi.org/10.5281/zenodo.20670769) -->
[![DOI](https://zenodo.org/badge/1267581633.svg)](https://doi.org/10.5281/zenodo.20670769)

## What this is

A proposal for quantum key distribution that places single-photon **time
lenses** inside the receivers of a dispersive-optics QKD link, magnifying the
arrival-time structure of energy–time entangled photon pairs before detection
— projecting 13–15 bits per detected coincidence and key rates of order
10⁸ b/s from demonstrated components, plus a **nonlocal variant** in which the
transmission fiber's own dispersion completes an imaging system that exists
only in coincidences.

And, deliberately, it is also a working specimen of a publication format:
**every quantitative claim in the paper is executable, every revision is
versioned, and the adversarial review ships with the work.**

## Read it

- **Living paper (start here):** https://m4gr4th34.github.io/dossier-001/
- **Audit trail** (red team, citation audit, live checks): https://m4gr4th34.github.io/dossier-001/dossier.html
- **PDF:** [`paper/manuscript.pdf`](paper/manuscript.pdf)

## Run it

```bash
python3 verification/verify_numbers.py
```

Sixteen checks recompute every number in the manuscript from its stated
assumptions and exit nonzero on any failure. CI runs this on every commit —
the badge above is the paper's claims passing, continuously. The same checks
run in your browser on the living-paper page.

## Review it

This repository **is** the review venue. To referee this paper:

1. Run the checks; drag the explorer past its stated ranges.
2. Read [`verification/red_team_report.md`](verification/red_team_report.md)
   — 1 resolved finding, 7 open ones, published rather than hidden.
3. **[File an issue](../../issues) against any claim** — cite the claim id
   from [`claim_ledger.csv`](claim_ledger.csv) if possible. Disagreement is a
   contribution. Every response is versioned; nothing is memory-holed.

Known open items a referee should attack first: the nonlocal-imaging
derivation (Finding 2 — posted as an **open challenge**, see below) and the
cw-frame vs. lens-aperture tension (Finding 3).

## The open challenge

Claim **C11** — the Section 5 nonlocal distributed-imaging condition — is
labeled `OPEN-UNVERIFIED` in the ledger, by design. Nobody, human or machine,
has carried the derivation through. **The first correct treatment, confirming
or refuting it, gets named credit in release v1.1.** Fork, branch, derive,
open a PR. This is what "review venue" means here: unknown, unrelated people
chipping away at an idea in public, with the version history preserving
exactly who contributed what, when.

## Priority & ownership

Attribution is preserved by the record itself, not by gatekeepers:

- **Git history** — every contribution hashed, attributed, and ordered.
- **Tagged releases + Zenodo DOI** — each version archived at CERN with a
  permanent citable identifier.
- **Software Heritage** — independent perpetual archive of the repository.
- **OpenTimestamps** (optional, see `DEPLOY.md`) — release hashes anchored in
  the Bitcoin blockchain: institution-free, cryptographic proof of priority.

Fork it, branch it, attack it. The record keeps the receipts.

## Repository map

| Path | Layer |
|---|---|
| `index.html`, `dossier.html` | Reading layer (GitHub Pages) |
| `paper/manuscript.tex` / `.pdf` | Citable artifact |
| `verification/verify_numbers.py` | Executable claims (CI-enforced) |
| `verification/citation_audit.md` | All 37 references, verification status |
| `verification/red_team_report.md` | Adversarial review, RESOLVED + OPEN |
| `verification/research_pipeline.md` | The method, reusable for Dossier 002 |
| `claim_ledger.csv` | Every claim, typed and routed to its verifier |

## Cite it

See [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository"
button from it). Tagged releases are archived with a DOI via Zenodo.

## Disclosure

Built with substantive AI assistance (Claude, Anthropic): literature search,
prior-art analysis, drafting, rate modeling, verification tooling, and the
site. The verification model is **honest labeling, not universal
verification**: every claim carries a public, granular status (machine-
recomputed, source-audited, reality-checked, or open), and claims nobody has
verified are labeled, never asserted. The author's review was conducted at
the level of consistency and reality checks on end results — the thesis of
this project is that, as in modern software practice, that plus public
machine verification plus open community review is a stronger guarantee than
a private hand-check nobody can inspect. Responsibility rests with the
author on that explicitly stated basis.

## License

Paper and prose: CC BY 4.0 · Code: MIT. See [`LICENSE.md`](LICENSE.md).
