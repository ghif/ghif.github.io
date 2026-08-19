# Ghif Lab

Personal technical notes from Muhammad Ghifary's work across artificial intelligence, machine learning, computer vision, mathematics, and software implementation.

The site is built with [Quarto](https://quarto.org) and deployed to GitHub Pages through GitHub Actions.

## Site Structure

- `index.qmd`: Landing page with searchable, categorized notes.
- `archive.qmd`: Chronological archive.
- `about.qmd`: Author profile.
- `privacy.qmd`: Analytics and privacy notice.
- `posts/`: Individual Quarto articles and their local `media/` folders.
- `assets/`: Shared site assets, such as the profile image.
- `custom-dark.scss`: Dark theme styling.
- `_quarto.yml`: Website, search, MathJax, analytics, and rendering configuration.
- `scripts/migrate-notion.sh`: Concise Notion-export migration command.

## Local Development

Install [Quarto](https://quarto.org/docs/get-started/) and run:

```bash
quarto preview
```

To render the complete site:

```bash
quarto render
```

Notion exports belong in the ignored `notion-export/` directory. Import one with:

```bash
scripts/migrate-notion.sh <export-directory> <target-post-directory> <category ...>
```

Imports are visible by default. Add `--draft` before the categories only when an article should remain hidden.

## Deployment

A push to `main` renders and deploys the site through `.github/workflows/publish.yml`. The `Journal/`, `notion-export/`, `_site/`, and Quarto cache directories are local-only and are not committed.
