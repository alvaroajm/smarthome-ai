---
title: Comece aqui: instalando o Home Assistant do zero
slug: instalacao
description: A trilha completa — escolher o hardware, gravar a imagem, fazer o primeiro acesso, proteger com backup e adicionar o primeiro dispositivo.
category: Começando
icon: rocket
order: 1
featured: true
reading: 12 min de leitura
date: 2026-09-21
tags: [Home Assistant, Instalação, Raspberry Pi, Backup]
---

Se você só quer que **as luzes acendam sozinhas** e não pretende virar administrador de servidores, esta é a
rota mais curta. O objetivo desta página é te levar do "não tenho nada" até "minha primeira automação rodando",
sem decisões que você vá se arrepender daqui a seis meses.

## 1. Escolha onde o Home Assistant vai morar

O Home Assistant precisa de um computador ligado 24 horas por dia. As três escolhas sensatas hoje:

| Opção | Ideal para | Pontos de atenção |
|---|---|---|
| **Appliance pronto** (Home Assistant Green e similares) | Quem quer ligar e usar | Menos expansível; armazenamento fixo |
| **Raspberry Pi 5 + SSD NVMe** | Quem gosta de mexer | **Nunca use cartão SD** como disco principal |
| **Mini-PC x86 (N100/N150)** | Quem quer rodar câmeras, IA local, Frigate | Consome mais energia; instalação via Proxmox ou HAOS direto |

!!! dica "Regra de ouro"
    Qualquer uma das três serve. O que **não** serve é rodar sua casa num notebook que você leva para o trabalho
    ou num cartão microSD barato — cartão SD morre por desgaste de escrita, normalmente no pior momento possível.

Os detalhes de cada opção, com consumo e custo, estão no [guia de hardware](/hardware/).

## 2. Escolha o método de instalação

Existem quatro formas de instalar, e elas **não** são equivalentes:

- **Home Assistant OS (HAOS)** — sistema operacional dedicado. Tem a loja de add-ons, atualizações com um clique
  e backup integrado. **É o recomendado para 95% das pessoas.**
- **Home Assistant Supervised** — em cima de um Debian que você mantém. Só se você souber exatamente por quê.
- **Home Assistant Container (Docker)** — leve e flexível, mas **sem add-ons**; você instala Mosquitto,
  Zigbee2MQTT e companhia por conta própria.
- **Home Assistant Core (venv Python)** — para desenvolvimento. Evite no dia a dia.

!!! atencao "O erro mais comum de quem começa"
    Instalar a versão Container por achar "mais profissional" e só descobrir semanas depois que metade dos
    tutoriais da internet pressupõe add-ons que você não tem. Comece com **HAOS**.

!!! dica "Quer o passo a passo detalhado?"
    Este guia é a visão geral. Para o tutorial completo, com todos os links de download, gravação no
    Raspberry Pi 5 (inclusive NVMe) e no mini-PC x86, e criação da VM no Proxmox, veja
    **[Instalar o Home Assistant OS passo a passo](/instalar-haos/)**.

## 3. Grave a imagem e ligue

1. Baixe a imagem HAOS correspondente ao seu hardware em [home-assistant.io/installation](https://www.home-assistant.io/installation/).
2. Grave com o **Raspberry Pi Imager** (opção "Use custom image") ou com o **balenaEtcher**, no SSD ou no eMMC.
3. Conecte o aparelho **ao roteador por cabo de rede** na primeira instalação — Wi-Fi na largada só complica o diagnóstico.
4. Ligue e espere de 5 a 20 minutos na primeira inicialização: o sistema está se expandindo e baixando componentes.
5. No navegador do seu Mac ou PC, acesse:

```text
http://homeassistant.local:8123
```

Se o endereço `.local` não resolver (comum em redes com Wi-Fi mesh ou VLANs), descubra o IP no painel do
roteador e use `http://192.168.x.y:8123`.

## 4. Os primeiros 10 minutos que importam

Ao criar a conta de administrador, o assistente vai detectar sozinho boa parte dos aparelhos da rede.
Antes de sair clicando, faça estas quatro coisas:

1. **Defina a localização e o fuso horário corretos.** Metade das automações depende do nascer e do pôr do sol.
2. **Crie o primeiro backup** em *Configurações → Sistema → Backups* e ative os backups automáticos.
3. **Reserve o IP no roteador** (DHCP estático) para o Home Assistant nunca trocar de endereço.
4. **Renomeie tudo com calma.** `sensor.temperatura_quarto` envelhece bem; `sensor.0x00158d0004f2a1` não.

!!! nota "Backup é o que separa um hobby de um susto"
    Guarde uma cópia **fora do aparelho** — Google Drive, um NAS, uma pasta do iCloud no seu Mac. O add-on
    *Samba Backup* ou a integração com armazenamento em nuvem resolvem isso em cinco minutos.

## 5. Adicione o primeiro dispositivo

A ordem que causa menos frustração:

1. **Algo que já está na rede**: sua TV, o receptor AV, a impressora, um aspirador. Vá em
   *Configurações → Dispositivos e serviços* e aceite as integrações descobertas automaticamente.
2. **Um sensor Zigbee barato** (temperatura ou contato de porta), com um coordenador USB.
   Veja [Zigbee2MQTT ou ZHA](/zigbee/) para escolher o rádio e o software.
3. **Um dispositivo Matter**, se você já tem uma Apple TV, um HomePod ou um hub que sirva de
   [border router Thread](/matter-thread/).

## 6. Sua primeira automação (a que realmente se usa)

Esqueça cenas complicadas. Comece com uma automação que resolve um incômodo real — luz do corredor à noite:

```yaml
alias: Corredor - luz suave ao detectar movimento à noite
description: Acende em 20% entre 22h e 6h e apaga sozinha
triggers:
  - trigger: state
    entity_id: binary_sensor.corredor_movimento
    to: "on"
conditions:
  - condition: time
    after: "22:00:00"
    before: "06:00:00"
actions:
  - action: light.turn_on
    target:
      entity_id: light.corredor
    data:
      brightness_pct: 20
  - delay: "00:02:00"
  - action: light.turn_off
    target:
      entity_id: light.corredor
mode: restart
```

O `mode: restart` é o detalhe que faz a automação parecer inteligente: se houver movimento de novo durante
os dois minutos, o contador reinicia em vez de apagar a luz na sua cara.

## 7. Checklist antes de expandir

- [x] Backup automático ativo e com cópia externa
- [x] IP reservado no roteador
- [x] Acesso remoto resolvido (Nabu Casa, VPN do roteador ou Tailscale — **nunca** abrindo a porta 8123 na internet)
- [x] Coordenador Zigbee numa extensão USB, longe do gabinete e das portas USB 3.0
- [x] Nomes e áreas organizados

Se precisar de linha de comando em algum momento, a [referência de comandos do HAOS](/comandos-haos/) cobre o CLI `ha` e o shell Alpine.

Com isso pronto, siga para o [guia do Home Assistant](/home-assistant/) e entenda como a plataforma pensa —
é o que transforma uma coleção de aparelhos numa casa que funciona.
