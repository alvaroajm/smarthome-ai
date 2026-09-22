---
title: Adaptadores ZBT-1 e ZBT-2
slug: zbt-dongles
description: Veja para que servem e o que conferir antes de escolher.
category: Hardware
icon: mesh
order: 7
featured: true
reading: 9 min de leitura
date: 2026-09-21
tags: [ZBT-1, ZBT-2, SkyConnect, Zigbee, Thread, Coordenador]
---

Se você está começando, guarde esta frase: **o Home Assistant não fala Zigbee sozinho**. Ele precisa de um
rádio — um pen drive que serve de "antena" para conversar com sensores, lâmpadas e fechaduras. Esse
aparelhinho se chama **coordenador** (ou dongle), e os oficiais do projeto são o **ZBT-1** e o **ZBT-2**.

## Primeiro: o que esse pen drive faz

Imagine que seus sensores falam um idioma de rádio próprio, o Zigbee. Seu servidor (Raspberry Pi, mini-PC)
só fala Wi-Fi e Ethernet. O dongle é o **tradutor**: ele fica plugado na USB, conversa em Zigbee com os
dispositivos e entrega tudo ao Home Assistant.

Os dongles oficiais fazem esse papel para **dois idiomas diferentes**:

- **Zigbee** — a malha mais comum e barata de sensores ([guia completo](/zigbee/))
- **Thread** — a rede usada pelos dispositivos **Matter over Thread** ([guia completo](/matter-thread/))

!!! atencao "Um idioma de cada vez"
    O dongle roda **ou** Zigbee **ou** Thread — nunca os dois ao mesmo tempo. O modo "multiprotocolo"
    existiu como experimento e foi abandonado por instabilidade. Se você quer as duas redes, a resposta
    honesta é: **dois dongles**, ou um dongle Zigbee + um border router Thread (uma Apple TV ou um HomePod
    já servem).

## ZBT-1 x ZBT-2: a comparação

O **ZBT-1** é o antigo *SkyConnect*, apenas renomeado. O **ZBT-2** é a geração seguinte, lançada no fim de 2025.

| | **ZBT-1** (ex-SkyConnect) | **ZBT-2** |
|---|---|---|
| Chip de rádio | Silicon Labs EFR32MG21 | **Silicon Labs MG24** (mais sensível) |
| Ponte USB | Integrada | ESP32-S3 (atualização mais simples e robusta) |
| Antena | Interna, minúscula | **Externa, omnidirecional** (~16 cm, 4,16 dBi) |
| Velocidade serial | 115200 | **460800** (4× mais rápida) |
| Conector | USB-A | **USB-C**, com cabo de 1,5 m incluído |
| Zigbee 3.0 | Sim | Sim |
| Thread / Matter | Sim | Sim (melhor desempenho) |
| Preço de lançamento | — | US$ 49 / 45 € |
| Manutenção | Precisa abrir com cuidado | Abre sem cola nem clipes, com pinos expostos |

### Qual comprar?

- **Está começando agora?** ZBT-2. A antena externa e o cabo incluso resolvem, de fábrica, o maior problema
  de todo mundo — interferência e alcance.
- **Já tem um ZBT-1 funcionando bem?** Não precisa trocar. Migre só se sofrer com sensores distantes caindo,
  ou se a rede passou de umas 40 peças.
- **Quer Zigbee e Thread?** Compre os dois: ZBT-2 para Zigbee (a rede maior) e o ZBT-1 antigo reaproveitado
  como border router Thread.

Alternativas populares e igualmente boas: **Sonoff ZBDongle-P** (chip TI, amplificado) e **ZBDongle-E**
(Silicon Labs). Os oficiais têm a vantagem do assistente de instalação integrado e das atualizações de
firmware com um clique dentro do Home Assistant.

## Instalação passo a passo (ZBT-2)

1. **Não plugue direto no servidor.** Use o cabo de 1,5 m que vem na caixa — ele existe exatamente para
   afastar o rádio do computador.
2. Plugue o cabo numa porta **USB 2.0**, se houver. Portas USB 3.0 e SSDs NVMe emitem ruído justamente na
   faixa de 2,4 GHz usada pelo Zigbee.
3. Deixe a antena **na vertical**, longe de caixas metálicas, do roteador e da TV.
4. No Home Assistant, vá em *Configurações → Dispositivos e serviços*. O dongle é detectado sozinho e o
   assistente pergunta o que você quer: **Zigbee** ou **Thread**.
5. Escolhendo Zigbee, decida entre [ZHA ou Zigbee2MQTT](/zigbee/). Escolhendo Thread, o assistente instala
   o **OpenThread Border Router**.
6. Confirme a atualização de firmware se ela for oferecida — é um clique e reduz problemas futuros.

Para conferir que o sistema enxergou o aparelho, pelo [terminal](/comandos-haos/):

```bash
ls -l /dev/serial/by-id/
# saída parecida com:
# usb-Nabu_Casa_Home_Assistant_Connect_ZBT-2_...-if00-port0 -> ../../ttyUSB0
ha hardware info | grep -i zbt
```

!!! dica "Use sempre o caminho by-id"
    Configure o software com `/dev/serial/by-id/usb-Nabu_Casa_...` e **nunca** com `/dev/ttyUSB0`. O número
    do `ttyUSB` muda quando você reinicia ou pluga outro aparelho; o `by-id` é fixo para sempre.

## Migrando de um dongle antigo para o novo

Trocar de coordenador **não** significa parear tudo de novo — desde que você faça um backup da rede Zigbee:

1. No **Zigbee2MQTT** ou no **ZHA**, faça o backup do coordenador (ambos oferecem essa função; o Home
   Assistant também traz um assistente de migração).
2. Desligue o Home Assistant, troque o dongle, ligue de novo.
3. Restaure o backup no novo coordenador: ele assume a mesma **chave de rede** e o mesmo **PAN ID**, e os
   dispositivos voltam a se conectar sozinhos.
4. Dê um tempo: sensores a pilha podem levar horas para acordar e reencontrar a rede. Não saia repareando
   tudo no susto.

!!! atencao "O que não se migra"
    Backup de coordenador serve para trocar de hardware, não para trocar de software. Sair do ZHA para o
    Zigbee2MQTT (ou o contrário) continua exigindo parear dispositivo por dispositivo.

## Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| Sensores distantes caem | Dongle colado no gabinete ou em USB 3.0 | Use o cabo de extensão, afaste e deixe a antena vertical |
| Rede lenta ou instável | Canal Zigbee sobreposto ao Wi-Fi | Fixe o Wi-Fi em 1, 6 ou 11 e o Zigbee em 15, 20 ou 25 |
| Só funciona perto do servidor | Falta de roteadores na malha | Espalhe 3 a 5 tomadas inteligentes pela casa |
| Dongle "sumiu" após reiniciar | Uso de `/dev/ttyUSB0` | Troque pelo caminho `by-id` |
| Não aparece no Home Assistant | Cabo USB só de energia | Use o cabo original (dados + energia) |

Com o rádio bem posicionado, o resto é fácil: [Zigbee na prática](/zigbee/) explica como montar a malha, e
[Matter e Thread](/matter-thread/) mostra onde o outro modo do dongle entra.
