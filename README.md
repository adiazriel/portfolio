# Portfolio

Scaffold for a static portfolio site — plain HTML, CSS, and JavaScript, no
framework or build step. Structure is in place; content is not filled in
yet.

## Structure

```
index.html               Page skeleton: header/nav, hero, about, projects, contact, footer
css/style.css             Base reset + CSS variables (colors, spacing) — no visual design yet
js/main.js                Minimal stub (sets footer year)
assets/images/            Put images here (photos, project screenshots)
content/                  Structured content extracted from the old site goes here
                          (e.g. content/projects.json, content/about.md)
.github/workflows/deploy.yml   GitHub Pages deploy on push to main
```

## Status

- [ ] Extract content/images from the current Squarespace site into `content/` and `assets/images/`
- [ ] Fill in hero, about, projects, contact sections in `index.html`
- [ ] Style the site in `css/style.css`
- [ ] Wire up any interactivity needed in `js/main.js`
- [ ] Enable GitHub Pages (Settings → Pages → Source: GitHub Actions) and deploy

## Run locally

```bash
npx serve .
# or
python3 -m http.server 8000
```
