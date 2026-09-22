---
title: Sua primeira automação pelas telas
slug: primeira-automacao
description: Acenda uma luz ao anoitecer, sem escrever código.
category: Passo a passo
icon: book
order: 7
featured: true
level: basico
reading: 4 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Vamos criar a regra **“ao pôr do sol, ligar a luz da sala”**. Antes, confirme que a lâmpada já funciona pelo painel e que a localização da casa está correta.

## 1. Abra o editor

Acesse **Configurações → Automações e cenas → Criar automação → Criar nova automação**.

<figure class="ha-screen"><a href="/static/img/ha-guide/automation.png" target="_blank" rel="noopener" aria-label="Ampliar tela: O editor visual: Quando, E se e Então fazer."><img src="/static/img/ha-guide/automation.png" alt="O editor visual: Quando, E se e Então fazer." width="1021" height="586" loading="lazy" decoding="async"></a><figcaption>O editor visual: Quando, E se e Então fazer. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 2. Escolha quando a luz deve acender

Em **Quando**, selecione **Adicionar gatilho**, procure **Sol** e escolha **Pôr do sol**. Deixe o deslocamento em zero para usar o horário do pôr do sol.

O campo **E se** é opcional. Vamos deixá-lo vazio neste primeiro teste.

## 3. Escolha o que deve acontecer

Em **Então fazer**, clique em **Adicionar ação**, procure **Luz: ligar** e selecione sua lâmpada como alvo. Se ela permitir, escolha também o brilho.

<figure class="ha-screen"><a href="/static/img/ha-guide/action.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo."><img src="/static/img/ha-guide/action.png" alt="Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo." width="953" height="330" loading="lazy" decoding="async"></a><figcaption>Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

A captura oficial usa uma área como alvo. Para começar, você pode escolher apenas uma luz.

## 4. Salve e teste

Clique em **Salvar** e dê um nome claro, como “Luz da sala ao anoitecer”. No menu da automação, use **Executar ações** para conferir se a luz acende.

Esse teste verifica a ação, **não o gatilho do pôr do sol**. Para testar a regra completa sem esperar até a noite, crie uma automação temporária com um horário próximo; depois remova-a ou desative-a.

## Funcionou? Pare por aqui por enquanto

Você já tem uma automação útil. Observe o resultado e mantenha seus backups antes de adicionar outras regras. A mesma ideia poderá usar um sensor de movimento como gatilho depois.

[Quando quiser, conheça integrações e Apps](/apps-integracoes/).

Fontes: [primeiras automações](https://www.home-assistant.io/getting-started/automation/) e [como testar](https://www.home-assistant.io/docs/automation/troubleshooting/#testing-your-automation).
