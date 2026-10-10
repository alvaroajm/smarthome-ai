---
title: Zigbee2MQTT desconectando: como encontrar a causa
slug: zigbee2mqtt-desconectando
description: Diferencie falhas de MQTT, coordenador e dispositivos Zigbee. Um roteiro de diagnóstico antes de resetar ou parear sua rede novamente.
category: Diagnóstico
icon: book
order: 92
featured: false
level: avancado
reading: 5 min de leitura
date: 2026-10-09
tags: [Zigbee2MQTT, Zigbee, Home Assistant, MQTT]
---

**“Desconectado” pode significar problemas em três lugares diferentes:** no serviço Zigbee2MQTT, na conexão com o servidor MQTT ou em um aparelho da rede Zigbee. Descobrir qual deles falhou evita trocar uma configuração que estava funcionando.

Este roteiro usa a documentação oficial do projeto. Ele não representa um teste de todos os modelos de dispositivos.

## 1. Descubra o tamanho da falha

| O que você observa | Primeira verificação |
|---|---|
| O Zigbee2MQTT não inicia ou reinicia | Leia o log de inicialização e confira o acesso ao coordenador. |
| Os aparelhos respondem na interface do Zigbee2MQTT, mas não no Home Assistant | Confira a conexão MQTT e a integração no Home Assistant. |
| Só um aparelho deixa de responder | Confira alimentação, bateria e as instruções do modelo exato. |
| Vários aparelhos falham depois de mover ou desligar uma tomada/lâmpada | Investigue a mudança de rotas na malha. |

Antes de alterar algo, anote o horário, os modelos afetados e o que mudou recentemente. Faça um teste manual no aparelho e na interface do Zigbee2MQTT para separar uma falha de automação de uma falha de comunicação.

## 2. Se o serviço não inicia, confira o coordenador

Um erro de descoberta do adaptador é diferente de um sensor com bateria fraca. Verifique o cabo, a alimentação, a porta configurada e o tipo de adaptador exigido pelo seu modelo. A documentação de [configuração do adaptador](https://www.zigbee2mqtt.io/guide/configuration/adapter-settings.html) explica como identificar a porta.

O coordenador deve estar dedicado àquela rede: ZHA e Zigbee2MQTT não podem usar o mesmo rádio ao mesmo tempo. Se o log apontar outro erro, consulte o [guia de falhas na inicialização](https://www.zigbee2mqtt.io/guide/installation/20_zigbee2mqtt-fails-to-start_crashes-runtime.html) antes de apagar dados ou atualizar firmware.

## 3. Se o problema está no MQTT, confira essa conexão

O Zigbee2MQTT depende de um servidor MQTT. Confira se ele está disponível e se endereço e autenticação correspondem à configuração. Leia os logs dos dois serviços no mesmo horário; uma mensagem de falha de conexão não comprova defeito no rádio Zigbee.

Veja as [configurações MQTT oficiais](https://www.zigbee2mqtt.io/guide/configuration/mqtt.html). Não publique senhas nem arquivos de configuração completos ao pedir ajuda.

## 4. Se um dispositivo aparece offline, entenda o critério

A opção de disponibilidade é desativada por padrão. Quando habilitada, diferencia aparelhos alimentados pela rede elétrica de aparelhos a bateria. Nos valores padrão documentados, os primeiros são verificados após dez minutos sem comunicação; os segundos podem ficar até 25 horas sem comunicação antes de serem marcados offline.

Esses tempos podem ser personalizados. Um sensor silencioso não deve ser julgado pelo mesmo intervalo de uma tomada. Após reiniciar o Zigbee2MQTT, aparelhos também podem aparecer offline até voltarem a comunicar.

Confira a [documentação de disponibilidade](https://www.zigbee2mqtt.io/guide/configuration/device-availability.html) e a página do seu dispositivo no [catálogo oficial](https://www.zigbee2mqtt.io/supported-devices/). Teste uma ação prevista pelo fabricante, como abrir a porta monitorada pelo sensor.

## 5. Se a rede está instável, comece pelo posicionamento

Para coordenadores USB, use uma extensão para afastar o rádio do computador, SSD e roteador Wi-Fi. O projeto cita uma extensão de 50 cm como medida que já pode reduzir interferência e sugere avaliar uma porta USB 2 em vez de USB 3.

Observe também a alimentação dos roteadores Zigbee. Aparelhos que fazem parte da malha precisam permanecer ligados; confirme a função do modelo no catálogo. Aumentar apenas a potência do coordenador não garante que a resposta do sensor consiga retornar.

Alterar o canal Zigbee pode exigir novo pareamento de alguns dispositivos. Primeiro teste o posicionamento, registre o resultado e consulte o [guia oficial de alcance e estabilidade](https://www.zigbee2mqtt.io/advanced/zigbee/02_improve_network_range_and_stability.html).

## 6. Mudou a malha? Dê tempo para ela se reorganizar

Mover, remover ou parear novamente um roteador pode causar erros de rota e respostas lentas temporárias. A documentação recomenda deixar a rede se estabilizar antes de realizar novas mudanças; isso pode levar de minutos a algumas horas.

Faça uma alteração por vez. Antes de qualquer migração ou reset, preserve os backups e siga o procedimento específico do adaptador. Consulte o [roteiro de troubleshooting](https://www.zigbee2mqtt.io/guide/usage/troubleshooting.html).

## O que registrar para pedir ajuda

- Modelo do coordenador e versão do Zigbee2MQTT.
- Modelo exato e tipo de alimentação dos aparelhos afetados.
- Horário da falha e trecho do log correspondente, sem credenciais.
- Se o comando funciona no Zigbee2MQTT e se funciona no Home Assistant.
- Mudança recente de posição, alimentação, firmware ou configuração.

Continue com [Zigbee2MQTT ou ZHA](/zigbee/) e [como funciona o MQTT](/mqtt/).
