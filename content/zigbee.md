---
title: Zigbee: o básico para luzes e sensores
slug: zigbee
description: Nossa primeira rede: local, de baixo consumo e gerenciada pelo ZHA.
category: Passo a passo
icon: book
order: 4
featured: true
level: basico
reading: 6 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

**Zigbee** é uma conexão sem fio usada por sensores, lâmpadas, tomadas e botões. Os aparelhos conversam em uma rede própria; não entram individualmente no seu Wi-Fi.

<div class="zigbee-story"><div class="zigbee-intro"><p>Pense em uma conversa por rádio: o sensor avisa “a porta abriu” e o Home Assistant pode mandar acender uma luz. Zigbee é o padrão usado nessa conversa. Gasta pouca energia e é ótimo para mensagens pequenas — não para transmitir vídeo.</p><p>O Wi-Fi continua servindo ao celular e a outros aparelhos. Os dispositivos Zigbee usam uma rede separada, que pode funcionar sem internet.</p></div>
<div class="zigbee-coordinator"><figure><img src="/static/img/zigbee-guide/zbt-2.webp" width="675" height="450" alt="Home Assistant Connect ZBT-2, com base e antena vertical, sobre uma mesa." loading="lazy" decoding="async"><figcaption><a class="ext" href="https://www.home-assistant.io/connect/zbt-2/" target="_blank" rel="noopener">Foto e produto oficiais ↗</a></figcaption></figure><div><p class="eyebrow">A ponte para o Home Assistant</p><h3>Este é o ZBT-2.</h3><p>É o rádio Zigbee conectado por USB à sua central com HAOS. Como coordenador, ele cria a rede. O ZHA, já incluído no Home Assistant, cuida dos dispositivos pelas telas.</p><p>Você precisa de um coordenador para a rede inteira, não de um para cada sensor. Green, Raspberry Pi e mini-PC podem usar o ZBT-2.</p></div></div>
<h3>Pequenos aparelhos, tarefas bem práticas.</h3><div class="zigbee-products">
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/contact.avif" width="1600" height="1600" alt="SONOFF SNZB-04P — Sensor de porta e janela" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Pilha · dispositivo final</span><h4>Sensor de porta e janela</h4><p>Avisa quando abriu ou fechou.</p><small>SONOFF SNZB-04P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-door-window-sensor-snzb-04p" target="_blank" rel="noopener">Foto e produto oficiais ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/motion.avif" width="1600" height="1600" alt="SONOFF SNZB-03P — Sensor de movimento" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Pilha · dispositivo final</span><h4>Sensor de movimento</h4><p>Percebe movimento para acender a luz.</p><small>SONOFF SNZB-03P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-motion-sensor-snzb-03p" target="_blank" rel="noopener">Foto e produto oficiais ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/button.png" width="1600" height="1600" alt="SONOFF SNZB-01P — Botão / interruptor sem fio" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Pilha · dispositivo final</span><h4>Botão / interruptor sem fio</h4><p>Um toque pode chamar uma cena.</p><small>SONOFF SNZB-01P</small><a class="ext" href="https://sonoff.tech/products/sonoff-zigbee-wireless-switch-snzb-01p" target="_blank" rel="noopener">Foto e produto oficiais ↗</a></figcaption></figure>
<figure class="zigbee-product"><img src="/static/img/zigbee-guide/switch.avif" width="1600" height="1600" alt="SONOFF ZBMINIR2 — Módulo para interruptor" loading="lazy" decoding="async"><figcaption><span class="zigbee-role">Energia contínua · router</span><h4>Módulo para interruptor</h4><p>Controla a luz e também repete o sinal.</p><small>SONOFF ZBMINIR2</small><a class="ext" href="https://sonoff.tech/en-us/products/sonoff-zbmini-extreme-zigbee-smart-switch-zbminir2" target="_blank" rel="noopener">Foto e produto oficiais ↗</a></figcaption></figure>
</div><p class="feature-small">São exemplos: confira as funções do modelo no ZHA. O ZBMINIR2 requer neutro e instalação por eletricista; os sensores e o botão funcionam a pilha.</p>
<figure class="zigbee-mesh"><figcaption><p class="eyebrow">Uma rede simples, dentro de casa</p><h3>Quem conversa com quem?</h3><p>Aparelhos que repetem o sinal ajudam a mensagem a chegar mais longe. Isso forma uma rede em malha.</p></figcaption>
<div class="mesh-hub"><div class="mesh-node mesh-server"><strong>Home Assistant OS</strong><span>ZHA gerencia a rede</span></div><span class="mesh-usb">↔ USB ↔</span><div class="mesh-node mesh-coordinator"><strong>ZBT-2</strong><span>Coordenador · cria a rede</span></div></div>
<div class="mesh-radio-link"><span>Zigbee · comunicação sem fio</span></div>
<div class="mesh-branches">
<div class="mesh-branch"><div class="mesh-node mesh-router"><span class="mesh-kind">Router / repetidor</span><strong>Tomada Zigbee¹</strong><span>Repassa mensagens</span></div><div class="mesh-stem" aria-hidden="true">↕</div><div class="mesh-node mesh-end"><span class="mesh-kind">End device / dispositivo final</span><strong>Sensor de porta</strong><span>Envia “abriu / fechou”</span></div></div>
<div class="mesh-branch"><div class="mesh-node mesh-router"><span class="mesh-kind">Router / repetidor</span><strong>Interruptor ZBMINIR2</strong><span>Controla e repassa mensagens</span></div><div class="mesh-stem" aria-hidden="true">↕</div><div class="mesh-node mesh-end"><span class="mesh-kind">End device / dispositivo final</span><strong>Sensor de movimento</strong><span>Envia “há movimento”</span></div></div>
</div>
<p class="mesh-caption">Os routers também podem trocar mensagens entre si. Um sensor pode se conectar diretamente ao coordenador ou a um router; o desenho mostra apenas um exemplo de caminhos.</p></figure>
<div class="zigbee-roles"><article><h4>Router: ajuda os vizinhos</h4><p>Encaminha mensagens de outros dispositivos. Precisa permanecer energizado; aqui, “router” não é o roteador do Wi-Fi.¹ Nem todo aparelho ligado à tomada repete sinal: confira o modelo.</p></article><article><h4>End device: cuida da sua tarefa</h4><p>Envia e recebe suas próprias informações, sem repassar mensagens dos vizinhos. Sensores e botões a pilha costumam ser dispositivos finais: economizam energia para durar mais.</p></article></div>
<p class="feature-small">Referências: <a class="ext" href="https://www.home-assistant.io/integrations/zha/" target="_blank" rel="noopener">ZHA / Home Assistant</a> · <a href="/static/img/zigbee-guide/README.md">Créditos das fotos</a></p></div>

## Por que vamos começar por ele?

- **Baixo consumo:** combina com sensores pequenos, alimentados por pilha.
- **Muitas opções:** há dispositivos de várias categorias e fabricantes.
- **Controle local:** com ZHA, a comunicação com a central acontece dentro de casa.
- **Rede que pode crescer:** aparelhos compatíveis ligados à energia podem repetir o sinal.

Essas vantagens tornam Zigbee uma boa escolha para nossa primeira luz e nossos primeiros sensores. Preço, qualidade e funções variam por modelo.

## Quais são as limitações?

É necessário um coordenador. Paredes, metal e outros equipamentos de 2,4 GHz podem interferir. Nem toda função de todo fabricante aparece no ZHA: confira o modelo antes da compra.

Um dispositivo Zigbee pertence a uma rede por vez. Se já estava em outra central, normalmente precisa ser colocado em modo de redefinição/pareamento conforme o manual.

## E o Thread?

Thread também é uma rede de baixo consumo e pode formar uma malha. É usada por muitos produtos Matter, mas precisa de um **roteador de borda Thread** para se ligar à rede doméstica.

É útil para dispositivos compatíveis entre ecossistemas. A desvantagem, para quem começa, é mais um requisito para conferir. Zigbee e Thread são redes diferentes; um sensor Zigbee não entra em Thread.

Primeiro, [entenda o que é Matter](/matter-thread/). Depois, [configure ZBT-2 + ZHA pelas telas](/zbt-dongles/).

Existe a alternativa **Zigbee2MQTT**, tratada no [aprofundamento](/aprofundamento/#zigbee2mqtt). Ela não é necessária nesta trilha.

Fontes: [ZHA](https://www.home-assistant.io/integrations/zha/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/) e [Thread](https://www.home-assistant.io/integrations/thread/).
