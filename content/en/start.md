---
title: Start your smart home
slug: start
key: instalacao
description: From choosing your hub to your first automated light.
category: Getting started
icon: rocket
order: 1
featured: true
reading: 4 min read
date: 2026-09-21
tags: [Home Assistant, Installation, Raspberry Pi, Backup]
---

Start with **one light and one sensor**. Build a small setup, test it, then expand.

<img class="guide-image" src="/static/img/home-comfort.webp" alt="Illustration of a living room with smart lighting and a sensor" width="1536" height="1024" loading="lazy">

## 1. Choose your hub

Your hub stays on to coordinate the home. Home Assistant Green comes with the system installed. A Raspberry Pi or mini PC needs setup first.

The official documentation recommends **Home Assistant OS** for most users. Follow the [installation instructions for your hardware](https://www.home-assistant.io/installation/).

## 2. Connect and set up

Connect power and Ethernet. Once the system is ready, open:

```text
http://homeassistant.local:8123
```

Create your account and check your location and time zone. If the address does not work, find the hub’s IP address in your router.

## 3. Add a device

Open **Settings → Devices & services**. Start with a supported device you already own. Check the [integration for its model](https://www.home-assistant.io/integrations/) before buying more hardware.

Zigbee needs a compatible adapter or hub. Matter over Thread also needs support for the Thread network.

## 4. Make a simple automation

Use **Settings → Automations & scenes**:

- **When:** motion is detected.
- **If:** it is night.
- **Then:** turn on the hallway light.

Save and test it. You can later add an action to turn the light off when motion stops. Basic automations do not require code.

## 5. Back up your setup

Set up backups under **Settings → System → Backups**. Keep a copy outside the hub, name devices clearly and organize them by room.

For remote control, consider Home Assistant Cloud or a properly configured VPN. Avoid exposing port 8123 directly to the internet. Offline operation depends on the devices and integrations you choose.

## Keep learning

- [Official beginner automation guide](https://www.home-assistant.io/getting-started/automation/)
- [Home Assistant terminology](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Full guide library (Portuguese)](/en/guides/)
