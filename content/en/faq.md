---
title: Home Assistant, servers and protocols: questions and answers
slug: faq
key: faq
description: Answers about Home Assistant OS, Raspberry Pi, x86 mini PCs, Zigbee, ZHA, Zigbee2MQTT, Thread, Matter, Wi-Fi, backups and automations.
category: FAQ
icon: help
order: 2
section: pagina
reading: 12 min read
date: 2026-09-22
updated: 2026-10-09
tags: [FAQ, Home Assistant, HAOS, Zigbee, Thread, Matter]
level: basico
---

## Home Assistant and Home Assistant OS

### What is Home Assistant?

It is a home automation platform running on your own hub. It brings devices and services into dashboards and lets you create rules, such as turning on a light when a sensor detects motion.

### Are Home Assistant and HAOS the same thing?

No. Home Assistant is the automation software. Home Assistant OS, or HAOS, is the operating system prepared to run it, with management of updates, backups and additional apps.

### Do I need to code?

Not to start. You can add integrations, build dashboards and create automations through the interface. YAML and programming help with customization but are not prerequisites for your first light or sensor.

### Should I choose HAOS or Home Assistant Container?

HAOS is recommended for most users. Container suits people already managing Docker and the host system; services such as MQTT must be managed separately, without the HAOS Apps catalog.

### Does Home Assistant work without internet?

Local integrations can keep working while your hub and network have power. Services depending on external servers, remote notifications and access from outside your home may stop. Check how each integration communicates.

### Do I need a subscription?

Home Assistant is free and open source. Hardware and electricity have costs. Nabu Casa's optional Home Assistant Cloud offers conveniences such as remote access and voice assistant connections.

Sources: [installation types](https://www.home-assistant.io/installation/) and [remote access](https://www.home-assistant.io/docs/configuration/remote/). Continue with [the Home Assistant guide (PT)](/home-assistant/).

## Servers: Green, Raspberry Pi and x86

### What does server mean in a smart home?

It is the device keeping Home Assistant running: a ready-made hub, Raspberry Pi board or computer. It coordinates your automations; it does not need to be enterprise server hardware.

### What is the simplest way to start?

Home Assistant Green comes with HAOS installed. Connect network and power and follow onboarding. For Zigbee devices or your own Thread border router, you may still need to add a compatible radio.

### Can I use a Raspberry Pi?

Yes. The official HAOS path lists Raspberry Pi 4 or 5 with at least 2 GB RAM, suitable power and Ethernet. Consider storage, an enclosure and cooling before assembling your setup.

### Should I use microSD or SSD?

microSD is an official installation option: an A2 card with at least 32 GB. SSD is an alternative when the hardware and boot method support it. Keep backups outside the hub either way.

### What is an x86-64 mini PC?

It is a compact computer with a 64-bit Intel or AMD processor. HAOS provides an image for generic x86-64 hardware using UEFI boot. Check compatibility for the specific machine.

### Is a Raspberry Pi or mini PC better?

It depends on your workload and existing equipment. Consider storage, power supply, energy consumption, cooling and maintenance together. Cameras and video processing need a different assessment from simple sensors and automations.

### Does installing HAOS on a PC keep Windows?

Writing the image directly to the target disk erases that disk. To retain another operating system, consider HAOS in a virtual machine with suitable resources and properly configured radio access.

### Does the hub need to stay on all the time?

Yes, to run automations continuously. Turning it off stops functions depending on it. Choose equipment suited to continuous operation and prevent the host system from sleeping.

Sources: [Green and hardware options](https://www.home-assistant.io/faq/what-hardware-do-i-need/), [Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi/), [x86-64](https://www.home-assistant.io/installation/generic-x86-64/) and [virtual machines](https://www.home-assistant.io/installation/alternative/). Read the installation guides for [Green (PT)](/instalar-green/), [RPi 5 (PT)](/instalar-raspberry-pi-5/) and [mini PCs (PT)](/instalar-mini-pc/).

## Wi-Fi, Ethernet and choosing protocols

### Are Zigbee, Thread, Matter and Wi-Fi direct competitors?

They are not all at the same layer. Zigbee, Thread and Wi-Fi describe communication technologies; Matter defines how devices and platforms understand each other over IP networks such as Thread, Wi-Fi and Ethernet.

### Do I need one protocol for the whole house?

No. Home Assistant can bring different protocols together through appropriate integrations. A Wi-Fi light can participate in an automation with a Zigbee sensor without those devices communicating directly.

### Does every Wi-Fi device work with Home Assistant?

No. Wi-Fi only describes how it joins your network. Check the manufacturer's integration, exact model, available features and whether control depends on the cloud or works locally.

### Should the hub use Wi-Fi or Ethernet?

For this learning path, prefer Ethernet for the hub: it simplifies installation and removes one wireless dependency. Your smart devices do not all need cables. Available options depend on the hardware and installation.

### Can Wi-Fi interfere with Zigbee and Thread?

Yes, when using the 2.4 GHz band. Placement and channel planning help. Keep coordinators away from Wi-Fi routers, USB 3 and SSDs; changing channels without planning can create reconnection work.

Sources: [available integrations](https://www.home-assistant.io/integrations/), [Matter](https://www.home-assistant.io/integrations/matter/) and [Zigbee range and interference](https://www.zigbee2mqtt.io/advanced/zigbee/02_improve_network_range_and_stability.html). Continue with [your home network (PT)](/rede-wifi/).

## Zigbee: coordinators, mesh and compatibility

### What is Zigbee?

It is wireless technology widely used in lights, sensors, buttons and plugs. It forms its own low-power network for small control and measurement messages. It is not suitable for streaming camera video.

### Do I need a Zigbee coordinator?

To form a Zigbee network with ZHA or Zigbee2MQTT, yes. The coordinator is the radio starting and managing that network. A manufacturer's hub can form a separate network exposed through its own integration.

### How do coordinators, routers and end devices differ?

The coordinator manages the network. Routers forward messages through the mesh. End devices communicate through a parent device and are typically battery-powered sensors or controls.

### Does every plug or light repeat the Zigbee signal?

Many continuously powered devices act as routers, but exceptions exist. Check the model. Cutting power to a routing light may affect other devices using that path.

### Do different brands work together?

Often, but the Zigbee logo does not guarantee every feature. Check the model's support in ZHA or the Zigbee2MQTT catalog. Some devices need specific adaptations called quirks or converters.

### Can a device join two Zigbee networks simultaneously?

A typical Zigbee device belongs to one network at a time. Moving from a hub to another coordinator usually requires resetting and pairing again. This differs from Matter multi-admin sharing.

### Can I keep Hue Bridge while using ZHA or Z2M?

Yes, as separate networks. Hue Bridge devices stay on that bridge while others use another coordinator. Plan channels and use the Hue integration to bring control into Home Assistant.

### Does low LQI mean my device is faulty?

Not on its own. LQI indicates link quality, not a complete diagnosis. Observe lost messages, delays, routes, power and changes over time. Avoid deciding from one number alone.

Sources: [ZHA](https://www.home-assistant.io/integrations/zha/), [Zigbee networking](https://www.zigbee2mqtt.io/guide/configuration/zigbee-network.html), [Z2M device catalog](https://www.zigbee2mqtt.io/supported-devices/) and [Hue integration](https://www.home-assistant.io/integrations/hue/). Continue with [Zigbee in practice (PT)](/zigbee/).

## ZHA, Zigbee2MQTT and MQTT

### What is ZHA?

Zigbee Home Automation is Home Assistant's built-in Zigbee integration. It uses a compatible coordinator and keeps management in the Home Assistant interface without requiring an MQTT server.

### What is Zigbee2MQTT or Z2M?

It is a service managing a Zigbee network and exchanging messages with other applications over MQTT. It can integrate with Home Assistant and has its own interface and device catalog.

### Should I choose ZHA or Z2M?

Our beginner path uses ZHA. Consider Z2M when support for your specific devices or its features justify the additional services. Neither choice is universally better for every network.

### Can ZHA and Z2M use the same coordinator?

Not simultaneously. The radio must be dedicated to one of them. Separate solutions can use their own coordinators and networks; devices do not automatically move between networks.

### What is MQTT? Is it always required?

It is a messaging protocol using an intermediary server called a broker. Z2M needs it; ZHA does not. Install MQTT when an integration or device requires it, rather than treating it as a Home Assistant prerequisite.

### Does moving from ZHA to Z2M require pairing again?

Plan it as a network migration and check the procedure for the versions and adapters involved. Do not assume one solution accepts the other's backup. Preserve backups before changing the coordinator.

Sources: [ZHA](https://www.home-assistant.io/integrations/zha/), [starting with Z2M](https://www.zigbee2mqtt.io/guide/getting-started/), [Z2M adapters](https://www.zigbee2mqtt.io/guide/adapters/) and [MQTT](https://www.home-assistant.io/integrations/mqtt/). Read [when to consider Z2M (PT)](/zigbee2mqtt/) and [connection troubleshooting (PT)](/zigbee2mqtt-desconectando/).

## Thread and Matter

### Are Thread and Matter the same thing?

No. Thread is a low-power IPv6 network. Matter is a communication standard for devices and platforms; it can use Thread, Wi-Fi or Ethernet.

### What does a Thread border router do?

It connects the Thread mesh to your home's IP network. It is not a Zigbee coordinator or necessarily a Matter controller. One product may have multiple roles, depending on its model.

### Does Matter over Wi-Fi need a Thread border router?

No. A Thread border router is needed when the device uses Thread. Matter over Wi-Fi needs a Wi-Fi network and a compatible Matter controller.

### Can HomePod mini or Apple TV provide this function?

HomePod mini and certain Apple TV models support Thread. Check the exact model and configuration; not every Apple TV has a Thread radio. They do not replace a Zigbee coordinator.

### Do two border routers automatically form one Thread network?

No. They may create separate networks with different credentials. To cooperate in the same mesh, they must join the same Thread network. Discovering a border router in Home Assistant does not mean its credentials are known.

### Does ZBT-2 run Zigbee and Thread at the same time?

No. ZBT-2 uses one protocol at a time. For Zigbee and your own Thread border router, use dedicated radios or an existing compatible border router.

### Does Matter guarantee every feature and make any Zigbee device compatible?

No. Features depend on the category and platform support. A Zigbee device does not become Matter by joining Home Assistant; a specific Matter bridge may expose features from devices connected to it.

### Can I share a Matter device between Apple Home and Home Assistant?

With compatible devices and platforms, yes, using multi-admin. For an existing device, generate a sharing code in its current platform and follow the existing-device flow. This is different from resetting it.

### Does Matter need IPv6 from my internet provider?

It needs working IPv6 on your local network, not an IPv6 internet connection. Multicast and mDNS also matter. Guest networks, client isolation and incorrectly configured VLANs can block discovery and communication.

Sources: [Thread](https://www.home-assistant.io/integrations/thread/), [Matter](https://www.home-assistant.io/integrations/matter/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/) and [Apple TV models and specifications](https://support.apple.com/en-us/101605). Continue with [Thread and Matter explained (PT)](/matter-thread/).

## Integrations, Apps, HACS and ESPHome

### How do integrations, devices and entities differ?

An integration connects Home Assistant to a technology or service. A device represents the hardware. Entities represent its functions or information: a plug might have entities for switching, power and energy measurement.

### Are Apps and integrations the same thing?

No. Apps, previously called add-ons, are extra services installable on HAOS, such as an MQTT broker. Integrations connect services and devices to Home Assistant. An App may work alongside an integration.

### What is HACS? Is it mandatory?

HACS helps install community-maintained integrations and interface resources. It is optional and is not the HAOS Apps catalog. Check each project's documentation, maintenance and requirements before installing it.

### What is ESPHome? Does it require MQTT?

ESPHome lets you create firmware for supported microcontrollers, including many ESP32 boards. Its integration can communicate directly with Home Assistant through the native API. MQTT is optional for this connection.

### Can I keep Alexa, Google Home and Apple Home?

Yes, with appropriate integrations and configuration. HomeKit Bridge can expose compatible entities to Apple Home. Alexa and Google Assistant have their own options, including Home Assistant Cloud. Check dashboard control first.

Sources: [concepts](https://www.home-assistant.io/getting-started/concepts-terminology/), [Apps](https://www.home-assistant.io/apps/), [HACS](https://www.hacs.xyz/docs/use/), [ESPHome](https://www.home-assistant.io/integrations/esphome/) and [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/). Continue with [integrations and Apps (PT)](/apps-integracoes/).

## Automations, access and maintenance

### My first automation failed. What should I check?

Test the action from the dashboard first. Then inspect automation traces: trigger, conditions and actions. Running actions manually skips triggers and conditions, so it does not prove the complete rule works.

### Can I access my home while away?

Yes. Home Assistant Cloud and VPN are possible options. Follow the remote-access documentation and protect your accounts. Your hub's local address alone does not provide internet access.

### What makes a useful backup?

A recent backup you can restore. Keep a copy outside the hub and retain the emergency kit or recovery key when encryption is used. A file on the same disk does not protect against losing that disk.

### Can I change servers without rebuilding everything?

Backup and restore help migrate an installation. Besides the data, check radios, device paths, credentials and service compatibility on the destination. Allow time to test devices after restoring.

### A device went offline: should I reset it immediately?

Not as your first step. Check power, battery, the relevant service and logs. If several devices failed together, investigate the hub and network. For Z2M, follow the [diagnostic guide (PT)](/zigbee2mqtt-desconectando/) before removing pairing.

Sources: [automations](https://www.home-assistant.io/docs/automation/troubleshooting/), [remote access](https://www.home-assistant.io/docs/configuration/remote/) and [backups and restore](https://www.home-assistant.io/common-tasks/general/).

[Follow the beginner path](/en/start/) · [Explore all guides](/en/guides/).
