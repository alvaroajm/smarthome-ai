---
title: ZBT-2 e ZHA: conecte seu primeiro dispositivo
slug: zbt-dongles
description: ZBT-1 e ZBT-2 comparados, como conectar o adaptador à central, configurar o ZHA pelas telas e parear a primeira lâmpada ou sensor Zigbee.
category: Passo a passo
icon: book
order: 6
featured: true
level: basico
reading: 8 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

Você precisa do **HAOS funcionando**, de um **Home Assistant Connect ZBT-2** e de uma luz ou sensor Zigbee compatível.

O **ZBT-2 é o rádio USB**. O **ZHA é a integração incluída no Home Assistant** que organiza a rede. Não é necessário instalar um App extra.

## ZBT-1 ou ZBT-2?

Os dois são adaptadores oficiais da equipe do Home Assistant (Nabu Casa) e funcionam com o ZHA. Se você
ainda vai comprar, o ZBT-2 é o atual; se já tem um ZBT-1 (vendido antes como SkyConnect), ele serve
igualmente para esta trilha.

| | ZBT-1 (ex-SkyConnect) | ZBT-2 |
|---|---|---|
| **Chip de rádio** | Silicon Labs EFR32MG21 | Silicon Labs MG24, com um ESP32-S3 para a conexão USB |
| **Antena** | Interna | Externa, articulada, que pode ser apontada |
| **Conector** | USB-A, com extensão incluída | USB-C, com cabo incluído |
| **Protocolos** | Zigbee ou Thread (um por vez) | Zigbee ou Thread (um por vez) |
| **Alcance** | Bom | Melhor, pela antena externa |

Nenhum dos dois executa Zigbee e Thread ao mesmo tempo: o modo multiprotocolo foi descontinuado. Nesta
trilha, o adaptador fica no modo Zigbee.

## 1. Conecte o ZBT-2

Monte a antena conforme o manual e use o cabo USB fornecido para conectá-lo à central. Mantenha-o na vertical, afastado do computador, do roteador e de superfícies metálicas.

!!! dica "Extensão USB e porta USB 2.0"
    Portas e discos USB 3.0 geram interferência na faixa de 2,4 GHz, a mesma do Zigbee. Use o cabo de
    extensão incluído (ou um de 30 cm a 1 m) e, se a central tiver, prefira uma porta USB 2.0, em geral
    a de cor preta. Um adaptador encostado na central costuma ser a causa de pareamentos que falham e de
    sensores que "somem" sem motivo.

### Antes do primeiro pareamento: o canal

O Zigbee e o Wi-Fi dividem a faixa de 2,4 GHz. O ZHA escolhe o canal automaticamente na instalação
recomendada, e para a maioria das casas isso basta. Se o seu roteador usa o canal Wi-Fi 1, os canais
Zigbee 15, 20 ou 25 ficam mais livres; se usa o 11, o canal 15 é a opção segura. Decida isso antes de
parear o primeiro aparelho: trocar o canal depois obriga a parear tudo de novo.

## 2. Abra o dispositivo descoberto

Acesse **Configurações → Dispositivos e serviços**. No cartão do Connect ZBT-2, selecione **Adicionar**.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-discovery.png" target="_blank" rel="noopener" aria-label="Ampliar tela: O Home Assistant detecta o Connect ZBT-2 conectado por USB."><img src="/static/img/ha-guide/zbt-discovery.png" alt="O Home Assistant detecta o Connect ZBT-2 conectado por USB." width="350" height="230" loading="lazy" decoding="async"></a><figcaption>O Home Assistant detecta o Connect ZBT-2 conectado por USB. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 3. Escolha Zigbee e a instalação recomendada

No assistente, selecione **Usar como adaptador Zigbee / Use as Zigbee adapter**. Depois, escolha **Instalação recomendada / Recommended installation**. Essa opção configura o ZHA.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Nesta trilha, escolha Zigbee."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="Nesta trilha, escolha Zigbee." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>Nesta trilha, escolha Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

Siga as solicitações até concluir e atribua o adaptador a um cômodo. Não escolha Thread para esta rede.

## 4. Adicione a primeira luz ou sensor

Em **Configurações → Dispositivos e serviços**, abra **Zigbee Home Automation** e clique em **Adicionar dispositivo**.

Coloque o aparelho em modo de pareamento, seguindo o manual do fabricante. Em lâmpadas, costuma ser
ligar e desligar a energia de cinco a seis vezes; em sensores, segurar o botão de reset por alguns
segundos até o LED piscar. Aguarde a descoberta, dê um nome como “Luz da sala” e escolha o cômodo.

### A ordem certa: roteadores primeiro, bateria depois

Aparelhos ligados à energia (lâmpadas, interruptores de parede, tomadas) são **roteadores**: além de
funcionar, eles retransmitem mensagens e estendem a rede. Aparelhos de bateria (sensores de porta,
movimento, temperatura, botões) são **dispositivos finais**: só conversam com o roteador mais próximo e
não retransmitem nada.

Por isso, pareie primeiro os aparelhos de energia, do cômodo mais próximo do adaptador para o mais
distante, e só depois os de bateria, cada um perto do roteador pelo qual ele vai se comunicar. Um sensor
pareado colado no adaptador e depois levado para a garagem vai cair, porque ele guarda a rota antiga.

Uma casa com três ou quatro roteadores bem distribuídos (uma lâmpada ou tomada Zigbee por cômodo
importante) tem uma rede muito mais estável do que uma com um adaptador potente e dez sensores de
bateria. Na [casa do autor](/minha-instalacao/), os interruptores Zemismart Zigbee nas paredes cumprem
esse papel de roteador, além de controlar as luzes.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Use Adicionar dispositivo para buscar aparelhos em pareamento."><img src="/static/img/ha-guide/zha-add.png" alt="Use Adicionar dispositivo para buscar aparelhos em pareamento." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Adicionar dispositivo para buscar aparelhos em pareamento. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 5. Teste antes de continuar

Abra o dispositivo e use o controle da luz. Se for um sensor de abertura, abra e feche a porta e confira a mudança do estado. Faça esse teste no local onde o aparelho será usado.

<details><summary>O aparelho não apareceu?</summary><p>Confira o modo de pareamento, a bateria e o suporte do modelo no ZHA. Se estava em outra central, siga a redefinição do fabricante. Para o ZBT-2 não detectado, confira cabo, conexão USB e atualizações do Home Assistant; consulte o suporte oficial antes de alterar configurações.</p></details>

## Problemas comuns e o que conferir

| Sintoma | Causa mais provável | O que fazer |
|---|---|---|
| A lâmpada não aparece no pareamento | Ainda está pareada a outra central (hub Hue, app Tuya) ou o reset não foi concluído | Faça o reset de fábrica pelo manual e tente de novo a menos de 3 m do adaptador |
| Pareia, mas aparece como "desconhecido" com poucas funções | Modelo sem suporte completo no ZHA | Procure o modelo exato na comunidade; veja [Zigbee2MQTT ou ZHA](/zigbee2mqtt/) |
| Sensor de bateria some depois de alguns dias | Pareado longe do roteador que usa, ou sem roteadores no caminho | Pareie de novo no local definitivo; acrescente uma lâmpada ou tomada Zigbee no cômodo |
| Vários aparelhos caem ao mesmo tempo | Interferência: adaptador perto de USB 3.0, SSD externo ou roteador Wi-Fi | Extensão USB, porta USB 2.0, afastar do roteador |
| Lâmpada "indisponível" | Alguém desligou o interruptor comum da parede | Deixar o interruptor ligado ou trocar por um interruptor Zigbee |
| Comandos demoram ou falham em horários de pico | Canal Zigbee sobreposto ao Wi-Fi | Conferir o canal do Wi-Fi; mudar o canal Zigbee exige parear tudo de novo |

## Backup da rede Zigbee

O ZHA faz backups automáticos da rede (chaves, canal e identificação do coordenador) e os inclui no
backup do Home Assistant. Isso permite trocar o adaptador por outro do mesmo tipo ou restaurar a central
num novo equipamento sem parear tudo de novo. Depois que a primeira lâmpada funcionar, faça um backup
completo em **Configurações → Sistema → Backups** e guarde uma cópia fora da central.

[Agora crie uma automação pelo editor visual](/primeira-automacao/).

Já usa ZBT-1? Não precisa trocá-lo apenas para seguir os conceitos do guia. Zigbee2MQTT é uma alternativa disponível no [aprofundamento](/zigbee2mqtt/).

Fontes: [assistente oficial do ZBT-2](https://support.nabucasa.com/hc/en-us/articles/29400591254301) e [ZHA](https://www.home-assistant.io/integrations/zha/).
