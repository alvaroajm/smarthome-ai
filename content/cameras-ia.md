---
level: avancado
title: Câmeras com inteligência artificial
slug: cameras-ia
description: Entenda os alertas e as opções de análise de imagens.
category: Câmeras & vídeo
icon: eye
order: 113
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [Frigate, LLM Vision, IA, Câmeras, Notificações, Ollama]
---

Um alerta de câmera comum diz: *"movimento detectado"*. Um bom sistema diz: *"pessoa detectada no portão"*.
E o estágio atual diz: *"um entregador de uniforme deixou uma caixa ao lado do portão e foi embora"* — com
a foto junto.

A diferença entre os três níveis é o que este guia explica.

## Os três níveis de inteligência

| Nível | Tecnologia | O que você recebe | Custo |
|---|---|---|---|
| **1. Movimento** | Detecção de pixels da própria câmera | "Movimento" (inclusive da árvore) | Zero |
| **2. Objetos** | [Frigate](/scrypted/) com modelo de visão | "Pessoa", "carro", "cachorro", na zona que você desenhou | Zero (roda local) |
| **3. Descrição** | Modelo de linguagem com visão | Uma frase explicando a cena | Centavos por evento, ou zero se local |

O caminho recomendado é **somar**, não substituir: o Frigate filtra (só chama a IA quando há uma pessoa de
verdade) e o modelo descreve. Sem essa filtragem, você vai mandar centenas de imagens por dia para um
modelo e pagar por galhos balançando.

## Nível 2: o Frigate faz o trabalho pesado

O [guia de câmeras](/scrypted/) cobre a instalação. O ponto importante aqui é que o Frigate publica cada
evento no [MQTT](/mqtt/) — `frigate/events` — com rótulo (`person`, `car`), câmera, zona e um link para a
foto. Isso é o gatilho perfeito para o próximo nível.

## Nível 3: LLM Vision, a casa que descreve o que vê

**LLM Vision** é uma integração da comunidade (instalada via HACS) que manda uma imagem — ou um trecho de
vídeo — para um modelo com visão e devolve **texto**. Ela aceita vários provedores:

- **Local**: Ollama com modelos de visão, rodando no seu mini-PC ou Mac mini — sem custo por uso e sem
  imagem saindo de casa
- **Nuvem**: Anthropic, OpenAI, Google — mais precisos, custo por imagem, e as imagens saem da sua rede

Instalação resumida: HACS → adicione o repositório do **LLM Vision** → instale → *Configurações →
Dispositivos e serviços → Adicionar integração → LLM Vision* → escolha o provedor e informe a chave (ou o
endereço do Ollama).

### A automação completa

```yaml
alias: Câmera - descrever pessoa detectada no portão
description: Frigate detecta a pessoa, o modelo descreve a cena e o iPhone recebe tudo
triggers:
  - trigger: mqtt
    topic: frigate/events
conditions:
  - condition: template
    value_template: >
      {{ trigger.payload_json['type'] == 'new'
         and trigger.payload_json['after']['label'] == 'person'
         and trigger.payload_json['after']['camera'] == 'portao' }}
actions:
  - variables:
      evento: "{{ trigger.payload_json['after']['id'] }}"
  - action: llmvision.image_analyzer
    data:
      provider: !secret llmvision_provider
      model: gpt-4o-mini
      message: >
        Descreva em uma frase curta, em português, o que esta pessoa está fazendo.
        Mencione se carrega pacotes, se é entregador e se há veículo.
      image_file: /media/frigate/clips/portao-{{ evento }}.jpg
      max_tokens: 80
      temperature: 0.2
    response_variable: resposta
  - action: notify.mobile_app_iphone
    data:
      title: Movimento no portão
      message: "{{ resposta.response_text }}"
      data:
        image: /api/frigate/notifications/{{ evento }}/snapshot.jpg
        url: /lovelace/cameras
mode: queued
max: 5
```

O resultado no iPhone: a foto, uma frase descrevendo a cena e um toque para abrir o painel de câmeras.

!!! dica "Peça frases curtas e específicas"
    Modelos são prolixos por padrão. Instruções como *"em uma frase"*, *"em português"* e
    *"não descreva o cenário, apenas a ação"* deixam a notificação legível na tela bloqueada. `temperature`
    baixa (0,1–0,3) produz descrições mais consistentes.

## Local ou nuvem?

| | **Local (Ollama)** | **Nuvem (API)** |
|---|---|---|
| Custo por evento | Zero | Frações de centavo — somam com o volume |
| Privacidade | Imagem nunca sai de casa | A imagem vai para um servidor externo |
| Qualidade | Boa, melhorando rápido | Melhor em cenas complexas e em texto na imagem |
| Velocidade | Depende do seu hardware | Alguns segundos |
| Funciona sem internet | **Sim** | Não |
| Hardware | Mini-PC com GPU ou Mac com bastante RAM | Qualquer coisa |

A escolha sensata: **câmeras internas → sempre local**; câmeras externas de entrada → nuvem, se você quiser
o melhor texto e o volume for baixo.

!!! atencao "Controle o gasto antes do primeiro susto"
    Sem filtro do Frigate, uma câmera de rua pode disparar centenas de eventos por dia. Defina zonas,
    exija o rótulo `person`, use `mode: queued` com `max` baixo e configure um **teto de gastos** no painel
    do provedor.

## Além da notificação bonita

- **Resumo diário**: um script que junta os eventos do dia e pede "resuma em cinco linhas o que aconteceu
  na frente de casa hoje".
- **Busca em linguagem natural**: guardando as descrições num `input_text` ou num banco, você passa a
  perguntar ao [Claude via MCP](/claude-mcp/) *"teve entrega ontem de tarde?"*.
- **Automação condicionada**: se a descrição mencionar "entregador", acender a luz da entrada e falar no
  alto-falante *"deixe na portaria, por favor"*.
- **Alarme mais esperto**: só notificar de madrugada se a descrição mencionar pessoa se aproximando —
  gato no muro não acorda ninguém.

## Privacidade: combine antes, não depois

Câmera com IA descrevendo pessoas é um salto grande em relação a gravar vídeo. Duas medidas que evitam
conflitos em casa:

1. **Internas só com processamento local.** É a diferença entre um experimento divertido e mandar a sala de
   casa para um servidor de terceiros.
2. **Automação de privacidade**: desligar a análise quando há moradores em casa — o mesmo padrão sugerido
   no [guia de câmeras](/scrypted/).

## Referências

- [LLM Vision](https://llmvision.org/) e o [repositório no GitHub](https://github.com/valentinfrlch/ha-llmvision)
- [Frigate](https://frigate.video/) — detecção de objetos local
- [Ollama](https://ollama.com/) — modelos locais, inclusive com visão
