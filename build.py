#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Gerador estático bilíngue (pt-BR / en) do SmartHome-AI

Lê content/*.md (português) e content/en/*.md (inglês), aplica os templates
de templates/, copia static/ e escreve o site pronto em dist/.

    python3 build.py            # gera o site em dist/
    python3 build.py --clean    # apaga dist/ antes de gerar
"""
from __future__ import annotations

from beginner_content import beginner_home
from visual_content import home_visual_context
from brand_icons import decorate_project_links, icons_for_link, project_icons

import hashlib
import html as html_lib
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

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

SITE = {
    "name": "SmartHome-AI",
    "url": "https://smarthome-ai.com",
    "author": "Dr. Álvaro Menezes",
    "og_image": "/static/img/og-smarthome-ai.jpg",
}

# --------------------------------------------------------------------------
# Contato e ecossistema
# --------------------------------------------------------------------------
CONTACT = {
    "name": "Dr. Álvaro Menezes",
    "credentials": "CRM 11.393/CE · RQE 6562",
    "photo": "/static/img/author-original.jpg",
    "email": "admin@alvaro-menezes.com",
    "card": "https://alvaro-menezes.com/",
}

SOCIAL = [
    ("GitHub", "https://github.com/alvaroajm", "github"),
    ("Instagram", "https://www.instagram.com/alvaroajm/", "instagram"),
    ("Facebook", "https://facebook.com/alvaroajm", "facebook"),
    ("X", "https://x.com/alvaromenezesMD", "x"),
    ("LinkedIn", "https://www.linkedin.com/in/dr-alvaro-menezes/", "linkedin"),
]

PLACES = [
    ("Instituto Doutor José Frota", "Rua Barão do Rio Branco, 1816 · Centro, Fortaleza/CE"),
    ("Hospital Universitário Walter Cantídio", "Rua Pastor Samuel Munguba, 1290 · Rodolfo Teófilo, Fortaleza/CE"),
    ("Clínica Boghos Boyadjian", "Av. Rui Barbosa, 1975 · Aldeota, Fortaleza/CE"),
]

ECOSYSTEM = [
    {
        "name": "SmartHome-AI",
        "url": "https://smarthome-ai.com",
        "img": "/static/img/logo-smarthome-ai-marca.png",
        "pt": "Casa inteligente, automação local e código aberto",
        "en": "Smart home, local automation and open source",
    },
    {
        "name": "Dr. Álvaro Menezes",
        "url": "https://alvaro-menezes.com",
        "img": "/static/img/author-seal.jpg",
        "pt": "Radiologia geral e musculoesquelética · Fortaleza/CE",
        "en": "General and musculoskeletal radiology · Fortaleza, Brazil",
    },
    {
        "name": "RadApps",
        "url": "https://radapps.app",
        "img": "/static/img/radapps-brand.jpg",
        "pt": "Aplicativos para radiologistas · iOS e Android",
        "en": "Apps for radiologists · iOS and Android",
    },
]

# Ícones de marca — Simple Icons (CC0)
BRAND_ICONS = {
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
    "instagram": "M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077",
    "facebook": "M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z",
    "x": "M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z",
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
}

# Ícones de linha usados nos cards de conteúdo
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
    "message": '<path d="M20 4H4a1.5 1.5 0 0 0-1.5 1.5v9A1.5 1.5 0 0 0 4 16h4l4 4 4-4h4a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 20 4Z"/><path d="M7 8h10M7 11.5h6"/>',
    "cloud": '<path d="M7.5 19h10a4 4 0 0 0 .6-7.95 6 6 0 0 0-11.6-1.4A3.8 3.8 0 0 0 7.5 19Z"/><path d="M12 15.5V9.5m0 0-2.2 2.2M12 9.5l2.2 2.2"/>',
    "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
    "bot": '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 8V5M9.5 13h.01M14.5 13h.01M9.5 16h5"/><circle cx="12" cy="3.8" r="1.3"/>',
    "key": '<circle cx="8" cy="12" r="4"/><path d="M12 12h9m-3 0v3m-2.5-3v2"/>',
    "terminal": '<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="m7.5 10 2.8 2.4-2.8 2.4M13.2 15h3.5"/>',
    "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2Z"/><path d="M6 17h13"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
    "pin": '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
    "card": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 10h18M7 14.5h4"/>',
}

MD_EXTENSIONS = ["extra", "toc", "sane_lists", "admonition", "attr_list"]
MD_CONFIG = {"toc": {"permalink": "#", "toc_depth": "2-3", "baselevel": 1}}

# --------------------------------------------------------------------------
# Idiomas
# --------------------------------------------------------------------------
LANGS = {
    "pt": {
        "code": "pt",
        "html_lang": "pt-BR",
        "locale": "pt_BR",
        "intl": "pt-BR",
        "prefix": "",
        "dir": CONTENT,
        "home_tpl": "home.pt.html",
        "tagline": "Inteligência para o seu lar",
        "description": (
            "Casa inteligente para iniciantes: entenda as plataformas, instale o Home Assistant OS "
            "e conecte luzes e sensores com Zigbee, ZBT-2 e ZHA. Passo a passo pelas telas."
        ),
        "nav": [
            ("Início", ""),
            ("Guias", "artigos/"),
            ("Dispositivos", "#dispositivos"),
            ("Links úteis", "#recursos"),
            ("Comece aqui", "instalacao/"),
            ("Sobre", "sobre/"),
        ],
        "ui": {
            "skip": "Pular para o conteúdo",
            "close": "Fechar busca",
            "search": "Buscar no site",
            "search_ph": "Buscar: luz, Zigbee, instalação…",
            "search_empty": "Digite para buscar nos guias.",
            "search_none": "Nada encontrado. Tente “zigbee”, “ZHA” ou “matter”.",
            "theme": "Alternar tema claro/escuro",
            "menu": "Abrir menu",
            "nav_label": "Navegação principal",
            "toc": "Neste guia",
            "prev": "← Anterior",
            "next": "Próximo →",
            "listing_eyebrow": "Biblioteca",
            "listing_title": "Todos os guias",
            "listing_lead": "Siga a trilha básica. Os demais assuntos ficam no aprofundamento, ao final.",
            "all_guides": "Ver todos os guias →",
            "pt_badge": "em português",
            "e404_eyebrow": "Erro 404",
            "e404_title": "Esta automação não existe (ainda)",
            "e404_lead": "A página que você procurou não foi encontrada. Que tal voltar ao início ou consultar a lista de guias?",
            "e404_home": "Voltar ao início",
            "e404_list": "Ver todos os guias",
            "f_platforms": "Primeiros passos",
            "f_protocols": "Conectar e automatizar",
            "f_ai": "Depois do básico",
            "f_site": "Site",
            "f_ecosystem": "Ecossistema",
            "f_contact": "Contato",
            "f_follow": "Redes",
            "f_places": "Locais de atendimento",
            "f_card": "Cartão de contato",
            "f_about_site": "Guias independentes de casa inteligente, automação local e código aberto.",
            "f_made": "Feito com HTML, CSS, JavaScript e um gerador estático em Python.",
            "f_by": "conteúdo por",
            "lang_label": "Idioma",
            "to_top": "Voltar ao topo",
            "search_suggest": "Guias populares",
            "breadcrumb_home": "Início",
            "related": "Continue por aqui",
            "clock_label": "Data e hora em Fortaleza",
        },
    },
    "en": {
        "code": "en",
        "html_lang": "en",
        "locale": "en_US",
        "intl": "en-US",
        "prefix": "en/",
        "dir": CONTENT / "en",
        "home_tpl": "home.en.html",
        "tagline": "Intelligence for your home",
        "description": (
            "Smart homes for beginners: compare platforms, set up Home Assistant OS "
            "and connect lights and sensors with Zigbee, ZBT-2 and ZHA. Visual steps, no code."
        ),
        "nav": [
            ("Home", ""),
            ("Guides", "guides/"),
            ("Devices", "#dispositivos"),
            ("Resources", "#recursos"),
            ("Start here", "start/"),
            ("FAQ", "faq/"),
            ("About", "about/"),
        ],
        "ui": {
            "skip": "Skip to content",
            "close": "Close search",
            "search": "Search the site",
            "search_ph": "Search: light, Zigbee, installation…",
            "search_empty": "Type to search the guides.",
            "search_none": "Nothing found. Try “zigbee”, “ZHA” or “matter”.",
            "theme": "Toggle light/dark theme",
            "menu": "Open menu",
            "nav_label": "Main navigation",
            "toc": "In this guide",
            "prev": "← Previous",
            "next": "Next →",
            "listing_eyebrow": "Library",
            "listing_title": "All guides",
            "listing_lead": "Follow the beginner path. Additional topics are in further learning, at the end.",
            "all_guides": "See all guides →",
            "pt_badge": "in Portuguese",
            "e404_eyebrow": "Error 404",
            "e404_title": "This automation doesn't exist (yet)",
            "e404_lead": "The page you asked for was not found. Head back home or browse the guides.",
            "e404_home": "Back home",
            "e404_list": "See all guides",
            "f_platforms": "First steps",
            "f_protocols": "Connect and automate",
            "f_ai": "After the basics",
            "f_site": "Site",
            "f_ecosystem": "Ecosystem",
            "f_contact": "Contact",
            "f_follow": "Social",
            "f_places": "Practice locations",
            "f_card": "Contact card",
            "f_about_site": "Independent guides on smart homes, local automation and open source.",
            "f_made": "Built with HTML, CSS, JavaScript and a static site generator in Python.",
            "f_by": "written by",
            "lang_label": "Language",
            "to_top": "Back to top",
            "search_suggest": "Popular guides",
            "breadcrumb_home": "Home",
            "related": "Read next",
            "clock_label": "Date and time in Fortaleza",
        },
    },
}

FOOTER_LINKS = {
    "pt": {
        "f_platforms": [("O que é casa inteligente?", "/casa-inteligente/"), ("Home Assistant", "/home-assistant/"), ("Instalar o HAOS", "/instalar-haos/")],
        "f_protocols": [("Entender Zigbee", "/zigbee/"), ("ZBT-2 com ZHA", "/zbt-dongles/"), ("Primeira automação", "/primeira-automacao/")],
        "f_ai": [("Integrações e Apps", "/apps-integracoes/"), ("Aprofundamento", "/aprofundamento/")],
        "f_site": [("Todos os guias", "/artigos/"), ("Dúvidas frequentes", "/faq/"), ("Sobre", "/sobre/")],
    },
    "en": {
        "f_platforms": [("Start here", "/en/start/"), ("Home Assistant (PT)", "/home-assistant/"), ("Install HAOS (PT)", "/instalar-haos/")],
        "f_protocols": [("Zigbee (PT)", "/zigbee/"), ("ZBT-2 with ZHA (PT)", "/zbt-dongles/"), ("First automation (PT)", "/primeira-automacao/")],
        "f_ai": [("Integrations and Apps (PT)", "/apps-integracoes/"), ("Further learning (PT)", "/aprofundamento/")],
        "f_site": [("All guides", "/en/guides/"), ("FAQ", "/en/faq/"), ("About", "/en/about/")],
    },
}


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------
def log(msg: str) -> None:
    print(f"  {msg}")


def parse_front_matter(raw: str) -> tuple[dict, str]:
    meta: dict = {}
    body = raw
    if raw.lstrip().startswith("---"):
        raw = raw.lstrip()
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            block, body = parts[1], parts[2]
            for line in block.strip().splitlines():
                if not line.strip() or line.strip().startswith("#") or ":" not in line:
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
    return TPL_RE.sub(lambda m: str(ctx.get(m.group(1), "")), template)


def read_template(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def icon_svg(name: str, cls: str = "icon") -> str:
    path = ICONS.get(name, ICONS["book"])
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{path}</svg>')


def brand_svg(name: str) -> str:
    if name == "github":
        return project_icons("github")
    return (f'<svg class="icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            f'<path d="{BRAND_ICONS[name]}"/></svg>')


EXT_RE = re.compile(r'<a href="(https?://(?!(?:www\.)?smarthome-ai\.com)[^"]+)"')


def mark_external_links(html: str) -> str:
    """Links para fora do site abrem em nova aba e ganham um indicador visual."""
    return EXT_RE.sub(lambda m: f'<a class="ext" target="_blank" rel="noopener" href="{m.group(1)}"', html)


def strip_html(text: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def esc(text: str) -> str:
    return html_lib.escape(text or "", quote=True)


def asset_url(rel: str) -> str:
    """URL do arquivo estático com hash de conteúdo — invalida o cache do navegador."""
    f = STATIC / rel
    if not f.exists():
        return "/static/" + rel
    digest = hashlib.md5(f.read_bytes()).hexdigest()[:8]
    return f"/static/{rel}?v={digest}"


# --------------------------------------------------------------------------
# Conteúdo
# --------------------------------------------------------------------------
class Page:
    def __init__(self, path: Path, lang: str):
        raw = path.read_text(encoding="utf-8")
        self.meta, body = parse_front_matter(raw)
        md = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
        self.html = md.convert(body)
        self.toc = getattr(md, "toc", "")
        self.lang = lang
        self.source = path
        self.slug = self.meta.get("slug", path.stem)
        self.key = self.meta.get("key", self.slug)
        self.title = self.meta.get("title", self.slug)
        self.description = self.meta.get("description", "")
        self.category = self.meta.get("category", "Guia")
        self.icon = self.meta.get("icon", "book")
        self.section = self.meta.get("section", "artigo")
        self.featured = bool(self.meta.get("featured", False))
        self.level = self.meta.get("level", "avancado")
        self.order = int(self.meta.get("order", 99))
        self.date = self.meta.get("date", "")
        self.tags = self.meta.get("tags", []) or []
        self.reading = self.meta.get("reading", "")
        self.url = "/" + LANGS[lang]["prefix"] + self.slug + "/"
        self.html = mark_external_links(self.html)
        self.text = strip_html(self.html)


def load_pages(lang: str) -> list[Page]:
    folder = LANGS[lang]["dir"]
    if not folder.exists():
        return []
    files = sorted(p for p in folder.glob("*.md"))
    pages = [Page(p, lang) for p in files]
    pages.sort(key=lambda p: (p.order, p.title))
    return pages


# --------------------------------------------------------------------------
# Componentes
# --------------------------------------------------------------------------
def nav_html(lang: str, current: str) -> str:
    prefix = "/" + LANGS[lang]["prefix"]
    items = []
    for label, path in LANGS[lang]["nav"]:
        url = prefix + path
        active = ' class="active" aria-current="page"' if url == current else ""
        items.append(f'<a href="{url}"{active}>{label}</a>')
    return "\n        ".join(items)


def card_html(page: Page, ui: dict, foreign: bool = False) -> str:
    badge = f'<span class="badge-lang">{ui["pt_badge"]}</span>' if foreign else ""
    return f"""<a class="card" href="{page.url}">
        <span class="card-icon">{icons_for_link(page.url) or icon_svg(page.icon)}</span>
        <span class="card-tag">{esc(page.category)}{badge}</span>
        <h3>{esc(page.title)}</h3>
        <p>{esc(page.description)}</p>
        <span class="card-go">{'Read the guide' if foreign or page.lang == 'en' else 'Ler o guia'} <span aria-hidden="true">→</span></span>
      </a>"""


def list_item_html(page: Page, ui: dict, foreign: bool = False) -> str:
    meta = " · ".join(x for x in [esc(page.category), esc(page.reading)] if x)
    badge = f'<span class="badge-lang">{ui["pt_badge"]}</span>' if foreign else ""
    return f"""<li class="post">
        <a href="{page.url}">
          <span class="post-icon">{icons_for_link(page.url) or icon_svg(page.icon)}</span>
          <span class="post-body">
            <span class="post-title">{esc(page.title)}{badge}</span>
            <span class="post-desc">{esc(page.description)}</span>
            <span class="post-meta">{meta}</span>
          </span>
        </a>
      </li>"""


def tags_html(tags: list[str]) -> str:
    if not tags:
        return ""
    return '<ul class="tags">' + "".join(f"<li>{esc(t)}</li>" for t in tags) + "</ul>"


def topbar_html(lang: str, alt_url: str) -> str:
    ui = LANGS[lang]["ui"]
    other = "en" if lang == "pt" else "pt"
    pt_url = alt_url if lang == "en" else "#"
    en_url = alt_url if lang == "pt" else "#"
    def lang_link(code: str, label: str, url: str) -> str:
        if code == lang:
            return f'<span class="lang-current" aria-current="true">{label}</span>'
        return f'<a href="{url}" hreflang="{code}" lang="{code}">{label}</a>'
    return f"""<div class="topbar">
    <div class="wrap topbar-inner">
      <p class="clock" id="clock" data-intl="{LANGS[lang]['intl']}" aria-label="{ui['clock_label']}">&nbsp;</p>
      <div class="topbar-actions">
        <div class="lang-switch" role="group" aria-label="{ui['lang_label']}">
          {lang_link('pt', 'PT', pt_url)}
          <span aria-hidden="true">·</span>
          {lang_link('en', 'EN', en_url)}
        </div>
        <button class="icon-btn" id="theme-toggle" aria-label="{ui['theme']}" title="{ui['theme']}">
          <svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a6.8 6.8 0 0 0 10.5 10.5Z"/></svg>
          <svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 3v2m0 14v2M3 12h2m14 0h2M5.6 5.6l1.4 1.4m10 10 1.4 1.4m0-12.8-1.4 1.4m-10 10-1.4 1.4"/></svg>
        </button>
      </div>
    </div>
  </div>"""


def header_html(lang: str, current: str) -> str:
    ui = LANGS[lang]["ui"]
    home = "/" + LANGS[lang]["prefix"]
    return f"""<header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{home}" aria-label="{SITE['name']}">
        <img class="brand-mark" src="/static/img/logo-smarthome-ai-marca.png" width="44" height="44" alt="" loading="eager">
        <span class="brand-text">
          <strong>SmartHome<span class="accent">-AI</span></strong>
          <small>{LANGS[lang]['tagline']}</small>
        </span>
      </a>
      <nav class="site-nav" id="menu" aria-label="{ui['nav_label']}">
        {nav_html(lang, current)}
      </nav>
      <div class="header-actions">
        <button class="icon-btn" id="search-open" aria-label="{ui['search']}" title="{ui['search']} (/)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        </button>
        <button class="icon-btn menu-btn" id="menu-btn" aria-label="{ui['menu']}" aria-expanded="false" aria-controls="menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
    </div>
  </header>"""


def ecosystem_html(lang: str) -> str:
    tiles = []
    for item in ECOSYSTEM:
        current = item["url"].startswith(SITE["url"])
        rel = "" if current else ' target="_blank" rel="noopener"'
        href = ("/" + LANGS[lang]["prefix"]) if current else item["url"]
        tiles.append(f"""<a class="eco-tile" href="{href}"{rel}>
          <span class="eco-logo"><img src="{item['img']}" alt="{esc(item['name'])}" width="56" height="56" loading="lazy"></span>
          <span class="eco-text"><strong>{esc(item['name'])}</strong><small>{esc(item[lang])}</small></span>
        </a>""")
    return "\n        ".join(tiles)


def footer_html(lang: str) -> str:
    ui = LANGS[lang]["ui"]
    links = FOOTER_LINKS[lang]
    cols = []
    for key in ("f_platforms", "f_protocols", "f_ai", "f_site"):
        items = "".join(f'<a href="{u}">{esc(t)}</a>' for t, u in links[key])
        cols.append(f'<div><h4>{ui[key]}</h4>{items}</div>')
    social = "".join(
        f'<a class="social" href="{url}" target="_blank" rel="noopener me" aria-label="{name}" title="{name}">{brand_svg(key)}</a>'
        for name, url, key in SOCIAL
    )
    places = "".join(f'<li><strong>{esc(n)}</strong><span>{esc(a)}</span></li>' for n, a in PLACES)
    return f"""<footer class="site-footer">
    <section class="wrap eco">
      <h2 class="eco-title">{ui['f_ecosystem']}</h2>
      <div class="eco-grid">
        {ecosystem_html(lang)}
      </div>
    </section>

    <section class="wrap contact-card" id="contato">
      <div class="contact-person">
        <img class="contact-photo" src="{CONTACT['photo']}" width="96" height="96" alt="{esc(CONTACT['name'])}" loading="lazy">
        <div>
          <p class="contact-name">{esc(CONTACT['name'])}</p>
          <p class="contact-cred">{esc(CONTACT['credentials'])}</p>
          <p class="contact-cred">{ui['f_about_site']}</p>
          <div class="contact-social">{social}</div>
        </div>
      </div>
      <div class="contact-actions">
        <h4>{ui['f_contact']}</h4>
        <a class="contact-line" href="mailto:{CONTACT['email']}">{icon_svg('mail')}<span>{esc(CONTACT['email'])}</span></a>
        <a class="contact-line" href="{CONTACT['card']}" target="_blank" rel="noopener">{icon_svg('card')}<span>{ui['f_card']}</span></a>
      </div>
      <div class="contact-places">
        <h4>{ui['f_places']}</h4>
        <ul>{places}</ul>
      </div>
    </section>

    <div class="wrap footer-inner">
      <div class="footer-brand">
        <strong>SmartHome<span class="accent">-AI</span></strong>
        <p>{LANGS[lang]['tagline']} — {ui['f_about_site']}</p>
      </div>
      <nav class="footer-nav" aria-label="{ui['f_site']}">
        {''.join(cols)}
      </nav>
    </div>
    <div class="wrap footer-bottom">
      <p>© {date.today().year} {SITE['name']} · {ui['f_by']} {esc(SITE['author'])}</p>
      <p>{ui['f_made']}</p>
    </div>
  </footer>"""


# --------------------------------------------------------------------------
# Montagem das páginas
# --------------------------------------------------------------------------
AUTOR_LD = {
    "@type": "Person",
    "name": "Dr. Álvaro Menezes",
    "url": "https://alvaro-menezes.com",
    "jobTitle": "Radiologista",
    "sameAs": [u for _, u, _ in SOCIAL],
}

EDITOR_LD = {
    "@type": "Organization",
    "name": SITE["name"],
    "url": SITE["url"],
    "logo": {"@type": "ImageObject", "url": SITE["url"] + "/static/img/logo-smarthome-ai-marca.png",
             "width": 360, "height": 360},
}


def jsonld(data) -> str:
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def site_ld(lang: str) -> dict:
    cfg = LANGS[lang]
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE["name"],
        "alternateName": f"{SITE['name']} — {cfg['tagline']}",
        "url": SITE["url"] + "/" + cfg["prefix"],
        "inLanguage": cfg["html_lang"],
        "description": cfg["description"],
        "publisher": EDITOR_LD,
    }


def breadcrumb_ld(lang: str, page) -> dict:
    ui = LANGS[lang]["ui"]
    home = SITE["url"] + "/" + LANGS[lang]["prefix"]
    listing = home + ("artigos/" if lang == "pt" else "guides/")
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["breadcrumb_home"], "item": home},
            {"@type": "ListItem", "position": 2, "name": ui["listing_title"], "item": listing},
            {"@type": "ListItem", "position": 3, "name": page.title, "item": SITE["url"] + page.url},
        ],
    }


def article_ld(lang: str, page) -> dict:
    data = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": page.title[:110],
        "description": page.description,
        "inLanguage": LANGS[lang]["html_lang"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE["url"] + page.url},
        "author": AUTOR_LD,
        "publisher": EDITOR_LD,
        "image": SITE["url"] + SITE["og_image"],
        "isAccessibleForFree": True,
    }
    if page.date:
        data["datePublished"] = str(page.date)
        data["dateModified"] = str(page.date)
    if page.tags:
        data["keywords"] = ", ".join(page.tags)
    if page.category:
        data["articleSection"] = page.category
    return data


# com baselevel=2 no Markdown, os "##" do texto viram <h3>
FAQ_RE = re.compile(r'<h3 id="[^"]*">(.*?)</h3>(.*?)(?=<h3 |\Z)', re.S)


def faq_ld(page) -> dict | None:
    itens = []
    for pergunta, resposta in FAQ_RE.findall(page.html):
        q = strip_html(pergunta).replace("¶", "").rstrip(" #").strip()
        a = strip_html(resposta).replace("¶", "").strip()
        if not q or not a or "?" not in q:
            continue
        itens.append({"@type": "Question", "name": q,
                      "acceptedAnswer": {"@type": "Answer", "text": a[:800]}})
    if len(itens) < 2:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": itens}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".html":
        content = decorate_project_links(content)
    path.write_text(content, encoding="utf-8")


def out_path(url: str) -> Path:
    if url == "/":
        return DIST / "index.html"
    return DIST / url.strip("/") / "index.html"


def hreflang_html(alts: dict) -> str:
    tags = [f'<link rel="alternate" hreflang="{code}" href="{SITE["url"]}{url}">'
            for code, url in alts.items()]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE["url"]}{alts.get("pt", "/")}">')
    return "\n  ".join(tags)


def base_context(lang: str, page_title: str, description: str, url_path: str,
                 alts: dict, content: str, body_class: str = "", extra_head: str = "") -> dict:
    cfg = LANGS[lang]
    ui = cfg["ui"]
    other = "en" if lang == "pt" else "pt"
    alt_url = alts.get(other, "/" + LANGS[other]["prefix"])
    title = page_title if page_title == SITE["name"] else f"{page_title} · {SITE['name']}"
    return {
        "site_name": SITE["name"],
        "lang": cfg["html_lang"],
        "locale": cfg["locale"],
        "lang_code": lang,
        "intl": cfg["intl"],
        "title": esc(title),
        "description": esc(description or cfg["description"]),
        "canonical": SITE["url"] + url_path,
        "og_image": SITE["url"] + SITE["og_image"],
        "alternates": hreflang_html(alts),
        "topbar": topbar_html(lang, alt_url),
        "header": header_html(lang, url_path),
        "footer": footer_html(lang),
        "content": content,
        "body_class": body_class,
        "author": esc(SITE["author"]),
        "search_index": "/" + cfg["prefix"] + "search-index.json",
        "css_url": asset_url("css/style.css"),
        "js_url": asset_url("js/main.js"),
        "favicon_url": asset_url("img/favicon-sa-32.png"),
        "favicon_large_url": asset_url("img/favicon-sa-192.png"),
        "favicon_ico_url": asset_url("img/favicon-sa.ico"),
        "apple_icon_url": asset_url("img/apple-touch-icon-sa.png"),
        "ui_skip": ui["skip"],
        "ui_close": ui["close"],
        "ui_search": ui["search"],
        "ui_search_ph": ui["search_ph"],
        "ui_search_empty": ui["search_empty"],
        "ui_search_none": ui["search_none"],
        "ui_search_suggest": ui["search_suggest"],
        "ui_to_top": ui["to_top"],
        "extra_head": jsonld(site_ld(lang)) + extra_head,
        "tagline_meta": esc(cfg["tagline"]),
        "robots": "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
    }


def breadcrumbs_html(lang: str, page: Page) -> str:
    ui = LANGS[lang]["ui"]
    home = "/" + LANGS[lang]["prefix"]
    listing = home + ("artigos/" if lang == "pt" else "guides/")
    return (f'<nav class="crumbs" aria-label="breadcrumb"><ol>'
            f'<li><a href="{home}">{ui["breadcrumb_home"]}</a></li>'
            f'<li><a href="{listing}">{ui["listing_title"]}</a></li>'
            f'<li aria-current="page">{esc(page.category)}</li>'
            f'</ol></nav>')


def related_html(lang: str, page: Page, pool: list[Page]) -> str:
    if page.level == "basico":
        return ""
    ui = LANGS[lang]["ui"]
    pool = [p for p in pool if p.level == page.level]
    same = [p for p in pool if p is not page and p.category == page.category]
    rest = [p for p in pool if p is not page and p not in same]
    picked = (same + rest)[:3]
    if not picked:
        return ""
    cards = "\n      ".join(card_html(p, ui, lang == "en" and p.lang != lang) for p in picked)
    return (f'<section class="related"><h2>{ui["related"]}</h2>'
            f'<div class="cards">{cards}</div></section>')


def build_articles(lang: str, pages: list[Page], alts_for, pool: list[Page] | None = None) -> None:
    tpl_base = read_template("base.html")
    tpl_article = read_template("article.html")
    ui = LANGS[lang]["ui"]
    artigos = [p for p in pages if p.section == "artigo"]
    pool = pool or artigos

    for page in pages:
        artigos = [p for p in pages if p.section == "artigo" and p.level == page.level]
        idx = artigos.index(page) if page in artigos else -1
        prev_html = next_html = ""
        if idx > 0:
            p = artigos[idx - 1]
            prev_html = f'<a class="pager-prev" href="{p.url}"><span>{ui["prev"]}</span><strong>{esc(p.title)}</strong></a>'
        if 0 <= idx < len(artigos) - 1:
            n = artigos[idx + 1]
            next_html = f'<a class="pager-next" href="{n.url}"><span>{ui["next"]}</span><strong>{esc(n.title)}</strong></a>'

        toc_block = ""
        if page.toc and page.meta.get("toc", True) is not False and "<li>" in page.toc:
            toc_block = (f'<nav class="toc" aria-label="{ui["toc"]}">'
                         f'<p class="toc-title">{ui["toc"]}</p>{page.toc}</nav>')

        body = render(tpl_article, {
            "title": esc(page.title),
            "description": esc(page.description),
            "category": esc(page.category),
            "content": page.html,
            "toc": toc_block,
            "tags": tags_html(page.tags),
            "reading": esc(page.reading),
            "prev": prev_html,
            "next": next_html,
            "crumbs": breadcrumbs_html(lang, page),
            "related": related_html(lang, page, [p for p in pool if p.section == "artigo"]),
        })
        extra = jsonld(article_ld(lang, page)) + jsonld(breadcrumb_ld(lang, page))
        if page.slug == "faq":
            faq = faq_ld(page)
            if faq:
                extra += jsonld(faq)
        if page.date:
            extra += (f'<meta property="article:published_time" content="{page.date}">'
                      f'<meta property="article:modified_time" content="{page.date}">')
        ctx = base_context(lang, page.title, page.description, page.url,
                           alts_for(page.key, page.url), body, "article", extra)
        write(out_path(page.url), render(tpl_base, ctx))
        log(page.url)


def build_home(lang: str, own: list[Page], foreign: list[Page], alts_for) -> None:
    cfg = LANGS[lang]
    ui = cfg["ui"]
    tpl = read_template(cfg["home_tpl"])
    tpl_base = read_template("base.html")

    guides = [p for p in foreign if p.section == "artigo"] if lang == "en" else \
             [p for p in own if p.section == "artigo"]
    featured = [p for p in (foreign if lang == "en" else own) if p.featured]
    is_foreign = lang == "en"

    visual = home_visual_context(lang)
    discovery = render(read_template(f"discovery.{lang}.html"), visual)
    body = render(tpl, {
        **visual,
        "beginner_path": beginner_home(lang, discovery),
        "cards": "\n      ".join(card_html(p, ui, is_foreign) for p in featured if p.slug in {"instalacao", "home-assistant", "hardware", "zigbee", "matter-thread", "apple-homekit"}),
        "recentes": "\n      ".join(list_item_html(p, ui, is_foreign) for p in guides[:6]),
        "total_guias": len(guides),
        "tagline": cfg["tagline"],
    })
    url = "/" + cfg["prefix"]
    ctx = base_context(lang, SITE["name"], cfg["description"], url,
                       alts_for("home", url), body, "home")
    write(out_path(url), render(tpl_base, ctx))
    log(url)


def build_listing(lang: str, own: list[Page], foreign: list[Page], alts_for) -> None:
    cfg = LANGS[lang]
    ui = cfg["ui"]
    tpl_base = read_template("base.html")
    url = "/" + cfg["prefix"] + ("artigos/" if lang == "pt" else "guides/")

    own_articles = [p for p in own if p.section == "artigo"]
    foreign_articles = [p for p in foreign if p.section == "artigo"] if lang == "en" else []
    total = len(own_articles) + len(foreign_articles)

    all_articles = own_articles + foreign_articles
    basics = [p for p in all_articles if p.level == "basico"]
    advanced = [p for p in all_articles if p.level != "basico"]
    items = "\n".join(list_item_html(p, ui, p.lang != lang) for p in basics)
    advanced_items = "\n".join(list_item_html(p, ui, p.lang != lang) for p in advanced)
    basics_title = "Comece por aqui, nesta ordem" if lang == "pt" else "Start here, in this order"
    advanced_title = "Aprofundamento — para depois" if lang == "pt" else "Further learning — for later"

    note = ""
    if lang == "en":
        note = ('<p class="table-note">The full guide library is currently written in Brazilian '
                'Portuguese and is being translated. Every guide below is open and readable — '
                'browser translation works well on these pages.</p>')

    body = f"""<article class="page">
    <header class="page-head">
      <p class="eyebrow">{ui['listing_eyebrow']}</p>
      <h1>{ui['listing_title']}</h1>
      <p class="lead">{ui['listing_lead'].format(n=total)}</p>
      {note}
    </header>
    <h2>{basics_title}</h2>
    <ul class="post-list">
      {items}
    </ul>
    <details class="library-advanced"><summary>{advanced_title}</summary><ul class="post-list">{advanced_items}</ul></details>
  </article>"""
    ctx = base_context(lang, ui["listing_title"], ui["listing_lead"].format(n=total), url,
                       alts_for("listing", url), body, "listing")
    write(out_path(url), render(tpl_base, ctx))
    log(url)


def build_404(lang: str, alts_for) -> None:
    cfg = LANGS[lang]
    ui = cfg["ui"]
    tpl_base = read_template("base.html")
    home = "/" + cfg["prefix"]
    listing = home + ("artigos/" if lang == "pt" else "guides/")
    body = f"""<article class="page page-404">
    <header class="page-head">
      <p class="eyebrow">{ui['e404_eyebrow']}</p>
      <h1>{ui['e404_title']}</h1>
      <p class="lead">{ui['e404_lead']}</p>
      <p class="cta-row">
        <a class="btn btn-primary" href="{home}">{ui['e404_home']}</a>
        <a class="btn btn-ghost" href="{listing}">{ui['e404_list']}</a>
      </p>
    </header>
  </article>"""
    url = home + "404.html"
    ctx = base_context(lang, ui["e404_title"], ui["e404_lead"], url,
                       {"pt": "/404.html", "en": "/en/404.html"}, body, "error")
    write(DIST / ("404.html" if lang == "pt" else "en/404.html"), render(tpl_base, ctx))
    log(url)


def build_search_index(lang: str, own: list[Page], foreign: list[Page]) -> None:
    pages = own + ([p for p in foreign if p.section == "artigo"] if lang == "en" else [])
    data = [{"t": p.title, "u": p.url, "d": p.description, "c": p.category, "x": p.text[:1200]}
            for p in pages]
    path = DIST / (LANGS[lang]["prefix"] + "search-index.json")
    write(path, json.dumps(data, ensure_ascii=False))
    log("/" + LANGS[lang]["prefix"] + "search-index.json")


def build_sitemap(urls: list[tuple[str, str, dict]]) -> None:
    hoje = date.today().isoformat()
    blocos = []
    vistos = set()
    for loc, lastmod, alts in urls:
        if loc in vistos:
            continue
        vistos.add(loc)
        alt = "".join(
            f'<xhtml:link rel="alternate" hreflang="{code}" href="{SITE["url"]}{href}"/>'
            for code, href in sorted(alts.items())
        )
        blocos.append(
            f"  <url><loc>{SITE['url']}{loc}</loc>"
            f"<lastmod>{lastmod or hoje}</lastmod>"
            f"<changefreq>monthly</changefreq>"
            f"<priority>{'1.0' if loc in ('/', '/en/') else '0.7'}</priority>"
            f"{alt}</url>"
        )
    write(DIST / "sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(blocos) + "\n</urlset>\n")
    write(DIST / "robots.txt",
          f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
    log("sitemap.xml + robots.txt")


def copy_static() -> None:
    if STATIC.exists():
        shutil.copytree(STATIC, DIST / "static", dirs_exist_ok=True)
        log("static/")
    shutil.copy2(STATIC / "img/favicon-sa.ico", DIST / "favicon.ico")
    for extra in ("_headers", "_redirects"):
        src = ROOT / extra
        if src.exists():
            shutil.copy2(src, DIST / extra)
            log(extra)
    # chave do IndexNow (arquivo de 32 caracteres hexadecimais na raiz)
    for chave in ROOT.glob("*.txt"):
        if re.fullmatch(r"[0-9a-f]{32}", chave.stem):
            shutil.copy2(chave, DIST / chave.name)
            log(chave.name + " (IndexNow)")


def main() -> None:
    if "--clean" in sys.argv and DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    print(f"\n🏠  Gerando {SITE['name']} (pt + en) → {DIST.relative_to(ROOT)}/\n")

    pages = {lang: load_pages(lang) for lang in LANGS}
    if not pages["pt"]:
        sys.exit("Nenhum arquivo .md encontrado em content/.")

    # mapa de equivalências entre idiomas
    index: dict[str, dict[str, str]] = {}
    for lang, plist in pages.items():
        for p in plist:
            index.setdefault(p.key, {})[lang] = p.url
    for lang in LANGS:
        prefix = "/" + LANGS[lang]["prefix"]
        index.setdefault("home", {})[lang] = prefix
        index.setdefault("listing", {})[lang] = prefix + ("artigos/" if lang == "pt" else "guides/")

    def alts_for(key: str, own_url: str) -> dict:
        found = dict(index.get(key, {}))
        for lang in LANGS:
            found.setdefault(lang, "/" + LANGS[lang]["prefix"])
        return found

    all_urls: list[tuple[str, str, dict]] = []
    for lang in ("pt", "en"):
        other = "en" if lang == "pt" else "pt"
        pool = pages[lang] + (pages[other] if lang == "en" else [])
        build_articles(lang, pages[lang], alts_for, pool)
        build_home(lang, pages[lang], pages[other], alts_for)
        build_listing(lang, pages[lang], pages[other], alts_for)
        build_404(lang, alts_for)
        build_search_index(lang, pages[lang], pages[other])
        all_urls.append(("/" + LANGS[lang]["prefix"], "", alts_for("home", "")))
        all_urls.append(("/" + LANGS[lang]["prefix"] + ("artigos/" if lang == "pt" else "guides/"),
                         "", alts_for("listing", "")))
        all_urls.extend((p.url, str(p.date or ""), alts_for(p.key, p.url)) for p in pages[lang])

    build_sitemap(all_urls)
    copy_static()

    files = sum(1 for f in DIST.rglob("*") if f.is_file())
    print(f"\n✅  {len(pages['pt'])} páginas em pt · {len(pages['en'])} em en · {files} arquivos em dist/\n")
    print("    Pré-visualize com:  python3 serve.py\n")


if __name__ == "__main__":
    main()
