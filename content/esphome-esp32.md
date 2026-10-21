---
level: avancado
title: Sensores com ESPHome e ESP32
slug: esphome-esp32
description: Monte sensores de temperatura, presença e energia com ESP32 e ESPHome, sem programar em C: componentes, primeiro projeto e integração com o HA.
category: DIY & firmware
icon: chip
order: 105
featured: true
reading: 5 min de leitura
date: 2026-09-22
tags: [ESPHome, ESP32, DIY, YAML, Sensores]
---

Um sensor que cabe exatamente onde você precisa. Um botão que ativa sua cena favorita. Uma telinha com a temperatura do quarto. **ESP32 + ESPHome** permite criar esses pequenos projetos e conectá-los ao Home Assistant.

**IoT** significa objetos conectados trocando informações. **DIY** é fazer você mesmo. Aqui, sua placa conversa com a central pela rede local; não precisa de um aplicativo de fabricante para cada projeto.

## Duas formas de começar

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/esp32.webp" target="_blank" rel="noopener" aria-label="Ampliar: ESP32-DevKitC: placa de uso geral para conectar sensores e outros componentes."><img src="/static/img/ha-features/esp32.webp" width="900" height="389" alt="ESP32-DevKitC: placa de uso geral para conectar sensores e outros componentes." loading="lazy" decoding="async"></a><figcaption>ESP32-DevKitC: placa de uso geral para conectar sensores e outros componentes. · <a class="ext" href="https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

As placas ESP32 de desenvolvimento oferecem conexões para sensores, botões e telas. Existem muitas variantes: confira o chip, a pinagem, a memória e os componentes antes de seguir uma receita.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/atom-s3.webp" target="_blank" rel="noopener" aria-label="Ampliar: M5Stack ATOM-S3: ESP32-S3 com tela, botão e conectores em uma caixinha."><img src="/static/img/ha-features/atom-s3.webp" width="800" height="800" alt="M5Stack ATOM-S3: ESP32-S3 com tela, botão e conectores em uma caixinha." loading="lazy" decoding="async"></a><figcaption>M5Stack ATOM-S3: ESP32-S3 com tela, botão e conectores em uma caixinha. · <a class="ext" href="https://docs.m5stack.com/en/core/AtomS3" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

O **ATOM-S3** inclui uma pequena tela e um botão, úteis para controles e informações. A configuração da tela e de seus componentes é específica. Ele não deve ser confundido com **ATOM Echo**, que possui hardware de áudio e tem um tutorial oficial para usar o Assist.

## ESPHome Device Builder: o painel dos seus projetos

O **ESPHome** é um projeto de código aberto da Open Home Foundation, apoiado pela Nabu Casa. O **Device Builder** pode ser instalado como App no HAOS e organiza seus dispositivos pelo navegador.

<figure class="feature-figure"><a href="/static/img/ha-features/esphome-builder.webp" target="_blank" rel="noopener" aria-label="Ampliar: Tela oficial do ESPHome Device Builder, com dispositivos e seu estado de conexão."><img src="/static/img/ha-features/esphome-builder.webp" width="1000" height="667" alt="Tela oficial do ESPHome Device Builder, com dispositivos e seu estado de conexão." loading="lazy" decoding="async"></a><figcaption>Tela oficial do ESPHome Device Builder, com dispositivos e seu estado de conexão. · <a class="ext" href="https://esphome.io/install/getting-started/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

1. Em **Configurações → Apps**, abra a loja e instale **ESPHome Device Builder**.
2. Inicie o App e abra a interface web.
3. Escolha **Create device / Criar dispositivo** e siga o assistente de nova configuração.
4. Confirme o tipo de placa e a rede Wi-Fi.
5. Use **Install / Instalar** e siga a opção de gravação por USB. Pelo navegador, use Chrome ou Edge no computador, com acesso seguro e suporte a Web Serial.
6. Adicione o dispositivo descoberto em **Configurações → Dispositivos e serviços → ESPHome**.

Após a primeira instalação e com a rede funcionando, muitas atualizações podem ser enviadas por Wi-Fi. O caminho exato depende da placa e da configuração.

## Preciso saber programar?

Você não precisa começar escrevendo C++. O ESPHome usa **YAML**, um arquivo que descreve os componentes e o que eles devem fazer. O assistente monta a base; projetos prontos reduzem bastante o trabalho. Sensores e telas personalizados ainda podem exigir edição desse arquivo.

Uma **IA pode ser uma boa tutora**: explicar cada parte, adaptar um exemplo e ajudar a interpretar erros. Um pedido útil é:

> “Tenho esta placa ESP32 e este sensor. Use a documentação atual do ESPHome, explique as conexões e proponha uma configuração mínima. Não invente pinos; indique o que preciso confirmar.”

Informe o modelo exato e não inclua senhas reais no pedido. Compare a resposta com a documentação, use **Validate / Validar** e teste um componente por vez. Uma configuração que compila ainda precisa corresponder à ligação física.

## Voz com ESP32

Com microfone, alto-falante e configuração compatíveis, um dispositivo ESP32 pode servir como ponto de voz para o **Assist**. O [tutorial oficial do ATOM Echo](https://www.home-assistant.io/voice_control/thirteen-usd-voice-remote/) oferece instalação pelo navegador.

A placa captura e reproduz áudio; o reconhecimento e a resposta podem usar processamento local no sistema ou serviços de nuvem, conforme a configuração. Não é necessário começar por voz: um botão de cena costuma ser um projeto mais simples.

## Seu primeiro projeto

Comece com um **sensor de temperatura ou botão alimentado por USB**, em baixa tensão. Depois que ele aparecer no Home Assistant, crie a automação pelo editor visual. Projetos ligados à rede elétrica exigem componentes adequados e instalação por profissional qualificado.

## Exemplo pronto: balança no Home Assistant via Bluetooth

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

[Voltar ao Home Assistant](/home-assistant/).

Fontes: [iniciar no ESPHome](https://esphome.io/install/getting-started/), [instalar ESPHome](https://esphome.io/install/), [ESP32-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [ATOM-S3](https://docs.m5stack.com/en/core/AtomS3), [componente xiaomi_miscale](https://esphome.io/components/sensor/xiaomi_miscale.html) e [Nabu Casa e Open Home Foundation](https://www.nabucasa.com/).
