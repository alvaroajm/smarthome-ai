# Revisão para AdSense — 20/10/2026

## Diagnóstico e limites

O aviso recebido é “Conteúdo de baixo valor”. Ele não identifica páginas específicas. A análise da home pública e dos arquivos locais sugere oportunidades editoriais; não comprova qual fator motivou a decisão do Google. Não houve acesso ao painel AdSense, Search Console ou Analytics nesta revisão.

O site tem navegação, fontes, privacidade e contato. Há 30 arquivos de conteúdo em português e 4 em inglês. Páginas de navegação curtas podem cumprir bem sua função; quantidade de palavras, por si só, não mede utilidade nem garante aprovação.

## Evidências e prioridades

| Evidência | Ação |
|---|---|
| `/zigbee2mqtt/` apresenta uma decisão de migração em poucos parágrafos, sem um caso concreto comparado. | Documentar um modelo efetivamente usado: função desejada, suporte nas duas integrações, custos de migração e resultado. Não migrar equipamentos apenas para produzir conteúdo. |
| `/matter-thread/` explica conceitos, mas não acompanha uma instalação real. | Acrescentar um exemplo reproduzível quando houver equipamento disponível; ou manter a proposta explicitamente introdutória. |
| Guias usam imagens oficiais creditadas. | Preservar créditos e acrescentar capturas próprias quando houver teste documentado, explicando o que o leitor deve observar. |
| “Sobre” generalizava que as configurações publicadas rodavam numa casa real. | Texto ajustado para distinguir orientação documental de relatos de experiência. Incluído apenas o equipamento confirmado pelo autor. |
| Autor e datas estavam nos metadados, mas não no cabeçalho visível dos artigos. | Corrigido no template, em PT e EN. Datas existentes preservadas; revisão marcada apenas nos textos alterados. |

## Alterações preparadas

- Autor com link para a página Sobre, publicação e atualização visíveis.
- Primeira automação: roteiro de aceitação, diagnóstico por etapa, limites do gatilho solar e ficha de registro reutilizável. É um roteiro proposto, não um teste alegadamente realizado.
- Sobre em PT/EN: distinção entre fontes oficiais e experiência, histórico público de alterações e conjunto residencial informado pelo autor: mini-PC Ryzen 7 com HAOS, interruptores Zemismart Zigbee e luzes Philips Hue Zigbee.
- Site regenerado em `dist/`.

O autor esclareceu que possui vários Echo Dot Max e um Echo Studio Max na sala; são equipamentos distintos, não uma substituição do nome anterior. Confirmou a integração da Alexa com o Home Assistant pelo Nabu Casa e duas Apple TV 4K usadas como centrais do Apple HomeKit. Nomes comerciais dos Echo não verificados; quantidade exata e localização dos Echo Dot Max e geração das Apple TV não informadas. Não inferir conexão direta dos dispositivos Zigbee aos Echo, suporte a Thread ou o caminho de integração entre Home Assistant e HomeKit.

Câmeras: o autor relatou o fluxo câmeras → Home Assistant → Scrypted → HomeKit Secure Video. Registrado como relato da instalação, não como procedimento técnico validado. Equipamentos confirmados pelo autor: Tapo TC70, DVR Intelbras (modelo não informado) e Intelbras iM4. Confirmar modelo do DVR, origem de vídeo configurada no Scrypted e plugins utilizados antes de elaborar um tutorial; não inferir que Scrypted exige Home Assistant como intermediário.

## Trabalho editorial antes de reenviar

Referência adicional enviada pelo autor: tomada Zemismart, anúncio https://a.aliexpress.com/_mNfZFZN . O link não pôde ser consultado nesta sessão. O autor confirmou que a tomada está instalada na sala e controla as luzes desse ambiente, e que utiliza Philips Hue na sala e na suíte master. O acionamento das luzes ocorre pelo aplicativo Casa da Apple (HomeKit) no celular, por voz pela Alexa e diretamente pelo Home Assistant. Não foi confirmada a topologia das integrações, se a tomada controla as próprias Hue ou outras luzes, nem a existência de regras automáticas por horário ou sensor. Modelo, variante e protocolo da tomada ainda precisam de confirmação; não substituir a identificação dos interruptores nem atribuir especificações à tomada com base apenas na marca. O segundo link enviado é um redirecionamento publicitário do Google, sem identificação legível do produto na URL.

1. Completar um caso real com modelos exatos, rádio/coordenador, integração (ZHA, Zigbee2MQTT ou outra), versões, problema, configuração, falhas e resultado observado. Não inventar medições, fotos ou períodos de uso.
2. Revisar os guias prioritários pela tarefa do leitor: ele consegue executar, verificar o resultado e diagnosticar uma falha? Consolidar páginas sobrepostas quando isso melhorar a navegação; não esconder conteúdo apenas para a avaliação.
3. Depois de publicar, conferir as URLs públicas e a navegação móvel. Verificar no Search Console rastreamento, indexação e eventuais ações manuais; no Analytics, observar quais guias atraem leitura e retorno. Não foram consultadas métricas nesta revisão.
4. Reenviar pelo AdSense depois de melhorias substanciais estarem disponíveis. Não há prazo, quantidade de artigos ou volume de tráfego prometido aqui como garantia de aprovação.

## Fontes

- https://support.google.com/adsense/answer/7299563 — páginas prontas para AdSense, conteúdo original e navegação.
- https://support.google.com/adsense/answer/9724 — requisitos de participação.
- https://support.google.com/adsense/answer/10502938 — políticas para publishers.
- https://developers.google.com/search/docs/essentials/spam-policies — políticas de spam da Pesquisa; não equivalem a um diagnóstico da rejeição AdSense deste site.

## Publicação e sincronização

Mudanças somente locais nesta etapa, sem commit, push ou alteração da Cloudflare. A sincronização diária preserva essas edições e não aplicará atualizações remotas enquanto a árvore estiver modificada. A publicação usa o fluxo existente de commit/push da `main`, com `dist/` versionado.

## Fotografias recebidas

Recebidos dez anexos da sala. Selecionadas as fotos 2, 6 e 3 para galeria na página Sobre em PT/EN, com legendas descritivas, dimensões explícitas e carregamento tardio. Originais copiados sem edição para `static/img/casa-do-autor/`. Fotografias não comprovam modelos, protocolos ou resultados de automações.

Tiras de LED: o autor confirmou controle pelo aplicativo WLED via Wi-Fi. Modelo do controlador e eventual integração do WLED com Home Assistant não foram informados.

Acrescentadas à página Minha instalação as fotos dos interruptores Zemismart Zigbee e do controle Broadlink IR/RF. Modelo e aparelhos controlados pelo Broadlink ainda não informados.
