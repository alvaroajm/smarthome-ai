---
title: "ZBT-2 and ZHA: connect your first device"
slug: zbt-dongles
key: zbt-dongles
description: ZBT-1 and ZBT-2 compared, how to connect the adapter to the hub, set up ZHA through the screens and pair your first Zigbee bulb or sensor.
category: Step by step
icon: book
order: 6
featured: true
level: basico
section: artigo
reading: 8 min read
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

You need **HAOS up and running**, a **Home Assistant Connect ZBT-2** and a compatible Zigbee light or sensor.

The **ZBT-2 is the USB radio**. **ZHA is the integration included in Home Assistant** that organises the network. No extra App is needed.

## ZBT-1 or ZBT-2?

Both are official adapters from the Home Assistant team (Nabu Casa) and work with ZHA. If you are still buying, the ZBT-2 is the current one; if you already have a ZBT-1 (previously sold as SkyConnect), it serves this path just as well.

| | ZBT-1 (formerly SkyConnect) | ZBT-2 |
|---|---|---|
| **Radio chip** | Silicon Labs EFR32MG21 | Silicon Labs MG24, with an ESP32-S3 for the USB link |
| **Antenna** | Internal | External, hinged, can be aimed |
| **Connector** | USB-A, extension cable included | USB-C, cable included |
| **Protocols** | Zigbee or Thread (one at a time) | Zigbee or Thread (one at a time) |
| **Range** | Good | Better, thanks to the external antenna |

Neither runs Zigbee and Thread at the same time: multiprotocol mode was discontinued. On this path, the adapter stays in Zigbee mode.

## 1. Connect the ZBT-2

Fit the antenna as the manual shows and use the supplied USB cable to connect it to the hub. Keep it upright, away from the computer, the router and metal surfaces.

!!! dica "USB extension and a USB 2.0 port"
    USB 3.0 ports and drives generate interference in the 2.4 GHz band, the same one Zigbee uses. Use the included extension cable (or one of 30 cm to 1 m) and, if the hub has one, prefer a USB 2.0 port, usually the black one. An adapter sitting against the hub is a frequent cause of failed pairings and sensors that "vanish" for no reason.

### Before the first pairing: the channel

Zigbee and Wi-Fi share the 2.4 GHz band. ZHA picks the channel automatically on the recommended installation, and for most homes that is enough. If your router uses Wi-Fi channel 1, Zigbee channels 15, 20 or 25 are freer; if it uses 11, channel 15 is the safe option. Decide this before pairing the first device: changing the channel later means pairing everything again.

## 2. Open the discovered device

Go to **Settings → Devices & services**. On the Connect ZBT-2 card, select **Add**.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-discovery.png" target="_blank" rel="noopener" aria-label="Enlarge: Home Assistant detects the Connect ZBT-2 plugged in over USB."><img src="/static/img/ha-guide/zbt-discovery.png" alt="Home Assistant detects the Connect ZBT-2 plugged in over USB." width="350" height="230" loading="lazy" decoding="async"></a><figcaption>Home Assistant detects the Connect ZBT-2 plugged in over USB. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Official screenshot · Nabu Casa</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

## 3. Choose Zigbee and the recommended installation

In the wizard, select **Use as Zigbee adapter**. Then choose **Recommended installation**. That option sets up ZHA.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Enlarge: On this path, choose Zigbee."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="On this path, choose Zigbee." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>On this path, choose Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Official screenshot · Nabu Casa</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

Follow the prompts to the end and assign the adapter to a room. Do not choose Thread for this network.

## 4. Add the first light or sensor

Under **Settings → Devices & services**, open **Zigbee Home Automation** and click **Add device**.

Put the device into pairing mode as the manufacturer's manual describes. For bulbs it is usually switching the power on and off five or six times; for sensors, holding the reset button for a few seconds until the LED blinks. Wait for discovery, give it a name such as "Living room light" and choose the room.

### The right order: routers first, batteries later

Mains-powered devices (bulbs, wall switches, plugs) are **routers**: besides doing their job, they relay messages and extend the network. Battery devices (door, motion and temperature sensors, buttons) are **end devices**: they only talk to the nearest router and relay nothing.

So pair the mains devices first, from the room closest to the adapter to the farthest, and only then the battery ones, each near the router it will use. A sensor paired next to the adapter and then carried to the garage will drop off, because it keeps the old route.

A home with three or four well-spread routers (a Zigbee bulb or plug in each important room) has a far more stable network than one with a powerful adapter and ten battery sensors. In [my home](/minha-instalacao/) (in Portuguese), I use Zemismart Zigbee wall switches to control the lights; repeater support needs to be checked for the exact model.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Enlarge: Use Add device to search for devices in pairing mode."><img src="/static/img/ha-guide/zha-add.png" alt="Use Add device to search for devices in pairing mode." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Add device to search for devices in pairing mode. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Official screenshot · Nabu Casa</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

## 5. Test before moving on

Open the device and use the light control. If it is a contact sensor, open and close the door and watch the state change. Do this test where the device will actually be used.

<details><summary>The device did not show up?</summary><p>Check pairing mode, the battery and the model's support in ZHA. If it was on another hub, follow the manufacturer's reset procedure. If the ZBT-2 itself is not detected, check the cable, the USB connection and Home Assistant updates; consult official support before changing settings.</p></details>

## Common problems and what to check

| Symptom | Most likely cause | What to do |
|---|---|---|
| The bulb does not appear while pairing | Still paired to another hub (Hue bridge, Tuya app) or the reset was not completed | Factory-reset it per the manual and try again within 3 m of the adapter |
| Pairs, but shows as "unknown" with few functions | Model without full ZHA support | Look up the exact model in the community; see [Zigbee2MQTT or ZHA](/zigbee2mqtt/) (PT) |
| A battery sensor disappears after a few days | Paired far from the router it uses, or no routers along the way | Pair it again in its final place; add a Zigbee bulb or plug in that room |
| Several devices drop at once | Interference: adapter next to USB 3.0, an external SSD or the Wi-Fi router | USB extension, USB 2.0 port, move away from the router |
| Bulb "unavailable" | Someone switched off the ordinary wall switch | Leave the switch on or replace it with a Zigbee switch |
| Commands lag or fail at peak hours | Zigbee channel overlapping Wi-Fi | Check the Wi-Fi channel; changing the Zigbee channel means pairing everything again |

## Backing up the Zigbee network

ZHA makes automatic backups of the network (keys, channel and coordinator identity) and includes them in the Home Assistant backup. That lets you replace the adapter with another of the same type, or restore the hub on new hardware, without pairing everything again. Once the first bulb works, make a full backup under **Settings → System → Backups** and keep a copy outside the hub.

[Now create an automation in the visual editor](/primeira-automacao/) (in Portuguese).

Already using a ZBT-1? You do not need to replace it just to follow this guide. Zigbee2MQTT is an alternative covered in [further learning](/zigbee2mqtt/) (in Portuguese).

Sources: [official ZBT-2 wizard](https://support.nabucasa.com/hc/en-us/articles/29400591254301) and [ZHA](https://www.home-assistant.io/integrations/zha/).
