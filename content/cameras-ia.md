---
level: avancado
title: Câmeras com inteligência artificial
slug: cameras-ia
description: Entenda os alertas e as opções de análise de imagens.
category: Câmeras & vídeo
icon: eye
order: 113
featured: true
reading: 5 min de leitura
date: 2026-09-22
tags: [Frigate, LLM Vision, IA, Câmeras, Notificações, Ollama]
---

Uma câmera fica muito mais útil quando participa da casa: mostra a entrada no painel, avisa quando alguém chega e ajuda a acender a luz na hora certa. Comece pelo vídeo ao vivo; adicione inteligência aos poucos.

## Primeiro: ver a imagem

Confira se o modelo tem uma integração compatível. **Reolink**, **Tapo** e algumas câmeras **Intelbras** oferecem caminhos diferentes. Em modelos com suporte, ONVIF ou RTSP permitem acesso ao vídeo pela rede local; isso não garante todas as funções do aplicativo original.

<figure class="feature-figure feature-product"><a href="/static/img/ha-features/reolink.webp" target="_blank" rel="noopener" aria-label="Ampliar: Reolink RLC-810A: exemplo de câmera PoE, que recebe rede e energia pelo cabo."><img src="/static/img/ha-features/reolink.webp" width="800" height="444" alt="Reolink RLC-810A: exemplo de câmera PoE, que recebe rede e energia pelo cabo." loading="lazy" decoding="async"></a><figcaption>Reolink RLC-810A: exemplo de câmera PoE, que recebe rede e energia pelo cabo. · <a class="ext" href="https://reolink.com/product/rlc-810a/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

Adicione a integração em **Configurações → Dispositivos e serviços** e depois uma visualização da câmera ao dashboard. Confirme imagem, estabilidade e acesso antes de pensar em gravação ou IA.

## Depois: gravar e encontrar eventos

**NVR** é o sistema que organiza e grava vídeos de câmeras de rede. O **Frigate** é uma opção com processamento local e integração com o Home Assistant. Ele pode reunir câmeras, gravações e detecções em uma interface própria.

<figure class="feature-figure"><a href="/static/img/ha-features/frigate-live.webp" target="_blank" rel="noopener" aria-label="Ampliar: Tela oficial do Frigate: visão ao vivo de várias câmeras."><img src="/static/img/ha-features/frigate-live.webp" width="1400" height="786" alt="Tela oficial do Frigate: visão ao vivo de várias câmeras." loading="lazy" decoding="async"></a><figcaption>Tela oficial do Frigate: visão ao vivo de várias câmeras. · <a class="ext" href="https://frigate.video/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>
<figure class="feature-figure"><a href="/static/img/ha-features/frigate-review.webp" target="_blank" rel="noopener" aria-label="Ampliar: Tela oficial do Frigate: revisão de alertas e detecções."><img src="/static/img/ha-features/frigate-review.webp" width="1400" height="1236" alt="Tela oficial do Frigate: revisão de alertas e detecções." loading="lazy" decoding="async"></a><figcaption>Tela oficial do Frigate: revisão de alertas e detecções. · <a class="ext" href="https://frigate.video/" target="_blank" rel="noopener">Imagem oficial</a></figcaption></figure>

As imagens acima são exemplos do projeto Frigate. Não são capturas da casa do autor. A aparência e os menus variam conforme a versão.

## Três níveis de inteligência

| Recurso | Para que serve | O que precisa |
|---|---|---|
| Detectar objetos | Diferenciar pessoas, carros e animais, conforme as classes do modelo. | Câmera compatível, detector configurado e processamento adequado. |
| Reconhecer rostos | Comparar uma pessoa detectada com rostos cadastrados. | Biblioteca de rostos e hardware compatível com o recurso. |
| Descrever cenas e ações | Resumir algo como “uma pessoa deixou uma caixa”. | Modelo com visão, local ou em nuvem, configuração e recursos adicionais. |

**Movimento não é reconhecimento.** Uma mudança na imagem pode ser uma sombra. Detectar uma pessoa não revela sua identidade. E uma descrição de ação é uma interpretação do modelo, que pode errar.

## Rostos: um recurso opcional

O Frigate oferece reconhecimento facial local: após detectar uma pessoa, compara o rosto com uma biblioteca cadastrada. A documentação atual exige CPU compatível com AVX/AVX2; o modelo maior pede aceleração adequada. Portanto, esse recurso não deve ser presumido em um Green ou Raspberry Pi.

O recurso é ativado nas configurações de enriquecimento do Frigate. O cadastro, a qualidade da imagem, o ângulo e a iluminação influenciam o resultado. Comece com alertas e confira os eventos; não use reconhecimento como único critério para abrir portas ou desarmar alarmes.

## Ações e cenas descritas por IA

Recursos de IA generativa do Frigate e integrações adicionais podem produzir descrições de eventos. Um modelo local mantém o processamento em seu equipamento. Um provedor em nuvem recebe os dados enviados para análise e pode cobrar pelo uso.

É uma etapa posterior à detecção básica: defina quais câmeras e eventos serão analisados, quais dados podem sair da rede e quanto processamento ou orçamento está disponível. Uma descrição não é prova de intenção nem confirmação infalível do que aconteceu.

## Como isso entra nas automações?

Com a integração e os eventos disponíveis, você escolhe os gatilhos no editor do Home Assistant. Exemplos:

- Pessoa na zona da entrada **e** pouca luz → acender a iluminação externa.
- Carro na garagem → enviar um aviso com imagem.
- Animal detectado no quintal → registrar o evento para consulta.

A detecção pode vir da própria câmera ou de um NVR. O Frigate exige configuração e integração adicionais; não é um recurso que aparece automaticamente ao instalar o HAOS. O [guia oficial de integração](https://docs.frigate.video/integrations/home-assistant/) explica os requisitos.

## Cresça sem sobrecarregar a central

Quantidade de câmeras, resolução, gravação e tipo de IA mudam muito o consumo de disco e processamento. Comece com uma câmera. Para várias gravações e análise pesada, avalie hardware dedicado e armazenamento dimensionado.

[Conhecer as centrais para HAOS](/#hardware-haos) · [Voltar às automações](/primeira-automacao/).

Fontes: [Frigate](https://docs.frigate.video/), [reconhecimento facial](https://docs.frigate.video/configuration/face_recognition/), [descrições de objetos e ações](https://docs.frigate.video/configuration/genai/genai_objects/), [Reolink](https://www.home-assistant.io/integrations/reolink/), [TP-Link/Tapo](https://www.home-assistant.io/integrations/tplink/) e [ONVIF](https://www.home-assistant.io/integrations/onvif/).
