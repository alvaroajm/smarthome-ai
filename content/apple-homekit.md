---
level: avancado
title: Home Assistant no app Casa
slug: apple-homekit
description: Leve dispositivos compatíveis ao iPhone e à Siri.
category: Ecossistemas
icon: apple
order: 110
featured: true
reading: 5 min de leitura
date: 2026-09-22
tags: [HomeKit, Apple, Siri, Matter, iOS]
---

Você pode combinar a interface familiar do **app Casa**, da Apple, com a variedade de dispositivos e automações do **Home Assistant**.

## Uma ponte para um ecossistema mais fechado

Apple Home / HomeKit tem regras próprias de compatibilidade e depende de produtos Apple para parte da experiência. A integração **HomeKit Bridge** publica funções suportadas do Home Assistant no app Casa, inclusive de aparelhos que não possuem HomeKit nativo.

Assim, uma luz Zigbee ou um controle criado com ESPHome pode aparecer ao lado dos acessórios Apple Home que você já usa. A compatibilidade depende do tipo de entidade: nem toda função do Home Assistant pode ser traduzida para o app Casa.

## Configure pelas telas

1. No Home Assistant, abra **Configurações → Dispositivos e serviços → Adicionar integração**.
2. Procure **HomeKit Bridge** e siga o assistente para escolher os tipos de dispositivos que deseja compartilhar.
3. Abra a notificação com o código de pareamento.
4. No iPhone, abra **Casa → Adicionar acessório** e escaneie o código apresentado.
5. Organize os acessórios nos cômodos e teste um comando simples com a Siri.

Comece com poucas luzes ou cortinas. Depois, ajuste o filtro da ponte pelas opções da integração para compartilhar mais dispositivos. Algumas categorias exigem configuração específica; siga a documentação do modelo e da integração.

## Siri e acesso remoto

Os controles compatíveis podem ser acionados pela Siri. Para controlar pelo app Casa fora de casa, é necessária uma **central Apple compatível**, como um HomePod ou Apple TV configurado como central.

Isso é diferente do acesso remoto pelo **Home Assistant Companion**, que pode usar Home Assistant Cloud ou VPN. A Nabu Casa não é necessária para criar a ponte HomeKit local.

## HomeKit Bridge e HomeKit Device não são a mesma coisa

| Integração | Direção |
|---|---|
| HomeKit Bridge | Leva funções do Home Assistant ao app Casa. |
| HomeKit Device | Adiciona ao Home Assistant acessórios que falam o protocolo HomeKit. |
| Matter | Conecta acessórios Matter compatíveis; o compartilhamento entre controladores depende do suporte do produto. |

Acessórios **Eve** e **Aqara**, por exemplo, podem ter versões HomeKit, Matter ou Zigbee. Confira o modelo antes de escolher a integração. HomeKit sobre Thread também exige a infraestrutura Thread adequada.

## E as câmeras?

Mostrar uma câmera através da HomeKit Bridge não fornece automaticamente gravação **HomeKit Secure Video**. Vídeo ao vivo, eventos, áudio e gravação são recursos distintos. Deixe a integração avançada de câmeras para uma etapa posterior.

[Voltar às possibilidades do Home Assistant](/home-assistant/) · [Conhecer o acesso remoto da Nabu Casa](/nabu-casa/).

Fontes: [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/), [HomeKit Device](https://www.home-assistant.io/integrations/homekit_controller/), [Matter](https://www.home-assistant.io/integrations/matter/) e [central da casa Apple](https://support.apple.com/pt-br/102557).
