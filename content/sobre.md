---
title: Sobre o SmartHome-AI
slug: sobre
description: Criei o SmartHome-AI para compartilhar minha instalação, fotografias e guias de casa inteligente com Home Assistant.
category: Sobre
icon: book
order: 20
section: pagina
reading: 3 min de leitura
date: 2026-09-21
updated: 2026-10-21
tags: [Sobre, Contato, Open Source]
---

<img src="/static/img/smarthome-banner.jpg?v=20261021" alt="Banner do SmartHome-AI" width="1400" height="788" decoding="async">


Criei o **SmartHome-AI** para compartilhar o que aprendo ao montar minha casa inteligente e reunir meus registros de instalação, fotografias e guias.

Meu compromisso é **explicar o porquê antes do como**, com orientações para quem está começando e exemplos que precisam ser adaptados a cada casa.

## Princípios editoriais

1. **Local primeiro.** Nuvem é conveniência, nunca dependência.
2. **Código aberto sempre que possível.** Home Assistant, ESPHome, Zigbee2MQTT, Frigate, Scrypted.
3. **Nada de lista patrocinada.** Quando um produto é citado, é porque resolve um problema descrito.
4. **O plano B importa.** Toda automação precisa funcionar (ou falhar com segurança) quando algo cai.
5. **Respeito a quem mora na casa.** Automação que irrita os outros moradores é automação mal feita.

## Temas cobertos

- [Home Assistant](/home-assistant/) — a plataforma
- [ESPHome e ESP32](/esphome-esp32/) — dispositivos feitos por você
- [Zigbee2MQTT e ZHA](/zigbee/) — a malha dos sensores
- [ZBT-1 e ZBT-2](/zbt-dongles/) — os dongles oficiais
- [MQTT](/mqtt/) — o correio da casa
- [Nabu Casa](/nabu-casa/) — a assinatura oficial
- [Claude e MCP](/claude-mcp/), [câmeras com IA](/cameras-ia/) e [OpenClaw](/openclaw/) — inteligência artificial em casa
- [Matter e Thread](/matter-thread/) — o padrão que atravessa ecossistemas
- [Apple HomeKit](/apple-homekit/) — integração com iPhone, Siri e Apple TV
- [Scrypted, Frigate e câmeras](/scrypted/) — vídeo local
- [Hardware](/hardware/) e [rede](/rede-wifi/) — a base de tudo
- [CasaOS e umbrelOS](/casaos-umbrel/) — os serviços da casa
- [Comandos do HAOS](/comandos-haos/) — referência de linha de comando

## Como o site é feito

Construí este site com HTML, CSS e JavaScript sem frameworks. Uso um gerador em **Python** a partir de
arquivos Markdown, versionado no **GitHub** e publicado no **Cloudflare**. Sem banco de dados, sem
cadastro de leitores. Uso Google Analytics para métricas de acesso e incluí integração com Google AdSense
para publicidade, sujeita à aprovação do site pelo Google. Anúncios não determinam os temas ou as
recomendações editoriais. Veja a [Política de privacidade](/privacidade/) para conhecer o uso de cookies,
os serviços de terceiros e as opções de controle.

O gerador fica em `build.py`, com módulos separados para os componentes visuais e a biblioteca
`Markdown` como dependência declarada. O conteúdo fica em arquivos `.md` na pasta `content/`.
Depois de instalar as dependências de `requirements.txt`, `python3 build.py` gera o site em `dist/`;
`python3 scripts/check.py` verifica os links internos e os templates antes da publicação.

<span id="quem-escreve"></span>

## Quem sou

<div class="author-box" markdown="0">
  <img src="/static/img/alvaro-retrato-20261021.jpg" alt="Álvaro Menezes" width="666" height="1180" loading="lazy">
  <div>
    <p class="author-name">Álvaro Menezes</p>
    <p class="author-role">Montei minha instalação de automação e criei o SmartHome-AI para compartilhar o que aprendo.</p>
    <p class="author-links">
      <a class="ext" href="https://github.com/alvaroajm" target="_blank" rel="noopener">GitHub</a>
    </p>
  </div>
</div>

Sou **Álvaro Menezes**, entusiasta de automação residencial, Home Assistant, ESP32 e sistemas locais. Escrevo os guias e compartilho aqui a instalação que montei em casa.

<span id="outros-canais-do-autor"></span>

## Meus outros canais

Também mantenho projetos de vídeo gerados com IA, sem relação direta com casa inteligente. Deixo os links aqui, fora dos guias, para quem quiser conhecer:

{{channels}}

## Equipamentos usados em casa

Uso **Home Assistant OS em um mini-PC com processador Ryzen 7**, **interruptores inteligentes Zemismart Zigbee** e **luzes Philips Hue Zigbee**.

Controlo minha rede Zigbee pelo **Home Assistant**, por meio do **Zigbee2MQTT**, com o **ZBT-2 da Nabu Casa** como coordenador.

Minha rede **Thread** é compartilhada com a rede Thread da **Apple**. Uso o **ZBT-1** como adaptador de rádio Thread, separado do ZBT-2 usado para Zigbee.

Na **sala**, tenho uma **tomada Zemismart** que controla as luzes do ambiente. Uso **Philips Hue** na **sala** e na **suíte master**. Aciono as luzes pelo **aplicativo Casa da Apple (HomeKit)** no celular, por voz pela **Alexa** e diretamente pelo **Home Assistant**.

Esta é a minha instalação, não uma lista de produtos que submeti a testes comparativos. Ainda preciso detalhar aqui os modelos exatos dos demais dispositivos. Não apresento essa relação como garantia de compatibilidade para uma compra.

Uso vários dispositivos que identifiquei como **Echo Dot Max** e **um Echo Studio Max na sala**. Faço a integração da Alexa com o Home Assistant pelo **Nabu Casa**. Também uso **duas Apple TV 4K como centrais do Apple HomeKit**.

Tenho ainda um **controle Broadlink IR e RF**, fotografado no [registro da minha instalação](/minha-instalacao/#interruptores-na-parede-e-controle-broadlink), junto aos interruptores Zemismart Zigbee.

### Tiras de LED

Controlo as **tiras de LED da minha instalação pelo WLED, via Wi-Fi**.

### Câmeras

Uso **Tapo TC70**, **Intelbras iM4** e um **DVR Intelbras**. Na minha instalação, descrevo o caminho das imagens como **câmeras → Home Assistant → Scrypted → HomeKit Secure Video**. Ainda preciso documentar aqui o modelo do DVR, a origem de vídeo e os plugins usados no Scrypted; esse arranjo não é um procedimento universal para outras instalações.

## Registro da instalação

Veja [minha instalação em detalhes](/minha-instalacao/), com fotos do mini-PC, Mac mini M4, tela ESP32-S3 configurada pelo ESPHome, Apple TV e robô aspirador Roborock. O conjunto também inclui um hub Philips Hue.

<div class="lesson-split" markdown="0">
<figure class="ha-screen"><a href="/static/img/casa-do-autor/central-home-assistant.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Minha central com Home Assistant"><img src="/static/img/casa-do-autor/central-home-assistant.jpg" alt="Minha central com Home Assistant" width="960" height="1280" loading="lazy" decoding="async"></a><figcaption><strong>Minha central com Home Assistant</strong> O mini-PC com HAOS e o Mac mini M4 são computadores distintos.</figcaption></figure>
<figure class="ha-screen"><a href="/static/img/casa-do-autor/tela-esphome.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Minha tela ESP32-S3 com ESPHome"><img src="/static/img/casa-do-autor/tela-esphome.jpg" alt="Minha tela ESP32-S3 com ESPHome" width="960" height="1280" loading="lazy" decoding="async"></a><figcaption><strong>Minha tela ESP32-S3 com ESPHome</strong> Uma interface dedicada com informações e atalhos para os cômodos.</figcaption></figure>
</div>

## A sala em imagens

Estas são fotos da minha sala: iluminação junto ao painel da TV, luminárias e luzes de destaque nos móveis. Controlo as tiras de LED pelo WLED via Wi-Fi e uso o app Casa, a Alexa e o Home Assistant para acionar as luzes. As fotografias mostram os ambientes e os equipamentos; os detalhes das integrações precisam acompanhar os respectivos guias.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" target="_blank" rel="noopener" aria-label="Ampliar foto: Vista da sala integrada à área de jantar, com sofá, poltronas e piano."><img src="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" alt="Vista da sala integrada à área de jantar, com sofá, poltronas e piano." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Vista da sala integrada à área de jantar, com sofá, poltronas e piano. Foto da minha instalação.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-painel-tv.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Painel da televisão com abajures e iluminação sob o móvel."><img src="/static/img/casa-do-autor/sala-painel-tv.jpg" alt="Painel da televisão com abajures e iluminação sob o móvel." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Painel da televisão com abajures e iluminação sob o móvel. Foto da minha instalação.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira."><img src="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" alt="Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira. Foto da minha instalação.</figcaption></figure>

## Como interpretar os guias

Os diagramas originais são esquemas conceituais, não capturas da interface nem retratos de modelos comerciais. As instruções oficiais estão vinculadas junto às ilustrações. Exemplos de configuração e roteiros de teste devem ser adaptados à sua instalação. Um exemplo didático não comprova compatibilidade com todos os aparelhos.

Nos meus relatos, procuro distinguir os equipamentos que uso das configurações e dos resultados que documentei. Quando esses detalhes não estiverem presentes, apresento orientações baseadas nas fontes citadas, não um ensaio de produto. Você pode consultar o [histórico público de alterações](https://github.com/alvaroajm/smarthome-ai/commits/main/) e enviar correções pelo contato abaixo.

## Contato e correções

Encontrou um erro, tem uma sugestão ou quer indicar um tema? Correções são muito bem-vindas — este site é
mantido publicamente e melhora com quem o lê.

Fale comigo pelo e-mail [alvaroajm@gmail.com](mailto:alvaroajm@gmail.com).
