---
title: O que é Home Assistant?
slug: home-assistant
description: Uma central, um painel e automações para sua casa.
category: Passo a passo
icon: book
order: 2
featured: true
level: basico
reading: 4 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

O **Home Assistant** é um programa gratuito e de código aberto que reúne aparelhos compatíveis em um painel. Ele recebe informações dos sensores e executa as automações que você cria.

O **Home Assistant OS (HAOS)** é o sistema que cuida dessa instalação, das atualizações e dos Apps. É o método que vamos usar.

## Como ele aparece para você?

Você abre uma página no navegador ou o aplicativo no celular. Usa botões para controlar as luzes e menus para configurar os aparelhos.

<figure class="ha-screen"><a href="/static/img/ha-guide/dashboard.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Um painel do Home Assistant: botões e informações por cômodo."><img src="/static/img/ha-guide/dashboard.png" alt="Um painel do Home Assistant: botões e informações por cômodo." width="1701" height="1299" loading="lazy" decoding="async"></a><figcaption>Um painel do Home Assistant: botões e informações por cômodo. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding_dashboard/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

A captura mostra um painel já organizado. O seu começa com os dispositivos que você adicionar; não precisa montar uma tela elaborada.

## O que fica ligado em casa?

Uma central, como o **Home Assistant Green**, executa o sistema. O celular apenas acessa essa central: instalar o app no telefone não instala o HAOS.

Com dispositivos e integrações locais, suas regras funcionam sem internet. A central, os aparelhos e a rede local precisam continuar ligados. Recursos de nuvem ainda dependem de internet.

## Só quatro palavras novas

| Palavra | Significado |
|---|---|
| **Integração** | A conexão com uma marca, rede ou serviço. O ZHA é uma delas. |
| **Dispositivo** | O aparelho físico, como uma lâmpada. |
| **Entidade** | Uma função ou leitura, como ligar a luz ou medir a bateria. |
| **Área** | O cômodo onde fica o aparelho. |

Um sensor pode aparecer com movimento e bateria: duas entidades do mesmo dispositivo.

## Seu primeiro objetivo

Adicionar uma luz, controlá-la pelo painel e criar uma regra simples. Você faz isso pela interface, sem escrever código.

[Prepare sua central com Home Assistant OS](/instalar-haos/).

Fontes: [conceitos](https://www.home-assistant.io/getting-started/concepts-terminology/), [painéis](https://www.home-assistant.io/dashboards/) e [instalação](https://www.home-assistant.io/installation/).
