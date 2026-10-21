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

## A ready-made example: a scale in Home Assistant over Bluetooth {#example-scale}

A gateway that listens to the **Bluetooth (BLE)** advertisement from scales and publishes the weight to Home Assistant — without relying on the manufacturer's cloud. It runs on an **M5Stack ATOM Lite (ESP32)** and covers two protocols: **OKOK/QJ-J** scales (weight read straight from the advertisement) and the **Xiaomi Mi Scale 2** (through the native `xiaomi_miscale` component, with weight and impedance).

> **Replace with your own data before flashing.** The scale MAC addresses, the static IP and the `!secret` keys below are only examples. Never publish real MAC addresses, IPs or passwords.

```yaml
# BLE gateway -> Home Assistant for OKOK and Xiaomi Mi Scale 2 scales
# Hardware: M5Stack ATOM Lite (ESP32-PICO-D4) | Framework: ESP-IDF
# Replace the MACs, the static IP and the !secret keys with your own.

esphome:
  name: atom-bt-gateway-balanca
  friendly_name: "ATOM BT GATEWAY SCALE"

esp32:
  board: m5stack-atom
  framework:
    type: esp-idf

# ---- Connectivity ----
logger:
  level: DEBUG

api:
  encryption:
    key: !secret balanca_api_key

ota:
  - platform: esphome
    encryption:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:                    # adjust to your network (or remove to use DHCP)
    static_ip: 192.168.1.50
    gateway: 192.168.1.1
    subnet: 255.255.255.0
    dns1: 1.1.1.1
    dns2: 8.8.8.8
  power_save_mode: NONE

# ---- Internal state variables ----
globals:
  - id: medindo
    type: bool
    restore_value: no
    initial_value: 'false'
  - id: ultimo_peso
    type: float
    restore_value: no
    initial_value: '0'

# ---- ATOM Lite RGB LED (optional visual feedback) ----
light:
  - platform: esp32_rmt_led_strip
    id: status_led
    name: "Scale Status LED"
    pin: GPIO27
    num_leds: 1
    chipset: SK6812
    channel_colors: GRB
    entity_category: config

script:
  - id: pisca_ok
    then:
      - light.turn_on:
          id: status_led
          red: 0%
          green: 100%
          blue: 20%
          brightness: 40%
      - delay: 1500ms
      - light.turn_off: status_led

# ---- BLE listening ----
esp32_ble_tracker:
  scan_parameters:
    active: true          # requests scan response; does not open a GATT connection
    interval: 320ms
    window: 160ms
  on_ble_advertise:
    - mac_address: AA:BB:CC:DD:EE:FF   # <- MAC of YOUR OKOK scale
      then:
        - lambda: |-
            // The counter occupies the high byte: don't filter by the full ID.
            for (const auto &manu : x.get_manufacturer_datas()) {
              const auto uuid = manu.uuid.get_uuid();
              if (uuid.len != ESP_UUID_LEN_16 || (uuid.uuid.uuid16 & 0xFF) != 0xC0)
                continue;
              const auto &d = manu.data;
              if (d.size() != 13) continue;
              // Confirm the MAC embedded in the payload (use your own MAC bytes)
              if (!(d[7]==0xAA && d[8]==0xBB && d[9]==0xCC &&
                    d[10]==0xDD && d[11]==0xEE && d[12]==0xFF)) continue;

              uint16_t peso_raw = (uint16_t(d[0]) << 8) | d[1];
              uint8_t  flag     = d[6];
              if (flag != 0x24 && flag != 0x25) continue;
              if (flag == 0x25 && peso_raw == 0) continue;

              float peso = peso_raw / 100.0f;   // kg

              // Avoid re-sending hundreds of identical values to the API.
              if (!id(balanca_peso_vivo).has_state() ||
                  fabsf(id(balanca_peso_vivo).state - peso) > 0.005f) {
                id(balanca_peso_vivo).publish_state(peso);
              }

              if (flag == 0x24) {
                id(medindo) = true;
                id(balanca_estavel).publish_state(false);
              } else if (flag == 0x25) {
                const bool nova = id(medindo) || !id(balanca_peso).has_state() ||
                    fabsf(peso - id(ultimo_peso)) > 0.005f;
                id(medindo) = false;
                id(balanca_estavel).publish_state(true);
                if (nova) {
                  ESP_LOGI("balanca", "OKOK: weight=%.2f kg", peso);
                  id(ultimo_peso) = peso;
                  id(balanca_peso).publish_state(peso);
                  id(pisca_ok).execute();
                }
              }
            }

# ---- Sensors published to Home Assistant ----
sensor:
  - platform: template
    name: "Scale Weight"
    id: balanca_peso
    update_interval: never
    unit_of_measurement: "kg"
    device_class: weight
    state_class: measurement
    accuracy_decimals: 2
    icon: "mdi:scale-bathroom"

  - platform: template
    name: "Scale Weight (live)"
    id: balanca_peso_vivo
    update_interval: never
    unit_of_measurement: "kg"
    state_class: measurement
    accuracy_decimals: 2
    icon: "mdi:scale"
    entity_category: diagnostic

  - platform: wifi_signal
    name: "Scale Gateway WiFi"
    update_interval: 120s
    entity_category: diagnostic

  # Xiaomi: shares the BLE scanner; the only source of impedance.
  - platform: xiaomi_miscale
    id: xiaomi_balanca
    mac_address: 11:22:33:44:55:66   # <- MAC of YOUR Xiaomi Mi Scale 2
    clear_impedance: true
    weight:
      name: "Xiaomi Weight"
      id: xiaomi_peso
    impedance:
      name: "Xiaomi Impedance"
      id: xiaomi_impedancia

binary_sensor:
  - platform: template
    name: "Scale Measurement Stable"
    id: balanca_estavel
    icon: "mdi:check-circle"
    entity_category: diagnostic

  - platform: status
    name: "Scale Gateway Online"

text_sensor:
  - platform: version
    name: "Scale Gateway ESPHome"
    entity_category: diagnostic

switch:
  - platform: restart
    name: "Scale Gateway RESTART"
    id: balanca_gateway_restart
```

**How it works, in short:**

- The ESP32 only **listens** to BLE advertisements (`esp32_ble_tracker`); it never pairs with the scales.
- In the **OKOK** protocol, the weight comes in the first two bytes (`weight = (byte0 << 8 | byte1) / 100`). Flag **`0x24`** means an unstable (live) reading and **`0x25`** the final weight.
- The OKOK impedance is ignored; **impedance comes only from the Xiaomi**, through the `xiaomi_miscale` component.
- The ATOM LED blinks green on each final weight — an optional visual cue.

Validate it in the **ESPHome Device Builder** (*Validate*), create the entities in Home Assistant and test one component at a time.

## A ready-made example: a Bluetooth Proxy with the ATOM-S3 {#example-bt-proxy}

A **Bluetooth Proxy** extends Home Assistant's Bluetooth range: the ESP32 relays, over the network, the BLE signals of nearby devices (sensors, bulbs, tags). Here, on a **M5Stack ATOM-S3 (ESP32-S3)**, it also includes an LED that changes colour with the Wi-Fi state and a small optional *sniffer* that logs the BLE advertisements of **Philips Hue** bulbs — handy for diagnostics.

> **Replace with your own data before flashing.** The API encryption key, the OTA password, the static IP and the `!secret` keys below are only examples. Never publish real keys, passwords, MAC addresses or IPs — generate your own.

```yaml
# Bluetooth Proxy on a M5Stack ATOM-S3 (ESP32-S3), with a Wi-Fi status LED
# and an optional sniffer of Philips Hue BLE advertisements (diagnostics).
# Replace the API key, the OTA password, the static IP and the !secret keys.

esphome:
  name: atom-s3-bt-proxy
  friendly_name: "ATOM-S3 BT PROXY"
  on_boot:
    priority: -10
    then:
      - script.execute: atualizar_led_wifi

esp32:
  board: esp32-s3-devkitc-1
  variant: esp32s3
  framework:
    type: esp-idf
  flash_size: 8MB

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder

ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:                    # adjust to your network (or remove to use DHCP)
    static_ip: 192.168.1.51
    gateway: 192.168.1.1
    subnet: 255.255.255.0
  power_save_mode: NONE
  on_connect:
    then:
      - script.execute: atualizar_led_wifi
  on_disconnect:
    then:
      - light.turn_on:
          id: led_rgb
          red: 100%
          green: 0%
          blue: 0%
          brightness: 100%
  ap:
    ssid: atom-s3-bt-proxy

captive_portal:

light:
  - platform: esp32_rmt_led_strip
    id: led_rgb
    name: "Internal RGB LED"
    pin: GPIO35
    num_leds: 1
    chipset: WS2812
    channel_colors: GRB
    restore_mode: ALWAYS_OFF

esp32_ble_tracker:
  scan_parameters:
    interval: 1100ms
    window: 1100ms
    active: true
  # Optional C++ filter (lambda): logs only Philips Hue advertisements
  on_ble_advertise:
    then:
      - lambda: |-
          // 1. Filter by Signify's service UUID (0xFE0F), if available
          bool is_hue = false;

          for (auto data : x.get_service_uuids()) {
              if (data.to_string() == "0000fe0f-0000-1000-8000-00805f9b34fb" || data.to_string() == "0XFE0F") {
                  is_hue = true;
              }
          }

          // 2. Filter by manufacturer data (Manufacturer Data ID 0xFE0F)
          for (auto data : x.get_manufacturer_datas()) {
              if (data.uuid.to_string() == "0XFE0F" || data.uuid.to_string() == "0000fe0f-0000-1000-8000-00805f9b34fb") {
                  is_hue = true;
              }
          }

          // If it is a Hue bulb, print the raw details to the log
          if (is_hue) {
              ESP_LOGI("HUE_SNIFFER", "Hue bulb found!");
              ESP_LOGI("HUE_SNIFFER", "  MAC address: %s", x.address_str().c_str());
              ESP_LOGI("HUE_SNIFFER", "  BLE name: %s", x.get_name().c_str());
              ESP_LOGI("HUE_SNIFFER", "  Signal (RSSI): %d dBm", x.get_rssi());

              for (auto data : x.get_manufacturer_datas()) {
                  std::string hex_data = "";
                  for (uint8_t byte : data.data) {
                      char buf[4];
                      sprintf(buf, "%02X ", byte);
                      hex_data += buf;
                  }
                  ESP_LOGI("HUE_SNIFFER", "  Manufacturer Data [%s]: %s", data.uuid.to_string().c_str(), hex_data.c_str());
              }
          }

bluetooth_proxy:
  active: true

script:
  - id: atualizar_led_wifi
    mode: restart
    then:
      - if:
          condition:
            wifi.connected:
          then:
            - light.turn_on:
                id: led_rgb
                red: 0%
                green: 100%
                blue: 0%
                brightness: 100%
          else:
            - light.turn_on:
                id: led_rgb
                red: 100%
                green: 0%
                blue: 0%
                brightness: 100%

button:
  - platform: restart
    name: "Restart"
  - platform: safe_mode
    name: "Safe Mode"

binary_sensor:
  - platform: status
    name: "ESPHome Status"
    entity_category: diagnostic

sensor:
  - platform: wifi_signal
    name: "Wi-Fi Signal"
    update_interval: 60s
    entity_category: diagnostic
  - platform: uptime
    name: "Uptime"
    update_interval: 60s
    entity_category: diagnostic

text_sensor:
  - platform: wifi_info
    ip_address:
      name: "WI-FI IP Address"
      entity_category: diagnostic
    dns_address:
      name: "DNS Address"
      entity_category: diagnostic
    mac_address:
      name: "WI-FI MAC Address"
      entity_category: diagnostic
    ssid:
      name: "SSID"
      entity_category: diagnostic
    bssid:
      name: "BSSID"
      entity_category: diagnostic

safe_mode:
```

**How it works, in short:**

- `bluetooth_proxy` + `esp32_ble_tracker` make the ESP32 relay the BLE signals it sees to Home Assistant — **extending the home's Bluetooth coverage**.
- The LED turns **green** when Wi-Fi connects and **red** when it drops, driven by the `script`.
- The `lambda` block is an optional filter: it identifies **Philips Hue** advertisements (Signify's `0xFE0F` service UUID) and logs the MAC, the RSSI and the manufacturer bytes — for diagnostics only.
- Diagnostic sensors (Wi-Fi signal, uptime, IP, MAC, SSID) help you monitor the device; the **Restart** and **Safe Mode** buttons make recovery easier.

Validate it in the **ESPHome Device Builder** (*Validate*) and test one component at a time.

## A ready-made example: an infrared (IR) receiver in Home Assistant {#example-ir}

Want Home Assistant to "learn" the codes from your TV, air-conditioner or stereo remote? An **infrared receiver** wired to an ESP32 captures those signals. With `remote_receiver` and `dump: all`, every button you press shows up in the ESPHome log with its protocol and code — ready to reuse in an automation or a virtual remote.

> **Replace with your own data before flashing.** The API encryption key, the static IP, the DNS and the `!secret` keys below are only examples. Never publish real keys, passwords or IPs — generate your own.

```yaml
# Infrared (IR) receiver on an ESP32, exposed to Home Assistant.
# Replace the API key, the static IP, the DNS and the !secret keys with your own.

esphome:
  name: esp32-ir-receiver-escritorio
  friendly_name: "ESP32-IR-RECEIVER-OFFICE"

esp32:
  board: esp32-devkit-v1
  variant: esp32
  framework:
    type: esp-idf

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder

ota:
  - platform: esphome
    encryption:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  power_save_mode: NONE
  manual_ip:                    # adjust to your network (or remove to use DHCP)
    static_ip: 192.168.1.52
    gateway: 192.168.1.1
    subnet: 255.255.255.0
    dns1: 1.1.1.1
    dns2: 8.8.8.8

remote_receiver:
  id: ir_rx
  pin:
    number: GPIO27
    inverted: true
    mode:
      input: true
      pullup: true
  dump: all          # logs the codes of every protocol
  tolerance: 25%

# Exposes the receiver to Home Assistant's infrared integration.
infrared:
  - platform: ir_rf_proxy
    id: receptor_lg_escritorio
    name: "LG IR Receiver OFFICE"
    receiver_frequency: 38kHz
    remote_receiver_id: ir_rx
    icon: "mdi:remote"

button:
  - platform: restart
    name: "Restart"
  - platform: safe_mode
    name: "Safe Mode"

binary_sensor:
  - platform: status
    name: "ESPHome Status"
    entity_category: diagnostic

text_sensor:
  - platform: wifi_info
    ip_address:
      name: "WI-FI IP Address"
      entity_category: diagnostic
    dns_address:
      name: "DNS Address"
      entity_category: diagnostic
    mac_address:
      name: "WI-FI MAC Address"
      entity_category: diagnostic
```

**How it works, in short:**

- An **IR sensor** (for example a VS1838B/TSOP, 38 kHz) is wired to pin `GPIO27`, with `pullup`.
- `remote_receiver` with `dump: all` **decodes and logs** signals from several protocols — that's how you discover the code for each button.
- The `infrared` block exposes the receiver to Home Assistant's infrared integration.
- Diagnostic sensors (IP, DNS, MAC) and the **Restart** and **Safe Mode** buttons help with maintenance.

Check your receiver's pinout (VCC, GND and signal) and validate it in the **ESPHome Device Builder** before flashing.

[Back to Home Assistant](/en/home-assistant/).

Sources: [getting started with ESPHome](https://esphome.io/install/getting-started/), [install ESPHome](https://esphome.io/install/), [ESP32-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [ATOM-S3](https://docs.m5stack.com/en/core/AtomS3), [xiaomi_miscale component](https://esphome.io/components/sensor/xiaomi_miscale.html), [Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy.html), [remote_receiver (IR)](https://esphome.io/components/remote_receiver.html) and [Nabu Casa and the Open Home Foundation](https://www.nabucasa.com/).
