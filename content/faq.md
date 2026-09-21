---
title: Dúvidas frequentes sobre casa inteligente
slug: faq
description: Respostas diretas às perguntas que mais aparecem — custo, internet, aluguel, marcas, privacidade, Alexa e por onde começar.
category: FAQ
icon: help
order: 19
section: pagina
reading: 7 min de leitura
date: 2026-09-21
tags: [FAQ, Dúvidas, Iniciantes]
---

## Preciso saber programar?

Não. Boa parte das automações é construída por interface gráfica, e os blueprints da comunidade cobrem os
casos mais comuns. Saber ler YAML ajuda quando você quiser algo mais fino — e é uma linguagem de configuração,
não de programação: em uma tarde você entende o essencial.

## Quanto custa começar?

Um começo honesto tem três itens: o servidor (appliance, Raspberry Pi com SSD ou mini-PC), um coordenador
Zigbee e três a cinco sensores. A partir daí, cada dispositivo é uma decisão isolada. O erro caro é comprar
kits grandes antes de entender o que a casa precisa — praticamente todo mundo que faz isso tem uma gaveta
de aparelhos não usados.

## Funciona sem internet?

Com Home Assistant rodando local, sim: automações, sensores, painéis na rede interna e acionamentos
continuam funcionando com a internet fora do ar. O que para são serviços externos — previsão do tempo,
notificações no celular fora de casa, assistentes em nuvem e dispositivos que dependem do servidor do fabricante.

## Moro de aluguel. Dá para automatizar?

Dá, e bem. Evite tudo que exija obra:

- **Lâmpadas e tomadas inteligentes** em vez de módulos dentro da parede
- **Sensores a pilha** colados com fita dupla-face
- **Botões e controles Zigbee** avulsos, que substituem interruptores sem trocar nada
- **Controle de ar-condicionado por infravermelho** (um emissor IR cobre vários aparelhos)

Na mudança, tudo sai com você em uma caixa.

## Qual marca devo comprar?

A pergunta melhor é: **"esse aparelho funciona localmente?"**. Prefira, nesta ordem: Zigbee, Matter over
Thread, dispositivos com ESPHome/Tasmota, e Wi-Fi com integração local. Evite produtos que só funcionem pelo
app do fabricante com conta obrigatória na nuvem — são os primeiros a virar lixo eletrônico quando a
empresa muda de estratégia.

## E a Alexa e o Google? Preciso abandonar?

Não. Eles continuam ótimos como **interface de voz**. A diferença é que passam a comandar o Home Assistant,
que é quem realmente decide. Assim, se o serviço sair do ar ou você mudar de assistente, suas automações
permanecem intactas.

## Zigbee ou Wi-Fi para sensores?

Zigbee, quase sempre. Sensores Wi-Fi consomem muito mais energia (raramente funcionam a pilha por anos),
ocupam endereços na sua rede e sobrecarregam o roteador. Detalhes em [Zigbee na prática](/zigbee/).

## Matter resolve todos os problemas de compatibilidade?

Resolve muitos, mas não é mágica: a especificação cobre categorias de dispositivos progressivamente, e
recursos avançados de um fabricante nem sempre cabem no padrão. Matter garante o básico funcionando em todo
lugar — que já é enorme. Veja [Matter e Thread](/matter-thread/).

## Meus dados estão seguros?

Com processamento local, os dados ficam na sua casa. As regras práticas: ative a autenticação em duas
etapas, **nunca** exponha o Home Assistant diretamente na internet (use VPN ou Nabu Casa), mantenha backups
criptografados fora do servidor e coloque câmeras numa rede sem acesso à internet.

## Cartão SD realmente não serve?

Não para uso permanente. O banco de dados do Home Assistant escreve continuamente e cartões de consumo
falham por desgaste, em geral entre 6 e 18 meses — e a falha costuma ser silenciosa até o dia em que nada liga.
SSD NVMe ou eMMC, sempre.

## Por onde começo hoje, se tenho pouco tempo?

1. Instale o [Home Assistant](/instalacao/) num hardware simples
2. Integre o que **já existe** na sua rede (TV, aspirador, impressora, receptor)
3. Compre um coordenador Zigbee e **um** sensor de movimento
4. Automatize **um** incômodo real (a luz do corredor à noite costuma ser o melhor primeiro caso)
5. Só então planeje a casa inteira

## Preciso mesmo de MQTT?

Só quando **mais de um programa** precisa dos mesmos dados — Zigbee2MQTT, Frigate e Tasmota, por exemplo.
Se você usa apenas ZHA e ESPHome (que tem API própria), pode viver sem broker. Entenda em
[MQTT para iniciantes](/mqtt/).

## Vale pagar a assinatura da Nabu Casa?

Vale se você usa Alexa ou Google, quer acesso remoto sem configurar nada e não tem backup fora de casa.
Se você já tem VPN e backup, é opcional — mas continua sendo a forma mais direta de financiar o projeto.
A comparação completa, com preços e alternativas gratuitas, está em [Nabu Casa](/nabu-casa/).

## Dá para usar inteligência artificial sem mandar minha casa para a nuvem?

Dá. Modelos locais (Ollama num mini-PC ou Mac) atendem voz, descrição de imagens de câmera e conversas
simples sem que nada saia da sua rede. Veja [Claude e MCP](/claude-mcp/) e
[câmeras com IA](/cameras-ia/).

## Posso deixar um agente de IA cuidando da casa?

Pode, mas com limites: máquina separada, token restrito, sem acesso SSH, e nada de fechadura, portão ou
alarme na lista de coisas que ele controla. Os motivos — e os incidentes já documentados — estão em
[OpenClaw](/openclaw/).

## Minha automação funciona às vezes. O que faço?

Abra o **rastro (trace)** da automação no Home Assistant: ele mostra passo a passo onde a execução parou e
qual condição falhou. Em 90% dos casos o culpado é uma condição de tempo/estado mal escrita, um
`mode` inadequado (`single` engolindo disparos) ou uma entidade que ficou `unavailable`.
