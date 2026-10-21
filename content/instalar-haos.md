---
title: Home Assistant OS: escolha sua instalação
slug: instalar-haos
description: Green, Raspberry Pi 5 ou mini-PC: qual escolher, o que preparar, o que acontece no primeiro acesso, o que fazer quando o endereço não abre e os passos seguintes.
category: Instalação guiada
icon: book
order: 3
featured: true
level: basico
reading: 7 min de leitura
date: 2026-09-22
updated: 2026-10-21
tags: [Home Assistant]
---

O **Home Assistant OS (HAOS)** é o sistema que cuida da central, das atualizações e dos Apps. Escolha **apenas o guia do seu equipamento**: cada um leva da preparação ao primeiro sensor Zigbee funcionando.

## Qual equipamento você vai instalar?

<div class="install-card-grid"><a class="install-card" href="/instalar-green/"><img src="/static/img/hardware/green.webp" width="800" height="533" alt="Home Assistant Green" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">01 / Pronto para conectar</span><h3>Home Assistant Green</h3><span class="install-card-description">Ligue a rede e a energia. Crie sua conta e conecte o ZBT-2, pelas telas.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a><a class="install-card" href="/instalar-raspberry-pi-5/"><img src="/static/img/devices/raspberry-pi-5-case.jpg" width="800" height="535" alt="Raspberry Pi 5 + NVMe" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">02 / Monte sua central</span><h3>Raspberry Pi 5 + NVMe</h3><span class="install-card-description">Escolha placa, case e SSD. Prepare o NVMe no Mac ou PC e instale o HAOS.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a><a class="install-card" href="/instalar-mini-pc/"><img src="/static/img/hardware/n150.webp" width="800" height="800" alt="Mini-PC x86-64" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">03 / Intel ou AMD</span><h3>Mini-PC x86-64</h3><span class="install-card-description">Prepare o pendrive e grave o HAOS no SSD interno, com um passo a passo visual.</span><span class="install-card-cta">Ver instalação passo a passo →</span></span></a></div>

Ainda não comprou? [Compare os equipamentos, fotos e preços](/#hardware-haos).

## Como escolher entre os três

| | Home Assistant Green | Raspberry Pi 5 + NVMe | Mini-PC x86-64 |
|---|---|---|---|
| **Para quem** | Quer ligar e usar, sem gravar nada. | Gosta de montar e quer gastar menos num conjunto compacto. | Quer folga para câmeras, IA local, máquinas virtuais e muitos Apps. |
| **Preparação** | Nenhuma: o HAOS já vem gravado. | Gravar o HAOS no SSD NVMe com o Raspberry Pi Imager, num computador. | Criar um pendrive de instalação e gravar o HAOS no SSD interno. |
| **Desempenho** | Suficiente para Zigbee, automações e alguns Apps. | Bom; o SSD NVMe faz diferença em relação ao cartão microSD. | O maior dos três; sobra para Frigate, Scrypted e modelos de IA. |
| **Consumo e ruído** | Muito baixo, sem ventoinha. | Baixo; a ventoinha do case pode ser audível. | Baixo a médio; a maioria tem ventoinha. |
| **Armazenamento** | eMMC interno de 32 GB. | SSD NVMe que você escolhe. | SSD interno, em geral de 256 GB ou mais. |
| **Backup e troca** | Backup pelo HAOS; o hardware é fechado. | Fácil trocar o SSD ou a placa. | Fácil trocar SSD e memória. |

Na dúvida, o **Green** é a escolha mais segura para quem só quer luzes, sensores e automações; o
**mini-PC** é a escolha de quem já sabe que vai colocar câmeras com análise de imagem. Na
[instalação do autor](/minha-instalacao/) a central é um mini-PC com processador Ryzen 7, justamente
porque a casa tem câmeras e uma tela ESPHome além das luzes.

## Antes de começar, separe

- Um **cabo de rede** até o roteador. A central deve ficar por Ethernet.
- Uma tomada estável. Se houver quedas de energia frequentes, um nobreak pequeno evita corrupção do
  armazenamento.
- **Outro computador** na mesma rede, com navegador atualizado, para gravar o sistema (Pi e mini-PC) e
  para o primeiro acesso.
- Para o Pi e o mini-PC: um **pendrive de 8 GB ou mais**, que será apagado, e o **SSD** de destino,
  que também será apagado.
- O **ZBT-2** e uma **extensão USB** curta, para depois da instalação.

## O que os três caminhos têm em comum?

1. A central fica ligada à energia e à rede por **Ethernet**.
2. Você configura pelo navegador de **outro computador**, na mesma rede, em [http://homeassistant.local:8123](http://homeassistant.local:8123).
3. Cria sua conta e conhece o painel.
4. Conecta o **ZBT-2 à central** e configura o **ZHA pelas telas**.
5. Adiciona uma luz ou um sensor e faz o primeiro backup.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: A mesma interface de primeiro acesso, no Green, Pi ou mini-PC."><img src="/static/img/ha-guide/onboarding.png" alt="A mesma interface de primeiro acesso, no Green, Pi ou mini-PC." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>A mesma interface de primeiro acesso, no Green, Pi ou mini-PC. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

O Green já vem pronto. No Pi e no mini-PC, a gravação apaga a mídia escolhida: confira o destino e guarde seus arquivos antes de começar. Para esta trilha, não precisa de terminal, Proxmox ou máquinas virtuais.

## O que acontece no primeiro acesso

1. Ao ligar pela primeira vez, o HAOS baixa e prepara os componentes do Home Assistant. A tela
   "Preparing Home Assistant" pode levar **até 20 minutos**, conforme a documentação oficial. Não
   desligue a central nesse período.
2. Em seguida aparece a tela de boas-vindas. Crie o **usuário dono** (nome, usuário e senha). Guarde
   a senha: não há recuperação por e-mail.
3. Informe o **nome da casa, a localização, o fuso horário e as unidades**. A localização define o
   horário do pôr do sol usado na primeira automação, então marque o ponto certo no mapa.
4. Decida se compartilha dados de uso anônimos com o projeto. É opcional.
5. O Home Assistant mostra os aparelhos que já descobriu na rede, como TVs, impressoras ou o hub
   Philips Hue. Você pode configurá-los agora ou depois.

## Se o endereço não abrir

- **`homeassistant.local` não resolve.** Alguns roteadores e o Windows mais antigo não entendem esse
  tipo de nome. Abra a página de administração do roteador, procure o aparelho chamado
  `homeassistant` na lista de dispositivos conectados e use o endereço IP dele, por exemplo
  `http://192.168.1.50:8123`.
- **A página carrega sem fim.** Espere os 20 minutos iniciais. Se passar disso, ligue um monitor na
  central (Pi e mini-PC) e veja se aparece o prompt `ha >`; se aparecer, o sistema está no ar e o
  problema é de rede.
- **Erro de certificado ou "conexão não segura".** O primeiro acesso é por `http://`, sem `s`.
  Alguns navegadores forçam `https://`; digite o endereço completo.
- **Sem rede após a gravação no mini-PC.** Confira na BIOS se o computador está iniciando pelo SSD
  interno e não pelo pendrive, e se o cabo de rede está na porta certa.

## Logo depois de instalar

1. **Atualize.** Configurações → Sistema → Atualizações. O HAOS, o Supervisor e o Core atualizam
   separadamente; aplique o que estiver pendente.
2. **Reserve o endereço IP** da central no roteador (reserva DHCP). Assim ele nunca muda, e o app do
   celular e as integrações continuam encontrando a central.
3. **Faça o primeiro backup** em Configurações → Sistema → Backups e guarde a chave de criptografia.
   Ative o backup automático semanal com uma cópia fora da central.
4. **Instale o app companheiro** no celular e faça login com o mesmo usuário.
5. Conecte o **ZBT-2** pela extensão USB e siga o guia de [ZBT-2 com ZHA](/zbt-dongles/).

## O que o HAOS cuida por você

O Home Assistant OS inclui o **Supervisor**, que gerencia atualizações, backups e a **loja de Apps**
(Mosquitto, ESPHome, Matter Server, Studio Code Server e outros). Outras formas de instalação, como
Container ou máquina virtual, existem e estão descritas em [Aprofundamento](/aprofundamento/), mas
transferem essa manutenção para você. Para a primeira casa, o HAOS é o caminho com menos atrito.

Depois da instalação, [entenda melhor a rede Zigbee](/zigbee/) e [crie sua primeira automação](/primeira-automacao/).

Fontes: [instalação oficial](https://www.home-assistant.io/installation/),
[primeiro acesso](https://www.home-assistant.io/getting-started/onboarding/) e
[Home Assistant Green](https://www.home-assistant.io/green/).
