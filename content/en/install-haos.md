---
title: "Home Assistant OS: choose your installation"
slug: install-haos
key: instalar-haos
description: Green, Raspberry Pi 5 or mini PC: which to choose, what to prepare, what happens on first access, what to do when the address does not open, and the next steps.
category: Guided installation
icon: book
order: 3
featured: true
level: basico
section: artigo
reading: 7 min read
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

**Home Assistant OS (HAOS)** is the system that looks after the hub, its updates and the Apps. Pick **only the guide for your hardware**: each one takes you from preparation to the first working Zigbee sensor. The three illustrated guides are in Portuguese; the screenshots are from the English interface.

## Which hardware are you installing on?

<div class="install-card-grid"><a class="install-card" href="/instalar-green/"><img src="/static/img/hardware/green.webp" width="800" height="533" alt="Home Assistant Green" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">01 / Ready to plug in</span><h3>Home Assistant Green</h3><span class="install-card-description">Connect network and power. Create your account and add the ZBT-2 through the screens.</span><span class="install-card-cta">Step-by-step guide (PT) →</span></span></a><a class="install-card" href="/instalar-raspberry-pi-5/"><img src="/static/img/devices/raspberry-pi-5-case.jpg" width="800" height="535" alt="Raspberry Pi 5 + NVMe" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">02 / Build your hub</span><h3>Raspberry Pi 5 + NVMe</h3><span class="install-card-description">Choose board, case and SSD. Prepare the NVMe on a Mac or PC and install HAOS.</span><span class="install-card-cta">Step-by-step guide (PT) →</span></span></a><a class="install-card" href="/instalar-mini-pc/"><img src="/static/img/hardware/n150.webp" width="800" height="800" alt="x86-64 mini PC" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">03 / Intel or AMD</span><h3>x86-64 mini PC</h3><span class="install-card-description">Prepare the USB stick and write HAOS to the internal SSD, with a visual walkthrough.</span><span class="install-card-cta">Step-by-step guide (PT) →</span></span></a></div>

Not bought yet? [Compare the hardware, photos and prices](/#hardware-haos) (in Portuguese).

## How to choose between the three

| | Home Assistant Green | Raspberry Pi 5 + NVMe | x86-64 mini PC |
|---|---|---|---|
| **For whom** | Wants to plug in and use, without writing anything. | Likes building and wants a compact, cheaper setup. | Wants headroom for cameras, local AI, virtual machines and many Apps. |
| **Preparation** | None: HAOS comes pre-installed. | Write HAOS to the NVMe SSD with Raspberry Pi Imager on a computer. | Create an installer USB stick and write HAOS to the internal SSD. |
| **Performance** | Enough for Zigbee, automations and a few Apps. | Good; the NVMe SSD makes a real difference over a microSD card. | The highest of the three; room for Frigate, Scrypted and AI models. |
| **Power and noise** | Very low, fanless. | Low; the case fan can be audible. | Low to medium; most have a fan. |
| **Storage** | 32 GB internal eMMC. | The NVMe SSD you choose. | Internal SSD, usually 256 GB or more. |
| **Backup and replacement** | HAOS backups; closed hardware. | Easy to swap SSD or board. | Easy to swap SSD and memory. |

When in doubt, the **Green** is the safest choice for anyone who only wants lights, sensors and automations; the **mini PC** is the choice for those who already know cameras with image analysis are coming. In the [author's home](/minha-instalacao/) the hub is a mini PC with a Ryzen 7 processor, precisely because the house has cameras and an ESPHome display besides the lights.

## Before you start, have ready

- A **network cable** to the router. The hub should be on Ethernet.
- A stable power outlet. If power cuts are frequent, a small UPS prevents storage corruption.
- **Another computer** on the same network, with an up-to-date browser, to write the system (Pi and mini PC) and for the first access.
- For the Pi and the mini PC: a **USB stick of 8 GB or more**, which will be erased, and the target **SSD**, which will also be erased.
- The **ZBT-2** and a short **USB extension cable**, for after the installation.

## What the three paths have in common

1. The hub stays connected to power and to the network over **Ethernet**.
2. You configure it from the browser of **another computer** on the same network, at [http://homeassistant.local:8123](http://homeassistant.local:8123).
3. You create your account and get to know the dashboard.
4. You connect the **ZBT-2 to the hub** and set up **ZHA through the screens**.
5. You add a light or a sensor and make the first backup.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Enlarge: The same first-access screen on the Green, Pi or mini PC."><img src="/static/img/ha-guide/onboarding.png" alt="The same first-access screen on the Green, Pi or mini PC." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>The same first-access screen on the Green, Pi or mini PC. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Official screenshot · Home Assistant</a> <span>Names may vary by version. Tap to enlarge.</span><a href="/static/img/ha-guide/README.md">Image credits</a></figcaption></figure>

The Green comes ready. On the Pi and the mini PC, writing the image erases the chosen media: double-check the target and save your files first. For this path you do not need a terminal, Proxmox or virtual machines.

## What happens on first access

1. On the first boot, HAOS downloads and prepares the Home Assistant components. The "Preparing Home Assistant" screen can take **up to 20 minutes**, according to the official documentation. Do not switch the hub off during that time.
2. The welcome screen follows. Create the **owner user** (name, username and password). Keep the password safe: there is no email recovery.
3. Enter the **home name, location, time zone and units**. The location defines the sunset time used by the first automation, so place the pin accurately on the map.
4. Decide whether to share anonymous usage data with the project. It is optional.
5. Home Assistant shows the devices it has already discovered on the network, such as TVs, printers or a Philips Hue bridge. You can set them up now or later.

## If the address does not open

- **`homeassistant.local` does not resolve.** Some routers and older Windows versions do not understand that kind of name. Open the router's admin page, find the device called `homeassistant` in the connected-devices list and use its IP address, for example `http://192.168.1.50:8123`.
- **The page loads forever.** Wait out the initial 20 minutes. Beyond that, plug a monitor into the hub (Pi and mini PC) and check for the `ha >` prompt; if it is there, the system is up and the problem is the network.
- **Certificate error or "connection not secure".** First access is over `http://`, without the `s`. Some browsers force `https://`; type the full address.
- **No network after writing the image on the mini PC.** Check in the BIOS that the computer boots from the internal SSD, not the USB stick, and that the cable is in the right port.

## Right after installing

1. **Update.** Settings → System → Updates. HAOS, the Supervisor and Core update separately; apply whatever is pending.
2. **Reserve the hub's IP address** on the router (DHCP reservation). It never changes, and the phone app and integrations keep finding the hub.
3. **Make the first backup** under Settings → System → Backups and keep the encryption key. Enable weekly automatic backups with a copy outside the hub.
4. **Install the companion app** on your phone and sign in with the same user.
5. Connect the **ZBT-2** through the USB extension and follow the [ZBT-2 with ZHA](/en/zbt-dongles/) guide.

## What HAOS handles for you

Home Assistant OS includes the **Supervisor**, which manages updates, backups and the **App store** (Mosquitto, ESPHome, Matter Server, Studio Code Server and others). Other installation methods, such as Container or a virtual machine, exist and are described in [Further learning](/aprofundamento/) (in Portuguese), but they hand that maintenance over to you. For a first home, HAOS is the path with the least friction.

After installing, [understand the Zigbee network](/en/zigbee/) and [create your first automation](/primeira-automacao/) (in Portuguese).

Sources: [official installation](https://www.home-assistant.io/installation/), [onboarding](https://www.home-assistant.io/getting-started/onboarding/) and [Home Assistant Green](https://www.home-assistant.io/green/).
