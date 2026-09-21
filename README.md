# SmartHome-AI

Site estático sobre casa inteligente local e código aberto — Home Assistant, ESPHome, ESP32,
Zigbee2MQTT, ZHA, Matter over Thread, Matter over Wi-Fi, Apple HomeKit, Scrypted, Raspberry Pi e mini-PCs.

**Produção:** https://smarthome-ai.com · https://www.smarthome-ai.com
**Pré-visualização Cloudflare:** https://smarthome-ai.pages.dev
**Repositório:** https://github.com/alvaroajm/smarthome-ai

> O projeto no Cloudflare Pages está conectado a este repositório: **cada `git push` na branch `main`
> publica o site automaticamente** (sem build na Cloudflare — a pasta `dist/` já vem pronta).
> Fluxo de atualização: editar `content/*.md` → `python3 build.py` → `git commit` → `git push`.

---

## Como funciona

```
content/*.md      → conteúdo (Markdown com cabeçalho de metadados)
templates/*.html  → layout (base, home, artigo)
static/           → CSS, JS e imagens
build.py          → gerador: lê o conteúdo, aplica os templates e escreve dist/
serve.py          → servidor local de pré-visualização
scripts/          → utilitários (verificação e criação de artigos)
dist/             → SITE GERADO — é esta pasta que o Cloudflare publica
```

Sem frameworks, sem Node.js e com **uma única dependência** (`Markdown`).

## Uso no dia a dia

```bash
# 1. dependência (uma vez)
pip3 install -r requirements.txt

# 2. gerar o site
python3 build.py            # ou: python3 build.py --clean

# 3. pré-visualizar em http://localhost:8000
python3 serve.py            # python3 serve.py --watch regera a cada requisição

# 4. verificar links internos e templates
python3 scripts/check.py

# 5. criar um novo guia
python3 scripts/novo-artigo.py "Como integrar meu ar-condicionado"
```

### Cabeçalho de um artigo

```yaml
---
title: Título do guia
slug: url-do-guia          # vira /url-do-guia/
description: Frase usada no card, no Google e nas redes sociais.
category: Protocolos
icon: mesh                 # hub, chip, mesh, thread, apple, camera, server, rocket, help, wifi, book
order: 5                   # ordem na listagem
featured: true             # aparece como card na home
section: artigo            # "artigo" (entra na lista) ou "pagina"
reading: 10 min de leitura
date: 2026-09-21
tags: [Zigbee, MQTT]
---
```

Recursos de escrita disponíveis: tabelas, blocos de código com botão de copiar, sumário automático
(gerado dos `##`) e caixas de destaque:

```markdown
!!! dica "Título"
    Texto da dica.      (variantes: nota, atencao)
```

---

## Publicação

### 1. GitHub

```bash
git init -b main                       # já feito
git add -A && git commit -m "mensagem"
git remote add origin https://github.com/<SEU-USUARIO>/smarthome-ai.git
git push -u origin main
```

### 2. Cloudflare Pages

No painel da Cloudflare: **Workers & Pages → Create → Pages → Connect to Git**, escolha este repositório e configure:

| Campo | Valor |
|---|---|
| Framework preset | **None** |
| Build command | *(deixe vazio)* |
| Build output directory | `dist` |

Como a pasta `dist/` é versionada no repositório, **não é necessário rodar build na Cloudflare** — cada
`git push` publica o site em segundos.

> **Alternativa** (não versionar `dist/`): acrescente `dist/` ao `.gitignore` e configure
> Build command: `pip install -r requirements.txt && python build.py` · Output: `dist`.

### 3. Domínio smarthome-ai.com

1. No projeto do Pages: **Custom domains → Set up a custom domain → `smarthome-ai.com`**
2. Repita para `www.smarthome-ai.com`
3. Se o domínio já está na Cloudflare, os registros são criados automaticamente. Se estiver em outro
   registrador, aponte os *nameservers* para a Cloudflare ou crie um `CNAME` para o domínio `*.pages.dev` do projeto.
4. Em **SSL/TLS**, use o modo **Full (strict)** e ative *Always Use HTTPS*.

Os arquivos `_headers` (cabeçalhos de segurança e cache) e `_redirects` já são copiados para `dist/`
e lidos automaticamente pelo Cloudflare Pages.

---

## IndexNow (Bing, Yandex, Seznam)

A chave fica em `static/98575e0ecd5320e9a56c0a1e956b825d.txt` e é publicada em `https://smarthome-ai.com/98575e0ecd5320e9a56c0a1e956b825d.txt`.
Para avisar os buscadores depois de publicar novidades:

```bash
curl -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json' \
  -d '{"host":"smarthome-ai.com","key":"98575e0ecd5320e9a56c0a1e956b825d",
       "keyLocation":"https://smarthome-ai.com/98575e0ecd5320e9a56c0a1e956b825d.txt",
       "urlList":["https://smarthome-ai.com/","https://smarthome-ai.com/instalar-haos/"]}'
```

O Google não usa IndexNow — para ele, use o Search Console.

## Licença

Código do gerador: MIT. Conteúdo dos artigos: © SmartHome-AI.

## Redesign visual (setembro de 2026)

As homes PT/EN incluem uma sala SVG interativa, um catálogo de 12 tipos de dispositivos,
três fotografias com crédito e 16 links filtráveis. As cenas são apenas demonstrações visuais.
O conteúdo desses componentes está em `visual_content.py`; os layouts estão em `templates/home.*.html`.
Ilustrações dos gadgets: `python3 scripts/draw-devices.py`. Fontes, autoria e licenças: `docs-assets.md`.

Newsreader e Inter são servidas localmente. O tema claro é o padrão; uma preferência anterior
é mantida. Busca com foco contido no diálogo, fechamento por botão/Esc e navegação por teclado.
Todas as cartas e links estão no HTML, inclusive sem JavaScript.
