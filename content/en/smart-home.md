---
title: What is a smart home?
slug: smart-home
key: casa-inteligente
description: What a smart home is, how Home Assistant, Alexa, Google Home, Apple Home, SmartThings and Tuya compare, the local-versus-cloud difference and where to start without wasting money.
category: Step by step
icon: book
order: 1
featured: true
level: basico
section: artigo
reading: 7 min read
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

A **smart home** uses connected devices to make everyday tasks easier. You can switch off a light from your phone, ask for something by voice, or let a rule act on its own.

**Control** is you pressing the button. **Automation** is the house acting when something happens: switching a light on at dusk, for example. A home is only really "smart" when the second part works without anyone thinking about it.

## The four layers of every smart home

Every installation, from the simplest to the most elaborate, has the same four layers. Understanding them keeps you from buying parts that cannot talk to each other.

| Layer | What it is | Examples |
|---|---|---|
| **Devices** | What measures or acts: bulbs, switches, sensors, plugs, locks, cameras. | Zigbee bulb, door sensor, energy-monitoring plug. |
| **Network or protocol** | How the device communicates. | Zigbee, Thread, Wi-Fi, Bluetooth, infrared. |
| **Hub** | What receives the information, stores the rules and sends the commands. | Home Assistant, Hue bridge, an Echo with Zigbee, an Apple TV as a HomeKit hub. |
| **Interface** | How you interact. | Phone app, voice, wall panel, physical button, an automation acting by itself. |

The hub is the part that defines almost everything: it decides which protocols the house understands, whether the rules run on your network or in someone's cloud, and whether devices from different brands can work together.

## Local or cloud: the difference that matters most

A **local** device talks to the hub inside your home. A **cloud** device sends the command to the manufacturer's server, which sends it back to the device, even if both are in the same room. In practice:

- **Without internet**, the local one keeps working; the cloud one stops.
- **Speed**: local responds in a fraction of a second; cloud takes one to several seconds.
- **Longevity**: if the manufacturer shuts the service down, a cloud device becomes a paperweight. It has happened to several brands.
- **Privacy**: locally, what happens in your home stays in it.

Many cheap Wi-Fi products are cloud devices. Zigbee, Thread and Matter products are local by design. Home Assistant lets you mix both, but this path starts with local.

## Which platform should you choose?

A platform brings the controls and the rules together. They can coexist: Home Assistant can handle the automations while, with the right connection, you keep using the Apple Home app or a voice assistant.

<div class="platform-choices"><article class="platform-choice platform-featured"><p class="eyebrow">The focus of this site</p><h3>Home Assistant</h3><p>The hub that brings devices and automations from different brands together.</p><dl><dt>Strengths</dt><dd>Local control, freedom of choice and flexible automations.</dd><dt>Limitations</dt><dd>Needs a hub that stays on, initial setup and maintenance.</dd></dl><a class="ext" href="https://www.home-assistant.io/" target="_blank" rel="noopener">Official reference</a></article><article class="platform-choice"><p class="eyebrow">Platform</p><h3>Alexa</h3><p>Amazon's ecosystem, known for Echo devices and voice commands.</p><dl><dt>Strengths</dt><dd>Convenient for voice and simple routines with compatible devices.</dd><dt>Limitations</dt><dd>Many functions depend on the cloud; radios and features vary between Echo models.</dd></dl><a class="ext" href="https://developer.amazon.com/en-US/docs/alexa/smarthome/wwa-connection-options.html" target="_blank" rel="noopener">Official reference</a></article><article class="platform-choice"><p class="eyebrow">Platform</p><h3>Google Home</h3><p>Google's app and ecosystem for organising and controlling the home.</p><dl><dt>Strengths</dt><dd>Brings controls, voice and compatible Matter devices together.</dd><dt>Limitations</dt><dd>Matter requires a compatible hub; remote access and online services depend on the internet.</dd></dl><a class="ext" href="https://support.google.com/googlehome/answer/13127223" target="_blank" rel="noopener">Official reference</a></article><article class="platform-choice"><p class="eyebrow">Platform</p><h3>Apple Home / HomeKit</h3><p>The Home app integrates compatible accessories with the iPhone and Siri.</p><dl><dt>Strengths</dt><dd>Tight integration with Apple devices and Home app automations.</dd><dt>Limitations</dt><dd>Remote access and automations need an Apple home hub; check accessory support.</dd></dl><a class="ext" href="https://support.apple.com/en-us/102557" target="_blank" rel="noopener">Official reference</a></article><article class="platform-choice"><p class="eyebrow">Platform</p><h3>Samsung SmartThings</h3><p>An app that gathers Samsung devices and other compatible brands.</p><dl><dt>Strengths</dt><dd>Graphical routines; some can run locally on a compatible hub.</dd><dt>Limitations</dt><dd>Not every routine is local. Features and protocols depend on the devices and the hub.</dd></dl><a class="ext" href="https://developer.smartthings.com/docs/automations/rules" target="_blank" rel="noopener">Official reference</a></article><article class="platform-choice"><p class="eyebrow">Platform</p><h3>Tuya / Smart Life</h3><p>A platform used by many brands, usually through the Smart Life app.</p><dl><dt>Strengths</dt><dd>Easy to start from the phone, with devices in many categories.</dd><dt>Limitations</dt><dd>Features and quality vary by manufacturer; many functions use the cloud, although some hubs run local scenes.</dd></dl><a class="ext" href="https://developer.tuya.com/en/docs/iot/user-manual-for-tuya-smart-v3177?id=K9obrofrfk4sk" target="_blank" rel="noopener">Official reference</a></article></div>

## Why Home Assistant?

This path prioritises freedom of choice and local automations. Home Assistant provides that foundation, but needs a device that stays on and some care with updates and backups. Compatibility depends on the model and the integration.

**We start with Home Assistant OS, Zigbee, ZHA and the ZBT-2.** Learn one step at a time; voice, cameras and extras can wait.

The platforms are not mutually exclusive. In [my home](/minha-instalacao/) (page in Portuguese), Home Assistant is the hub, and the same lights are switched from the Apple Home app and by voice through Alexa. The difference is who keeps the rules: Home Assistant.

## What to automate first

Good automations solve a real annoyance and are easy to switch off if they get in the way. Five examples that work for most homes, from easiest to hardest:

1. **A light at dusk.** A living-room or entrance lamp turns on at sunset and off at a fixed time. It is the [first automation](/primeira-automacao/) of this path.
2. **A hallway light on motion.** A presence sensor turns on a dim light in the small hours and off two minutes after the last movement.
3. **Door-left-open alert.** A contact sensor on the fridge or the gate sends a phone notification if it stays open for more than five minutes.
4. **Everything off when leaving.** When the last family phone leaves the house, selected lights and plugs switch off.
5. **Room climate.** A temperature sensor turns on a fan or an air conditioner over infrared above 28 °C and off below 25 °C.

Locks, heaters and gates deserve to wait, with the safeguards described in the [Terms of use](/en/terms/#2-electrical-work-hardware-and-firmware).

## How much does it cost to start

A hub, a Zigbee adapter and one bulb are enough to learn everything this path teaches. The guide [Choose your hub](/hardware/) (in Portuguese) compares prices and models; the [Zigbee](/en/zigbee/) guide explains why a mains-powered bulb is worth more than a battery sensor at the beginning. The most expensive mistake is not choosing the wrong hub: it is buying ten cloud devices in a promotional kit before knowing what the house needs.

## Minimum vocabulary

- **Hub:** the device that runs Home Assistant.
- **Integration:** the connection between Home Assistant and a brand, service or protocol.
- **Device:** the physical unit; **entity:** each thing it measures or controls.
- **Area:** the room where the device lives, used for grouping and voice commands.
- **Scene:** a set of states ("movie": lights at 20%, TV on).
- **Automation:** trigger + condition + action, running on its own.
- **Zigbee coordinator:** the USB radio (ZBT-2) that creates the home's Zigbee network.

Continue with [What is Home Assistant?](/en/home-assistant/).
