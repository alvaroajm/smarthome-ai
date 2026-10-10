---
title: Home Assistant, servidores e protocolos: perguntas e respostas
slug: faq
description: Tire dúvidas sobre Home Assistant OS, Raspberry Pi, mini-PC x86, Zigbee, ZHA, Zigbee2MQTT, Thread, Matter, Wi-Fi, backups e automações.
category: FAQ
icon: help
order: 19
section: pagina
reading: 12 min de leitura
date: 2026-09-22
updated: 2026-10-09
tags: [FAQ, Home Assistant, HAOS, Zigbee, Thread, Matter]
level: basico
---

## Home Assistant e Home Assistant OS

### O que é Home Assistant?

É uma plataforma de automação residencial que roda na sua própria central. Reúne dispositivos e serviços em painéis e permite criar regras, como acender uma luz quando um sensor detecta movimento.

### Home Assistant e HAOS são a mesma coisa?

Não. Home Assistant é o software de automação. Home Assistant OS, ou HAOS, é o sistema operacional preparado para executá-lo, com gerenciamento de atualizações, backups e aplicativos adicionais.

### Preciso saber programar?

Não para começar. Você pode adicionar integrações, montar painéis e criar automações pela interface. YAML e programação ajudam em personalizações, mas não são pré-requisitos para a primeira luz ou sensor.

### HAOS ou Home Assistant Container: qual escolher?

HAOS é a opção recomendada para a maioria dos usuários. Container faz sentido para quem já administra Docker e o sistema hospedeiro; serviços como MQTT precisam ser gerenciados separadamente, sem o catálogo de Apps do HAOS.

### O Home Assistant funciona sem internet?

Integrações locais podem continuar funcionando se a central e a rede estiverem ligadas. Serviços que dependem de servidores externos, notificações remotas e acesso de fora da casa podem parar. Confira como cada integração se comunica.

### Preciso pagar uma assinatura?

O Home Assistant é gratuito e de código aberto. Há custos de equipamentos e energia. O Home Assistant Cloud, da Nabu Casa, é opcional e oferece facilidades como acesso remoto e conexão com assistentes de voz.

Fontes: [tipos de instalação](https://www.home-assistant.io/installation/) e [acesso remoto](https://www.home-assistant.io/docs/configuration/remote/). Continue com [o guia do Home Assistant](/home-assistant/).

## Servidores: Green, Raspberry Pi e x86

### O que significa servidor nessa casa inteligente?

É o aparelho que mantém o Home Assistant em execução. Pode ser uma central pronta, uma placa Raspberry Pi ou um computador. Ele coordena as automações; não precisa ser um servidor empresarial.

### Qual é o jeito mais simples de começar?

O Home Assistant Green já vem com HAOS instalado. Conecte rede e energia e siga a configuração inicial. Para dispositivos Zigbee ou um roteador de borda Thread próprio, ainda pode ser necessário adicionar um rádio compatível.

### Posso usar um Raspberry Pi?

Sim. A trilha oficial de HAOS indica Raspberry Pi 4 ou 5 com pelo menos 2 GB de RAM, fonte adequada e Ethernet. Verifique também armazenamento, gabinete e refrigeração antes de montar o conjunto.

### microSD ou SSD: qual usar?

microSD é uma opção oficial de instalação: cartão A2 com pelo menos 32 GB. SSD é uma alternativa, desde que o conjunto e o método de inicialização sejam compatíveis. Em ambos os casos, mantenha backups fora da central.

### O que é um mini-PC x86-64?

É um computador compacto com processador Intel ou AMD de 64 bits. O HAOS tem uma imagem para hardware x86-64 genérico, com inicialização UEFI. A compatibilidade precisa ser conferida para o equipamento escolhido.

### Raspberry Pi ou mini-PC: qual é melhor?

Depende do uso e do que você já possui. Considere o conjunto completo: armazenamento, fonte, consumo, refrigeração e manutenção. Câmeras e processamento de vídeo exigem uma avaliação diferente de sensores e automações simples.

### Instalar HAOS no PC mantém o Windows?

A gravação direta da imagem no disco de destino apaga o conteúdo desse disco. Para manter outro sistema, avalie HAOS em uma máquina virtual, com recursos e acesso ao rádio devidamente configurados.

### A central precisa ficar ligada o tempo todo?

Sim, para executar automações continuamente. Desligá-la interrompe as funções que dependem dela. Use um aparelho adequado para operação contínua e evite que o sistema hospedeiro entre em suspensão.

Fontes: [Green e opções de hardware](https://www.home-assistant.io/faq/what-hardware-do-i-need/), [Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi/), [x86-64](https://www.home-assistant.io/installation/generic-x86-64/) e [máquinas virtuais](https://www.home-assistant.io/installation/alternative/). Veja os guias de [Green](/instalar-green/), [RPi 5](/instalar-raspberry-pi-5/) e [mini-PC](/instalar-mini-pc/).

## Wi-Fi, Ethernet e escolha de protocolos

### Zigbee, Thread, Matter e Wi-Fi são concorrentes diretos?

Não estão todos na mesma camada. Zigbee, Thread e Wi-Fi descrevem formas de comunicação; Matter define como aparelhos e plataformas se entendem sobre redes IP, como Thread, Wi-Fi e Ethernet.

### Preciso escolher um único protocolo para a casa?

Não. O Home Assistant pode reunir dispositivos de protocolos diferentes por meio das integrações apropriadas. Uma lâmpada Wi-Fi pode participar de uma automação com um sensor Zigbee sem que os aparelhos falem diretamente entre si.

### Todo aparelho Wi-Fi funciona no Home Assistant?

Não. Estar no Wi-Fi só informa como ele entra na rede. Verifique a integração do fabricante, o modelo exato, as funções disponíveis e se o controle depende de nuvem ou funciona localmente.

### A central deve usar Wi-Fi ou cabo Ethernet?

Nesta trilha, prefira Ethernet para a central: facilita a instalação e reduz uma dependência sem fio. Isso não obriga os dispositivos da casa a usar cabo. O método disponível depende do hardware e da instalação.

### Wi-Fi pode interferir no Zigbee e no Thread?

Sim, quando usam a faixa de 2,4 GHz. Posicionamento e planejamento dos canais ajudam. Afaste coordenadores de roteadores, USB 3 e SSDs; mudar canais sem planejamento pode causar trabalho de reconexão.

Fontes: [integrações disponíveis](https://www.home-assistant.io/integrations/), [Matter](https://www.home-assistant.io/integrations/matter/) e [alcance e interferência Zigbee](https://www.zigbee2mqtt.io/advanced/zigbee/02_improve_network_range_and_stability.html). Continue com [a rede da casa](/rede-wifi/).

## Zigbee: coordenador, malha e compatibilidade

### O que é Zigbee?

É uma tecnologia sem fio muito usada em lâmpadas, sensores, botões e tomadas. Forma uma rede própria, de baixo consumo, adequada a pequenas mensagens de controle e medição. Não serve para transmitir vídeo de câmeras.

### Preciso de um coordenador Zigbee?

Para formar uma rede Zigbee com ZHA ou Zigbee2MQTT, sim. O coordenador é o rádio que inicia e administra essa rede. Um hub do fabricante pode formar outra rede e expô-la por uma integração própria.

### Qual a diferença entre coordenador, roteador e dispositivo final?

O coordenador administra a rede. Roteadores encaminham mensagens pela malha. Dispositivos finais usam um aparelho pai para se comunicar e geralmente são sensores ou controles a bateria.

### Toda tomada ou lâmpada repete o sinal Zigbee?

Muitos aparelhos alimentados continuamente funcionam como roteadores, mas há exceções. Confira o modelo. Desligar a energia de uma lâmpada roteadora pode afetar outros aparelhos que usam esse caminho.

### Dispositivos de marcas diferentes funcionam juntos?

Frequentemente, mas o logotipo Zigbee não garante todas as funções. Confira o modelo e o suporte no ZHA ou no catálogo do Zigbee2MQTT. Alguns aparelhos precisam de adaptações específicas, chamadas quirks ou converters.

### Um dispositivo pode estar em duas redes Zigbee ao mesmo tempo?

Um dispositivo Zigbee comum pertence a uma rede por vez. Para sair de um hub e entrar em outro coordenador, normalmente precisa de reset e novo pareamento. Isso é diferente do compartilhamento multi-admin do Matter.

### Posso manter o Hue Bridge e usar ZHA ou Z2M?

Sim, como redes separadas. Os aparelhos do Hue Bridge continuam ligados a ele, e os demais podem usar outro coordenador. Planeje canais e use a integração Hue para reunir o controle no Home Assistant.

### LQI baixo significa que o dispositivo está com defeito?

Não isoladamente. LQI é um indicador da qualidade do enlace, não um diagnóstico completo. Observe perdas de mensagens, atrasos, rotas, alimentação e mudanças ao longo do tempo. Evite decidir apenas por um número.

Fontes: [ZHA](https://www.home-assistant.io/integrations/zha/), [rede Zigbee](https://www.zigbee2mqtt.io/guide/configuration/zigbee-network.html), [catálogo Z2M](https://www.zigbee2mqtt.io/supported-devices/) e [integração Hue](https://www.home-assistant.io/integrations/hue/). Continue com [Zigbee na prática](/zigbee/).

## ZHA, Zigbee2MQTT e MQTT

### O que é ZHA?

Zigbee Home Automation é a integração nativa de Zigbee do Home Assistant. Usa um coordenador compatível e reúne o gerenciamento na interface do Home Assistant, sem exigir um servidor MQTT.

### O que é Zigbee2MQTT ou Z2M?

É um serviço que administra a rede Zigbee e troca mensagens com outras aplicações por MQTT. Pode ser integrado ao Home Assistant e possui interface e catálogo próprios de dispositivos.

### ZHA ou Z2M: qual escolher?

Para começar, nossa trilha usa ZHA. Avalie Z2M quando o suporte ao seu modelo ou os recursos oferecidos justificarem os serviços adicionais. Não existe uma escolha universalmente superior para toda rede.

### Posso usar ZHA e Z2M no mesmo coordenador?

Não simultaneamente. O rádio deve ser dedicado a um deles. É possível manter soluções separadas com coordenadores e redes próprios; um aparelho não passa automaticamente de uma rede para a outra.

### O que é MQTT? Preciso dele em toda instalação?

É um protocolo de mensagens com um servidor intermediário, chamado broker. O Z2M precisa dele; ZHA não. Instale MQTT quando uma integração ou dispositivo exigir, em vez de tratá-lo como requisito do Home Assistant.

### Migrar de ZHA para Z2M exige parear tudo novamente?

Planeje a migração como uma mudança de rede e confira o procedimento das versões e adaptadores envolvidos. Não presuma que um backup de uma solução será aceito pela outra. Preserve backups antes de modificar o coordenador.

Fontes: [ZHA](https://www.home-assistant.io/integrations/zha/), [começar com Z2M](https://www.zigbee2mqtt.io/guide/getting-started/), [adaptadores Z2M](https://www.zigbee2mqtt.io/guide/adapters/) e [MQTT](https://www.home-assistant.io/integrations/mqtt/). Veja [quando considerar Z2M](/zigbee2mqtt/) e [diagnóstico de desconexões](/zigbee2mqtt-desconectando/).

## Thread e Matter

### Thread e Matter são a mesma coisa?

Não. Thread é uma rede de baixo consumo baseada em IPv6. Matter é um padrão de comunicação entre aparelhos e plataformas; pode usar Thread, Wi-Fi ou Ethernet.

### O que faz um roteador de borda Thread?

Conecta a malha Thread à rede IP da casa. Não é o coordenador Zigbee nem necessariamente o controlador Matter. Um mesmo produto pode desempenhar vários papéis, dependendo do modelo.

### Preciso de roteador de borda para Matter sobre Wi-Fi?

Não. O roteador de borda Thread só é necessário quando o dispositivo usa Thread. Para Matter sobre Wi-Fi, você precisa da rede Wi-Fi e de um controlador Matter compatível.

### HomePod mini ou Apple TV podem cumprir esse papel?

HomePod mini e determinados modelos de Apple TV têm suporte a Thread. Confira o modelo exato e a configuração; nem toda Apple TV possui rádio Thread. Eles não substituem um coordenador Zigbee.

### Dois roteadores de borda criam automaticamente uma rede Thread única?

Não. Eles podem formar redes distintas, com credenciais diferentes. Para cooperarem na mesma malha, precisam participar da mesma rede Thread. Detectar um roteador de borda no Home Assistant não significa conhecer suas credenciais.

### Um rádio ZBT-2 faz Zigbee e Thread ao mesmo tempo?

Não. O ZBT-2 usa um protocolo por vez. Se precisar de Zigbee e de um roteador de borda Thread próprio, use rádios dedicados ou aproveite um roteador de borda compatível já existente.

### Matter garante todas as funções e torna qualquer Zigbee compatível?

Não. As funções dependem da categoria e do suporte da plataforma. Um Zigbee não vira Matter por estar no Home Assistant; uma ponte Matter específica pode expor funções de dispositivos conectados a ela.

### Posso compartilhar um Matter entre Apple Casa e Home Assistant?

Em dispositivos e plataformas compatíveis, sim, usando multi-admin. Para um aparelho já configurado, gere o código de compartilhamento na plataforma atual e siga o fluxo de dispositivo existente. Não confunda esse código com um reset.

### Matter precisa de IPv6 fornecido pela operadora?

Precisa de IPv6 funcionando na rede local, não de uma conexão de internet IPv6. Multicast e mDNS também são importantes. Redes de convidados, isolamento entre clientes e VLANs mal configuradas podem impedir descoberta e comunicação.

Fontes: [Thread](https://www.home-assistant.io/integrations/thread/), [Matter](https://www.home-assistant.io/integrations/matter/), [ZBT-2](https://www.home-assistant.io/connect/zbt-2/) e [Apple TV: modelos e especificações](https://support.apple.com/en-us/101605). Continue com [Thread e Matter sem confusão](/matter-thread/).

## Integrações, Apps, HACS e ESPHome

### Integração, dispositivo e entidade: qual é a diferença?

Uma integração conecta o Home Assistant a uma tecnologia ou serviço. O dispositivo representa o aparelho. Entidades representam funções ou informações dele: uma tomada pode ter entidades para ligar, medir potência e informar energia.

### Apps e integrações são a mesma coisa?

Não. Apps, antes chamados add-ons, são serviços adicionais instaláveis no HAOS, como um broker MQTT. Integrações conectam serviços e dispositivos ao Home Assistant. Um App pode funcionar junto com uma integração.

### O que é HACS? É obrigatório?

HACS facilita instalar integrações e recursos de interface mantidos pela comunidade. Não é obrigatório nem o catálogo de Apps do HAOS. Confira documentação, manutenção e requisitos de cada projeto antes de instalá-lo.

### O que é ESPHome? Preciso de MQTT para usá-lo?

ESPHome permite criar firmware para microcontroladores compatíveis, como muitos ESP32. A integração pode comunicar diretamente com o Home Assistant pela API nativa. MQTT é uma opção, não uma exigência desse caminho.

### Posso continuar usando Alexa, Google Home e Apple Casa?

Sim, com integrações e configuração apropriadas. HomeKit Bridge pode expor entidades compatíveis ao Apple Casa. Alexa e Google Assistant têm caminhos próprios, incluindo opções pelo Home Assistant Cloud. Primeiro confira o controle pelo painel.

Fontes: [conceitos](https://www.home-assistant.io/getting-started/concepts-terminology/), [Apps](https://www.home-assistant.io/apps/), [HACS](https://www.hacs.xyz/docs/use/), [ESPHome](https://www.home-assistant.io/integrations/esphome/) e [HomeKit Bridge](https://www.home-assistant.io/integrations/homekit/). Continue com [integrações e Apps](/apps-integracoes/).

## Automações, acesso e manutenção

### Minha primeira automação não funcionou. O que verifico?

Teste primeiro a ação no painel. Depois, consulte os rastros da automação: gatilho, condições e ações. Executar ações manualmente pula gatilhos e condições, portanto não prova que a regra completa funciona.

### Posso acessar a casa quando estiver fora?

Sim. Home Assistant Cloud e VPN são caminhos possíveis. Siga a documentação de acesso remoto e proteja as contas. O endereço local da central, sozinho, não oferece acesso pela internet.

### Qual é o backup que realmente importa?

Um backup recente que você consegue restaurar. Mantenha uma cópia fora da central e guarde o kit de emergência ou a chave de recuperação quando houver criptografia. Um arquivo no mesmo disco não protege contra perda desse disco.

### Posso trocar o servidor sem reconstruir toda a casa?

O processo de backup e restauração ajuda a migrar a instalação. Além dos dados, confira rádios, caminhos de dispositivos, credenciais e compatibilidade dos serviços no destino. Reserve tempo para testar os dispositivos após a restauração.

### Um aparelho ficou offline: devo resetá-lo imediatamente?

Não como primeiro passo. Confira alimentação, bateria, serviço responsável e logs. Se vários aparelhos falharam juntos, investigue a central e a rede. Para Z2M, use o [roteiro de diagnóstico](/zigbee2mqtt-desconectando/) antes de apagar o pareamento.

Fontes: [automações](https://www.home-assistant.io/docs/automation/troubleshooting/), [acesso remoto](https://www.home-assistant.io/docs/configuration/remote/) e [backups e restauração](https://www.home-assistant.io/common-tasks/general/).

[Seguir a trilha para iniciantes](/instalacao/) · [Explorar todos os guias](/artigos/).
