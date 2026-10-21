---
title: Sua primeira automação pelas telas
slug: primeira-automacao
description: Crie no editor visual do Home Assistant uma automação que acende a luz ao pôr do sol, teste cada etapa e aprenda a diagnosticar quando não funciona.
category: Passo a passo
icon: book
order: 7
featured: true
level: basico
reading: 6 min de leitura
date: 2026-09-22
updated: 2026-10-20
tags: [Home Assistant]
---

Vamos criar a regra **“ao pôr do sol, ligar a luz da sala”**. Antes, confirme que a lâmpada já funciona pelo painel e que a localização da casa está correta.

## 1. Abra o editor

Acesse **Configurações → Automações e cenas → Criar automação → Criar nova automação**.

<figure class="ha-screen"><a href="/static/img/ha-guide/automation.png" target="_blank" rel="noopener" aria-label="Ampliar tela: O editor visual: Quando, E se e Então fazer."><img src="/static/img/ha-guide/automation.png" alt="O editor visual: Quando, E se e Então fazer." width="1021" height="586" loading="lazy" decoding="async"></a><figcaption>O editor visual: Quando, E se e Então fazer. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

## 2. Escolha quando a luz deve acender

Em **Quando**, selecione **Adicionar gatilho**, procure **Sol** e escolha **Pôr do sol**. Deixe o deslocamento em zero para usar o horário do pôr do sol.

O campo **E se** é opcional. Vamos deixá-lo vazio neste primeiro teste.

## 3. Escolha o que deve acontecer

Em **Então fazer**, clique em **Adicionar ação**, procure **Luz: ligar** e selecione sua lâmpada como alvo. Se ela permitir, escolha também o brilho.

<figure class="ha-screen"><a href="/static/img/ha-guide/action.png" target="_blank" rel="noopener" aria-label="Ampliar tela: Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo."><img src="/static/img/ha-guide/action.png" alt="Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo." width="953" height="330" loading="lazy" decoding="async"></a><figcaption>Exemplo da ação de ligar luzes; escolha sua lâmpada no campo de alvo. <a class="ext" href="https://www.home-assistant.io/getting-started/automation/" target="_blank" rel="noopener">Tela oficial · Home Assistant</a> <span>Em inglês; os nomes podem variar por versão. Toque para ampliar.</span><a href="/static/img/ha-guide/README.md">Créditos das imagens</a></figcaption></figure>

A captura oficial usa uma área como alvo. Para começar, você pode escolher apenas uma luz.

## 4. Salve e teste

Clique em **Salvar** e dê um nome claro, como “Luz da sala ao anoitecer”. No menu da automação, use **Executar ações** para conferir se a luz acende.

Esse teste verifica a ação, **não o gatilho do pôr do sol**. Para testar a regra completa sem esperar até a noite, crie uma automação temporária com um horário próximo; depois remova-a ou desative-a.

## Defina o que conta como sucesso

Antes de adicionar outras regras, use este pequeno roteiro na sua própria instalação. Ele é uma proposta de teste, não um relato de teste realizado pelo autor.

| Etapa | O que fazer | Resultado que você procura |
|---|---|---|
| Controle básico | Com a luz apagada, ligue e desligue pelo painel. | O aparelho físico acompanha os comandos. |
| Ação isolada | Use **Executar ações** na automação salva. | A luz escolhida acende; outra luz não é acionada por engano. |
| Regra completa | Observe a execução no próximo pôr do sol. | Há uma execução no horário esperado e a luz acende. |
| Uso cotidiano | Depois da execução, desligue a luz pelo controle habitual. | Os moradores continuam conseguindo escolher o estado da luz. |

Anote separadamente “a interface mudou” e “a lâmpada acendeu”. Uma confirmação na tela, sozinha, não demonstra o resultado físico. Se você testar usando uma regra temporária por horário, registre isso: ainda falta observar o gatilho solar original.

## A luz não acendeu: qual etapa falhou?

Comece pelo primeiro teste da tabela que não passou. Não recrie a instalação inteira para corrigir uma automação.

- **Nem o painel controla a luz:** confira alimentação e disponibilidade do aparelho na integração. A regra depende desse controle básico.
- **O painel funciona, mas Executar ações não:** revise o alvo selecionado e abra o rastreamento da execução para localizar o passo com erro.
- **Executar ações funciona, mas não há execução automática:** confira se a automação está habilitada. Execução manual não comprova que o gatilho ocorreu.
- **Executou em horário inesperado:** confira localização e fuso horário da instalação. O cálculo solar depende da localização, não de um horário fixo como 18h.

Abra os **rastreamentos (Traces)** da automação e escolha a execução pelo horário da falha. Eles ajudam a distinguir um gatilho que não ocorreu de uma ação que falhou. Veja a [documentação de diagnóstico](https://www.home-assistant.io/docs/automation/troubleshooting/).

## Escolha a regra pelo problema da sala

O pôr do sol é um ponto de partida previsível, mas não mede a luminosidade dentro da casa. Um cômodo pode escurecer antes por causa de chuva, cortinas ou posição das janelas. Observe primeiro; só depois decida se precisa de um deslocamento de horário ou de um sensor de luminosidade. A [integração Sol](https://www.home-assistant.io/integrations/sun/) explica os cálculos e as opções de gatilho.

Essa regra também não define quando apagar a luz. Combine com os moradores se o desligamento será manual ou se merece uma segunda automação. Mantenha as duas decisões separadas enquanto estiver aprendendo: assim fica mais fácil descobrir qual regra produziu um resultado inesperado.

## Ficha para acompanhar sua instalação

Copie e preencha este registro. Não inclua endereço da casa, senhas ou tokens ao compartilhar.

```text
Data e versão do Home Assistant:
Modelo da luz e integração utilizada:
Nome da automação:
Horário esperado / horário observado:
Controle pelo painel: passou / falhou
Executar ações: passou / falhou
Gatilho observado: solar / horário temporário / ainda não observado
Resultado físico:
Erro no rastreamento (sem dados privados):
Única alteração feita após o teste:
Resultado da nova tentativa:
```

Se pedir ajuda pelo [contato do site](/sobre/#contato-e-correcoes), informe em qual etapa parou. Isso é mais útil para reproduzir o problema do que apenas dizer “a automação não funciona”.

## Funcionou? Pare por aqui por enquanto

Você já tem uma automação útil. Observe o resultado e mantenha seus backups antes de adicionar outras regras. A mesma ideia poderá usar um sensor de movimento como gatilho depois.

[Quando quiser, conheça integrações e Apps](/apps-integracoes/).

Fontes: [primeiras automações](https://www.home-assistant.io/getting-started/automation/) e [como testar](https://www.home-assistant.io/docs/automation/testing/).
