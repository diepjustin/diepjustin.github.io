# diepjustin.github.io

Justin Diep's personal site, and the reporting project that grew out of it.
Live at **[diepjustin.github.io](https://diepjustin.github.io)**.

Justin is a journalism, advertising/PR and broadcasting-media production student
at the University of Nebraska–Lincoln.

---

## Nebraska State Contracts

**[diepjustin.github.io/ne-contracts](https://diepjustin.github.io/ne-contracts/)**

The state publishes its contracts and purchase orders one record at a time,
behind a search form. This scrapes them and rebuilds the lot as a single page
you can search, filter and sort in the browser.

| | |
| --- | ---: |
| Records | 743,899 |
| Entities — every state agency, board and commission, plus all nine University of Nebraska and Nebraska State College campuses | 92 |
| Records carrying the state's own description of the work | 551,018 |
| Records asked what documents they publish | 741,852 |
| Records publishing more than one document | 37,609 |

Everything on the page is the state's own words. Descriptions are lifted from
the filings verbatim — never rewritten, never summarised — and where one could
not be read the page says so rather than leaving a blank to be misread.

The whole thing is static: no server, no database, no API. The payload is packed
into binary columns so 743,899 rows can be filtered on a keystroke, with link
tokens and descriptions fetched only for the rows someone actually opens.

**[`ne-contracts/README.md`](ne-contracts/README.md) is the real documentation** —
what the data does and does not cover, how the scraper and payload work, the
guard rails around re-running it, and a long list of things that went wrong and
what they cost. Read it before changing anything in that folder.

### Before quoting it

The scraper reproduces the state's records faithfully, including their errors.
This is **not** a complete record of state spending: by the state's own
[FAQ](https://das.nebraska.gov/materiel/contract-database/faq.html) the database
excludes several agencies' contracts entirely, and only documents active on or
after 1 January 2014 are in it at all. The full list of gaps, quirks and known
bad values is in that folder's README.

---

## The rest of the repo

| | |
| --- | --- |
| `index.html` | the homepage — about, awards, immigration reporting, featured writing, photography |
| `404.html` | custom not-found page |
| `assets/`, `photos/` | profile photo, résumé, and the photography on the homepage |
| `main-in-ballot-search/` | a small standalone lookup page |
| `ne-contracts/` | the contracts scraper and site |

Plain HTML and CSS, hand-written, with no framework and no build step for the
site itself. GitHub Pages publishes from the `Publish to Pages` workflow rather
than from the branch, so the contracts payload never has to be committed.

---

Public records used here come from the Nebraska Department of Administrative
Services and are published under
[Neb. Rev. Stat. § 84-602.04](https://nebraskalegislature.gov/laws/statutes.php?statute=84-602.04).
Code is MIT licensed — see [`ne-contracts/LICENSE`](ne-contracts/LICENSE).
