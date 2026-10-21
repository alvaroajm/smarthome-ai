---
title: Start your smart home
slug: start
key: instalacao
description: The full path from nothing to your first automated light, without programming: what to buy, in which order, how long it takes and the usual mistakes.
category: Getting started
icon: rocket
order: 0
featured: true
reading: 6 min read
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant, Installation, Raspberry Pi, Backup]
level: basico
---

Start small: **Home Assistant OS → ZBT-2 with ZHA → one light → one visual automation**. You do not
need to program. This page is the map; each step has its own illustrated guide. The core guides of this path are
available in English; the remaining guides are in Portuguese, with screenshots from the English
Home Assistant interface, and the [English homepage](/en/#casa-inteligente) introduces every topic.

## What you need on the table

| Item | What it does | Where to choose |
|---|---|---|
| **A hub running Home Assistant OS** | Runs Home Assistant 24/7. A Home Assistant Green, a Raspberry Pi 5 or a mini PC. | [Choose your hub (PT)](/hardware/) |
| **A Zigbee adapter (ZBT-2)** | Creates your Zigbee network and talks to lights and sensors. | [ZBT-1 vs ZBT-2](/en/zbt-dongles/) |
| **One Zigbee bulb or switch** | Your first device. Pick a model listed as supported by ZHA. | [Zigbee basics](/en/zigbee/) |
| **An Ethernet cable** | The hub should be wired to the router, not on Wi-Fi. | — |
| **Another computer or phone** | Where you open the Home Assistant dashboard in a browser. | — |

You do not need a camera, a voice assistant, Thread, Matter, MQTT or any extra App yet. All of that
comes later, when a real need shows up.

!!! dica "A short USB extension helps Zigbee"
    Connect the Zigbee adapter through a 30 cm to 1 m USB extension cable, away from the hub and from
    USB 3.0 ports. Those ports produce interference in the 2.4 GHz band, one of the most common reasons
    for "the bulb won't pair". The Home Assistant documentation itself recommends the extension.

## Follow this path

Every guide ends with something working. Times are rough estimates for a first-timer, not counting
shopping.

1. [What is a smart home?](/en/smart-home/) — 10 minutes. Compare Home Assistant, Alexa, Google
   Home, Apple Home, SmartThings and Tuya, and learn what "local automation" means.
2. [Meet Home Assistant](/en/home-assistant/) — 15 minutes. Dashboard, devices, entities, areas and
   automations, before you install anything.
3. [Install Home Assistant OS](/en/install-haos/) — 30 minutes (Green) to 1 hour (Pi 5 or mini PC).
   You end up at `http://homeassistant.local:8123`, with an account and an empty dashboard.
4. [Understand Zigbee](/en/zigbee/) — 10 minutes. Coordinator, routers and end devices, and why mains-
   powered bulbs strengthen the mesh.
5. [Thread and Matter, briefly (PT)](/matter-thread/) — 10 minutes. Enough to read a box in the shop and
   avoid buying what your network cannot serve yet.
6. [Connect ZBT-2 and set up ZHA](/en/zbt-dongles/) — 20 minutes. The bulb shows up on the dashboard
   and turns on from your phone.
7. [Create your first automation (PT)](/primeira-automacao/) — 20 minutes. The light turns on at sunset,
   with menus only.

## Mistakes that slow beginners down

- **Putting the hub on Wi-Fi.** Use Ethernet. Wi-Fi on the hub works, but causes drop-outs that are
  hard to diagnose exactly when you cannot diagnose anything yet.
- **Pairing the bulb too far from the adapter.** For the first pairing, keep the bulb a few metres
  from the ZBT-2. Move it to its final place afterwards.
- **Buying ten bulbs before the first one works.** Test with one. If the model is well supported,
  buy more of the same.
- **Leaving a Zigbee bulb behind an ordinary wall switch.** When someone flips the switch, the bulb
  disappears from the network. Keep the switch on, or replace it with a Zigbee switch, like the
  Zemismart ones in [my home (PT)](/minha-instalacao/).
- **Ignoring the exact model.** Before buying, search the exact model (not just the brand) in the ZHA
  or Zigbee2MQTT device lists. "Works with Alexa" on the box says nothing about Zigbee.
- **Skipping the backup.** Next topic.

## Keep it manageable

Name devices and rooms clearly. Set up backups under **Settings → System → Backups**, keep a copy
outside the hub, and store the encryption key somewhere safe — without it, the backup cannot be
restored.

With supported local devices and integrations, automations keep working without internet. The hub and
the local network still need power; cloud-based services need internet.

After the first light, in this order: update Home Assistant if an update is pending; install the
companion app on your phone (it also provides a home/away sensor used in many automations); add one
sensor (door, motion or temperature) and build a second automation; then explore
[integrations, Apps, HACS and cameras (PT)](/apps-integracoes/) as needs appear.

## Common questions at this stage

**Do I need the internet for the house to work?** Not for what this path builds. Home Assistant,
Zigbee and the sunset automation run on the local network. The internet is needed for updates, remote
access and cloud services such as voice assistants.

**Can I use Alexa or Apple Home as well?** Yes, later. Home Assistant can expose devices to Alexa
through [Home Assistant Cloud (PT)](/nabu-casa/) and to the Apple Home app through the
[HomeKit integration (PT)](/apple-homekit/). I use all three in my home.

**Zigbee or Wi-Fi bulbs?** Zigbee for this path: it does not load the router, forms a mesh and works
without the manufacturer's cloud. Wi-Fi products can come later, case by case.

## Later, if you need more

[Further learning (PT)](/aprofundamento/) covers alternative installations, Zigbee2MQTT, cameras and other
advanced topics. None of it is required for your first ZHA light. If you get stuck, check the
[FAQ](/en/faq/) or write through the [contact page](/en/contact/), stating hub, version, adapter and
device model.

Reference: [official Home Assistant installation guide](https://www.home-assistant.io/installation/).
