---
level: avancado
title: Exemplos prontos de ESPHome
slug: esphome-exemplos
key: esphome-examples
description: Configurações completas de ESPHome prontas para copiar — balança via Bluetooth, Bluetooth Proxy, receptor de IR, dispositivos Thread e telas — para o seu Home Assistant.
category: DIY & firmware
icon: chip
order: 106
featured: false
reading: 6 exemplos
date: 2026-10-21
updated: 2026-10-21
tags: [ESPHome, ESP32, YAML, Exemplos, Thread]
---

Configurações completas de **ESPHome**, prontas para copiar e adaptar ao seu Home Assistant. Cada exemplo já vem com os dados sensíveis redigidos (MACs, IPs, chaves de API e *datasets* Thread como exemplos) — **troque pelos seus antes de gravar**.

Novo no ESPHome? Comece pelo artigo [Sensores com ESPHome e ESP32](/esphome-esp32/).

## Índice

- [Balança no HA via Bluetooth](#exemplo-balanca)
- [Bluetooth Proxy (ATOM-S3)](#exemplo-bt-proxy)
- [Receptor de infravermelho (IR)](#exemplo-ir)
- [Dispositivo Thread (NanoC6)](#exemplo-thread)
- [Painel de toque (clima, cortinas e ar)](#exemplo-tela)
- [Tela Thread com temperatura e umidade (C6-GEEK)](#exemplo-c6geek)
- [Painel de parede 7" para a casa toda (Waveshare 7B)](#exemplo-painel7b)

## Exemplo pronto: balança no Home Assistant via Bluetooth {#exemplo-balanca}

Um gateway que escuta o anúncio **Bluetooth (BLE)** de balanças e publica o peso no Home Assistant — sem depender da nuvem do fabricante. Roda num **M5Stack ATOM Lite (ESP32)** e cobre dois protocolos: balanças **OKOK/QJ-J** (peso lido direto do anúncio) e **Xiaomi Mi Scale 2** (pelo componente nativo `xiaomi_miscale`, com peso e impedância).

> **Troque pelos seus dados antes de gravar.** Os MACs das balanças, o IP fixo e as chaves `!secret` abaixo são apenas exemplos. Nunca publique MACs, IPs ou senhas reais.

```yaml
# Gateway BLE -> Home Assistant para balanças OKOK e Xiaomi Mi Scale 2
# Hardware: M5Stack ATOM Lite (ESP32-PICO-D4) | Framework: ESP-IDF
# Troque os MACs, o IP fixo e as chaves !secret pelos seus.

esphome:
  name: atom-bt-gateway-balanca
  friendly_name: "ATOM BT GATEWAY BALANCA"

esp32:
  board: m5stack-atom
  framework:
    type: esp-idf

# ---- Conectividade ----
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
  manual_ip:                    # ajuste para a sua rede (ou remova para usar DHCP)
    static_ip: 192.168.1.50
    gateway: 192.168.1.1
    subnet: 255.255.255.0
    dns1: 1.1.1.1
    dns2: 8.8.8.8
  power_save_mode: NONE

# ---- Variáveis de estado interno ----
globals:
  - id: medindo
    type: bool
    restore_value: no
    initial_value: 'false'
  - id: ultimo_peso
    type: float
    restore_value: no
    initial_value: '0'

# ---- LED RGB do ATOM Lite (feedback visual, opcional) ----
light:
  - platform: esp32_rmt_led_strip
    id: status_led
    name: "Balança Status LED"
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

# ---- Escuta BLE ----
esp32_ble_tracker:
  scan_parameters:
    active: true          # pede scan response; não abre conexão GATT
    interval: 320ms
    window: 160ms
  on_ble_advertise:
    - mac_address: AA:BB:CC:DD:EE:FF   # <- MAC da SUA balança OKOK
      then:
        - lambda: |-
            // O contador ocupa o high byte: não filtrar pelo ID completo.
            for (const auto &manu : x.get_manufacturer_datas()) {
              const auto uuid = manu.uuid.get_uuid();
              if (uuid.len != ESP_UUID_LEN_16 || (uuid.uuid.uuid16 & 0xFF) != 0xC0)
                continue;
              const auto &d = manu.data;
              if (d.size() != 13) continue;
              // Confirma o MAC embutido no payload (troque pelos bytes do seu MAC)
              if (!(d[7]==0xAA && d[8]==0xBB && d[9]==0xCC &&
                    d[10]==0xDD && d[11]==0xEE && d[12]==0xFF)) continue;

              uint16_t peso_raw = (uint16_t(d[0]) << 8) | d[1];
              uint8_t  flag     = d[6];
              if (flag != 0x24 && flag != 0x25) continue;
              if (flag == 0x25 && peso_raw == 0) continue;

              float peso = peso_raw / 100.0f;   // kg

              // Não reenviar centenas de valores idênticos à API.
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
                  ESP_LOGI("balanca", "OKOK: Peso=%.2f kg", peso);
                  id(ultimo_peso) = peso;
                  id(balanca_peso).publish_state(peso);
                  id(pisca_ok).execute();
                }
              }
            }

# ---- Sensores publicados no Home Assistant ----
sensor:
  - platform: template
    name: "Balança Peso"
    id: balanca_peso
    update_interval: never
    unit_of_measurement: "kg"
    device_class: weight
    state_class: measurement
    accuracy_decimals: 2
    icon: "mdi:scale-bathroom"

  - platform: template
    name: "Balança Peso (ao vivo)"
    id: balanca_peso_vivo
    update_interval: never
    unit_of_measurement: "kg"
    state_class: measurement
    accuracy_decimals: 2
    icon: "mdi:scale"
    entity_category: diagnostic

  - platform: wifi_signal
    name: "Balança Gateway WiFi"
    update_interval: 120s
    entity_category: diagnostic

  # Xiaomi: compartilha o scanner BLE; única fonte de impedância.
  - platform: xiaomi_miscale
    id: xiaomi_balanca
    mac_address: 11:22:33:44:55:66   # <- MAC da SUA Xiaomi Mi Scale 2
    clear_impedance: true
    weight:
      name: "Xiaomi Peso"
      id: xiaomi_peso
    impedance:
      name: "Xiaomi Impedância"
      id: xiaomi_impedancia

binary_sensor:
  - platform: template
    name: "Balança Medida Estável"
    id: balanca_estavel
    icon: "mdi:check-circle"
    entity_category: diagnostic

  - platform: status
    name: "Balança Gateway Online"

text_sensor:
  - platform: version
    name: "Balança Gateway ESPHome"
    entity_category: diagnostic

switch:
  - platform: restart
    name: "Balança Gateway RESTART"
    id: balanca_gateway_restart
```

**Como funciona, em resumo:**

- O ESP32 apenas **escuta** os anúncios BLE (`esp32_ble_tracker`), sem parear com as balanças.
- No protocolo **OKOK**, o peso vem nos dois primeiros bytes (`peso = (byte0 << 8 | byte1) / 100`). O flag **`0x24`** indica medição instável (ao vivo) e o **`0x25`**, o peso final.
- A impedância da OKOK é ignorada; a **impedância vem apenas da Xiaomi**, pelo componente `xiaomi_miscale`.
- O LED do ATOM pisca verde a cada peso final — um feedback visual opcional.

Valide no **ESPHome Device Builder** (*Validate*), gere as entidades no Home Assistant e teste um componente por vez.

## Exemplo pronto: Bluetooth Proxy com ATOM-S3 {#exemplo-bt-proxy}

Um **Bluetooth Proxy** estende o alcance Bluetooth do Home Assistant: o ESP32 repassa, pela rede, os sinais BLE de dispositivos próximos (sensores, lâmpadas, etiquetas). Aqui, num **M5Stack ATOM-S3 (ESP32-S3)**, ele também traz um LED que muda de cor conforme o Wi-Fi e um pequeno *sniffer* opcional que registra no log os anúncios BLE de lâmpadas **Philips Hue** — útil para diagnóstico.

> **Troque pelos seus dados antes de gravar.** A chave de criptografia da API, a senha de OTA, o IP fixo e as chaves `!secret` abaixo são apenas exemplos. Nunca publique chaves, senhas, MACs ou IPs reais — gere os seus.

```yaml
# Bluetooth Proxy em M5Stack ATOM-S3 (ESP32-S3), com LED de status Wi-Fi
# e um sniffer opcional de anúncios BLE da Philips Hue (diagnóstico).
# Troque a chave da API, a senha de OTA, o IP fixo e as chaves !secret.

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
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder

ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:                    # ajuste para a sua rede (ou remova para usar DHCP)
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
    name: "LED RGB Interno"
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
  # Filtro opcional em C++ (lambda): registra no log apenas anúncios da Philips Hue
  on_ble_advertise:
    then:
      - lambda: |-
          // 1. Filtrar pelo UUID de serviço da Signify (0xFE0F), se disponível
          bool is_hue = false;

          for (auto data : x.get_service_uuids()) {
              if (data.to_string() == "0000fe0f-0000-1000-8000-00805f9b34fb" || data.to_string() == "0XFE0F") {
                  is_hue = true;
              }
          }

          // 2. Filtrar pelos dados de fabricante (Manufacturer Data ID 0xFE0F)
          for (auto data : x.get_manufacturer_datas()) {
              if (data.uuid.to_string() == "0XFE0F" || data.uuid.to_string() == "0000fe0f-0000-1000-8000-00805f9b34fb") {
                  is_hue = true;
              }
          }

          // Se for uma lâmpada Hue, imprime as informações brutas no log
          if (is_hue) {
              ESP_LOGI("HUE_SNIFFER", "Lampada Hue encontrada!");
              ESP_LOGI("HUE_SNIFFER", "  Endereco MAC: %s", x.address_str().c_str());
              ESP_LOGI("HUE_SNIFFER", "  Nome BLE: %s", x.get_name().c_str());
              ESP_LOGI("HUE_SNIFFER", "  Sinal (RSSI): %d dBm", x.get_rssi());

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
    name: "Reiniciar"
  - platform: safe_mode
    name: "Safe Mode"

binary_sensor:
  - platform: status
    name: "Status ESPHome"
    entity_category: diagnostic

sensor:
  - platform: wifi_signal
    name: "Sinal Wi-Fi"
    update_interval: 60s
    entity_category: diagnostic
  - platform: uptime
    name: "Tempo Ligado"
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

**Como funciona, em resumo:**

- `bluetooth_proxy` + `esp32_ble_tracker` fazem o ESP32 repassar ao Home Assistant os sinais BLE que ele enxerga — **ampliando a cobertura Bluetooth** da casa.
- O LED fica **verde** quando o Wi-Fi conecta e **vermelho** quando cai, controlado pelo `script`.
- O bloco `lambda` é um filtro opcional: identifica anúncios da **Philips Hue** (UUID de serviço `0xFE0F`, da Signify) e imprime no log o MAC, o RSSI e os bytes do fabricante — apenas para diagnóstico.
- Sensores de diagnóstico (sinal Wi-Fi, uptime, IP, MAC, SSID) ajudam a monitorar o dispositivo; os botões **Reiniciar** e **Safe Mode** facilitam a recuperação.

Valide no **ESPHome Device Builder** (*Validate*) e teste um componente por vez.

## Exemplo pronto: receptor de infravermelho (IR) no Home Assistant {#exemplo-ir}

Quer que o Home Assistant "aprenda" os códigos do controle remoto da TV, do ar-condicionado ou do som? Um **receptor de infravermelho** ligado a um ESP32 captura esses sinais. Com `remote_receiver` e `dump: all`, cada botão pressionado aparece no log do ESPHome com o protocolo e o código — pronto para reutilizar numa automação ou num controle virtual.

> **Troque pelos seus dados antes de gravar.** A chave de criptografia da API, o IP fixo, o DNS e as chaves `!secret` abaixo são apenas exemplos. Nunca publique chaves, senhas ou IPs reais — gere os seus.

```yaml
# Receptor de infravermelho (IR) em ESP32, exposto ao Home Assistant.
# Troque a chave da API, o IP fixo, o DNS e as chaves !secret pelos seus.

esphome:
  name: esp32-ir-receiver-escritorio
  friendly_name: "ESP32-IR-RECEIVER-ESCRITORIO"

esp32:
  board: esp32-devkit-v1
  variant: esp32
  framework:
    type: esp-idf

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder

ota:
  - platform: esphome
    encryption:

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  power_save_mode: NONE
  manual_ip:                    # ajuste para a sua rede (ou remova para usar DHCP)
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
  dump: all          # registra no log os códigos de todos os protocolos
  tolerance: 25%

# Expõe o receptor à integração de infravermelho do Home Assistant.
infrared:
  - platform: ir_rf_proxy
    id: receptor_lg_escritorio
    name: "Receptor IR LG ESCRITORIO"
    receiver_frequency: 38kHz
    remote_receiver_id: ir_rx
    icon: "mdi:remote"

button:
  - platform: restart
    name: "Reiniciar"
  - platform: safe_mode
    name: "Safe Mode"

binary_sensor:
  - platform: status
    name: "Status ESPHome"
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

**Como funciona, em resumo:**

- Um **sensor de IR** (por exemplo VS1838B/TSOP, 38 kHz) é ligado ao pino `GPIO27`, com `pullup`.
- `remote_receiver` com `dump: all` **decodifica e registra no log** os sinais de vários protocolos — é assim que você descobre o código de cada botão.
- O bloco `infrared` expõe o receptor à integração de infravermelho do Home Assistant.
- Sensores de diagnóstico (IP, DNS, MAC) e os botões **Reiniciar** e **Safe Mode** ajudam na manutenção.

Confira a pinagem do seu receptor (VCC, GND e sinal) e valide no **ESPHome Device Builder** antes de gravar.

## Exemplo pronto: dispositivo Thread com M5Stack NanoC6 {#exemplo-thread}

**Thread** é uma rede sem fio de malha (*mesh*), de baixo consumo, que serve de base para o **Matter**. O **M5Stack NanoC6 (ESP32-C6)** tem o rádio 802.15.4 necessário e, com o componente `openthread`, entra na sua rede Thread como um dispositivo FTD (roteador). O LED RGB sinaliza o estado: pisca **vermelho** sem conexão com o Home Assistant e fica **azul** quando conecta.

> **Dado MUITO sensível.** O campo `tlv` (o *dataset*) do Thread contém a **chave da sua rede** — quem tiver esse valor entra na sua malha. Nunca o publique. A chave da API e os demais dados abaixo também são exemplos; gere os seus.

```yaml
# M5Stack NanoC6 (ESP32-C6) como dispositivo Thread (OpenThread).
# Troque a chave da API e, principalmente, o dataset TLV da sua rede Thread.

esphome:
  name: nanoc6-thread
  friendly_name: "NanoC6 Thread"
  on_boot:
    # Prioridade -10: executa só depois que luzes e switches já existem.
    priority: -10
    then:
      - switch.turn_on: pwr_g19   # garante a energia do LED RGB
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
      CONFIG_ESP_TASK_WDT_TIMEOUT_S: "60"   # watchdog maior p/ FTD (init pode demorar)
      CONFIG_PM_ENABLE: "n"
      CONFIG_ESP_INT_WDT_TIMEOUT_MS: "2000"

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder
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

# IPv6 é necessário para o Thread
network:
  enable_ipv6: true

# Rádio Thread. ATENÇÃO: o 'tlv' (dataset) contém a CHAVE DA SUA REDE THREAD.
# Nunca publique o seu; cole o dataset da sua rede aqui.
openthread:
  device_type: FTD
  tlv: "COLE_AQUI_O_DATASET_TLV_DA_SUA_REDE_THREAD"
  force_dataset: true
  output_power: 20dBm

# ===== Periféricos do M5 Nano-C6 =====

# LED de diagnóstico nativo do ESPHome no pino 7
status_led:
  pin: GPIO7

switch:
  - platform: gpio
    pin: GPIO19
    id: pwr_g19
    name: "NanoC6 Thread Energia Periféricos"
    restore_mode: ALWAYS_ON
  - platform: restart
    id: restart_switch
    name: "NanoC6 Thread Restart Switch"

# LED RGB (GPIO20)
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
    name: "Reiniciar Nano C6"

# Botão físico (GPIO9): segurar por 5s reinicia
binary_sensor:
  - platform: gpio
    id: btn_gpio9
    name: "Botão M5Stack"
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
    name: "NanoC6 Thread Status de Conexão"
    id: status_conexao

# ===== Sensores de diagnóstico =====
sensor:
  - platform: uptime
    name: "NanoC6 Thread Tempo de Atividade"
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

**Como funciona, em resumo:**

- `openthread` com `device_type: FTD` faz o NanoC6 participar da rede Thread; o `tlv` é o *dataset* que descreve a rede (canal, PAN ID e a **chave**) — por isso é sigiloso. O `network: enable_ipv6` é obrigatório.
- O LED RGB dá feedback visual: **azul** com o HA conectado, **vermelho piscando** sem conexão.
- O `switch` em `GPIO19` liga a energia dos periféricos do NanoC6 (incluindo o LED); o botão físico em `GPIO9`, segurado por 5 s, reinicia.
- Os `text_sensor` do `openthread_info` expõem o diagnóstico da rede (IP, canal, papel, PAN ID etc.) no Home Assistant.

Obtenha o *dataset* TLV da sua rede Thread (pelo Home Assistant ou pelo seu Border Router) e valide no **ESPHome Device Builder** antes de gravar.

## Exemplo pronto: painel de toque (clima, cortinas e ar) {#exemplo-tela}

Uma telinha de toque na parede que mostra **relógio, data e clima** e controla **cortinas, ventilador e ar-condicionado** direto no Home Assistant. Este exemplo usa uma placa **Guition JC3248W535 (ESP32-S3, 3,5" 320×480)** com a biblioteca de interface **LVGL** do ESPHome, em três páginas e uma barra de navegação inferior.

> **Personalize antes de gravar.** No topo, o bloco `substitutions` define as **entidades do seu Home Assistant** (clima, ventilador, ar) e a cidade — ajuste para as suas. A chave da API é um exemplo; gere a sua. Os nomes `cover.cortina_1..3` também são exemplos.

```yaml
substitutions:
  device_name: tela-clima
  friendly_name: "Tela Clima"
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

# Placa: Guition JC3248W535C_I_Y — ESP32-S3, tela QSPI 3.5" 320x480 (AXS15231B),
# toque capacitivo no mesmo chip via I2C. Confirme flash/PSRAM da sua unidade
# (16MB / PSRAM octal é o padrão dessa família; se a compilação/boot falhar,
# tente psram.mode: quad).
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
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder

ota:
  - platform: esphome
    encryption:

# Necessário para a Home Assistant "empurrar" a entidade de clima para o
# dispositivo E para o dispositivo chamar serviços de volta (cortinas/ar/vent).
# Só funciona depois que o device for adicionado à integração ESPHome no HA.

time:
  - platform: sntp
    id: sntp_time
    timezone: "${tz}"
    servers:
      - time.google.com
      - time1.google.com
      - pool.ntp.org

# --- Barramentos ---------------------------------------------------------
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

# --- Tela + toque (AXS15231B, driver nativo mipi_spi) -----------------------
display:
  - id: main_display
    platform: mipi_spi
    model: JC3248W535
    rotation: 0°   # 0° = retrato 320x480 nesta placa; troque p/ 90°/270° se vier deitada
    data_rate: 40MHz
    update_interval: never
    auto_clear_enabled: false

touchscreen:
  - id: main_touchscreen
    platform: axs15231

# --- Fontes ------------------------------------------------------------
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

  # Ícones grandes do clima (sol / nuvem / chuva)
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
      - "\U000F0596"  # weather-pouring (chuva)

  # Ícone de WiFi (pequeno)
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

  # Ícones da barra de navegação inferior
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_nav
    size: 30
    bpp: 4
    glyphs:
      - "\U000F02DC"  # home
      - "\U000F111C"  # window-shutter (cortinas)
      - "\U000F001B"  # air-conditioner

  # Ícones dos botões de controle
  - file:
      type: web
      url: "https://github.com/Templarian/MaterialDesign-Webfont/raw/master/fonts/materialdesignicons-webfont.ttf"
    id: font_icon
    size: 40
    bpp: 4
    glyphs:
      - "\U000F0737"  # arrow-up-bold (abrir)
      - "\U000F072E"  # arrow-down-bold (fechar)
      - "\U000F04DB"  # stop (parar)
      - "\U000F0425"  # power
      - "\U000F0210"  # fan
      - "\U000F001B"  # air-conditioner
      - "\U000F111C"  # window-shutter

# --- Sensores ------------------------------------------------------------
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

  # Ar-condicionado: temperatura atual da sala
  - platform: homeassistant
    id: ha_ac_current
    entity_id: ${ha_ac_entity}
    attribute: current_temperature
    internal: true
    on_value:
      - lvgl.label.update:
          id: ac_current_label
          text:
            format: "Atual: %.1f°C"
            args: [x]
            if_nan: "Atual: --"

  # Ar-condicionado: temperatura alvo (setpoint)
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

  # Ventilador: velocidade atual (%)
  - platform: homeassistant
    id: ha_fan_pct
    entity_id: ${ha_fan_entity}
    attribute: percentage
    internal: true
    on_value:
      - lvgl.label.update:
          id: fan_speed_label
          text:
            format: "Velocidade: %.0f%%"
            args: [x]
            if_nan: "Velocidade: --"

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
            if (c == "sunny") return std::string("Ensolarado");
            if (c == "clear-night") return std::string("Céu limpo");
            if (c == "partlycloudy") return std::string("Parcialmente nublado");
            if (c == "cloudy") return std::string("Nublado");
            if (c == "fog") return std::string("Neblina");
            if (c == "windy" || c == "windy-variant") return std::string("Ventania");
            if (c == "rainy") return std::string("Chuva");
            if (c == "pouring") return std::string("Chuva forte");
            if (c == "lightning") return std::string("Tempestade");
            if (c == "lightning-rainy") return std::string("Tempestade com chuva");
            if (c == "hail") return std::string("Granizo");
            if (c == "snowy") return std::string("Neve");
            if (c == "snowy-rainy") return std::string("Chuva com neve");
            return std::string("Indisponível");

  # Ar-condicionado: modo atual (off/cool/dry/...) — atualiza rótulo e cor do power
  - platform: homeassistant
    id: ha_ac_mode
    entity_id: ${ha_ac_entity}
    internal: true
    on_value:
      - lvgl.label.update:
          id: ac_mode_label
          text: !lambda |-
            std::string m = x;
            if (m == "off") return std::string("Desligado");
            if (m == "cool") return std::string("Refrigerar");
            if (m == "dry") return std::string("Desumidificar");
            if (m == "fan_only") return std::string("Ventilar");
            if (m == "heat") return std::string("Aquecer");
            if (m == "heat_cool") return std::string("Automático");
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

# --- Relógio / data (atualizados localmente, não dependem do HA) -----------
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
            if (!t.is_valid()) return std::string("Sincronizando...");
            static const char *dias[] = {"", "Domingo", "Segunda-feira", "Terça-feira",
                "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"};
            static const char *meses[] = {"", "Janeiro", "Fevereiro", "Março", "Abril",
                "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"};
            char buf[48];
            snprintf(buf, sizeof(buf), "%s, %d de %s de %d",
                dias[t.day_of_week], t.day_of_month, meses[t.month], t.year);
            return std::string(buf);

# --- Interface LVGL ----------------------------------------------------
lvgl:
  displays:
    - main_display
  touchscreens:
    - main_touchscreen
  bg_color: 0x000000

  # Barra de navegação inferior — sempre visível sobre todas as páginas
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
    # ===================== PÁGINA 1: CLIMA / RELÓGIO =====================
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
            text: "Sincronizando..."
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
            text: "Aguardando dados..."
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

    # ===================== PÁGINA 2: CORTINAS =====================
    - id: page_cortinas
      bg_color: 0x000000
      widgets:
        - label:
            text: "Cortinas"
            text_font: font_text_md
            text_color: 0xFFFFFF
            align: TOP_MID
            y: 14

        # ---- Linha: Todas ----
        - label:
            text: "Todas"
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

        # ---- Linha: Cortina 1 ----
        - label:
            text: "Cortina 1"
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

        # ---- Linha: Cortina 2 ----
        - label:
            text: "Cortina 2"
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

        # ---- Linha: Cortina 3 ----
        - label:
            text: "Cortina 3"
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

    # ===================== PÁGINA 3: VENTILADOR + AR =====================
    - id: page_ar
      bg_color: 0x000000
      widgets:
        # ---------- Ventilador ----------
        - label:
            text: "\U000F0210"
            text_font: font_icon
            text_color: 0x2196F3
            align: TOP_LEFT
            x: 14
            y: 10
        - label:
            text: "Ventilador"
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
              - label: {text: "Desl", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
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
              - label: {text: "Baixa", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
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
              - label: {text: "Média", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
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
              - label: {text: "Alta", text_font: font_text_md, text_color: 0xFFFFFF, align: CENTER}
            on_click:
              - homeassistant.action:
                  action: fan.set_percentage
                  data: {entity_id: "${ha_fan_entity}", percentage: "100"}

        - label:
            id: fan_speed_label
            text: "Velocidade: --"
            text_font: font_text_md
            text_color: 0x90A4AE
            align: TOP_MID
            y: 124

        # ---------- Ar-condicionado ----------
        - label:
            text: "\U000F001B"
            text_font: font_icon
            text_color: 0x2196F3
            align: TOP_LEFT
            x: 14
            y: 166
        - label:
            text: "Ar Sala"
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
            text: "Atual: --"
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

**Como funciona, em resumo:**

- `substitutions` no topo centraliza o que você troca: nome do dispositivo, **entidades do HA** (`weather`, `fan`, `climate`), cidade e fuso — sem procurar no meio do arquivo.
- `display` (driver `mipi_spi`, modelo `JC3248W535`) + `touchscreen` (`axs15231`) ativam a tela e o toque; `lvgl` desenha a interface em 3 páginas com barra inferior.
- Sensores `platform: homeassistant` **puxam** dados do HA (temperatura do clima, modo do ar, velocidade do ventilador) e atualizam os rótulos; os botões chamam serviços de volta (`homeassistant.action`) para abrir/fechar cortinas, ligar o ar e mudar a velocidade.
- O relógio e a data são gerados localmente (via `sntp`), sem depender do HA.
- **Hardware:** confirme a flash/PSRAM da sua unidade; se o boot falhar, teste `psram.mode: quad`. A rotação da tela pode precisar de `90°`/`270°`.

Ajuste as `substitutions` para as suas entidades e valide no **ESPHome Device Builder** antes de gravar.

## Exemplo pronto: tela Thread com temperatura e umidade (Waveshare C6-GEEK) {#exemplo-c6geek}

A placa **Waveshare ESP32-C6-GEEK** junta três coisas num dispositivo só: conexão **Thread**, uma **telinha ST7789V** (240×135) e um **sensor DHT** (AM2302/DHT11) de temperatura e umidade. A tela mostra **relógio, data e as leituras do sensor**, enquanto o dispositivo entra na sua rede Thread.

> **Dado MUITO sensível.** O campo `tlv` (o *dataset*) do Thread contém a **chave da sua rede** — nunca o publique. A chave da API também é um exemplo; gere a sua.

```yaml
# Waveshare ESP32-C6-GEEK: dispositivo Thread com tela ST7789V e sensor DHT.
# Troque a chave da API e, principalmente, o dataset TLV da sua rede Thread.

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
      CONFIG_ESP_TASK_WDT_TIMEOUT_S: "60"   # watchdog maior p/ FTD (init pode demorar)
      CONFIG_PM_ENABLE: "n"
      CONFIG_ESP_INT_WDT_TIMEOUT_MS: "2000"

logger:
  level: DEBUG

api:
  encryption:
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder
  # Mantém a tela funcionando mesmo sem conexão com o HA.
  reboot_timeout: 0s

ota:
  - platform: esphome
    encryption:

# Thread usa IPv6.
network:
  enable_ipv6: true

# Rádio Thread. ATENÇÃO: o 'tlv' (dataset) contém a CHAVE DA SUA REDE THREAD.
# Nunca publique o seu; cole o dataset da sua rede aqui.
openthread:
  device_type: FTD
  force_dataset: true
  tlv: "COLE_AQUI_O_DATASET_TLV_DA_SUA_REDE_THREAD"
  output_power: 20dBm

# Horário do Google, exibido no fuso de Fortaleza.
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

# As fontes são baixadas durante a preparação do firmware.
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
    name: "Waveshare ESP32-C6-GEEK Tempo de Atividade"
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
    # Geometria nativa; a rotação resulta em 240 × 135.
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

      // Hora e data.
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
          TextAlign::TOP_CENTER, "Sincronizando hora..."
        );
      }

      // Separadores e títulos.
      it.line(8, 57, 231, 57, cinza);
      it.line(120, 67, 120, 125, cinza);

      it.print(
        60, 65, id(fonte_pequena), cinza,
        TextAlign::TOP_CENTER, "Temperatura"
      );
      it.print(
        180, 65, id(fonte_pequena), cinza,
        TextAlign::TOP_CENTER, "Umidade"
      );

      // Leituras do DHT.
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
    name: "Waveshare ESP32-C6-GEEK Status de Conexão"
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

**Como funciona, em resumo:**

- `openthread` (FTD) conecta a placa à rede Thread; o `tlv` é o *dataset* sigiloso (contém a chave da rede). O `network: enable_ipv6` é obrigatório.
- Um sensor **DHT** no `GPIO11` lê temperatura e umidade a cada 10 s.
- O `display` **ST7789V** desenha, no `lambda`, o relógio (via `sntp`), a data e as duas leituras — tudo localmente, sem depender do HA para a tela (`reboot_timeout: 0s` mantém a tela viva mesmo sem o HA).
- Sensores de diagnóstico (uptime, status, dados do Thread) ajudam a monitorar.

Confira o sensor e a pinagem da sua placa, e valide no **ESPHome Device Builder** antes de gravar.

## Exemplo de referência: painel de parede 7" para a casa toda (Waveshare 7B) {#exemplo-painel7b}

Um **painel de parede de 7"** (Waveshare ESP32-S3-Touch-LCD-7B, 1024×600) que vira o **controle central da casa**: mostra relógio, clima com previsão de 5 dias, cotação do **Bitcoin** (com mini-gráfico) e uma página por cômodo com **luzes (liga/desliga + brilho), ar-condicionado, ventilador e cortinas** — tudo via Home Assistant, com LVGL v9.

Por ser grande e depender de arquivos próprios, vai aqui como **referência comentada** (trechos-chave), não o arquivo inteiro.

> **Este exemplo NÃO é autossuficiente.** Ele precisa acompanhar:
> - **`waveshare_7b/panel_data.h`** — um *header* C++ com a lógica do Bitcoin (parsing da Coinbase, mini-gráfico) e a função `condition_pt()`, que traduz as condições do clima;
> - as **imagens dos cômodos** (`waveshare_7b/assets/*.jpg`).
>
> Requer **ESPHome 2026.9+** e, no HA, a opção **"Permitir que o dispositivo realize ações do Home Assistant"** ativada. A chave da API e o IP fixo são apenas exemplos — gere/ajuste os seus.

**1. Base (placa, PSRAM, API e Wi-Fi):**

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
    - waveshare_7b/panel_data.h   # header C++ (lógica do Bitcoin, condition_pt) — precisa acompanhar
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
    key: !secret api_encryption_key   # gere a sua no ESPHome Builder
  reboot_timeout: 0s                   # mantém a tela viva mesmo sem o HA

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  # manual_ip opcional — ajuste à sua rede ou remova para usar DHCP
```

**2. Tela RGB + toque (a parte mais sensível do hardware):**

```yaml
# Tela RGB 1024x600 (driver nativo mipi_rgb) + toque GT911 no barramento I2C.
# Um expansor I2C (waveshare_io_ch32v003) controla reset/enable/backlight.
display:
  - platform: mipi_rgb
    id: disp1
    model: RPI
    dimensions: { width: 1024, height: 600 }
    color_order: RGB
    pclk_frequency: 30MHz
    pclk_inverted: true
    # pinos de dados e sincronismo conforme a placa (ver config completa)
    update_interval: never
    auto_clear_enabled: false

touchscreen:
  - platform: gt911
    id: touch_panel
    display: disp1
    i2c_id: touch_bus
    address: 93
```

**3. Cotação do Bitcoin (requisição HTTP à Coinbase, sem depender do HA):**

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

**4. Padrão de controle por entidade (repetido para cada luz/cômodo):**

```yaml
# Um sensor lê o brilho da luz no HA e move o slider da tela:
sensor:
  - platform: homeassistant
    id: level_light_led_sala
    entity_id: light.led_sala
    attribute: brightness
    on_value:
      - lvgl.slider.update:
          id: slider_light_led_sala
          value: !lambda "return std::isfinite(x) ? (int)lroundf(x * 100.0f / 255.0f) : 0;"

# E, dentro da página do cômodo, o botão/slider chama o serviço de volta:
#   button (toggle) + slider (brilho) -> homeassistant.action: light.toggle / light.turn_on
```

**Como funciona, em resumo:**

- A tela usa o driver nativo **`mipi_rgb`** (1024×600) e o toque **`gt911`**; um expansor I²C (`waveshare_io_ch32v003`) cuida de reset, enable e backlight.
- Dezenas de sensores **`platform: homeassistant`** espelham o estado das entidades (brilho, modo do ar, estado das cortinas) e atualizam os widgets LVGL; os botões e sliders chamam serviços de volta com **`homeassistant.action`**.
- O relógio, a previsão (via `weather.get_forecasts` do HA) e o **Bitcoin** (API da Coinbase) são atualizados por `interval`/`script`.
- A interface tem uma **página principal** (clima + BTC + atalhos por cômodo) e **uma página por cômodo**, com rolagem.

Trate este exemplo como um **ponto de partida avançado**: o arquivo completo (com `panel_data.h` e as imagens) é extenso e específico da casa.

[Voltar ao Home Assistant](/home-assistant/).

Fontes: [componente xiaomi_miscale](https://esphome.io/components/sensor/xiaomi_miscale.html), [Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy.html), [remote_receiver (IR)](https://esphome.io/components/remote_receiver.html), [OpenThread](https://esphome.io/components/openthread.html), [LVGL](https://esphome.io/components/lvgl/), [display ST7789V](https://esphome.io/components/display/st7789v.html), [http_request](https://esphome.io/components/http_request.html), [touchscreen GT911](https://esphome.io/components/touchscreen/gt911.html) e [Nabu Casa e Open Home Foundation](https://www.nabucasa.com/).
