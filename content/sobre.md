---
title: Sobre o SmartHome-AI
slug: sobre
description: Um projeto independente sobre casa inteligente local, código aberto e automação que funciona no mundo real.
category: Sobre
icon: book
order: 20
section: pagina
reading: 3 min de leitura
date: 2026-09-21
updated: 2026-10-20
tags: [Sobre, Contato, Open Source]
---

<img src="/static/img/smarthome-banner.jpg?v=20261021" alt="Banner do SmartHome-AI" width="1400" height="788" decoding="async">


O **SmartHome-AI** nasceu de uma frustração comum: a maior parte do conteúdo sobre casa inteligente ou é
propaganda de produto, ou é tão técnica que assume que você já sabe o que é um broker MQTT.

Aqui o compromisso é outro: **explicar o porquê antes do como**, com exemplos que funcionam em casas reais
— inclusive nas que têm internet instável, paredes grossas e moradores que não querem saber de tecnologia.

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

Este site é estático: HTML, CSS e JavaScript sem frameworks, gerado por um script em **Python** a partir de
arquivos Markdown, versionado no **GitHub** e publicado no **Cloudflare**. Sem banco de dados, sem
cadastro de leitores. Usa Google Analytics para métricas de acesso e inclui integração com Google AdSense
para publicidade, sujeita à aprovação do site pelo Google. Anúncios não determinam os temas ou as
recomendações editoriais. Veja a [Política de privacidade](/privacidade/) para conhecer o uso de cookies,
os serviços de terceiros e as opções de controle.

O código do gerador é simples de propósito: cerca de 300 linhas, com uma única dependência
(a biblioteca `Markdown`). Qualquer pessoa consegue clonar, escrever um arquivo `.md` na pasta `content/`,
rodar `python3 build.py` e ter o site pronto.

## Quem escreve

<div class="author-box" markdown="0">
  <img src="/static/img/author-original.jpg" alt="Dr. Álvaro Menezes" width="170" height="238" loading="lazy">
  <div>
    <p class="author-name">Dr. Álvaro Menezes</p>
    <p class="author-role">Médico radiologista · CRM 11.393/CE · RQE 6562<br>Radiologia geral e musculoesquelética — Fortaleza/CE</p>
    <p class="author-links">
      <a class="ext" href="https://alvaro-menezes.com" target="_blank" rel="noopener">alvaro-menezes.com</a> ·
      <a class="ext" href="https://radapps.app" target="_blank" rel="noopener">radapps.app</a> ·
      <a class="ext" href="https://github.com/alvaroajm" target="_blank" rel="noopener">GitHub</a>
    </p>
  </div>
</div>

Conteúdo por **Dr. Álvaro Menezes** — médico radiologista, entusiasta de automação residencial, Home Assistant,
ESP32 e sistemas locais. Os guias reúnem explicações e referências para quem está montando sua própria instalação.

## Outros canais do autor

Além do canal principal no YouTube, o autor mantém projetos de vídeo gerados com IA, sem relação direta com casa inteligente. Ficam aqui, fora dos guias, para quem quiser conhecer:

{{channels}}

## Equipamentos usados em casa

O autor utiliza **Home Assistant OS em um mini-PC com processador Ryzen 7**, **interruptores inteligentes Zemismart Zigbee** e **luzes Philips Hue Zigbee**.

Na **sala**, uma **tomada Zemismart** está instalada e controla as luzes do ambiente, conforme relato do autor. As **luzes Philips Hue** estão presentes na **sala** e na **suíte master**. O autor aciona as luzes pelo celular usando o **aplicativo Casa da Apple (HomeKit)**, por comandos de voz pela **Alexa** e diretamente pelo **Home Assistant**.

Esse é o conjunto informado pelo autor, não uma lista de produtos testados neste site. Os modelos exatos, o coordenador e a integração Zigbee utilizada ainda não estão documentados aqui; por isso, essa descrição não deve ser usada como garantia de compatibilidade para uma compra. Relatos específicos de automações precisam trazer a configuração e os resultados de cada caso.

O autor utiliza vários dispositivos identificados por ele como **Echo Dot Max** e **um Echo Studio Max na sala**. A integração da Alexa com o **Home Assistant** é feita pelo **Nabu Casa**, conforme seu relato. Também utiliza **duas Apple TV 4K como centrais da casa no Apple HomeKit**.

O conjunto inclui também um **controle Broadlink IR e RF**, fotografado no [registro da instalação](/minha-instalacao/#interruptores-na-parede-e-controle-broadlink), junto aos interruptores Zemismart Zigbee.

### Tiras de LED

As **tiras de LED** da instalação são controladas pelo **aplicativo WLED, via Wi-Fi**, conforme informado pelo autor.

### Câmeras

Na instalação descrita pelo autor, as câmeras enviam imagens ao **Home Assistant** e, a partir dele, o **Scrypted** encaminha o vídeo ao **HomeKit Secure Video**. Os equipamentos informados são a **câmera Tapo TC70**, um **DVR Intelbras** e a **câmera Intelbras iM4**. Esse é o fluxo relatado para sua casa; o modelo do DVR e a configuração da conexão de cada equipamento com o Scrypted ainda não estão documentados aqui.

## Registro da instalação

Veja [minha instalação em detalhes](/minha-instalacao/), com fotos do mini-PC, Mac mini M4, tela ESP32-S3 configurada pelo ESPHome, Apple TV e robô aspirador Roborock. O conjunto também inclui um hub Philips Hue.

## A sala em imagens

Fotos da sala fornecidas pelo autor. Elas mostram o ambiente em que os equipamentos descritos são usados: iluminação junto ao painel da TV, luminárias e luzes de destaque nos móveis. O autor informa que controla as tiras de LED pelo WLED via Wi-Fi. O controle das luzes pelo Casa, Alexa e Home Assistant foi relatado pelo autor; as imagens mostram a disposição física, não o funcionamento das integrações.

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" target="_blank" rel="noopener" aria-label="Ampliar foto: Vista da sala integrada à área de jantar, com sofá, poltronas e piano."><img src="/static/img/casa-do-autor/sala-vista-geral.jpg?v=20261021" alt="Vista da sala integrada à área de jantar, com sofá, poltronas e piano." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Vista da sala integrada à área de jantar, com sofá, poltronas e piano. Imagem fornecida por Álvaro Menezes.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-painel-tv.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Painel da televisão com abajures e iluminação sob o móvel."><img src="/static/img/casa-do-autor/sala-painel-tv.jpg" alt="Painel da televisão com abajures e iluminação sob o móvel." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Painel da televisão com abajures e iluminação sob o móvel. Imagem fornecida por Álvaro Menezes.</figcaption></figure>

<figure class="ha-screen"><a href="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" target="_blank" rel="noopener" aria-label="Ampliar foto: Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira."><img src="/static/img/casa-do-autor/sala-iluminacao-lateral.jpg" alt="Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira." width="1280" height="960" loading="lazy" decoding="async"></a><figcaption>Vista lateral da sala, com luminárias de piso e iluminação ao redor da cristaleira. Imagem fornecida por Álvaro Menezes.</figcaption></figure>

## Como interpretar os guias

Capturas identificadas como oficiais pertencem à documentação dos respectivos projetos; não são capturas da casa do autor. Exemplos de configuração e roteiros de teste devem ser adaptados à sua instalação. Um exemplo didático não comprova compatibilidade com todos os aparelhos.

Relatos de experiência devem informar os equipamentos, versões, condições e resultados observados. Quando esses dados não estiverem presentes, trate o conteúdo como orientação baseada nas fontes citadas, e não como ensaio de produto. Você pode consultar o [histórico público de alterações](https://github.com/alvaroajm/smarthome-ai/commits/main/) e enviar correções pelo contato abaixo.

## Contato e correções

Encontrou um erro, tem uma sugestão ou quer indicar um tema? Correções são muito bem-vindas — este site é
mantido publicamente e melhora com quem o lê.

Fale comigo pelo WhatsApp [+55 (85) 99662-1818](https://wa.me/5585996621818) ou pelo e-mail [alvaroajm@gmail.com](mailto:alvaroajm@gmail.com).
