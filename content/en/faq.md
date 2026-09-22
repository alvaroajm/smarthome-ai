---
title: Frequently asked questions
slug: faq
key: faq
description: Straight answers to the questions that come up most — cost, internet, renting, brands, privacy, voice assistants and where to begin.
category: FAQ
icon: help
order: 2
section: pagina
reading: 3 min read
date: 2026-09-22
tags: [FAQ, Beginners]
level: basico
---

## Do I need to code?

Not for this learning path. Installation, ZHA pairing and the first automation use buttons and menus.

## What do I need to start?

A hub running HAOS, such as Green or a supported Raspberry Pi, a ZBT-2 and one ZHA-compatible Zigbee light or sensor. Check devices you already own before buying.

## Are Home Assistant and HAOS the same thing?

Home Assistant is the program that controls your home. Home Assistant OS (HAOS) runs it and simplifies updates, backups and Apps.

## Does it work without internet?

Local devices and integrations can keep working. The hub and local network need power. Cloud services and remote access need a connection.

## Can I keep Alexa or Google Home?

Yes. Platforms can coexist. Connecting them to Home Assistant is an extra step; first, get your light working from the dashboard.

## Does ZHA need MQTT or HACS?

No. ZHA is a built-in integration. It needs a supported coordinator, such as ZBT-2, to form the Zigbee network.

## Does ZBT-2 run Zigbee and Thread at the same time?

No. It uses one protocol at a time. For this guide, choose Zigbee and the recommended installation with ZHA.

## Can I install HAOS on microSD?

Yes. The official Raspberry Pi installation includes an A2 microSD card of at least 32 GB. Use suitable storage and power, and keep backups outside the hub.

## Does Matter guarantee every feature?

No. Check whether the chosen platform supports the device category and its features. Matter over Thread also needs a Thread border router.

## My first automation failed. What next?

Check whether the light responds from the dashboard. Then open the automation menu and use Run actions. This skips triggers and conditions; use traces to inspect an actual run.

[Follow the beginner path](/en/start/).

Official references: [HAOS](https://www.home-assistant.io/installation/raspberrypi/), [ZHA](https://www.home-assistant.io/integrations/zha/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/), [Matter](https://www.home-assistant.io/integrations/matter/) e [automações](https://www.home-assistant.io/docs/automation/troubleshooting/).
