---
title: O que é Home Assistant?
slug: home-assistant
description: Entenda a central que conecta e automatiza sua casa.
category: Plataforma
icon: hub
order: 3
featured: true
reading: 3 min de leitura
date: 2026-09-21
tags: [Home Assistant, Automação, Local, YAML]
---

O **Home Assistant** reúne aparelhos compatíveis em um painel e permite criar automações. Ele roda em uma central dentro da sua casa.

## O que dá para fazer?

- Acender a luz quando alguém entrar no corredor.
- Receber um aviso se uma porta ficar aberta.
- Acionar uma cena de cinema com luz suave.

O funcionamento sem internet depende dos dispositivos e das integrações escolhidas. Serviços de nuvem continuam precisando de conexão.

## Quatro termos para começar

| Termo | Exemplo simples |
|---|---|
| **Integração** | A conexão que permite usar uma marca ou serviço. |
| **Dispositivo** | O aparelho: uma lâmpada ou um sensor. |
| **Entidade** | Uma função ou leitura: ligar a luz ou medir a temperatura. |
| **Área** | O cômodo onde está o aparelho. |

Um sensor pode ter várias entidades, como movimento e nível da bateria.

## Como uma automação funciona?

Pense em três partes:

1. **Quando:** algo acontece, como detectar movimento.
2. **Se:** uma condição permite continuar, como estar escuro.
3. **Então:** a casa responde, acendendo uma luz.

Comece pelo editor visual. Não é necessário escrever código para criar automações básicas.

## E os painéis e as cenas?

O **painel** reúne botões e informações. Uma **cena** guarda uma combinação, como “luz da sala em 30%”. Um **script** executa uma sequência de ações.

Apps complementares, antes chamados add-ons, acrescentam serviços ao Home Assistant OS. Instale apenas os necessários para seu projeto.

## Por onde seguir?

Se ainda não tem uma central, abra o [guia para começar](/instalacao/). Se já está usando, organize os cômodos, configure backups e teste uma automação por vez.

Depois, explore [Zigbee](/zigbee/), [Matter e Thread](/matter-thread/) ou a [conexão com o app Casa](/apple-homekit/).

## Fontes

- [Conceitos do Home Assistant](https://www.home-assistant.io/getting-started/concepts-terminology/)
- [Como automatizar](https://www.home-assistant.io/getting-started/automation/)
- [Tipos de instalação](https://www.home-assistant.io/installation/)
