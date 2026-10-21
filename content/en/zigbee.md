---
title: "Zigbee: the basics for lights and sensors"
slug: zigbee
key: zigbee
description: How Zigbee connects lights and sensors without Wi-Fi: coordinator, routers, battery devices, channels, range and what to check before buying.
category: Step by step
icon: book
order: 4
featured: true
level: basico
section: artigo
reading: 5 min read
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

**Zigbee** is a wireless connection used by sensors, bulbs, plugs and buttons. The devices talk on a network of their own; they do not join your Wi-Fi individually.

<div class="zigbee-story"><div class="zigbee-intro"><p>Think of a radio conversation: the sensor says "the door opened" and Home Assistant can turn on a light. Zigbee is the standard used in that conversation. It uses very little energy and is great for small messages — not for streaming video.</p><p>Wi-Fi keeps serving your phone and other devices. Zigbee devices use a separate network that can work without the internet.</p></div>
<div class="zigbee-coordinator"><figure><img src="/static/img/zigbee-guide/zbt-2.webp" width="675" height="450" alt="Home Assistant Connect ZBT-2, with its base and vertical antenna, on a table." loading="lazy" decoding="async"><figcaption><a class="ext" href="https://www.home-assistant.io/connect/zbt-2/" target="_blank" rel="noopener">Official photo and product ↗</a></figcaption></figure><div><p class="eyebrow">The bridge to Home Assistant</p><h3>This is the ZBT-2.</h3><p>It is the Zigbee radio connected over USB to your HAOS hub. As the coordinator, it creates the network. ZHA, already included in Home Assistant, manages the devices through the screens.</p><p>You need one coordinator for the whole network, not one per sensor. Green, Raspberry Pi and mini PCs can all use the ZBT-2.</p></div></div>
<h3>Small devices, very practical jobs.</h3><div class="zigbee-products">
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/contact.avif" width="1600" height="1600" alt="SONOFF SNZB-04P — Door and window sensor" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Battery · end device</span><h4>Door and window sensor</h4><p>Reports when it opened or closed.</p><small>SONOFF SNZB-04P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-door-window-sensor-snzb-04p" target="_blank" rel="noopener">Official photo and product ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/motion.avif" width="1600" height="1600" alt="SONOFF SNZB-03P — Motion sensor" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Battery · end device</span><h4>Motion sensor</h4><p>Detects movement to turn on a light.</p><small>SONOFF SNZB-03P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-motion-sensor-snzb-03p" target="_blank" rel="noopener">Official photo and product ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/button.png" width="1600" height="1600" alt="SONOFF SNZB-01P — Wireless button" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Battery · end device</span><h4>Wireless button</h4><p>One press can call a scene.</p><small>SONOFF SNZB-01P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-wireless-switch-snzb-01p" target="_blank" rel="noopener">Official photo and product ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/switch.avif" width="1600" height="1600" alt="SONOFF ZBMINIR2 — In-wall switch module" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Mains power · router</span><h4>In-wall switch module</h4><p>Controls the light and also repeats the signal.</p><small>SONOFF ZBMINIR2</small><a class="ext" href="https://sonoff.tech/en-us/products/sonoff-zbmini-extreme-zigbee-smart-switch-zbminir2" target="_blank" rel="noopener">Official photo and product ↗</a></figcaption></figure>
</div><p class="feature-small">These are examples: check the model's functions in ZHA. The ZBMINIR2 needs a neutral wire and installation by an electrician; the sensors and the button run on batteries.</p>
<figure class="zigbee-mesh"><figcaption><p class="eyebrow">A simple network, inside the house</p><h3>Who talks to whom?</h3><p>Devices that repeat the signal help messages travel further. That forms a mesh network.</p></figcaption>
<div class="mesh-hub"><div class="mesh-node mesh-server"><strong>Home Assistant OS</strong><span>ZHA manages the network</span></div><span class="mesh-usb">↔ USB ↔</span><div class="mesh-node mesh-coordinator"><strong>ZBT-2</strong><span>Coordinator · creates the network</span></div></div>
<div class="mesh-radio-link"><span>Zigbee · wireless communication</span></div>
<div class="mesh-branches">
<div class="mesh-branch"><div class="mesh-node mesh-router"><span class="mesh-kind">Router / repeater</span><strong>Zigbee plug¹</strong><span>Forwards messages</span></div><div class="mesh-stem" aria-hidden="true">↕</div><div class="mesh-node mesh-end"><span class="mesh-kind">End device</span><strong>Door sensor</strong><span>Sends "opened / closed"</span></div></div>
<div class="mesh-branch"><div class="mesh-node mesh-router"><span class="mesh-kind">Router / repeater</span><strong>ZBMINIR2 switch</strong><span>Controls and forwards messages</span></div><div class="mesh-stem" aria-hidden="true">↕</div><div class="mesh-node mesh-end"><span class="mesh-kind">End device</span><strong>Motion sensor</strong><span>Sends "motion detected"</span></div></div>
</div>
<p class="mesh-caption">Routers can also exchange messages with each other. A sensor may connect directly to the coordinator or to a router; the drawing shows only one example of paths.</p></figure>
<div class="zigbee-roles"><article><h4>Router: helps the neighbours</h4><p>Forwards messages from other devices. It must stay powered; here "router" is not your Wi-Fi router.¹ Not every mains-powered device repeats the signal: check the model.</p></article><article><h4>End device: minds its own job</h4><p>Sends and receives its own information without forwarding the neighbours' messages. Battery sensors and buttons are usually end devices: they save energy to last longer.</p></article></div>
<p class="feature-small">References: <a class="ext" href="https://www.home-assistant.io/integrations/zha/" target="_blank" rel="noopener">ZHA / Home Assistant</a> · <a href="/static/img/zigbee-guide/README.md">Photo credits</a></p></div>

## Why start with Zigbee?

- **Low power:** suits small, battery-powered sensors.
- **Plenty of choice:** devices in many categories from many manufacturers.
- **Local control:** with ZHA, communication with the hub happens inside the house.
- **A network that grows:** compatible mains-powered devices repeat the signal.

Those advantages make Zigbee a good choice for our first light and first sensors. Price, quality and features vary by model.

## What are the limitations?

A coordinator is required. Walls, metal and other 2.4 GHz equipment can interfere. Not every function of every manufacturer shows up in ZHA: check the model before buying.

A Zigbee device belongs to one network at a time. If it was on another hub, it usually needs to be put into reset/pairing mode as described in the manual.

## Channels, Wi-Fi and range

Zigbee and 2.4 GHz Wi-Fi share the same band. Zigbee channels 15, 20 and 25 sit between the common Wi-Fi channels 1, 6 and 11, so they are the usual safe picks; ZHA chooses a channel automatically on the recommended installation. Decide this before pairing the first device, because changing the channel later means pairing everything again.

Indoors, count on roughly 10 metres per hop through typical walls, less through concrete or metal. The cure for range is not a stronger coordinator but more routers: a mains-powered bulb, plug or switch in each important room. Keep the coordinator on a short USB extension, away from USB 3.0 ports and SSDs, which emit noise in the same band.

## What to check before buying

1. **The exact model**, not just the brand, in the ZHA community reports or the Zigbee2MQTT device list.
2. **Power source:** mains devices extend the network; battery devices do not.
3. **Neutral wire** for in-wall switches and modules; many homes have no neutral at the switch box.
4. **"Zigbee 3.0"** on the box, which means a device certified to the current standard.
5. **What the device exposes:** on/off only, or also brightness, colour temperature, energy, battery.

## What about Thread?

Thread is also a low-power network and can form a mesh. It is used by many Matter products, but needs a **Thread border router** to connect to the home network.

It is useful for devices shared between ecosystems. The downside, for a beginner, is one more requirement to check. Zigbee and Thread are different networks; a Zigbee sensor cannot join Thread.

First, [understand what Matter is](/matter-thread/) (in Portuguese). Then [set up ZBT-2 + ZHA through the screens](/en/zbt-dongles/).

There is an alternative, **Zigbee2MQTT**, covered in [further learning](/zigbee2mqtt/) (in Portuguese). It is not needed on this path.

Sources: [ZHA](https://www.home-assistant.io/integrations/zha/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/) and [Thread](https://www.home-assistant.io/integrations/thread/).
