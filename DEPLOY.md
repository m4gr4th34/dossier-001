# DEPLOY.md — Dossier 001 launch sheet
## From zip to live, DOI'd publication. No command line required.

Total time: ~20 minutes. Steps 1–4 get you live; 5–6 get you a DOI; 7 is launch.

---

### Step 1 — Create the repository (2 min)
1. Go to **github.com/new**.
2. Repository name: `dossier-001` (or your choice — short is better for the URL).
3. Description box (optional but do it): `Dossier 001 — the first Open Dossier. Don't trust this paper — run it.`
4. **Public**. Do NOT initialize with a README (you're bringing your own).
5. Click **Create repository**.

### Step 2 — Upload the files (5 min)
1. Unzip `dossier-001.zip` on your computer.
2. On the new repo page, click **"uploading an existing file"**.
3. Drag the ENTIRE CONTENTS of the unzipped folder (not the folder itself)
   into the upload area — including the `paper/` and `verification/` folders.
   GitHub preserves folder structure on drag-and-drop.
4. ⚠️ The `.github` folder (hidden, starts with a dot) sometimes doesn't drag
   from Finder/Explorer. If it's missing after upload: in the repo click
   **Add file → Create new file**, type the path
   `.github/workflows/verify.yml`, and paste in the contents of that file
   from the zip.
5. Commit message: `Dossier 001 — v1.0`. Click **Commit changes**.

### Step 3 — Fix the placeholders (3 min)
The files contain `YOURUSER` and `YOURREPO` placeholders. In the repo, open
each of these, click the pencil (edit), use your browser's find (Ctrl/Cmd-F)
to locate and replace, then commit:
- `README.md` (badge URL, Pages links)
- `index.html` (two links: "Source & issues" button, "file an issue" footer)
- `CITATION.cff` (repository-code and url lines)

Replace with your actual username and repo name, e.g. `iak-physics/dossier-001`.

### Step 4 — Turn on the website (2 min)
1. Repo → **Settings → Pages** (left sidebar).
2. Source: **Deploy from a branch**. Branch: **main**, folder: **/ (root)**. Save.
3. Wait ~2 minutes. Your paper is live at
   `https://YOURUSER.github.io/dossier-001/`
4. Meanwhile, check the **Actions** tab: the `verify-claims` workflow should
   already show a green check — that's CI recomputing the paper's 16 claims.
   The README badge goes green with it.

✅ **You are now published** — versioned, traceable, executable. Steps 5–6
make it permanently archived and citable.

### Step 5 — Connect Zenodo for the DOI (4 min)
1. Go to **zenodo.org** → Log in → **Sign in with GitHub**. Authorize.
2. In Zenodo: click your name → **GitHub** (in the dropdown).
3. Find `dossier-001` in the repository list and flip its toggle **ON**.
   (If it's not listed, click "Sync now".)

### Step 6 — Tag v1.0 = the publication event (3 min)
1. Back on GitHub: repo → **Releases** (right sidebar) → **Create a new release**.
2. Tag: `v1.0.0`. Title: `Dossier 001 — v1.0 (publication of record)`.
3. Description: paste the abstract. Click **Publish release**.
4. Zenodo automatically archives the release and mints a **DOI** (check the
   GitHub page on Zenodo a minute later; the DOI badge appears there).
5. Copy the DOI badge markdown Zenodo gives you, edit `README.md`, and paste
   it where the comment says so. Also add the DOI to `CITATION.cff` as a new
   line:  `doi: "10.5281/zenodo.XXXXXXX"`.

Your work is now archived at CERN, has a permanent citable identifier, and is
indexed independently of GitHub's existence. (Software Heritage also archives
public GitHub repos automatically; you can trigger it explicitly at
archive.softwareheritage.org → "Save code now" if you want belt and braces.)

### Step 6b — OpenTimestamps (optional, 3 min)
For institution-free, cryptographic proof of priority: download your release
archive (Releases page -> v1.0.0 -> "Source code (tar.gz)"), go to
**opentimestamps.org**, drag the file in, and download the `.ots` proof file
it gives you. Commit the `.ots` file to the repo. Your release hash is now
anchored in the Bitcoin blockchain - anyone can verify what existed and when,
trusting no institution, forever.

### Step 7 — Launch (your move)
- LinkedIn post linking the **Pages URL** (not the repo — lead with the
  living paper, mention "view source / file an issue" as the kicker).
- Direct emails with the link to the groups the work builds on (DO-QKD
  lineage at MIT; the Gaeta time-lens group; Karpiński's lab). One paragraph,
  one link, one question: "I'd value your criticism — issues tab is open."
- Pin the repo on your GitHub profile.

### Updating after launch (the living part)
Edit any file → commit. The site updates in ~1 minute; CI re-verifies the
claims; the history records everything. For substantive revisions, cut a new
release (`v1.1.0` etc.) — Zenodo mints a new version DOI automatically while
the concept DOI keeps pointing at the latest. Reviewer comments arrive as
issues; your replies are part of the permanent record. That's the format.
