---
title: Zigbee2MQTT ou ZHA: quando considerar a mudança
slug: zigbee2mqtt
description: ZHA e Zigbee2MQTT comparados ponto a ponto — arquitetura, suporte a dispositivos, interface, manutenção — e um roteiro para decidir se vale migrar, como conferir seu modelo e como planejar a troca sem perder a rede.
category: Aprofundamento
icon: book
order: 91
featured: true
level: avancado
reading: 8 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

**O ZHA é a escolha da nossa trilha inicial.** Zigbee2MQTT, ou Z2M, é outra forma de gerenciar a mesma
rede Zigbee e integrá-la ao Home Assistant. Os dois fazem o mesmo trabalho essencial, parear e
controlar luzes, interruptores e sensores, mas chegam lá por caminhos diferentes, e é nesses caminhos
que mora a decisão.

## Como cada um funciona

| | ZHA | Zigbee2MQTT |
|---|---|---|
| **O que é** | Integração incluída no Home Assistant, baseada na biblioteca `zigpy`. | Programa separado (um App no HAOS) que conversa com o adaptador e publica tudo num servidor MQTT. |
| **Peças envolvidas** | Só o Home Assistant e o adaptador. | Zigbee2MQTT + servidor MQTT (App Mosquitto) + integração MQTT no Home Assistant. |
| **Onde você configura** | Configurações → Dispositivos e serviços → ZHA. | Interface própria do Z2M (aba no menu lateral), com um painel completo da rede. |
| **Suporte a dispositivos** | Bom para marcas grandes; modelos "estranhos" dependem de *quirks* (correções mantidas pela comunidade). | Catálogo com milhares de modelos e *converters* adicionados rapidamente pela comunidade, inclusive para muitos aparelhos Tuya. |
| **Atualização de firmware (OTA)** | Disponível para alguns fabricantes, com ajustes na configuração. | Disponível na interface, com índice mantido pelo projeto. |
| **Mapa da rede, grupos e binding** | Existem, dentro das telas do Home Assistant. | Existem, com mapa visual e ferramentas mais detalhadas. |
| **Quem mantém** | Equipe do Home Assistant e comunidade zigpy. | Projeto independente, de código aberto, muito ativo. |
| **Curva de aprendizado** | Menor: tudo acontece no Home Assistant. | Maior: dois serviços extras e a lógica do MQTT para entender. |

Para o iniciante, a diferença prática é esta: com o ZHA você conecta o ZBT-2 e segue as telas; com o
Z2M você instala e mantém dois serviços a mais, em troca de um catálogo maior e de ferramentas de
diagnóstico mais ricas.

## Quando avaliar a mudança

Avalie o Z2M quando um destes sinais aparecer, e não antes:

1. **Um modelo que você precisa não é reconhecido pelo ZHA**, ou aparece com menos funções do que a
   embalagem promete (por exemplo, um sensor de presença que mostra só "movimento", sem distância ou
   sensibilidade).
2. **Aparelhos de uma marca pouco comum** chegam ao catálogo do Z2M meses antes de ganharem *quirk*
   no ZHA. Isso é frequente com dispositivos Tuya de modelo genérico, os famosos `TS0601`, que usam um
   protocolo próprio por cima do Zigbee e precisam de tradução específica para cada variante.
3. **Você quer diagnosticar a rede com mais detalhe**: ver a qualidade de cada enlace, forçar rotas,
   configurar intervalos de relatório de sensores de bateria ou atualizar firmware de vários aparelhos.
4. **Você já usa MQTT** para outros projetos, como sensores com ESPHome ou Tasmota, e prefere
   centralizar tudo nesse padrão.

Se nenhum sinal apareceu, não há ganho em migrar. Uma rede ZHA estável vale mais do que um catálogo
maior que você não vai usar.

## Como conferir o seu modelo antes de decidir

Procure sempre pelo **modelo exato**, não pela marca. O nome está na etiqueta do aparelho, na página
da loja ou, se ele já estiver pareado, na tela do dispositivo no Home Assistant.

- **Zigbee2MQTT:** abra o [catálogo de dispositivos](https://www.zigbee2mqtt.io/supported-devices/) e
  pesquise o modelo. A página mostra quais funções ("exposes") o Z2M entrega: liga/desliga, brilho,
  temperatura de cor, energia, bateria, sensibilidade e assim por diante.
- **ZHA:** não há um catálogo oficial único. Confira se o modelo tem *quirk* no repositório
  [zha-device-handlers](https://github.com/zigpy/zha-device-handlers) e procure relatos no fórum da
  comunidade. Marcas com Zigbee padrão, como Philips Hue, IKEA, Aqara e Sonoff, costumam funcionar
  bem sem *quirk*.

Um exemplo didático: um sensor de presença Tuya `TS0601` de uma variante nova pode entrar no ZHA como
"dispositivo desconhecido", oferecendo apenas uma entidade genérica, enquanto no catálogo do Z2M a
mesma variante lista presença, distância, sensibilidade e iluminância. Esse é o tipo de diferença que
justifica a troca. Se, ao contrário, as duas listas mostram as mesmas funções, fique no ZHA.

## O que o Z2M acrescenta à sua central

1. **Servidor MQTT.** No HAOS, instale o App **Mosquitto broker** e crie um usuário para o Zigbee2MQTT.
2. **Integração MQTT.** Adicione a integração MQTT no Home Assistant apontando para o Mosquitto. É por
   ela que os dispositivos do Z2M aparecerão no painel, pela descoberta automática.
3. **App Zigbee2MQTT.** Instale conforme as
   [instruções oficiais para o Home Assistant](https://www.zigbee2mqtt.io/guide/installation/03_ha_addon.html).
   Na configuração, informe a porta serial do adaptador (prefira o caminho `/dev/serial/by-id/...`,
   que não muda ao reiniciar) e o tipo de adaptador. Para o ZBT-1 e o ZBT-2, que usam chip Silicon
   Labs, o adaptador é `ember`; o ZBT-2 exige a velocidade de 460800, conforme a documentação do
   Home Assistant.
4. **Interface.** Depois de iniciar o App, abra a aba Zigbee2MQTT no menu lateral: é lá que você
   permite o pareamento, renomeia aparelhos, vê o mapa da rede e atualiza firmware.

!!! atencao "Um adaptador, uma solução"
    Não use o mesmo adaptador no ZHA e no Z2M ao mesmo tempo. Desative ou remova a integração ZHA
    antes de iniciar o Z2M com o mesmo dongle. Se quiser testar o Z2M sem desmontar a rede atual, use
    um segundo adaptador: as duas redes podem coexistir, em canais diferentes.

## Planejando a migração

A troca de ZHA para Z2M é, na prática, a criação de uma rede nova. Planeje assim:

1. **Backup completo** do Home Assistant em Configurações → Sistema → Backups, antes de qualquer passo.
2. **Inventário.** Liste cada dispositivo, o cômodo, o nome usado nas automações e se ele é alimentado
   pela rede elétrica (roteador Zigbee) ou por bateria (dispositivo final).
3. **Automações e painéis.** Os identificadores das entidades vão mudar. Anote onde cada entidade é
   usada; depois da migração, renomeie as novas entidades com os mesmos nomes ou corrija as automações.
4. **Ordem de pareamento.** Pareie primeiro os aparelhos ligados à energia (lâmpadas, interruptores,
   tomadas), que estendem a rede, e só depois os de bateria, cada um perto de um roteador já pareado.
5. **Canal.** O Z2M usa por padrão o canal 11; o ZHA costuma escolher 15 ou outro. Se o Wi-Fi do
   roteador estiver nos canais 1 ou 6, prefira os canais Zigbee 15, 20 ou 25 e defina isso antes do
   primeiro pareamento, porque trocar de canal depois obriga a parear tudo de novo.
6. **Um cômodo por vez.** Migre, teste as automações daquele cômodo e só então siga para o próximo.

No sentido contrário, do Z2M para o ZHA, o Home Assistant documenta a importação do arquivo de backup
do coordenador gerado pelo Zigbee2MQTT, o que pode preservar a rede. Do ZHA para o Z2M, conte com
parear os aparelhos novamente.

## O que não muda

Zigbee é Zigbee. Alcance, interferência com Wi-Fi em 2,4 GHz, a necessidade de roteadores na rede e a
regra de manter o adaptador numa extensão USB, longe de portas USB 3.0, valem para os dois. Uma rede
que cai no ZHA por falta de roteadores vai cair igual no Z2M.

## Referências

Se a sua rede já usa Zigbee2MQTT e apresenta falhas, siga o
[roteiro para diagnosticar desconexões](/zigbee2mqtt-desconectando/) antes de migrar ou parear os
aparelhos novamente.

- [Instalação oficial no Home Assistant](https://www.zigbee2mqtt.io/guide/installation/03_ha_addon.html)
- [Catálogo de dispositivos do Zigbee2MQTT](https://www.zigbee2mqtt.io/supported-devices/)
- [Integração ZHA, com requisitos do ZBT-2](https://www.home-assistant.io/integrations/zha/)
- [Integração MQTT](https://www.home-assistant.io/integrations/mqtt/) e o nosso guia de [MQTT](/mqtt/)
- [Voltar ao ZHA com ZBT-2](/zbt-dongles/)
