---
level: avancado
title: Sensores com ESPHome e ESP32
slug: esphome-esp32
description: Conheça os componentes e monte seu primeiro projeto.
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

[Voltar ao Home Assistant](/home-assistant/).

Fontes: [iniciar no ESPHome](https://esphome.io/install/getting-started/), [instalar ESPHome](https://esphome.io/install/), [ESP32-DevKitC](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), [ATOM-S3](https://docs.m5stack.com/en/core/AtomS3) e [Nabu Casa e Open Home Foundation](https://www.nabucasa.com/).
