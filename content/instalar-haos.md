---
title: Instalar o Home Assistant OS: passo a passo no Raspberry Pi 5 e no mini-PC
slug: instalar-haos
description: Tutorial completo, com todos os links de download, para gravar e configurar o Home Assistant OS num Raspberry Pi 5 (NVMe ou microSD) e num mini-PC x86 — direto no disco ou em VM no Proxmox.
category: Começando
icon: server
order: 2
featured: true
reading: 16 min de leitura
date: 2026-09-21
tags: [Home Assistant OS, Raspberry Pi 5, Mini-PC, Proxmox, Instalação, NVMe]
---

Este é o passo a passo completo, do download ao primeiro acesso. Escolha o seu caminho:
**[Raspberry Pi 5](#caminho-a-raspberry-pi-5)** ou **[mini-PC x86](#caminho-b-mini-pc-x86-64)**. Os dois
terminam no mesmo lugar: `http://homeassistant.local:8123` funcionando na sua rede.

!!! nota "Versão usada neste guia"
    Os links diretos apontam para o **Home Assistant OS 18.3**, publicado em setembro de 2026. Para pegar
    sempre a mais recente, use a página de
    [releases oficiais](https://github.com/home-assistant/operating-system/releases/latest) e troque o
    número da versão no nome do arquivo.

## Downloads — tudo em um lugar

| O que | Para quê | Link |
|---|---|---|
| **Raspberry Pi Imager** | Gravar o cartão/SSD do Pi (e atualizar o bootloader) | [Página oficial](https://www.raspberrypi.com/software/) · [Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe) · [macOS](https://downloads.raspberrypi.org/imager/imager_latest.dmg) · [Ubuntu](https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb) |
| **HAOS para Raspberry Pi 5** | Imagem do sistema (arm64) | [haos_rpi5-64-18.3.img.xz](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_rpi5-64-18.3.img.xz) |
| **HAOS para PC x86-64** | Imagem para gravar direto no disco | [haos_generic-x86-64-18.3.img.xz](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_generic-x86-64-18.3.img.xz) |
| **HAOS em qcow2** | Máquina virtual (Proxmox, QEMU/KVM) | [haos_ova-18.3.qcow2.xz](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_ova-18.3.qcow2.xz) |
| **balenaEtcher** | Gravador de imagens (Windows, macOS, Linux) | [etcher.balena.io](https://etcher.balena.io/) |
| **Ventoy** | Pendrive que inicia vários ISOs | [ventoy.net](https://www.ventoy.net/en/download.html) |
| **Ubuntu Desktop** | Live USB para gravar o disco do mini-PC | [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop) |
| **Proxmox VE** | Virtualizador para o caminho B2 | [proxmox.com/downloads](https://www.proxmox.com/en/downloads) |
| Documentação oficial | Referência | [Raspberry Pi](https://www.home-assistant.io/installation/raspberrypi) · [x86-64](https://www.home-assistant.io/installation/generic-x86-64) · [Outros métodos](https://www.home-assistant.io/installation/alternative) |

---

## Caminho A: Raspberry Pi 5

### A1. O que você precisa

- **Raspberry Pi 5** (4 ou 8 GB de RAM — 4 GB já basta para a maioria das casas)
- **Fonte oficial de 27 W USB-C PD** — fontes genéricas causam reinícios aleatórios
- **Armazenamento**: HAT NVMe + SSD de 128–256 GB (recomendado) **ou** cartão microSD de boa marca,
  só para testar
- **Gabinete com dissipador e ventoinha** — o Pi 5 esquenta
- **Cabo de rede** (deixe o Wi-Fi para a segunda etapa)
- Um cartão microSD extra, se você for atualizar o bootloader (passo A2)

!!! atencao "Cartão SD é para teste, não para morar"
    O banco de dados do Home Assistant escreve o tempo todo. Cartões de consumo falham em geral entre 6 e
    18 meses — e em silêncio. Se for usar SD agora, planeje migrar para SSD depois com
    `ha os datadisk move`, descrito nos [comandos do HAOS](/comandos-haos/).

### A2. Prepare o bootloader para NVMe (só se for usar SSD)

O Pi 5 de fábrica pode não estar configurado para iniciar por NVMe. Resolve-se em cinco minutos, **antes**
de gravar o Home Assistant:

1. Abra o **Raspberry Pi Imager** e escolha *Raspberry Pi 5* como dispositivo
2. Em **Sistema Operacional**, vá em **Misc utility images → Bootloader (Pi 5) → NVMe/USB Boot**
3. Grave num cartão microSD qualquer
4. Ligue o Pi com esse cartão, espere a tela ficar verde (cerca de 10 segundos), desligue e remova o cartão

Pronto: a EEPROM foi atualizada e a ordem de inicialização passa a tentar o NVMe primeiro.

### A3. Grave o Home Assistant OS

**Jeito mais simples — pelo próprio Imager:**

1. Abra o Raspberry Pi Imager
2. **Dispositivo**: Raspberry Pi 5
3. **Sistema Operacional**: role até **Other specific-purpose OS → Home assistants and home automation →
   Home Assistant → Home Assistant OS (RPi 5)**
4. **Armazenamento**: selecione o SSD NVMe (ou o cartão microSD)
5. Clique em **Gravar** e confirme. Quando pedir personalizações (usuário, Wi-Fi), escolha **Não** — o
   HAOS não usa essas opções

**Jeito manual — com a imagem baixada:**

1. Baixe [haos_rpi5-64-18.3.img.xz](https://github.com/home-assistant/operating-system/releases/download/18.3/haos_rpi5-64-18.3.img.xz)
2. Abra o [balenaEtcher](https://etcher.balena.io/) → *Flash from file* → selecione o `.img.xz`
   (**não precisa descompactar**)
3. Escolha o disco de destino e grave

No macOS, se preferir o terminal:

```bash
# descubra o disco (cuidado: escolher errado apaga o disco errado)
diskutil list

# desmonte e grave (troque diskN pelo seu)
diskutil unmountDisk /dev/diskN
xzcat ~/Downloads/haos_rpi5-64-18.3.img.xz | sudo dd of=/dev/rdiskN bs=4m status=progress
sync
```

### A4. Primeiro boot

1. Monte o SSD/cartão no Pi, conecte o **cabo de rede** e ligue
2. A primeira inicialização leva de 5 a 20 minutos (o sistema expande partições e baixa componentes)
3. No navegador do computador, abra:

```text
http://homeassistant.local:8123
```

Se o `.local` não resolver — comum em redes com mesh ou VLAN —, descubra o IP no painel do roteador e use
`http://192.168.x.y:8123`. Siga para o [primeiro acesso](#primeiro-acesso-em-qualquer-caminho).

---

## Caminho B: mini-PC x86-64

Serve para N100, N150, Ryzen, NUC, ThinkCentre e qualquer PC antigo com 64 bits. Escolha:

- **B1 — HAOS direto no disco**: a máquina é "do Home Assistant". Mais simples e mais rápido.
- **B2 — HAOS em VM no Proxmox**: permite snapshots antes de cada atualização e outras VMs na mesma máquina.

### B0. Ajustes de BIOS (vale para os dois)

Entre no BIOS (geralmente <kbd>Del</kbd>, <kbd>F2</kbd> ou <kbd>F7</kbd> ao ligar) e configure:

| Opção | Valor | Por quê |
|---|---|---|
| **Restore on AC Power Loss** | **Power On** | A casa volta sozinha depois de uma queda de energia |
| **Secure Boot** | Desativado | O HAOS não é assinado para Secure Boot |
| **Boot Mode** | UEFI | O HAOS x86-64 instala em UEFI |
| **Suspensão / Sleep** | Desativado | Servidor não dorme |
| **Virtualização (VT-x / AMD-V, IOMMU)** | Ativado | Necessário só no caminho B2 |

### B1. HAOS direto no disco

O truque: você **não instala** o HAOS, você **grava a imagem no disco**. Para isso é preciso iniciar a
máquina por outro sistema.

1. Num pendrive de 8 GB ou mais, instale o [Ventoy](https://www.ventoy.net/en/download.html) e copie para
   ele o ISO do [Ubuntu Desktop](https://ubuntu.com/download/desktop)
2. Inicie o mini-PC pelo pendrive e escolha **Experimentar Ubuntu** (*Try Ubuntu*)
3. Conecte a rede e abra o Terminal:

```bash
# ferramentas
sudo apt update && sudo apt install -y xz-utils curl

# identifique o disco de destino (nvme0n1, sda...) — confira o tamanho!
lsblk

# baixe a imagem
curl -L -o haos.img.xz \
  https://github.com/home-assistant/operating-system/releases/download/18.3/haos_generic-x86-64-18.3.img.xz

# grave no disco interno (TROQUE /dev/nvme0n1 pelo seu disco)
xzcat haos.img.xz | sudo dd of=/dev/nvme0n1 bs=4M status=progress conv=fsync
sync
```

4. Desligue, **remova o pendrive** e ligue novamente. O Home Assistant inicia sozinho.

!!! atencao "O `dd` não pergunta duas vezes"
    Esse comando apaga **todo** o disco indicado, sem confirmação e sem volta. Confira a saída do `lsblk`
    com calma: `nvme0n1` é o disco inteiro; `nvme0n1p1` seria uma partição. Se houver dois discos, tenha
    certeza de qual é qual pelo tamanho.

Prefere interface gráfica? Instale o [balenaEtcher](https://etcher.balena.io/) dentro da sessão do Ubuntu e
grave o `.img.xz` escolhendo o disco interno como destino — mesmo resultado.

### B2. HAOS em VM no Proxmox

1. Instale o [Proxmox VE](https://www.proxmox.com/en/downloads) no mini-PC (ISO gravado com Ventoy ou Etcher)
2. Acesse o painel em `https://IP-DO-PROXMOX:8006` e abra o **Shell** do nó
3. Crie a VM:

```bash
# baixe e descompacte a imagem de disco
cd /var/lib/vz/template
wget https://github.com/home-assistant/operating-system/releases/download/18.3/haos_ova-18.3.qcow2.xz
xz -d haos_ova-18.3.qcow2.xz

# crie a VM (UEFI, q35 — exigido pelo HAOS)
qm create 100 --name haos --memory 4096 --cores 2 --machine q35 --bios ovmf \
  --net0 virtio,bridge=vmbr0 --ostype l26 --scsihw virtio-scsi-pci \
  --efidisk0 local-lvm:0,efitype=4m,pre-enrolled-keys=0

# importe o disco (anote o nome que o comando imprime no final)
qm importdisk 100 haos_ova-18.3.qcow2 local-lvm

# conecte o disco importado e defina a ordem de boot
qm set 100 --scsi0 local-lvm:vm-100-disk-1
qm set 100 --boot order=scsi0

# opcional: repasse o dongle Zigbee para dentro da VM
qm set 100 --usb0 host=10c4:ea60

qm start 100
```

4. Na aba **Console** da VM aparece o IP do Home Assistant

!!! dica "Atalho conhecido"
    Se preferir não digitar nada, existe um script da comunidade que cria essa VM com uma linha:
    [Proxmox VE Helper-Scripts — Home Assistant OS VM](https://community-scripts.github.io/ProxmoxVE/scripts?id=haos-vm).
    Leia o script antes de rodar — ele executa com privilégios de root no seu servidor.

!!! atencao "Descubra o ID do seu dongle antes do passthrough"
    Rode `lsusb` no shell do Proxmox: `10c4:ea60` é o par fabricante:produto de muitos adaptadores, mas o
    seu pode ser outro. Repassar o dispositivo **pelo ID** sobrevive a mudanças de porta.

---

## Primeiro acesso (em qualquer caminho)

1. Abra `http://homeassistant.local:8123` (ou o IP) e crie a **conta de administrador**
2. Confirme **localização, fuso horário e unidades** — metade das automações depende do nascer e do pôr do sol
3. Aceite os dispositivos descobertos automaticamente que fizerem sentido
4. Vá em *Configurações → Sistema → Backups* e **ative o backup automático**, com uma cópia fora do aparelho
5. No roteador, **reserve o IP** do Home Assistant (DHCP estático)
6. Em *Configurações → Sistema → Atualizações*, atualize o Core e o sistema operacional

Checagem rápida pelo terminal (app **Terminal & SSH**):

```bash
ha os info          # versão do sistema operacional
ha core info        # versão do Home Assistant
ha hardware info    # discos, USB e o caminho do dongle Zigbee
ha backups new --name "instalacao-inicial"
```

## Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| `homeassistant.local` não abre | mDNS bloqueado pela rede | Use o IP direto; veja [rede e VLANs](/rede-wifi/) |
| Pi 5 não inicia pelo SSD | Bootloader antigo | Refaça o passo [A2](#a2-prepare-o-bootloader-para-nvme-so-se-for-usar-ssd) |
| Reinícios aleatórios no Pi | Fonte fraca | Use a fonte oficial de 27 W |
| Mini-PC volta ao pendrive | Ordem de boot | Remova o pendrive e ajuste a ordem no BIOS |
| Tela preta no x86 após gravar | Secure Boot ligado | Desative o Secure Boot |
| VM não inicia no Proxmox | BIOS SeaBIOS em vez de OVMF | Recrie com `--bios ovmf --machine q35` |
| Não volta após queda de luz | BIOS em "Power Off" | Ajuste *Restore on AC Power Loss* |
| Dongle Zigbee some ao reiniciar | Uso de `/dev/ttyUSB0` | Use o caminho `/dev/serial/by-id/...` |

## Próximos passos

- [Comece aqui](/instalacao/) — a visão geral, se você pulou direto para este tutorial
- [Escolha do hardware](/hardware/) — Pi 5, mini-PC Intel ou AMD, e o que muda nas câmeras
- [Zigbee na prática](/zigbee/) e [os dongles ZBT](/zbt-dongles/) — os primeiros sensores
- [Comandos do HAOS](/comandos-haos/) — a referência de linha de comando
