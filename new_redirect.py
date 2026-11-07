#!/usr/bin/env python3
"""Create a redirect page for GitHub Pages.

Usage:  python3 new_redirect.py <slug> <destination-url>
Example: python3 new_redirect.py dguide https://www.etsy.com/listing/4523705429/cervical-dilation-teaching-aid-1-10cm-3d

Writes <slug>/index.html next to this script. After publishing, the QR URL is
https://<github-user>.github.io/<slug>/   (plain https:// - no x-safari- prefix).
"""
import html, os, re, sys

if len(sys.argv) != 3 or not re.fullmatch(r"[a-z0-9-]+", sys.argv[1]) or not sys.argv[2].startswith("https://"):
    sys.exit(__doc__)
slug, url = sys.argv[1], sys.argv[2]
u = html.escape(url, quote=True)
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Pete's Props</title>
<meta http-equiv="refresh" content="0; url={u}">
<script>location.replace("{u}");</script>
</head>
<body style="font-family:-apple-system,Helvetica,Arial,sans-serif;text-align:center;padding:3rem 1rem">
<p>Taking you to Pete's Props&hellip;</p>
<p><a href="{u}">Tap here if nothing happens</a></p>
</body>
</html>
"""
here = os.path.dirname(os.path.abspath(__file__))
folder = here if slug == "-" else os.path.join(here, slug)
os.makedirs(folder, exist_ok=True)
open(os.path.join(folder, "index.html"), "w").write(page)
print(f"Wrote {os.path.join(folder, 'index.html')}")
