---
title: About SmartHome-AI
slug: about
key: sobre
description: I created SmartHome-AI to share my installation, photographs and smart home guides using Home Assistant.
category: About
icon: book
order: 3
section: pagina
reading: 3 min read
date: 2026-09-21
updated: 2026-10-21
tags: [About, Contact, Open Source]
---

<img src="/static/img/smarthome-banner.jpg?v=20261021" alt="SmartHome-AI banner" width="1400" height="788" decoding="async">


I created **SmartHome-AI** to share what I learn while building my smart home and bring together my installation records, photographs and guides.

My commitment is to **explain the why before the how**, with guidance for beginners and examples that need to be adapted to each home.

## Editorial principles

1. **Local first.** The cloud is a convenience, never a dependency.
2. **Open source whenever possible.** Home Assistant, ESPHome, Zigbee2MQTT, Frigate, Scrypted.
3. **No sponsored lists.** When a product is named, it is because it solves a described problem.
4. **Plan B matters.** Every automation must work — or fail safely — when something goes down.
5. **Respect for the people living there.** Automation that annoys the household is bad automation.

## Topics covered

- [Home Assistant](/en/home-assistant/) — the platform
- [ESPHome and ESP32 (PT)](/esphome-esp32/) — devices you build yourself
- [Zigbee and ZHA](/en/zigbee/), [Zigbee2MQTT (PT)](/zigbee2mqtt/) and the [ZBT-1 / ZBT-2 dongles](/en/zbt-dongles/)
- [Matter and Thread (PT)](/matter-thread/) — the standard that crosses ecosystems
- [MQTT (PT)](/mqtt/) — the postal service of the smart home
- [Apple HomeKit (PT)](/apple-homekit/) — iPhone, Siri and Apple TV
- [Scrypted, Frigate and cameras (PT)](/scrypted/) and [AI cameras (PT)](/cameras-ia/)
- [Claude and MCP (PT)](/claude-mcp/) and [OpenClaw (PT)](/openclaw/) — AI at home
- [Hardware (PT)](/hardware/), [networking (PT)](/rede-wifi/) and [CasaOS / umbrelOS (PT)](/casaos-umbrel/)

## About the language

The beginner library includes English guides; links marked **PT** lead to Brazilian Portuguese pages
that do not yet have an English edition. Configuration examples still need to be adapted to your setup,
including entity IDs and any text used in labels or notifications.

## How this site is built

I built this static site with HTML, CSS and JavaScript without frameworks, using a **Python** generator for
Markdown files, versioned on **GitHub** and published on **Cloudflare**. There is no reader registration
or site database. I use Google Analytics for traffic metrics and included Google AdSense
integration for advertising, subject to Google's site approval. Advertising does not determine my
topics or editorial recommendations. See the [Privacy policy](/en/privacy/) for cookies,
third-party services and your control options.

The generator lives in `build.py`, with separate modules for visual components and the `Markdown`
library as its declared dependency. Content is stored as `.md` files under `content/`. After installing
`requirements.txt`, run `python3 build.py` to generate `dist/` and `python3 scripts/check.py` to check
internal links and templates before publishing.

<span id="who-writes-it"></span>

## Who I am

<div class="author-box" markdown="0">
  <img src="/static/img/alvaro-retrato-20261021.jpg" alt="Álvaro Menezes" width="666" height="1180" loading="lazy">
  <div>
    <p class="author-name">Álvaro Menezes</p>
    <p class="author-role">I built my home automation setup and created SmartHome-AI to share what I learn.</p>
    <p class="author-links">
      <a href="https://github.com/alvaroajm" target="_blank" rel="noopener">GitHub</a>
    </p>
  </div>
</div>

I am **Álvaro Menezes**, an enthusiast of home automation, Home Assistant, ESP32 and local systems. I write these guides and share the installation I built at home.

<span id="the-authors-other-channels"></span>

## My other channels

I also run AI-generated video projects that are not directly related to smart homes. I keep their links here, outside the guides, for anyone curious:

{{channels}}

## Equipment used at home

I use **Home Assistant OS on a mini-PC with a Ryzen 7 processor**, **Zemismart Zigbee smart switches** and **Philips Hue Zigbee lights**.

I control my Zigbee network from **Home Assistant** through **Zigbee2MQTT**, with the **ZBT-2 from Nabu Casa** as the coordinator.

My **Thread** network is shared with **Apple's** Thread network. I use the **ZBT-1** as the Thread radio adapter, separate from the ZBT-2 used for Zigbee.

In my **living room**, a **Zemismart smart plug** controls the room's lights. I use **Philips Hue** in the **living room** and the **primary suite**. I operate the lights from my phone using **Apple Home (HomeKit)**, by voice through **Alexa**, and directly through **Home Assistant**.

This is my installation, not a list of products I subjected to comparative tests. I still need to document the exact models of the other devices here. I do not present this list as a compatibility guarantee for a purchase.

I use several devices I identified as **Echo Dot Max** and **one Echo Studio Max in the living room**. I connect Alexa to Home Assistant through **Nabu Casa**. I also use **two Apple TV 4K devices as Apple HomeKit home hubs**.

I also have a **Broadlink IR and RF controller**, pictured beside the Zemismart Zigbee switches in [my installation report (PT)](/minha-instalacao/#interruptores-na-parede-e-controle-broadlink).

### LED strips

I control my installation's **LED strips with WLED over Wi-Fi**.

### Cameras

I use **Tapo TC70**, **Intelbras iM4** and an **Intelbras DVR**. In my setup, I describe the image path as **cameras → Home Assistant → Scrypted → HomeKit Secure Video**. I still need to document the DVR model, video source and Scrypted plugins here; this arrangement is not a universal procedure for other installations.

## Installation record

See the [installation photo report (in Portuguese)](/minha-instalacao/), including the mini-PC, Mac mini M4, ESP32-S3 display configured with ESPHome, Apple TV and Roborock robot vacuum. The setup also includes a Philips Hue hub.

<div class="lesson-split" markdown="0">
<figure class="ha-screen"><a href="/static/img/casa-do-autor/central-home-assistant.jpg" target="_blank" rel="noopener" aria-label="Enlarge photo: My Home Assistant hub"><img src="/static/img/casa-do-autor/central-home-assistant.jpg" alt="My Home Assistant hub" width="960" height="1280" loading="lazy" decoding="async"></a><figcaption><strong>My Home Assistant hub</strong> The HAOS mini-PC and Mac mini M4 are separate computers.</figcaption></figure>
<figure class="ha-screen"><a href="/static/img/casa-do-autor/tela-esphome.jpg" target="_blank" rel="noopener" aria-label="Enlarge photo: My ESP32-S3 display with ESPHome"><img src="/static/img/casa-do-autor/tela-esphome.jpg" alt="My ESP32-S3 display with ESPHome" width="960" height="1280" loading="lazy" decoding="async"></a><figcaption><strong>My ESP32-S3 display with ESPHome</strong> A dedicated interface with information and room shortcuts.</figcaption></figure>
</div>

## Inside the living room

These are photographs of my living room: lighting around the TV wall, lamps and accent lighting on furniture. I control the LED strips with WLED over Wi-Fi and use Apple Home, Alexa and Home Assistant to operate the lights. The photographs show the rooms and equipment; integration details belong in the corresponding guides.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" target="_blank" rel="noopener" aria-label="Enlarge photo: Living room opening onto the dining area, with a sofa, armchairs and piano."><img src="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" alt="Living room opening onto the dining area, with a sofa, armchairs and piano." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Living room opening onto the dining area, with a sofa, armchairs and piano. Photo of my installation.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-painel-tv.jpg" target="_blank" rel="noopener" aria-label="Enlarge photo: TV wall with table lamps and lighting beneath the cabinet."><img src="/static/img/casa-do-autor/sala-painel-tv.jpg" alt="TV wall with table lamps and lighting beneath the cabinet." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>TV wall with table lamps and lighting beneath the cabinet. Photo of my installation.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" target="_blank" rel="noopener" aria-label="Enlarge photo: Side view of the living room, with floor lamps and lighting around the glass cabinet."><img src="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" alt="Side view of the living room, with floor lamps and lighting around the glass cabinet." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Side view of the living room, with floor lamps and lighting around the glass cabinet. Photo of my installation.</figcaption></figure>

## How to read these guides

Original diagrams are conceptual overviews, not interface screenshots or drawings of commercial models. Official instructions are linked beside the illustrations. Configuration examples and test plans need to be adapted to your installation. An educational example does not establish compatibility with every device.

In my reports, I distinguish equipment I use from configurations and results I have documented. Where those details are absent, I offer guidance based on the cited sources rather than a product test. You can consult the [public change history](https://github.com/alvaroajm/smarthome-ai/commits/main/) and submit corrections using the contact details below.

## Contact and corrections

Found an error, have a suggestion or want to request a topic? Corrections are very welcome — this site is
maintained in the open and improves with the people who read it.

Reach me by e-mail at [alvaroajm@gmail.com](mailto:alvaroajm@gmail.com).
