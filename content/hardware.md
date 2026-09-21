---
title: Raspberry Pi, mini-PC ou appliance: escolhendo o hardware
slug: hardware
description: Comparação honesta entre Home Assistant Green, Raspberry Pi 5, mini-PCs N100 e NAS, com consumo, armazenamento e quando cada um vale a pena.
category: Hardware
icon: server
order: 4
featured: true
reading: 9 min de leitura
date: 2026-09-21
tags: [Raspberry Pi, Mini-PC, Proxmox, NAS, Hardware]
---

A pergunta certa não é "qual é o mais potente", e sim **"quanto trabalho de manutenção eu quero ter"**.
Quem escolhe hardware demais acaba com um servidor para cuidar; quem escolhe de menos troca tudo em um ano.

## Comparação direta

| | Appliance (HA Green) | Raspberry Pi 5 + NVMe | Mini-PC N100/N150 | NAS / servidor existente |
|---|---|---|---|---|
| **Instalação** | Ligou, funcionou | Média | Média | Avançada (Docker/VM) |
| **Consumo típico** | ~2 W | 4–7 W | 7–15 W | 20–40 W |
| **Preço (BR, estimado)** | Médio | Médio-alto | Médio-alto | Já é seu |
| **Roda Frigate/IA** | Não | Limitado | **Sim** (veja Intel x AMD abaixo) | Sim |
| **Expansão** | Baixa | Boa (HAT, PoE) | Ótima | Ótima |
| **Manutenção** | Mínima | Baixa | Baixa | Alta |

!!! dica "Resumo em uma linha"
    Quer uma casa inteligente? **HA Green ou Pi 5 com SSD.** Quer também câmeras com detecção de objetos,
    dupla função de servidor de mídia e experimentos com IA local? **Mini-PC x86.**

## Armazenamento: onde quase todo projeto morre

- **Cartão microSD: não.** O Home Assistant grava métricas continuamente no banco de dados; cartões de consumo
  desgastam e corrompem, em geral entre 6 e 18 meses.
- **SSD NVMe via HAT** no Raspberry Pi 5 ou **SSD interno** no mini-PC é o padrão hoje.
- 128 GB bastam para o sistema; câmeras exigem disco à parte (e, de preferência, um HDD, que aguenta escrita contínua).
- Se você insiste em SD para testar, **reduza a retenção** do recorder e mantenha backups diários.

```yaml
# configuration.yaml — banco de dados mais leve
recorder:
  purge_keep_days: 10
  commit_interval: 30
  exclude:
    domains:
      - device_tracker
      - automation
    entity_globs:
      - sensor.*_rssi
      - sensor.*_uptime
```

## Raspberry Pi 5: o que comprar junto

- Fonte oficial de 27 W (USB-C PD) — fontes genéricas causam reinícios aleatórios
- HAT NVMe + SSD de 128–256 GB
- Gabinete com dissipador e ventoinha (o Pi 5 esquenta mais que os anteriores)
- **Uma extensão USB 2.0 de 1 metro** para o coordenador Zigbee (explicação abaixo)
- Cabo de rede — deixe o Wi-Fi para os dispositivos, não para o servidor

## Mini-PC x86: quando compensa

Um N100 com 16 GB de RAM e SSD de 512 GB roda, ao mesmo tempo: Home Assistant, Frigate com detecção por
aceleração Intel (OpenVINO/Quick Sync), Zigbee2MQTT, Mosquitto, Scrypted, um servidor de mídia e ainda sobra.
Um Ryzen 5 ou Ryzen 7 entrega bem mais processamento pelo mesmo preço — com uma ressalva nas câmeras que
está explicada na seção seguinte. Duas formas de instalar:

1. **HAOS direto no disco** — mais simples, o aparelho é "do Home Assistant".
2. **Proxmox com o Home Assistant em VM** — permite snapshots antes de cada atualização, outras VMs e
   containers. É a escolha de quem gosta de laboratório — e o caminho natural para quem já tem um
   [home server com CasaOS ou umbrelOS](/casaos-umbrel/).

## Intel ou AMD? A diferença que só aparece nas câmeras

Para o Home Assistant puro, tanto faz: qualquer processador x86 dos últimos dez anos sobra. A escolha só
pesa quando entram **câmeras com detecção de objetos** e **IA local**, porque as duas plataformas resolvem
isso de formas diferentes.

| | **Intel (N100, N150, Core série H)** | **AMD (Ryzen 5 / Ryzen 7)** |
|---|---|---|
| Decodificar vídeo das câmeras | Quick Sync — maduro e simples | VAAPI na Radeon integrada — funciona bem |
| **Detectar objetos no Frigate** | **OpenVINO** na iGPU ou na NPU: suporte oficial, um parâmetro e pronto | **ROCm**: oficial só para **GPUs dedicadas**; na iGPU "funciona na maioria dos casos", sem suporte formal |
| Configuração extra | Praticamente nenhuma | Pode exigir a variável `HSA_OVERRIDE_GFX_VERSION` |
| Força bruta de CPU | Modesta no N100 | Bem superior num Ryzen 7 |
| Consumo em repouso | ~7 W (N100) | ~10–20 W |

Traduzindo: o **Intel é o caminho sem atrito** para quem quer câmeras funcionando rápido. O **AMD entrega
muito mais processamento pelo mesmo dinheiro**, ao custo de meia hora de configuração no Frigate — ou de um
plano B.

!!! dica "O plano B do AMD para câmeras"
    Duas ou três câmeras com detecção em 640×480 a 5 fps rodam em CPU num Ryzen 7 sem sofrimento. Passando
    disso, um módulo **Hailo-8L** (M.2) resolve de vez — a própria documentação do Frigate já desaconselha o
    Coral para instalações novas. Para descobrir a versão da sua iGPU antes de configurar o ROCm, rode
    `rocminfo` e procure a linha `gfx`.

### Exemplo: um Ryzen 7 com 16 GB e 1 TB

É uma configuração comum e generosa. O erro clássico é instalar o HAOS direto no disco e usar 20% da
máquina. Com **Proxmox**, ela vira quatro coisas ao mesmo tempo:

| Máquina virtual | vCPU | RAM | Disco | Função |
|---|---|---|---|---|
| Home Assistant OS | 2 | 4 GB | 64 GB | A casa, com Supervisor e apps completos |
| [Frigate](/cameras-ia/) (VM ou LXC) | 4 | 4–6 GB | 32 GB + volume de vídeo | Câmeras e detecção |
| Docker / [CasaOS](/casaos-umbrel/) | 2 | 2–4 GB | 100 GB | Mídia, fotos, Ollama, utilidades |
| Proxmox (host) | — | ~1,5 GB | — | Snapshots antes de cada atualização |

Dois avisos que valem mais que qualquer benchmark:

- **16 GB é o gargalo, não o processador.** Somando as VMs acima não sobra espaço para um modelo local
  (um modelo de 7–8B quantizado quer 5–6 GB só para ele). Quase todo mini-PC Ryzen tem **dois slots
  SO-DIMM** — subir para 32 GB é o melhor upgrade por real gasto nessa máquina.
- **O NVMe não deve gravar vídeo.** Gravação contínua é escrita 24 horas por dia, e é assim que SSD morre.
  Sistema e VMs no NVMe; gravações do Frigate num **HDD** (baia interna ou USB 3). Só com o NVMe, limite a
  retenção a poucos dias e grave apenas eventos.

### Ajustes de BIOS de qualquer mini-PC servidor

- **Restore on AC Power Loss → Power On** — sem isso, a casa não volta sozinha depois de uma queda de energia
- Desativar suspensão e estados de sono
- Reservar VRAM para a iGPU (*UMA Frame Buffer*), se for usar IA local
- Ativar virtualização (VT-x / AMD-V e IOMMU) se for usar Proxmox

!!! atencao "Mac mini e Raspberry Pi como servidor"
    Um Mac mini M4 é excelente para Scrypted, transcodificação e IA local — mas o Home Assistant no macOS só
    roda em Docker/VM, sem add-ons. O arranjo que funciona bem: **HAOS num Pi ou mini-PC** cuidando da casa e
    o **Mac cuidando de vídeo, mídia e modelos locais**.

## O detalhe que salva a rede Zigbee

Coordenadores USB (SkyConnect/ZBT-1, Sonoff ZBDongle, ConBee) operam em 2,4 GHz — exatamente a faixa que as
portas **USB 3.0 e SSDs NVMe poluem** com ruído eletromagnético. Plugar o dongle direto no gabinete é a causa
número um de "meus sensores caem sozinhos".

**Solução**: extensão USB 2.0 de 1 a 2 metros, dongle longe do servidor, do roteador e de qualquer metal.
É barato e resolve 80% dos problemas de estabilidade.

## Energia e continuidade

- Um **nobreak pequeno (600 VA)** cobre servidor, roteador e ONT por 20 a 40 minutos. Numa casa com automação,
  isso é a diferença entre uma queda de energia e uma remontagem de rede.
- Ligue o nobreak ao Home Assistant por USB com a integração **NUT** e crie uma automação que desliga
  o sistema com elegância quando a bateria chega a 20%.

## Roteiro de compra sugerido

1. Servidor (Green, Pi 5 + NVMe ou mini-PC)
2. Coordenador Zigbee + extensão USB
3. Três a cinco sensores baratos (movimento, porta, temperatura)
4. Dois ou três atuadores que resolvam incômodos reais (módulo de relé, tomada inteligente com medição)
5. **Só depois** pense em painel dedicado, voz e câmeras

Comprar nessa ordem evita a gaveta cheia de aparelhos que nunca foram integrados.
