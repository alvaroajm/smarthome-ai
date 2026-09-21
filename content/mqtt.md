---
title: MQTT explicado para iniciantes
slug: mqtt
description: O que é um broker, o que são tópicos e payloads, para que servem retain e QoS, e como instalar o Mosquitto no Home Assistant em dez minutos.
category: Protocolos
icon: message
order: 8
featured: true
reading: 11 min de leitura
date: 2026-09-21
tags: [MQTT, Mosquitto, Zigbee2MQTT, ESPHome, Integração]
---

MQTT é o "correio" da casa inteligente. É um protocolo simples, antigo e extremamente confiável, criado para
aparelhos pequenos com pouca memória. Se você usa Zigbee2MQTT, Frigate, Tasmota ou quase qualquer projeto
DIY, você já depende dele — mesmo sem saber.

## A ideia central, sem jargão

Imagine um **quadro de avisos** no corredor do prédio. Qualquer morador pode:

- **pendurar um bilhete** num assunto específico ("Elevador — em manutenção")
- **acompanhar um assunto** e ser avisado toda vez que um bilhete novo aparece ali

Ninguém precisa saber quem é o outro. Quem pendura não conhece quem lê; quem lê não conhece quem pendurou.
Só precisam concordar sobre **o nome do assunto**.

No MQTT:

| Quadro de avisos | MQTT | Exemplo na sua casa |
|---|---|---|
| O quadro em si | **Broker** | Mosquitto, rodando no Home Assistant |
| O assunto | **Tópico** (*topic*) | `zigbee2mqtt/sensor_varanda` |
| O bilhete | **Payload** (mensagem) | `{"temperature": 27.4, "battery": 88}` |
| Quem pendura | **Publisher** | O sensor, via Zigbee2MQTT |
| Quem acompanha | **Subscriber** | O Home Assistant |

Esse desacoplamento é a mágica: você troca o Home Assistant de máquina, ou adiciona um segundo sistema
ouvindo os mesmos sensores, e **nada** precisa ser reconfigurado do lado dos dispositivos.

## Tópicos: o endereço da mensagem

Tópicos são organizados com barras, como pastas, do geral para o específico:

```text
casa/sala/temperatura
casa/sala/umidade
casa/cozinha/temperatura
zigbee2mqtt/porta_frente
frigate/portao/person
```

Ao assinar, dois curingas ajudam:

- `+` substitui **um nível**: `casa/+/temperatura` pega sala **e** cozinha
- `#` substitui **todos os níveis a partir dali**: `casa/#` pega tudo da casa

!!! dica "Convenção que evita bagunça"
    Use minúsculas, sem acentos e sem espaços, e vá do geral para o específico:
    `local/comodo/dispositivo/medida`. Você vai agradecer quando tiver 200 tópicos.

## Retain e QoS — os dois conceitos que confundem todo mundo

### Retain (mensagem retida)

Normalmente, quem chega depois **não vê** o que já foi publicado. Com a flag `retain`, o broker guarda a
**última** mensagem de cada tópico e entrega imediatamente a quem assinar.

É por isso que, ao reiniciar o Home Assistant, a temperatura do sensor aparece na hora, em vez de esperar
meia hora pela próxima leitura. **Estado** (temperatura, ligado/desligado) pede `retain: true`;
**evento** (um botão apertado) não deve ser retido — senão a casa "revive" o clique a cada reinício.

### QoS (qualidade de serviço)

Quanto empenho o broker coloca na entrega:

| QoS | Garantia | Use para |
|---|---|---|
| **0** | Envia e esquece; pode se perder | Leituras frequentes (temperatura a cada minuto) |
| **1** | Entrega ao menos uma vez; pode duplicar | O padrão sensato para quase tudo |
| **2** | Entrega exatamente uma vez; mais lento | Comandos críticos (abrir portão, trancar porta) |

Na dúvida: **QoS 1**.

### LWT — o testamento

O *Last Will and Testament* é uma mensagem que o dispositivo combina com o broker **antecipadamente**:
"se eu cair sem avisar, publique `offline` neste tópico". É assim que o Home Assistant sabe mostrar um
sensor como *indisponível* em vez de exibir para sempre o último valor — que pode ser de três dias atrás.

## Instalando o Mosquitto em dez minutos

O broker recomendado é o **Mosquitto**, disponível como app dentro do Home Assistant.

**1. Crie um usuário só para o MQTT**
Em *Configurações → Pessoas → Usuários*, crie um usuário (por exemplo `mqtt_user`) com uma senha forte.
Não use a sua conta de administrador.

**2. Instale o app**
*Configurações → Apps → Loja de apps → Mosquitto broker → Instalar → Iniciar* (deixe "iniciar no boot" ligado).

**3. Aceite a integração**
O Home Assistant detecta o broker sozinho e mostra "MQTT descoberto". Clique em configurar e confirme.

**4. Teste**
Em *Configurações → Dispositivos e serviços → MQTT → Configurar*, existe uma área para publicar e ouvir.
Assine `#` (tudo) e veja as mensagens aparecerem.

Os dados de conexão que outros programas vão pedir:

```yaml
servidor: core-mosquitto      # de dentro do Home Assistant
porta: 1883
usuario: mqtt_user
senha: (a que você criou)
# de fora (ESP32, computador): use o IP do Home Assistant no lugar de core-mosquitto
```

!!! atencao "Porta 1883 nunca vai para a internet"
    MQTT sem TLS trafega em texto puro. Use apenas dentro da sua rede. Se precisar de acesso externo,
    faça por [VPN](/rede-wifi/) — jamais abrindo a porta no roteador.

## MQTT Discovery: por que os dispositivos aparecem sozinhos

Quando você pareia um sensor no Zigbee2MQTT e ele **surge no Home Assistant já com nome, ícone e unidade**,
o responsável é o *discovery*: o programa publica, num tópico especial, um "cartão de visita" em JSON
descrevendo o dispositivo. O Home Assistant lê e cria a entidade.

Exemplo de um sensor caseiro se apresentando:

```json
{
  "name": "Temperatura da estufa",
  "state_topic": "casa/estufa/temperatura",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "unique_id": "estufa_temp_01",
  "device": { "identifiers": ["estufa_esp32"], "name": "ESP32 da estufa" }
}
```

Publicado (com `retain`) no tópico de configuração correspondente, ele vira uma entidade sem você escrever
uma linha de YAML.

## Quem fala MQTT na sua casa

- **[Zigbee2MQTT](/zigbee/)** — publica tudo que a malha Zigbee reporta
- **[ESPHome](/esphome-esp32/)** — opcional (a API nativa é melhor), útil para falar com outros sistemas
- **Tasmota** — firmware de dispositivos comerciais, MQTT de nascença
- **[Frigate](/scrypted/)** — publica eventos de câmera (`frigate/eventos`)
- **Node-RED, Grafana, scripts em Python** — consomem e publicam com poucas linhas
- **[CasaOS / umbrelOS](/casaos-umbrel/)** — qualquer app do seu home server pode entrar na conversa

## Ferramenta indispensável: o MQTT Explorer

Instale o **MQTT Explorer** no seu computador, aponte para o IP do Home Assistant e veja **a árvore inteira
de tópicos em tempo real**. Em cinco minutos ele explica o que uma hora de tutorial não explica — e é a
primeira coisa a abrir quando algo "não chega".

## Erros comuns de quem está começando

1. **Tópico errado por um caractere.** MQTT diferencia maiúsculas e minúsculas e não avisa quando ninguém
   ouve — a mensagem simplesmente cai no vazio.
2. **Esquecer o `retain` em estados.** O painel fica vazio depois de cada reinício.
3. **Usar `retain` em eventos.** A casa "reencena" comandos antigos ao ligar.
4. **Usar a conta de administrador** como usuário MQTT.
5. **Publicar texto onde o Home Assistant espera JSON** (ou o contrário) — confira com o MQTT Explorer.
6. **Achar que precisa de MQTT para tudo.** Se o ESPHome se conecta pela API nativa e o Zigbee funciona no
   ZHA, você talvez não precise de broker nenhum. Ele entra quando **mais de um programa** precisa dos
   mesmos dados.
