#!/usr/bin/env python3
"""Cria um novo artigo em content/ já com o cabeçalho preenchido.

Uso:  python3 scripts/novo-artigo.py "Título do guia" [slug]
"""
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
ICONES = "hub, chip, mesh, thread, apple, camera, server, rocket, help, wifi, book"


def slugify(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    titulo = sys.argv[1]
    slug = sys.argv[2] if len(sys.argv) > 2 else slugify(titulo)
    destino = CONTENT / f"{slug}.md"
    if destino.exists():
        sys.exit(f"Já existe: {destino}")
    proxima_ordem = len(list(CONTENT.glob("*.md"))) + 1
    destino.write_text(f"""---
title: {titulo}
slug: {slug}
description: Uma frase que explica o guia e aparece no card e no Google.
category: Guia
icon: book           # opções: {ICONES}
order: {proxima_ordem}
featured: false      # true coloca o card na home
reading: 8 min de leitura
date: {date.today().isoformat()}
tags: [Tag1, Tag2]
---

Parágrafo de abertura.

## Primeiro tópico

Conteúdo.

!!! dica "Dica"
    Texto do destaque. Use também `!!! nota` e `!!! atencao`.
""", encoding="utf-8")
    print(f"Criado: {destino}\nAgora rode:  python3 build.py")


if __name__ == "__main__":
    main()
