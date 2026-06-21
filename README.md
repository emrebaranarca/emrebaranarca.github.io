# emrebaranarca.github.io

Personal portfolio site for Emre Baran Arca — full-stack software engineer.

Live: [emrebaranarca.github.io](https://emrebaranarca.github.io/) · Türkçe: [/tr.html](https://emrebaranarca.github.io/tr.html)

## Stack

Static site. No framework, no build step. Hand-written HTML + CSS + vanilla JS, served straight from GitHub Pages.

- `index.html` — English version
- `tr.html` — Turkish version
- `404.html` — error page
- `assets/` — portrait, app screenshots, OG image
- `sitemap.xml`, `robots.txt` — SEO
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## Local development

```sh
python3 -m http.server 8000
```

Open http://localhost:8000/.

## Regenerate the social card

```sh
python3 assets/gen_og.py
```

Produces `assets/og.png` (1200×630) used for `og:image` and `twitter:image`.
