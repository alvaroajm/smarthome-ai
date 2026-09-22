---
title: Thread e Matter, sem confusão
slug: matter-thread
description: Entenda a rede, o padrão e o que conferir na embalagem.
category: Passo a passo
icon: book
order: 5
featured: true
level: basico
reading: 3 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

**Thread é uma rede. Matter é um padrão de comunicação entre aparelhos e plataformas.** Um produto Matter pode usar Thread, Wi-Fi ou Ethernet.

## A diferença em um exemplo

Uma lâmpada pode falar o padrão Matter e usar Wi-Fi para chegar à sua rede. Já um sensor Matter pode usar Thread para economizar energia.

| Na embalagem | O que conferir |
|---|---|
| **Matter sobre Wi-Fi** | Rede Wi-Fi e controlador Matter compatível. |
| **Matter sobre Thread** | Controlador Matter e roteador de borda Thread compatíveis. |
| **Zigbee** | Coordenador Zigbee e suporte do modelo no ZHA. |

Um único equipamento pode cumprir os papéis de controlador Matter e roteador de borda, mas isso depende do modelo.

## O que o Matter facilita?

Ajuda aparelhos de marcas diferentes a funcionar em plataformas compatíveis. Também permite compartilhar dispositivos entre ecossistemas, quando suportado.

## O que ele não garante?

O logotipo não garante todos os recursos do app do fabricante em todas as plataformas. Categorias e funções suportadas variam. Verifique **o modelo, o tipo de rede e a função que você deseja**.

Um produto Zigbee não passa a ser Matter só porque você adicionou o Home Assistant. Alguns fabricantes oferecem pontes, com recursos específicos.

## Preciso disso agora?

Não. **Nossa primeira rede continua sendo Zigbee com ZHA.** O ZBT-2 deve ficar no modo Zigbee; ele não executa Zigbee e Thread ao mesmo tempo.

Se no futuro adicionar Matter sobre Thread, você precisará de uma rede Thread adequada. Vamos cuidar disso apenas quando houver um dispositivo que justifique essa etapa.

[Próximo: conecte o ZBT-2 e configure o ZHA](/zbt-dongles/).

Fontes: [Matter no Home Assistant](https://www.home-assistant.io/integrations/matter/), [Thread](https://www.home-assistant.io/integrations/thread/) e [Matter no Google Home](https://support.google.com/googlehome/answer/13127223?hl=pt-BR).
