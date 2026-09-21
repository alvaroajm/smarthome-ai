---
title: ESPHome e ESP32: construa seus próprios dispositivos
slug: esphome-esp32
description: Como transformar um ESP32 de vinte reais em sensor, interruptor ou controlador integrado ao Home Assistant — com YAML, sem escrever uma linha de C++.
category: DIY & firmware
icon: chip
order: 5
featured: true
reading: 12 min de leitura
date: 2026-09-21
tags: [ESPHome, ESP32, DIY, YAML, Sensores]
---

O ESPHome é o atalho mais elegante da casa inteligente: você descreve o dispositivo em **YAML**, ele compila
um firmware sob medida, grava no microcontrolador e o aparelho aparece sozinho no Home Assistant — com
atualização por Wi-Fi para sempre.

## Por que isso muda o jogo

- **Sem nuvem e sem app**: o ESP32 conversa direto com o Home Assistant pela API nativa (criptografada).
- **Sem programação**: nada de Arduino IDE, bibliotecas e conflitos de versão.
- **Atualização OTA**: subiu uma mudança no YAML, o dispositivo se atualiza pelo ar.
- **Custo**: um sensor comercial de presença custa o equivalente a três ESP32 com sensores.

## Qual placa escolher

| Placa | Boa para | Observação |
|---|---|---|
| **ESP32 (clássico)** | Uso geral, Bluetooth | Melhor custo-benefício; muitos exemplos |
| **ESP32-S3** | Voz, câmera, telas | Mais RAM e PSRAM |
| **ESP32-C6** | Futuro: **Thread/Matter** e Wi-Fi 6 | Suporte em amadurecimento |
| **ESP8266** | Projetos mínimos | Sem Bluetooth; evite em projetos novos |
| **M5Stack ATOM / ATOM Echo** | Protótipo pronto em caixinha | Ótimo para satélites de voz |

!!! dica "Compre com USB-C e antena externa quando possível"
    Placas com conector de antena resolvem casos de Wi-Fi fraco em áreas externas e garagens.

## O primeiro dispositivo, do zero

Instale o add-on **ESPHome Device Builder** no Home Assistant (*Configurações → Add-ons*). Crie um novo
dispositivo, conecte a placa por USB e grave a primeira vez pelo navegador — depois disso, só OTA.

Um sensor de temperatura e umidade completo cabe em 30 linhas:

```yaml
esphome:
  name: sensor-varanda
  friendly_name: Sensor da Varanda

esp32:
  board: esp32dev
  framework:
    type: esp-idf

logger:
api:
  encryption:
    key: !secret api_key_varanda
ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  # Cria um ponto de acesso de resgate se o Wi-Fi sumir
  ap:
    ssid: "Varanda Fallback"

sensor:
  - platform: dht
    pin: GPIO4
    model: DHT22
    temperature:
      name: "Temperatura da varanda"
      filters:
        - median:
            window_size: 5
    humidity:
      name: "Umidade da varanda"
    update_interval: 60s

  - platform: wifi_signal
    name: "Sinal Wi-Fi"
    update_interval: 120s
```

Salve, clique em *Install → Wirelessly* e o dispositivo aparece no Home Assistant com as entidades prontas.

## Projetos que valem o fim de semana

### 1. Sensor de presença real (mmWave)
Sensores PIR só detectam movimento — você fica parado lendo e a luz apaga. Um sensor de radar de onda
milimétrica (LD2410, LD2450) detecta **presença**, inclusive de quem está imóvel:

```yaml
uart:
  tx_pin: GPIO17
  rx_pin: GPIO16
  baud_rate: 256000
  parity: NONE
  stop_bits: 1

ld2410:

binary_sensor:
  - platform: ld2410
    has_target:
      name: "Presença"
    has_moving_target:
      name: "Movimento"

number:
  - platform: ld2410
    timeout:
      name: "Tempo até considerar vazio"
```

### 2. Interruptor de parede que mantém a tecla física
Um módulo relé atrás do interruptor preserva o uso normal da casa e adiciona controle remoto:

```yaml
switch:
  - platform: gpio
    pin: GPIO12
    id: rele_corredor
    name: "Luz do corredor"
    restore_mode: RESTORE_DEFAULT_OFF

binary_sensor:
  - platform: gpio
    pin:
      number: GPIO14
      mode: INPUT_PULLUP
      inverted: true
    id: tecla
    on_press:
      - switch.toggle: rele_corredor
```

!!! atencao "Rede elétrica exige respeito"
    Trabalhar com 127/220 V dentro de caixas de parede é sério: desligue o disjuntor, confira com um
    detector de tensão e, em caso de dúvida, chame um eletricista. Módulos certificados (Sonoff, Shelly)
    já vêm com isolamento adequado e também rodam ESPHome.

### 3. Rastreador de presença por Bluetooth
Um ESP32 por cômodo com `esp32_ble_tracker` transforma a casa num sistema de localização por aproximação,
útil para saber em qual ambiente alguém está sem instalar câmeras.

### 4. Satélite de voz
Com um M5Stack ATOM Echo e 15 linhas de YAML você tem um ponto de voz do *Assist* na cozinha —
processamento local, sem enviar áudio para fora.

## Boas práticas que evitam dor de cabeça

- **Use `secrets.yaml`** para Wi-Fi, chaves de API e senhas OTA; nunca versione esse arquivo no Git.
- **Nomes com padrão**: `sala-presenca`, `varanda-clima`. O nome vira o hostname e o prefixo das entidades.
- **`update_interval` honesto**: um sensor de temperatura a cada 10 segundos só enche o banco de dados.
- **Filtros no dispositivo** (`median`, `sliding_window_moving_average`, `delta`) evitam ruído e escrita inútil.
- **`api: reboot_timeout`** define o que acontece se o Home Assistant cair — avalie antes de deixar o padrão.
- **Guarde os YAMLs num repositório Git**; são a documentação real da sua casa.

## ESPHome x Tasmota x firmware de fábrica

- **ESPHome**: integração mais profunda com o Home Assistant, configuração declarativa. **Padrão recomendado.**
- **Tasmota**: excelente para flashar dispositivos comerciais prontos e falar MQTT com qualquer sistema.
- **Firmware de fábrica**: funciona, mas costuma exigir nuvem e app próprio. Quando o aparelho é baseado em
  ESP, vale trocar — muitos aceitam gravação pelo ar com ferramentas da comunidade.

Próximo passo natural: escolher o rádio dos sensores comprados prontos em
[Zigbee2MQTT ou ZHA](/zigbee/) e entender onde entra o [Matter over Thread](/matter-thread/).
