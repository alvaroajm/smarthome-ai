---
title: Home Assistant OS: instalar pelas telas
slug: instalar-haos
description: Comece com Green ou Raspberry Pi e configure pelo navegador.
category: Passo a passo
icon: book
order: 3
featured: true
level: basico
reading: 5 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Nesta trilha, usamos apenas **Home Assistant OS (HAOS)**. Ele reúne o Home Assistant e as ferramentas para mantê-lo atualizado.

Ainda está escolhendo? [Compare as centrais, fotos e preços](/#hardware-haos).

## Opção mais simples: Home Assistant Green

O Green já vem com o sistema instalado. Conecte-o ao roteador com um cabo de rede, ligue a fonte e aguarde a preparação. Você pode seguir direto para **Primeiro acesso**, abaixo.

O adaptador ZBT-2 é separado: vamos conectá-lo na etapa Zigbee.

## Já tem um Raspberry Pi?

Use um Pi 4 ou 5 compatível, fonte adequada, leitor de cartão, cabo de rede e microSD A2 de pelo menos 32 GB. O cartão é uma opção da instalação oficial; mantenha backups.

No computador, instale o [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Pela interface:

1. Escolha o modelo do Raspberry Pi.
2. Em **Sistema operacional**, procure **Other specific-purpose OS → Home automation → Home Assistant**.
3. Selecione **Home Assistant OS** para o modelo correto.
4. Escolha o cartão em **Armazenamento** e avance para **Gravar / Write**.

**A gravação apaga o cartão escolhido.** Confira o nome e a capacidade antes de confirmar. Aguarde o término, ejete o cartão e coloque-o no Pi. Conecte o cabo de rede e a fonte.

<figure class="ha-screen"><a href="/static/img/ha-guide/imager.png" target="_blank" rel="noopener" aria-label="Ampliar tela: No Imager, selecione Home Assistant OS para o seu Raspberry Pi."><img src="/static/img/ha-guide/imager.png" alt="No Imager, selecione Home Assistant OS para o seu Raspberry Pi." width="860" height="538" loading="lazy" decoding="async"></a><figcaption>No Imager, selecione Home Assistant OS para o seu Raspberry Pi. <a class="ext" href="https://www.home-assistant.io/installation/raspberrypi/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

<details><summary>Escolhi um Pi 5 com SSD NVMe</summary><p>Além do Pi 5 de 8 GB, você precisa de fonte adequada, refrigeração e um adaptador M.2 HAT compatível. Prefira um kit montado e preparado para iniciar pelo NVMe. A instalação inicial acima usa cartão; depois, a interface do HAOS permite mover os dados para o SSD em <strong>Configurações → Sistema → Armazenamento → Mover disco de dados</strong>. Isso mantém a inicialização no cartão e apaga o SSD escolhido. Faça um backup antes; o SSD precisa ter capacidade maior que a do cartão. Para iniciar diretamente pelo NVMe, siga as orientações do fabricante do kit. Veja a <a class="ext" href="https://www.home-assistant.io/common-tasks/os/#using-external-data-disk">orientação oficial para o disco de dados</a>.</p></details>

## Primeiro acesso

No computador ou celular conectado à mesma rede, abra **http://homeassistant.local:8123**. Espere a preparação terminar.

Escolha criar uma nova casa, cadastre o usuário e a senha e siga as telas. Confira localização, unidade de medida e fuso horário. Se o endereço não abrir, consulte o IP da central no roteador.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A criação da conta acontece no navegador."><img src="/static/img/ha-guide/onboarding.png" alt="A criação da conta acontece no navegador." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>A criação da conta acontece no navegador. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## Organize e proteja

Dê nomes simples aos cômodos e aparelhos. Em **Configurações → Sistema → Backups**, configure cópias automáticas e uma cópia fora da central; guarde a chave de recuperação indicada.

Pronto: você tem o HAOS. Antes de conectar o rádio, [entenda como funciona o Zigbee](/zigbee/).

<details><summary>Já tem um mini-PC?</summary><p>É possível instalar HAOS diretamente em um mini-PC compatível. A <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/">documentação oficial</a> explica a gravação no disco pela interface gráfica. Ela substitui o sistema existente e exige conferir o disco de destino. O Green é a opção que dispensa essa instalação.</p></details>

Fontes: [Green](https://www.home-assistant.io/green/), [Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi/), [primeiro acesso](https://www.home-assistant.io/getting-started/onboarding/) e [backups](https://www.home-assistant.io/common-tasks/general/#backups).
