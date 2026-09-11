# diepjustin.github.io

Personal portfolio site for Justin Diep — journalism, advertising/PR, and broadcasting-media production student at the University of Nebraska-Lincoln. Hosted on **GitHub Pages** at https://diepjustin.github.io.

## Stack

Plain static site — hand-written HTML and inline CSS. No framework, no package manager, no build step. Pushing to `main` publishes the site through the `Publish to Pages` workflow (`.github/workflows/pages.yml`), which stages the checkout and deploys it as a Pages artifact — a push still takes a couple of minutes rather than being instant, though there is nothing left here to build.

## Layout

- `index.html` — the whole homepage in one file (header, About, Awards, Immigration Reporting, Featured Writing, Photography). Sections use `id` anchors (`#about`, `#awards`, `#writing`) and CSS custom properties like `var(--text-color)`.
- `404.html` — custom not-found page.
- `assets/` — profile photo (`diepjustin-mug.jpeg`) and `justin-diep-resume.pdf`, both linked from `index.html`.
- `photos/JPEG/` — the photography the homepage serves. Only this folder is referenced; the camera originals were untracked on 8 Sep 2026.
- `serve.py` — preview server. With every data project split into its own repo, only the homepage lives here now; run it from the repo root and open http://127.0.0.1:8765/, or just open `index.html` directly since the homepage fetches nothing.
- `main-in-ballot-search/` — a small standalone sub-page (`index.html` + `cleanmail.csv`). Not a data project, stays in this repo.
- `robots.txt`, `sitemap.xml` — lists the homepage, ne-contracts and the ballot page. ne-contracts' URL didn't change when it moved to its own repo, so this entry is still correct as-is.

## The data projects

Nebraska public-records/data projects that used to live as sibling folders in this
repo have each moved to their own GitHub repo, still owned by `diepjustin` —
completed 10-11 Sep 2026. Each keeps publishing at the same
`diepjustin.github.io/<name>/` path it always had: a GitHub Pages project repo
serves there automatically, so nothing on the homepage changed. Local clones live
as siblings of this repo directly under `~/Documents/GitHub/`. Each has a README
(unl-events has `MAINTAINING.md`) that is the single source of truth for it —
read that before touching anything inside.

| repo | what | notes |
| --- | --- | --- |
| [`ne-contracts`](https://github.com/diepjustin/ne-contracts) | state contracts and purchase orders | the largest and the one with guard rails — a full scrape is 20+ hours against a government server, see its README before touching the scraper; own Actions-based Pages deploy (tests, lint, payload build from a repo-scoped Actions cache); extraction-data-* releases (long document downloads) live on this repo now, not the portfolio |
| [`ne-connect`](https://github.com/diepjustin/ne-connect) | hub joining contracts, campaign finance and lobbying | `d/entities.json` is committed, unlike ne-contracts' payload; `new/` is the handoff spec the README says it was reconciled against; `ingest/sources.py` reads its three sources from sibling repo clones, so it needs ne-contracts, ne-campaign-finance and ne-lobbying cloned alongside it; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-campaign-finance`](https://github.com/diepjustin/ne-campaign-finance) | NADC bulk extracts | `data/raw/`, `data/processed/` gitignored; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-lobbying`](https://github.com/diepjustin/ne-lobbying) | lobbyist positions and expense forms | CSVs gitignored and exist only locally; long sweeps, see its README; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-ice`](https://github.com/diepjustin/ne-ice) | ICE arrests and detention stays | `build.py` turns gitignored `.xlsx` exports into the committed `data.json`; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-betting`](https://github.com/diepjustin/ne-betting) | Kalshi and Polymarket markets on Nebraska football | `uv`-managed, own `pyproject.toml`; daily collector workflow lives in that repo, cold-started there since the Actions cache didn't carry over the split; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`salary-search`](https://github.com/diepjustin/salary-search) | University of Nebraska salaries, 2010-11 to 2026-27 | roster PDFs and budgeted-employee spreadsheets, each checked against the other; per-year CSVs committed, `data/raw/` is not; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`unl-events-calender`](https://github.com/diepjustin/unl-events-calender) | UNL events by major | nightly workflow lives in that repo and commits `data/events.json`; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |

Each project's tests run with `./venv/bin/python -m pytest tests/ -q` from its own
clone (ne-betting: `uv run pytest`). None of that applies here any more — this
repo has no Python, no tests, and no `.gitignore` rules beyond `.DS_Store` and
`.claude/`.

## Working on the site

- Article/award entries live directly in `index.html` as `.article-card` blocks; each has a `.tag` (publication) and a right-aligned date. Match the existing inline-style pattern when adding entries.
- To preview locally, run `python3 serve.py` in the repo root and open http://127.0.0.1:8765/ (or open `index.html` directly; the homepage fetches nothing).
- Deploy = commit + push to `origin/main` (only when the user asks).
