---
title: Integrações, Apps, HACS e câmeras
slug: apps-integracoes
description: Integrações, Apps e HACS explicados: quais valem no começo, como reconhecer uma integração local ou de nuvem e como colocar a primeira câmera no painel.
category: Passo a passo
icon: book
order: 8
featured: true
level: basico
reading: 8 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

Sua primeira automação não precisa de tudo isto. Conheça os nomes para saber o que procurar quando
quiser expandir, e principalmente para não instalar o que não precisa: cada peça a mais é uma peça a
manter.

## As quatro peças, numa frase cada

- **Integração:** a conexão do Home Assistant com uma marca, um serviço ou um protocolo. Vem com o
  Home Assistant.
- **App (antes "Add-on"):** um programa extra que roda ao lado do Home Assistant, dentro do HAOS, como
  um servidor MQTT ou o editor de arquivos.
- **HACS:** um catálogo da comunidade para integrações e cartões de painel que não fazem parte do
  conjunto oficial.
- **Câmera:** no Home Assistant, é só mais uma entidade, trazida por uma integração.

## 1. Integrações: conexões com aparelhos

Uma **integração** permite que o Home Assistant converse com uma marca, serviço ou rede. O ZHA já é a
integração da sua rede Zigbee. Cada integração cria **dispositivos** (o aparelho físico) e
**entidades** (cada coisa que ele mede ou controla: a luz, o brilho, a temperatura, a bateria).

Para adicionar outra, abra **Configurações → Dispositivos e serviços → Adicionar integração**. Procure a
marca ou o serviço e siga as instruções. Alguns aparelhos aparecem automaticamente na seção
*Descobertos*, porque se anunciam na rede.

<figure class="ha-screen"><a href="/static/img/ha-guide/integrations.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A tela reúne integrações configuradas e aparelhos descobertos."><img src="/static/img/ha-guide/integrations.png" alt="A tela reúne integrações configuradas e aparelhos descobertos." width="1365" height="860" loading="lazy" decoding="async"></a><figcaption>A tela reúne integrações configuradas e aparelhos descobertos. <a class="ext" href="https://www.home-assistant.io/getting-started/integration/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

### Local ou nuvem? Leia o selo

Na página de cada integração, a documentação oficial informa a classe de conexão. Ela decide se a
automação sobrevive sem internet:

| Classe | Significa | Exemplos |
|---|---|---|
| **Local push** | O aparelho avisa o Home Assistant na hora, pela rede local. É a melhor. | ZHA, ESPHome, MQTT, hub Philips Hue. |
| **Local polling** | O Home Assistant pergunta ao aparelho de tempos em tempos, pela rede local. | Muitas câmeras ONVIF, impressoras, alguns roteadores. |
| **Cloud push / polling** | Passa pelos servidores do fabricante. Sem internet, para. | Integrações oficiais de robôs aspiradores e de muitos produtos Wi-Fi. |

Prefira as locais sempre que houver escolha. Quando só existe a de nuvem, use e saiba o que acontece
quando a internet cai.

### Integrações que valem no primeiro mês

- **App companheiro (Mobile App):** configurada ao fazer login no celular. Traz localização, bateria,
  e notificações, que são a base de "avise se a porta ficou aberta".
- **Sun (Sol):** já vem ativa; é o pôr do sol da primeira automação.
- **Philips Hue:** se você tem o hub Hue, a integração local aparece sozinha; basta apertar o botão
  do hub. É o caso da [minha casa](/minha-instalacao/), que mantém as Hue no hub da Philips.
- **HomeKit Bridge:** expõe dispositivos do Home Assistant ao app Casa da Apple. Guia:
  [Home Assistant no app Casa](/apple-homekit/).
- **Home Assistant Cloud:** necessária para Alexa e Google Assistant sem abrir portas. Guia:
  [Nabu Casa](/nabu-casa/).
- **Cast, Apple TV, DLNA:** controle de TVs e caixas de som, úteis para "pausar o filme quando a
  campainha toca".

## 2. Apps, antes chamados Add-ons

**Apps** são programas extras instalados no HAOS. Eles têm uma função própria, como acrescentar um
serviço que determinado projeto exige. São diferentes das integrações: o App fornece o serviço; a
integração conecta o Home Assistant a ele.

Procure **Configurações → Apps** e a loja. Em versões anteriores, o nome pode aparecer como
**Complementos / Add-ons**. Leia a documentação do App e instale somente quando necessário.

**ZHA não precisa de MQTT nem de um App adicional.**

<figure class="ha-screen"><a href="/static/img/ha-guide/apps.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A loja de Apps do Home Assistant OS. Você não precisa instalar tudo."><img src="/static/img/ha-guide/apps.png" alt="A loja de Apps do Home Assistant OS. Você não precisa instalar tudo." width="1138" height="608" loading="lazy" decoding="async"></a><figcaption>A loja de Apps do Home Assistant OS. Você não precisa instalar tudo. <a class="ext" href="https://www.home-assistant.io/getting-started/concepts-terminology/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

### Os Apps que mais aparecem, e quando cada um entra

| App | Para quê | Quando instalar |
|---|---|---|
| **Studio Code Server** ou **File editor** | Editar `configuration.yaml` e outros arquivos pelo navegador. | Quando um guia pedir uma edição manual. |
| **Terminal & SSH** | Linha de comando dentro do HAOS. | Para os [comandos do HAOS](/comandos-haos/) e diagnósticos. |
| **Samba share** | Ver a pasta de configuração a partir do Mac ou do Windows, inclusive para copiar backups. | Ao configurar backups fora da central. |
| **Mosquitto broker** | Servidor MQTT. | Só com Zigbee2MQTT, Tasmota ou projetos que usem [MQTT](/mqtt/). |
| **Zigbee2MQTT** | Alternativa ao ZHA. | Só após ler [quando considerar a mudança](/zigbee2mqtt/). |
| **ESPHome Device Builder** | Criar e atualizar dispositivos [ESPHome](/esphome-esp32/). | Com a primeira placa ESP32. |
| **Matter Server** | Instalado automaticamente pela integração Matter. | Com o primeiro dispositivo [Matter](/matter-thread/). |
| **Music Assistant** | Música e rádio em caixas de som e TVs. | Quando quiser som nas automações. |
| **Frigate** | Gravação e detecção de objetos nas câmeras. | Depois de ver a imagem; veja [câmeras com IA](/cameras-ia/). |

Dois ou três Apps bastam para a maioria das casas. Um sinal de alerta é a lista passar de dez: cada
App consome memória e pede atualização.

## 3. HACS: deixe para uma necessidade concreta

O **HACS** é um catálogo da comunidade para integrações e elementos de painel que não vêm no conjunto
oficial. Não é a loja de Apps do HAOS, e os componentes que ele instala não passam pela revisão da
equipe do Home Assistant.

Ele é opcional e seus componentes podem exigir manutenção ou deixar de funcionar após atualizações.
Prefira primeiro as integrações oficiais. Exemplos do que costuma motivar a instalação: cartões de
painel com visual diferente, integrações para marcas sem suporte oficial e temas. Quando houver um
recurso específico que você precise, siga a [documentação do HACS](https://hacs.xyz/docs/use/) e,
antes de instalar qualquer componente, veja a data da última atualização e as *issues* abertas no
repositório: um projeto abandonado quebra na próxima versão do Home Assistant.

## 4. Câmeras: comece vendo a imagem

Antes da compra, confira a integração do modelo. Algumas câmeras oferecem conexão local por **RTSP**
ou **ONVIF**, padrões que o Home Assistant entende sem app do fabricante; outras dependem do serviço do
fabricante e podem nem oferecer imagem ao vivo fora dele. Procure na caixa ou na documentação as
palavras "RTSP" ou "ONVIF": são o melhor sinal de que a câmera funcionará localmente.

1. Adicione a integração em **Dispositivos e serviços**: a da marca, se existir e for local; senão,
   **ONVIF**; senão, **Generic Camera** com o endereço RTSP da câmera (usuário e senha ficam na
   configuração da própria câmera).
2. Confirme que a imagem abre no Home Assistant, na página da entidade.
3. Pelo editor do painel, adicione um cartão de **imagem** ou **câmera ao vivo**.

Exibir vídeo não significa gravar. Gravação, alertas e detecção de pessoas são etapas posteriores,
abordadas em [câmeras no aprofundamento](/aprofundamento/#3-cameras). O painel ao vivo com várias
câmeras também pesa: no celular, prefira a imagem estática com atualização de alguns segundos.

Você não precisa instalar HACS para todas as câmeras. Primeiro veja o que a integração oficial oferece.

!!! nota "Câmeras e privacidade"
    Câmeras internas gravam quem mora e quem visita. Combine regras com a família, evite apontar para
    quartos e banheiros, troque a senha padrão da câmera e bloqueie o acesso dela à internet quando ela
    for usada só localmente.

## Em que ordem fazer tudo isto

1. Integrações locais dos aparelhos que você já tem (Hue, TV, impressora).
2. App companheiro no celular e a primeira notificação.
3. Um ou dois Apps, só quando um guia pedir.
4. A primeira câmera, até vê-la no painel.
5. HACS, apenas com um componente específico em mente.

Fontes: [integrações](https://www.home-assistant.io/getting-started/integration/),
[classes de conexão](https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things/),
[Apps](https://www.home-assistant.io/addons/), [HACS](https://hacs.xyz/docs/use/),
[câmeras](https://www.home-assistant.io/integrations/camera/), [ONVIF](https://www.home-assistant.io/integrations/onvif/)
e [Generic Camera](https://www.home-assistant.io/integrations/generic/).
