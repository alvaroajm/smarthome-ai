---
title: Comece aqui: sua primeira casa inteligente
slug: instalacao
description: A trilha completa do zero até uma luz automatizada, sem programar — o que comprar, em que ordem fazer, quanto tempo leva e os erros que mais atrasam iniciantes.
category: Passo a passo
icon: book
order: 0
featured: true
level: basico
reading: 6 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

Comece pequeno: **uma central, um adaptador Zigbee e uma luz compatível** já permitem aprender tudo o que
importa. Um sensor pode entrar depois. Esta página é o mapa da trilha; cada etapa tem seu próprio guia
ilustrado.

## O que você precisa ter em mãos

| Item | Para que serve | Onde escolher |
|---|---|---|
| **Central com Home Assistant OS** | Executa o Home Assistant 24 h por dia. Pode ser um Home Assistant Green, um Raspberry Pi 5 ou um mini-PC. | [Escolha sua central](/hardware/) |
| **Adaptador Zigbee (ZBT-2)** | Cria a rede Zigbee da casa e conversa com luzes e sensores. | [ZBT-1 x ZBT-2](/zbt-dongles/) |
| **Uma lâmpada ou um interruptor Zigbee** | O primeiro dispositivo para testar. Prefira um modelo listado como compatível com ZHA. | [Zigbee: o básico](/zigbee/) |
| **Cabo de rede** | A central deve ficar ligada ao roteador por Ethernet, não por Wi-Fi. | — |
| **Outro computador ou celular** | É nele que você abre o painel do Home Assistant pelo navegador. | — |

Ainda não precisa de câmera, assistente de voz, Thread, Matter, MQTT ou qualquer App extra. Tudo
isso entra depois, quando surgir uma necessidade concreta.

!!! dica "Uma extensão USB curta ajuda o Zigbee"
    Ligue o adaptador Zigbee por um cabo de extensão USB de 30 cm a 1 m, afastado da central e de
    portas USB 3.0. Essas portas geram interferência na faixa de 2,4 GHz, e esse é um dos motivos mais
    comuns para "a lâmpada não pareia". A própria documentação do Home Assistant recomenda a extensão.

## Siga nesta ordem

Cada guia termina com algo funcionando. Os tempos são estimativas para quem está começando, sem contar
a espera por compras.

1. [Entenda o que é uma casa inteligente e conheça as plataformas](/casa-inteligente/) — 10 minutos
   de leitura. Ao final, você sabe por que o Home Assistant é a escolha deste site e o que significa
   "automação local".
2. [Conheça o Home Assistant e sua tela de controle](/home-assistant/) — 15 minutos. Você reconhece
   painel, dispositivos, entidades, áreas e automações antes de instalar qualquer coisa.
3. [Prepare o Home Assistant OS e faça o primeiro acesso](/instalar-haos/) — de 30 minutos (Green)
   a 1 hora (Pi 5 ou mini-PC). Ao final, você abre `http://homeassistant.local:8123`, cria sua conta
   e vê o painel vazio.
4. [Entenda o Zigbee e como ele conecta luzes e sensores](/zigbee/) — 10 minutos. Você entende
   coordenador, roteador e dispositivo final, e por que a lâmpada ligada à energia ajuda a rede.
5. [Veja a diferença entre Thread e Matter](/matter-thread/) — 10 minutos. Serve para ler a embalagem
   certa na loja e não comprar um produto que a sua rede ainda não atende.
6. [Conecte o ZBT-2, configure o ZHA e adicione sua luz](/zbt-dongles/) — 20 minutos. A lâmpada
   aparece no painel e acende pelo celular.
7. [Crie a primeira automação pelo editor visual](/primeira-automacao/) — 20 minutos. A luz acende
   sozinha ao pôr do sol, sem uma linha de código.

## O que você vai usar

- **Home Assistant OS:** o sistema que executa a central e cuida das atualizações, dos backups e da
  loja de Apps. É a instalação recomendada para quem está começando.
- **ZBT-2:** o adaptador USB da própria equipe do Home Assistant para a comunicação Zigbee. Nesta
  trilha ele fica no modo Zigbee; Thread fica para outra etapa.
- **ZHA:** a integração Zigbee incluída no Home Assistant. Não exige MQTT nem App extra.

Não precisa instalar programas no computador além do navegador. Siga as telas, dê nomes simples aos
aparelhos ("Luz da sala", "Sensor do corredor") e teste cada dispositivo antes de acrescentar outro.

## Erros que mais atrasam iniciantes

- **Pôr a central no Wi-Fi.** Use Ethernet. O Wi-Fi na central é possível, mas gera quedas difíceis
  de diagnosticar justamente quando você ainda não sabe diagnosticar nada.
- **Parear a lâmpada longe demais do adaptador.** Para o primeiro pareamento, deixe a lâmpada a
  poucos metros do ZBT-2. Depois ela pode ir para o lugar definitivo.
- **Comprar um pacote de dez lâmpadas antes da primeira funcionar.** Teste com uma. Se o modelo for
  bem suportado, compre mais do mesmo.
- **Lâmpada no interruptor de parede comum.** Se alguém desliga o interruptor, a lâmpada Zigbee some
  da rede. Deixe o interruptor sempre ligado ou troque-o por um interruptor Zigbee, como os
  Zemismart usados na [minha instalação](/minha-instalacao/).
- **Ignorar o nome do modelo.** Antes de comprar, procure o modelo exato (não só a marca) na lista de
  dispositivos do ZHA ou do Zigbee2MQTT. "Compatível com Alexa" na caixa não diz nada sobre Zigbee.
- **Esquecer o backup.** Está no próximo tópico.

## Quando a primeira luz funcionar

Faça um backup em **Configurações → Sistema → Backups**. Guarde uma cópia fora da central (no
computador, num pendrive ou numa nuvem) e anote a chave de criptografia em local seguro: sem ela, o
backup não pode ser restaurado.

Depois, com calma, nesta ordem:

1. **Atualize** o Home Assistant pela tela de Configurações, se houver atualização pendente.
2. **Instale o app companheiro** no celular (iOS ou Android). Ele dá acesso ao painel e cria sensores
   úteis, como a presença em casa, usados em muitas automações.
3. **Adicione um sensor** — porta, movimento ou temperatura — e crie a segunda automação.
4. Explore [integrações, Apps, HACS e câmeras](/apps-integracoes/) conforme surgir uma necessidade.
5. As [instalações alternativas e os assuntos avançados](/aprofundamento/) ficam para o final.

## Dúvidas comuns nesta fase

**Preciso de internet para a casa funcionar?** Não para o que esta trilha monta. Home Assistant,
Zigbee e a automação do pôr do sol funcionam na rede local. Internet é necessária para atualizações,
acesso remoto e serviços de nuvem, como assistentes de voz.

**Posso usar Alexa ou o app Casa da Apple junto?** Sim, mais tarde. O Home Assistant pode expor os
dispositivos para a Alexa pelo [Home Assistant Cloud](/nabu-casa/) e para o app Casa pela
[integração HomeKit](/apple-homekit/). Uso as três formas de controle na minha casa.

**Zigbee ou Wi-Fi para as lâmpadas?** Zigbee, para esta trilha: não ocupa o roteador, forma uma rede
em malha e funciona sem a nuvem do fabricante. Produtos Wi-Fi podem entrar depois, caso a caso.

**E se eu travar?** Consulte as [dúvidas frequentes](/faq/) e, se não resolver, escreva pela página de
[contato](/contato/) informando central, versão, adaptador e o modelo do dispositivo.
