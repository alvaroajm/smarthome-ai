---
level: avancado
title: Sensors with ESPHome and ESP32
slug: esphome-esp32
key: esphome-esp32
description: Build temperature, presence and energy sensors with ESP32 and ESPHome, without coding in C: components, your first project and Home Assistant integration.
category: DIY & firmware
icon: chip
order: 105
featured: true
section: artigo
reading: 5 min read
date: 2026-09-22
updated: 2026-10-21
tags: [ESPHome, ESP32, DIY, YAML, Sensors]
---

A sensor that fits exactly where you need it. A button that triggers your favourite scene. A tiny screen showing the bedroom temperature. **ESP32 + ESPHome** lets you build these small projects and connect them to Home Assistant.

**IoT** means connected objects exchanging information. **DIY** is doing it yourself. Here, your board talks to the hub over the local network; you don't need a manufacturer's app for each project.

## Two ways to start

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/esp32.webp" target="_blank" rel="noopener" aria-label="Enlarge: ESP32-DevKitC: a general-purpose board for connecting sensors and other components."><img src="/static/img/ha-features/esp32.webp" width="900" height="389" alt="ESP32-DevKitC: a general-purpose board for connecting sensors and other components." loading="lazy" decoding="async"></a><figcaption>ESP32-DevKitC: a general-purpose board for connecting sensors and other components. · <a class="ext" href="https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html" target="_blank" rel="noopener">Official image</a></figcaption></figure>

ESP32 development boards offer connections for sensors, buttons and screens. There are many variants: check the chip, the pinout, the memory and the components before following a recipe.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/atom-s3.webp" target="_blank" rel="noopener" aria-label="Enlarge: M5Stack ATOM-S3: an ESP32-S3 with a screen, a button and connectors in a tiny case."><img src="/static/img/ha-features/atom-s3.webp" width="800" height="800" alt="M5Stack ATOM-S3: an ESP32-S3 with a screen, a button and connectors in a tiny case." loading="lazy" decoding="async"></a><figcaption>M5Stack ATOM-S3: an ESP32-S3 with a screen, a button and connectors in a tiny case. · <a class="ext" href="https://docs.m5stack.com/en/core/AtomS3" target="_blank" rel="noopener">Official image</a></figcaption></figure>

The **ATOM-S3** includes a small screen and a button, useful for controls and information. Configuring the screen and its components is specific to the board. It should not be confused with the **ATOM Echo**, which has audio hardware and an official tutorial for using Assist.

## ESPHome Device Builder: the dashboard for your projects

**ESPHome** is an open-source project from the Open Home Foundation, backed by Nabu Casa. The **Device Builder** can be installed as an App on HAOS and organises your devices from the browser.

<figure class="feature-figure"><a href="/static/img/ha-features/esphome-builder.webp" target="_blank" rel="noopener" aria-label="Enlarge: Official ESPHome Device Builder screen, showing devices and their connection state."><img src="/static/img/ha-features/esphome-builder.webp" width="1000" height="667" alt="Official ESPHome Device Builder screen, showing devices and their connection state." loading="lazy" decoding="async"></a><figcaption>Official ESPHome Device Builder screen, showing devices and their connection state. · <a class="ext" href="https://esphome.io/install/getting-started/" target="_blank" rel="noopener">Official image</a></figcaption></figure>

1. In **Settings → Apps**, open the store and install **ESPHome Device Builder**.
2. Start the App and open the web interface.
3. Choose **Create device** and follow the new-configuration wizard.
4. Confirm the board type and the Wi-Fi network.
5. Use **Install** and follow the USB flashing option. In the browser, use Chrome or Edge on a computer, with a secure context and Web Serial support.
6. Add the discovered device in **Settings → Devices & services → ESPHome**.

After the first install, and with the network working, many updates can be sent over Wi-Fi. The exact path depends on the board and the configuration.

## Do I need to know how to code?

You don't need to start by writing C++. ESPHome uses **YAML**, a file that describes the components and what they should do. The wizard builds the base; ready-made projects save a lot of work. Custom sensors and screens may still require editing that file.

An **AI can be a good tutor**: explaining each part, adapting an example and helping you interpret errors. A useful request is:

> "I have this ESP32 board and this sensor. Use the current ESPHome documentation, explain the connections and propose a minimal configuration. Don't invent pins; tell me what I need to confirm."

State the exact model and don't include real passwords in the request. Compare the answer with the documentation, use **Validate** and test one component at a time. A configuration that compiles still has to match the physical wiring.

## Voice with ESP32

With a compatible microphone, speaker and configuration, an ESP32 device can act as a voice point for **Assist**. The [official ATOM Echo tutorial](https://www.home-assistant.io/voice_control/thirteen-usd-voice-remote/) offers browser-based installation.

The board captures and plays back audio; recognition and the response can use local processing on the system or cloud services, depending on the configuration. You don't have to start with voice: a scene button is usually a simpler project.

## Your first project

Start with a **temperature sensor or a button powered over USB**, at low voltage. Once it shows up in Home Assistant, create the automation from the visual editor. Projects wired to mains power require suitable components and installation by a qualified professional.

## Ready-made examples to copy

I've put together a gallery of **complete ESPHome configurations** — a Bluetooth scale, a Bluetooth Proxy, an IR receiver, Thread devices and displays — ready to copy and adapt to your Home Assistant: the **[ESPHome examples gallery](/en/esphome-examples/)**.

[Back to Home Assistant](/en/home-assistant/).

Sources: [getting started with ESPHome](https://esphome.io/install/getting-started/), [install ESPHome](https://esphome.io/install/), [ESP32-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [ATOM-S3](https://docs.m5stack.com/en/core/AtomS3) and [Nabu Casa and the Open Home Foundation](https://www.nabucasa.com/).
