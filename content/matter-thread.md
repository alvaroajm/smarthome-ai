---
title: Thread e Matter, sem confusão
slug: matter-thread
description: Thread é a rede, Matter é o padrão. Entenda os papéis (controlador, roteador de borda, pareamento), o que conferir na embalagem, o que o Home Assistant precisa para cada caso e quando isso faz sentido na sua casa.
category: Passo a passo
icon: book
order: 5
featured: true
level: basico
reading: 8 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

**Thread é uma rede. Matter é um padrão de comunicação entre aparelhos e plataformas.** Um produto
Matter pode usar Thread, Wi-Fi ou Ethernet para chegar até a sua casa. Entender essa separação evita a
compra errada mais comum de quem está começando: um sensor "Matter" que não funciona porque a casa não
tem a rede que ele usa.

## A diferença em um exemplo

Uma lâmpada pode falar o padrão Matter e usar **Wi-Fi** para chegar ao roteador: ela precisa de energia
constante e tem rádio potente. Já um sensor de porta Matter costuma usar **Thread** para economizar
bateria: o rádio é fraco e de baixo consumo, por isso ele depende de uma malha de vizinhos e de um
"tradutor" que o leve até a rede principal.

| Na embalagem | O que conferir antes de comprar |
|---|---|
| **Matter sobre Wi-Fi** | Rede Wi-Fi de 2,4 GHz e um controlador Matter (o Home Assistant, o app Casa, o Google Home ou a Alexa). |
| **Matter sobre Thread** | Um controlador Matter **e** um roteador de borda Thread na mesma rede. Sem o roteador de borda, o aparelho não chega a lugar nenhum. |
| **Zigbee** | Coordenador Zigbee (ZBT-2) e suporte do modelo no ZHA. Não tem nada a ver com Matter, mesmo que a caixa use o mesmo rádio de 2,4 GHz. |

Um único equipamento pode cumprir os papéis de controlador Matter e roteador de borda Thread, mas isso
depende do modelo: um HomePod mini ou uma Apple TV 4K com Wi-Fi e Ethernet fazem os dois; uma Apple TV
HD não faz nenhum.

## Os papéis, em palavras simples

- **Controlador Matter:** quem comanda os aparelhos e guarda a lista deles. É o papel do Home
  Assistant, do app Casa, do Google Home ou da Alexa. Um aparelho pode ter vários controladores ao
  mesmo tempo (o padrão chama isso de *multi-admin*).
- **Roteador de borda Thread (Thread border router):** a ponte entre a rede Thread, de baixo consumo,
  e a rede IP da casa. Sem ele, dispositivos Thread conversam só entre si.
- **Malha (mesh):** aparelhos Thread ligados à energia retransmitem mensagens para os de bateria, como
  os roteadores no Zigbee.
- **Código de pareamento:** o QR code ou o número de 11 dígitos na embalagem. Guarde a etiqueta; sem
  ela, parear de novo exige o reset de fábrica.
- **Tecido (fabric):** o conjunto de aparelhos sob um controlador. Compartilhar um dispositivo com
  outra plataforma significa colocá-lo num segundo tecido.

## Zigbee, Thread e Wi-Fi lado a lado

| | Zigbee | Thread | Wi-Fi |
|---|---|---|---|
| **Rádio** | 2,4 GHz (IEEE 802.15.4) | 2,4 GHz (IEEE 802.15.4) | 2,4 ou 5 GHz |
| **Consumo** | Muito baixo; sensores duram anos na bateria. | Muito baixo, igual ao Zigbee. | Alto; só com energia constante. |
| **Malha** | Sim, pelos aparelhos ligados à energia. | Sim, pelos aparelhos ligados à energia. | Não; cada aparelho fala com o roteador. |
| **O que precisa na central** | Coordenador (ZBT-2) + ZHA ou Z2M. | Roteador de borda + controlador Matter. | Só o roteador Wi-Fi da casa. |
| **Fala IP?** | Não; o coordenador traduz. | Sim, IPv6 nativo. | Sim. |
| **Maturidade em 2026** | Enorme catálogo, preços baixos. | Catálogo crescendo; preços maiores. | Muito comum; depende do app ou da nuvem do fabricante, salvo em Matter. |

## O que o Matter facilita

Ajuda aparelhos de marcas diferentes a funcionar em plataformas compatíveis, com o mesmo QR code.
Permite controle local, sem a nuvem do fabricante, e compartilhar o mesmo dispositivo entre
ecossistemas, por exemplo no app Casa da Apple e no Home Assistant ao mesmo tempo, quando os dois
suportam a categoria do aparelho.

## O que ele não garante

O logotipo não garante todos os recursos do app do fabricante em todas as plataformas. As categorias
suportadas e as funções dentro de cada categoria variam: um robô aspirador Matter pode expor só "iniciar
e parar", e uma lâmpada pode perder efeitos exclusivos. Verifique **o modelo, o tipo de rede e a
função que você deseja**, de preferência em relatos de quem usa na mesma plataforma.

Um produto Zigbee não passa a ser Matter só porque você adicionou o Home Assistant. Alguns fabricantes
oferecem pontes, como o hub Philips Hue, que expõe as lâmpadas Zigbee como dispositivos Matter, com
recursos específicos de cada ponte.

## O que o Home Assistant precisa

- **Para Matter (qualquer rede):** a integração **Matter**, que no HAOS instala sozinha o App
  *Matter Server*. O pareamento é feito pelo **app companheiro** no celular, porque o primeiro
  contato com o aparelho usa Bluetooth. A rede precisa de IPv6 habilitado no roteador e de descoberta
  mDNS funcionando; redes segmentadas em VLANs exigem configuração extra.
- **Para Matter sobre Thread, além do item acima:** um roteador de borda. Pode ser um da Apple, do
  Google ou da Amazon já existente na casa, ou o próprio Home Assistant com o App **OpenThread Border
  Router** e um ZBT-1 ou ZBT-2 gravado com firmware Thread. O ZBT-2 roda Zigbee **ou** Thread, nunca
  os dois ao mesmo tempo: na nossa trilha ele fica no Zigbee.
- **Para usar um roteador de borda da Apple ou do Google:** a integração **Thread** do Home Assistant
  recebe as credenciais da rede pelo app companheiro no iPhone ou Android, para que o Home Assistant
  possa parear dispositivos nessa mesma rede Thread.

!!! nota "Uma rede Thread, não várias"
    Cada ecossistema tende a criar a própria rede Thread. Duas redes separadas na mesma casa
    significam duas malhas fracas em vez de uma forte. Antes de parear o primeiro dispositivo Thread,
    decida qual roteador de borda será o principal e compartilhe as credenciais com os demais.

## Como fica o pareamento, na prática

1. Com o aparelho em modo de pareamento, abra o app companheiro do Home Assistant → **Configurações
   → Dispositivos e serviços → Adicionar integração → Matter** e leia o QR code.
2. Para um aparelho que já está no app Casa da Apple, use no app Casa a opção de ativar o modo de
   pareamento ("Ativar modo de emparelhamento", no aparelho) e informe ao Home Assistant o código gerado;
   o aparelho passa a responder às duas plataformas.
3. Dê um nome ao dispositivo e coloque-o numa área, como faria com um Zigbee.

## Preciso disso agora?

Não. **Nossa primeira rede continua sendo Zigbee com ZHA.** Há mais modelos, preços menores e um
caminho de instalação que não depende de Bluetooth, IPv6 nem roteador de borda.

Faz sentido pensar em Matter sobre Thread quando: você já tem um HomePod ou uma Apple TV recente e quer
sensores que apareçam também no app Casa; um fabricante só oferece o produto em Matter; ou quer evitar
depender da nuvem de produtos Wi-Fi. Na [instalação do autor](/minha-instalacao/), duas Apple TV 4K
servem como centrais do HomeKit e as luzes são acionadas também pelo app Casa; o caminho exato dessa
integração ainda não está documentado naquela página.

[Próximo: conecte o ZBT-2 e configure o ZHA](/zbt-dongles/).

Fontes: [Matter no Home Assistant](https://www.home-assistant.io/integrations/matter/),
[Thread no Home Assistant](https://www.home-assistant.io/integrations/thread/),
[OpenThread Border Router](https://github.com/home-assistant/addons/tree/master/openthread_border_router),
[Matter no Google Home](https://support.google.com/googlehome/answer/13127223?hl=pt-BR) e
[Connectivity Standards Alliance](https://csa-iot.org/all-solutions/matter/).
