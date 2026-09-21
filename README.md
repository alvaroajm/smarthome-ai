# SmartHome-AI

Site estático sobre casa inteligente local e código aberto — Home Assistant, ESPHome, ESP32,
Zigbee2MQTT, ZHA, Matter over Thread, Matter over Wi-Fi, Apple HomeKit, Scrypted, Raspberry Pi e mini-PCs.

**Produção:** https://smarthome-ai.com

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

## Licença

Código do gerador: MIT. Conteúdo dos artigos: © SmartHome-AI.
