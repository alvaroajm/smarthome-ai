---
level: avancado
title: Home Assistant no app Casa
slug: apple-homekit
description: Exponha luzes, sensores e câmeras do Home Assistant ao app Casa da Apple e à Siri com a integração HomeKit Bridge, passo a passo pelas telas.
category: Ecossistemas
icon: apple
order: 110
featured: true
reading: 8 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [HomeKit, Apple, Siri, Matter, iOS]
---

Você pode combinar a interface familiar do **app Casa**, da Apple, com a variedade de dispositivos e automações do **Home Assistant**.

## Uma ponte para um ecossistema mais fechado

Apple Home / HomeKit tem regras próprias de compatibilidade e depende de produtos Apple para parte da experiência. A integração **HomeKit Bridge** publica funções suportadas do Home Assistant no app Casa, inclusive de aparelhos que não possuem HomeKit nativo.

Assim, uma luz Zigbee ou um controle criado com ESPHome pode aparecer ao lado dos acessórios Apple Home que você já usa. A compatibilidade depende do tipo de entidade: nem toda função do Home Assistant pode ser traduzida para o app Casa.

## Configure pelas telas

1. No Home Assistant, abra **Configurações → Dispositivos e serviços → Adicionar integração**.
2. Procure **HomeKit Bridge** e siga o assistente para escolher os tipos de dispositivos que deseja compartilhar.
3. Abra a notificação com o código de pareamento.
4. No iPhone, abra **Casa → Adicionar acessório** e escaneie o código apresentado.
5. Organize os acessórios nos cômodos e teste um comando simples com a Siri.

Comece com poucas luzes ou cortinas. Depois, ajuste o filtro da ponte pelas opções da integração para compartilhar mais dispositivos. Algumas categorias exigem configuração específica; siga a documentação do modelo e da integração.

## O que aparece no app Casa, e o que não aparece

A ponte traduz **tipos de entidade** do Home Assistant para categorias de acessório do HomeKit. A
documentação da integração lista o que é suportado; em resumo:

| Funciona bem | Com limitações | Não passa pela ponte |
|---|---|---|
| Luzes (liga/desliga, brilho, cor, temperatura de cor), interruptores, tomadas, sensores binários (porta, movimento, fumaça, vazamento), sensores de temperatura, umidade, luminosidade, CO₂, cortinas e persianas, ventiladores, termostatos, fechaduras, ar-condicionado por infravermelho (como "climate") | Câmeras e media players exigem o **modo acessório**, um por ponte; umidificadores, aspiradores e alarmes têm funções parciais; botões e controles remotos viram "interruptores programáveis" com uso limitado | Entidades sem equivalente no HomeKit, como texto, seletores, calendários e a maioria dos sensores com unidades fora do padrão, que podem aparecer como sensor genérico ou não aparecer |

A regra prática: se o aparelho faz algo que o app Casa já sabe mostrar, a ponte funciona; se faz algo
exclusivo do Home Assistant, continue usando o Home Assistant para isso.

## Modo ponte e modo acessório

A integração pode ser criada mais de uma vez, de dois modos:

- **Ponte (bridge):** uma única entrada no app Casa que carrega muitos acessórios. É o modo normal, e o
  limite recomendado é de cerca de 150 acessórios por ponte.
- **Acessório (accessory):** uma entrada para um único dispositivo. É obrigatório para câmeras, media
  players e TVs, porque o HomeKit trata cada um como um acessório próprio, com pareamento separado.

Se quiser uma câmera e dez luzes no app Casa, crie uma ponte para as luzes e uma integração em modo
acessório para cada câmera.

## Filtre antes de compartilhar

Na configuração da ponte, escolha **só os domínios e entidades** que fazem sentido no app Casa. Dois
motivos: cada entidade exposta aparece como acessório no iPhone de toda a família, e entidades que
mudam de nome ou somem no Home Assistant viram acessórios "sem resposta" no app Casa. Uma boa primeira
seleção é: luzes, cortinas, sensores de porta e de temperatura dos cômodos principais.

## Onde deixar as automações

As duas plataformas automatizam, e é tentador espalhar regras pelas duas. Uma divisão que funciona:

- **No Home Assistant:** tudo que depende de vários dispositivos, de horários complexos, de
  condições ou de aparelhos que só o Home Assistant vê. É onde as regras ficam documentadas e com
  histórico.
- **No app Casa:** só o que é da Apple, como cenas acionadas pela Siri, atalhos no iPhone e a automação
  "ao chegar em casa" baseada na localização dos iPhones, quando ela funcionar melhor do que a do
  Home Assistant.

Na [minha casa](/minha-instalacao/), o Home Assistant é a central, e duas Apple TV 4K servem como
centrais do HomeKit para o acesso pelo app Casa.

## Siri e acesso remoto

Os controles compatíveis podem ser acionados pela Siri. Para controlar pelo app Casa fora de casa, é necessária uma **central Apple compatível**, como um HomePod ou Apple TV configurado como central.

Isso é diferente do acesso remoto pelo **Home Assistant Companion**, que pode usar Home Assistant Cloud ou VPN. A Nabu Casa não é necessária para criar a ponte HomeKit local.

## HomeKit Bridge e HomeKit Device não são a mesma coisa

| Integração | Direção |
|---|---|
| HomeKit Bridge | Leva funções do Home Assistant ao app Casa. |
| HomeKit Device | Adiciona ao Home Assistant acessórios que falam o protocolo HomeKit. |
| Matter | Conecta acessórios Matter compatíveis; o compartilhamento entre controladores depende do suporte do produto. |

Acessórios **Eve** e **Aqara**, por exemplo, podem ter versões HomeKit, Matter ou Zigbee. Confira o modelo antes de escolher a integração. HomeKit sobre Thread também exige a infraestrutura Thread adequada.

## E as câmeras?

Mostrar uma câmera através da HomeKit Bridge não fornece automaticamente gravação **HomeKit Secure Video**. Vídeo ao vivo, eventos, áudio e gravação são recursos distintos. Para gravação na nuvem da Apple e detecção de pessoas no app Casa, a ferramenta usada é o [Scrypted](/scrypted/), que publica as câmeras como acessórios compatíveis com o HomeKit Secure Video. Deixe a integração avançada de câmeras para uma etapa posterior.

## Problemas comuns

- **O app Casa não encontra a ponte.** A descoberta usa mDNS na rede local. Celular e central precisam
  estar na mesma rede (ou com mDNS repetido entre VLANs), e o Wi-Fi do iPhone não pode isolar clientes.
  Confira também se o Home Assistant mostra a notificação com o código; sem ela, a ponte ainda não
  está pronta.
- **"Acessório já adicionado".** Uma ponte antiga ficou registrada no app Casa. Remova-a lá, apague e
  recrie a integração no Home Assistant e pareie de novo.
- **Acessórios "sem resposta".** Em geral, a entidade mudou de nome ou foi removida no Home Assistant.
  Corrija a seleção da ponte; se o problema é geral, reinicie a integração.
- **Comando funciona no Home Assistant, mas não pela Siri.** A Siri precisa de uma central Apple ativa
  (HomePod ou Apple TV) para comandos fora de casa e para algumas categorias; dentro de casa, confira se
  o iPhone está na mesma rede.
- **Depois de restaurar um backup do Home Assistant em outra máquina, tudo sumiu do app Casa.** O
  pareamento HomeKit é guardado na central; restaure o backup completo e, se necessário, pareie de
  novo.

## Quando usar Matter em vez da ponte

A ponte HomeKit leva ao app Casa aparelhos que o Home Assistant já controla, de qualquer protocolo. O
[Matter](/matter-thread/) faz o caminho inverso: um aparelho Matter pode ser pareado diretamente no
app Casa e também no Home Assistant, sem ponte. Para dispositivos Zigbee, ESPHome e de nuvem, a ponte
continua sendo o único caminho; para um aparelho novo que já é Matter, parear nos dois controladores
costuma ser mais simples.

[Voltar às possibilidades do Home Assistant](/home-assistant/) · [Conhecer o acesso remoto da Nabu Casa](/nabu-casa/).

Fontes: [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/), [HomeKit Device](https://www.home-assistant.io/integrations/homekit_controller/), [Matter](https://www.home-assistant.io/integrations/matter/) e [central da casa Apple](https://support.apple.com/pt-br/102557).
