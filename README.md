# Bible Curriculum

High school Bible curriculum for Watersprings School, built around the *Understanding the Times* series and a cohort-style, discussion-first teaching model.

## Repository Structure

```
bible-curriculum/
├── CLAUDE.md              # Agentic context for Claude Code
├── _skill/                # Reusable skill definitions
├── _shared/               # Shared resources (calendar, tools, resource library)
└── classes/               # One folder per course
    ├── understanding-the-faith/
    ├── old-testament-survey/
    ├── new-testament-survey/
    └── worldview/
```

## Quick Start

This repo is designed to work with [Claude Code](https://claude.ai/code). Two custom commands are available:

- **`/new-class`** — Scaffold a new class with the standard folder structure.
- **`/generate-map`** — Generate a cohort teaching map for any class using the school calendar and chapter list.

## Classes

- **Understanding the Faith** — Active. Full teaching map and lesson structure in place. Grade 11–12.
- **Old Testament Survey** — Stub. Ready for development.
- **New Testament Survey** — Stub. Ready for development.
- **Worldview** — Stub. Ready for development.

## Teaching Model

Every course follows a cohort-style rhythm:

1. **Discussion Brief** — Students write a short position before class discussion.
2. **Pair & Defend** — Paired students argue assigned positions, then debrief.
3. **Case Study** — Small groups work through a real-world scenario and vote on a response.
4. **Capstone** — End-of-unit presentation with Q&A and a final written brief.

See `_shared/cohort-tools.md` for the full reference.
