---
title: Home Assistant OS: escolha sua instalação
slug: instalar-haos
description: Três guias ilustrados: Green, Raspberry Pi 5 com NVMe ou mini-PC Intel e AMD.
category: Instalação guiada
icon: book
order: 3
featured: true
level: basico
reading: 3 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

O **Home Assistant OS (HAOS)** é o sistema que cuida da central, das atualizações e dos Apps. Escolha **apenas o guia do seu equipamento**: cada um leva da preparação ao primeiro sensor Zigbee funcionando.

## Qual equipamento você vai instalar?

<div class="install-card-grid"><a class="install-card" href="/instalar-green/"><img src="/static/img/hardware/green.webp" width="800" height="533" alt="Home Assistant Green" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">01 / Pronto para conectar</span><h3>Home Assistant Green</h3><span class="install-card-description">Ligue a rede e a energia. Crie sua conta e conecte o ZBT-2, pelas telas.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a><a class="install-card" href="/instalar-raspberry-pi-5/"><img src="/static/img/devices/raspberry-pi-5-case.jpg" width="800" height="535" alt="Raspberry Pi 5 + NVMe" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">02 / Monte sua central</span><h3>Raspberry Pi 5 + NVMe</h3><span class="install-card-description">Escolha placa, case e SSD. Prepare o NVMe no Mac ou PC e instale o HAOS.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a><a class="install-card" href="/instalar-mini-pc/"><img src="/static/img/hardware/n150.webp" width="800" height="800" alt="Mini-PC x86-64" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">03 / Intel ou AMD</span><h3>Mini-PC x86-64</h3><span class="install-card-description">Prepare o pendrive e grave o HAOS no SSD interno, com um passo a passo visual.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a></div>

Ainda não comprou? [Compare os equipamentos, fotos e preços](/#hardware-haos).

## O que os três caminhos têm em comum?

1. A central fica ligada à energia e à rede por **Ethernet**.
2. Você configura pelo navegador de **outro computador**, na mesma rede, em [http://homeassistant.local:8123](http://homeassistant.local:8123).
3. Cria sua conta e conhece o painel.
4. Conecta o **ZBT-2 à central** e configura o **ZHA pelas telas**.
5. Adiciona uma luz ou um sensor e faz o primeiro backup.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A mesma interface de primeiro acesso, no Green, Pi ou mini-PC."><img src="/static/img/ha-guide/onboarding.png" alt="A mesma interface de primeiro acesso, no Green, Pi ou mini-PC." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>A mesma interface de primeiro acesso, no Green, Pi ou mini-PC. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

O Green já vem pronto. No Pi e no mini-PC, a gravação apaga a mídia escolhida: confira o destino e guarde seus arquivos antes de começar. Para esta trilha, não precisa de terminal, Proxmox ou máquinas virtuais.

Depois da instalação, [entenda melhor a rede Zigbee](/zigbee/) e [crie sua primeira automação](/primeira-automacao/).
