---
title: CasaOS e umbrelOS: o home server fácil ao lado do Home Assistant
slug: casaos-umbrel
description: O que são esses sistemas de home server, como se comparam entre si e ao Home Assistant, e como fazer os dois conviverem na mesma casa sem conflito.
category: Home server
icon: server
order: 16
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [CasaOS, umbrelOS, ZimaOS, Docker, NAS, Self-hosting]
---

Home Assistant cuida da **casa**. CasaOS e umbrelOS cuidam dos **serviços da casa** — arquivos, fotos, mídia,
backups, painéis, IA local. São camadas diferentes, e é muito comum (e recomendável) ter as duas.

## O que essas coisas são, afinal

Ambos são **camadas amigáveis em cima do Docker**: uma interface web com loja de aplicativos, em que
instalar o Jellyfin, o Nextcloud ou o Immich vira um clique em vez de um `docker-compose.yml` escrito à mão.

| | **CasaOS** | **umbrelOS** | **ZimaOS** |
|---|---|---|---|
| O que é | Camada instalável sobre Debian/Ubuntu/Raspberry Pi OS | Sistema completo para home server | Sistema completo com foco em NAS, da mesma equipe do CasaOS |
| Instalação | Um comando sobre um Linux existente | Imagem gravada no disco ou VM | Imagem gravada no disco |
| Loja de apps | Curada + qualquer container Docker | 300+ apps com instalação em um clique | Curada, orientada a armazenamento |
| Armazenamento | Simples (montagem de discos) | Inclui redundância (RAID/FailSafe) | Gestão de discos mais completa |
| Licença/código | Aberto (Apache 2.0) | Aberto | Aberto |
| Melhor para | Reaproveitar um PC antigo ou Raspberry Pi | Quem quer "ligar e usar", com fotos e arquivos | Quem quer NAS de verdade em hardware Zima |

Links oficiais: [CasaOS](https://casaos.io/) · [CasaOS no GitHub](https://github.com/IceWhaleTech/CasaOS) ·
[umbrelOS](https://umbrel.com/umbrelos) · [Umbrel App Store](https://apps.umbrel.com/) ·
[Umbrel no GitHub](https://github.com/getumbrel/umbrel) · [ZimaOS](https://github.com/IceWhaleTech/ZimaOS)

!!! nota "Nenhum deles substitui o Home Assistant"
    Os dois até oferecem o Home Assistant na loja de apps — mas nessa forma ele roda como **container**,
    sem Supervisor e, portanto, **sem add-ons** (Zigbee2MQTT, ESPHome Device Builder, Mosquitto, Terminal &
    SSH). Serve para experimentar; para a casa de verdade, veja a comparação logo abaixo.

## CasaOS na prática

Roda em amd64, arm64 e armv7 — de um Intel NUC ou mini-PC a um Raspberry Pi. Instala sobre um Linux que você
já tenha (Debian 12, Ubuntu Server, Raspberry Pi OS são os oficialmente suportados):

```bash
# instalação (sobre um Debian/Ubuntu/Raspberry Pi OS já funcionando)
wget -qO- https://get.casaos.io | sudo bash
```

Depois é só abrir `http://<ip-do-servidor>` no navegador. A interface traz monitor de CPU, memória e disco,
gerenciador de arquivos visual e a loja de apps — e, como tudo é Docker por baixo, você pode importar
qualquer `docker-compose` que encontrar.

!!! atencao "Rode o instalador com cuidado"
    `wget | sudo bash` executa um script remoto como root. Use em uma máquina dedicada ao laboratório,
    nunca no servidor que cuida da casa, e leia o script antes se quiser ser rigoroso.

**Bom para**: reaproveitar aquele notebook velho ou um Raspberry Pi extra como servidor de mídia, backup e
utilidades, sem virar administrador de Linux.

## umbrelOS na prática

É um sistema completo: você grava a imagem (Raspberry Pi, mini-PC/NUC ou máquina virtual), liga na rede e faz
toda a configuração pelo navegador em `http://umbrel.local` — sem monitor nem teclado. Não precisa de Linux
prévio nem de linha de comando.

Destaques da linha atual: loja com mais de 300 apps, aplicativo de **fotos** com backup automático do rolo da
câmera do iPhone, gerenciador de **arquivos** com busca, contas separadas para cada pessoa da casa,
redundância de disco e integração com agentes de IA via **MCP**. A linha 2.x está em beta público, então
confira o estado atual antes de migrar algo importante.

**Bom para**: quem quer sair do Google Fotos e do Dropbox com o mínimo de atrito, ou quem comprou um
Umbrel Home / Umbrel Pro pronto.

## Onde o Home Assistant entra

Há três arranjos que funcionam bem — em ordem de recomendação:

### 1. Duas máquinas (o mais tranquilo)

- **Máquina A**: Home Assistant OS (appliance, Raspberry Pi ou mini-PC) — só a casa, com Supervisor, add-ons
  e backups automáticos.
- **Máquina B**: CasaOS ou umbrelOS — mídia, fotos, arquivos, Frigate, IA local.

Atualizar ou reiniciar uma não derruba a outra. É o arranjo que o
[guia de hardware](/hardware/) recomenda, e o motivo é simples: você não quer que um `docker pull` de um
servidor de filmes deixe a casa sem luz automática.

### 2. Um mini-PC com virtualização

Proxmox no metal, uma **VM com Home Assistant OS** (completo, com add-ons) e outra VM ou container com
CasaOS/umbrelOS. Snapshot antes de cada atualização. É o caminho de quem gosta de laboratório.

### 3. Tudo no mesmo CasaOS/umbrelOS (com ressalvas)

Instalar o Home Assistant pela loja de apps funciona, mas você fica com o **Home Assistant Container**:

- ❌ sem add-ons → Zigbee2MQTT, Mosquitto, ESPHome e Terminal & SSH viram containers que você instala e
  mantém manualmente
- ❌ sem backup integrado do Supervisor → o backup passa a ser problema seu
- ⚠️ passar o dongle Zigbee para dentro do container exige mapear o dispositivo (`--device`) na mão
- ✅ em compensação, tudo convive numa máquina só

Se você escolher esse caminho, mapeie o coordenador pelo caminho estável:

```yaml
# trecho de docker-compose para o Home Assistant Container
services:
  homeassistant:
    image: ghcr.io/home-assistant/home-assistant:stable
    container_name: homeassistant
    network_mode: host          # necessário para descoberta automática (mDNS)
    privileged: true
    restart: unless-stopped
    volumes:
      - /DATA/AppData/homeassistant:/config
      - /etc/localtime:/etc/localtime:ro
    devices:
      - /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus-if00-port0:/dev/ttyUSB0
```

!!! dica "Descoberta automática precisa de rede host"
    Sem `network_mode: host`, o Home Assistant em container não enxerga dispositivos por mDNS/SSDP —
    Apple TV, Sonos, impressoras e boa parte das integrações "mágicas" simplesmente não aparecem.

## O que rodar no home server (e não no Home Assistant)

Serviços que pesam ou que nada têm a ver com automação ficam melhor na outra máquina:

- **Frigate** (detecção de objetos nas [câmeras](/scrypted/)) e **Scrypted**
- **Jellyfin / Plex** — mídia
- **Immich** — substituto do Google Fotos, com app para iPhone
- **Nextcloud** ou **Syncthing** — arquivos e sincronização
- **Uptime Kuma** — monitoramento (inclusive do próprio Home Assistant)
- **Vaultwarden** — senhas
- **AdGuard Home** ou **Pi-hole** — DNS e bloqueio de anúncios
- **Ollama / LM Studio** — modelos de linguagem locais, úteis como agente de conversa do Assist

Depois é só integrar: quase todos expõem uma API que o Home Assistant consome, e o MQTT costuma ser a
ponte mais simples entre os dois mundos.

## Resumo

- Quer **automatizar a casa**? Home Assistant OS, sempre.
- Quer **serviços caseiros** com pouco esforço? CasaOS (sobre um Linux que você já tem) ou umbrelOS
  (sistema completo, mais "plug and play").
- Quer os dois? **Separe as máquinas** ou use virtualização. É a diferença entre um hobby e um
  incidente doméstico numa noite de terça.
