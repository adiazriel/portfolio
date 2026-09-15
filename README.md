# Portfolio

Scaffold for a static portfolio site — plain HTML, CSS, and JavaScript, no
framework or build step. Structure is in place; content is not filled in
yet.

## Structure

```
index.html               Page skeleton: header/nav, hero, about, projects, contact, footer
css/style.css             Base reset + CSS variables (colors, spacing) — no visual design yet
js/main.js                Minimal stub (sets footer year)
assets/images/            Project images go here (not downloaded yet, see below)
content/projects.json     Project titles/slugs/image refs extracted from the old Squarespace export
scripts/fetch-images.py   Downloads the images referenced in projects.json into assets/images/
.github/workflows/deploy.yml   GitHub Pages deploy on push to main
```

## Content extracted from Squarespace

`content/projects.json` was generated from a Squarespace WordPress-style
export (Settings → Advanced → Import/Export → Export). It has 19 project
pages with titles, slugs, and references to 13 images — but **no body
text**: Squarespace's export doesn't capture page-builder copy, so every
project's `"description"` field is empty and needs to be written by hand.

Images haven't been downloaded into `assets/images/` yet — this sandbox's
network policy blocks `images.squarespace-cdn.com`. Once that host is
reachable (e.g. from a session whose environment allows it), run:

```bash
python3 scripts/fetch-images.py
```

## Status

- [x] Extract project titles/slugs/image references from Squarespace export → `content/projects.json`
- [ ] Download images via `scripts/fetch-images.py` once network access allows it
- [ ] Write a description for each project (export didn't include body text)
- [ ] Fill in hero, about, projects, contact sections in `index.html` from `content/projects.json`
- [ ] Style the site in `css/style.css`
- [ ] Wire up any interactivity needed in `js/main.js`
- [ ] Enable GitHub Pages (Settings → Pages → Source: GitHub Actions) and deploy

## Run locally

```bash
npx serve .
# or
python3 -m http.server 8000
```
