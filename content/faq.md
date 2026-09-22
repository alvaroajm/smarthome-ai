---
title: Dúvidas frequentes sobre casa inteligente
slug: faq
description: Respostas diretas às perguntas que mais aparecem — custo, internet, aluguel, marcas, privacidade, Alexa e por onde começar.
category: FAQ
icon: help
order: 19
section: pagina
reading: 3 min de leitura
date: 2026-09-22
tags: [FAQ, Dúvidas, Iniciantes]
level: basico
---

## Preciso saber programar?

Não para acompanhar esta trilha. A instalação, o pareamento no ZHA e a primeira automação usam botões e menus.

## Do que preciso para começar?

Uma central com HAOS, como o Green ou um Raspberry Pi compatível, um ZBT-2 e uma luz ou um sensor Zigbee compatível com ZHA. Se já tiver aparelhos, confira o suporte antes de comprar.

## Home Assistant e HAOS são a mesma coisa?

Home Assistant é o programa que controla a casa. Home Assistant OS (HAOS) é o sistema que o executa e facilita atualizações, backups e instalação de Apps.

## Funciona sem internet?

Dispositivos e integrações locais podem continuar funcionando. A central e a rede precisam estar ligadas. Serviços de nuvem e acesso de fora da casa dependem de conexão.

## Posso continuar usando Alexa ou Google Home?

Sim. As plataformas podem coexistir. A conexão com o Home Assistant é uma etapa adicional; primeiro, faça a luz funcionar pelo painel.

## ZHA precisa de MQTT ou HACS?

Não. ZHA é uma integração nativa do Home Assistant. Basta um coordenador compatível, como o ZBT-2, para formar a rede Zigbee.

## ZBT-2 usa Zigbee e Thread ao mesmo tempo?

Não. Ele usa um protocolo por vez. Neste guia, escolha Zigbee e a instalação recomendada com ZHA.

## Posso instalar o HAOS em cartão microSD?

Sim. A instalação oficial para Raspberry Pi inclui microSD A2 de pelo menos 32 GB. Use cartão e fonte adequados e mantenha backups fora da central.

## Matter garante todas as funções?

Não. Confira se a categoria e os recursos do modelo são aceitos na plataforma escolhida. Matter sobre Thread também precisa de um roteador de borda Thread.

## Minha primeira automação não funcionou. E agora?

Veja se a luz responde pelo painel. Depois, abra o menu da automação e use Executar ações. Esse teste não avalia o gatilho nem as condições; consulte os rastros para entender uma execução real.

[Seguir a trilha para iniciantes](/instalacao/).

Referências oficiais: [HAOS](https://www.home-assistant.io/installation/raspberrypi/), [ZHA](https://www.home-assistant.io/integrations/zha/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/), [Matter](https://www.home-assistant.io/integrations/matter/) e [automações](https://www.home-assistant.io/docs/automation/troubleshooting/).
