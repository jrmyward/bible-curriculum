# Apologetics — Course-Wide Publisher Docs

Authoritative course-level documents from the Summit portal. These validate and detail the
deduced [syllabus](../../../syllabus/) and teaching map (`../../../teaching-map.md`, created
by `/generate-map`).

Drop the course-wide exports here as you pull them from summitportal.org. Expected set
(mirrors the *Foundations* volume — confirm the exact titles for this volume on import):

| File | What it is | Notes |
| --- | --- | --- |
| `course-overview.pdf` | Course description + **full lesson-by-lesson outline** (every subsection per chapter) | The map for building compressed lesson plans — the exact publisher lessons to merge into each daily block |
| `scope-and-sequence.pdf` | Official Key Themes + Key Verses per chapter | Confirms chapter count × lessons-per-chapter = publisher day design |
| `teacher-resources-all-chapters.pdf` | All chapters' teacher-resource handouts + tests (`TR n.nA …`) in one file | Source for per-chapter tests; extract to markdown per chapter as needed |
| `presentation-slides-all-chapters.pdf` | Publisher slide deck, all lessons | Large — kept local, not committed (see note) |

## Confirmed facts (fill in after import)

_To be completed once the course-wide docs are staged and read:_

- [ ] Chapter count (scaffolded as 18 — confirm).
- [ ] Lessons-per-chapter / total publisher lessons → drives the compressed pacing.
- [ ] Course goal / worldview focus as stated by the publisher.
- [ ] Any preview or shorter review/conclusion chapters.
- [ ] Whether the final chapter is a **cumulative** test.

## Note on the slide deck

A course-wide `presentation-slides-all-chapters.pdf` is typically large (tens of MB /
hundreds of pp.). It is **kept local, not committed** — large slide decks (`*slides*.pdf`,
`*.pptx`, `*.key`) under `portal/` are gitignored to keep the repo lean. The file lives here
on disk; re-download from the portal if it's ever lost.
