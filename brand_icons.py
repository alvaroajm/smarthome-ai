"""Official project artwork for resource cards, guide links and navigation.

Assets are served locally, unchanged. Their official sources and checksums are
recorded in static/img/brands/sources.json. Text remains the accessible link name.
"""
from functools import lru_cache
from hashlib import md5
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

BRAND_DIR = Path(__file__).resolve().parent / "static/img/brands"
FILES = {
    "casaos": "casaos.png", "umbrel": "umbrel.png", "zimaos": "zimaos.png",
    "home-assistant": "home-assistant.svg", "esphome": "esphome.svg",
    "nabu-casa": "nabu-casa.svg", "zigbee2mqtt": "zigbee2mqtt.png",
    "wled": "wled.png", "home-assistant-brasil": "home-assistant-brasil.png",
    "scrypted": "scrypted.png", "open-home": "open-home.png",
    "github": "github.svg", "wikipedia": "wikipedia.svg", "assist": "assist.png",
    "proxmox": "proxmox.png", "ubuntu": "ubuntu.png", "hacs": "hacs.png",
    "frigate": "frigate.svg", "ollama": "ollama.png", "balena-etcher": "balena-etcher.png",
    "ventoy": "ventoy.ico", "llmvision": "llmvision.png", "alpine": "alpine.ico",
    "raspberry-pi": "raspberry-pi.png",
}

HOSTS = {
    "casaos.zimaspace.com": "casaos", "casaos.io": "casaos",
    "umbrel.com": "umbrel", "apps.umbrel.com": "umbrel",
    "zimaspace.com": "zimaos", "home-assistant.io": "home-assistant",
    "community.home-assistant.io": "home-assistant", "nabucasa.com": "nabu-casa",
    "esphome.io": "esphome", "devices.esphome.io": "esphome",
    "zigbee2mqtt.io": "zigbee2mqtt", "install.wled.me": "wled", "kno.wled.ge": "wled",
    "homeassistantbrasil.com.br": "home-assistant-brasil", "scrypted.app": "scrypted",
    "openhomefoundation.org": "open-home", "en.wikipedia.org": "wikipedia",
    "proxmox.com": "proxmox", "ubuntu.com": "ubuntu", "hacs.xyz": "hacs",
    "frigate.video": "frigate", "ollama.com": "ollama", "etcher.balena.io": "balena-etcher",
    "ventoy.net": "ventoy", "llmvision.org": "llmvision",
    "alpinelinux.org": "alpine", "wiki.alpinelinux.org": "alpine",
    "raspberrypi.com": "raspberry-pi", "downloads.raspberrypi.org": "raspberry-pi",
}

# A comparison guide gets both project marks; unrelated guides keep their own icons.
GUIDES = {
    "/home-assistant/": ("home-assistant",),
    "/esphome-esp32/": ("esphome",),
    "/nabu-casa/": ("nabu-casa",),
    "/casaos-umbrel/": ("casaos", "umbrel"),
    "/scrypted/": ("scrypted",),
    "/zigbee/": ("home-assistant",),
    "/zigbee2mqtt/": ("zigbee2mqtt",),
    "/instalar-haos/": ("home-assistant",),
    "/comandos-haos/": ("home-assistant",),
}


def brands_for_link(url: str) -> tuple[str, ...]:
    parsed = urlsplit(url)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    if parsed.scheme and parsed.scheme not in ("http", "https"):
        return ()
    if not host or host == "smarthome-ai.com":
        path = parsed.path
        if path.startswith("/en/"):
            path = path[3:]
        return GUIDES.get(path, ())
    if host == "home-assistant.io" and parsed.path.startswith("/voice_control/"):
        return ("assist",)
    key = "github" if host == "github.com" else HOSTS.get(host)
    return (key,) if key else ()


@lru_cache(maxsize=None)
def brand_image(key: str) -> str:
    filename = FILES[key]
    digest = md5((BRAND_DIR / filename).read_bytes()).hexdigest()[:8]
    return (f'<img class="project-logo" data-project="{key}" '
            f'src="/static/img/brands/{filename}?v={digest}" '
            'width="32" height="32" alt="" decoding="async">')


def project_icons(*keys: str) -> str:
    if not keys:
        return ""
    pair = " project-icons-pair" if len(keys) > 1 else ""
    return (f'<span class="project-icons{pair}" aria-hidden="true">'
            + "".join(brand_image(key) for key in keys) + "</span>")


def icons_for_link(url: str) -> str:
    return project_icons(*brands_for_link(url))


class _ProjectLinks(HTMLParser):
    """Keep original markup, adding decorative icons only to textual links."""
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.line_starts = [0]
        for line in source.splitlines(keepends=True):
            self.line_starts.append(self.line_starts[-1] + len(line))
        self.output = []
        self.anchor = None

    def emit(self, text):
        (self.anchor[2] if self.anchor else self.output).append(text)

    def handle_starttag(self, tag, attrs):
        source = self.get_starttag_text()
        if tag == "a" and self.anchor is None:
            self.anchor = (source, dict(attrs), [])
        else:
            self.emit(source)

    def handle_endtag(self, tag):
        line, column = self.getpos()
        start = self.line_starts[line - 1] + column
        closing = self.source[start:self.source.index(">", start) + 1]
        if tag == "a" and self.anchor is not None:
            opening, attrs, fragments = self.anchor
            self.anchor = None
            body = "".join(fragments)
            # Existing image links, SVG controls and populated brand slots stay intact.
            illustrated = any(mark in body.lower() for mark in ("<img", "<svg", "<picture"))
            icon = "" if illustrated else icons_for_link(attrs.get("href", ""))
            self.output.append(opening + icon + body + closing)
        else:
            self.emit(closing)

    def handle_startendtag(self, tag, attrs):
        self.emit(self.get_starttag_text())

    def handle_data(self, data):
        self.emit(data)

    def handle_entityref(self, name):
        self.emit(f"&{name};")

    def handle_charref(self, name):
        self.emit(f"&#{name};")

    def handle_comment(self, data):
        self.emit(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.emit(f"<!{decl}>")


def decorate_project_links(html: str) -> str:
    parser = _ProjectLinks(html)
    parser.feed(html)
    parser.close()
    if parser.anchor is not None:
        raise ValueError("Unclosed link while adding project icons")
    return "".join(parser.output)
