---
title: O que é Home Assistant?
slug: home-assistant
description: Descubra automações, voz, aplicativos, marcas, ESPHome e câmeras em uma casa conectada com Home Assistant.
category: Passo a passo
icon: book
order: 2
featured: true
level: basico
reading: 9 min de leitura
date: 2026-09-23
tags: [Home Assistant]
---

Imagine dizer **“hora do cinema”** e ver a TV ligar, as cortinas fecharem e as luzes assumirem a cor que você escolheu. Ou entrar no corredor à noite e encontrar uma luz suave, acesa apenas enquanto você precisa dela.

O **Home Assistant** reúne aparelhos compatíveis e transforma essas ideias em controles, cenas e automações. É gratuito, de código aberto e dá prioridade ao controle local. O **Home Assistant OS (HAOS)** cuida da instalação, das atualizações e dos Apps: é o caminho deste guia.

## Um painel para a casa inteira

Luzes, TVs, ar-condicionados, ventiladores, termostatos, interruptores (switches), tomadas, cortinas e alarmes podem aparecer no mesmo painel. Você escolhe os cômodos, os controles e as informações que fazem sentido para sua família.

<figure class="ha-screen"><a href="/static/img/ha-guide/dashboard.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Um exemplo real de dashboard do Home Assistant, organizado por ambiente."><img src="/static/img/ha-guide/dashboard.png" alt="Um exemplo real de dashboard do Home Assistant, organizado por ambiente." width="1701" height="1299" loading="lazy" decoding="async"></a><figcaption>Um exemplo real de dashboard do Home Assistant, organizado por ambiente. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding_dashboard/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

**RGBCCT** combina cores RGB com ajuste da temperatura do branco. Assim, uma lâmpada ou fita compatível pode oferecer luz branca para trabalhar, um tom quente para jantar e cores para uma noite de cinema. Brilho e funções disponíveis dependem do produto.

Você controla pelo navegador, celular, voz ou automação. Um comando para ar-condicionado pode usar uma integração de rede ou um emissor infravermelho compatível; neste último caso, nem sempre há confirmação do estado real do aparelho.

## As marcas conversam através do Home Assistant

O catálogo oficial apresenta **mais de 1.500 integrações**. Elas conectam marcas, aparelhos e serviços; não é necessário que todos sejam do mesmo fabricante.

<div class="ha-brand-list" aria-label="Exemplos de integrações"><a href="https://www.home-assistant.io/integrations/webostv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/lg.png" width="537" height="256" alt="" loading="lazy" decoding="async"></span><strong>LG</strong><span class="manufacturer-description">TVs e eletrodomésticos conectados.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/samsungtv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/samsung.png" width="1150" height="256" alt="" loading="lazy" decoding="async"></span><strong>Samsung</strong><span class="manufacturer-description">TVs e aparelhos do ecossistema SmartThings.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/tuya/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/tuya.png" width="512" height="256" alt="" loading="lazy" decoding="async"></span><strong>Tuya / Smart Life</strong><span class="manufacturer-description">A plataforma por trás de muitos produtos Smart Life.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/zha/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/aqara.png" width="881" height="256" alt="" loading="lazy" decoding="async"></span><strong>Aqara</strong><span class="manufacturer-description">Sensores, botões, cortinas e outros acessórios.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/braviatv/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/sony.png" width="1465" height="256" alt="" loading="lazy" decoding="async"></span><strong>Sony</strong><span class="manufacturer-description">TVs Bravia para completar a cena de cinema.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/homekit_controller/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/eve.png" width="666" height="256" alt="" loading="lazy" decoding="async"></span><strong>Eve</strong><span class="manufacturer-description">Sensores, tomadas e acessórios para a casa.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/tplink/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/tapo.png" width="646" height="256" alt="" loading="lazy" decoding="async"></span><strong>Tapo / TP-Link</strong><span class="manufacturer-description">Tomadas, iluminação e câmeras conectadas.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/reolink/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/reolink.png" width="1166" height="256" alt="" loading="lazy" decoding="async"></span><strong>Reolink</strong><span class="manufacturer-description">Câmeras e gravadores de vídeo em rede.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/onvif/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/intelbras.png" width="1248" height="256" alt="" loading="lazy" decoding="async"></span><strong>Intelbras</strong><span class="manufacturer-description">Câmeras de segurança; verifique ONVIF ou RTSP.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/hue/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/hue.png" width="653" height="256" alt="" loading="lazy" decoding="async"></span><strong>Philips Hue</strong><span class="manufacturer-description">Lâmpadas, fitas e luminárias para criar ambientes.</span><span class="manufacturer-cta">Ver integração ↗</span></a><a href="https://www.home-assistant.io/integrations/epson/" target="_blank" rel="noopener"><span class="manufacturer-logo" aria-hidden="true"><img src="/static/img/manufacturers/epson.png" width="957" height="256" alt="" loading="lazy" decoding="async"></span><strong>Epson</strong><span class="manufacturer-description">Projetores compatíveis para o seu cinema em casa.</span><span class="manufacturer-cta">Ver integração ↗</span></a></div>
<aside class="hue-explainer"><h4>Philips Hue: a luz também cria o ambiente.</h4><p>Hue é uma linha de iluminação inteligente: lâmpadas, fitas de LED e luminárias. Conforme o modelo, você ajusta brilho, branco quente ou frio e cores. Uma cena combina esses ajustes — como uma luz suave para jantar ou tons coloridos para o cinema.</p><p>A Hue Bridge é a central da marca. O Home Assistant conversa localmente com ela para controlar luzes e cenas. Outra opção é parear lâmpadas Zigbee compatíveis diretamente com ZHA + ZBT-2; nesse caso, os recursos disponíveis podem mudar.</p><a class="ext" href="https://www.philips-hue.com/en-us/explore-hue" target="_blank" rel="noopener">Conhecer a Philips Hue</a></aside>
<details class="feature-details"><summary>Como conectar cada marca?</summary><ul class="ha-brand-notes"><li><strong>LG</strong><span>TVs webOS com controle local; eletrodomésticos ThinQ usam outra integração, em nuvem.</span></li><li><strong>Samsung</strong><span>TVs compatíveis pela rede local; outros aparelhos podem usar SmartThings, em nuvem.</span></li><li><strong>Tuya / Smart Life</strong><span>A integração oficial usa nuvem. Dispositivos Zigbee compatíveis podem entrar direto no ZHA.</span></li><li><strong>Aqara</strong><span>Sensores Zigbee compatíveis pelo ZHA; produtos Matter ou HomeKit seguem outro caminho.</span></li><li><strong>Sony</strong><span>TVs Bravia compatíveis: volume, entradas e reprodução, conforme o modelo.</span></li><li><strong>Eve</strong><span>Acessórios HomeKit pelo HomeKit Device; versões Matter pela integração Matter.</span></li><li><strong>Tapo / TP-Link</strong><span>Tomadas, interruptores, luzes e câmeras suportadas; confira a lista e a autenticação.</span></li><li><strong>Reolink</strong><span>Vídeo e eventos locais nos modelos suportados; aparelhos a bateria têm requisitos próprios.</span></li><li><strong>Intelbras</strong><span>Câmeras com ONVIF Profile S compatível ou fluxo RTSP. Nem toda a linha oferece esses recursos.</span></li><li><strong>Philips Hue</strong><span>Luzes e cenas locais pela Hue Bridge. Lâmpadas Zigbee compatíveis também podem usar ZHA.</span></li><li><strong>Epson</strong><span>Projetores de rede compatíveis: energia e seleção de entrada para a cena de cinema.</span></li></ul><p>Antes de comprar, confira modelo, firmware e funções disponíveis. Uma integração pode atender várias marcas; uma marca pode usar várias integrações.</p></details><p class="feature-small"><a href="/static/img/manufacturers/README.md">Créditos dos logotipos</a> · Marcas de seus respectivos titulares. Exemplos, sem vínculo oficial.</p>

Uma TV LG, um sensor Aqara e uma luz Philips Hue podem participar da mesma automação. A compatibilidade é do **modelo e da função**, não apenas da marca. TVs LG webOS e Samsung têm opções locais; [LG ThinQ](https://www.home-assistant.io/integrations/lg_thinq/) e [SmartThings](https://www.home-assistant.io/integrations/smartthings/) usam nuvem nas respectivas integrações.

## Cenas de luz: a mesma sala, seis climas

Depois de escolher as lâmpadas, o que muda a casa de verdade são as **cenas**. Passe o mouse ou toque nas imagens para ver cada ambiente em movimento; clique para trocar a iluminação de RGB exagerado para branco dia, leitura, manhã, pôr do sol e luz noturna.

{{scenes_showcase}}

## Automações: a parte mais divertida

Pense em três perguntas: **quando acontece, em quais condições e o que fazer?** O editor visual organiza exatamente isso.

- **Ao chegar:** acender a entrada se já estiver escuro.
- **Ao abrir a janela:** pausar a climatização, se a integração permitir.
- **Ao anoitecer:** fechar cortinas e escolher uma iluminação acolhedora.
- **Ao detectar alguém no portão:** enviar uma notificação com imagem, usando uma câmera ou NVR compatível.
- **Ao sair:** avisar se alguma porta ou janela ficou aberta.

<figure class="ha-screen"><a href="/static/img/ha-guide/automation.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Editor visual: escolha o gatilho, as condições e a ação."><img src="/static/img/ha-guide/automation.png" alt="Editor visual: escolha o gatilho, as condições e a ação." width="1021" height="586" loading="lazy" decoding="async"></a><figcaption>Editor visual: escolha o gatilho, as condições e a ação. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

Uma **cena** guarda estados desejados, como as luzes e cortinas para o cinema. Uma **automação** decide quando aplicar esses estados. Você pode criar ambas pelas telas. **Blueprints** são modelos reutilizáveis para certas automações: escolha um confiável e preencha os dispositivos pedidos.

[Crie sua primeira automação sem código](/primeira-automacao/).

## Alexa, Google Nest e Assist: pode falar

Você pode usar **Alexa em um Echo** ou **Google Assistant em um Google Nest** para acionar os dispositivos e cenas que disponibilizar. O Home Assistant Cloud, da Nabu Casa, simplifica essa conexão. Esses serviços dependem da internet e têm limites próprios para tipos de aparelho e comandos.

O **Assist** é o assistente de voz do Home Assistant. Funciona no celular e em equipamentos dedicados. Com processamento, idioma e hardware adequados, pode trabalhar localmente; também pode usar os serviços de voz do Home Assistant Cloud.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/voice-pe.webp" target="_blank" rel="noopener" aria-label="Ampliar: Home Assistant Voice Preview Edition ao lado do Green."><img src="/static/img/ha-features/voice-pe.webp" width="360" height="360" alt="Home Assistant Voice Preview Edition ao lado do Green." loading="lazy" decoding="async"></a><figcaption>Home Assistant Voice Preview Edition ao lado do Green. · <a class="ext" href="https://www.home-assistant.io/voice-pe/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

Também existem pontos de voz feitos com **ESP32 e ESPHome**, como o ATOM Echo. Eles captam sua fala e a encaminham ao Home Assistant. Uma placa ESP32 comum precisa dos componentes de áudio adequados; o ATOM-S3 com tela não é, sozinho, esse conjunto.

## O app no bolso e a casa ao alcance

O aplicativo **Home Assistant Companion**, para iOS e Android, mostra seu painel e pode receber avisos. No iPhone, iPad ou Android, você consulta sensores, controla aparelhos e vê as câmeras integradas.

Com sua permissão, o telefone também pode informar localização e outros sensores para automações. Em casa, a conexão pode ser local. Fora de casa, é necessário configurar um caminho de acesso remoto, como **Home Assistant Cloud ou VPN**. O app não substitui a central que permanece ligada em casa.

## Nabu Casa: praticidade e apoio ao projeto

A assinatura opcional **Home Assistant Cloud** oferece acesso remoto criptografado sem abrir portas no roteador, conexão facilitada com Alexa e Google, backup na nuvem e processamento de voz para o Assist.

A Nabu Casa é parceira comercial da **Open Home Foundation**, organização dos projetos Home Assistant e ESPHome. A assinatura ajuda a financiar esse desenvolvimento. Você pode usar automações locais sem contratar o serviço.

[Conheça as vantagens e a ativação pelas telas](/nabu-casa/).

## E quem gosta do app Casa da Apple?

O ecossistema Apple Home / HomeKit é mais fechado, com critérios próprios de compatibilidade. A integração **HomeKit Bridge** permite levar funções suportadas do Home Assistant ao app Casa e à Siri, inclusive de dispositivos sem HomeKit nativo.

Você escolhe o que compartilhar. Nem todos os recursos têm equivalente no app Casa. Para acesso remoto por ele, é necessária uma central Apple compatível, como HomePod ou Apple TV. Acessórios Matter ampliam a interoperabilidade.

[Conecte o Home Assistant ao app Casa](/apple-homekit/).

## IoT e DIY: crie o que está faltando

**IoT** é a internet das coisas: objetos conectados trocando informações, inclusive dentro da sua rede local. **DIY** é fazer você mesmo. Uma placa ESP32 pode virar um sensor de temperatura, um botão de cena ou um pequeno painel.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/esp32.webp" target="_blank" rel="noopener" aria-label="Ampliar: ESP32-DevKitC: placa de desenvolvimento de uso geral, com componentes identificados."><img src="/static/img/ha-features/esp32.webp" width="900" height="389" alt="ESP32-DevKitC: placa de desenvolvimento de uso geral, com componentes identificados." loading="lazy" decoding="async"></a><figcaption>ESP32-DevKitC: placa de desenvolvimento de uso geral, com componentes identificados. · <a class="ext" href="https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>
<figure class="feature-figure feature-product"><a href="/static/img/ha-features/atom-s3.webp" target="_blank" rel="noopener" aria-label="Ampliar: M5Stack ATOM-S3: uma opção compacta com tela e botão."><img src="/static/img/ha-features/atom-s3.webp" width="800" height="800" alt="M5Stack ATOM-S3: uma opção compacta com tela e botão." loading="lazy" decoding="async"></a><figcaption>M5Stack ATOM-S3: uma opção compacta com tela e botão. · <a class="ext" href="https://docs.m5stack.com/en/core/AtomS3" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

O **ESPHome**, projeto da Open Home Foundation apoiado pela Nabu Casa, oferece o App **Device Builder** no HAOS. O assistente cria uma configuração inicial. Projetos prontos ajudam você a começar; personalizações costumam usar YAML, uma descrição do dispositivo, sem escrever um programa em C++.

Uma IA pode explicar as opções, propor uma configuração e ajudar a entender erros. Isso torna o aprendizado mais acessível, mas ainda é preciso conferir placa, pinos e documentação e validar antes de gravar. Comece com um projeto alimentado por USB, em baixa tensão.

[Conheça o ESPHome pelas telas](/esphome-esp32/).

## Câmeras que ajudam a entender o que acontece

Ver a imagem no painel já é útil. Um **NVR**, sistema que grava e organiza os vídeos, acrescenta histórico e eventos. O Frigate pode detectar pessoas, carros e animais conforme o modelo de IA e fornecer eventos ao Home Assistant.

<figure class="feature-figure"><a href="/static/img/ha-features/frigate-live.webp" target="_blank" rel="noopener" aria-label="Ampliar: Tela oficial do Frigate NVR com várias câmeras."><img src="/static/img/ha-features/frigate-live.webp" width="1400" height="786" alt="Tela oficial do Frigate NVR com várias câmeras." loading="lazy" decoding="async"></a><figcaption>Tela oficial do Frigate NVR com várias câmeras. · <a class="ext" href="https://frigate.video/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

O reconhecimento facial compara rostos com uma biblioteca cadastrada e pode funcionar localmente, em hardware compatível. Já modelos de visão podem descrever ações, como alguém deixando uma caixa, usando processamento local ou nuvem conforme o provedor.

Esses recursos são adicionais, exigem configuração e podem errar. Use-os para enriquecer avisos; não para decidir sozinhos destrancar portas ou desarmar alarmes. Gravação e análise de várias câmeras precisam de armazenamento e processamento dimensionados.

[Veja os próximos passos para câmeras e IA](/cameras-ia/).

## Local, remoto e automático: cada coisa no seu lugar

**Local:** com aparelhos e integrações locais, as regras continuam sem internet, desde que a central, a rede e os dispositivos estejam ligados. Integrações de nuvem continuam dependendo dos serviços externos.

**Remoto:** você acessa a central de fora de casa por uma conexão configurada e protegida. Normalmente, isso exige internet nos dois lados.

**Automático:** sensores, horários e eventos iniciam regras na central, sem você precisar abrir o app.

**Zigbee e Thread** são especialmente interessantes para sensores a pilha: baixo consumo e rede em malha. Aparelhos adequados podem repetir o sinal. Eles precisam de uma central ou roteador de borda apropriado; Wi-Fi e Ethernet continuam úteis para câmeras, TVs e maior tráfego. Vamos detalhar isso depois, começando por **ZHA + ZBT-2**.

## Dê o primeiro passo

Você não precisa fazer tudo isso hoje. Escolha uma central, conecte uma luz e crie uma regra. A melhor parte é poder crescer no seu ritmo.

[Escolher o hardware](/#hardware-haos) · [Instalar o HAOS](/instalar-haos/) · [Entender Zigbee](/zigbee/).

Referências: [catálogo de integrações](https://www.home-assistant.io/integrations/), [automações](https://www.home-assistant.io/getting-started/automation/), [cenas](https://www.home-assistant.io/docs/scene/), [Assist](https://www.home-assistant.io/voice_control/), [aplicativos](https://companion.home-assistant.io/), [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/), [Nabu Casa](https://www.nabucasa.com/), [ESPHome](https://esphome.io/install/getting-started/) e [Frigate](https://docs.frigate.video/).
