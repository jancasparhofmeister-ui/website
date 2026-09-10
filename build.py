#!/usr/bin/env python3
"""Baut aus body.html (Vorlage mit Bildplatzhaltern) die fertige index.html.

Aufruf:  python3 build.py
Bilder:  img/portrait_a.jpg, img/portrait_b.jpg
"""
import base64, pathlib, sys

here = pathlib.Path(__file__).parent
tpl = (here / 'body.html').read_text(encoding='utf-8')

def uri(name):
    p = here / 'img' / name
    if not p.exists():
        sys.exit('Bild fehlt: %s' % p)
    return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()

body = tpl.replace('@@PORTRAIT_A@@', uri('portrait_a.jpg')) \
          .replace('@@PORTRAIT_B@@', uri('portrait_b.jpg'))

marker = '</style>'
i = body.index(marker) + len(marker)
head, rest = body[:i], body[i:]

(here / 'index.html').write_text(
    '<!doctype html>\n<html lang="de">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<meta name="description" content="Jan Caspar Hofmeister, B.Sc. Wirtschaftswissenschaft (FU Berlin). '
    'Schwerpunkte Controlling, Finance und Recht.">\n'
    '<meta name="theme-color" content="#FBFBFA">\n'
    + head + '</head>\n<body>\n' + rest + '\n</body>\n</html>\n',
    encoding='utf-8')

print('geschrieben: index.html (%d KB)' % ((here / 'index.html').stat().st_size // 1024))
