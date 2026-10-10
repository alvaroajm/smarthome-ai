---
title: Zigbee2MQTT ou ZHA: quando considerar a mudança
slug: zigbee2mqtt
description: Compare suporte a dispositivos e os serviços necessários para usar Zigbee2MQTT no Home Assistant. Saiba o que conferir antes de migrar do ZHA.
category: Aprofundamento
icon: book
order: 91
featured: true
level: avancado
reading: 2 min de leitura
date: 2026-09-22
updated: 2026-10-09
tags: [Home Assistant]
---

**O ZHA é a escolha da nossa trilha inicial.** Zigbee2MQTT, ou Z2M, é outra forma de gerenciar uma rede Zigbee e integrá-la ao Home Assistant.

## Quando avaliar?

Quando um modelo ou função de que você precisa tiver suporte mais adequado no Zigbee2MQTT. Confira o modelo exato no catálogo e compare com o ZHA antes de mudar.

## O que acrescenta?

Um serviço Zigbee2MQTT e um servidor MQTT, responsáveis por encaminhar as mensagens. No HAOS, siga as instruções mantidas pelo projeto para instalar e abrir sua interface.

Não use o mesmo coordenador no ZHA e no Z2M ao mesmo tempo. Trocar de solução normalmente exige planejar a rede e parear novamente os aparelhos.

## Referências

Se a sua rede já usa Zigbee2MQTT e apresenta falhas, siga o [roteiro para diagnosticar desconexões](/zigbee2mqtt-desconectando/) antes de migrar ou parear os aparelhos novamente.

- [Instalação oficial no Home Assistant](https://www.zigbee2mqtt.io/guide/installation/03_ha_addon.html)
- [Catálogo de dispositivos](https://www.zigbee2mqtt.io/supported-devices/)
- [Voltar ao ZHA com ZBT-2](/zbt-dongles/)
