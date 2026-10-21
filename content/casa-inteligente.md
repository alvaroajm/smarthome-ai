---
title: O que é uma casa inteligente?
slug: casa-inteligente
description: O que é uma casa inteligente, como Home Assistant, Alexa, Google Home, Apple Home, SmartThings e Tuya se comparam e por onde começar sem gastar à toa.
category: Passo a passo
icon: book
order: 1
featured: true
level: basico
reading: 7 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

Uma **casa inteligente** usa aparelhos conectados para facilitar tarefas. Você pode apagar uma luz pelo celular, pedir uma ação por voz ou deixar uma regra agir automaticamente.

**Controle** é você apertar o botão. **Automação** é a casa agir quando algo acontecer: por exemplo, acender a luz ao anoitecer. Uma casa só é "inteligente" de verdade quando a segunda parte funciona sem ninguém pensar nela.

## As quatro camadas de qualquer casa inteligente

Toda instalação, da mais simples à mais elaborada, tem as mesmas quatro camadas. Entender isso evita comprar peças que não conversam entre si.

| Camada | O que é | Exemplos |
|---|---|---|
| **Dispositivos** | O que mede ou age: lâmpadas, interruptores, sensores, tomadas, fechaduras, câmeras. | Lâmpada Zigbee, sensor de porta, tomada com medição de energia. |
| **Rede ou protocolo** | Como o dispositivo se comunica. | Zigbee, Thread, Wi-Fi, Bluetooth, infravermelho. |
| **Central (hub)** | Quem recebe as informações, guarda as regras e manda os comandos. | Home Assistant, hub Hue, Echo com Zigbee, Apple TV como central do HomeKit. |
| **Interface** | Como você interage. | App no celular, voz, painel na parede, botão físico, automação que age sozinha. |

A central é a peça que define quase tudo: ela decide quais protocolos a casa entende, se as regras rodam
na sua rede ou na nuvem de alguém, e se dispositivos de marcas diferentes podem trabalhar juntos.

## Local ou nuvem: a diferença que mais importa

Um dispositivo **local** conversa com a central dentro da sua casa. Um dispositivo **de nuvem** manda o
comando para o servidor do fabricante, que o devolve para o aparelho, mesmo que os dois estejam na mesma
sala. Na prática:

- **Sem internet**, o local continua funcionando; o de nuvem para.
- **Velocidade**: o local responde em frações de segundo; o de nuvem leva de um a vários segundos.
- **Longevidade**: se o fabricante encerra o serviço, o aparelho de nuvem vira peso de papel. Isso já
  aconteceu com várias marcas.
- **Privacidade**: no local, o que acontece na sua casa não sai dela.

Muitos produtos Wi-Fi baratos são de nuvem. Zigbee, Thread e os produtos Matter são locais por
definição. O Home Assistant permite misturar os dois tipos, mas esta trilha começa pelo local.

## Qual plataforma escolher?

Uma plataforma reúne os controles e as regras. Elas podem coexistir: o Home Assistant pode cuidar das automações e, com a conexão adequada, você continua usando o app Casa ou um assistente de voz.

<div class="platform-choices"><article class="platform-choice platform-featured"><p class="eyebrow">O foco do nosso guia</p><h3>Home Assistant</h3><p>A central que reúne aparelhos e automações de marcas diferentes.</p><dl><dt>Vantagens</dt><dd>Controle local, liberdade de escolha e automações flexíveis.</dd><dt>Limitações</dt><dd>Precisa de uma central ligada, configuração inicial e manutenção.</dd></dl><a class="ext" href="https://www.home-assistant.io/" target="_blank" rel="noopener">Referência oficial</a></article><article class="platform-choice"><p class="eyebrow">Plataforma</p><h3>Alexa</h3><p>O ecossistema da Amazon, conhecido pelos aparelhos Echo e comandos de voz.</p><dl><dt>Vantagens</dt><dd>Prático para voz e rotinas simples com aparelhos compatíveis.</dd><dt>Limitações</dt><dd>Muitas funções dependem da nuvem; rádios e recursos variam entre modelos Echo.</dd></dl><a class="ext" href="https://developer.amazon.com/en-US/docs/alexa/smarthome/wwa-connection-options.html" target="_blank" rel="noopener">Referência oficial</a></article><article class="platform-choice"><p class="eyebrow">Plataforma</p><h3>Google Home</h3><p>O app e o ecossistema do Google para organizar e controlar a casa.</p><dl><dt>Vantagens</dt><dd>Reúne controles, voz e dispositivos Matter compatíveis.</dd><dt>Limitações</dt><dd>Matter exige uma central compatível; acesso remoto e serviços online dependem da internet.</dd></dl><a class="ext" href="https://support.google.com/googlehome/answer/13127223?hl=pt-BR" target="_blank" rel="noopener">Referência oficial</a></article><article class="platform-choice"><p class="eyebrow">Plataforma</p><h3>Apple Home / HomeKit</h3><p>O app Casa integra acessórios compatíveis ao iPhone e à Siri.</p><dl><dt>Vantagens</dt><dd>Boa integração com os aparelhos Apple e automações do app Casa.</dd><dt>Limitações</dt><dd>Acesso remoto e automações precisam de uma central Apple; confira o suporte do acessório.</dd></dl><a class="ext" href="https://support.apple.com/pt-br/102557" target="_blank" rel="noopener">Referência oficial</a></article><article class="platform-choice"><p class="eyebrow">Plataforma</p><h3>Samsung SmartThings</h3><p>Um app para reunir aparelhos Samsung e de outras marcas compatíveis.</p><dl><dt>Vantagens</dt><dd>Rotinas gráficas; algumas podem rodar localmente em uma central compatível.</dd><dt>Limitações</dt><dd>Nem toda rotina é local. Recursos e protocolos dependem dos aparelhos e da central.</dd></dl><a class="ext" href="https://developer.smartthings.com/docs/automations/rules" target="_blank" rel="noopener">Referência oficial</a></article><article class="platform-choice"><p class="eyebrow">Plataforma</p><h3>Tuya / Smart Life</h3><p>Uma plataforma usada por muitas marcas, geralmente pelo app Smart Life.</p><dl><dt>Vantagens</dt><dd>Facilita começar pelo celular e oferece aparelhos de várias categorias.</dd><dt>Limitações</dt><dd>Recursos e qualidade variam por fabricante; muitas funções usam nuvem, embora alguns hubs executem cenas locais.</dd></dl><a class="ext" href="https://developer.tuya.com/en/docs/iot/user-manual-for-tuya-smart-v3177?id=K9obrofrfk4sk" target="_blank" rel="noopener">Referência oficial</a></article></div>

## Por que vamos usar Home Assistant?

Nossa trilha prioriza liberdade de escolha e automações locais. O Home Assistant oferece essa base, mas pede um aparelho ligado e cuidado com atualizações e backups. A compatibilidade depende do modelo e da integração.

**Vamos começar pelo Home Assistant OS, com Zigbee, ZHA e ZBT-2.** Aprenda uma etapa de cada vez; voz, câmeras e recursos extras podem esperar.

As plataformas não se excluem. Na [minha casa](/minha-instalacao/), o Home Assistant é a central, e as
mesmas luzes são acionadas pelo app Casa da Apple e por voz pela Alexa. A diferença é quem guarda as
regras: o Home Assistant.

## O que automatizar primeiro

Automações boas resolvem um incômodo real e são fáceis de desligar se incomodarem. Cinco exemplos
que funcionam para a maioria das casas, em ordem de dificuldade:

1. **Luz ao anoitecer.** Uma lâmpada da sala ou da entrada acende ao pôr do sol e apaga numa hora fixa.
   É a [primeira automação](/primeira-automacao/) desta trilha.
2. **Luz de corredor por movimento.** Um sensor de presença acende uma luz fraca de madrugada e apaga
   dois minutos depois do último movimento.
3. **Aviso de porta aberta.** Um sensor de abertura na porta da geladeira ou do portão envia uma
   notificação ao celular se ficar aberta por mais de cinco minutos.
4. **Desligar tudo ao sair.** Quando o último celular da família sai de casa, luzes e tomadas
   selecionadas desligam.
5. **Clima da sala.** Um sensor de temperatura liga um ventilador ou o ar-condicionado por
   infravermelho quando passa de 28 °C, e desliga abaixo de 25 °C.

Fechaduras, aquecedores e portões merecem ficar para depois, com as proteções descritas nos
[Termos de uso](/termos/#2-instalacoes-eletricas-hardware-e-firmware).

## Quanto custa começar

Com uma central, um adaptador Zigbee e uma lâmpada, dá para aprender tudo o que esta trilha ensina. O
guia [Escolha sua central](/hardware/) compara preços e modelos; o guia de [Zigbee](/zigbee/) explica
por que uma lâmpada ligada à energia vale mais do que um sensor de bateria no começo. O erro mais caro
não é escolher a central errada: é comprar dez dispositivos de nuvem num kit promocional antes de
saber o que a casa precisa.

## Vocabulário mínimo

- **Hub / central:** o aparelho que roda o Home Assistant.
- **Integração:** a conexão do Home Assistant com uma marca, serviço ou protocolo.
- **Dispositivo:** o aparelho físico; **entidade:** cada coisa que ele mede ou controla.
- **Área:** o cômodo onde o dispositivo fica, usado para agrupar e para comandos de voz.
- **Cena:** um conjunto de estados ("filme": luzes a 20%, TV ligada).
- **Automação:** gatilho + condição + ação, que roda sozinha.
- **Coordenador Zigbee:** o rádio USB (ZBT-2) que cria a rede Zigbee da casa.

Continue em [O que é Home Assistant?](/home-assistant/).
