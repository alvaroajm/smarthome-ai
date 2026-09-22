---
title: ZBT-2 e ZHA: conecte seu primeiro dispositivo
slug: zbt-dongles
description: Configure o adaptador e conecte uma luz ou um sensor pelas telas.
category: Passo a passo
icon: book
order: 6
featured: true
level: basico
reading: 5 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Você precisa do **HAOS funcionando**, de um **Home Assistant Connect ZBT-2** e de uma luz ou sensor Zigbee compatível.

O **ZBT-2 é o rádio USB**. O **ZHA é a integração incluída no Home Assistant** que organiza a rede. Não é necessário instalar um App extra.

## 1. Conecte o ZBT-2

Monte a antena conforme o manual e use o cabo USB fornecido para conectá-lo à central. Mantenha-o na vertical, afastado do computador, do roteador e de superfícies metálicas.

## 2. Abra o dispositivo descoberto

Acesse **Configurações → Dispositivos e serviços**. No cartão do Connect ZBT-2, selecione **Adicionar**.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-discovery.png" target="_blank" rel="noopener" aria-label="Ampliar tela: O Home Assistant detecta o Connect ZBT-2 conectado por USB."><img src="/static/img/ha-guide/zbt-discovery.png" alt="O Home Assistant detecta o Connect ZBT-2 conectado por USB." width="350" height="230" loading="lazy" decoding="async"></a><figcaption>O Home Assistant detecta o Connect ZBT-2 conectado por USB. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 3. Escolha Zigbee e a instalação recomendada

No assistente, selecione **Usar como adaptador Zigbee / Use as Zigbee adapter**. Depois, escolha **Instalação recomendada / Recommended installation**. Essa opção configura o ZHA.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Nesta trilha, escolha Zigbee."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="Nesta trilha, escolha Zigbee." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>Nesta trilha, escolha Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

Siga as solicitações até concluir e atribua o adaptador a um cômodo. Não escolha Thread para esta rede.

## 4. Adicione a primeira luz ou sensor

Em **Configurações → Dispositivos e serviços**, abra **Zigbee Home Automation** e clique em **Adicionar dispositivo**.

Coloque o aparelho em modo de pareamento, seguindo o manual do fabricante. Aguarde a descoberta, dê um nome como “Luz da sala” e escolha o cômodo.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Use Adicionar dispositivo para buscar aparelhos em pareamento."><img src="/static/img/ha-guide/zha-add.png" alt="Use Adicionar dispositivo para buscar aparelhos em pareamento." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Adicionar dispositivo para buscar aparelhos em pareamento. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 5. Teste antes de continuar

Abra o dispositivo e use o controle da luz. Se for um sensor de abertura, abra e feche a porta e confira a mudança do estado. Faça esse teste no local onde o aparelho será usado.

<details><summary>O aparelho não apareceu?</summary><p>Confira o modo de pareamento, a bateria e o suporte do modelo no ZHA. Se estava em outra central, siga a redefinição do fabricante. Para o ZBT-2 não detectado, confira cabo, conexão USB e atualizações do Home Assistant; consulte o suporte oficial antes de alterar configurações.</p></details>

[Agora crie uma automação pelo editor visual](/primeira-automacao/).

Já usa ZBT-1? Não precisa trocá-lo apenas para seguir os conceitos do guia. Zigbee2MQTT é uma alternativa disponível no [aprofundamento](/aprofundamento/#zigbee2mqtt).

Fontes: [assistente oficial do ZBT-2](https://support.nabucasa.com/hc/en-us/articles/29400591254301) e [ZHA](https://www.home-assistant.io/integrations/zha/).
