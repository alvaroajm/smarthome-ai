---
title: Comandos do Home Assistant OS e do shell Alpine
slug: comandos-haos
description: Referência prática do CLI ha, do terminal Alpine do app Terminal & SSH e dos comandos de diagnóstico que resolvem 90% dos problemas do Home Assistant.
category: Referência
icon: terminal
order: 17
featured: true
reading: 11 min de leitura
date: 2026-09-21
tags: [Home Assistant, CLI, Alpine, Linux, SSH, Diagnóstico]
---

O Home Assistant OS tem **três shells diferentes**, e confundi-los é a origem de metade da frustração com
linha de comando. Antes da lista de comandos, vale entender onde você está pisando.

## Os três lugares onde você digita comandos

| Onde | Como chegar | O que é |
|---|---|---|
| **Console do host** | Teclado e monitor ligados no aparelho, ou porta serial | O sistema do HAOS (construído com Buildroot, mínimo e somente leitura). Mostra o prompt `ha >` |
| **Terminal & SSH (app)** | App *Terminal & SSH* → aba Terminal, ou SSH na porta configurada | Um **container Alpine Linux** com o CLI `ha`, `apk`, `nano`, `git` e acesso a `/config` |
| **Dentro do container do Core** | `docker exec -it homeassistant bash` (exige modo de proteção desligado) | O container do Home Assistant, também **Alpine**, com o Python e as dependências da aplicação |

!!! nota "Onde está o Alpine, afinal"
    O **sistema operacional** do HAOS não é Alpine — é uma imagem enxuta feita com Buildroot. Alpine é o
    Linux de dentro dos **containers**: o do Home Assistant Core e o do app Terminal & SSH. Por isso o
    `apk add` funciona no terminal do app, mas o que você instalar ali **desaparece quando o app reinicia
    ou atualiza**. Nada instalado por `apk` é permanente.

No console do host, o prompt já é o CLI: digite `login` para cair num shell raiz do host (ambiente mínimo,
para emergências). Nos demais lugares, os comandos começam com `ha`.

---

## O CLI `ha` — o que você mais vai usar

```bash
ha help                      # lista tudo
ha info                      # visão geral: versões de core, supervisor, OS e canal
ha --help <comando>          # ajuda de um subcomando
```

### Core (o Home Assistant em si)

```bash
ha core check                # valida a configuração ANTES de reiniciar — use sempre
ha core restart              # reinicia o Home Assistant
ha core restart --safe-mode  # reinicia sem integrações/temas personalizados (modo de resgate)
ha core stop                 # para
ha core start                # inicia
ha core rebuild              # recria o container do Core (não apaga /config)
ha core update               # atualiza para a última versão
ha core update --version 2026.8.3   # atualiza (ou volta) para uma versão específica
ha core info                 # versão instalada, versão disponível, porta, IP
ha core logs                 # últimos registros
ha core logs -f              # acompanha em tempo real
ha core stats                # CPU e memória do container
```

!!! dica "O par que evita dor de cabeça"
    `ha core check` e depois `ha core restart`. Reiniciar com um YAML inválido deixa o Home Assistant
    sem subir, e aí o diagnóstico fica bem menos confortável.

### Supervisor

```bash
ha supervisor info           # versão, canal, arquitetura, diagnósticos
ha supervisor logs           # registros do Supervisor (útil quando um app não inicia)
ha supervisor reload         # recarrega o estado
ha supervisor update         # atualiza o Supervisor
ha supervisor repair         # tenta reparar a instalação (containers/imagens)
```

### Host e sistema operacional

```bash
ha host reboot               # reinicia a máquina
ha host shutdown             # desliga
ha host info                 # nome, sistema operacional, kernel, disco
ha host update               # atualiza o sistema do host
ha os info                   # versão do HAOS e do bootloader
ha os update                 # atualiza o Home Assistant OS
ha os datadisk list          # lista discos candidatos a disco de dados
ha os datadisk move /dev/sda # move os dados para outro disco (migrar de SD para SSD)
ha hardware info             # todo o hardware detectado (inclui os caminhos /dev/serial/by-id)
ha hardware audio            # dispositivos de áudio
```

!!! atencao "`ha os datadisk move` migra tudo"
    É o comando que tira sua instalação do cartão SD e a coloca num SSD. Faça um **backup completo e
    baixado para outra máquina** antes — a operação reescreve o destino inteiro.

### Apps (os antigos add-ons)

Os add-ons passaram a se chamar **apps** na interface; o CLI aceita as duas formas.

```bash
ha apps                      # lista os apps instalados  (ha addons também funciona)
ha apps info core_mosquitto  # detalhes, estado, opções e versão
ha apps logs core_mosquitto  # registros do app
ha apps restart core_mosquitto
ha apps stop  core_mosquitto
ha apps start core_mosquitto
ha apps update core_mosquitto
ha apps stats core_mosquitto # consumo de CPU e memória
ha apps rebuild core_zigbee2mqtt
```

Slugs úteis: `core_mosquitto`, `core_ssh`, `core_configurator`, `a0d7b954_zigbee2mqtt`,
`5c53de3b_esphome` — confirme os seus com `ha apps --raw-json | grep slug`.

### Backups

```bash
ha backups                                  # lista os backups
ha backups new --name "antes-da-atualizacao"
ha backups new --name "so-config" --folders config --addons core_mosquitto
ha backups info <slug>                      # detalhes de um backup
ha backups restore <slug>                   # restaura tudo
ha backups restore <slug> --folders config  # restaura apenas parte
ha backups remove <slug>
```

O `<slug>` é o código de 8 caracteres que aparece na listagem. Backup criado pela linha de comando
aparece normalmente em *Configurações → Sistema → Backups*.

### Rede

```bash
ha network info                    # interfaces, IP, gateway, DNS
ha network update eth0 --ipv4-method auto
ha network update eth0 --ipv4-method static \
   --ipv4-address 192.168.1.50/24 \
   --ipv4-gateway 192.168.1.1 \
   --ipv4-nameserver 192.168.1.1
ha network vlan eth0 10            # cria uma VLAN na interface
ha dns info                        # servidor DNS interno do Supervisor
ha dns options --servers dns://1.1.1.1
```

### Diagnóstico e outros

```bash
ha resolution info           # problemas detectados e sugestões do Supervisor
ha resolution healthcheck    # roda a verificação de saúde
ha jobs info                 # tarefas em andamento
ha observer info             # o vigia que responde na porta 4357
ha multicast info            # serviço de mDNS/multicast
ha audio info                # servidor de áudio (PulseAudio)
ha cli info                  # versão do próprio CLI
```

Acrescente `--raw-json` a qualquer comando para obter a resposta crua da API — ótimo para usar em
scripts:

```bash
ha core info --raw-json | jq '.data.version'
```

---

## No terminal Alpine (app Terminal & SSH)

É um Alpine normal, com **BusyBox** no lugar de várias ferramentas GNU. O gerenciador de pacotes é o `apk`:

```bash
apk update                       # atualiza o índice de pacotes
apk add --no-cache sqlite        # instala (some ao reiniciar o app!)
apk add --no-cache jq nmap tcpdump usbutils
apk search mosquitto             # procura um pacote
apk info -L sqlite               # lista os arquivos de um pacote
```

!!! atencao "Nada instalado com `apk` sobrevive a um restart"
    Só o que está em `/config`, `/addons`, `/ssl`, `/share`, `/backup` e `/media` persiste. Se você
    precisa de uma ferramenta sempre disponível, coloque o `apk add` no campo *init commands* do app
    Terminal & SSH, ou use um app próprio.

### Arquivos e pastas que importam

```bash
ls -la /config                   # sua configuração (configuration.yaml, automations.yaml...)
ls -la /config/.storage          # registros de entidades/dispositivos — NÃO edite com o HA rodando
ls -lh /config/home-assistant_v2.db     # tamanho do banco de dados
ls -la /share /media /ssl /backup
du -sh /config/* | sort -h | tail -15   # o que está ocupando espaço
df -h                            # espaço livre por partição
free -m                          # memória
```

### Edição e verificação de YAML

```bash
nano /config/configuration.yaml     # ou: vi
ha core check                        # valida antes de reiniciar
grep -rn "sensor.temperatura" /config --include=*.yaml
```

### Banco de dados (quando o disco começa a encher)

```bash
apk add --no-cache sqlite
sqlite3 /config/home-assistant_v2.db \
  "SELECT COUNT(*) AS registros, metadata_id FROM states GROUP BY metadata_id ORDER BY registros DESC LIMIT 15;"
```

Pare o Home Assistant (`ha core stop`) antes de qualquer escrita no banco, e prefira resolver pelo
`recorder:` no `configuration.yaml` — excluir entidades barulhentas vale mais que qualquer faxina manual.

### Rede e dispositivos USB

```bash
ip a                                 # endereços IP do container
ping -c 3 1.1.1.1
nslookup homeassistant.local
nc -vz 192.168.1.50 1883             # testa se a porta do MQTT responde
ls -l /dev/serial/by-id/             # caminho estável do dongle Zigbee/Z-Wave
lsusb                                # exige: apk add --no-cache usbutils
dmesg | tail -30                     # o dongle foi reconhecido?
```

---

## Acesso ao Docker (modo de proteção desligado)

Por padrão, o app Terminal & SSH roda **isolado**. Desligando a opção *Protection mode* na página do app,
o terminal ganha acesso ao Docker do host:

```bash
docker ps                                  # todos os containers do sistema
docker exec -it homeassistant bash         # entra no container do Core (Alpine)
docker logs -f homeassistant               # registros direto do container
docker stats                               # consumo em tempo real
docker system df                           # espaço usado por imagens e volumes
```

Dentro do container do Core você tem o Python do Home Assistant:

```bash
python3 -m homeassistant --script check_config --config /config
pip list | grep -i zigbee
```

!!! atencao "Modo de proteção existe por um motivo"
    Com ele desligado, um app malicioso (ou um comando distraído) alcança o Docker e, portanto, todo o
    sistema. Ligue para o que precisa, faça o que veio fazer e **volte a ativar** a proteção.

---

## Sequências que resolvem problemas reais

**A configuração quebrou e o Home Assistant não sobe**

```bash
ha core logs | tail -50        # veja o erro exato
ha core check                  # onde está o YAML inválido
ha core restart --safe-mode    # sobe sem integrações personalizadas
```

**Um app (add-on) não inicia**

```bash
ha apps logs <slug>
ha supervisor logs | tail -40
ha apps rebuild <slug>
```

**Sensores Zigbee sumiram depois de uma reinicialização**

```bash
ls -l /dev/serial/by-id/                 # o caminho mudou?
ha apps logs a0d7b954_zigbee2mqtt | tail -30
ha hardware info | grep -A3 serial
```

**Antes de qualquer atualização**

```bash
ha backups new --name "pre-$(date +%Y%m%d)"
ha core check
ha core update
```

**O disco está enchendo**

```bash
df -h
du -sh /config/* /share/* /backup/* 2>/dev/null | sort -h | tail -20
docker system df                # se a proteção estiver desligada
```

---

## Referências oficiais

- [Tarefas comuns no Home Assistant OS](https://www.home-assistant.io/common-tasks/os/)
- [Home Assistant CLI (código-fonte)](https://github.com/home-assistant/cli)
- [App Terminal & SSH](https://github.com/home-assistant/addons/tree/master/ssh)
- [Documentação do Alpine Linux — `apk`](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper)

Os nomes de subcomandos mudam de tempos em tempos (os add-ons viraram "apps", por exemplo). Quando algo
não funcionar como descrito aqui, `ha help` e `ha <comando> --help` são sempre a fonte mais atual.
