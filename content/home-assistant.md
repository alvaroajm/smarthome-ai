---
title: Home Assistant: o cérebro local da sua casa
slug: home-assistant
description: O que é, por que roda local, como se organiza em entidades, dispositivos e áreas, e as decisões que definem se a sua casa será estável ou frustrante.
category: Plataforma
icon: hub
order: 2
featured: true
reading: 11 min de leitura
date: 2026-09-21
tags: [Home Assistant, Automação, Local, YAML]
---

O Home Assistant é um software de código aberto que conversa com **mais de mil marcas** de dispositivos e
coloca todos eles sob o mesmo teto — rodando dentro da sua casa, sem depender da nuvem de ninguém.

## Por que local importa

Uma lâmpada que só acende se o servidor do fabricante na Virgínia responder é um ponto de falha que você
não controla. Com processamento local:

- **Latência**: o interruptor responde em milissegundos, não em "um Mississippi".
- **Disponibilidade**: a internet cair não apaga a sua casa.
- **Longevidade**: quando o fabricante encerrar o app, o aparelho continua funcionando.
- **Privacidade**: dados de presença, rotina e câmeras não saem da sua rede.

!!! nota "Nuvem não é proibida, é opcional"
    Assinar o Home Assistant Cloud (Nabu Casa) é a forma mais simples e segura de ter acesso remoto e
    integração com Alexa e Google — e ainda financia o desenvolvimento do projeto. A diferença é que a nuvem
    vira uma conveniência, não uma dependência.

## O modelo mental: entidade, dispositivo, área

Entender esta hierarquia economiza meses de confusão:

- **Entidade** — a menor unidade de estado. `light.sala`, `sensor.temperatura_quarto`,
  `binary_sensor.porta_frente`. Toda automação fala com entidades.
- **Dispositivo** — o aparelho físico que agrupa várias entidades. Um sensor Zigbee de movimento costuma
  expor movimento, luminosidade, temperatura e bateria: quatro entidades, um dispositivo.
- **Área** e **andar** — onde o dispositivo está. Permite dizer "apague tudo do primeiro andar" sem listar nada.
- **Rótulos (labels)** — marcações transversais: `crítico`, `exterior`, `natal`. Excelentes para automações amplas.

## As peças que você vai usar toda semana

### Integrações
São os "drivers". Instale por *Configurações → Dispositivos e serviços*. Prefira sempre a integração
**local** quando houver duas opções (por exemplo, LocalTuya ou Matter em vez do app do fabricante).

### Add-ons
Programas que rodam ao lado do Home Assistant (apenas no HAOS e no Supervised). Os que quase todo mundo acaba instalando:

| Add-on | Para quê |
|---|---|
| **File editor** ou **Studio Code Server** | Editar YAML pelo navegador |
| **Mosquitto broker** | Servidor MQTT, base do Zigbee2MQTT |
| **Zigbee2MQTT** | Rede Zigbee independente do fabricante |
| **ESPHome Device Builder** | Compilar e atualizar seus ESP32 |
| **Terminal & SSH** | Acesso ao sistema |
| **Samba Backup** | Cópia dos backups para um NAS |

### Helpers
Entidades que você cria sem hardware nenhum: `input_boolean` (modo férias), `input_number` (temperatura alvo),
`timer`, `counter`, `schedule`, grupos e templates. São a cola das automações boas.

### Painéis (dashboards)
O Lovelace monta um painel automático. Quando quiser controlar o layout, a seção **Sections** com cards
condicionais cobre quase tudo; o restante se resolve com cards do [HACS](https://hacs.xyz/) como o
*Mushroom* ou o *Bubble Card*.

## Automação: interface gráfica ou YAML?

As duas produzem o mesmo resultado — a interface gera YAML por baixo. Use o editor visual para aprender e
alterne para "Editar em YAML" quando precisar de condições mais finas. A anatomia é sempre:

```yaml
alias: Sala - clima de cinema
triggers:
  - trigger: state
    entity_id: media_player.apple_tv_sala
    to: "playing"
conditions:
  - condition: sun
    after: sunset
actions:
  - action: scene.turn_on
    target:
      entity_id: scene.cinema
  - action: cover.close_cover
    target:
      entity_id: cover.cortina_sala
mode: single
```

- **triggers** — o que dispara (estado, hora, evento, webhook, NFC, template…)
- **conditions** — o que precisa ser verdade para continuar
- **actions** — o que fazer, incluindo esperas, repetições e `choose` (o "se/senão")
- **mode** — `single`, `restart`, `queued` ou `parallel`, para quando o gatilho repete

!!! dica "Depure com as ferramentas de desenvolvedor"
    *Ferramentas de desenvolvedor → Modelo* avalia templates Jinja ao vivo. *→ Estados* mostra todos os
    atributos de uma entidade. E o **rastro (trace)** de cada automação mostra exatamente em que passo ela parou —
    é o melhor recurso de diagnóstico da plataforma.

## Scripts, cenas e blueprints

- **Cena** — um conjunto de estados finais ("sala em 30%, cortina fechada").
- **Script** — uma sequência de passos reaproveitável, chamada por várias automações.
- **Blueprint** — um modelo de automação parametrizável. A comunidade publica centenas deles; importar um
  blueprint de "luz por movimento com luminosidade" resolve em dois minutos o que levaria uma tarde.

## Voz, IA e agentes

O Home Assistant tem um pipeline de voz próprio (*Assist*), com reconhecimento de fala local (Whisper),
síntese (Piper) e detecção de palavra de ativação. Você também pode ligar um modelo de linguagem como agente
de conversação, mantendo o controle dos dispositivos local e usando a IA só para interpretar o pedido.

Para quem usa Mac e iPhone, há ainda o caminho do **MCP**: o Home Assistant expõe um servidor MCP e um
assistente pode consultar estados e executar serviços de forma estruturada.

## Erros comuns (e caros)

1. **Automatizar antes de nomear.** Renomear 80 entidades depois é penoso.
2. **Depender de Wi-Fi para tudo.** Trinta dispositivos Wi-Fi baratos derrubam roteadores domésticos.
3. **Não ter backup externo.** Um SSD morre em silêncio.
4. **Expor a porta 8123 na internet.** Use Nabu Casa, VPN ou Tailscale.
5. **Atualizar sem ler o que mudou.** As notas de versão avisam sobre mudanças que quebram configurações.

## Próximos passos

- Monte seus próprios sensores com [ESPHome e ESP32](/esphome-esp32/)
- Escolha entre [Zigbee2MQTT e ZHA](/zigbee/)
- Entenda [Matter e Thread](/matter-thread/) antes da próxima compra
- Integre com o [ecossistema Apple](/apple-homekit/)
