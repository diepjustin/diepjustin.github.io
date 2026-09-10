# diepjustin.github.io

Personal portfolio site for Justin Diep — journalism, advertising/PR, and broadcasting-media production student at the University of Nebraska-Lincoln. Hosted on **GitHub Pages** at https://diepjustin.github.io.

## Stack

Plain static site — hand-written HTML and inline CSS. No framework, no package manager. Pushing to `main` publishes the site through the `Publish to Pages` workflow (`.github/workflows/pages.yml`), which takes a couple of minutes rather than being instant. Pages is deployed from that workflow's artifact, not from the branch, so the `ne-contracts/` payload never has to be committed — see that folder's `README.md`.

## Layout

- `index.html` — the whole homepage in one file (header, About, Awards, Immigration Reporting, Featured Writing, Photography). Sections use `id` anchors (`#about`, `#awards`, `#writing`) and CSS custom properties like `var(--text-color)`.
- `404.html` — custom not-found page.
- `assets/` — profile photo (`diepjustin-mug.jpeg`) and `justin-diep-resume.pdf`, both linked from `index.html`.
- `photos/JPEG/` — the photography the homepage serves. Only this folder is referenced; the camera originals were untracked on 8 Sep 2026.
- `serve.py` — preview server for the whole repo. Serves the root so every project loads at its Pages path; takes an optional port.
- `main-in-ballot-search/` — a small standalone sub-page (`index.html` + `cleanmail.csv`).
- `robots.txt`, `sitemap.xml` — the sitemap lists only the homepage, ne-contracts and the ballot page.

## The data projects

Each of these was originally a sibling folder in this repo, publishing at that folder's URL. They are being migrated one at a time to their own GitHub repo, still owned by `diepjustin`, so each keeps publishing at the same `diepjustin.github.io/<name>/` path — a GitHub Pages project repo serves there automatically, so nothing on the homepage has to change. Local clones live as siblings of this repo directly under `~/Documents/GitHub/`. Each has a README (unl-events has `MAINTAINING.md`) that is the single source of truth for it.

| repo/folder | what | notes |
| --- | --- | --- |
| `ne-contracts/` | state contracts and purchase orders | see below; the largest and the one with guard rails; still in this repo |
| `ne-connect/` | hub joining contracts, campaign finance and lobbying | `d/entities.json` is committed, unlike ne-contracts' payload; `new/` is the handoff spec the README says it was reconciled against; still in this repo |
| [`ne-campaign-finance`](https://github.com/diepjustin/ne-campaign-finance) | NADC bulk extracts | split out 10 Sep 2026; `data/raw/`, `data/processed/` gitignored; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-lobbying`](https://github.com/diepjustin/ne-lobbying) | lobbyist positions and expense forms | split out 10 Sep 2026; CSVs gitignored and exist only locally; long sweeps, see its README; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| [`ne-ice`](https://github.com/diepjustin/ne-ice) | ICE arrests and detention stays | split out 10 Sep 2026; `build.py` turns gitignored `.xlsx` exports into the committed `data.json`; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| `ne-betting/` | Kalshi and Polymarket markets on Nebraska football | `uv`-managed, own `pyproject.toml`; daily collector workflow; still in this repo |
| [`salary-search`](https://github.com/diepjustin/salary-search) | University of Nebraska salaries, 2010-11 to 2026-27 | split out 10 Sep 2026; roster PDFs and budgeted-employee spreadsheets, each checked against the other; per-year CSVs committed, `data/raw/` is not; deploys from its own `main` (branch-deploy Pages, `.nojekyll`) |
| `unl-events-calender/` | UNL events by major | nightly workflow commits `data/events.json`; still in this repo |

Python working files (`venv/`, `__pycache__/`, `.pytest_cache/`) are ignored from the root `.gitignore`; each project's own `.gitignore` carries only its data rules. Every project's tests run with `./venv/bin/python -m pytest tests/ -q` from its folder (ne-betting: `uv run pytest`).

## Working on the site

- Article/award entries live directly in `index.html` as `.article-card` blocks; each has a `.tag` (publication) and a right-aligned date. Match the existing inline-style pattern when adding entries.
- To preview locally, run `python3 serve.py` in the repo root and open http://127.0.0.1:8765/ (or open `index.html` directly; the homepage fetches nothing).
- Deploy = commit + push to `origin/main` (only when the user asks).

## `ne-contracts/`

A second, much larger project living in this same repo: a scraper and static
searchable site for Nebraska state spending records, published at
`https://diepjustin.github.io/ne-contracts/` off this repo's `main` branch.
Its `README.md` is the single source of truth for that project — data caveats,
architecture, guard rails, things that bit us before, and what is still open.
(It absorbed the separate `HANDOFF.md` on 17 Aug 2026; two documents covering
the same ground had already drifted apart and shipped a false claim to the
site.) Read it before touching anything in that folder, especially the guard
rails before re-running the scraper — a full run is 20+ hours against a
government server.
