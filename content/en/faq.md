---
title: Frequently asked questions
slug: faq
key: faq
description: Straight answers to the questions that come up most — cost, internet, renting, brands, privacy, voice assistants and where to begin.
category: FAQ
icon: help
order: 2
section: pagina
reading: 7 min read
date: 2026-09-21
tags: [FAQ, Beginners]
---

## Do I need to know how to code?

No. Most automations are built through a graphical editor, and community blueprints cover the common cases.
Reading YAML helps when you want something finer — and it is a configuration language, not a programming
language: an afternoon is enough to grasp the essentials.

## How much does it cost to start?

An honest start has three items: the server (appliance, Raspberry Pi with an SSD, or a mini PC), a Zigbee
coordinator, and three to five sensors. After that, every device is a separate decision. The expensive
mistake is buying large kits before understanding what your home needs — almost everyone who does that ends
up with a drawer full of unused gadgets.

## Does it work without internet?

With Home Assistant running locally, yes: automations, sensors, local dashboards and switches keep working
while the internet is down. What stops are external services — weather forecasts, push notifications away
from home, cloud assistants, and devices that depend on a vendor's server.

## I rent. Can I still automate?

Absolutely. Avoid anything that requires construction work:

- **Smart bulbs and plugs** instead of modules inside the wall
- **Battery sensors** attached with double-sided tape
- **Standalone Zigbee buttons** that replace switches without rewiring anything
- **Infrared control for air conditioning** (one IR blaster covers several units)

When you move, everything leaves with you in a single box.

## Which brand should I buy?

The better question is: **"does this device work locally?"**. Prefer, in this order: Zigbee, Matter over
Thread, devices running ESPHome or Tasmota, and Wi-Fi devices with a local integration. Avoid products that
only work through the vendor's app with a mandatory cloud account — they are the first to become e-waste
when the company changes strategy.

## Do I have to drop Alexa and Google?

No. They remain excellent as a **voice interface**. The difference is that they now command Home Assistant,
which is what actually decides. If the service goes down or you switch assistants, your automations survive.

## Zigbee or Wi-Fi for sensors?

Zigbee, almost always. Wi-Fi sensors use far more power (they rarely last years on a battery), take up
addresses on your network and overload the router. Details in [Zigbee in practice](/zigbee/).

## Does Matter solve every compatibility problem?

It solves many, but it is not magic: the specification covers device categories progressively, and a
vendor's advanced features do not always fit the standard. Matter guarantees the basics working everywhere —
which is already a lot. See [Matter and Thread](/matter-thread/).

## Is my data safe?

With local processing, your data stays in your house. The practical rules: enable two-factor authentication,
**never** expose Home Assistant directly to the internet (use a VPN or Nabu Casa), keep encrypted backups
off the server, and put cameras on a network without internet access.

## Is an SD card really that bad?

Yes, for permanent use. The Home Assistant database writes continuously and consumer cards fail from wear,
usually between 6 and 18 months — and the failure tends to be silent until the day nothing boots. NVMe SSD
or eMMC, always.

## Where do I start today if I am short on time?

1. Install [Home Assistant](/en/start/) on simple hardware
2. Integrate what you **already** have on the network (TV, vacuum, printer, receiver)
3. Buy a Zigbee coordinator and **one** motion sensor
4. Automate **one** real annoyance (the hallway light at night is usually the best first case)
5. Only then plan the whole house
