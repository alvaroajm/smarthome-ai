---
title: Instalar HAOS no Raspberry Pi 5 com SSD NVMe
slug: instalar-raspberry-pi-5
description: Peças, case, HAT, preparo do boot e gravação do HAOS no NVMe pelo Mac ou PC.
category: Instalação guiada
icon: book
order: 3
featured: false
level: basico
reading: 15 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Vamos montar um **Raspberry Pi 5 de 8 GB com SSD NVMe** e instalar o Home Assistant OS diretamente no SSD. O Mac ou PC prepara a mídia; depois, o Pi funciona sozinho como central.

O caminho abaixo usa **M.2 HAT+ oficial**, com detecção automática. A preparação de inicialização é feita pelo Raspberry Pi Imager, sem terminal. O cartão microSD será usado só nessa preparação, não como disco permanente.

[← Escolher outro equipamento](/instalar-haos/)

## 1. Escolha peças que encaixam entre si

| Peça | O que escolher |
|---|---|
| Placa | Raspberry Pi 5, preferencialmente 8 GB para esta montagem. |
| Fonte | Fonte oficial USB-C de 27 W para o Pi 5, ou equivalente expressamente compatível. Carregador de celular pode não oferecer a alimentação necessária. |
| SSD | **M.2 NVMe**, de 500/512 GB ou 1 TB; confirme o tamanho físico aceito pelo adaptador. M.2 SATA é outro tipo de SSD. |
| Adaptador | M.2 HAT+ é a placa que conecta o SSD ao pequeno conector PCIe do Pi 5. Não é um hub USB. |
| Case e refrigeração | Um conjunto compatível com o Pi 5, o HAT e o SSD escolhidos. Veja as opções abaixo. |
| Para preparar no Mac/PC | Leitor de microSD, cartão microSD de 32 GB e uma **case USB para SSD NVMe** compatível com seu SSD. Essa case USB é temporária e não é o gabinete do Pi. |
| Para usar em casa | Ethernet, ZBT-2 com cabo USB e um dispositivo Zigbee para testar. |

**Escolha uma montagem:**

- **M.2 HAT+ padrão:** aceita SSDs **2230 ou 2242**. Pode ficar acima do **Active Cooler**, usando os espaçadores próprios. Escolha um gabinete com espaço para esse conjunto.
- **M.2 HAT+ Compact:** aceita apenas **2230** e cabe no case oficial do Pi 5 com a ventoinha do próprio case. Não combine essa montagem com o Active Cooler por baixo.
- **Argon ONE V3 M.2 NVMe para Pi 5:** é uma alternativa com gabinete e adaptador próprios. Na versão M.2 NVMe, não se compra outro HAT para empilhar por cima. Confira o [manual da versão exata](https://argon40.com/blogs/argon-resources/argon-one-v3-case-and-m-2-nvme-pcie-case-manual), o tamanho do SSD e as instruções de montagem.

<aside class="install-note"><strong>Sobre o Argon:</strong> o antigo ONE M.2 para Pi 4 não serve para o Pi 5. Cases com adaptador não HAT+ podem precisar de ajustes próprios de inicialização; ventoinha e botão também podem exigir suporte específico no HAOS. Para seguir este guia inteiramente pelas telas, use o HAT+ oficial ou um kit Argon já preparado e testado para HAOS pelo fornecedor. Não execute instaladores de Raspberry Pi OS dentro do HAOS.</aside>

## 2. Baixe o programa no seu Mac ou PC

| Download oficial | Para que serve |
|---|---|
| [Raspberry Pi Imager](https://www.raspberrypi.com/software/) | Preparar o cartão de inicialização e gravar HAOS no SSD. Escolha a versão de macOS ou Windows. |
| [balenaEtcher](https://etcher.balena.io/) | Alternativa para gravar a imagem do HAOS no SSD; o preparo do boot continua pelo Imager. |
| [Imagem HAOS para Pi 5 — 18.3](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_rpi5-64-18.3.img.xz) | Download manual, se usar Etcher. O nome precisa conter **rpi5-64**. |
| [Página oficial da instalação](https://www.home-assistant.io/installation/raspberrypi/) | Consulte aqui a imagem estável mais recente. No Imager, use a opção disponível no catálogo. |
| [Montagem do M.2 HAT+](https://www.raspberrypi.com/documentation/accessories/m2-hat-plus.html) | Fotos de cada encaixe, para a versão padrão ou Compact. |

**No Mac:** abra o arquivo baixado e siga o instalador; se houver uma janela com o ícone do aplicativo, arraste-o para **Aplicativos**. **No Windows:** abra o instalador oficial e conclua as telas. Não precisa instalar programas no Pi antes disso.

A imagem 18.3 é a versão consultada em 22/09/2026. Se houver uma versão estável mais recente na documentação, prefira-a; evite versões de teste para começar.

## 3. Prepare o Pi para iniciar pelo NVMe

O **bootloader** é o pequeno programa que decide de onde o Pi vai iniciar. Esta etapa atualiza e redefine essa configuração; é indicada para a central nova que estamos montando.

1. No Mac/PC, coloque o microSD no leitor. Desconecte outros discos removíveis para facilitar a identificação.
2. Abra o **Raspberry Pi Imager** e escolha **Raspberry Pi 5** em dispositivo.
3. Em sistema operacional, abra **Misc utility images → Bootloader (Pi 5 family) → NVMe/USB Boot**. Os nomes podem aparecer traduzidos.
4. Em armazenamento, selecione **o microSD**, conferindo capacidade e nome. Avance e grave. **Isso apaga o cartão.** Aguarde a verificação e ejete-o.
5. Com o Pi sem energia, coloque o cartão. Ligue a fonte, aguarde pelo menos 10 segundos e espere o LED verde piscar rapidamente de forma contínua. Com monitor HDMI conectado, o sucesso também aparece como uma tela verde. Não interrompa a gravação.
6. Depois da indicação de sucesso, desligue a alimentação e retire o cartão de preparação. Ele não deve ficar no Pi na inicialização normal.

Se aparecer uma tela vermelha ou um padrão de erro, não continue como se a atualização tivesse terminado: confira o cartão, a fonte e o [procedimento oficial de recuperação](https://github.com/raspberrypi/rpi-eeprom/blob/master/imager/README-2712.txt).

## 4. Grave o HAOS no SSD NVMe

1. Com a case USB desconectada, encaixe o SSD NVMe nela conforme o manual. Conecte essa case ao Mac/PC.
2. No Imager, escolha **Raspberry Pi 5**. Em sistema operacional, abra **Other specific-purpose OS → Home automation → Home Assistant** e selecione **Home Assistant OS para Raspberry Pi 5**.
3. Em armazenamento, selecione **o SSD externo**, identificando o modelo e a capacidade. Não escolha o disco do computador nem o microSD da etapa anterior.
4. Se o assistente oferecer personalizações de Wi-Fi, usuário ou SSH, pule-as para HAOS. Essas opções de Raspberry Pi OS não são necessárias aqui.
5. Confirme a gravação. **Todo o conteúdo do SSD escolhido será apagado.** Aguarde gravação e verificação completas; depois, ejete a unidade.
6. Se o Mac ou Windows pedir para formatar/inicializar o SSD gravado, **cancele**: as partições do HAOS não são um disco comum para arquivos.

<figure class="ha-screen"><a href="/static/img/ha-guide/imager.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Selecione Home Assistant OS para Pi 5; na etapa de armazenamento, o destino deste guia é o SSD NVMe conectado por USB."><img src="/static/img/ha-guide/imager.png" alt="Selecione Home Assistant OS para Pi 5; na etapa de armazenamento, o destino deste guia é o SSD NVMe conectado por USB." width="860" height="538" loading="lazy" decoding="async"></a><figcaption>Selecione Home Assistant OS para Pi 5; na etapa de armazenamento, o destino deste guia é o SSD NVMe conectado por USB. <a class="ext" href="https://www.home-assistant.io/installation/raspberrypi/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

<details><summary>Prefiro usar o balenaEtcher para gravar o SSD</summary><p>Baixe a imagem <strong>haos_rpi5-64-…img.xz</strong> no link acima. No Etcher, escolha <strong>Flash from file</strong>, selecione o arquivo, use <strong>Select target</strong> para marcar o SSD externo e confira novamente sua capacidade. Clique em <strong>Flash!</strong>, autorize a gravação e espere a validação. Ejete o SSD. Não use a imagem de Pi 4 ou de mini-PC x86-64. O Etcher aceita imagens comprimidas em XZ; se sua versão não as abrir, extraia para .img antes.</p></details>

## 5. Monte placa, refrigeração, HAT e SSD

Retire o SSD da case USB **com tudo desconectado da energia**. Monte sobre uma superfície limpa, segurando as placas pelas bordas.

1. Instale a refrigeração da montagem escolhida. No HAT+ padrão, coloque o Active Cooler antes do HAT. No Compact, siga o arranjo do case oficial.
2. Coloque os espaçadores, para que as placas não encostem uma na outra. No HAT+ padrão, alinhe o extensor GPIO com todos os pinos antes de pressionar.
3. Abra com cuidado a trava do conector **PCIe** do Pi 5. Insira o cabo flat reto e trave novamente. Siga a orientação de contatos ilustrada no manual da sua versão; não force as travas.
4. Fixe o HAT e conecte a outra ponta do cabo flat. Nenhum cabo deve ficar preso sob o SSD ou a tampa.
5. Encaixe o SSD levemente inclinado no M.2. Abaixe-o e prenda a ponta com o parafuso próprio, sem apertar demais.
6. Confira ventoinha, folgas e cabos. Feche apenas um gabinete compatível com a altura do conjunto.

<div class="install-photo-pair"><figure class="install-figure"><a href="/static/img/install/pi-ribbon.png" target="_blank" rel="noopener" aria-label="Ampliar: HAT+ padrão: espaçadores e cabo flat no conector PCIe."><img src="/static/img/install/pi-ribbon.png" width="2084" height="2084" alt="HAT+ padrão: espaçadores e cabo flat no conector PCIe." loading="lazy" decoding="async"></a><figcaption>HAT+ padrão: espaçadores e cabo flat no conector PCIe. <a class="ext" href="https://www.raspberrypi.com/documentation/accessories/m2-hat-plus.html" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure><figure class="install-figure"><a href="/static/img/install/pi-ssd.png" target="_blank" rel="noopener" aria-label="Ampliar: HAT+ padrão: encaixe inclinado do SSD antes de prendê-lo."><img src="/static/img/install/pi-ssd.png" width="2084" height="2084" alt="HAT+ padrão: encaixe inclinado do SSD antes de prendê-lo." loading="lazy" decoding="async"></a><figcaption>HAT+ padrão: encaixe inclinado do SSD antes de prendê-lo. <a class="ext" href="https://www.raspberrypi.com/documentation/accessories/m2-hat-plus.html" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure></div>

As ilustrações acima são do **HAT+ padrão**. Para o Compact e para o Argon, use as imagens do manual correspondente; a posição dos encaixes muda.

## 6. Ligue a rede e inicie pelo SSD

Conecte Ethernet entre o Pi e o roteador/switch. Confira se o cartão de preparação foi removido e ligue a fonte. O Pi deverá iniciar pelo NVMe e preparar o HAOS. Não é necessário deixar a case USB conectada nem manter o Mac/PC ligado depois da configuração.

**Não iniciou?** Confira a fonte de 27 W, o cabo flat, o encaixe do SSD e se foi gravada a imagem **rpi5-64**. O monitor micro-HDMI pode mostrar o diagnóstico. Um adaptador não HAT+ pode exigir ajustes adicionais do fabricante; a simples seleção NVMe/USB Boot não garante seu funcionamento. Não ative PCIe Gen 3 para este começo.

<details><summary>Quero começar com microSD e adicionar o SSD depois</summary><p>No Imager, grave HAOS para Pi 5 em um microSD A2 de pelo menos 32 GB e inicie por ele. Depois de fazer um backup, você pode usar <strong>Configurações → Sistema → Armazenamento → Mover disco de dados</strong>, se o SSD for detectado e tiver capacidade maior que a mídia atual. Isso apaga o SSD e transfere os dados; o cartão continua necessário para iniciar. É diferente do caminho principal deste guia, que grava o sistema inteiro no NVMe. Veja a <a href="https://www.home-assistant.io/common-tasks/os/#using-external-data-disk">orientação oficial</a>.</p></details>

## 7. Abra a sua casa no navegador

No **outro computador**, conectado à mesma rede da central, abra [http://homeassistant.local:8123](http://homeassistant.local:8123). Esse computador pode usar Wi-Fi; a central fica ligada ao roteador por Ethernet.

1. Aguarde a tela de preparação terminar. O primeiro início baixa componentes e pode demorar, conforme a internet. Mantenha a central ligada.
2. Se aparecer **Criar minha casa inteligente / Create my smart home**, siga por essa opção. Quem já tem um backup pode escolher restaurá-lo.
3. Crie o **usuário administrador e uma senha exclusiva**. É uma conta da sua central, diferente da conta opcional da Nabu Casa.
4. Confira localização, fuso horário e unidades. Autorize compartilhamentos opcionais apenas se desejar.
5. Conclua até chegar ao painel. Dispositivos encontrados automaticamente podem ser configurados depois.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central."><img src="/static/img/ha-guide/onboarding.png" alt="Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

**O endereço não abriu?** Digite-o na barra de endereços, incluindo `http://` e `:8123`. Confira cabos, energia e se o computador está na mesma rede, fora da rede de convidados. No app do roteador, procure o IP atribuído ao Home Assistant e abra `http://IP-DA-CENTRAL:8123`, substituindo pelo número real. Algumas instalações recentes usam a porta padrão: experimente também [http://homeassistant.local](http://homeassistant.local). Não abra portas no roteador para este acesso dentro de casa.

## 8. Conecte o ZBT-2 e ative o ZHA

O **ZBT-2** é o rádio USB do Zigbee. **ZHA** é a integração que já vem no Home Assistant para cuidar dessa rede. Não precisa instalar MQTT ou outro App.

1. Com o Home Assistant funcionando, conecte o ZBT-2 a uma porta USB da **central**, usando seu cabo. Não o conecte ao computador usado apenas para abrir o navegador.
2. Deixe o rádio afastado de metal, roteador Wi-Fi e dispositivos USB 3.0, com espaço ao redor da antena.
3. Abra **Configurações → Dispositivos e serviços**. No dispositivo descoberto **Home Assistant Connect ZBT-2**, escolha **Adicionar / Configurar**.
4. Selecione **Usar como adaptador Zigbee** e a **instalação recomendada**. Aguarde as etapas de firmware indicadas na tela, sem desconectar o cabo. O assistente cria a integração ZHA.
5. Se não houver descoberta, use **Adicionar integração** e procure **Home Assistant Connect ZBT-2**. Confira se aparece no hardware da central; siga o [assistente oficial](https://support.nabucasa.com/hc/en-us/articles/29400591254301) para sua versão.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

O ZBT-2 usa **Zigbee ou Thread, um por vez**. Aqui, escolha Zigbee.

## 9. Adicione um sensor ou uma luz

1. Em **Configurações → Dispositivos e serviços → Zigbee Home Automation**, abra **Adicionar dispositivo**.
2. Perto do ZBT-2, coloque seu sensor ou sua lâmpada em pareamento conforme o manual. O tempo de pressionar o botão varia por modelo; aparelhos ligados a outra central podem precisar de redefinição.
3. Espere a descoberta e a configuração terminarem. Dê um nome, como **Sensor da porta**, e escolha o cômodo.
4. Abra o dispositivo e faça um teste: abra a porta ou ligue a luz pela tela. Confira se o estado muda.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee."><img src="/static/img/ha-guide/zha-add.png" alt="Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 10. Faça o primeiro backup e siga em frente

Em **Configurações → Sistema → Backups**, configure backups automáticos. Guarde uma cópia fora da central e o **kit de emergência / chave de criptografia** indicado na interface; você precisa dele para restaurar backups criptografados. A cópia pode ficar no computador, em armazenamento de rede ou no serviço de nuvem escolhido.

Confira as atualizações em **Configurações** e faça um backup antes de aplicá-las. Para desligar ou mexer no hardware, use **Configurações → Sistema → menu de energia → Desligar sistema**, aguarde o encerramento e só então retire a fonte.

**Seu ponto de chegada:** painel acessível, ZHA configurado e o primeiro dispositivo respondendo. Agora, [crie uma automação simples pelas telas](/primeira-automacao/).

Referências desta parte: [primeiro acesso](https://www.home-assistant.io/getting-started/onboarding/), [ZBT-2 e ZHA](https://support.nabucasa.com/hc/en-us/articles/29400591254301), [backups](https://www.home-assistant.io/common-tasks/general/#backups). [Créditos das novas ilustrações](/static/img/install/README.md).


Referências da montagem: [Raspberry Pi / HAOS](https://www.home-assistant.io/installation/raspberrypi/), [M.2 HAT+ e Compact](https://www.raspberrypi.com/documentation/accessories/m2-hat-plus.html), [catálogo oficial do Imager](https://downloads.raspberrypi.com/os_list_imagingutility_v4.json), [bootloader do Pi 5](https://github.com/raspberrypi/rpi-eeprom/blob/master/imager/README-2712.txt) e [Argon ONE V3](https://argon40.com/blogs/argon-resources/argon-one-v3-case-and-m-2-nvme-pcie-case-manual).
