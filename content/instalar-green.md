---
title: Instalar o Home Assistant Green, passo a passo
slug: instalar-green
description: Da tomada ao primeiro sensor Zigbee: Green, primeiro acesso, ZBT-2, ZHA e backup.
category: Instalação guiada
icon: book
order: 3
featured: false
level: basico
reading: 8 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

O **Home Assistant Green já vem com HAOS instalado**. Você não precisa gravar cartão, instalar Windows ou conectar monitor ao Green. Vamos ligar os cabos e terminar pelo navegador de outro computador.

[← Escolher outro equipamento](/instalar-haos/)

## 1. Separe o que vai usar

- Home Assistant Green, a fonte original e cabo Ethernet.
- Uma tomada e uma porta livre no roteador ou switch da casa, com internet.
- Um Mac ou PC com navegador atualizado, na mesma rede.
- ZBT-2 e seu cabo USB, vendidos separadamente, para adicionar Zigbee.
- Um sensor, botão ou lâmpada Zigbee compatível para o primeiro teste.

**Downloads:** nenhum programa é necessário no computador. Tenha à mão o [guia rápido oficial em PDF](https://raw.githubusercontent.com/NabuCasa/support/main/static/docs/green/ha-green_quick-start-guide_v1-0.pdf) e o [manual de primeiros passos](https://support.nabucasa.com/hc/en-us/articles/24737667232413). O [aplicativo oficial para iOS e Android](https://companion.home-assistant.io/) pode ser instalado depois.

## 2. Conecte o cabo de rede

Com o Green ainda desligado, encaixe uma ponta do cabo **Ethernet** na porta de rede do aparelho, até prender. Ligue a outra ponta a uma porta **LAN** do roteador ou a um switch conectado à sua rede. O Green usa cabo de rede; não tem Wi-Fi integrado.

<figure class="install-figure"><a href="/static/img/install/green-ethernet.webp" target="_blank" rel="noopener" aria-label="Ampliar: Ethernet: Green de um lado, roteador ou switch do outro."><img src="/static/img/install/green-ethernet.webp" width="350" height="198" alt="Ethernet: Green de um lado, roteador ou switch do outro." loading="lazy" decoding="async"></a><figcaption>Ethernet: Green de um lado, roteador ou switch do outro. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/24737667232413" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

## 3. Ligue a fonte e aguarde

Conecte a fonte original à tomada e ao Green. Deixe-o em local ventilado e aguarde alguns minutos. O LED amarelo piscando como um batimento indica atividade normal do sistema; a preparação inicial ainda pode continuar no navegador.

<figure class="install-figure"><a href="/static/img/install/green-power.webp" target="_blank" rel="noopener" aria-label="Ampliar: Depois da rede, conecte a alimentação do Green."><img src="/static/img/install/green-power.webp" width="350" height="198" alt="Depois da rede, conecte a alimentação do Green." loading="lazy" decoding="async"></a><figcaption>Depois da rede, conecte a alimentação do Green. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/24737667232413" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

Não há imagem para baixar nem pendrive para preparar. Siga para a tela de boas-vindas.

## 4. Abra a sua casa no navegador

No **outro computador**, conectado à mesma rede da central, abra [http://homeassistant.local:8123](http://homeassistant.local:8123). Esse computador pode usar Wi-Fi; a central fica ligada ao roteador por Ethernet.

1. Aguarde a tela de preparação terminar. O primeiro início baixa componentes e pode demorar, conforme a internet. Mantenha a central ligada.
2. Se aparecer **Criar minha casa inteligente / Create my smart home**, siga por essa opção. Quem já tem um backup pode escolher restaurá-lo.
3. Crie o **usuário administrador e uma senha exclusiva**. É uma conta da sua central, diferente da conta opcional da Nabu Casa.
4. Confira localização, fuso horário e unidades. Autorize compartilhamentos opcionais apenas se desejar.
5. Conclua até chegar ao painel. Dispositivos encontrados automaticamente podem ser configurados depois.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central."><img src="/static/img/ha-guide/onboarding.png" alt="Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

**O endereço não abriu?** Digite-o na barra de endereços, incluindo `http://` e `:8123`. Confira cabos, energia e se o computador está na mesma rede, fora da rede de convidados. No app do roteador, procure o IP atribuído ao Home Assistant e abra `http://IP-DA-CENTRAL:8123`, substituindo pelo número real. Algumas instalações recentes usam a porta padrão: experimente também [http://homeassistant.local](http://homeassistant.local). Não abra portas no roteador para este acesso dentro de casa.

## 5. Conecte o ZBT-2 e ative o ZHA

<figure class="install-figure"><a href="/static/img/install/green-zbt.png" target="_blank" rel="noopener" aria-label="Ampliar: O cabo USB liga o ZBT-2 ao Green. O rádio fica fora da caixa da central."><img src="/static/img/install/green-zbt.png" width="800" height="533" alt="O cabo USB liga o ZBT-2 ao Green. O rádio fica fora da caixa da central." loading="lazy" decoding="async"></a><figcaption>O cabo USB liga o ZBT-2 ao Green. O rádio fica fora da caixa da central. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>


O **ZBT-2** é o rádio USB do Zigbee. **ZHA** é a integração que já vem no Home Assistant para cuidar dessa rede. Não precisa instalar MQTT ou outro App.

1. Com o Home Assistant funcionando, conecte o ZBT-2 a uma porta USB da **central**, usando seu cabo. Não o conecte ao computador usado apenas para abrir o navegador.
2. Deixe o rádio afastado de metal, roteador Wi-Fi e dispositivos USB 3.0, com espaço ao redor da antena.
3. Abra **Configurações → Dispositivos e serviços**. No dispositivo descoberto **Home Assistant Connect ZBT-2**, escolha **Adicionar / Configurar**.
4. Selecione **Usar como adaptador Zigbee** e a **instalação recomendada**. Aguarde as etapas de firmware indicadas na tela, sem desconectar o cabo. O assistente cria a integração ZHA.
5. Se não houver descoberta, use **Adicionar integração** e procure **Home Assistant Connect ZBT-2**. Confira se aparece no hardware da central; siga o [assistente oficial](https://support.nabucasa.com/hc/en-us/articles/29400591254301) para sua versão.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

O ZBT-2 usa **Zigbee ou Thread, um por vez**. Aqui, escolha Zigbee.

## 6. Adicione um sensor ou uma luz

1. Em **Configurações → Dispositivos e serviços → Zigbee Home Automation**, abra **Adicionar dispositivo**.
2. Perto do ZBT-2, coloque seu sensor ou sua lâmpada em pareamento conforme o manual. O tempo de pressionar o botão varia por modelo; aparelhos ligados a outra central podem precisar de redefinição.
3. Espere a descoberta e a configuração terminarem. Dê um nome, como **Sensor da porta**, e escolha o cômodo.
4. Abra o dispositivo e faça um teste: abra a porta ou ligue a luz pela tela. Confira se o estado muda.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee."><img src="/static/img/ha-guide/zha-add.png" alt="Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 7. Faça o primeiro backup e siga em frente

Em **Configurações → Sistema → Backups**, configure backups automáticos. Guarde uma cópia fora da central e o **kit de emergência / chave de criptografia** indicado na interface; você precisa dele para restaurar backups criptografados. A cópia pode ficar no computador, em armazenamento de rede ou no serviço de nuvem escolhido.

Confira as atualizações em **Configurações** e faça um backup antes de aplicá-las. Para desligar ou mexer no hardware, use **Configurações → Sistema → menu de energia → Desligar sistema**, aguarde o encerramento e só então retire a fonte.

**Seu ponto de chegada:** painel acessível, ZHA configurado e o primeiro dispositivo respondendo. Agora, [crie uma automação simples pelas telas](/primeira-automacao/).

Referências desta parte: [primeiro acesso](https://www.home-assistant.io/getting-started/onboarding/), [ZBT-2 e ZHA](https://support.nabucasa.com/hc/en-us/articles/29400591254301), [backups](https://www.home-assistant.io/common-tasks/general/#backups). [Créditos das novas ilustrações](/static/img/install/README.md).



Se precisar de ajuda específica do aparelho, consulte o [suporte oficial do Green](https://support.nabucasa.com/hc/en-us/categories/24638797677853).
