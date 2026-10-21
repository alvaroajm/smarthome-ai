---
title: Minha instalação: Home Assistant, luzes e controles
slug: minha-instalacao
description: Fotos e equipamentos da casa de Álvaro Menezes: mini-PC com HAOS, WLED, Philips Hue, Alexa, Apple HomeKit e uma tela ESP32-S3 com ESPHome.
category: Instalação do autor
icon: hub
order: 93
featured: true
level: avancado
reading: 5 min de leitura
date: 2026-10-20
tags: [Home Assistant, ESPHome, WLED, HomeKit, Alexa]
---

Esta é a instalação residencial de **Álvaro Menezes**, documentada com suas fotografias e informações. O conjunto reúne iluminação, câmeras e diferentes formas de controle. A página descreve o que está em uso; ainda não é um tutorial para reproduzir todas as conexões.

## A sala e as formas de controle

As luzes são acionadas pelo **Home Assistant**, pelo **aplicativo Casa da Apple** e por **voz pela Alexa**. Uma tomada Zemismart instalada na sala controla luzes desse ambiente. Há também interruptores Zemismart Zigbee e luzes Philips Hue Zigbee na casa, com Hue na sala e na suíte master.

As **tiras de LED são controladas pelo WLED via Wi-Fi**. A foto mostra a iluminação azul na sala; ela não é uma medição de brilho nem uma comparação antes e depois.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-luz-azul.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Sala com iluminação azul junto à cristaleira e robô aspirador na base."><img src="/static/img/casa-do-autor/sala-luz-azul.jpg" alt="Sala com iluminação azul junto à cristaleira e robô aspirador na base." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Sala com iluminação azul junto à cristaleira e robô aspirador na base. Foto fornecida por Álvaro Menezes.</figcaption></figure>

Ter várias formas de comando atende a situações diferentes: o painel reúne os controles, o celular permite escolher uma luz pelo aplicativo e a voz dispensa abrir uma tela. Neste relato, esses são comandos solicitados pelo morador. Não foi documentada uma regra automática por horário ou presença.

## Interruptores na parede e controle Broadlink

Os **interruptores Zemismart Zigbee** também fazem parte da instalação. Na foto, os comandos têm identificações visíveis, como “Spots” e “Cristaleira”, que ajudam a distinguir os pontos de iluminação no painel da parede.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/interruptores-zemismart.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos."><img src="/static/img/casa-do-autor/interruptores-zemismart.jpg" alt="Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos. Foto fornecida por Álvaro Menezes.</figcaption></figure>

O autor utiliza ainda um **controle Broadlink IR e RF**. O modelo exato, os aparelhos comandados e a configuração de integração não foram informados; a fotografia registra o equipamento instalado.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/controle-broadlink.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Controle Broadlink IR e RF instalado na parede, conforme identificação do autor."><img src="/static/img/casa-do-autor/controle-broadlink.jpg" alt="Controle Broadlink IR e RF instalado na parede, conforme identificação do autor." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Controle Broadlink IR e RF instalado na parede, conforme identificação do autor. Foto fornecida por Álvaro Menezes.</figcaption></figure>

## A central: mini-PC com Home Assistant OS

O Home Assistant OS está instalado num **mini-PC com processador Ryzen 7**. A bancada também tem um **Mac mini M4**, visível na fotografia. São computadores distintos: o equipamento informado como central do Home Assistant é o mini-PC.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/central-home-assistant.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor."><img src="/static/img/casa-do-autor/central-home-assistant.jpg" alt="Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor. Foto fornecida por Álvaro Menezes.</figcaption></figure>

O painel no monitor organiza a navegação por áreas da casa. Essa organização ajuda a localizar o ambiente antes de escolher o dispositivo. Não foram registrados consumo elétrico, uso de memória ou tempo de resposta, por isso esta instalação não serve como benchmark do processador.

Para comparar opções de central, consulte o [guia de hardware](/hardware/). A escolha de uma máquina deve considerar a carga que você pretende executar; a fotografia não significa que um Ryzen 7 seja necessário para começar.

## Alexa e Apple HomeKit

O autor utiliza vários Echo Dot Max e um aparelho identificado como Echo Studio Max na sala. A conexão da **Alexa com o Home Assistant passa pelo Nabu Casa**.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/echo-sala.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Dispositivo Echo da sala, identificado pelo autor como Echo Studio Max."><img src="/static/img/casa-do-autor/echo-sala.jpg" alt="Dispositivo Echo da sala, identificado pelo autor como Echo Studio Max." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Dispositivo Echo da sala, identificado pelo autor como Echo Studio Max. Foto fornecida por Álvaro Menezes.</figcaption></figure>

Há **duas Apple TV 4K usadas como centrais do Apple HomeKit**. Uma delas aparece abaixo. A geração das Apple TV e o caminho exato de exposição dos dispositivos ao HomeKit ainda não foram registrados neste relato.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/apple-tv.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit."><img src="/static/img/casa-do-autor/apple-tv.jpg" alt="Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit. Foto fornecida por Álvaro Menezes.</figcaption></figure>

Os papéis são diferentes: o mini-PC executa Home Assistant, enquanto as Apple TV atuam como centrais do ecossistema Apple. Consulte os guias de [Nabu Casa](/nabu-casa/) e [Apple HomeKit](/apple-homekit/) para entender essas conexões.

## Uma tela ESP32-S3 com ESPHome

A tela **ESP32-S3 foi configurada pelo ESPHome do Home Assistant**. Na foto, aparecem informações de clima, um gráfico e atalhos para cômodos. É um exemplo concreto de uma interface dedicada, além do celular e do monitor da bancada.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/tela-esphome.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Tela ESP32-S3 configurada pelo autor com ESPHome, mostrando informações e atalhos para os cômodos."><img src="/static/img/casa-do-autor/tela-esphome.jpg" alt="Tela ESP32-S3 configurada pelo autor com ESPHome, mostrando informações e atalhos para os cômodos." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Tela ESP32-S3 configurada pelo autor com ESPHome, mostrando informações e atalhos para os cômodos. Foto fornecida por Álvaro Menezes.</figcaption></figure>

Para reproduzir essa tela seriam necessários o modelo completo da placa, o display utilizado e a configuração ESPHome. Esses arquivos ainda não acompanham este relato. O [guia de ESPHome e ESP32](/esphome-esp32/) apresenta os conceitos para iniciar um projeto próprio.

## Robô aspirador e hub Philips Hue

Um **robô aspirador Roborock** e sua base ficam na sala. A fotografia documenta o equipamento, mas não estabelece seu modelo exato, uma rotina de limpeza ou integração com o Home Assistant.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/roborock.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Robô aspirador Roborock junto à base, instalado na sala."><img src="/static/img/casa-do-autor/roborock.jpg" alt="Robô aspirador Roborock junto à base, instalado na sala." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Robô aspirador Roborock junto à base, instalado na sala. Foto fornecida por Álvaro Menezes.</figcaption></figure>

O conjunto inclui também um **hub Philips Hue**, confirmado pelo autor. Ainda falta documentar quais luzes estão vinculadas a esse hub e como ele se conecta aos demais sistemas.

## Câmeras: equipamentos e fluxo relatado

O autor utiliza **Tapo TC70**, **Intelbras iM4** e um **DVR Intelbras**, cujo modelo ainda não foi informado. Ele descreve o caminho das imagens como **câmeras → Home Assistant → Scrypted → HomeKit Secure Video**.

Antes de transformar esse relato em instruções, é necessário registrar a origem de vídeo configurada no Scrypted e os plugins usados. Essa sequência não deve ser interpretada como exigência de que toda instalação Scrypted passe pelo Home Assistant. Veja o [guia de câmeras](/scrypted/) para o contexto das ferramentas.

## O que falta para reproduzir esta instalação

| Parte | Informação que precisa acompanhar um passo a passo |
|---|---|
| Zigbee | Coordenador, integração e modelos exatos dos dispositivos. |
| WLED | Controlador das tiras e sua configuração. |
| ESPHome | Modelo completo da tela e YAML sem credenciais. |
| Câmeras | Modelo do DVR, plugins e origem de vídeo no Scrypted. |
| Rotinas | Gatilho, ação esperada, teste realizado e resultado observado. |

A descrição separa os equipamentos em uso das configurações ainda não documentadas. Para relatar uma falha ou sugerir uma etapa a detalhar, use o [contato do autor](/sobre/#contato-e-correcoes).
