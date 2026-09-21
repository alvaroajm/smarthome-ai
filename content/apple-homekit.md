---
title: Apple HomeKit + Home Assistant: o melhor dos dois mundos
slug: apple-homekit
description: Como expor tudo do Home Assistant no app Casa, usar Siri e atalhos sem abrir mão da automação local, e quando o caminho inverso faz mais sentido.
category: Ecossistemas
icon: apple
order: 9
featured: true
reading: 8 min de leitura
date: 2026-09-21
tags: [HomeKit, Apple, Siri, Matter, iOS]
---

Quem vive no ecossistema Apple costuma querer duas coisas ao mesmo tempo: a elegância do app **Casa** no
iPhone, no Apple Watch e no CarPlay, e a liberdade do **Home Assistant** para automações que o app Casa nunca
vai permitir. A boa notícia: não é preciso escolher.

## As três formas de conectar

### 1. HomeKit Bridge — do Home Assistant para a Apple (o caminho principal)

O Home Assistant vira um acessório HomeKit e publica as entidades que você escolher no app Casa. Qualquer
dispositivo — Zigbee, ESPHome, Wi-Fi, Matter, sensores calculados — aparece no iPhone como acessório nativo,
com Siri e automações do app Casa funcionando.

```yaml
# configuration.yaml — publique só o que interessa
homekit:
  - name: Casa HA
    port: 21063
    filter:
      include_domains:
        - light
        - climate
        - cover
        - lock
      include_entities:
        - sensor.temperatura_quarto
        - binary_sensor.porta_garagem
      exclude_entity_globs:
        - "*_bateria"
```

Depois de reiniciar, o Home Assistant mostra uma notificação com o **código de pareamento** — escaneie no
app Casa. A partir daí, tudo o que você criar no Home Assistant pode ser espelhado na Apple.

!!! dica "Publique pouco e com critério"
    Enviar 300 entidades para o HomeKit deixa o app Casa lento e bagunçado. Exponha o que você realmente
    controla pelo iPhone: luzes, cortinas, ar-condicionado, fechaduras e uns poucos sensores.

### 2. HomeKit Device — da Apple para o Home Assistant

O caminho inverso: acessórios que falam HomeKit nativamente (Eve, Aqara, Nanoleaf, muitas câmeras) podem ser
adicionados **diretamente** ao Home Assistant pela integração *HomeKit Device*, sem app Casa e sem nuvem.
Funciona muito bem — mas um acessório só pode ser pareado por um controlador HomeKit por vez, então escolha
antes se ele vai morar na Casa da Apple ou no Home Assistant.

### 3. Matter — os dois ao mesmo tempo, de verdade

Com [Matter](/matter-thread/), o recurso **multi-admin** permite que o mesmo dispositivo esteja na Casa da
Apple **e** no Home Assistant simultaneamente, sem ponte e sem duplicação. É a melhor situação possível e o
motivo principal para preferir Matter nos aparelhos novos.

## O arranjo que funciona bem no dia a dia

1. **Automação de verdade no Home Assistant**: condições, horários, presença, lógica com vários sensores.
2. **App Casa como controle remoto**: botões, Siri, widgets, Apple Watch, CarPlay e a tela bloqueada.
3. **Atalhos (Shortcuts) como cola**: um atalho pode chamar um webhook do Home Assistant, e um NFC colado
   na mesa de cabeceira dispara "modo dormir" sem tocar em nada.

```text
NFC na cabeceira → Atalho do iOS → webhook do Home Assistant
→ apaga luzes, tranca portas, arma sensores, baixa o ar para 24 °C
```

Webhook correspondente:

```yaml
alias: Modo dormir (via NFC)
triggers:
  - trigger: webhook
    webhook_id: modo_dormir_cabeceira
    allowed_methods: [POST]
    local_only: true
actions:
  - action: script.rotina_dormir
```

## Siri e a linguagem natural

O truque para a Siri entender sua casa é **nomear bem os acessórios** no app Casa: nomes curtos, sem
acentuação exótica e sem repetir o cômodo ("Luz" no quarto, e não "Luz do Quarto do Quarto"). Se você
prefere falar com o **Assist** do Home Assistant, também dá: um atalho chamando a conversação do Home
Assistant pode ser acionado por "E aí, Siri, falar com a casa".

## Presença: o que funciona melhor no iPhone

- **App oficial do Home Assistant** (Companion) com localização em segundo plano e **zonas** definidas.
- **Geofencing do app Casa** disparando um atalho quando chega/sai.
- **Bluetooth por cômodo** com ESP32 (`esp32_ble_tracker`) para presença interna — mais preciso e sem GPS.

!!! atencao "Automação boa não depende só de presença"
    Presença por celular tem latência e falha quando a bateria acaba. Combine com sensores de porta, de
    movimento e horários; a casa precisa se comportar bem mesmo quando o telefone está sem sinal.

## Câmeras da Apple x câmeras no Home Assistant

O HomeKit Secure Video é conveniente, mas fecha as imagens no ecossistema Apple e cobra armazenamento no
iCloud. Se você quer detecção de objetos local, gravação contínua e exportação, veja
[Scrypted e câmeras](/scrypted/) — inclusive para levar câmeras "não-HomeKit" para dentro do app Casa.
