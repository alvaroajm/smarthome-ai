---
title: OpenClaw na casa inteligente: o que é e como usar sem se machucar
slug: openclaw
description: O agente autônomo de código aberto que virou febre, como ele se conecta ao Home Assistant e as precauções de segurança que ninguém deveria ignorar.
category: IA & agentes
icon: key
order: 15
featured: true
reading: 10 min de leitura
date: 2026-09-21
tags: [OpenClaw, Agentes, IA, Segurança, Home Assistant]
---

Se o [MCP](/claude-mcp/) permite **você perguntar** algo à sua casa, um agente autônomo tenta **agir sozinho**
a partir de um objetivo. O OpenClaw é o projeto de código aberto que popularizou essa ideia — e é também um
ótimo estudo de caso sobre o que acontece quando damos autonomia a um software dentro de casa.

## O que é o OpenClaw

É um **agente de IA autônomo, gratuito e de código aberto**, que roda na sua própria máquina e usa modelos
de linguagem externos (Claude, GPT, DeepSeek, ou modelos locais) para executar tarefas. A interface
principal não é um site: são **aplicativos de mensagem** — Signal, Telegram, Discord. Você manda uma
mensagem e o agente trabalha.

Um pouco de história, porque o nome muda a cada três meses e isso confunde:

- **Nov/2025** — lançado por Peter Steinberger com o nome **Warelay**
- **Jan/2026** — vira **Clawdbot**, depois **Moltbot** (por questão de marca) e enfim **OpenClaw**
- **Fev/2026** — o criador é contratado pela OpenAI e o projeto passa a ser tocado pela **OpenClaw Foundation**

O conceito central são as **skills**: pastas com instruções e metadados que ensinam novas capacidades ao
agente. É o que o torna extensível — e também o que o torna perigoso, como veremos.

## Como ele se conecta ao Home Assistant

Há um **add-on comunitário** (não oficial) que instala o OpenClaw dentro do Home Assistant, com suporte a
amd64, aarch64 e armv7. Uma vez rodando, ele pode:

- **ler e alterar arquivos em `/config`** — inclusive o `configuration.yaml` e as automações
- **usar o [MCP](/claude-mcp/)** para consultar estados e acionar dispositivos
- **receber acesso SSH**, se você conceder, e administrar o sistema
- conversar com você pelo Telegram enquanto faz tudo isso

Também é possível rodá-lo **fora** do Home Assistant — num [home server com CasaOS ou
umbrelOS](/casaos-umbrel/), por exemplo — e deixá-lo conversar com a casa apenas pela API. Essa segunda
opção é bem mais sensata, pelos motivos abaixo.

!!! nota "Onde ele brilha"
    Tarefas repetitivas e chatas: renomear cinquenta entidades seguindo um padrão, converter automações
    antigas para a sintaxe nova, montar um painel a partir de uma descrição, vasculhar logs de uma semana
    atrás procurando um padrão, escrever a configuração de um sensor ESPHome novo.

## A parte que ninguém deveria pular: os riscos

O projeto é jovem, evoluiu rápido demais e acumulou problemas de segurança **documentados publicamente**:

- **Permissões amplas por padrão** — pede acesso a e-mail, calendário e mensagens; mal configurado, expõe
  muito mais do que se imagina.
- **Injeção de prompt** — instruções maliciosas escondidas em textos que o agente lê (um e-mail, uma página,
  o nome de um arquivo) podem alterar o comportamento dele.
- **Skills de terceiros** — pesquisadores da Cisco encontraram skills que exfiltravam dados sem que o
  usuário percebesse.
- **Ações não solicitadas** — houve caso de um agente criar um perfil em site de relacionamento por conta
  própria, fora do que o usuário pediu.
- **Segredos sem criptografia** — a versão 2.0 guardava senhas e chaves de API em texto puro, sem
  isolamento de rede e sem sandbox ativada por padrão.
- **Restrições institucionais** — em março de 2026, a China proibiu o uso em órgãos estatais e bancos,
  justamente por essas questões.

!!! atencao "Traduzindo para a sua casa"
    Um agente com acesso a `/config` e SSH pode, na prática, **reescrever a sua casa**. Se ele interpretar
    mal um pedido — ou for induzido por um texto malicioso — o estrago vai de apagar automações a abrir a
    fechadura da porta. Isso não é motivo para não usar; é motivo para usar **com limites explícitos**.

## Como usar com segurança

**1. Máquina separada.** Não instale no mesmo aparelho que cuida da casa. Um mini-PC, um container no
[CasaOS/umbrelOS](/casaos-umbrel/) ou uma VM. Se algo der errado, o problema fica contido.

**2. Token restrito.** Crie um token de longa duração **só para o agente**, com nome próprio, e exponha ao
Assist apenas o que ele precisa ver. Fechadura, portão, alarme e câmeras ficam de fora — pelo menos no começo.

**3. Modo leitura primeiro.** Passe algumas semanas com o agente podendo apenas consultar. Você vai aprender
onde ele erra antes de ele poder errar com consequências.

**4. Nada de SSH.** A opção existe; a resposta é não. Se você precisa de administração do sistema, faça pelo
[terminal](/comandos-haos/), com as suas mãos.

**5. Backup antes, sempre.**

```bash
ha backups new --name "antes-do-agente-$(date +%Y%m%d)"
```

**6. Git no `/config`.** Assim qualquer alteração feita pelo agente aparece num `git diff` — e volta atrás
com um comando.

**7. Limite de gastos.** Agentes rodando em laço consomem tokens de API rapidamente. Configure um teto de
gastos no painel do provedor; é o equivalente a um disjuntor.

**8. Desconfie de skills.** Instale apenas o que você leu ou o que vem de fonte reconhecida. Uma skill é
código com a força de um agente por trás.

## OpenClaw, MCP ou Assist: qual usar?

| Você quer… | Use |
|---|---|
| Perguntar coisas e controlar a casa por voz | **[Assist](/claude-mcp/)**, com ou sem modelo de linguagem |
| Conversar com a casa pelo computador e escrever automações | **[Claude + MCP](/claude-mcp/)** |
| Delegar tarefas longas e repetitivas, aceitando os riscos | **OpenClaw**, isolado e com escopo mínimo |
| Que a casa funcione quando a internet cair | **Automações locais** — sempre a base de tudo |

!!! dica "A regra que resume tudo"
    Automação crítica não se delega a modelo nenhum. Luz, clima e cenas podem ser inteligentes; fechadura,
    portão, alarme e irrigação merecem lógica simples, local e previsível — do tipo que você consegue
    depurar às duas da manhã.

## Para acompanhar

- [OpenClaw (verbete da Wikipédia)](https://en.wikipedia.org/wiki/OpenClaw) — histórico e incidentes documentados
- [Add-on comunitário para Home Assistant](https://github.com/techartdev/OpenClawHomeAssistant)
- [Discussão na comunidade do Home Assistant](https://community.home-assistant.io/t/openclaw-clawdbot-on-home-assistant/981467)

O campo de agentes autônomos está mudando rápido — e boa parte do que se lê hoje envelhece em semanas.
Vale acompanhar, experimentar numa máquina isolada e manter a casa de verdade rodando em cima de
automações locais e entediantes.
