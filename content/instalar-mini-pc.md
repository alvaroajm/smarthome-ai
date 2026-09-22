---
title: Instalar HAOS no mini-PC x86-64, passo a passo
slug: instalar-mini-pc
description: Pendrive, BIOS UEFI e gravação do HAOS no SSD interno de um mini-PC Intel ou AMD.
category: Instalação guiada
icon: book
order: 3
featured: false
level: basico
reading: 15 min de leitura
date: 2026-09-22
tags: [Home Assistant]
---

Vamos transformar um **mini-PC Intel ou AMD de 64 bits** em uma central dedicada ao Home Assistant OS. O procedimento serve a máquinas compatíveis, como modelos N150 e Ryzen; confira o hardware específico antes de comprar.

Usaremos um pendrive com **Ubuntu em modo de teste**, apenas para gravar o HAOS no SSD interno. Depois, o pendrive sai e o mini-PC inicia direto no Home Assistant. Tudo pelas telas.

[← Escolher outro equipamento](/instalar-haos/)

<aside class="install-note"><strong>Antes de começar:</strong> este procedimento substitui o Windows/Linux do mini-PC e apaga o disco escolhido. Copie seus arquivos, guarde chaves de recuperação e tenha o backup fora dele. Use uma máquina dedicada. O Mac/PC usado para preparar o pendrive não será formatado: confira sempre o disco de destino.</aside>

## 1. Separe equipamentos e confira compatibilidade

- Mini-PC **x86-64 (Intel ou AMD)** com inicialização **UEFI**. Este guia não é para mini-PC ARM.
- RAM e SSD já instalados. Para nossas sugestões de hardware, 16 GB e SSD/NVMe de 500/512 GB ou 1 TB são um bom ponto de partida; não são requisitos mínimos do HAOS.
- SSD com setores lógicos de **512 bytes (512n/512e)**. Unidades exclusivamente **4Kn** não servem para iniciar esta imagem do HAOS; confira a ficha do fabricante.
- Pendrive vazio de **16 GB ou mais** e um Mac/PC para prepará-lo.
- Monitor, teclado e mouse conectados ao mini-PC durante a instalação.
- Cabo Ethernet, roteador com internet, fonte do mini-PC e o ZBT-2 para a etapa Zigbee.

Se o mini-PC tiver mais de um disco, identifique de antemão o que receberá HAOS. Desconecte mídias externas que não serão usadas.

## 2. Baixe os arquivos oficiais

| Download | Onde usar |
|---|---|
| [Ubuntu Desktop LTS — Intel/AMD 64 bits](https://ubuntu.com/download/desktop) | Baixe a imagem **ISO amd64**, para preparar o pendrive. Mesmo que seu Mac seja Apple Silicon, o destino é o mini-PC Intel/AMD. |
| [balenaEtcher para macOS ou Windows](https://etcher.balena.io/) | No computador auxiliar, grava a ISO do Ubuntu no pendrive. Escolha o aplicativo compatível com esse computador. |
| [HAOS Generic x86-64 — 18.3](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_generic-x86-64-18.3.img.xz) | Baixe **dentro do Ubuntu temporário**, na etapa 5; ele será gravado no SSD interno. |
| [Instalação oficial Generic x86-64](https://www.home-assistant.io/installation/generic-x86-64/) | Referência e link para a versão estável mais recente do HAOS. |

A imagem 18.3 é a versão consultada em 22/09/2026. Se a documentação oficial indicar uma estável mais recente, use-a. O nome do arquivo precisa conter **generic-x86-64**, não Raspberry Pi, VDI, VMDK ou QCOW2.

As capturas oficiais podem mostrar versões anteriores do Ubuntu, Etcher ou HAOS. Use os botões como referência e baixe a imagem atual indicada acima; toque nas imagens para ampliar.

## 3. Prepare o pendrive no Mac ou PC

1. Instale e abra o **balenaEtcher** oficial. No Mac, siga o instalador ou arraste o aplicativo para Aplicativos; no Windows, conclua o instalador baixado.
2. Conecte o pendrive. Em **Flash from file**, escolha a **ISO do Ubuntu**.
3. Em **Select target**, marque **o pendrive**, conferindo nome e capacidade. Não selecione o SSD do seu computador.
4. Clique em **Flash!**, confirme a gravação e espere a validação. **Todo o pendrive será apagado.**
5. Ejete o pendrive. Se aparecer uma solicitação para formatá-lo, cancele.

<figure class="install-figure"><a href="/static/img/install/etcher-file.png" target="_blank" rel="noopener" aria-label="Ampliar: Etcher: escolha Flash from file. Nesta etapa, use a ISO do Ubuntu, embora a tela oficial exemplifique uma imagem do HAOS."><img src="/static/img/install/etcher-file.png" width="802" height="519" alt="Etcher: escolha Flash from file. Nesta etapa, use a ISO do Ubuntu, embora a tela oficial exemplifique uma imagem do HAOS." loading="lazy" decoding="async"></a><figcaption>Etcher: escolha Flash from file. Nesta etapa, use a ISO do Ubuntu, embora a tela oficial exemplifique uma imagem do HAOS. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

<figure class="install-figure"><a href="/static/img/install/etcher-target.png" target="_blank" rel="noopener" aria-label="Ampliar: Confira o destino antes de gravar. Aqui deve ser o pendrive, não o disco do Mac/PC."><img src="/static/img/install/etcher-target.png" width="802" height="519" alt="Confira o destino antes de gravar. Aqui deve ser o pendrive, não o disco do Mac/PC." loading="lazy" decoding="async"></a><figcaption>Confira o destino antes de gravar. Aqui deve ser o pendrive, não o disco do Mac/PC. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

## 4. Prepare o mini-PC e abra o Ubuntu temporário

1. Conecte monitor, teclado, mouse, Ethernet e o pendrive ao mini-PC.
2. Ligue-o e abra a configuração **BIOS/UEFI**. As teclas mais comuns são **F2** ou **Del**, mas use a indicada pelo fabricante.
3. Selecione inicialização **UEFI**. Desative **Secure Boot**, conforme exige o HAOS. Se houver modo Legacy/CSM, prefira UEFI. Não altere opções sem relação com a instalação.
4. Salve e reinicie. Abra o menu de boot — muitas máquinas usam F10, F11 ou F12 — e escolha a entrada **UEFI do pendrive**.
5. No Ubuntu, selecione **Try Ubuntu / Experimentar Ubuntu**, depois que o menu inicial abrir. **Não escolha instalar o Ubuntu no SSD.**
6. Aguarde a área de trabalho. Abra o navegador e confirme a conexão com a internet.

<div class="install-photo-pair"><figure class="install-figure"><a href="/static/img/install/uefi.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Exemplo de Intel NUC: inicialização UEFI habilitada."><img src="/static/img/install/uefi.jpg" width="1280" height="720" alt="Exemplo de Intel NUC: inicialização UEFI habilitada." loading="lazy" decoding="async"></a><figcaption>Exemplo de Intel NUC: inicialização UEFI habilitada. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure><figure class="install-figure"><a href="/static/img/install/secure-boot.jpg" target="_blank" rel="noopener" aria-label="Ampliar: Exemplo de Intel NUC: Secure Boot desabilitado para HAOS."><img src="/static/img/install/secure-boot.jpg" width="1280" height="720" alt="Exemplo de Intel NUC: Secure Boot desabilitado para HAOS." loading="lazy" decoding="async"></a><figcaption>Exemplo de Intel NUC: Secure Boot desabilitado para HAOS. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure></div>

As fotos mostram uma BIOS de exemplo. Os menus de seu N150 ou Ryzen podem ser diferentes; consulte o manual do mini-PC.

## 5. Baixe o HAOS dentro do Ubuntu

No navegador do Ubuntu, abra este guia ou a [página oficial x86-64](https://www.home-assistant.io/installation/generic-x86-64/) e baixe a imagem **haos_generic-x86-64-…img.xz**. Aguarde o download terminar na pasta **Downloads**.

O arquivo **.img.xz** é uma imagem de disco comprimida. O aplicativo **Discos** pode restaurá-la diretamente. Não precisa instalar o Home Assistant por cima do Ubuntu e não basta copiar o arquivo para o SSD.

## 6. Grave no SSD interno pelo aplicativo Discos

1. Abra **Mostrar aplicativos / Show Applications**, pesquise **Discos / Disks** e inicie o programa.
2. Na coluna da esquerda, selecione **o SSD interno do mini-PC**. Confira modelo e capacidade. Não escolha o pendrive de onde o Ubuntu está rodando.
3. No menu de três pontos, escolha **Restaurar imagem de disco / Restore Disk Image**.
4. Selecione o arquivo **haos_generic-x86-64-…img.xz** que terminou de baixar.
5. Revise a origem e o destino. Clique em **Iniciar restauração / Start Restoring** e confirme em **Restaurar / Restore**. Esta é a etapa que apaga o sistema anterior do SSD.
6. Aguarde a operação terminar sem erros. Não retire energia ou o pendrive durante a gravação.

<figure class="install-figure"><a href="/static/img/install/disks-restore.png" target="_blank" rel="noopener" aria-label="Ampliar: Discos: selecione o SSD interno à esquerda e Restaurar imagem de disco no menu."><img src="/static/img/install/disks-restore.png" width="952" height="652" alt="Discos: selecione o SSD interno à esquerda e Restaurar imagem de disco no menu." loading="lazy" decoding="async"></a><figcaption>Discos: selecione o SSD interno à esquerda e Restaurar imagem de disco no menu. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

<figure class="install-figure"><a href="/static/img/install/disks-image.png" target="_blank" rel="noopener" aria-label="Ampliar: Selecione a imagem Generic x86-64 que acabou de baixar."><img src="/static/img/install/disks-image.png" width="919" height="537" alt="Selecione a imagem Generic x86-64 que acabou de baixar." loading="lazy" decoding="async"></a><figcaption>Selecione a imagem Generic x86-64 que acabou de baixar. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

<figure class="install-figure"><a href="/static/img/install/disks-progress.png" target="_blank" rel="noopener" aria-label="Ampliar: Aguarde a restauração da imagem terminar. Ela grava o HAOS diretamente no SSD."><img src="/static/img/install/disks-progress.png" width="952" height="652" alt="Aguarde a restauração da imagem terminar. Ela grava o HAOS diretamente no SSD." loading="lazy" decoding="async"></a><figcaption>Aguarde a restauração da imagem terminar. Ela grava o HAOS diretamente no SSD. <a class="ext" href="https://www.home-assistant.io/installation/generic-x86-64/" target="_blank" rel="noopener">Fonte oficial</a> · Toque para ampliar.</figcaption></figure>

**Disco ocupado / erro ao desmontar?** Confira se está usando **Experimentar Ubuntu a partir do pendrive**. Se instalou ou iniciou Ubuntu pelo SSD interno, reinicie pelo pendrive e escolha o modo de teste. Se uma antiga partição **Swap** estiver ativa no SSD, selecione somente essa partição no aplicativo Discos e use o botão de parar para desativá-la antes de restaurar. Não force a gravação em um disco que está executando o sistema.

## 7. Retire o pendrive e inicie o HAOS

1. Pelo menu do Ubuntu, escolha **Desligar**. Remova o pendrive quando o sistema pedir ou depois que o mini-PC estiver desligado.
2. Deixe Ethernet e fonte conectadas. Ligue o mini-PC novamente; ele deve iniciar pelo SSD interno.
3. Se voltar ao Ubuntu ou à tela de instalação, confira se o pendrive foi retirado. Se não encontrar sistema, confira UEFI, Secure Boot e a ordem de boot do SSD.
4. A tela do HAOS no monitor pode mostrar texto e um endereço IP. Isso é normal: a configuração de uso acontece no navegador do outro computador. Depois, monitor e teclado podem ser retirados.

<details><summary>Alternativa: gravar o SSD fora do mini-PC</summary><p>Se o método com pendrive não funcionar e o SSD for removível, a documentação oficial também permite ligá-lo a outro computador por uma case USB compatível (NVMe ou SATA, conforme o disco). Com o equipamento desligado, remova o SSD seguindo o manual. Baixe a imagem Generic x86-64, use <strong>Flash from file → Select target → Flash!</strong> no Etcher e confira o SSD correto. Espere validar, ejete e recoloque o SSD no mini-PC. Isso também apaga o disco. Nunca tente gravar sobre o disco de onde seu Mac/Windows está rodando. <a href="https://www.home-assistant.io/installation/generic-x86-64/#method-2-installing-haos-directly-from-a-boot-medium">Ver o método oficial</a>.</p></details>

## 8. Abra a sua casa no navegador

No **outro computador**, conectado à mesma rede da central, abra [http://homeassistant.local:8123](http://homeassistant.local:8123). Esse computador pode usar Wi-Fi; a central fica ligada ao roteador por Ethernet.

1. Aguarde a tela de preparação terminar. O primeiro início baixa componentes e pode demorar, conforme a internet. Mantenha a central ligada.
2. Se aparecer **Criar minha casa inteligente / Create my smart home**, siga por essa opção. Quem já tem um backup pode escolher restaurá-lo.
3. Crie o **usuário administrador e uma senha exclusiva**. É uma conta da sua central, diferente da conta opcional da Nabu Casa.
4. Confira localização, fuso horário e unidades. Autorize compartilhamentos opcionais apenas se desejar.
5. Conclua até chegar ao painel. Dispositivos encontrados automaticamente podem ser configurados depois.

<figure class="ha-screen"><a href="/static/img/ha-guide/onboarding.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central."><img src="/static/img/ha-guide/onboarding.png" alt="Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central." width="614" height="575" loading="lazy" decoding="async"></a><figcaption>Crie a conta pelo navegador. O computador apenas mostra a interface; o HAOS roda na central. <a class="ext" href="https://www.home-assistant.io/getting-started/onboarding/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

**O endereço não abriu?** Digite-o na barra de endereços, incluindo `http://` e `:8123`. Confira cabos, energia e se o computador está na mesma rede, fora da rede de convidados. No app do roteador, procure o IP atribuído ao Home Assistant e abra `http://IP-DA-CENTRAL:8123`, substituindo pelo número real. Algumas instalações recentes usam a porta padrão: experimente também [http://homeassistant.local](http://homeassistant.local). Não abra portas no roteador para este acesso dentro de casa.

## 9. Conecte o ZBT-2 e ative o ZHA

O **ZBT-2** é o rádio USB do Zigbee. **ZHA** é a integração que já vem no Home Assistant para cuidar dessa rede. Não precisa instalar MQTT ou outro App.

1. Com o Home Assistant funcionando, conecte o ZBT-2 a uma porta USB da **central**, usando seu cabo. Não o conecte ao computador usado apenas para abrir o navegador.
2. Deixe o rádio afastado de metal, roteador Wi-Fi e dispositivos USB 3.0, com espaço ao redor da antena.
3. Abra **Configurações → Dispositivos e serviços**. No dispositivo descoberto **Home Assistant Connect ZBT-2**, escolha **Adicionar / Configurar**.
4. Selecione **Usar como adaptador Zigbee** e a **instalação recomendada**. Aguarde as etapas de firmware indicadas na tela, sem desconectar o cabo. O assistente cria a integração ZHA.
5. Se não houver descoberta, use **Adicionar integração** e procure **Home Assistant Connect ZBT-2**. Confira se aparece no hardware da central; siga o [assistente oficial](https://support.nabucasa.com/hc/en-us/articles/29400591254301) para sua versão.

<figure class="ha-screen"><a href="/static/img/ha-guide/zbt-zigbee.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface."><img src="/static/img/ha-guide/zbt-zigbee.png" alt="Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface." width="564" height="317" loading="lazy" decoding="async"></a><figcaption>Escolha Zigbee no assistente do ZBT-2; o ZHA será configurado pela interface. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

O ZBT-2 usa **Zigbee ou Thread, um por vez**. Aqui, escolha Zigbee.

## 10. Adicione um sensor ou uma luz

1. Em **Configurações → Dispositivos e serviços → Zigbee Home Automation**, abra **Adicionar dispositivo**.
2. Perto do ZBT-2, coloque seu sensor ou sua lâmpada em pareamento conforme o manual. O tempo de pressionar o botão varia por modelo; aparelhos ligados a outra central podem precisar de redefinição.
3. Espere a descoberta e a configuração terminarem. Dê um nome, como **Sensor da porta**, e escolha o cômodo.
4. Abra o dispositivo e faça um teste: abra a porta ou ligue a luz pela tela. Confira se o estado muda.

<figure class="ha-screen"><a href="/static/img/ha-guide/zha-add.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee."><img src="/static/img/ha-guide/zha-add.png" alt="Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee." width="684" height="288" loading="lazy" decoding="async"></a><figcaption>Use Adicionar dispositivo no ZHA para encontrar o primeiro aparelho Zigbee. <a class="ext" href="https://support.nabucasa.com/hc/en-us/articles/29400591254301" target="_blank" rel="noopener">Tela oficial · Nabu Casa</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 11. Faça o primeiro backup e siga em frente

Em **Configurações → Sistema → Backups**, configure backups automáticos. Guarde uma cópia fora da central e o **kit de emergência / chave de criptografia** indicado na interface; você precisa dele para restaurar backups criptografados. A cópia pode ficar no computador, em armazenamento de rede ou no serviço de nuvem escolhido.

Confira as atualizações em **Configurações** e faça um backup antes de aplicá-las. Para desligar ou mexer no hardware, use **Configurações → Sistema → menu de energia → Desligar sistema**, aguarde o encerramento e só então retire a fonte.

**Seu ponto de chegada:** painel acessível, ZHA configurado e o primeiro dispositivo respondendo. Agora, [crie uma automação simples pelas telas](/primeira-automacao/).

Referências desta parte: [primeiro acesso](https://www.home-assistant.io/getting-started/onboarding/), [ZBT-2 e ZHA](https://support.nabucasa.com/hc/en-us/articles/29400591254301), [backups](https://www.home-assistant.io/common-tasks/general/#backups). [Créditos das novas ilustrações](/static/img/install/README.md).


Referências da instalação: [HAOS Generic x86-64](https://www.home-assistant.io/installation/generic-x86-64/), [Ubuntu Desktop](https://ubuntu.com/download/desktop) e [balenaEtcher](https://etcher.balena.io/).
