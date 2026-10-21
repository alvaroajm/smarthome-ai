---
level: avancado
title: Converse com sua casa
slug: claude-mcp
description: Claude e Home Assistant com MCP: conector remoto, autenticação OAuth, diferença entre cliente e servidor e roteiro para verificar a conexão.
category: IA & agentes
icon: bot
order: 114
featured: true
reading: 6 min de leitura
date: 2026-09-21
updated: 2026-10-21
tags: [MCP, Claude, IA, Assist, Automação]
---

Você pode pedir a um assistente de IA que consulte a casa ou use ferramentas conectadas a ela. **MCP é o protocolo dessa conexão; não garante que qualquer pedido seja possível.** Histórico, criação de automações e edição de arquivos dependem das ferramentas disponíveis.

Este guia foi revisto pelas fontes oficiais em **21/10/2026**. É orientação documental e um roteiro de verificação, não um relato de conexão testada na minha casa.

## Cliente e servidor: duas direções diferentes

- O **Model Context Protocol Server** do Home Assistant oferece ferramentas para um cliente como Claude. É a integração relevante para conectar Claude à casa.
- A integração **Model Context Protocol**, sem “Server”, faz o caminho inverso: o Home Assistant consome ferramentas de outro servidor MCP para seus agentes de conversação. Adicioná-la não conecta o Claude à sua casa.

Fonte: [integração cliente MCP do Home Assistant](https://www.home-assistant.io/integrations/mcp/).

## Prepare o endereço do servidor

Na documentação atual, a URL é obtida em **Configurações → Sistema → IA**. Outra entrada de configuração é **Dispositivos e serviços → Adicionar integração → Model Context Protocol Server**. Use o endereço fornecido pela sua instalação.

Revise as APIs e entidades disponíveis: instalações novas podem expor todas as APIs LLM e exigir administrador por padrão. Instalações antigas podem manter escolhas anteriores. Não presuma um modo somente leitura nem acesso restrito apenas por ter configurado o Assist.

O servidor suporta **OAuth 2.0 com PKCE**. O fluxo oficial do Claude usa autenticação no Home Assistant; não exige copiar um token de longa duração para um JSON. Os nomes dos menus podem mudar entre versões.

Fonte: [servidor MCP e configuração de clientes](https://www.home-assistant.io/integrations/mcp_server/).

## Claude: conector remoto e servidor local são diferentes

Um **conector remoto** é acessado pela infraestrutura da Anthropic, inclusive quando você usa o aplicativo Desktop. Um endereço acessível somente na sua rede, como `homeassistant.local`, não fica acessível ao conector só porque o Mac está nessa rede.

No Claude, procure **Customize → Connectors → Add → Custom → Web**; em algumas versões aparece “Add custom connector”. Informe o nome e a URL MCP, revise a autenticação detectada, conecte e entre na sua instância do Home Assistant. A disponibilidade e as etapas dependem do plano e das regras da organização.

Já um **servidor MCP local** do Claude Desktop é um processo executado no computador. Não é o mesmo mecanismo do conector remoto. Uma configuração de ponte local precisa corresponder ao transporte, à autenticação e à versão do programa escolhido; não há aqui um JSON genérico prometido como pronto para uso.

Fontes: [conectores remotos e requisitos de rede](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) e [servidores locais no Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

## Verifique uma etapa de cada vez

O roteiro abaixo é uma proposta de teste. Registre o resultado real, inclusive falhas; não trate uma resposta convincente do modelo como confirmação de execução.

| Etapa | O que verificar |
|---|---|
| Identificar a casa | Confirme instância e conta antes de autorizar a conexão. |
| Conectar | O cliente deve concluir a autenticação e apresentar as ferramentas. Anote o erro exato se isso não acontecer. |
| Consultar | Peça o estado de uma luz conhecida e compare com o painel do Home Assistant. Não peça histórico antes de confirmar que existe ferramenta para isso. |
| Agir, se desejado | Escolha uma luz de teste, peça uma única mudança e confira o estado no painel e no ambiente. Evite comandos amplos como “desligue tudo”. |
| Documentar | Anote versões, cliente, tipo de conexão, ferramenta chamada, estado anterior e resultado observado. Não publique credenciais. |

**Se a conexão falhar:** separe alcance de rede, autenticação e ferramenta ausente. Um servidor inacessível da nuvem não é o mesmo problema que uma luz não exposta. Compare o erro com a seção de diagnóstico da documentação oficial antes de trocar configurações.

## Editar YAML é outra tarefa

Consultar ferramentas MCP não significa acesso automático a `/config`, ao Git ou ao sistema de arquivos. Se o objetivo for preparar uma automação, peça primeiro uma proposta de YAML, revise entidades e condições e use uma cópia da configuração. O [guia de comandos do HAOS](/comandos-haos/) explica a validação; a [primeira automação](/primeira-automacao/) segue pelas telas.

Também não basta executar o modelo localmente para garantir que todo o áudio permaneça em casa: reconhecimento de voz, modelo, síntese e serviços acionados precisam ser avaliados separadamente. Escolha a arquitetura pelo que cada componente realmente faz.

Para decidir o próximo passo, use o [guia do Home Assistant](/home-assistant/) e a [documentação do Assist](https://www.home-assistant.io/voice_control/). Relatos futuros da instalação devem incluir as configurações e os resultados efetivamente observados.
