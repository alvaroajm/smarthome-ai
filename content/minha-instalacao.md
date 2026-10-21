---
title: Minha instalação: Home Assistant, luzes e controles
slug: minha-instalacao
description: Fotos e equipamentos da minha casa: mini-PC com HAOS, WLED, Philips Hue, Alexa, Apple HomeKit e uma tela ESP32-S3 com ESPHome.
category: Minha instalação
icon: hub
order: 93
featured: true
level: avancado
reading: 5 min de leitura
date: 2026-10-20
updated: 2026-10-21
tags: [Home Assistant, ESPHome, WLED, HomeKit, Alexa]
---

Esta é a instalação que montei na minha casa. Reuni aqui minhas fotografias e os equipamentos que uso para iluminação, câmeras e diferentes formas de controle. Ainda preciso documentar alguns detalhes para transformar este registro em um tutorial completo.

## A sala e as formas de controle

Aciono as luzes pelo **Home Assistant**, pelo **aplicativo Casa da Apple** e por **voz pela Alexa**. Uma tomada Zemismart instalada na sala controla luzes desse ambiente. Há também interruptores Zemismart Zigbee e luzes Philips Hue Zigbee na casa, com Hue na sala e na suíte master.

As **tiras de LED são controladas pelo WLED via Wi-Fi**. A foto mostra a iluminação azul na sala; ela não é uma medição de brilho nem uma comparação antes e depois.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-luz-azul.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Sala com iluminação azul junto à cristaleira e robô aspirador na base."><img src="/static/img/casa-do-autor/sala-luz-azul.jpg" alt="Sala com iluminação azul junto à cristaleira e robô aspirador na base." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Sala com iluminação azul junto à cristaleira e robô aspirador na base. Foto da minha instalação.</figcaption></figure>

Ter várias formas de comando atende a situações diferentes: o painel reúne os controles, o celular permite escolher uma luz pelo aplicativo e a voz dispensa abrir uma tela. Neste relato, esses são comandos solicitados pelo morador. Não foi documentada uma regra automática por horário ou presença.

## Interruptores na parede e controle Broadlink

Os **interruptores Zemismart Zigbee** também fazem parte da instalação. Na foto, os comandos têm identificações visíveis, como “Spots” e “Cristaleira”, que ajudam a distinguir os pontos de iluminação no painel da parede.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/interruptores-zemismart.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos."><img src="/static/img/casa-do-autor/interruptores-zemismart.jpg" alt="Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Interruptores Zemismart Zigbee instalados na parede, com identificação dos comandos. Foto da minha instalação.</figcaption></figure>

Uso ainda um **controle Broadlink IR e RF**. Ainda não detalhei aqui o modelo exato, os aparelhos comandados e a configuração de integração; a fotografia mostra o equipamento instalado.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/controle-broadlink.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Controle Broadlink IR e RF instalado na parede, na minha instalação."><img src="/static/img/casa-do-autor/controle-broadlink.jpg" alt="Controle Broadlink IR e RF instalado na parede, na minha instalação." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Controle Broadlink IR e RF instalado na parede, na minha instalação. Foto da minha instalação.</figcaption></figure>

## A central: mini-PC com Home Assistant OS

Instalei o Home Assistant OS num **mini-PC com processador Ryzen 7**. Na minha bancada também há um **Mac mini M4**, visível na fotografia. São computadores distintos: uso o mini-PC como central do Home Assistant.

Controlo minha rede Zigbee pelo **Home Assistant**, por meio do **Zigbee2MQTT**, com o **ZBT-2 da Nabu Casa** como coordenador.

Minha rede **Thread** é compartilhada com a rede Thread da **Apple**. Uso o **ZBT-1** como adaptador de rádio Thread, separado do ZBT-2 usado para Zigbee.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/central-home-assistant.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor."><img src="/static/img/casa-do-autor/central-home-assistant.jpg" alt="Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Bancada com mini-PC rodando Home Assistant, Mac mini M4 e painel da casa no monitor. Foto da minha instalação.</figcaption></figure>

O painel no monitor organiza a navegação por áreas da casa. Essa organização ajuda a localizar o ambiente antes de escolher o dispositivo. Não publico aqui medições de consumo elétrico, uso de memória ou tempo de resposta; não apresento minha instalação como benchmark do processador.

Para comparar opções de central, consulte o [guia de hardware](/hardware/). A escolha de uma máquina deve considerar a carga que você pretende executar; a fotografia não significa que um Ryzen 7 seja necessário para começar.

## Alexa e Apple HomeKit

Uso vários Echo Dot Max e um aparelho que identifiquei como Echo Studio Max na sala. Conecto a **Alexa ao Home Assistant pelo Nabu Casa**.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/echo-sala.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Dispositivo Echo da sala, que identifiquei como Echo Studio Max."><img src="/static/img/casa-do-autor/echo-sala.jpg" alt="Dispositivo Echo da sala, que identifiquei como Echo Studio Max." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Dispositivo Echo da sala, que identifiquei como Echo Studio Max. Foto da minha instalação.</figcaption></figure>

Há **duas Apple TV 4K usadas como centrais do Apple HomeKit**. Uma delas aparece abaixo. A geração das Apple TV e o caminho exato de exposição dos dispositivos ao HomeKit ainda não foram registrados neste relato.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/apple-tv.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit."><img src="/static/img/casa-do-autor/apple-tv.jpg" alt="Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Uma das Apple TV 4K utilizadas como centrais do Apple HomeKit. Foto da minha instalação.</figcaption></figure>

Os papéis são diferentes: o mini-PC executa Home Assistant, enquanto as Apple TV atuam como centrais do ecossistema Apple. Consulte os guias de [Nabu Casa](/nabu-casa/) e [Apple HomeKit](/apple-homekit/) para entender essas conexões.

## Uma tela ESP32-S3 com ESPHome

A tela **ESP32-S3 foi configurada pelo ESPHome do Home Assistant**. Na foto, aparecem informações de clima, um gráfico e atalhos para cômodos. É um exemplo concreto de uma interface dedicada, além do celular e do monitor da bancada.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/tela-esphome.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Tela ESP32-S3 que configurei com ESPHome, mostrando informações e atalhos para os cômodos."><img src="/static/img/casa-do-autor/tela-esphome.jpg" alt="Tela ESP32-S3 que configurei com ESPHome, mostrando informações e atalhos para os cômodos." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Tela ESP32-S3 que configurei com ESPHome, mostrando informações e atalhos para os cômodos. Foto da minha instalação.</figcaption></figure>

Para reproduzir essa tela seriam necessários o modelo completo da placa, o display utilizado e a configuração ESPHome. Esses arquivos ainda não acompanham este relato. O [guia de ESPHome e ESP32](/esphome-esp32/) apresenta os conceitos para iniciar um projeto próprio.

## Robô aspirador e hub Philips Hue

Um **robô aspirador Roborock** e sua base ficam na sala. A fotografia documenta o equipamento, mas não estabelece seu modelo exato, uma rotina de limpeza ou integração com o Home Assistant.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/roborock.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Robô aspirador Roborock junto à base, instalado na sala."><img src="/static/img/casa-do-autor/roborock.jpg" alt="Robô aspirador Roborock junto à base, instalado na sala." width="960" height="1280" loading="lazy" decoding="async"></a><figcaption>Robô aspirador Roborock junto à base, instalado na sala. Foto da minha instalação.</figcaption></figure>

Também uso um **hub Philips Hue**. Ainda falta documentar quais luzes estão vinculadas a esse hub e como ele se conecta aos demais sistemas.

## Câmeras: equipamentos e fluxo relatado

Uso **Tapo TC70**, **Intelbras iM4** e um **DVR Intelbras**, cujo modelo ainda preciso registrar aqui. Descrevo o caminho das imagens da minha instalação como **câmeras → Home Assistant → Scrypted → HomeKit Secure Video**.

Antes de transformar esse relato em instruções, é necessário registrar a origem de vídeo configurada no Scrypted e os plugins usados. Essa sequência não deve ser interpretada como exigência de que toda instalação Scrypted passe pelo Home Assistant. Veja o [guia de câmeras](/scrypted/) para o contexto das ferramentas.

## Telas da minha instalação

Estas capturas mostram como organizei algumas interfaces do Home Assistant e do aplicativo Casa. As contagens e os estados são os que aparecem no momento do registro; não representam um teste de todas as integrações. Toque ou clique nas imagens para abrir o arquivo no tamanho original.

### Painel por áreas da casa

<figure class="ha-screen"><a href="/static/img/minha-instalacao-20261021/painel-areas-sanitizado.png" target="_blank" rel="noopener" aria-label="Ampliar captura do painel por áreas, com dados pessoais ocultados"><img src="/static/img/minha-instalacao-20261021/painel-areas-sanitizado.png" alt="Painel do Home Assistant organizado por áreas da casa, com um cartão ocultado para preservar dados pessoais." width="1708" height="921" loading="lazy" decoding="async"></a><figcaption>Meu painel do Home Assistant organizado por áreas da casa, com atalhos para os ambientes. O cartão com dados pessoais foi ocultado nesta cópia da captura.</figcaption></figure>

### Integrações no Home Assistant

<figure class="ha-screen"><a href="/static/img/minha-instalacao-20261021/integracoes.png" target="_blank" rel="noopener" aria-label="Ampliar captura das integrações no Home Assistant"><img src="/static/img/minha-instalacao-20261021/integracoes.png" alt="Tela de integrações do Home Assistant com ESPHome, Broadlink e os adaptadores Connect ZBT-1 e ZBT-2 entre os itens visíveis." width="2048" height="1087" loading="lazy" decoding="async"></a><figcaption>Integrações exibidas no meu Home Assistant, incluindo ESPHome, Broadlink e Connect ZBT-1 e ZBT-2. Os totais são os do momento da captura; não indicam o número de centrais Apple HomeKit.</figcaption></figure>

### Aplicativos no Home Assistant

<figure class="ha-screen"><a href="/static/img/minha-instalacao-20261021/aplicativos.png" target="_blank" rel="noopener" aria-label="Ampliar captura dos aplicativos no Home Assistant"><img src="/static/img/minha-instalacao-20261021/aplicativos.png" alt="Lista de aplicativos no Home Assistant, com Mosquitto broker, Matter Server, OpenThread Border Router, Scrypted e outros itens." width="2048" height="1100" loading="lazy" decoding="async"></a><figcaption>Lista de aplicativos no meu Home Assistant. Mosquitto broker, Matter Server, OpenThread Border Router e Scrypted aparecem entre os itens; os indicadores de execução pertencem ao instante registrado.</figcaption></figure>

### Projetos no ESPHome

<figure class="ha-screen"><a href="/static/img/minha-instalacao-20261021/esphome-projetos-sanitizado.png" target="_blank" rel="noopener" aria-label="Ampliar captura dos projetos no ESPHome, com dados pessoais ocultados"><img src="/static/img/minha-instalacao-20261021/esphome-projetos-sanitizado.png" alt="Projetos no ESPHome Device Builder, com um cartão ocultado para preservar o nome pessoal presente no título e no arquivo YAML." width="1697" height="927" loading="lazy" decoding="async"></a><figcaption>Projetos exibidos no meu ESPHome Device Builder; os estados correspondem ao momento da captura. O cartão com nome pessoal, inclusive no arquivo YAML, foi ocultado nesta cópia.</figcaption></figure>

### Controles no aplicativo Casa

<figure class="ha-screen" style="max-width:282px;margin-inline:auto"><a href="/static/img/minha-instalacao-20261021/apple-home-quarto.jpg" target="_blank" rel="noopener" aria-label="Abrir captura dos controles do quarto no aplicativo Casa"><img src="/static/img/minha-instalacao-20261021/apple-home-quarto.jpg" alt="Aplicativo Casa da Apple aberto no quarto, com controles de TV, ar-condicionado e iluminação." width="282" height="612" loading="lazy" decoding="async"></a><figcaption>Controles do quarto no aplicativo Casa da Apple, com TV, ar-condicionado e iluminação. Mantive a resolução recebida, sem ampliar artificialmente o texto.</figcaption></figure>

### Interface de terminal

<figure class="ha-screen"><a href="/static/img/minha-instalacao-20261021/claude-terminal.png" target="_blank" rel="noopener" aria-label="Ampliar captura do Claude Terminal Pro no Home Assistant"><img src="/static/img/minha-instalacao-20261021/claude-terminal.png" alt="Interface do Claude Terminal Pro aberta no Home Assistant, com a mensagem de que não há sessão iniciada." width="2047" height="1109" loading="lazy" decoding="async"></a><figcaption>Interface do Claude Terminal Pro no meu Home Assistant. A mensagem visível informa que não há sessão iniciada; esta captura não demonstra comandos ou automações executados.</figcaption></figure>

## O que falta para reproduzir esta instalação

| Parte | Informação que precisa acompanhar um passo a passo |
|---|---|
| Zigbee | Modelos exatos dos dispositivos e configuração necessária para reproduzir a rede. |
| WLED | Controlador das tiras e sua configuração. |
| ESPHome | Modelo completo da tela e YAML sem credenciais. |
| Câmeras | Modelo do DVR, plugins e origem de vídeo no Scrypted. |
| Rotinas | Gatilho, ação esperada, teste realizado e resultado observado. |

A descrição separa os equipamentos em uso das configurações ainda não documentadas. Para relatar uma falha ou sugerir uma etapa a detalhar, use o [meu contato](/sobre/#contato-e-correcoes).
