---
title: Start here: installing Home Assistant from scratch
slug: start
key: instalacao
description: The complete path — choosing hardware, flashing the image, the first login, protecting it with backups and adding your first device.
category: Getting started
icon: rocket
order: 1
featured: true
reading: 12 min read
date: 2026-09-21
tags: [Home Assistant, Installation, Raspberry Pi, Backup]
---

If you simply want **the lights to turn on by themselves** and have no plans to become a server
administrator, this is the shortest route. The goal of this page is to take you from "I have nothing" to
"my first automation is running", without decisions you will regret in six months.

## 1. Choose where Home Assistant will live

Home Assistant needs a computer that stays on 24/7. The three sensible options:

| Option | Best for | Watch out for |
|---|---|---|
| **Ready-made appliance** (Home Assistant Green and similar) | Plug in and use | Less expandable; fixed storage |
| **Raspberry Pi 5 + NVMe SSD** | People who like tinkering | **Never use an SD card** as the main disk |
| **x86 mini PC (N100 / Ryzen)** | Cameras, local AI, Frigate | Higher power draw; install via Proxmox or HAOS directly |

!!! tip "Golden rule"
    Any of the three works. What does **not** work is running your home on a laptop you take to the office,
    or on a cheap microSD card — SD cards die from write wear, usually at the worst possible moment.

Details of each option, with power draw and cost, are in the [hardware guide](/hardware/).

## 2. Choose the installation method

There are four ways to install, and they are **not** equivalent:

- **Home Assistant OS (HAOS)** — a dedicated operating system. It has the add-on store, one-click updates
  and built-in backups. **This is the right choice for 95% of people.**
- **Home Assistant Supervised** — on top of a Debian you maintain. Only if you know exactly why.
- **Home Assistant Container (Docker)** — light and flexible, but **no add-ons**; you install Mosquitto,
  Zigbee2MQTT and friends yourself.
- **Home Assistant Core (Python venv)** — for development. Avoid it day to day.

!!! warning "The most common beginner mistake"
    Installing the Container version because it sounds "more professional", then discovering weeks later
    that half the tutorials online assume add-ons you do not have. Start with **HAOS**.

## 3. Flash the image and boot

1. Download the HAOS image for your hardware at [home-assistant.io/installation](https://www.home-assistant.io/installation/).
2. Flash it with **Raspberry Pi Imager** ("Use custom image") or **balenaEtcher**, onto the SSD or eMMC.
3. Connect the device **to your router with an Ethernet cable** for the first install — Wi-Fi at this stage
   only makes troubleshooting harder.
4. Power it on and wait 5 to 20 minutes on first boot: the system is expanding itself and downloading components.
5. In a browser on your Mac or PC, open:

```text
http://homeassistant.local:8123
```

If the `.local` address does not resolve (common with mesh Wi-Fi or VLANs), find the IP in your router and
use `http://192.168.x.y:8123`.

## 4. The first 10 minutes that matter

When you create the administrator account, the wizard discovers much of your network automatically.
Before clicking around, do these four things:

1. **Set the correct location and time zone.** Half of all automations depend on sunrise and sunset.
2. **Create the first backup** under *Settings → System → Backups* and enable automatic backups.
3. **Reserve the IP in your router** (static DHCP lease) so Home Assistant never changes address.
4. **Rename everything, calmly.** `sensor.bedroom_temperature` ages well; `sensor.0x00158d0004f2a1` does not.

!!! note "Backups separate a hobby from a disaster"
    Keep a copy **off the device** — Google Drive, a NAS, an iCloud folder on your Mac. The *Samba Backup*
    add-on or a cloud storage integration solves this in five minutes.

## 5. Add your first device

The order that causes the least frustration:

1. **Something already on your network**: your TV, AV receiver, printer, robot vacuum. Go to
   *Settings → Devices & services* and accept the automatically discovered integrations.
2. **A cheap Zigbee sensor** (temperature or door contact) with a USB coordinator.
   See [Zigbee2MQTT or ZHA](/zigbee/) to pick the radio and the software.
3. **A Matter device**, if you already own an Apple TV, a HomePod or any hub that can act as a
   [Thread border router](/matter-thread/).

## 6. Your first automation (one you will actually use)

Forget elaborate scenes. Start with something that solves a real annoyance — the hallway light at night:

```yaml
alias: Hallway - soft light on motion at night
description: Turns on at 20% between 10pm and 6am and turns itself off
triggers:
  - trigger: state
    entity_id: binary_sensor.hallway_motion
    to: "on"
conditions:
  - condition: time
    after: "22:00:00"
    before: "06:00:00"
actions:
  - action: light.turn_on
    target:
      entity_id: light.hallway
    data:
      brightness_pct: 20
  - delay: "00:02:00"
  - action: light.turn_off
    target:
      entity_id: light.hallway
mode: restart
```

`mode: restart` is the detail that makes the automation feel intelligent: if motion happens again during
those two minutes, the timer restarts instead of switching the light off in your face.

## 7. Checklist before expanding

- [x] Automatic backups enabled, with an off-device copy
- [x] IP reserved in the router
- [x] Remote access solved (Nabu Casa, router VPN or Tailscale — **never** by opening port 8123)
- [x] Zigbee coordinator on a USB extension cable, away from the case and from USB 3.0 ports
- [x] Names and areas organised

With that in place, continue with the guides in the library — they are currently written in Portuguese and
translate well in the browser while the English versions are being written.
