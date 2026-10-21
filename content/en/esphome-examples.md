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

[Back to Home Assistant](/en/home-assistant/).

Sources: [xiaomi_miscale component](https://esphome.io/components/sensor/xiaomi_miscale.html), [Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy.html), [remote_receiver (IR)](https://esphome.io/components/remote_receiver.html), [OpenThread](https://esphome.io/components/openthread.html), [LVGL](https://esphome.io/components/lvgl/), [ST7789V display](https://esphome.io/components/display/st7789v.html), [http_request](https://esphome.io/components/http_request.html), [GT911 touchscreen](https://esphome.io/components/touchscreen/gt911.html) and [Nabu Casa and the Open Home Foundation](https://www.nabucasa.com/).
