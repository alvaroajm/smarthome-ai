---
title: Integrações, Apps, HACS e câmeras
slug: apps-integracoes
description: Acrescente recursos apenas quando precisar deles.
category: Passo a passo
icon: book
order: 8
featured: true
level: basico
reading: 4 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Sua primeira automação não precisa de tudo isto. Conheça os nomes para saber o que procurar quando quiser expandir.

## 1. Integrações: conexões com aparelhos

Uma **integração** permite que o Home Assistant converse com uma marca, serviço ou rede. O ZHA já é a integração da sua rede Zigbee.

Para adicionar outra, abra **Configurações → Dispositivos e serviços → Adicionar integração**. Procure a marca ou o serviço e siga as instruções. Alguns aparelhos aparecem automaticamente.

<figure class="ha-screen"><a href="/static/img/ha-guide/integrations.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A tela reúne integrações configuradas e aparelhos descobertos."><img src="/static/img/ha-guide/integrations.png" alt="A tela reúne integrações configuradas e aparelhos descobertos." width="1365" height="860" loading="lazy" decoding="async"></a><figcaption>A tela reúne integrações configuradas e aparelhos descobertos. <a class="ext" href="https://www.home-assistant.io/getting-started/integration/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 2. Apps, antes chamados Add-ons

**Apps** são programas extras instalados no HAOS. Eles têm uma função própria, como acrescentar um serviço que determinado projeto exige. São diferentes das integrações.

Procure **Configurações → Apps** e a loja. Em versões anteriores, o nome pode aparecer como **Complementos / Add-ons**. Leia a documentação do App e instale somente quando necessário.

**ZHA não precisa de MQTT nem de um App adicional.**

<figure class="ha-screen"><a href="/static/img/ha-guide/apps.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A loja de Apps do Home Assistant OS. Você não precisa instalar tudo."><img src="/static/img/ha-guide/apps.png" alt="A loja de Apps do Home Assistant OS. Você não precisa instalar tudo." width="1138" height="608" loading="lazy" decoding="async"></a><figcaption>A loja de Apps do Home Assistant OS. Você não precisa instalar tudo. <a class="ext" href="https://www.home-assistant.io/getting-started/concepts-terminology/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 3. HACS: deixe para uma necessidade concreta

O **HACS** é um catálogo da comunidade para integrações e elementos de painel que não vêm no conjunto oficial. Não é a loja de Apps do HAOS.

Ele é opcional e seus componentes podem exigir manutenção ou deixar de funcionar após atualizações. Prefira primeiro as integrações oficiais. Quando houver um recurso específico que você precise, consulte a [documentação do HACS](https://hacs.xyz/docs/use/).

## 4. Câmeras: comece vendo a imagem

Antes da compra, confira a integração do modelo. Algumas câmeras oferecem conexão local; outras dependem do serviço do fabricante.

1. Adicione a integração em **Dispositivos e serviços**.
2. Confirme que a imagem abre no Home Assistant.
3. Pelo editor do painel, adicione um cartão compatível com a câmera.

Exibir vídeo não significa gravar. Gravação, alertas e detecção de pessoas são etapas posteriores, abordadas em [câmeras no aprofundamento](/aprofundamento/#cameras).

Você não precisa instalar HACS para todas as câmeras. Primeiro veja o que a integração oficial oferece.

Fontes: [integrações](https://www.home-assistant.io/getting-started/integration/), [Apps](https://www.home-assistant.io/addons/), [HACS](https://hacs.xyz/docs/use/) e [câmeras](https://www.home-assistant.io/integrations/camera/).
