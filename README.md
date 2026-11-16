# reubs.link

Personal site for Reubs (@reubs_btc).

- `public/` — the site (served by Netlify)
- `netlify/functions/posts.mjs` — live X posts via the Typefully API (`/api/posts`)
- `netlify/functions/youtube.mjs` — latest Stacked Up video via YouTube RSS (`/api/youtube`)
- `tools/build_pages.py` — regenerates the Stacks / Tenero / Stacked Up / LEO / Contact pages

## Netlify settings
- Build command: none · Publish directory: `public` (both set in `netlify.toml`)
- Environment variable: `TYPEFULLY_API_KEY` (Typefully → Settings → API)

Accounts pulled live: reubs_btc, tenero_io, LeoCoinSTX, StackedUpStream (once connected in Typefully).
