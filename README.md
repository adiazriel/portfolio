# Portfolio

A static portfolio website built with plain HTML, CSS, and JavaScript — no
framework, no build step, no hosting fees.

## Structure

```
index.html        Single-page site: hero, about, projects, skills, contact
css/style.css      All styling, incl. light/dark theme
js/main.js         Mobile nav, theme toggle, scroll-reveal animation
.github/workflows/deploy.yml   Auto-deploys to GitHub Pages on push to main
```

## Customize

- Replace "Adi Zilber" and the tagline/bio text in `index.html`.
- Swap the placeholder project cards under `#projects` with your real
  projects (title, description, tags, links). Add real screenshots by
  putting images in `assets/` and swapping the `.project-thumb` gradient
  divs for `<img>` tags.
- Update the contact email and add real social links under `#contact`.
- Colors and spacing live in CSS custom properties at the top of
  `css/style.css` (`:root`) — change `--accent` to re-theme the whole site.

## Run locally

No build tools required. Either:

- Open `index.html` directly in a browser, or
- Serve it locally for a closer-to-production setup:

```bash
npx serve .
# or
python3 -m http.server 8000
```

## Deploy

This repo includes a GitHub Actions workflow that deploys to **GitHub
Pages** automatically on every push to `main`.

To enable it:
1. Push this repo to GitHub (if not already there).
2. Go to **Settings → Pages** in the GitHub repo.
3. Under "Build and deployment", set **Source** to "GitHub Actions".
4. Push to `main` — the site will be live at
   `https://<your-username>.github.io/<repo-name>/`.

No Squarespace subscription needed going forward — this repo *is* the site.
