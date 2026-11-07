# Redirects — QR links that avoid the Etsy App Clip problem

Each chip's QR points to a plain `https://<github-user>.github.io/<slug>/` page that forwards to the Etsy listing. Works on iPhone and (presumably) Android; no `x-safari-https://` prefix. Untested until the first chip is scanned.

## One-time setup (Pete, GitHub)
1. Create a **public** repo named exactly `<github-user>.github.io`.
2. Upload the contents of this folder (`index.html`, `dguide/`, `new_redirect.py`, this README) to the repo root.
3. Repo Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`. Wait a minute or two.
4. Open `https://<github-user>.github.io/dguide/` in a browser and on an iPhone; it should land on the D-Guide Etsy listing.

## Add a product
`python3 new_redirect.py <slug> <https-destination-url>` then upload the new `<slug>/index.html`.

## Notes
- Changing a destination later = edit that `index.html`; printed chips keep working.
- Shorter URL = less dense QR (better for the 0.2 mm nozzle). Keep slugs short.
- The page sets `noindex`, so search engines ignore it.
