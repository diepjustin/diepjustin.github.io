# diepjustin.github.io

Personal portfolio site for Justin Diep — journalism, advertising/PR, and broadcasting-media production student at the University of Nebraska-Lincoln. Hosted on **GitHub Pages** at https://diepjustin.github.io.

## Stack

Plain static site — hand-written HTML and inline CSS. No framework, no package manager. Pushing to `main` publishes the site through the `Publish to Pages` workflow (`.github/workflows/pages.yml`), which takes a couple of minutes rather than being instant. Pages is deployed from that workflow's artifact, not from the branch, so the `ne-contracts/` payload never has to be committed — see that folder's `README.md`.

## Layout

- `index.html` — the whole homepage in one file (header, About, Awards, Immigration Reporting, Featured Writing, Photography). Sections use `id` anchors (`#about`, `#awards`, `#writing`) and CSS custom properties like `var(--text-color)`.
- `404.html` — custom not-found page.
- `assets/` — profile photo (`diepjustin-mug.jpeg`) and `justin-diep-resume.pdf`, both linked from `index.html`.
- `photos/` — photography images (UUID- and camera-named `.jpeg/.JPG/.webp/.hires.jpg`).
- `main-in-ballot-search/` — a small standalone sub-page (`index.html` + `cleanmail.csv`).

## Working on the site

- Article/award entries live directly in `index.html` as `.article-card` blocks; each has a `.tag` (publication) and a right-aligned date. Match the existing inline-style pattern when adding entries.
- To preview locally, open `index.html` in a browser or run `python3 -m http.server` in the repo root.
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
