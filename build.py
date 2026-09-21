#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Gerador estático do site SmartHome-AI (https://smarthome-ai.com)

Lê os arquivos Markdown de content/, aplica os templates de templates/,
copia static/ e escreve o site pronto em dist/.

Uso:
    python3 build.py            # gera o site em dist/
    python3 build.py --clean    # apaga dist/ antes de gerar
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("Falta a dependência 'Markdown'. Rode:  pip3 install -r requirements.txt")

# --------------------------------------------------------------------------
# Configuração do site
# --------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

SITE = {
    "name": "SmartHome-AI",
    "tagline": "Inteligência para o seu lar",
    "url": "https://smarthome-ai.com",
    "description": (
        "Guias práticos e independentes de casa inteligente: Home Assistant, ESPHome, "
        "ESP32, Zigbee2MQTT, ZHA, Matter over Thread, Apple HomeKit, Scrypted, "
        "Raspberry Pi e mini-PCs."
    ),
    "author": "Dr. Álvaro Menezes",
    "lang": "pt-BR",
    "locale": "pt_BR",
    "og_image": "/static/img/logo-smarthome-ai.jpg",
    "github": "https://github.com/alvaroajm/smarthome-ai",
}

NAV = [
    ("Início", "/"),
    ("Artigos", "/artigos/"),
    ("Comece aqui", "/instalacao/"),
    ("FAQ", "/faq/"),
    ("Sobre", "/sobre/"),
]

# Ícones SVG (traço 1.5, currentColor) usados nos cards da home
ICONS = {
    "hub": '<path d="M12 3v4m0 10v4m9-9h-4M7 12H3m12.4-5.4-2.8 2.8m-5.2 5.2-2.8 2.8m10.8 0-2.8-2.8M8.6 8.6 5.8 5.8"/><circle cx="12" cy="12" r="3"/>',
    "chip": '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 3v4m4-4v4m-4 10v4m4-4v4M3 10h4m-4 4h4m10-4h4m-4 4h4"/>',
    "mesh": '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="17" r="2"/><circle cx="19" cy="17" r="2"/><path d="M12 7v6m-1.6 1.2L6.6 16M13.6 14.2 17.4 16"/><circle cx="12" cy="14" r="2"/>',
    "thread": '<path d="M12 21a9 9 0 1 0-9-9"/><path d="M12 17a5 5 0 1 0-5-5"/><circle cx="12" cy="12" r="1.5"/>',
    "apple": '<path d="M16.5 13.2c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.9-1.5-.1-2.8.8-3.6.8-.7 0-1.9-.8-3.1-.8-1.6 0-3.1.9-3.9 2.4-1.6 2.9-.4 7.2 1.2 9.5.8 1.2 1.7 2.4 2.9 2.4 1.2 0 1.6-.8 3-.8s1.8.8 3 .7c1.2 0 2-1.2 2.8-2.4.6-.9.9-1.7 1.2-2.6-2.7-1-3.1-4.5-3.1-3.8Z"/><path d="M14.3 5.9c.6-.8 1-1.9.9-3-.9 0-2 .6-2.7 1.4-.6.7-1.1 1.8-.9 2.9 1 .1 2-.5 2.7-1.3Z"/>',
    "camera": '<path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h2L9 4h6l1.5 2h2A2.5 2.5 0 0 1 21 8.5v9A2.5 2.5 0 0 1 18.5 20h-13A2.5 2.5 0 0 1 3 17.5Z"/><circle cx="12" cy="13" r="3.5"/>',
    "server": '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    "rocket": '<path d="M5 15c-1 2-1 4-1 4s2 0 4-1"/><path d="M13.5 4.5C16 2 21 3 21 3s1 5-1.5 7.5L14 16l-6-6 5.5-5.5Z"/><circle cx="15.5" cy="8.5" r="1.5"/><path d="m8 10-4 1 1 4 4-1"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.3 2.4c-.6.2-.8.7-.8 1.3v.3"/><path d="M12 17h.01"/>',
    "wifi": '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5.5 5.5 0 0 1 7 0"/><path d="M12 19.5h.01"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M6 17h13"/>',
}

MD_EXTENSIONS = [
    "extra",          # tabelas, listas de definição, atributos, fenced code
    "toc",
    "sane_lists",
    "admonition",
    "attr_list",
]
MD_CONFIG = {"toc": {"permalink": "#", "toc_depth": "2-3", "baselevel": 2}}


# --------------------------------------------------------------------------
# Utilitários
# --------------------------------------------------------------------------
def log(msg: str) -> None:
    print(f"  {msg}")


def parse_front_matter(raw: str) -> tuple[dict, str]:
    """Lê um bloco de metadados delimitado por --- no topo do arquivo."""
    meta: dict = {}
    body = raw
    if raw.lstrip().startswith("---"):
        raw = raw.lstrip()
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            block, body = parts[1], parts[2]
            for line in block.strip().splitlines():
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if ":" not in line:
                    continue
                key, _, value = line.partition(":")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if value.startswith("[") and value.endswith("]"):
                    meta[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
                elif value.lower() in ("true", "false"):
                    meta[key] = value.lower() == "true"
                else:
                    meta[key] = value
    return meta, body.lstrip("\n")


TPL_RE = re.compile(r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}")


def render(template: str, ctx: dict) -> str:
    """Substituição simples de {{chave}} — sem dependências externas."""
    return TPL_RE.sub(lambda m: str(ctx.get(m.group(1), "")), template)


def read_template(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def icon_svg(name: str, cls: str = "icon") -> str:
    path = ICONS.get(name, ICONS["book"])
    return (
        f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true">{path}</svg>'
    )


def strip_html(text: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def fmt_date(value: str) -> str:
    try:
        d = datetime.strptime(str(value), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return ""
    meses = ["jan", "fev", "mar", "abr", "mai", "jun",
             "jul", "ago", "set", "out", "nov", "dez"]
    return f"{d.day} {meses[d.month - 1]} {d.year}"


# --------------------------------------------------------------------------
# Leitura do conteúdo
# --------------------------------------------------------------------------
class Page:
    def __init__(self, path: Path):
        raw = path.read_text(encoding="utf-8")
        self.meta, body = parse_front_matter(raw)
        md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
        self.html = md.convert(body)
        self.toc = getattr(md, "toc", "")
        self.source = path
        self.slug = self.meta.get("slug", path.stem)
        self.title = self.meta.get("title", self.slug)
        self.description = self.meta.get("description", "")
        self.category = self.meta.get("category", "Guia")
        self.icon = self.meta.get("icon", "book")
        self.section = self.meta.get("section", "artigo")   # artigo | pagina
        self.featured = bool(self.meta.get("featured", False))
        self.order = int(self.meta.get("order", 99))
        self.date = self.meta.get("date", "")
        self.tags = self.meta.get("tags", []) or []
        self.reading = self.meta.get("reading", "")
        self.url = "/" if self.slug == "index" else f"/{self.slug}/"
        self.text = strip_html(self.html)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Page {self.slug}>"


def load_pages() -> list[Page]:
    pages = [Page(p) for p in sorted(CONTENT.glob("*.md"))]
    pages.sort(key=lambda p: (p.order, p.title))
    return pages


# --------------------------------------------------------------------------
# Componentes de HTML
# --------------------------------------------------------------------------
def nav_html(current: str) -> str:
    items = []
    for label, url in NAV:
        active = ' class="active" aria-current="page"' if url == current else ""
        items.append(f'<a href="{url}"{active}>{label}</a>')
    return "\n        ".join(items)


def card_html(page: Page) -> str:
    return f"""<a class="card" href="{page.url}">
        <span class="card-icon">{icon_svg(page.icon)}</span>
        <span class="card-tag">{page.category}</span>
        <h3>{page.title}</h3>
        <p>{page.description}</p>
        <span class="card-go">Ler o guia <span aria-hidden="true">→</span></span>
      </a>"""


def list_item_html(page: Page) -> str:
    meta = " · ".join(x for x in [page.category, page.reading] if x)
    return f"""<li class="post">
        <a href="{page.url}">
          <span class="post-icon">{icon_svg(page.icon)}</span>
          <span class="post-body">
            <span class="post-title">{page.title}</span>
            <span class="post-desc">{page.description}</span>
            <span class="post-meta">{meta}</span>
          </span>
        </a>
      </li>"""


def tags_html(tags: list[str]) -> str:
    if not tags:
        return ""
    return '<ul class="tags">' + "".join(f"<li>{t}</li>" for t in tags) + "</ul>"


# --------------------------------------------------------------------------
# Geração
# --------------------------------------------------------------------------
def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def base_context(page_title: str, description: str, url_path: str, **extra) -> dict:
    canonical = SITE["url"].rstrip("/") + url_path
    title = page_title if page_title == SITE["name"] else f"{page_title} · {SITE['name']}"
    ctx = {
        "site_name": SITE["name"],
        "tagline": SITE["tagline"],
        "lang": SITE["lang"],
        "locale": SITE["locale"],
        "title": title,
        "description": description or SITE["description"],
        "canonical": canonical,
        "og_image": SITE["url"] + SITE["og_image"],
        "nav": nav_html(url_path),
        "year": date.today().year,
        "author": SITE["author"],
        "github": SITE["github"],
        "site_url": SITE["url"],
        "body_class": "",
        "extra_head": "",
    }
    ctx.update(extra)
    return ctx


def build_home(pages: list[Page]) -> None:
    tpl_home = read_template("home.html")
    tpl_base = read_template("base.html")

    featured = [p for p in pages if p.featured]
    artigos = [p for p in pages if p.section == "artigo"]

    cards = "\n      ".join(card_html(p) for p in featured)
    recentes = "\n      ".join(list_item_html(p) for p in artigos[:6])

    body = render(tpl_home, {
        "cards": cards,
        "recentes": recentes,
        "tagline": SITE["tagline"],
        "total_guias": len(artigos),
        "icon_rocket": icon_svg("rocket", "icon icon-lg"),
        "icon_hub": icon_svg("hub", "icon icon-lg"),
        "icon_mesh": icon_svg("mesh", "icon icon-lg"),
    })
    ctx = base_context(SITE["name"], SITE["description"], "/", content=body,
                       body_class="home")
    write(DIST / "index.html", render(tpl_base, ctx))
    log("index.html")


def build_pages(pages: list[Page]) -> None:
    tpl_base = read_template("base.html")
    tpl_article = read_template("article.html")
    artigos = [p for p in pages if p.section == "artigo"]

    for page in pages:
        idx = artigos.index(page) if page in artigos else -1
        prev_html = next_html = ""
        if idx > 0:
            p = artigos[idx - 1]
            prev_html = f'<a class="pager-prev" href="{p.url}"><span>← Anterior</span><strong>{p.title}</strong></a>'
        if 0 <= idx < len(artigos) - 1:
            n = artigos[idx + 1]
            next_html = f'<a class="pager-next" href="{n.url}"><span>Próximo →</span><strong>{n.title}</strong></a>'

        toc_block = ""
        if page.toc and page.meta.get("toc", True) is not False and "<li>" in page.toc:
            toc_block = f'<nav class="toc" aria-label="Sumário"><p class="toc-title">Neste guia</p>{page.toc}</nav>'

        body = render(tpl_article, {
            "title": page.title,
            "description": page.description,
            "category": page.category,
            "icon": icon_svg(page.icon, "icon icon-lg"),
            "content": page.html,
            "toc": toc_block,
            "tags": tags_html(page.tags),
            "date": fmt_date(page.date),
            "reading": page.reading,
            "prev": prev_html,
            "next": next_html,
        })
        ctx = base_context(page.title, page.description, page.url, content=body,
                           body_class="article")
        out = DIST / "index.html" if page.url == "/" else DIST / page.slug / "index.html"
        write(out, render(tpl_base, ctx))
        log(f"{page.url}")


def build_index_artigos(pages: list[Page]) -> None:
    tpl_base = read_template("base.html")
    artigos = [p for p in pages if p.section == "artigo"]
    items = "\n      ".join(list_item_html(p) for p in artigos)
    body = f"""<article class="page">
    <header class="page-head">
      <p class="eyebrow">Biblioteca</p>
      <h1>Todos os guias</h1>
      <p class="lead">{len(artigos)} guias sobre plataformas, protocolos e hardware de casa inteligente — do primeiro sensor até a automação que ninguém percebe que existe.</p>
    </header>
    <ul class="post-list">
      {items}
    </ul>
  </article>"""
    ctx = base_context("Todos os guias", "Índice completo dos guias do SmartHome-AI.",
                       "/artigos/", content=body, body_class="listing")
    write(DIST / "artigos" / "index.html", render(tpl_base, ctx))
    log("/artigos/")


def build_404() -> None:
    tpl_base = read_template("base.html")
    body = """<article class="page page-404">
    <header class="page-head">
      <p class="eyebrow">Erro 404</p>
      <h1>Esta automação não existe (ainda)</h1>
      <p class="lead">A página que você procurou não foi encontrada. Que tal voltar ao início ou consultar a lista de guias?</p>
      <p class="cta-row">
        <a class="btn btn-primary" href="/">Voltar ao início</a>
        <a class="btn btn-ghost" href="/artigos/">Ver todos os guias</a>
      </p>
    </header>
  </article>"""
    ctx = base_context("Página não encontrada", "Página não encontrada.", "/404.html",
                       content=body, body_class="error")
    write(DIST / "404.html", render(tpl_base, ctx))
    log("404.html")


def build_search_index(pages: list[Page]) -> None:
    data = [
        {
            "t": p.title,
            "u": p.url,
            "d": p.description,
            "c": p.category,
            "x": p.text[:1200],
        }
        for p in pages
    ]
    write(DIST / "search-index.json", json.dumps(data, ensure_ascii=False))
    log("search-index.json")


def build_sitemap(pages: list[Page]) -> None:
    urls = ["/", "/artigos/"] + [p.url for p in pages if p.url != "/"]
    today = date.today().isoformat()
    entries = "\n".join(
        f"  <url><loc>{SITE['url']}{u}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>monthly</changefreq><priority>{'1.0' if u == '/' else '0.7'}</priority></url>"
        for u in dict.fromkeys(urls)
    )
    write(DIST / "sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          f"{entries}\n</urlset>\n")
    write(DIST / "robots.txt",
          f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    log("sitemap.xml + robots.txt")


def copy_static() -> None:
    if STATIC.exists():
        shutil.copytree(STATIC, DIST / "static", dirs_exist_ok=True)
        log("static/")
    for extra in ("_headers", "_redirects"):
        src = ROOT / extra
        if src.exists():
            shutil.copy2(src, DIST / extra)
            log(extra)


def main() -> None:
    if "--clean" in sys.argv and DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    print(f"\n🏠  Gerando {SITE['name']} → {DIST.relative_to(ROOT)}/\n")
    pages = load_pages()
    if not pages:
        sys.exit("Nenhum arquivo .md encontrado em content/.")

    build_pages(pages)
    build_home(pages)
    build_index_artigos(pages)
    build_404()
    build_search_index(pages)
    build_sitemap(pages)
    copy_static()

    files = sum(1 for _ in DIST.rglob("*") if _.is_file())
    print(f"\n✅  {len(pages)} páginas de conteúdo · {files} arquivos em dist/\n")
    print("    Pré-visualize com:  python3 serve.py\n")


if __name__ == "__main__":
    main()
