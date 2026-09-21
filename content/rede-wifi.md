---
title: Wi-Fi, VLANs e a rede que sustenta a casa
slug: rede-wifi
description: Como preparar a rede doméstica para dezenas de dispositivos: canais, SSID de 2,4 GHz, VLAN de IoT, mDNS, IPv6 e acesso remoto seguro.
category: Rede
icon: wifi
order: 9
featured: true
reading: 9 min de leitura
date: 2026-09-21
tags: [Wi-Fi, VLAN, Rede, Segurança, VPN]
---

Nenhuma casa inteligente é melhor que a rede em que ela roda. A maior parte dos problemas atribuídos ao
Home Assistant, ao Zigbee ou ao Matter é, na verdade, problema de rede.

## O básico bem feito

1. **Fixe os canais do Wi-Fi 2,4 GHz** (1, 6 ou 11 — nunca "automático") para conviver bem com o
   [canal do Zigbee](/zigbee/).
2. **Reserve IPs por DHCP** para servidor, dongles em rede, câmeras e o que mais for crítico.
3. **Cabo sempre que possível**: servidor, Apple TV, câmeras e NVR agradecem.
4. **Mantenha um SSID de 2,4 GHz acessível.** Muitos dispositivos IoT (e o comissionamento de vários
   aparelhos Matter) não enxergam redes exclusivas de 5 GHz.

!!! dica "Band steering pode atrapalhar"
    Se o seu sistema mesh unifica 2,4 e 5 GHz num SSID só, crie um SSID temporário exclusivo de 2,4 GHz
    para parear dispositivos teimosos. Depois de conectado, o aparelho costuma funcionar normalmente.

## IPv6 e mDNS: os dois invisíveis

- **Thread e Matter dependem de IPv6 local.** Se você desligou IPv6 "por segurança", sensores Thread
  simplesmente não vão funcionar.
- **mDNS/Bonjour** é como a Apple TV, o HomePod, o Home Assistant e as impressoras se descobrem.
  Recursos como "isolamento de clientes" ou "modo AP isolado" quebram isso silenciosamente.

## Vale a pena separar a IoT em VLAN?

Se você tem um roteador ou switch gerenciável, sim — com uma ressalva importante.

**Ganhos**: câmeras e aparelhos baratos ficam sem acesso à internet e sem acesso aos seus computadores.
Uma falha de segurança num aparelho de 40 reais deixa de ser uma falha na sua rede inteira.

**Custo**: você precisa **liberar mDNS entre as VLANs** (mDNS repeater/Avahi) e criar regras para o Home
Assistant alcançar os dispositivos. Sem isso, a descoberta automática e o HomeKit param de funcionar.

Desenho que costuma funcionar:

| Rede | O que fica nela | Internet? |
|---|---|---|
| **LAN principal** | Macs, iPhones, iPads, Apple TV, Home Assistant | Sim |
| **IoT** | Tomadas, lâmpadas Wi-Fi, TVs, aspiradores | Sim (limitada) |
| **Câmeras** | Câmeras IP, NVR | **Não** |
| **Convidados** | Visitas | Sim, isolada |

!!! atencao "Não comece pela VLAN"
    Monte a casa numa rede só, faça tudo funcionar, e só então segmente — um problema de cada vez.
    Segmentar antes de entender o tráfego transforma qualquer erro num mistério.

## Acesso remoto sem abrir a casa para a internet

**Nunca** redirecione a porta 8123 no roteador. As opções seguras, do mais simples ao mais técnico:

1. **Home Assistant Cloud (Nabu Casa)** — assinatura, funciona em qualquer lugar, dois cliques,
   e ainda resolve Alexa e Google.
2. **Tailscale** (add-on oficial) — VPN ponto a ponto, gratuita para uso pessoal, ótima com iPhone e Mac.
3. **WireGuard** no roteador — máximo controle, exige IP público ou DDNS.
4. **Cloudflare Tunnel** — expõe sem abrir porta; exige atenção redobrada com autenticação.

Qualquer que seja a escolha: **ative a autenticação em duas etapas** no Home Assistant e crie contas
separadas para cada morador, em vez de compartilhar a senha do administrador.

## Quantos dispositivos Wi-Fi a casa aguenta?

Roteadores domésticos comuns começam a sofrer entre 30 e 50 clientes. Sintomas: lentidão que "vem e vai",
aparelhos que somem à noite, latência alta em chamadas de vídeo.

É exatamente por isso que a recomendação recorrente aqui é: **o que puder ser Zigbee ou Thread, não coloque
no Wi-Fi**. Uma casa com 60 dispositivos pode ter apenas 10 no Wi-Fi — o resto vive em malhas próprias, de
baixíssimo consumo, sem tocar no seu roteador.

## Continuidade elétrica

Um nobreak alimentando **roteador + ONT + servidor** mantém a casa (e o acesso remoto) viva durante quedas
curtas. Com a integração NUT, o Home Assistant sabe que está na bateria e pode desligar cargas não
essenciais, enviar notificação e se desligar com segurança antes que a bateria acabe.
