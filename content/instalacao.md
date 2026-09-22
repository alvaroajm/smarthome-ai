---
title: Comece sua casa inteligente
slug: instalacao
description: Da escolha da central à primeira luz automatizada.
category: Começando
icon: rocket
order: 1
featured: true
reading: 4 min de leitura
date: 2026-09-21
tags: [Home Assistant, Instalação, Raspberry Pi, Backup]
---

Uma casa inteligente pode começar com **uma luz e um sensor**. Siga estes passos para montar a base.

<img class="guide-image" src="/static/img/home-comfort.webp" alt="Ilustração de uma sala com luz, sensor e caixa de som inteligente" width="1536" height="1024" loading="lazy">

## 1. Escolha a central

É o aparelho que fica ligado para coordenar a casa.

| Opção | O que esperar |
|---|---|
| **Home Assistant Green** | Vem com o sistema instalado. |
| **Raspberry Pi** | Você monta e instala o sistema. |
| **Mini-PC** | Exige instalação e permite projetos maiores. |

Confira os requisitos do aparelho no [guia de hardware](/hardware/). Para começar, o **Home Assistant OS** é o caminho recomendado pela documentação oficial.

## 2. Ligue e configure

No Green, conecte a energia e o cabo de rede. No Raspberry Pi ou mini-PC, siga primeiro o [passo a passo de instalação](/instalar-haos/).

Depois, abra no navegador:

```text
http://homeassistant.local:8123
```

Crie sua conta e confira a localização e o fuso horário. Se o endereço não abrir, procure o IP do aparelho no roteador.

## 3. Adicione um aparelho

Abra **Configurações → Dispositivos e serviços**. Veja o que foi descoberto e configure um dispositivo compatível que você já possui.

Antes de comprar algo novo, confira a [integração do modelo](https://www.home-assistant.io/integrations/). Dispositivos Zigbee precisam de um adaptador ou central compatível; Matter sobre Thread também exige suporte à rede Thread.

## 4. Crie uma automação simples

Use o editor em **Configurações → Automações e cenas**. Um exemplo para o corredor:

- **Quando:** o sensor detectar movimento.
- **Se:** estiver de noite.
- **Então:** acender a luz.

Salve e teste. Depois, acrescente o desligamento quando não houver movimento. Você pode fazer isso pela interface, sem programar.

## 5. Proteja antes de expandir

Ative os backups em **Configurações → Sistema → Backups** e mantenha uma cópia fora da central. Dê nomes claros aos aparelhos e organize-os por cômodo.

Para controlar a casa de fora, consulte [Home Assistant Cloud](/nabu-casa/). Evite expor diretamente a porta 8123 à internet.

**Próximo passo:** [entenda os termos do Home Assistant](/home-assistant/).

## Fontes e detalhes

- [Instalação oficial](https://www.home-assistant.io/installation/)
- [Primeiras automações](https://www.home-assistant.io/getting-started/automation/)
- [Tutorial completo de instalação](/instalar-haos/)
