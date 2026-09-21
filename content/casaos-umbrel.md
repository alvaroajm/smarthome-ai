---
title: CasaOS e umbrelOS: o home server fácil ao lado do Home Assistant
slug: casaos-umbrel
description: O que são esses sistemas de home server, como se comparam entre si e ao Home Assistant, e como fazer os dois conviverem na mesma casa sem conflito.
category: Home server
icon: server
order: 17
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [CasaOS, umbrelOS, ZimaOS, Docker, NAS, Self-hosting]
---

Home Assistant cuida da **casa**. CasaOS e umbrelOS cuidam dos **serviços da casa** — arquivos, fotos, mídia,
backups, painéis, IA local. São funções complementares e podem conviver no mesmo projeto.

## O que essas coisas são, afinal

O **CasaOS** adiciona um painel de arquivos e aplicativos Docker a um Linux compatível. O **umbrelOS** é um sistema completo para nuvem pessoal, com administração pelo navegador e loja de apps. Ambos facilitam o uso de serviços como Jellyfin e Nextcloud, mas têm instalação e licenças diferentes.

| | **CasaOS** | **umbrelOS** | **ZimaOS** |
|---|---|---|---|
| O que é | Camada instalável sobre Debian/Ubuntu/Raspberry Pi OS | Sistema completo para home server | Sistema completo com foco em NAS, da mesma equipe do CasaOS |
| Instalação | Um comando sobre um Linux existente | Imagem gravada no disco ou VM | Imagem gravada no disco |
| Loja de apps | Curada + qualquer container Docker | 300+ apps com instalação em um clique | Curada, orientada a armazenamento |
| Armazenamento | Gerenciamento de arquivos e discos | Arquivos, backups e recursos de armazenamento conforme versão e hardware | Foco em gestão de discos e NAS |
| Licença/código | Apache 2.0 | Código disponível; PolyForm Noncommercial 1.0.0 | Consulte as licenças dos componentes |
| Melhor para | Reaproveitar um PC antigo ou Raspberry Pi | Quem quer "ligar e usar", com fotos e arquivos | Quem quer NAS de verdade em hardware Zima |

**Em poucas palavras:** CasaOS ajuda a aproveitar um Linux que você já tem; umbrelOS oferece uma experiência de servidor pessoal integrada. O site do CasaOS também apresenta o **ZimaOS**, evolução do ecossistema com foco em NAS.

Links oficiais: [CasaOS](https://casaos.zimaspace.com/) · [CasaOS no GitHub](https://github.com/IceWhaleTech/CasaOS) ·
[umbrelOS](https://umbrel.com/umbrelos) · [Umbrel App Store](https://apps.umbrel.com/) ·
[Umbrel no GitHub](https://github.com/getumbrel/umbrel) · [ZimaOS](https://github.com/IceWhaleTech/ZimaOS)

!!! nota "Nenhum deles substitui o Home Assistant"
    Os dois até oferecem o Home Assistant na loja de apps — mas nessa forma ele roda como **container**,
    sem Supervisor e, portanto, **sem add-ons** (Zigbee2MQTT, ESPHome Device Builder, Mosquitto, Terminal &
    SSH) administrados pelo Supervisor. Esses serviços podem rodar separadamente. Veja as opções abaixo.

## CasaOS na prática

Roda em amd64, arm64 e armv7 — de um Intel NUC ou mini-PC a um Raspberry Pi. Instala sobre um Linux que você
já tenha (Debian 12, Ubuntu Server, Raspberry Pi OS são os oficialmente suportados):

```bash
# instalação (sobre um Debian/Ubuntu/Raspberry Pi OS já funcionando)
wget -qO- https://get.casaos.io | sudo bash
```

Depois é só abrir `http://<ip-do-servidor>` no navegador. A interface traz monitor de CPU, memória e disco,
gerenciador de arquivos visual e a loja de apps — e permite instalar containers adicionais. Confira volumes, portas e compatibilidade de cada aplicativo antes de importar uma configuração.

!!! atencao "Rode o instalador com cuidado"
    `wget | sudo bash` executa um script remoto como root. Use em uma máquina dedicada ao laboratório,
    após conferir a documentação e fazer backup. O Home Assistant OS não é um Linux genérico para receber esse instalador.

**Bom para**: reaproveitar aquele notebook velho ou um Raspberry Pi extra como servidor de mídia, backup e
utilidades, com uma interface mais simples para administrar os serviços.

## umbrelOS na prática

É um sistema completo: você grava a imagem (Raspberry Pi, mini-PC/NUC ou máquina virtual), liga na rede e faz
toda a configuração pelo navegador em `http://umbrel.local` — sem monitor nem teclado. Não precisa de Linux
prévio nem de linha de comando.

Destaques da linha atual: loja com mais de 300 apps, aplicativo de **fotos** com backup automático do rolo da
câmera do iPhone, gerenciador de **arquivos** com busca, contas separadas para cada pessoa da casa,
redundância de disco e integração com agentes de IA via **MCP**. Na consulta de **21/09/2026**, o site oficial informa beta público do umbrelOS 2.0 e lançamento previsto para 22/09. Confira a versão disponível antes de instalar; recursos variam por versão e hardware.

**Bom para**: quem quer sair do Google Fotos e do Dropbox com o mínimo de atrito, ou quem comprou um
Umbrel Home / Umbrel Pro pronto.

## Onde o Home Assistant entra

Há três arranjos possíveis, conforme sua experiência e disponibilidade de hardware:

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
- ✅ backups do Home Assistant estão disponíveis também no Container; os dados dos outros containers e do sistema anfitrião precisam de uma estratégia própria
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

- Quer **automatizar a casa**? Home Assistant OS é o caminho mais simples para a maioria das pessoas; Container é uma alternativa para quem administra Docker.
- Quer **serviços caseiros** com pouco esforço? CasaOS (sobre um Linux que você já tem) ou umbrelOS
  (sistema completo, mais "plug and play").
- Quer os dois? **Separe as máquinas** ou use virtualização. Isso permite manter automação e serviços com ciclos de manutenção separados.

## Referências oficiais

- [CasaOS: recursos, instalação e sistemas compatíveis](https://github.com/IceWhaleTech/CasaOS).
- [umbrelOS: plataforma e novidades](https://umbrel.com/umbrelos) e [licença do projeto](https://github.com/getumbrel/umbrel#license).
- [Métodos de instalação do Home Assistant](https://www.home-assistant.io/installation/).
- [Backups do Home Assistant](https://www.home-assistant.io/common-tasks/general/#backups).
