#!/usr/bin/env python3
"""Build index.html (GitHub Pages) from pregnancy-tracker.html (the artifact source).

The artifact file has no <html>/<head>/<body>; this wraps it in a full document
with the icon, manifest and theme-color tags. Run from the repo root:
    python3 tools/build_index.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAD = '<!doctype html>\n<html lang="ar" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="description" content="متتبع حمل باللغة العربية: عمر الحمل، موعد الولادة، الأسابيع والأشهر، التقويم، المواعيد والقوائم.">\n<meta name="theme-color" content="#F3F6F2" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0F1411" media="(prefers-color-scheme: dark)">\n<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">\n<link rel="icon" href="icons/favicon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n<link rel="manifest" href="manifest.webmanifest">\n<meta name="apple-mobile-web-app-title" content="مسار الحمل">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'

src = (ROOT / "pregnancy-tracker.html").read_text(encoding="utf-8")
split = src.index('<svg width="0"')
head_part = src[:split].replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
html = HEAD + head_part + "</head>\n<body>\n" + src[split:] + "\n</body>\n</html>\n"
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html written")
