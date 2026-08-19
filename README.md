# Ghif's Research Notes

Personal research blog and digital notebook on Machine Learning, Computer Vision, Deep Learning, and Foundational Mathematics by Muhammad Ghifary.

Built with [Quarto](https://quarto.org) and deployed via GitHub Actions to GitHub Pages.

## Site Structure

- `index.qmd`: Homepage listing of technical notes and articles with category filters and search.
- `archive.qmd`: Tabular chronological archive of all notes.
- `about.qmd`: Researcher profile and biography.
- `posts/`: Individual technical articles and research derivations.
- `assets/`: Media and diagram assets.
- `custom-dark.scss`: High-contrast dark theme styling overrides.
- `_quarto.yml`: Quarto website configuration and MathJax AMS equation numbering setup.

## Local Development & Preview

To preview the website locally with live reload:

```bash
# Preview the site locally
quarto preview

# Render the complete site to _site/
quarto render
```

## Publishing & Deployment

The site is automatically rendered and deployed to GitHub Pages via GitHub Actions upon push to `main` using `.github/workflows/publish.yml`.
