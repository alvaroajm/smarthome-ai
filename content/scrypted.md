---
level: avancado
title: Conecte suas câmeras
slug: scrypted
description: Conheça Scrypted, Frigate e as opções do app Casa.
category: Câmeras & vídeo
icon: camera
order: 112
featured: true
reading: 9 min de leitura
date: 2026-09-21
tags: [Scrypted, Frigate, HomeKit Secure Video, RTSP, Câmeras]
---

Câmera é o dispositivo mais sensível da casa — e o que mais tenta te empurrar para uma assinatura em nuvem.
Dá para fazer tudo localmente, com qualidade melhor e sem mensalidade.

## Os três papéis (e por que não competem entre si)

| Ferramenta | Faz o quê | Brilha quando |
|---|---|---|
| **Scrypted** | Ponte universal: pega RTSP/ONVIF de qualquer câmera e entrega para HomeKit, Google, Alexa e Home Assistant | Você quer câmeras no **app Casa** com HomeKit Secure Video |
| **Frigate** | NVR com detecção de objetos por IA local (pessoa, carro, animal) | Você quer **gravação e alertas inteligentes** sem falsos positivos |
| **Home Assistant** | Orquestra: exibe, automatiza, notifica | Sempre |

O arranjo completo: a câmera manda RTSP → Frigate detecta e grava → Home Assistant notifica →
Scrypted publica no HomeKit para ver pelo iPhone e pela Apple TV.

## Escolhendo a câmera certa

Procure, nesta ordem:

1. **RTSP ou ONVIF nativo** — sem isso, você fica refém do app do fabricante.
2. **Dois fluxos (main + sub)** — o fluxo secundário em baixa resolução é o que a IA analisa; o principal é o
   que grava. Isso reduz drasticamente o uso de CPU.
3. **Alimentação PoE** — um cabo só, energia e dados, sem depender do Wi-Fi.
4. **Áudio e H.265** se a sua máquina suportar decodificação por hardware.

!!! atencao "Câmeras sem RTSP"
    Muitas câmeras populares bloqueiam RTSP para forçar a nuvem. Algumas são resgatáveis por plugins do
    Scrypted; outras, não. Verifique antes de comprar, não depois.

## Scrypted: câmeras de qualquer marca no app Casa

O Scrypted roda como add-on do Home Assistant, container Docker ou app no Mac (funciona muito bem num
Mac mini, que tem aceleração de vídeo generosa).

Fluxo típico:

1. Instale o Scrypted e adicione a câmera pelo plugin correspondente (ONVIF, RTSP, Reolink, Unifi, etc.).
2. Ative o plugin **HomeKit** e escolha o modo **HomeKit Secure Video** (HKSV) se você tiver assinatura
   iCloud com espaço — a gravação vai criptografada para a Apple, com detecção de pessoas/animais/veículos.
3. Ative o plugin **Home Assistant** para as mesmas câmeras aparecerem no painel do Home Assistant.
4. Se a CPU sofrer, configure **rebroadcast** e transcodificação por hardware no plugin.

!!! dica "Uma câmera, vários destinos"
    O grande valor do Scrypted é deixar de duplicar conexões: a câmera entrega **um** fluxo ao Scrypted, e ele
    redistribui. Cinco apps puxando RTSP direto da câmera é receita para travamento.

## Frigate: alertas que não mentem

Detecção por movimento gera alerta quando a árvore balança. O Frigate roda um modelo de visão computacional
local e só avisa quando há **pessoa**, **carro** ou **animal** — na área que você desenhou.

```yaml
# frigate.yml (resumo)
mqtt:
  host: core-mosquitto
  user: frigate
  password: senha

cameras:
  portao:
    ffmpeg:
      inputs:
        - path: rtsp://usuario:senha@192.168.1.50:554/sub
          roles: [detect]
        - path: rtsp://usuario:senha@192.168.1.50:554/main
          roles: [record]
    detect:
      width: 640
      height: 480
      fps: 5
    objects:
      track: [person, car, dog]
    zones:
      calcada:
        coordinates: 0,480,640,480,640,300,0,300
    record:
      enabled: true
      retain:
        days: 7
```

Para rodar bem, ajuda muito ter aceleração: **Quick Sync** num mini-PC Intel, uma **Coral TPU** USB ou GPU.
Sem aceleração, limite-se a uma ou duas câmeras em baixa resolução de detecção.

Notificação útil no Home Assistant, com a foto do evento:

```yaml
alias: Alerta - pessoa no portão
triggers:
  - trigger: mqtt
    topic: frigate/events
conditions:
  - condition: template
    value_template: >
      {{ trigger.payload_json['after']['label'] == 'person'
         and trigger.payload_json['after']['camera'] == 'portao' }}
actions:
  - action: notify.mobile_app_iphone
    data:
      title: Movimento no portão
      message: Uma pessoa foi detectada
      data:
        image: /api/frigate/notifications/{{ trigger.payload_json['after']['id'] }}/snapshot.jpg
mode: single
```

## Armazenamento e rede

- **Grave em HDD**, não em SSD NVMe: vídeo é escrita contínua e desgasta memória flash rapidamente.
- Reserve cerca de **30 a 60 GB por câmera por semana** em 1080p com gravação contínua; muito menos se você
  gravar apenas eventos.
- Coloque as câmeras numa **VLAN sem acesso à internet**. É a forma mais simples de garantir que elas não
  "telefonem para casa" — e de continuar vendo tudo localmente.

## Privacidade: o combinado com quem mora na casa

Câmeras internas exigem conversa antes da instalação. Duas medidas que resolvem quase toda tensão:

1. **Automação de privacidade**: as câmeras internas desligam (ou giram) quando alguém está em casa.
2. **Transparência**: qualquer pessoa da casa deve saber onde há câmeras e ter acesso às imagens.

```yaml
alias: Privacidade - desliga câmeras internas quando alguém chega
triggers:
  - trigger: state
    entity_id: group.moradores
    to: "home"
actions:
  - action: switch.turn_off
    target:
      entity_id:
        - switch.camera_sala_deteccao
        - switch.camera_corredor_deteccao
```
