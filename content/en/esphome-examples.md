---
level: avancado
title: ESPHome examples
slug: esphome-examples
key: esphome-examples
description: Complete, ready-to-copy ESPHome configurations — a Bluetooth scale, a Bluetooth Proxy, an IR receiver, Thread devices and displays — for your Home Assistant.
category: DIY & firmware
icon: chip
order: 106
featured: false
section: artigo
reading: 6 examples
date: 2026-10-21
updated: 2026-10-21
tags: [ESPHome, ESP32, YAML, Examples, Thread]
---

Complete **ESPHome** configurations, ready to copy and adapt to your Home Assistant. Every example already has its sensitive data redacted (MACs, IPs, API keys and Thread *datasets* are placeholders) — **replace them with your own before flashing**.

New to ESPHome? Start with the [Sensors with ESPHome and ESP32](/en/esphome-esp32/) article.

## Index

- [A scale in Home Assistant over Bluetooth](#example-scale)
- [A Bluetooth Proxy (ATOM-S3)](#example-bt-proxy)
- [An infrared (IR) receiver](#example-ir)
- [A Thread device (NanoC6)](#example-thread)
- [A touchscreen panel (weather, curtains and AC)](#example-display)
- [A Thread display with temperature and humidity (C6-GEEK)](#example-c6geek)
- [A 7" wall panel for the whole home (Waveshare 7B)](#example-panel7b)
- [A voice assistant with a display (AtomS3R + Echo Base)](#example-voice)

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

## A ready-made example: a Thread device with the M5Stack NanoC6 {#example-thread}

**Thread** is a low-power wireless mesh network that underpins **Matter**. The **M5Stack NanoC6 (ESP32-C6)** has the required 802.15.4 radio and, with the `openthread` component, joins your Thread network as an FTD (router) device. The RGB LED signals the state: it blinks **red** with no connection to Home Assistant and turns **blue** once connected.

> **Highly sensitive data.** The `tlv` field (the *dataset*) contains **your Thread network key** — anyone who has that value can join your mesh. Never publish it. The API key and the other values below are examples too; generate your own.

```yaml
# M5Stack NanoC6 (ESP32-C6) as a Thread device (OpenThread).
# Replace the API key and, above all, your Thread network's TLV dataset.

esphome:
  name: nanoc6-thread
  friendly_name: "NanoC6 Thread"
  on_boot:
    # Priority -10: runs only after lights and switches already exist.
    priority: -10
    then:
      - switch.turn_on: pwr_g19   # ensures power to the RGB LED
      - delay: 1s
      - light.turn_on:
          id: rgb_led
          effect: "NanoC6 Thread Blink_Red"

esp32:
  board: esp32-c6-devkitc-1
  framework:
    type: esp-idf
    version: recommended
    sdkconfig_options:
      CONFIG_ESP_TASK_WDT_TIMEOUT_S: "60"   # larger watchdog for FTD (init can be slow)
      CONFIG_PM_ENABLE: "n"
      CONFIG_ESP_INT_WDT_TIMEOUT_MS: "2000"

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder
  on_client_connected:
    - light.turn_on:
        id: rgb_led
        red: 0.0
        green: 0.0
        blue: 1.0
        brightness: 1.0
        effect: none
  on_client_disconnected:
    - light.turn_on:
        id: rgb_led
        effect: "NanoC6 Thread Blink_Red"

ota:
  - platform: esphome
    encryption:

# IPv6 is required for Thread
network:
  enable_ipv6: true

# Thread radio. WARNING: the 'tlv' (dataset) contains YOUR THREAD NETWORK KEY.
# Never publish yours; paste your own network's dataset here.
openthread:
  device_type: FTD
  tlv: "PASTE_YOUR_THREAD_NETWORK_TLV_DATASET_HERE"
  force_dataset: true
  output_power: 20dBm

# ===== M5 Nano-C6 peripherals =====

# Native ESPHome diagnostic LED on pin 7
status_led:
  pin: GPIO7

switch:
  - platform: gpio
    pin: GPIO19
    id: pwr_g19
    name: "NanoC6 Thread Peripheral Power"
    restore_mode: ALWAYS_ON
  - platform: restart
    id: restart_switch
    name: "NanoC6 Thread Restart Switch"

# RGB LED (GPIO20)
light:
  - platform: esp32_rmt_led_strip
    id: rgb_led
    name: "Nano C6 RGB"
    pin: GPIO20
    num_leds: 1
    chipset: WS2812
    channel_colors: GRB
    effects:
      - strobe:
          name: "NanoC6 Thread Blink_Red"
          colors:
            - state: true
              red: 1.0
              green: 0.0
              blue: 0.0
              brightness: 1.0
              duration: 500ms
            - state: false
              duration: 500ms

button:
  - platform: restart
    id: restart_device
    name: "Restart Nano C6"

# Physical button (GPIO9): hold for 5s to restart
binary_sensor:
  - platform: gpio
    id: btn_gpio9
    name: "M5Stack Button"
    pin:
      number: GPIO9
      inverted: true
      mode:
        input: true
        pullup: true
    filters:
      - delayed_on: 5s
    on_press:
      - button.press: restart_device

  - platform: status
    name: "NanoC6 Thread Connection Status"
    id: status_conexao

# ===== Diagnostic sensors =====
sensor:
  - platform: uptime
    name: "NanoC6 Thread Uptime"
    id: uptime_sensor
    update_interval: 60s
    filters:
      - lambda: return x / 60.0;
    unit_of_measurement: "min"
    icon: mdi:clock-outline

text_sensor:
  - platform: openthread_info
    ip_address:
      name: "Thread IP Address"
    channel:
      name: "Thread Channel"
    role:
      name: "Thread Device Role"
    rloc16:
      name: "Thread RLOC16"
    ext_addr:
      name: "Thread Extended Address"
    eui64:
      name: "Thread EUI64"
    network_name:
      name: "Thread Network Name"
    network_key:
      name: "Thread Network Key"
    pan_id:
      name: "Thread PAN ID"
    ext_pan_id:
      name: "Thread Extended PAN ID"
```

**How it works, in short:**

- `openthread` with `device_type: FTD` makes the NanoC6 join the Thread network; the `tlv` is the *dataset* describing the network (channel, PAN ID and the **key**) — which is why it's confidential. `network: enable_ipv6` is mandatory.
- The RGB LED gives visual feedback: **blue** when Home Assistant is connected, **blinking red** when it isn't.
- The `switch` on `GPIO19` powers the NanoC6 peripherals (including the LED); the physical button on `GPIO9`, held for 5 s, restarts the device.
- The `openthread_info` `text_sensor`s expose the network diagnostics (IP, channel, role, PAN ID, etc.) in Home Assistant.

Get your Thread network's TLV dataset (from Home Assistant or your Border Router) and validate it in the **ESPHome Device Builder** before flashing.

## A ready-made example: a touchscreen panel (weather, curtains and AC) {#example-display}

A small wall touchscreen that shows the **clock, date and weather** and controls **curtains, a fan and an air-conditioner** straight from Home Assistant. This example uses a **Guition JC3248W535 board (ESP32-S3, 3.5" 320×480)** with ESPHome's **LVGL** UI library, across three pages and a bottom navigation bar.

> **Customise before flashing.** At the top, the `substitutions` block defines your **Home Assistant entities** (weather, fan, AC) and the city — adjust them to yours. The API key is an example; generate your own. The `cover.cortina_1..3` names are examples too.

```yaml
substitutions:
  device_name: tela-clima
  friendly_name: "Weather Display"
  city_name: "Fortaleza"
  ha_weather_entity: "weather.home"
  ha_fan_entity: "fan.ventilador_sala"
  ha_ac_entity: "climate.ar_sala"
  tz: "America/Fortaleza"

esphome:
  name: ${device_name}
  friendly_name: ${friendly_name}
  platformio_options:
    upload_speed: 921600
    board_build.flash_mode: dio
    board_build.f_flash: 80000000L
    board_build.f_cpu: 240000000L

# Board: Guition JC3248W535C_I_Y — ESP32-S3, 3.5" QSPI 320x480 screen (AXS15231B),
# capacitive touch on the same chip over I2C. Confirm your unit's flash/PSRAM
# (16MB / octal PSRAM is the usual default for this family; if compile/boot
# fails, try psram.mode: quad).
esp32:
  board: esp32-s3-devkitc-1
  variant: esp32s3
  flash_size: 16MB
  framework:
    type: esp-idf
    sdkconfig_options:
      COMPILER_OPTIMIZATION_SIZE: y
      CONFIG_ESP32S3_DEFAULT_CPU_FREQ_240: y
      CONFIG_ESP32S3_DATA_CACHE_64KB: y
      CONFIG_ESP32S3_DATA_CACHE_LINE_64B: y
      CONFIG_SPIRAM_FETCH_INSTRUCTIONS: y
      CONFIG_SPIRAM_RODATA: y

psram:
  mode: octal
  speed: 80MHz

logger:
  level: INFO

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  on_connect:
    - lvgl.label.update:
        id: wifi_icon
        text: "\U000F0928"
  on_disconnect:
    - lvgl.label.update:
        id: wifi_icon
        text: "\U000F092E"

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder

ota:
  - platform: esphome
    encryption:

# Required so Home Assistant can push the weather entity to the device AND so
# the device can call services back (curtains/AC/fan). It only works after the
# device has been added to the ESPHome integration in HA.

time:
  - platform: sntp
    id: sntp_time
    timezone: "${tz}"
    servers:
      - time.google.com
      - time1.google.com
      - pool.ntp.org

# --- Buses ---------------------------------------------------------------
spi:
  - type: quad
    clk_pin: 47
    data_pins: [21, 48, 40, 39]

i2c:
  - sda: 4
    scl: 8

# --- Backlight -------------------------------------------------------------
output:
  - id: gpio_backlight_pwm
    platform: ledc
    pin: 1

light:
  - id: backlight
    name: "Backlight"
    platform: monochromatic
    output: gpio_backlight_pwm
    restore_mode: ALWAYS_ON

# --- Screen + touch (AXS15231B, native mipi_spi driver) --------------------
display:
  - id: main_display
    platform: mipi_spi
    model: JC3248W535
    rotation: 0°   # 0° = portrait 320x480 on this board; use 90°/270° if it comes sideways
    data_rate: 40MHz
    update_interval: never
    auto_clear_enabled: false

touchscreen:
  - id: main_touchscreen
    platform: axs15231

# --- Fonts -------------------------------------------------------------
font:
  - file:
      type: gfonts
      family: Roboto
      weight: bold
    id: font_time
    size: 72
    bpp: 4
    glyphs: "0123456789:"

  - file: "gfonts://Roboto"
    id: font_text_md
    size: 22
    bpp: 4
    glyphsets: GF_Latin_Core
    glyphs: ["°", "•"]

  - file:
      type: gfonts
      family: Roboto
      weight: bold
    id: font_num_big
    size: 48
    bpp: 4
    glyphs: "0123456789°C+- "

  # Large weather icons (sun / cloud / rain)
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_icon_weather
    size: 150
    bpp: 4
    glyphs:
      - "\U000F0599"  # weather-sunny
      - "\U000F0594"  # weather-night (clear-night)
      - "\U000F0595"  # weather-partly-cloudy
      - "\U000F0590"  # weather-cloudy
      - "\U000F0596"  # weather-pouring (rain)

  # WiFi icon (small)
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_icon_wifi
    size: 22
    bpp: 4
    glyphs:
      - "\U000F0928"  # wifi-strength-4
      - "\U000F0925"  # wifi-strength-3
      - "\U000F0922"  # wifi-strength-2
      - "\U000F091F"  # wifi-strength-1
      - "\U000F092E"  # wifi-strength-off-outline

  # Bottom navigation bar icons
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_nav
    size: 30
    bpp: 4
    glyphs:
      - "\U000F02DC"  # home
      - "\U000F111C"  # window-shutter (curtains)
      - "\U000F001B"  # air-conditioner

  # Control button icons
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_icon
    size: 40
    bpp: 4
    glyphs:
      - "\U000F0737"  # arrow-up-bold (open)
      - "\U000F072E"  # arrow-down-bold (close)
      - "\U000F04DB"  # stop
      - "\U000F0425"  # power
      - "\U000F0210"  # fan
      - "\U000F001B"  # air-conditioner
      - "\U000F111C"  # window-shutter

# --- Sensors -------------------------------------------------------------
sensor:
  - platform: wifi_signal
    id: wifi_signal_dbm
    update_interval: 30s
    internal: true
    on_value:
      - lvgl.label.update:
          id: wifi_icon
          text: !lambda |-
            if (x >= -60) return std::string("\U000F0928");
            else if (x >= -67) return std::string("\U000F0925");
            else if (x >= -75) return std::string("\U000F0922");
            else return std::string("\U000F091F");

  - platform: homeassistant
    id: ha_weather_temp
    entity_id: ${ha_weather_entity}
    attribute: temperature
    internal: true
    on_value:
      - lvgl.label.update:
          id: temp_city_label
          text:
            format: "${city_name} • %.0f°C"
            args: [x]
            if_nan: "${city_name} • --°C"

  # Air-conditioner: current room temperature
  - platform: homeassistant
    id: ha_ac_current
    entity_id: ${ha_ac_entity}
    attribute: current_temperature
    internal: true
    on_value:
      - lvgl.label.update:
          id: ac_current_label
          text:
            format: "Current: %.1f°C"
            args: [x]
            if_nan: "Current: --"

  # Air-conditioner: target temperature (setpoint)
  - platform: homeassistant
    id: ha_ac_target
    entity_id: ${ha_ac_entity}
    attribute: temperature
    internal: true
    on_value:
      - lvgl.label.update:
          id: ac_target_label
          text:
            format: "%.0f°C"
            args: [x]
            if_nan: "--"

  # Fan: current speed (%)
  - platform: homeassistant
    id: ha_fan_pct
    entity_id: ${ha_fan_entity}
    attribute: percentage
    internal: true
    on_value:
      - lvgl.label.update:
          id: fan_speed_label
          text:
            format: "Speed: %.0f%%"
            args: [x]
            if_nan: "Speed: --"

text_sensor:
  - platform: homeassistant
    id: ha_weather_condition
    entity_id: ${ha_weather_entity}
    internal: true
    on_value:
      - lvgl.label.update:
          id: weather_icon
          text: !lambda |-
            std::string c = x;
            if (c == "sunny") return std::string("\U000F0599");
            if (c == "clear-night") return std::string("\U000F0594");
            if (c == "partlycloudy") return std::string("\U000F0595");
            if (c == "rainy" || c == "pouring" || c == "lightning" ||
                c == "lightning-rainy" || c == "hail" || c == "snowy" ||
                c == "snowy-rainy") return std::string("\U000F0596");
            return std::string("\U000F0590");
      - lvgl.label.update:
          id: forecast_label
          text: !lambda |-
            std::string c = x;
            if (c == "sunny") return std::string("Sunny");
            if (c == "clear-night") return std::string("Clear night");
            if (c == "partlycloudy") return std::string("Partly cloudy");
            if (c == "cloudy") return std::string("Cloudy");
            if (c == "fog") return std::string("Fog");
            if (c == "windy" || c == "windy-variant") return std::string("Windy");
            if (c == "rainy") return std::string("Rain");
            if (c == "pouring") return std::string("Heavy rain");
            if (c == "lightning") return std::string("Thunderstorm");
            if (c == "lightning-rainy") return std::string("Thunderstorm with rain");
            if (c == "hail") return std::string("Hail");
            if (c == "snowy") return std::string("Snow");
            if (c == "snowy-rainy") return std::string("Sleet");
            return std::string("Unavailable");

  # Air-conditioner: current mode (off/cool/dry/...) — updates the label and power colour
  - platform: homeassistant
    id: ha_ac_mode
    entity_id: ${ha_ac_entity}
    internal: true
    on_value:
      - lvgl.label.update:
          id: ac_mode_label
          text: !lambda |-
            std::string m = x;
            if (m == "off") return std::string("Off");
            if (m == "cool") return std::string("Cool");
            if (m == "dry") return std::string("Dry");
            if (m == "fan_only") return std::string("Fan only");
            if (m == "heat") return std::string("Heat");
            if (m == "heat_cool") return std::string("Auto");
            return m;
      - if:
          condition:
            lambda: 'return x == "off";'
          then:
            - lvgl.widget.update:
                id: btn_ac_power
                bg_color: 0x263238
          else:
            - lvgl.widget.update:
                id: btn_ac_power
                bg_color: 0x2196F3

# --- Clock / date (updated locally, independent of HA) ---------------------
interval:
  - interval: 1s
    then:
      - lvgl.label.update:
          id: time_label
          text: !lambda |-
            auto t = id(sntp_time).now();
            if (!t.is_valid()) return std::string("--:--");
            char buf[8];
            snprintf(buf, sizeof(buf), "%02d:%02d", t.hour, t.minute);
            return std::string(buf);

  - interval: 30s
    then:
      - lvgl.label.update:
          id: date_label
          text: !lambda |-
            auto t = id(sntp_time).now();
            if (!t.is_valid()) return std::string("Syncing...");
            static const char *days[] = {"", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"};
            static const char *months[] = {"", "January", "February", "March", "April",
                "May", "June", "July", "August", "September", "October", "November", "December"};
            char buf[48];
            snprintf(buf, sizeof(buf), "%s, %s %d, %d",
                days[t.day_of_week], months[t.month], t.day_of_month, t.year);
            return std::string(buf);

# --- LVGL interface ----------------------------------------------------
lvgl:
  displays:
    - main_display
  touchscreens:
    - main_touchscreen
  bg_color: 0x000000

  # Bottom navigation bar — always visible over every page
  top_layer:
    widgets:
      - obj:
          width: 320
          height: 56
          align: BOTTOM_MID
          y: 0
          bg_color: 0x11151A
          bg_opa: COVER
          border_width: 0
          radius: 0
          pad_all: 0

      - button:
          id: nav_clima
          width: 100
          height: 48
          align: BOTTOM_LEFT
          x: 4
          y: -4
          bg_color: 0x2196F3
          radius: 10
          border_width: 0
          widgets:
            - label:
                text: "\U000F02DC"
                text_font: font_nav
                text_color: 0xFFFFFF
                align: CENTER
          on_click:
            - lvgl.page.show: page_clima
            - lvgl.widget.update: {id: nav_clima, bg_color: 0x2196F3}
            - lvgl.widget.update: {id: nav_cortinas, bg_color: 0x263238}
            - lvgl.widget.update: {id: nav_ar, bg_color: 0x263238}

      - button:
          id: nav_cortinas
          width: 100
          height: 48
          align: BOTTOM_LEFT
          x: 110
          y: -4
          bg_color: 0x263238
          radius: 10
          border_width: 0
          widgets:
            - label:
                text: "\U000F111C"
                text_font: font_nav
                text_color: 0xFFFFFF
                align: CENTER
          on_click:
            - lvgl.page.show: page_cortinas
            - lvgl.widget.update: {id: nav_clima, bg_color: 0x263238}
            - lvgl.widget.update: {id: nav_cortinas, bg_color: 0x2196F3}
            - lvgl.widget.update: {id: nav_ar, bg_color: 0x263238}

      - button:
          id: nav_ar
          width: 100
          height: 48
          align: BOTTOM_LEFT
          x: 216
          y: -4
          bg_color: 0x263238
          radius: 10
          border_width: 0
          widgets:
            - label:
                text: "\U000F001B"
                text_font: font_nav
                text_color: 0xFFFFFF
                align: CENTER
          on_click:
            - lvgl.page.show: page_ar
            - lvgl.widget.update: {id: nav_clima, bg_color: 0x263238}
            - lvgl.widget.update: {id: nav_cortinas, bg_color: 0x263238}
            - lvgl.widget.update: {id: nav_ar, bg_color: 0x2196F3}

  pages:
    # ===================== PAGE 1: WEATHER / CLOCK =====================
    - id: page_clima
      bg_color: 0x000000
      widgets:
        - label:
            id: wifi_icon
            text: "\U000F092E"
            text_font: font_icon_wifi
            text_color: 0xB0BEC5
            align: TOP_LEFT
            x: 8
            y: 6

        - label:
            id: time_label
            text: "--:--"
            text_font: font_time
            text_color: 0xFFFFFF
            align: TOP_MID
            y: 4

        - label:
            id: date_label
            text: "Syncing..."
            text_font: font_text_md
            text_color: 0xB0BEC5
            align: TOP_MID
            y: 98

        - label:
            id: weather_icon
            text: "\U000F0595"
            text_font: font_icon_weather
            text_color: 0x90A4AE
            align: CENTER
            y: -20

        - label:
            id: forecast_label
            text: "Waiting for data..."
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: CENTER
            y: 120

        - label:
            id: temp_city_label
            text: "--"
            text_font: font_text_md
            text_color: 0xB0BEC5
            align: CENTER
            y: 155

    # ===================== PAGE 2: CURTAINS =====================
    - id: page_cortinas
      bg_color: 0x000000
      widgets:
        - label:
            text: "Curtains"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_MID
            y: 14

        # ---- Row: All ----
        - label:
            text: "All"
            text_font: font_text_md
            text_color: 0xB0BEC5
            align: TOP_LEFT
            x: 12
            y: 78
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 118
            y: 60
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F0737", text_font: font_icon, text_color: 0x4CAF50, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.open_cover
                  data: {entity_id: "cover.cortina_1, cover.cortina_2, cover.cortina_3"}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 186
            y: 60
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F04DB", text_font: font_icon, text_color: 0xFFB300, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.stop_cover
                  data: {entity_id: "cover.cortina_1, cover.cortina_2, cover.cortina_3"}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 254
            y: 60
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F072E", text_font: font_icon, text_color: 0xEF5350, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.close_cover
                  data: {entity_id: "cover.cortina_1, cover.cortina_2, cover.cortina_3"}

        # ---- Row: Curtain 1 ----
        - label:
            text: "Curtain 1"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_LEFT
            x: 12
            y: 170
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 118
            y: 152
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F0737", text_font: font_icon, text_color: 0x4CAF50, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.open_cover
                  data: {entity_id: cover.cortina_1}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 186
            y: 152
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F04DB", text_font: font_icon, text_color: 0xFFB300, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.stop_cover
                  data: {entity_id: cover.cortina_1}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 254
            y: 152
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F072E", text_font: font_icon, text_color: 0xEF5350, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.close_cover
                  data: {entity_id: cover.cortina_1}

        # ---- Row: Curtain 2 ----
        - label:
            text: "Curtain 2"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_LEFT
            x: 12
            y: 262
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 118
            y: 244
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F0737", text_font: font_icon, text_color: 0x4CAF50, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.open_cover
                  data: {entity_id: cover.cortina_2}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 186
            y: 244
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F04DB", text_font: font_icon, text_color: 0xFFB300, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.stop_cover
                  data: {entity_id: cover.cortina_2}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 254
            y: 244
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F072E", text_font: font_icon, text_color: 0xEF5350, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.close_cover
                  data: {entity_id: cover.cortina_2}

        # ---- Row: Curtain 3 ----
        - label:
            text: "Curtain 3"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_LEFT
            x: 12
            y: 354
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 118
            y: 336
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F0737", text_font: font_icon, text_color: 0x4CAF50, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.open_cover
                  data: {entity_id: cover.cortina_3}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 186
            y: 336
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F04DB", text_font: font_icon, text_color: 0xFFB300, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.stop_cover
                  data: {entity_id: cover.cortina_3}
        - button:
            width: 60
            height: 60
            align: TOP_LEFT
            x: 254
            y: 336
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F072E", text_font: font_icon, text_color: 0xEF5350, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: cover.close_cover
                  data: {entity_id: cover.cortina_3}

    # ===================== PAGE 3: FAN + AC =====================
    - id: page_ar
      bg_color: 0x000000
      widgets:
        # ---------- Fan ----------
        - label:
            text: "\U000F0210"
            text_font: font_icon
            text_color: 0x2196F3
            align: TOP_LEFT
            x: 14
            y: 10
        - label:
            text: "Fan"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_LEFT
            x: 62
            y: 20

        - button:
            width: 72
            height: 52
            align: TOP_LEFT
            x: 8
            y: 62
            bg_color: 0x37474F
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "Off", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: fan.turn_off
                  data: {entity_id: "${ha_fan_entity}"}
        - button:
            width: 72
            height: 52
            align: TOP_LEFT
            x: 84
            y: 62
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "Low", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: fan.set_percentage
                  data: {entity_id: "${ha_fan_entity}", percentage: "33"}
        - button:
            width: 72
            height: 52
            align: TOP_LEFT
            x: 160
            y: 62
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "Medium", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: fan.set_percentage
                  data: {entity_id: "${ha_fan_entity}", percentage: "66"}
        - button:
            width: 72
            height: 52
            align: TOP_LEFT
            x: 236
            y: 62
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "High", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: fan.set_percentage
                  data: {entity_id: "${ha_fan_entity}", percentage: "100"}

        - label:
            id: fan_speed_label
            text: "Speed: --"
            text_font: font_text_md
            text_color: 0x90A4AE
            align: TOP_MID
            y: 124

        # ---------- Air-conditioner ----------
        - label:
            text: "\U000F001B"
            text_font: font_icon
            text_color: 0x2196F3
            align: TOP_LEFT
            x: 14
            y: 166
        - label:
            text: "Living Room AC"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_LEFT
            x: 62
            y: 176

        - button:
            id: btn_ac_power
            width: 60
            height: 52
            align: TOP_RIGHT
            x: -10
            y: 166
            bg_color: 0x263238
            radius: 10
            border_width: 0
            widgets:
              - label: {text: "\U000F0425", text_font: font_icon, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - if:
                  condition:
                    lambda: 'return id(ha_ac_mode).state == "off";'
                  then:
                    - homeassistant.action:
                        action: climate.set_hvac_mode
                        data: {entity_id: "${ha_ac_entity}", hvac_mode: cool}
                  else:
                    - homeassistant.action:
                        action: climate.set_hvac_mode
                        data: {entity_id: "${ha_ac_entity}", hvac_mode: "off"}

        - button:
            width: 66
            height: 72
            align: TOP_LEFT
            x: 16
            y: 232
            bg_color: 0x263238
            radius: 12
            border_width: 0
            widgets:
              - label: {text: "-", text_font: font_num_big, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: climate.set_temperature
                  data: {entity_id: "${ha_ac_entity}"}
                  data_template:
                    temperature: "{{ [ (state_attr('${ha_ac_entity}','temperature') | float(21)) - 1, 16 ] | max }}"

        - label:
            id: ac_target_label
            text: "--"
            text_font: font_num_big
            text_color: 0xFFFFFF
            align: TOP_MID
            y: 244

        - button:
            width: 66
            height: 72
            align: TOP_RIGHT
            x: -16
            y: 232
            bg_color: 0x263238
            radius: 12
            border_width: 0
            widgets:
              - label: {text: "+", text_font: font_num_big, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: climate.set_temperature
                  data: {entity_id: "${ha_ac_entity}"}
                  data_template:
                    temperature: "{{ [ (state_attr('${ha_ac_entity}','temperature') | float(21)) + 1, 30 ] | min }}"

        - label:
            id: ac_current_label
            text: "Current: --"
            text_font: font_text_md
            text_color: 0x90A4AE
            align: TOP_MID
            y: 322

        - label:
            id: ac_mode_label
            text: "—"
            text_font: font_text_md
            text_color: 0x64B5F6
            align: TOP_MID
            y: 352
```

**How it works, in short:**

- `substitutions` at the top centralises what you change: the device name, your **HA entities** (`weather`, `fan`, `climate`), the city and the timezone — no hunting through the file.
- `display` (`mipi_spi` driver, `JC3248W535` model) + `touchscreen` (`axs15231`) bring up the screen and touch; `lvgl` draws the interface across 3 pages with a bottom bar.
- `platform: homeassistant` sensors **pull** data from HA (weather temperature, AC mode, fan speed) and update the on-screen labels; the buttons call services back (`homeassistant.action`) to open/close curtains, switch the AC and change the fan speed.
- The clock and date are generated locally (via `sntp`), independent of HA.
- **Hardware:** confirm your unit's flash/PSRAM; if boot fails, try `psram.mode: quad`. The screen rotation may need `90°`/`270°`.

Adjust the `substitutions` to your entities and validate it in the **ESPHome Device Builder** before flashing.

## A ready-made example: a Thread display with temperature and humidity (Waveshare C6-GEEK) {#example-c6geek}

The **Waveshare ESP32-C6-GEEK** board combines three things in a single device: a **Thread** connection, a small **ST7789V screen** (240×135) and a **DHT sensor** (AM2302/DHT11) for temperature and humidity. The screen shows the **clock, date and the sensor readings** while the device joins your Thread network.

> **Highly sensitive data.** The `tlv` field (the *dataset*) contains **your Thread network key** — never publish it. The API key is an example too; generate your own.

```yaml
# Waveshare ESP32-C6-GEEK: a Thread device with an ST7789V screen and a DHT sensor.
# Replace the API key and, above all, your Thread network's TLV dataset.

esphome:
  name: waveshare-esp32-c6-geek
  friendly_name: "Waveshare ESP32-C6-GEEK"
  min_version: 2026.9.0

esp32:
  board: esp32-c6-devkitc-1
  variant: esp32c6
  flash_size: 16MB
  framework:
    type: esp-idf
    version: recommended
    sdkconfig_options:
      CONFIG_ESP_TASK_WDT_TIMEOUT_S: "60"   # larger watchdog for FTD (init can be slow)
      CONFIG_PM_ENABLE: "n"
      CONFIG_ESP_INT_WDT_TIMEOUT_MS: "2000"

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder
  # Keeps the screen working even without a connection to HA.
  reboot_timeout: 0s

ota:
  - platform: esphome
    encryption:

# Thread uses IPv6.
network:
  enable_ipv6: true

# Thread radio. WARNING: the 'tlv' (dataset) contains YOUR THREAD NETWORK KEY.
# Never publish yours; paste your own network's dataset here.
openthread:
  device_type: FTD
  force_dataset: true
  tlv: "PASTE_YOUR_THREAD_NETWORK_TLV_DATASET_HERE"
  output_power: 20dBm

# Google time, shown in the Fortaleza timezone.
time:
  - platform: sntp
    id: horario_google
    timezone: America/Fortaleza
    servers:
      - time1.google.com
      - time2.google.com
      - time3.google.com
    update_interval: 1h

spi:
  clk_pin: GPIO1
  mosi_pin: GPIO2

# Fonts are downloaded while the firmware is prepared.
font:
  - file: "gfonts://Roboto"
    id: fonte_pequena
    size: 14

  - file: "gfonts://Roboto"
    id: fonte_valores
    size: 26
    glyphs: ["0123456789 .-°C%"]

  - file: "gfonts://Roboto"
    id: fonte_relogio
    size: 28

sensor:
  - platform: dht
    id: sensor_dht_1
    pin: GPIO11
    model: AM2302
    update_interval: 10s
    temperature:
      name: Temperature
      id: sensor_dht_1_temperature
      icon: "mdi:thermometer"
      accuracy_decimals: 0
    humidity:
      name: Humidity
      id: sensor_dht_1_humidity
      icon: "mdi:water-percent"
      accuracy_decimals: 0

  - platform: uptime
    name: "Waveshare ESP32-C6-GEEK Uptime"
    id: uptime_sensor
    update_interval: 60s
    filters:
      - lambda: return x / 60.0;
    unit_of_measurement: "min"
    icon: mdi:clock-outline

display:
  - platform: st7789v
    id: tela
    model: CUSTOM
    cs_pin: GPIO5
    dc_pin: GPIO3
    reset_pin: GPIO4
    backlight_pin: GPIO6
    # Native geometry; rotation yields 240 × 135.
    width: 135
    height: 240
    offset_width: 52
    offset_height: 40
    rotation: 270
    update_interval: 1s
    lambda: |-
      const Color branco(255, 255, 255);
      const Color cinza(160, 160, 160);
      const Color azul(80, 190, 255);
      const Color laranja(255, 180, 70);

      it.fill(Color(0, 0, 0));

      // Time and date.
      auto agora = id(horario_google).now();

      if (agora.is_valid()) {
        it.strftime(
          120, 0, id(fonte_relogio), branco,
          TextAlign::TOP_CENTER, "%H:%M:%S", agora
        );
        it.strftime(
          120, 34, id(fonte_pequena), cinza,
          TextAlign::TOP_CENTER, "%d/%m/%Y", agora
        );
      } else {
        it.print(
          120, 0, id(fonte_relogio), branco,
          TextAlign::TOP_CENTER, "--:--:--"
        );
        it.print(
          120, 34, id(fonte_pequena), cinza,
          TextAlign::TOP_CENTER, "Syncing time..."
        );
      }

      // Separators and titles.
      it.line(8, 57, 231, 57, cinza);
      it.line(120, 67, 120, 125, cinza);

      it.print(
        60, 65, id(fonte_pequena), cinza,
        TextAlign::TOP_CENTER, "Temperature"
      );
      it.print(
        180, 65, id(fonte_pequena), cinza,
        TextAlign::TOP_CENTER, "Humidity"
      );

      // DHT readings.
      const float temperatura =
        id(sensor_dht_1_temperature).state;
      const float umidade =
        id(sensor_dht_1_humidity).state;

      if (!isnan(temperatura)) {
        it.printf(
          60, 88, id(fonte_valores), laranja,
          TextAlign::TOP_CENTER, "%.0f °C", temperatura
        );
      } else {
        it.print(
          60, 88, id(fonte_valores), laranja,
          TextAlign::TOP_CENTER, "-- °C"
        );
      }

      if (!isnan(umidade)) {
        it.printf(
          180, 88, id(fonte_valores), azul,
          TextAlign::TOP_CENTER, "%.0f %%", umidade
        );
      } else {
        it.print(
          180, 88, id(fonte_valores), azul,
          TextAlign::TOP_CENTER, "-- %"
        );
      }

switch:
  - platform: restart
    id: restart_switch
    name: "Waveshare ESP32-C6-GEEK Restart Switch"

binary_sensor:
  - platform: status
    name: "Waveshare ESP32-C6-GEEK Connection Status"
    id: status_conexao

text_sensor:
  - platform: openthread_info
    ip_address:
      name: "Thread IP Address"
    channel:
      name: "Thread Channel"
    role:
      name: "Thread Device Role"
    rloc16:
      name: "Thread RLOC16"
    ext_addr:
      name: "Thread Extended Address"
    eui64:
      name: "Thread EUI64"
    network_name:
      name: "Thread Network Name"
    network_key:
      name: "Thread Network Key"
    pan_id:
      name: "Thread PAN ID"
    ext_pan_id:
      name: "Thread Extended PAN ID"
```

**How it works, in short:**

- `openthread` (FTD) connects the board to the Thread network; the `tlv` is the confidential *dataset* (it holds the network key). `network: enable_ipv6` is mandatory.
- A **DHT** sensor on `GPIO11` reads temperature and humidity every 10 s.
- The **ST7789V** `display` draws, in the `lambda`, the clock (via `sntp`), the date and the two readings — all locally, so the screen doesn't depend on HA (`reboot_timeout: 0s` keeps it alive even without HA).
- Diagnostic sensors (uptime, status, Thread info) help you monitor it.

Check your sensor and your board's pinout, and validate it in the **ESPHome Device Builder** before flashing.

## Reference example: a 7" wall panel for the whole home (Waveshare 7B) {#example-panel7b}

A **7" wall panel** (Waveshare ESP32-S3-Touch-LCD-7B, 1024×600) that becomes the **central controller for the home**: it shows the clock, the weather with a 5-day forecast, the **Bitcoin** price (with a mini-chart) and one page per room with **lights (on/off + brightness), air-conditioner, fan and curtains** — all via Home Assistant, with LVGL v9.

Because it's large and depends on its own files, it's included here as a **commented reference** (key snippets), not the whole file.

> **This example is NOT self-contained.** It must be accompanied by:
> - **`waveshare_7b/panel_data.h`** — a C++ *header* with the Bitcoin logic (Coinbase parsing, mini-chart) and the `condition_pt()` function that translates the weather conditions;
> - the **room images** (`waveshare_7b/assets/*.jpg`).
>
> It requires **ESPHome 2026.9+** and, in HA, the **"Allow the device to perform Home Assistant actions"** option enabled. The API key and static IP are only examples — generate/adjust your own. (The on-screen labels in this example are in Portuguese; adapt them as you like.)

**1. Base (board, PSRAM, API and Wi-Fi):**

```yaml
substitutions:
  name: waveshare-esp32-s3-touch-lcd-7b
  friendly_name: Waveshare ESP32-S3-Touch-LCD-7B
  weather_entity: weather.home

esphome:
  name: ${name}
  friendly_name: ${friendly_name}
  min_version: 2026.9.0
  includes:
    - waveshare_7b/panel_data.h   # C++ header (Bitcoin logic, condition_pt) — must be included
  on_boot:
    - priority: -100
      then:
        - light.turn_on: { id: screen_backlight, brightness: 75% }
        - script.execute: refresh_clock
        - delay: 8s
        - script.execute: fetch_market
        - script.execute: fetch_forecast

esp32:
  board: esp32-s3-devkitc-1
  variant: esp32s3
  flash_size: 16MB
  framework:
    type: esp-idf

psram:
  mode: octal
  speed: 80MHz

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder
  reboot_timeout: 0s                   # keeps the screen alive even without HA

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  # manual_ip is optional — adjust to your network or remove it to use DHCP
```

**2. RGB screen + touch (the trickiest hardware part):**

```yaml
# 1024x600 RGB screen (native mipi_rgb driver) + GT911 touch on the I2C bus.
# An I2C expander (waveshare_io_ch32v003) handles reset/enable/backlight.
display:
  - platform: mipi_rgb
    id: disp1
    model: RPI
    dimensions: { width: 1024, height: 600 }
    color_order: RGB
    pclk_frequency: 30MHz
    pclk_inverted: true
    # data and sync pins depend on the board (see the full config)
    update_interval: never
    auto_clear_enabled: false

touchscreen:
  - platform: gt911
    id: touch_panel
    display: disp1
    i2c_id: touch_bus
    address: 93
```

**3. Bitcoin price (an HTTP request to Coinbase, independent of HA):**

```yaml
http_request:
  id: market_http
  verify_ssl: true

script:
  - id: fetch_market
    then:
      - http_request.get:
          url: https://api.exchange.coinbase.com/products/BTC-USD/ticker
          capture_response: true
          on_response:
            - lambda: |-
                waveshare_panel::bitcoin().parse_quote(body, id(panel_time).now().strftime("%H:%M"));
            - script.execute: refresh_bitcoin
```

**4. Per-entity control pattern (repeated for each light/room):**

```yaml
# A sensor reads the light's brightness from HA and moves the on-screen slider:
sensor:
  - platform: homeassistant
    id: level_light_led_sala
    entity_id: light.led_sala
    attribute: brightness
    on_value:
      - lvgl.slider.update:
          id: slider_light_led_sala
          value: !lambda "return std::isfinite(x) ? (int)lroundf(x * 100.0f / 255.0f) : 0;"

# And, inside the room page, the button/slider calls the service back:
#   button (toggle) + slider (brightness) -> homeassistant.action: light.toggle / light.turn_on
```

**How it works, in short:**

- The screen uses the native **`mipi_rgb`** driver (1024×600) and **`gt911`** touch; an I²C expander (`waveshare_io_ch32v003`) handles reset, enable and backlight.
- Dozens of **`platform: homeassistant`** sensors mirror the entities' state (brightness, AC mode, cover state) and update the LVGL widgets; the buttons and sliders call services back with **`homeassistant.action`**.
- The clock, the forecast (via HA's `weather.get_forecasts`) and **Bitcoin** (Coinbase API) are refreshed by `interval`/`script`.
- The interface has a **main page** (weather + BTC + per-room shortcuts) and **one page per room**, with scrolling.

Treat this example as an **advanced starting point**: the full file (with `panel_data.h` and the images) is long and specific to the home.

## A ready-made example: a voice assistant with a display (M5Stack AtomS3R + Echo Base) {#example-voice}

A **voice assistant** with a small status screen, built with the **M5Stack AtomS3R + Echo Base**. It detects wake words (*Okay Nabu*, *Hey Jarvis*, *Hey Mycroft*) with the **wake word running on the device itself** (or in Home Assistant) and talks to HA's **Assist**; the screen shows each phase — listening, thinking, replying — with the *Casita* illustrations.

> **Replace with your own data before flashing.** The API key and the static IP are examples; generate/adjust your own. The illustrations, sounds and wake-word models are **downloaded from public URLs** at compile time — this example needs no local files. It requires **ESPHome 2026.7+** and the **Echo Base** audio hardware (microphone + speaker).

```yaml
substitutions:
  name: atom-lcd-echo
  friendly_name: "ATOM LCD ECHO"

  # Casita images
  loading_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/loading_320_240.png
  idle_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/idle_320_240.png
  listening_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/listening_320_240.png
  thinking_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/thinking_320_240.png
  replying_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/replying_320_240.png
  error_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/casita/error_320_240.png
  error_no_wifi_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/error_box_illustrations/error-no-wifi.png
  error_no_ha_illustration_file: https://github.com/esphome/wake-word-voice-assistants/raw/main/error_box_illustrations/error-no-ha.png

  # Fonts
  mdi_webfont_file: https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/fonts/materialdesignicons-webfont.ttf

  # Audio files
  wake_word_trigger_sound_file: https://github.com/esphome/home-assistant-voice-pe/raw/dev/sounds/wake_word_triggered.flac
  timer_finished_sound_file: https://github.com/esphome/home-assistant-voice-pe/raw/dev/sounds/timer_finished.flac
  error_cloud_expired_file: https://github.com/esphome/home-assistant-voice-pe/raw/dev/sounds/error_cloud_expired.mp3

  # Micro Wake Word models
  stop_model_file: https://github.com/kahrendt/microWakeWord/releases/download/stop/stop.json

  # Background colors
  loading_illustration_background_color: "000000"
  idle_illustration_background_color: "000000"
  listening_illustration_background_color: "FFFFFF"
  thinking_illustration_background_color: "FFFFFF"
  replying_illustration_background_color: "FFFFFF"
  error_illustration_background_color: "000000"

  # Voice assistant phases
  voice_assist_idle_phase_id: "1"
  voice_assist_listening_phase_id: "2"
  voice_assist_thinking_phase_id: "3"
  voice_assist_replying_phase_id: "4"
  voice_assist_not_ready_phase_id: "10"
  voice_assist_error_phase_id: "11"
  voice_assist_muted_phase_id: "12"
  voice_assist_timer_finished_phase_id: "20"

esphome:
  name: ${name}
  friendly_name: ${friendly_name}
  min_version: 2026.7.0
  on_boot:
    priority: 200
    then:
      - light.turn_on:
          id: lcd_backlight
          brightness: 100%
      - delay: 500ms
      - component.update: atoms3r_lcd
      - script.execute: draw_display
      - delay: 30s
      - if:
          condition:
            lambda: return id(init_in_progress);
          then:
            - lambda: id(init_in_progress) = false;
            - script.execute: draw_display

esp32:
  variant: ESP32S3
  board: esp32-s3-devkitc-1
  flash_size: 8MB
  cpu_frequency: 240MHz
  framework:
    type: esp-idf
    sdkconfig_options:
      CONFIG_ESP32S3_DEFAULT_CPU_FREQ_240: "y"
      CONFIG_ESP32S3_DATA_CACHE_64KB: "y"
      CONFIG_ESP32S3_DATA_CACHE_LINE_64B: "y"

psram:
  mode: octal
  speed: 80MHz

api:
  encryption:
    key: !secret api_encryption_key   # generate yours in the ESPHome Builder
  on_client_connected:
    - script.execute: draw_display
  on_client_disconnected:
    - script.execute: draw_display

ota:
  - platform: esphome
    id: ota_esphome
    encryption:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:                    # adjust to your network or remove it to use DHCP
    static_ip: 192.168.1.60
    gateway: 192.168.1.1
    subnet: 255.255.255.0
    dns1: 8.8.8.8
    dns2: 8.8.4.4
  power_save_mode: NONE
  on_connect:
    - script.execute: draw_display
  on_disconnect:
    then:
      - script.execute: draw_display
logger:
  level: DEBUG
  hardware_uart: USB_SERIAL_JTAG

button:
  - platform: factory_reset
    id: factory_reset_btn
    internal: true

  - platform: template
    name: "Test speaker"
    entity_category: diagnostic
    on_press:
      - switch.turn_on: speaker_enable
      - script.execute:
          id: play_sound
          priority: true
          sound_file: !lambda return id(wake_word_triggered_sound);

binary_sensor:
  - platform: gpio
    pin:
      number: GPIO41
      mode: INPUT_PULLUP
      inverted: true
    id: user_button
    internal: true
    on_multi_click:
      # Quick click toggles mute
      - timing:
          - ON for at least 50ms
          - OFF for at least 50ms
        then:
          - switch.toggle: mute
          - switch.turn_off: timer_ringing

      # Hold for 10 seconds to factory reset
      - timing:
          - ON for at least 10s
        then:
          - button.press: factory_reset_btn

external_components:
  - source: github://m5stack/esphome-yaml/components@main
    components:
      - lp5562
      - es8311
    refresh: 1d

i2c:
  - id: bsp_bus
    sda:
      number: GPIO45
      ignore_strapping_warning: true
    scl:
      number: GPIO0
      ignore_strapping_warning: true
    scan: true

  - id: ext_bus
    sda: GPIO38
    scl: GPIO39
    scan: true

pi4ioe5v6408:
  - id: pi4ioe5v6408_hub
    i2c_id: ext_bus
    address: 0x43

i2s_audio:
  - id: i2s_audio_bus
    i2s_lrclk_pin: GPIO6
    i2s_bclk_pin: GPIO8

spi:
  id: spi_bus
  clk_pin: GPIO15
  mosi_pin: GPIO21

audio_dac:
  - platform: es8311
    id: es8311_dac
    i2c_id: ext_bus
    bits_per_sample: 16bit
    sample_rate: 48000
    use_microphone: false
    use_mclk: false

microphone:
  - platform: i2s_audio
    id: i2s_mic
    sample_rate: 16000
    i2s_din_pin: GPIO7
    bits_per_sample: 16bit
    adc_type: external

speaker:
  - platform: i2s_audio
    id: i2s_speaker
    i2s_dout_pin: GPIO5
    dac_type: external
    sample_rate: 48000
    audio_dac: es8311_dac
    channel: left

media_player:
  - platform: speaker
    name: "Echo Base Player"
    id: echo_base_player
    volume_min: 0.5
    volume_max: 0.8

    announcement_pipeline:
      speaker: i2s_speaker
      format: FLAC
      sample_rate: 48000
      num_channels: 1

    files:
      - id: wake_word_triggered_sound
        file: ${wake_word_trigger_sound_file}

      - id: timer_finished_sound
        file: ${timer_finished_sound_file}

      - id: error_cloud_expired
        file: ${error_cloud_expired_file}

    on_state:
      - logger.log: "Media player state updated"

    on_play:
      - logger.log: "Playback started"

    on_announcement:
      then:
        - logger.log:
            format: "Playing announcement"
            level: DEBUG

        - if:
            condition:
              microphone.is_capturing:
            then:
              - script.execute: stop_wake_word

              - if:
                  condition:
                    lambda: |-
                      return id(wake_word_engine_location).current_option() ==
                             "In Home Assistant";
                  then:
                    - wait_until:
                        not:
                          voice_assistant.is_running:

        - if:
            condition:
              not:
                voice_assistant.is_running:
            then:
              - lambda: |-
                  id(voice_assistant_phase) =
                    ${voice_assist_muted_phase_id};
              - script.execute: draw_display

    on_idle:
      - if:
          condition:
            not:
              voice_assistant.is_running:
          then:
            - script.execute: start_wake_word
            - script.execute: set_idle_or_mute_phase
            - script.execute: draw_display

switch:
  # NS4150B amplifier enable
  - platform: gpio
    name: "Speaker Enable"
    id: speaker_enable
    pin:
      pi4ioe5v6408: pi4ioe5v6408_hub
      number: 0
      mode:
        output: true
    icon: "mdi:volume-high"
    restore_mode: ALWAYS_ON

  - platform: template
    name: "Mute Microphone"
    id: mute
    icon: "mdi:microphone-off"
    optimistic: true
    restore_mode: RESTORE_DEFAULT_OFF
    entity_category: config

    on_turn_off:
      - microphone.unmute:
      - lambda: |-
          id(voice_assistant_phase) =
            ${voice_assist_idle_phase_id};
      - script.execute: draw_display

    on_turn_on:
      - microphone.mute:
      - lambda: |-
          id(voice_assistant_phase) =
            ${voice_assist_muted_phase_id};
      - script.execute: draw_display

  - platform: template
    id: timer_ringing
    optimistic: true
    internal: true
    restore_mode: ALWAYS_OFF

    on_turn_off:
      - lambda: |-
          id(echo_base_player)
            ->make_call()
            .set_command(
              media_player::MediaPlayerCommand::
                MEDIA_PLAYER_COMMAND_REPEAT_OFF
            )
            .set_announcement(true)
            .perform();

          id(echo_base_player)->set_playlist_delay_ms(
            speaker::AudioPipelineType::ANNOUNCEMENT,
            0
          );

      - media_player.stop:
          id: echo_base_player
          announcement: true

      - script.execute: start_wake_word

    on_turn_on:
      - script.execute: stop_wake_word

      - lambda: |-
          id(echo_base_player)
            ->make_call()
            .set_command(
              media_player::MediaPlayerCommand::
                MEDIA_PLAYER_COMMAND_REPEAT_ONE
            )
            .set_announcement(true)
            .perform();

          id(echo_base_player)->set_playlist_delay_ms(
            speaker::AudioPipelineType::ANNOUNCEMENT,
            1000
          );

      - script.execute:
          id: play_sound
          priority: true
          sound_file: !lambda return id(timer_finished_sound);

      - delay: 15min
      - switch.turn_off: timer_ringing

select:
  - platform: template
    entity_category: config
    name: "Wake word engine location"
    id: wake_word_engine_location
    icon: "mdi:account-voice"
    optimistic: true
    restore_value: true

    options:
      - In Home Assistant
      - On device

    initial_option: On device

    on_value:
      - if:
          condition:
            lambda: return !id(init_in_progress);
          then:
            - wait_until:
                lambda: |-
                  return
                    id(voice_assistant_phase) ==
                      ${voice_assist_muted_phase_id} ||
                    id(voice_assistant_phase) ==
                      ${voice_assist_idle_phase_id};

            - if:
                condition:
                  lambda: return x == "In Home Assistant";
                then:
                  - micro_wake_word.stop:
                  - delay: 500ms

                  - if:
                      condition:
                        switch.is_off: mute
                      then:
                        - lambda: id(va).set_use_wake_word(true);
                        - voice_assistant.start_continuous:

            - if:
                condition:
                  lambda: return x == "On device";
                then:
                  - lambda: id(va).set_use_wake_word(false);
                  - voice_assistant.stop:
                  - delay: 500ms

                  - if:
                      condition:
                        switch.is_off: mute
                      then:
                        - micro_wake_word.start:

  - platform: template
    name: "Wake word sensitivity"
    id: wake_word_sensitivity
    optimistic: true
    initial_option: Slightly sensitive
    restore_value: true
    entity_category: config

    options:
      - Slightly sensitive
      - Moderately sensitive
      - Very sensitive

    on_value:
      - lambda: |-
          if (x == "Slightly sensitive") {
            id(okay_nabu).set_probability_cutoff(217);
            id(hey_jarvis).set_probability_cutoff(247);
            id(hey_mycroft).set_probability_cutoff(253);
          } else if (x == "Moderately sensitive") {
            id(okay_nabu).set_probability_cutoff(176);
            id(hey_jarvis).set_probability_cutoff(235);
            id(hey_mycroft).set_probability_cutoff(242);
          } else if (x == "Very sensitive") {
            id(okay_nabu).set_probability_cutoff(143);
            id(hey_jarvis).set_probability_cutoff(212);
            id(hey_mycroft).set_probability_cutoff(237);
          }

micro_wake_word:
  id: mww
  microphone: i2s_mic

  models:
    - model: okay_nabu
      id: okay_nabu

    - model: hey_jarvis
      id: hey_jarvis

    - model: hey_mycroft
      id: hey_mycroft

    - model: ${stop_model_file}
      id: stop
      internal: true

  vad:

  on_wake_word_detected:
    - script.execute:
        id: play_sound
        priority: true
        sound_file: !lambda return id(wake_word_triggered_sound);

    - wait_until:
        condition:
          media_player.is_announcing: echo_base_player
        timeout: 500ms

    - wait_until:
        condition:
          and:
            - not:
                media_player.is_announcing: echo_base_player
            - not:
                speaker.is_playing: i2s_speaker
        timeout: 10s

    - voice_assistant.start:
        wake_word: !lambda return wake_word;

voice_assistant:
  id: va
  microphone: i2s_mic
  media_player: echo_base_player
  micro_wake_word: mww
  noise_suppression_level: 2
  auto_gain: 31dBFS
  volume_multiplier: 2.0

  on_listening:
    - lambda: |-
        id(voice_assistant_phase) =
          ${voice_assist_listening_phase_id};
    - script.execute: draw_display

  on_stt_vad_end:
    - lambda: |-
        id(voice_assistant_phase) =
          ${voice_assist_thinking_phase_id};
    - script.execute: draw_display

  on_tts_start:
    - lambda: |-
        id(voice_assistant_phase) =
          ${voice_assist_replying_phase_id};
    - script.execute: draw_display

  on_end:
    - wait_until:
        condition:
          media_player.is_announcing: echo_base_player
        timeout: 500ms

    - wait_until:
        condition:
          and:
            - not:
                media_player.is_announcing: echo_base_player
            - not:
                speaker.is_playing: i2s_speaker
        timeout: 30s

    - if:
        condition:
          lambda: |-
            return id(wake_word_engine_location).current_option() ==
                   "On device";
        then:
          - lambda: id(va).set_use_wake_word(false);
          - micro_wake_word.start:

    - script.execute: set_idle_or_mute_phase
    - script.execute: draw_display

  on_error:
    - if:
        condition:
          and:
            - lambda: return !id(init_in_progress);
            - lambda: return code != "duplicate_wake_up_detected";
            - lambda: return code != "stt-no-text-recognized";
        then:
          - lambda: |-
              id(voice_assistant_phase) =
                ${voice_assist_error_phase_id};
          - script.execute: draw_display
          - delay: 1s
          - script.execute: set_idle_or_mute_phase
          - script.execute: draw_display

    - if:
        condition:
          lambda: return code == "cloud-auth-failed";
        then:
          - script.execute:
              id: play_sound
              priority: true
              sound_file: !lambda return id(error_cloud_expired);
          - script.execute: draw_display

  on_client_connected:
    - lambda: id(init_in_progress) = false;
    - script.execute: start_wake_word
    - script.execute: set_idle_or_mute_phase
    - script.execute: draw_display

  on_client_disconnected:
    - script.execute: stop_wake_word
    - lambda: |-
        id(voice_assistant_phase) =
          ${voice_assist_not_ready_phase_id};
    - script.execute: draw_display

  on_timer_finished:
    - switch.turn_on: timer_ringing

    - wait_until:
        condition:
          media_player.is_announcing: echo_base_player
        timeout: 5s

    - lambda: |-
        id(voice_assistant_phase) =
          ${voice_assist_timer_finished_phase_id};
    - script.execute: draw_display

globals:
  - id: init_in_progress
    type: bool
    restore_value: false
    initial_value: "true"

  - id: voice_assistant_phase
    type: int
    restore_value: false
    initial_value: ${voice_assist_not_ready_phase_id}

lp5562:
  id: lp5562_led
  i2c_id: bsp_bus
  use_internal_clk: true
  white_current: 17.5

output:
  - platform: lp5562
    id: lp5562_white_channel
    lp5562_id: lp5562_led
    channel: white

light:
  - platform: monochromatic
    name: "LCD Backlight"
    id: lcd_backlight
    output: lp5562_white_channel
    icon: "mdi:television"
    restore_mode: ALWAYS_ON

time:
  - platform: sntp
    id: sntp_time
    servers:
      - time.google.com
    timezone: "America/Fortaleza"
    on_time_sync:
      - script.execute: draw_display

font:
  - file: "gfonts://Roboto"
    id: time_font
    size: 18

  - file: "gfonts://Roboto"
    id: status_font
    size: 16

  - file: "gfonts://Roboto@700"
    id: time_bold_font
    size: 23

  - file: "gfonts://Roboto@400"
    id: date_font
    size: 14

  - file: "gfonts://Roboto@700"
    id: pronto_font
    size: 19

  - file: ${mdi_webfont_file}
    id: mdi_icon_128
    size: 128
    bpp: 4
    glyphs:
      - "\U000F036D" # mdi:mic-mute

color:
  - id: idle_color
    hex: ${idle_illustration_background_color}

  - id: listening_color
    hex: ${listening_illustration_background_color}

  - id: thinking_color
    hex: ${thinking_illustration_background_color}

  - id: replying_color
    hex: ${replying_illustration_background_color}

  - id: loading_color
    hex: ${loading_illustration_background_color}

  - id: error_color
    hex: ${error_illustration_background_color}

  - id: text_yellow
    red: 50%
    green: 50%
    blue: 0%

  - id: text_cyan
    red: 0%
    green: 50%
    blue: 50%

  - id: text_green
    red: 0%
    green: 100%
    blue: 0%

  - id: text_red
    red: 100%
    green: 0%
    blue: 0%

  - id: light_gray
    hex: "CCCCCC"

  - id: text_blue
    hex: "2196F3"

  - id: color_white
    hex: "FFFFFF"

  - id: color_black
    hex: "000000"

image:
  - file: ${error_illustration_file}
    id: casita_error
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${idle_illustration_file}
    id: casita_idle
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${listening_illustration_file}
    id: casita_listening
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${thinking_illustration_file}
    id: casita_thinking
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${replying_illustration_file}
    id: casita_replying
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${loading_illustration_file}
    id: casita_initializing
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${error_no_wifi_illustration_file}
    id: error_no_wifi
    resize: 160x120
    type: RGB
    transparency: alpha_channel

  - file: ${error_no_ha_illustration_file}
    id: error_no_ha
    resize: 160x120
    type: RGB
    transparency: alpha_channel

display:
  - platform: mipi_spi
    id: atoms3r_lcd
    model: M5STACK-ATOMS3R-GC9107
    spi_id: spi_bus
    rotation: 180°
    update_interval: never

    pages:
      - id: idle_page
        lambda: |-
          it.fill(id(idle_color));
          it.image(64, 64, id(casita_idle), ImageAlign::CENTER);
          it.strftime(64, 6, id(time_bold_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 32, id(date_font), id(light_gray), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 96, id(pronto_font), id(text_blue), TextAlign::CENTER, "READY!");

      - id: listening_page
        lambda: |-
          it.fill(id(listening_color));
          it.image(64, 64, id(casita_listening), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(text_yellow), TextAlign::CENTER, "Listening...");

      - id: thinking_page
        lambda: |-
          it.fill(id(thinking_color));
          it.image(64, 64, id(casita_thinking), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(text_cyan), TextAlign::CENTER, "Sending to HA...");

      - id: replying_page
        lambda: |-
          it.fill(id(replying_color));
          it.image(64, 64, id(casita_replying), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(text_green), TextAlign::CENTER, "Replying...");

      - id: error_page
        lambda: |-
          it.fill(id(error_color));
          it.image(64, 64, id(casita_error), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(text_red), TextAlign::CENTER, "Error");

      - id: no_ha_page
        lambda: |-
          it.fill(id(error_color));
          it.image(64, 64, id(error_no_ha), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 100, id(status_font), id(text_red), TextAlign::CENTER, "No HA connection");

      - id: no_wifi_page
        lambda: |-
          it.fill(id(error_color));
          it.image(64, 64, id(error_no_wifi), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 100, id(status_font), id(text_red), TextAlign::CENTER, "No Wi-Fi");

      - id: initializing_page
        lambda: |-
          it.fill(id(loading_color));
          it.image(64, 64, id(casita_initializing), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(color_white), TextAlign::CENTER, "Initializing...");

      - id: muted_page
        lambda: |-
          it.fill(id(color_black));
          it.image(64, 64, id(casita_idle), ImageAlign::CENTER);
          it.strftime(64, 8, id(time_font), id(color_white), TextAlign::CENTER, "%H:%M", id(sntp_time).now());
          it.strftime(64, 26, id(time_font), id(color_white), TextAlign::CENTER, "%d/%m/%Y", id(sntp_time).now());
          it.printf(64, 92, id(status_font), id(text_red), TextAlign::CENTER, "Microphone muted");

script:
  - id: start_wake_word
    mode: restart
    then:
      - if:
          condition:
            and:
              - switch.is_off: mute
              - not:
                  voice_assistant.is_running:
              - lambda: |-
                  return
                    id(wake_word_engine_location).current_option() ==
                    "On device";
          then:
            - lambda: id(va).set_use_wake_word(false);
            - micro_wake_word.start:

      - if:
          condition:
            and:
              - switch.is_off: mute
              - not:
                  voice_assistant.is_running:
              - lambda: |-
                  return
                    id(wake_word_engine_location).current_option() ==
                    "In Home Assistant";
          then:
            - lambda: id(va).set_use_wake_word(true);
            - voice_assistant.start_continuous:

  - id: stop_wake_word
    mode: restart
    then:
      - if:
          condition:
            lambda: |-
              return
                id(wake_word_engine_location).current_option() ==
                "In Home Assistant";
          then:
            - lambda: id(va).set_use_wake_word(false);
            - voice_assistant.stop:

      - if:
          condition:
            lambda: |-
              return
                id(wake_word_engine_location).current_option() ==
                "On device";
          then:
            - micro_wake_word.stop:

  - id: set_idle_or_mute_phase
    mode: restart
    then:
      - if:
          condition:
            switch.is_off: mute
          then:
            - lambda: |-
                id(voice_assistant_phase) =
                  ${voice_assist_idle_phase_id};
          else:
            - lambda: |-
                id(voice_assistant_phase) =
                  ${voice_assist_muted_phase_id};

  - id: play_sound
    mode: restart
    parameters:
      priority: bool
      sound_file: "audio::AudioFile*"
    then:
      - lambda: |-
          if (priority) {
            id(echo_base_player)
              ->make_call()
              .set_command(
                media_player::MediaPlayerCommand::
                  MEDIA_PLAYER_COMMAND_STOP
              )
              .set_announcement(true)
              .perform();
          }

          if (
            id(echo_base_player).state !=
              media_player::MediaPlayerState::
                MEDIA_PLAYER_STATE_ANNOUNCING ||
            priority
          ) {
            id(echo_base_player)->play_file(
              sound_file,
              true,
              false
            );
          }

  - id: draw_display
    mode: restart
    then:
      - if:
          condition:
            lambda: return !id(init_in_progress);
          then:
            - if:
                condition:
                  wifi.connected:
                then:
                  - if:
                      condition:
                        api.connected:
                      then:
                        - lambda: |-
                            switch (id(voice_assistant_phase)) {
                              case ${voice_assist_listening_phase_id}:
                                id(atoms3r_lcd).show_page(listening_page);
                                break;
                              case ${voice_assist_thinking_phase_id}:
                                id(atoms3r_lcd).show_page(thinking_page);
                                break;
                              case ${voice_assist_replying_phase_id}:
                                id(atoms3r_lcd).show_page(replying_page);
                                break;
                              case ${voice_assist_error_phase_id}:
                                id(atoms3r_lcd).show_page(error_page);
                                break;
                              case ${voice_assist_muted_phase_id}:
                                id(atoms3r_lcd).show_page(muted_page);
                                break;
                              case ${voice_assist_not_ready_phase_id}:
                                id(atoms3r_lcd).show_page(no_ha_page);
                                break;
                              default:
                                id(atoms3r_lcd).show_page(idle_page);
                                break;
                            }
                            id(atoms3r_lcd).update();
                      else:
                        - display.page.show: no_ha_page
                        - component.update: atoms3r_lcd
                else:
                  - display.page.show: no_wifi_page
                  - component.update: atoms3r_lcd
          else:
            - display.page.show: initializing_page
            - component.update: atoms3r_lcd

interval:
  # Refreshes the on-screen clock without over-redrawing
  - interval: 30s
    then:
      - if:
          condition:
            lambda: |-
              return
                !id(init_in_progress) &&
                id(voice_assistant_phase) ==
                  ${voice_assist_idle_phase_id};
          then:
            - script.execute: draw_display

text_sensor:
  - platform: wifi_info
    ip_address:
      name: "IP"
    dns_address:
      name: "DNS"
    mac_address:
      name: "MAC"
```

**How it works, in short:**

- **`micro_wake_word`** runs the models locally (okay_nabu, hey_jarvis, hey_mycroft). When a wake word is detected, **`voice_assistant`** starts and talks to Home Assistant's Assist.
- The screen (**`mipi_spi`**, AtomS3R GC9107) has one *page* per phase (idle, listening, thinking, replying, error, muted, no Wi-Fi, no HA); the `draw_display` script picks the page based on the state.
- The **physical button**: a short click mutes/unmutes the microphone; holding it for 10 s does a factory reset.
- Audio over **I²S** (microphone + speaker with an `es8311` DAC); M5Stack external components (`lp5562` for the LED/backlight and `es8311`).
- You can choose the **wake-word engine** (on device or in HA) and the **sensitivity**, plus a timer that plays a sound when it finishes.

Enable **Assist** in Home Assistant, validate it in the **ESPHome Device Builder** and test the wake words.

[Back to Home Assistant](/en/home-assistant/).

Sources: [xiaomi_miscale component](https://esphome.io/components/sensor/xiaomi_miscale.html), [Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy.html), [remote_receiver (IR)](https://esphome.io/components/remote_receiver.html), [OpenThread](https://esphome.io/components/openthread.html), [LVGL](https://esphome.io/components/lvgl/), [ST7789V display](https://esphome.io/components/display/st7789v.html), [http_request](https://esphome.io/components/http_request.html), [GT911 touchscreen](https://esphome.io/components/touchscreen/gt911.html), [voice_assistant](https://esphome.io/components/voice_assistant/index.html), [micro_wake_word](https://esphome.io/components/micro_wake_word.html) and [Nabu Casa and the Open Home Foundation](https://www.nabucasa.com/).
