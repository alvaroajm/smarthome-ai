---
title: Sobre o SmartHome-AI
slug: sobre
description: Um projeto independente sobre casa inteligente local, código aberto e automação que funciona no mundo real.
category: Sobre
icon: book
order: 13
section: pagina
reading: 3 min de leitura
date: 2026-09-21
tags: [Sobre, Contato, Open Source]
---

O **SmartHome-AI** nasceu de uma frustração comum: a maior parte do conteúdo sobre casa inteligente ou é
propaganda de produto, ou é tão técnica que assume que você já sabe o que é um broker MQTT.

Aqui o compromisso é outro: **explicar o porquê antes do como**, com exemplos que funcionam em casas reais
— inclusive nas que têm internet instável, paredes grossas e moradores que não querem saber de tecnologia.

## Princípios editoriais

1. **Local primeiro.** Nuvem é conveniência, nunca dependência.
2. **Código aberto sempre que possível.** Home Assistant, ESPHome, Zigbee2MQTT, Frigate, Scrypted.
3. **Nada de lista patrocinada.** Quando um produto é citado, é porque resolve um problema descrito.
4. **O plano B importa.** Toda automação precisa funcionar (ou falhar com segurança) quando algo cai.
5. **Respeito a quem mora na casa.** Automação que irrita os outros moradores é automação mal feita.

## Temas cobertos

- [Home Assistant](/home-assistant/) — a plataforma
- [ESPHome e ESP32](/esphome-esp32/) — dispositivos feitos por você
- [Zigbee2MQTT e ZHA](/zigbee/) — a malha dos sensores
- [Matter e Thread](/matter-thread/) — o padrão que atravessa ecossistemas
- [Apple HomeKit](/apple-homekit/) — integração com iPhone, Siri e Apple TV
- [Scrypted, Frigate e câmeras](/scrypted/) — vídeo local
- [Hardware](/hardware/) e [rede](/rede-wifi/) — a base de tudo
- [CasaOS e umbrelOS](/casaos-umbrel/) — os serviços da casa
- [Comandos do HAOS](/comandos-haos/) — referência de linha de comando

## Como o site é feito

Este site é estático: HTML, CSS e JavaScript sem frameworks, gerado por um script em **Python** a partir de
arquivos Markdown, versionado no **GitHub** e publicado no **Cloudflare**. Sem banco de dados, sem
rastreadores, sem anúncios — carrega rápido até no 3G da estrada.

O código do gerador é simples de propósito: cerca de 300 linhas, com uma única dependência
(a biblioteca `Markdown`). Qualquer pessoa consegue clonar, escrever um arquivo `.md` na pasta `content/`,
rodar `python3 build.py` e ter o site pronto.

## Quem escreve

Conteúdo por **Dr. Álvaro Menezes** — médico radiologista, entusiasta de automação residencial, Home Assistant,
ESP32 e sistemas locais. As configurações publicadas aqui rodam numa casa de verdade, com os erros já cometidos.

## Contato e correções

Encontrou um erro, tem uma sugestão ou quer indicar um tema? Correções são muito bem-vindas — este site é
mantido publicamente e melhora com quem o lê.
