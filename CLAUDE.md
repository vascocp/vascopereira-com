# vascopereira.eu

Personal/photography site for Vasco Pereira.

## Domains
- **vascopereira.eu**: the new site, built from this repo. Hosted on Vercel, which deploys from GitHub.
- **vascopereira.com** and **vascopereira.pt**: the old sites. Use them for reference and content only, never edit them from here.
- Plan: once .eu is ready, both old domains get a 301 redirect to vascopereira.eu.
- The repo is named `vascopereira-com` for historical reasons. It is the .eu site.

## Structure
Static HTML with inline CSS. No build step, no framework.
- `index.html`: the live site (served at the root).
- `styles.html`: index of design explorations; `style-*.html` are the alternative visual directions (analog, bauhaus, editorial, luxury, modern).
- `workshop-program.html` / `.pdf`: workshop programme.
- `vasco-pereira-mockup.pdf`: full-site mockup export.
- `Photos/`: images, organised by section (`about`, `hero`, `kids`, `workshop`).

## Local preview
`python3 serve.py` serves the repo on http://127.0.0.1:3456.
