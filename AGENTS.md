# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

## Quarto Website Architecture
- Configuration: `_quarto.yml` (website type, MathJax 3 with AMS tags, Dracula code highlighting, dark mode).
- Theme styling: `custom-dark.scss` layered on top of Bootstrap `cyborg`.
- Pages: `index.qmd` (listing with categories/search), `about.qmd` (profile with Jolla template), `archive.qmd` (table listing).
- Posts: `posts/<date>-<slug>/index.qmd`. Each post maintains backwards-compatible URL redirection via `aliases: ["/<slug>/"]`.
- Deployment: GitHub Pages via `.github/workflows/publish.yml` on push to `main`.
- Build & Validation: `quarto render` (must build cleanly to `_site/`). Local preview via `quarto preview`.
- Activity logging: `Journal/<date_time>_<title>.md` (ignored in `.gitignore`).

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
