---
title: Claude, MCP e Home Assistant: a casa que você conversa
slug: claude-mcp
description: O que é MCP explicado sem jargão, como ligar o Claude Desktop e o Claude no terminal ao Home Assistant, quais servidores MCP valem a pena e como fazer isso com segurança.
category: IA & agentes
icon: bot
order: 14
featured: true
reading: 13 min de leitura
date: 2026-09-21
tags: [MCP, Claude, IA, Assist, Ollama, Automação]
---

Existe uma diferença enorme entre "minha casa tem um assistente de voz" e "eu converso com a minha casa".
A primeira entende comandos decorados. A segunda entende **contexto**: *"a varanda ficou com a luz acesa
ontem à noite?"*, *"crie uma automação que feche as cortinas quando o sol bater na sala"*.

O que tornou isso possível chama-se **MCP**.

## O que é MCP, em uma analogia

Antes do USB, cada aparelho tinha um conector diferente. O USB não deixou a impressora mais inteligente —
só criou **um jeito padrão** de qualquer computador conversar com qualquer periférico.

O **MCP (Model Context Protocol)** é o USB dos modelos de inteligência artificial. É um padrão aberto que
define como um programa oferece **ferramentas** e **dados** para um modelo usar. Quem fala MCP de um lado
conversa com quem fala MCP do outro, sem integração feita à mão.

Na prática:

- **Servidor MCP** — quem oferece. O Home Assistant oferece "ligar a luz da sala", "qual a temperatura do
  quarto".
- **Cliente MCP** — quem consome. Claude Desktop, Claude no terminal, ChatGPT, Cursor, Antigravity.

!!! nota "O modelo não vira dono da casa"
    O servidor MCP decide **o que** fica exposto e se o cliente pode **agir** ou apenas **ler**. É você quem
    entrega as chaves, uma a uma.

## Passo 1: ligar o MCP no Home Assistant

O Home Assistant tem uma integração oficial chamada **Model Context Protocol Server**.

1. Vá em *Configurações → Dispositivos e serviços → Adicionar integração*
2. Escolha **Model Context Protocol Server**
3. Decida se os clientes poderão **controlar** a casa ou apenas consultá-la

Dois detalhes que costumam travar iniciantes:

- **Só entra no MCP o que está exposto ao Assist.** Em *Configurações → Assistentes de voz → Expor*,
  escolha as entidades. Nada exposto = o modelo não vê nada.
- **A autenticação usa um token.** No seu perfil (canto inferior esquerdo) → aba *Segurança* → **Criar
  token de longa duração**. Copie e guarde: ele aparece **uma única vez**.

O endereço do servidor é `http://<ip-do-home-assistant>:8123/api/mcp`.

!!! atencao "Um token de longa duração é uma chave mestra"
    Ele vale para sempre e dá acesso à API do Home Assistant. Guarde num gerenciador de senhas, nunca num
    arquivo versionado no Git, e revogue na mesma tela se desconfiar de algo.

## Passo 2: Claude Desktop (no seu Mac)

O Claude Desktop conversa com servidores MCP de duas formas:

**a) Conector remoto** — se o seu Home Assistant tem endereço público e HTTPS (por exemplo, o
`https://….ui.nabu.casa` da [Nabu Casa](/nabu-casa/)), basta adicioná-lo como conector e autenticar.

**b) Ponte local** — se a casa só existe na rede interna, um pequeno programa (*mcp-proxy*) faz a ponte
entre o Claude Desktop e o endereço local. A configuração fica no arquivo de configuração do Claude
Desktop, mais ou menos assim:

```json
{
  "mcpServers": {
    "home-assistant": {
      "command": "mcp-proxy",
      "args": ["http://192.168.1.50:8123/api/mcp"],
      "env": { "API_ACCESS_TOKEN": "SEU_TOKEN_DE_LONGA_DURACAO" }
    }
  }
}
```

Reinicie o Claude Desktop e a casa aparece como ferramenta disponível. A partir daí:

> *"Quais luzes estão acesas agora?"*
> *"A temperatura do quarto passou de 26 graus em algum momento desta madrugada?"*
> *"Desligue tudo da área de serviço."*

## Passo 3: Claude no terminal (o ajudante de configuração)

O Claude Desktop é ótimo para **conversar com a casa**. O Claude no terminal é ótimo para **trabalhar na
casa**: ele lê e escreve arquivos, roda comandos e entende projetos inteiros.

Casos em que isso muda o jogo:

- **Escrever e corrigir YAML** de automações complexas, com `ha core check` rodando logo depois
- **Criar configurações do [ESPHome](/esphome-esp32/)** para um sensor novo, já com os pinos certos
- **Refatorar o `configuration.yaml`** que cresceu demais, separando em pacotes
- **Investigar logs** e explicar o que aquele erro significa
- **Versionar tudo no Git**, com mensagens de commit decentes

Para ele enxergar os arquivos do Home Assistant, há três caminhos:

| Caminho | Como funciona | Quando usar |
|---|---|---|
| **Samba** | O app *Samba share* monta `/config` como pasta de rede no Mac | O mais simples no dia a dia |
| **Git** | Você versiona `/config` num repositório e trabalha na cópia local | O mais seguro: histórico e volta atrás |
| **SSH** | Acesso direto ao [shell do HAOS](/comandos-haos/) | Ajustes rápidos e diagnóstico |

!!! dica "A combinação que funciona"
    Configuração no Git + Claude no terminal + `ha core check` antes de reiniciar. Você ganha histórico,
    revisão e a possibilidade de voltar atrás — três coisas que faltam a quem edita YAML pela interface.

## Quais servidores MCP valem a pena

A lista cresce toda semana. Para quem cuida de uma casa inteligente, estes são os que realmente aparecem no
uso diário:

| Servidor MCP | Para quê |
|---|---|
| **Home Assistant (oficial)** | Ler estados e controlar a casa |
| **Filesystem** | Ler e escrever arquivos de configuração numa pasta específica |
| **Git** | Histórico, diferenças e commits da sua configuração |
| **Fetch** | Buscar uma página da web (documentação, tabela de referência) |
| **Memory** | Dar memória persistente ao assistente entre conversas |
| **SQLite** | Consultar bancos locais — inclusive o histórico do Home Assistant |
| **Playwright / navegador** | Automatizar páginas que não têm API |
| **Cloudflare, GitHub e afins** | Se você também publica sites, como este |

Os servidores de referência ficam em
[github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

!!! atencao "Servidor MCP roda código no seu computador"
    Instale apenas o que vier de fonte conhecida. Um servidor MCP malicioso tem o mesmo poder que qualquer
    programa que você executa — e ainda ganha a ajuda de um modelo para usá-lo. Dê a cada servidor **a menor
    pasta e o menor escopo** que resolvam o problema.

## O Assist do Home Assistant com um modelo por trás

Não é obrigatório sair do Home Assistant para ter conversa natural. Em
*Configurações → Assistentes de voz*, você pode definir um **agente de conversação** baseado em modelo de
linguagem — do Claude, do Google, da OpenAI ou **local**, via [Ollama](/casaos-umbrel/) rodando no seu
mini-PC ou no Mac mini.

O arranjo mais equilibrado:

- **Comandos simples** (acender, apagar, trancar) → processados localmente, rápidos e sem custo
- **Pedidos complexos** ("deixe a casa pronta para dormir") → vão para o modelo
- **Satélites de voz** ESP32 espalhados pela casa ([ESPHome](/esphome-esp32/)) como entrada de áudio

Rodando o modelo localmente, nenhum áudio sai de casa — e o custo por pergunta é zero.

## Segurança: as cinco regras

1. **Exponha só o necessário.** Comece com luzes e sensores; deixe fechaduras, portão e alarme de fora até
   confiar no conjunto.
2. **Um token por cliente**, com nome claro ("claude-desktop-mac"). Assim você revoga um sem derrubar os outros.
3. **Cuidado com injeção de prompt.** Um modelo lê textos de muitas fontes; se uma delas contiver instruções
   disfarçadas, ele pode tentar executá-las. Isso é mais um motivo para não expor o que é crítico.
4. **Nada de tokens no Git.** Use `secrets.yaml` e `.gitignore`.
5. **Prefira ler antes de agir.** Passe semanas em modo consulta; só depois libere o controle.

Um passo adiante nessa estrada são os **agentes autônomos**, que não esperam sua pergunta — e trazem
vantagens e riscos próprios. É o tema do guia sobre [OpenClaw](/openclaw/).
