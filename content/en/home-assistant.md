---
title: What is Home Assistant?
slug: home-assistant
key: home-assistant
description: Discover automations, voice, apps, brands, ESPHome and cameras in a connected home with Home Assistant — what the hub does and why it is the centre of this site.
category: Step by step
icon: book
order: 2
featured: true
level: basico
section: artigo
reading: 9 min read
date: 2026-09-23
updated: 2026-10-21
tags: [Home Assistant]
---

Imagine saying **"movie time"** and watching the TV turn on, the curtains close and the lights take on the colour you chose. Or walking into the hallway at night and finding a soft light that stays on only while you need it.

**Home Assistant** brings compatible devices together and turns those ideas into controls, scenes and automations. It is free, open source and prioritises local control. **Home Assistant OS (HAOS)** takes care of installation, updates and Apps: it is the path this guide follows.

## One dashboard for the whole house

Lights, TVs, air conditioners, fans, thermostats, switches, plugs, curtains and alarms can all appear on the same dashboard. You choose the rooms, the controls and the information that make sense for your family.

<figure class="ha-screen"><a href="/static/img/ha-guide/dashboard.png" target="_blank" rel="noopener" aria-label="Enlarge: A real Home Assistant dashboard, organised by room."><img src="/static/img/ha-guide/dashboard.png" alt="A real Home Assistant dashboard, organised by room." width="1701" height="1299" loading="lazy" decoding="async"></a><figcaption>A real Home Assistant dashboard, organised by room. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding_dashboard/" target="_blank" rel="noopener">Official screenshot · Home Assistant</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

**RGBCCT** combines RGB colours with adjustable white temperature. A compatible bulb or strip can give you white light for working, a warm tone for dinner and colours for a movie night. Brightness and features depend on the product.

You control it from the browser, the phone, by voice or through automations. A command to an air conditioner can go through a network integration or a compatible infrared blaster; in the latter case, there is not always confirmation of the appliance's real state.

## Brands talk to each other through Home Assistant

The official catalogue lists **more than 1,500 integrations**. They connect brands, devices and services; nothing has to come from the same manufacturer.

<div class="ha-brand-list" aria-label="Integration examples"><a href="https://www.home-assistant.io/integrations/webostv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/lg.png" width="537" height="256" alt="" loading="lazy" decoding="async"></span><strong>LG</strong><span class="manufacturer-description">TVs and connected appliances.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/samsungtv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/samsung.png" width="1150" height="256" alt="" loading="lazy" decoding="async"></span><strong>Samsung</strong><span class="manufacturer-description">TVs and devices from the SmartThings ecosystem.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/tuya/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/tuya.png" width="512" height="256" alt="" loading="lazy" decoding="async"></span><strong>Tuya / Smart Life</strong><span class="manufacturer-description">The platform behind many Smart Life products.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/zha/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/aqara.png" width="881" height="256" alt="" loading="lazy" decoding="async"></span><strong>Aqara</strong><span class="manufacturer-description">Sensors, buttons, curtains and other accessories.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/braviatv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/sony.png" width="1465" height="256" alt="" loading="lazy" decoding="async"></span><strong>Sony</strong><span class="manufacturer-description">Bravia TVs to complete the movie scene.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/homekit_controller/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/eve.png" width="666" height="256" alt="" loading="lazy" decoding="async"></span><strong>Eve</strong><span class="manufacturer-description">Sensors, plugs and home accessories.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/tplink/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/tapo.png" width="646" height="256" alt="" loading="lazy" decoding="async"></span><strong>Tapo / TP-Link</strong><span class="manufacturer-description">Connected plugs, lighting and cameras.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/reolink/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/reolink.png" width="1166" height="256" alt="" loading="lazy" decoding="async"></span><strong>Reolink</strong><span class="manufacturer-description">Cameras and network video recorders.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/onvif/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/intelbras.png" width="1248" height="256" alt="" loading="lazy" decoding="async"></span><strong>Intelbras</strong><span class="manufacturer-description">Security cameras; check for ONVIF or RTSP.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/hue/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/hue.png" width="653" height="256" alt="" loading="lazy" decoding="async"></span><strong>Philips Hue</strong><span class="manufacturer-description">Bulbs, strips and lamps to set the mood.</span><span class="manufacturer-cta">View integration ↗</span></a><a href="https://www.home-assistant.io/integrations/epson/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/epson.png" width="957" height="256" alt="" loading="lazy" decoding="async"></span><strong>Epson</strong><span class="manufacturer-description">Compatible projectors for your home cinema.</span><span class="manufacturer-cta">View integration ↗</span></a></div>
<aside class="hue-explainer"><h4>Philips Hue: light sets the mood too.</h4><p>Hue is a smart-lighting line: bulbs, LED strips and lamps. Depending on the model, you adjust brightness, warm or cool white, and colours. A scene combines those settings — soft light for dinner, coloured tones for the movie.</p><p>The Hue Bridge is the brand's hub. Home Assistant talks to it locally to control lights and scenes. Another option is to pair compatible Zigbee bulbs directly with ZHA + ZBT-2; in that case, the available features may change.</p><a class="ext" href="https://www.philips-hue.com/en-us/explore-hue" target="_blank" rel="noopener">Explore Philips Hue</a></aside>
<details class="feature-details"><summary>How does each brand connect?</summary><ul class="ha-brand-notes"><li><strong>LG</strong><span>webOS TVs with local control; ThinQ appliances use another, cloud-based integration.</span></li><li><strong>Samsung</strong><span>Compatible TVs over the local network; other devices may use SmartThings, in the cloud.</span></li><li><strong>Tuya / Smart Life</strong><span>The official integration uses the cloud. Compatible Zigbee devices can join ZHA directly.</span></li><li><strong>Aqara</strong><span>Compatible Zigbee sensors through ZHA; Matter or HomeKit products take another route.</span></li><li><strong>Sony</strong><span>Compatible Bravia TVs: volume, inputs and playback, depending on the model.</span></li><li><strong>Eve</strong><span>HomeKit accessories through HomeKit Device; Matter versions through the Matter integration.</span></li><li><strong>Tapo / TP-Link</strong><span>Supported plugs, switches, lights and cameras; check the list and the authentication.</span></li><li><strong>Reolink</strong><span>Local video and events on supported models; battery devices have their own requirements.</span></li><li><strong>Intelbras</strong><span>Cameras with compatible ONVIF Profile S or an RTSP stream. Not the whole line offers these.</span></li><li><strong>Philips Hue</strong><span>Local lights and scenes through the Hue Bridge. Compatible Zigbee bulbs can also use ZHA.</span></li><li><strong>Epson</strong><span>Compatible network projectors: power and input selection for the movie scene.</span></li></ul><p>Before buying, check the model, firmware and available functions. One integration can serve several brands; one brand can use several integrations.</p></details><p class="feature-small"><a href="/static/img/manufacturers/README.md">Logo credits</a> · Trademarks belong to their owners. Examples only, no official affiliation.</p>

An LG TV, an Aqara sensor and a Philips Hue light can take part in the same automation. Compatibility is about the **model and the function**, not just the brand. LG webOS and Samsung TVs have local options; [LG ThinQ](https://www.home-assistant.io/integrations/lg_thinq/) and [SmartThings](https://www.home-assistant.io/integrations/smartthings/) use the cloud in their respective integrations.

## Light scenes: the same room, six moods

Once the bulbs are chosen, what truly changes the house are the **scenes**. Hover or tap the images to see each room in motion; click to switch the lighting from loud RGB to daylight white, reading, morning, sunset and night light.

{{scenes_showcase}}

## Automations: the fun part

Think of three questions: **when does it happen, under which conditions, and what should be done?** The visual editor organises exactly that.

- **On arrival:** turn on the entrance light if it is already dark.
- **When a window opens:** pause the climate control, if the integration allows it.
- **At dusk:** close the curtains and choose cosy lighting.
- **When someone is at the gate:** send a notification with an image, using a compatible camera or NVR.
- **On leaving:** warn if any door or window was left open.

<figure class="ha-screen"><a href="/static/img/ha-guide/automation.png" target="_blank" rel="noopener" aria-label="Enlarge: Visual editor: choose the trigger, the conditions and the action."><img src="/static/img/ha-guide/automation.png" alt="Visual editor: choose the trigger, the conditions and the action." width="1021" height="586" loading="lazy" decoding="async"></a><figcaption>Visual editor: choose the trigger, the conditions and the action. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Official screenshot · Home Assistant</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

A **scene** stores desired states, such as the lights and curtains for the movie. An **automation** decides when to apply those states. You can create both through the screens. **Blueprints** are reusable templates for certain automations: pick a trusted one and fill in the devices it asks for.

[Create your first automation without code](/primeira-automacao/) (in Portuguese).

## Alexa, Google Nest and Assist: you can talk

You can use **Alexa on an Echo** or **Google Assistant on a Google Nest** to operate the devices and scenes you expose. Home Assistant Cloud, by Nabu Casa, simplifies that connection. These services depend on the internet and have their own limits on device types and commands.

**Assist** is Home Assistant's own voice assistant. It works on the phone and on dedicated hardware. With suitable processing power, language and hardware, it can run locally; it can also use the voice services of Home Assistant Cloud.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/voice-pe.webp" target="_blank" rel="noopener" aria-label="Enlarge: Home Assistant Voice Preview Edition next to the Green."><img src="/static/img/ha-features/voice-pe.webp" width="360" height="360" alt="Home Assistant Voice Preview Edition next to the Green." loading="lazy" decoding="async"></a><figcaption>Home Assistant Voice Preview Edition next to the Green. · <a class="ext" href="https://www.home-assistant.io/voice-pe/" target="_blank" rel="noopener">Official image</a></figcaption></figure>

There are also voice satellites built with **ESP32 and ESPHome**, such as the ATOM Echo. They capture your speech and forward it to Home Assistant. An ordinary ESP32 board needs the right audio components; the ATOM-S3 with a screen is not, by itself, that kit.

## The app in your pocket, the house within reach

The **Home Assistant Companion** app, for iOS and Android, shows your dashboard and can receive alerts. On an iPhone, iPad or Android you check sensors, control devices and watch the integrated cameras.

With your permission, the phone can also report location and other sensors for automations. At home, the connection can be local. Away from home, you need a configured remote-access path, such as **Home Assistant Cloud or a VPN**. The app does not replace the hub that stays on at home.

## Nabu Casa: convenience and support for the project

The optional **Home Assistant Cloud** subscription offers encrypted remote access without opening router ports, an easier connection to Alexa and Google, cloud backup and voice processing for Assist.

Nabu Casa is the commercial partner of the **Open Home Foundation**, the organisation behind the Home Assistant and ESPHome projects. The subscription helps fund that development. You can use local automations without subscribing.

[See the benefits and the setup screens](/nabu-casa/) (in Portuguese).

## What about Apple Home fans?

The Apple Home / HomeKit ecosystem is more closed, with its own compatibility criteria. The **HomeKit Bridge** integration brings supported Home Assistant functions to the Home app and Siri, including devices without native HomeKit support.

You choose what to share. Not every feature has an equivalent in the Home app. For remote access through it, you need a compatible Apple home hub, such as a HomePod or Apple TV. Matter accessories widen interoperability.

[Connect Home Assistant to the Home app](/apple-homekit/) (in Portuguese).

## IoT and DIY: build what is missing

**IoT** is the internet of things: connected objects exchanging information, including inside your local network. **DIY** is doing it yourself. An ESP32 board can become a temperature sensor, a scene button or a small wall panel.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/esp32.webp" target="_blank" rel="noopener" aria-label="Enlarge: ESP32-DevKitC: a general-purpose development board, with components labelled."><img src="/static/img/ha-features/esp32.webp" width="900" height="389" alt="ESP32-DevKitC: a general-purpose development board, with components labelled." loading="lazy" decoding="async"></a><figcaption>ESP32-DevKitC: a general-purpose development board, with components labelled. · <a class="ext" href="https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html" target="_blank" rel="noopener">Official image</a></figcaption></figure>
<figure class="feature-figure feature-product"><a href="/static/img/ha-features/atom-s3.webp" target="_blank" rel="noopener" aria-label="Enlarge: M5Stack ATOM-S3: a compact option with a screen and a button."><img src="/static/img/ha-features/atom-s3.webp" width="800" height="800" alt="M5Stack ATOM-S3: a compact option with a screen and a button." loading="lazy" decoding="async"></a><figcaption>M5Stack ATOM-S3: a compact option with a screen and a button. · <a class="ext" href="https://docs.m5stack.com/en/core/AtomS3" target="_blank" rel="noopener">Official image</a></figcaption></figure>

**ESPHome**, an Open Home Foundation project supported by Nabu Casa, provides the **Device Builder** App on HAOS. The wizard creates an initial configuration. Ready-made projects help you get started; customisation usually means YAML, a description of the device, without writing a C++ program.

An AI assistant can explain the options, propose a configuration and help you understand errors. That makes learning more accessible, but you still need to check the board, the pins and the documentation, and validate before flashing. Start with a USB-powered, low-voltage project.

[Meet ESPHome through the screens](/en/esphome-esp32/). There you'll find **ready-made examples to copy**: a [scale in Home Assistant over Bluetooth](/en/esphome-examples/#example-scale), a [Bluetooth Proxy with the ATOM-S3](/en/esphome-examples/#example-bt-proxy), an [infrared receiver](/en/esphome-examples/#example-ir), a [Thread device (NanoC6)](/en/esphome-examples/#example-thread), a [touchscreen panel (weather & controls)](/en/esphome-examples/#example-display) a [Thread display with temperature/humidity (C6-GEEK)](/en/esphome-examples/#example-c6geek) and a [7" wall panel for the whole home (Waveshare 7B)](/en/esphome-examples/#example-panel7b).

## Cameras that help you understand what is going on

Seeing the image on the dashboard is already useful. An **NVR**, a system that records and organises the video, adds history and events. Frigate can detect people, cars and animals depending on the AI model, and feed events to Home Assistant.

<figure class="feature-figure"><a href="/static/img/ha-features/frigate-live.webp" target="_blank" rel="noopener" aria-label="Enlarge: Official Frigate NVR screen with several cameras."><img src="/static/img/ha-features/frigate-live.webp" width="1400" height="786" alt="Official Frigate NVR screen with several cameras." loading="lazy" decoding="async"></a><figcaption>Official Frigate NVR screen with several cameras. · <a class="ext" href="https://frigate.video/" target="_blank" rel="noopener">Official image</a></figcaption></figure>

Face recognition compares faces against a registered library and can run locally on compatible hardware. Vision models can describe actions, such as someone leaving a box, using local or cloud processing depending on the provider.

These features are extras, require configuration and can make mistakes. Use them to enrich notifications; do not let them decide on their own to unlock doors or disarm alarms. Recording and analysing several cameras needs properly sized storage and processing.

[See the next steps for cameras and AI](/cameras-ia/) (in Portuguese).

## Local, remote and automatic: each in its place

**Local:** with local devices and integrations, the rules keep running without the internet, as long as the hub, the network and the devices are powered. Cloud integrations still depend on external services.

**Remote:** you reach the hub from outside through a configured, protected connection. That usually requires internet on both ends.

**Automatic:** sensors, schedules and events start rules on the hub without you opening the app.

**Zigbee and Thread** are especially interesting for battery sensors: low power and a mesh network. Suitable devices can repeat the signal. They need a proper hub or border router; Wi-Fi and Ethernet remain useful for cameras, TVs and heavier traffic. We will cover this later, starting with **ZHA + ZBT-2**.

## Take the first step

You do not have to do all of this today. Choose a hub, connect one light and create one rule. The best part is growing at your own pace.

[Choose the hardware](/#hardware-haos) · [Install HAOS](/en/install-haos/) · [Understand Zigbee](/en/zigbee/).

References: [integration catalogue](https://www.home-assistant.io/integrations/), [automations](https://www.home-assistant.io/getting-started/automation/), [scenes](https://www.home-assistant.io/docs/scene/), [Assist](https://www.home-assistant.io/voice_control/), [apps](https://companion.home-assistant.io/), [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/), [Nabu Casa](https://www.nabucasa.com/), [ESPHome](https://esphome.io/install/getting-started/) and [Frigate](https://docs.frigate.video/).
