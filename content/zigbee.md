---
title: Zigbee na prática: Zigbee2MQTT ou ZHA?
slug: zigbee
description: Como funciona a malha Zigbee, qual coordenador comprar, a diferença real entre Zigbee2MQTT e ZHA e como construir uma rede que não cai.
category: Protocolos
icon: mesh
order: 5
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [Zigbee, Zigbee2MQTT, ZHA, MQTT, Sensores]
---

Zigbee é o cavalo de batalha da casa inteligente: barato, de baixíssimo consumo, com malha própria e
independente do seu Wi-Fi. A maioria dos sensores que você vai comprar nos próximos anos fala Zigbee.

## Como a malha funciona

Existem três papéis na rede:

- **Coordenador** — o dongle USB ligado ao seu servidor. Só existe um; é quem forma a rede.
- **Roteadores** — dispositivos ligados na tomada (lâmpadas, tomadas inteligentes, módulos de relé).
  Cada um repete o sinal e amplia o alcance.
- **Dispositivos finais** — sensores a pilha. Dormem quase o tempo todo e **não repetem** sinal.

!!! nota "A regra que resolve quase tudo"
    Uma rede só de sensores a pilha é uma rede frágil. Coloque de **três a cinco roteadores bem distribuídos**
    (uma tomada inteligente por ambiente, por exemplo) e o alcance e a estabilidade mudam de patamar.

## Escolhendo o coordenador

| Coordenador | Chip | Comentário |
|---|---|---|
| **Home Assistant Connect ZBT-1 / SkyConnect** | Silicon Labs EFR32 | Suporta Zigbee e, com outro firmware, Thread |
| **Sonoff ZBDongle-P** | TI CC2652P | Amplificado, ótimo alcance, muito popular |
| **Sonoff ZBDongle-E** | Silicon Labs EFR32 | Também serve de roteador Thread com firmware alternativo |
| **ConBee III** | — | Boa reputação, muito usado com deCONZ |

Todos funcionam. O que realmente determina o resultado é **onde** você pluga: sempre numa
**extensão USB 2.0**, longe de SSDs NVMe, portas USB 3.0 e do gabinete metálico.

## Zigbee2MQTT x ZHA: a decisão

| | **Zigbee2MQTT (Z2M)** | **ZHA** |
|---|---|---|
| Instalação | Add-on + broker MQTT | Integração nativa, dois cliques |
| Compatibilidade | **Maior** — milhares de modelos, inclusive obscuros | Boa, cresce a cada versão |
| Controle fino | Excelente (interface web, OTA, mapa da rede, converters personalizados) | Bom, mais enxuto |
| Independência | Funciona sem o Home Assistant; publica em MQTT | Acoplado ao Home Assistant |
| Complexidade | Mais peças para manter | Menos peças |

**Escolha ZHA** se você quer o caminho mais curto e usa dispositivos comuns.
**Escolha Zigbee2MQTT** se você gosta de controle, compra dispositivos variados (inclusive Tuya sem marca)
ou quer que a rede Zigbee sobreviva a uma reinstalação do Home Assistant. É a escolha da maioria dos usuários avançados.

!!! atencao "Migrar depois dá trabalho"
    Trocar de Z2M para ZHA (ou o contrário) exige reparear **todos** os dispositivos, um a um, subindo em
    escadas para chegar nas lâmpadas. Decida agora, sem pressa.

## Montando com Zigbee2MQTT

1. Instale o add-on **Mosquitto broker** e crie um usuário MQTT do Home Assistant.
2. Instale o add-on **Zigbee2MQTT**.
3. Descubra a porta do dongle em *Configurações → Sistema → Hardware* (algo como
   `/dev/serial/by-id/usb-...`). **Use sempre o caminho `by-id`**, que não muda ao reiniciar.
4. Ajuste a configuração:

```yaml
mqtt:
  server: mqtt://core-mosquitto:1883
  user: !secret mqtt_user
  password: !secret mqtt_password
serial:
  port: /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus-if00-port0
  adapter: zstack
advanced:
  channel: 20           # evite sobrepor o Wi-Fi
  network_key: GENERATE
  transmit_power: 20
  log_level: warning
frontend:
  port: 8099
homeassistant:
  enabled: true
```

5. Abra a interface web, clique em **Permit join**, aproxime o dispositivo e pareie. Desative o
   "permit join" quando terminar.

## Canais: Zigbee e Wi-Fi brigam pelo mesmo espaço

Ambos usam 2,4 GHz. Combinação que funciona bem:

| Wi-Fi (2,4 GHz) | Zigbee sugerido |
|---|---|
| Canal 1 | 15, 20 ou 25 |
| Canal 6 | 15, 20 ou 25 |
| Canal 11 | 15 ou 20 |

Fixe o canal do Wi-Fi no roteador (nada de "automático") e escolha o canal Zigbee de acordo.
Mudar o canal Zigbee depois exige repareamento na maioria dos casos — acerte no início.

## Diagnóstico: quando um sensor "some"

1. **Veja o mapa da rede** (Z2M tem um; o ZHA também). Procure dispositivos ligados direto ao coordenador
   quando deveriam usar um roteador próximo.
2. **LQI baixo (< 50)** significa sinal ruim: aproxime um roteador.
3. **Lâmpadas de algumas marcas são roteadores ruins** e descartam rotas. Tomadas inteligentes costumam ser
   muito melhores repetidoras.
4. **Pilhas CR2032 genéricas** causam quedas fantasma no frio. Use marcas conhecidas.
5. **Repareie o dispositivo no lugar definitivo**, não na mesa ao lado do servidor.

## Zigbee ainda faz sentido com o Matter chegando?

Faz, e por muito tempo. Zigbee tem catálogo enorme, preços baixos e uma década de maturidade. Matter over
Thread é o futuro para dispositivos novos e multiplataforma, mas as duas redes convivem sem conflito —
inclusive no mesmo servidor, com dongles diferentes.

Continue em [Matter e Thread](/matter-thread/) para entender onde cada um se encaixa.
