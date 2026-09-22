---
title: Zigbee: o básico para luzes e sensores
slug: zigbee
description: Nossa primeira rede: local, de baixo consumo e gerenciada pelo ZHA.
category: Passo a passo
icon: book
order: 4
featured: true
level: basico
reading: 4 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

**Zigbee** é uma conexão sem fio usada por sensores, lâmpadas, tomadas e botões. Os aparelhos conversam em uma rede própria; não entram individualmente no seu Wi-Fi.

## Por que vamos começar por ele?

- **Baixo consumo:** combina com sensores pequenos, alimentados por pilha.
- **Muitas opções:** há dispositivos de várias categorias e fabricantes.
- **Controle local:** com ZHA, a comunicação com a central acontece dentro de casa.
- **Rede que pode crescer:** aparelhos compatíveis ligados à energia podem repetir o sinal.

Essas vantagens tornam Zigbee uma boa escolha para nossa primeira luz e nossos primeiros sensores. Preço, qualidade e funções variam por modelo.

## Três peças da rede

| Peça | Para que serve |
|---|---|
| **Coordenador, como o ZBT-2** | Cria a rede e a conecta ao Home Assistant. |
| **Repetidor Zigbee** | Encaminha mensagens para aumentar a cobertura; muitas tomadas fazem isso. |
| **Sensor a pilha** | Envia suas leituras e geralmente não repete o sinal. |

Uma lâmpada que repete sinal deixa de ajudar quando o interruptor corta sua energia. A rede deve ser planejada para os aparelhos que permanecem ligados.

## Quais são as limitações?

É necessário um coordenador. Paredes, metal e outros equipamentos de 2,4 GHz podem interferir. Nem toda função de todo fabricante aparece no ZHA: confira o modelo antes da compra.

Um dispositivo Zigbee pertence a uma rede por vez. Se já estava em outra central, normalmente precisa ser colocado em modo de redefinição/pareamento conforme o manual.

## E o Thread?

Thread também é uma rede de baixo consumo e pode formar uma malha. É usada por muitos produtos Matter, mas precisa de um **roteador de borda Thread** para se ligar à rede doméstica.

É útil para dispositivos compatíveis entre ecossistemas. A desvantagem, para quem começa, é mais um requisito para conferir. Zigbee e Thread são redes diferentes; um sensor Zigbee não entra em Thread.

Primeiro, [entenda o que é Matter](/matter-thread/). Depois, [configure ZBT-2 + ZHA pelas telas](/zbt-dongles/).

Existe a alternativa **Zigbee2MQTT**, tratada no [aprofundamento](/aprofundamento/#zigbee2mqtt). Ela não é necessária nesta trilha.

Fontes: [ZHA](https://www.home-assistant.io/integrations/zha/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/) e [Thread](https://www.home-assistant.io/integrations/thread/).
