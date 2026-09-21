---
title: Matter e Thread explicados sem marketing
slug: matter-thread
description: O que Matter realmente resolve, a diferença entre Matter over Thread e over Wi-Fi, o que é um border router e como isso funciona com Home Assistant e Apple.
category: Protocolos
icon: thread
order: 8
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [Matter, Thread, Border Router, HomeKit, Interoperabilidade]
---

A confusão começa aqui, então vamos separar de uma vez: **Matter é o idioma, Thread é a estrada.**

- **Matter** é o protocolo de aplicação — o vocabulário comum que define o que é uma lâmpada, uma
  fechadura ou um sensor, para que Apple, Google, Amazon e Home Assistant entendam o mesmo aparelho.
- **Thread** é a rede de rádio de baixo consumo, em malha, parecida com Zigbee na ideia, mas baseada em IPv6.
- **Wi-Fi e Ethernet** também transportam Matter, para aparelhos que já têm energia de sobra.

Portanto: um dispositivo pode ser **Matter over Thread** ou **Matter over Wi-Fi** — e a diferença prática é grande.

## Matter over Thread x Matter over Wi-Fi

| | **Matter over Thread** | **Matter over Wi-Fi** |
|---|---|---|
| Consumo | Baixíssimo — funciona com pilha | Alto — precisa de tomada |
| Precisa de ponte | Sim, um **border router** | Não |
| Malha | Sim, entre dispositivos alimentados | Não |
| Típico | Sensores, fechaduras, botões, válvulas | Tomadas, purificadores, eletrodomésticos |
| Carga na rede Wi-Fi | Nenhuma | Mais um cliente por dispositivo |

!!! dica "Como saber antes de comprar"
    A caixa costuma trazer o logotipo Matter e, em letras menores, "Thread" ou "Wi-Fi". Se for sensor a
    pilha e disser Matter, quase certamente é Thread — e você vai precisar de um border router.

## O que é um border router (e você provavelmente já tem um)

O border router liga a malha Thread à sua rede IP doméstica. Aparelhos que fazem esse papel:

- **Apple TV 4K** (modelos recentes) e **HomePod / HomePod mini**
- **Google Nest Hub (2ª geração)** e **Nest Wifi Pro**
- **Amazon Echo** (vários modelos recentes)
- **Home Assistant Connect ZBT-1 / SkyConnect** com firmware Thread, via add-on **OpenThread Border Router**
- Alguns roteadores e hubs de fabricantes (eero, SmartThings, Aqara)

!!! atencao "Várias redes Thread não se juntam sozinhas"
    Ter uma Apple TV e um Nest Hub pode criar **duas malhas Thread separadas**. O padrão prevê credenciais
    compartilhadas, e a Apple e o Google já trocam chaves em muitos cenários — mas a realidade doméstica ainda
    varia. Sinal de alerta: sensores que caem quando você desliga um aparelho específico.
    Verifique em *Configurações → Dispositivos e serviços → Thread* no Home Assistant, que lista as redes
    visíveis e qual é a preferencial.

## Matter no Home Assistant, passo a passo

1. Instale o add-on **Matter Server** e adicione a integração **Matter**.
2. Garanta um border router Thread na rede (add-on OpenThread com o ZBT-1, ou um aparelho Apple/Google).
3. Comissione o dispositivo pelo **app do Home Assistant no celular** — o comissionamento exige Bluetooth,
   por isso é feito pelo telefone, e não pelo navegador.
4. Aponte a câmera para o **QR code Matter** do produto (guarde esse código: ele é necessário em recomissionamentos).

### Multi-admin: o superpoder do Matter

Um mesmo dispositivo pode ser controlado por **vários ecossistemas ao mesmo tempo**. A fechadura pode estar
na Casa da Apple (para o Face ID e os atalhos do iPhone) e no Home Assistant (para as automações sérias),
sem ponte nenhuma. O caminho é sempre: comissione em um sistema, depois gere um **código de pareamento
adicional** e adicione no segundo.

```text
Home Assistant → Dispositivo Matter → ⋮ → "Compartilhar dispositivo"
→ gera um código de 11 dígitos → use no app Casa (Apple), Google Home, etc.
```

## Requisitos de rede que ninguém avisa

- **IPv6 precisa estar ativo** na sua rede local — Thread é IPv6 nativo. Roteadores com IPv6 desligado
  simplesmente não fazem Matter over Thread funcionar.
- **mDNS/Bonjour** precisa circular. Se você separa dispositivos em VLANs ou usa "isolamento de clientes"
  no Wi-Fi, é necessário liberar mDNS entre as redes.
- **Wi-Fi 2,4 GHz disponível**: muitos dispositivos Matter over Wi-Fi não enxergam redes exclusivas de 5 GHz
  durante o comissionamento. Redes unificadas (mesmo SSID) às vezes atrapalham; um SSID temporário de 2,4 GHz resolve.

## Vale esperar tudo virar Matter?

Não. Recomendação prática para quem está montando a casa hoje:

- **Sensores baratos, em quantidade**: Zigbee. Preço e catálogo ainda ganham.
- **Dispositivos novos que você quer usar em mais de um ecossistema** (fechaduras, persianas, termostatos):
  Matter over Thread.
- **Coisas que precisam de banda** (câmeras, alto-falantes, TVs): Wi-Fi.
- **O que for crítico** (portão, alarme, irrigação): prefira o que funcione **sem internet** e tenha
  acionamento físico de reserva.

Matter amadurece a cada revisão da especificação, incorporando novas categorias de dispositivos. É a aposta
certa para o longo prazo — desde que você não descarte o que já funciona bem.

Continue em [Apple HomeKit](/apple-homekit/) para ver como tudo isso aparece no iPhone.
