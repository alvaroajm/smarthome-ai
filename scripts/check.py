#!/usr/bin/env python3
"""Verificação rápida do site gerado: placeholders, links internos e metadados."""
import re, sys, json
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"
problems = []
htmls = sorted(DIST.rglob("*.html"))

targets = {"/"} | {"/" + p.parent.relative_to(DIST).as_posix() + "/" for p in htmls if p.name == "index.html" and p.parent != DIST}

for f in htmls:
    html = f.read_text(encoding="utf-8")
    rel = "/" + f.relative_to(DIST).as_posix()
    # blocos de código podem conter templates Jinja legítimos ({{ variavel }}) — ignore-os
    sem_codigo = re.sub(r"<pre.*?</pre>|<code.*?</code>", " ", html, flags=re.S)
    for ph in re.findall(r"\{\{\s*\w+\s*\}\}", sem_codigo):
        problems.append(f"{rel}: placeholder não substituído {ph}")
    if "<title>" not in html:
        problems.append(f"{rel}: sem <title>")
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    if t and ("&" in t.group(1) and "&amp;" not in t.group(1) and "&middot;" not in t.group(1)):
        pass
    for href in re.findall(r'href="(/[^"#?]*)"', html):
        if href.startswith("/static/") or href in ("/sitemap.xml", "/robots.txt"):
            if not (DIST / href.lstrip("/")).exists():
                problems.append(f"{rel}: arquivo ausente {href}")
        elif href.endswith(".html"):
            if not (DIST / href.lstrip("/")).exists():
                problems.append(f"{rel}: página ausente {href}")
        elif href not in targets:
            problems.append(f"{rel}: link interno quebrado {href}")

idx = json.loads((DIST / "search-index.json").read_text(encoding="utf-8"))
print(f"páginas HTML: {len(htmls)} | entradas no índice de busca: {len(idx)}")
print("títulos:")
for f in htmls:
    m = re.search(r"<title>(.*?)</title>", f.read_text(encoding="utf-8"), re.S)
    print("  -", m.group(1) if m else "??")

if problems:
    print("\n❌ PROBLEMAS:")
    for p in sorted(set(problems)):
        print("  ", p)
    sys.exit(1)
print("\n✅ Sem placeholders pendentes e todos os links internos válidos.")
