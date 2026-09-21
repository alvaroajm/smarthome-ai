# Imagens, tipografia e fontes — redesign SmartHome-AI

Atualização de 21/09/2026. A apresentação está nas homes PT/EN; tipografia, navegação e busca são compartilhadas com os guias. O gerador continua em `build.py`, com os componentes editoriais em `visual_content.py`. Gere `dist/` antes de publicar.

## Imagens fornecidas pelo autor

Arquivos copiados sem alteração dos anexos: `author-original.jpg` (IMG_2923), `author-seal.jpg` (IMG_2992), `radapps-brand.jpg` (IMG_3128), `smarthome-brand.jpg` (IMG_3207) e `smarthome-banner.jpg` (IMG_3209). IMG_3208 é uma alternativa de marca equivalente; foi usada a IMG_3207. As proporções e os recortes de apresentação são controlados por CSS. Links dos brasões: alvaro-menezes.com e radapps.app.

## Ilustrações originais

- `static/img/smart-room.svg`: ilustração da sala mantida no acervo. A home passou a usar a planta 3D enviada pelo autor.
- `static/img/devices/*.svg`: 12 ilustrações genéricas. Fonte editável em `scripts/draw-devices.py`. Não são imagens de modelos comerciais específicos, nem desenhos de instalação elétrica.

## Fotografias de produtos atuais

Atualizadas em 21/09/2026. Arquivos locais, sem retoque; a apresentação responsiva é feita por CSS. As legendas identificam o modelo e remetem à fonte. Imagens de divulgação dos fabricantes não são apresentadas como Creative Commons nem como fotografias do autor. A galeria tem finalidade editorial, sem preços, compra, patrocínio ou promessa de compatibilidade.

| Arquivo | Modelo | Fonte editorial |
|---|---|---|
| hue-liane-2026.jpg | Philips Hue Liane 360°, anúncio de 03/09/2026 | https://www.signify.com/global/our-company/news/press-releases/2026/20260903-philips-hue-expands-on-smart-lighting-with-ai-immersive-entertainment-and-design |
| echo-dot-max-2025.jpg | Echo Dot Max, geração 2025 | https://www.aboutamazon.com.br/noticias/dispositivos/echo-dot-max-chega-ao-brasil-com-novo-design-e-audio-premium |
| shelly-plug-gen4.png | Shelly Plug US Gen4, padrão EUA 120 V explicitado | https://us.shelly.com/products/shelly-plug-us-gen4-black |
| raspberry-pi-5-case.jpg | Raspberry Pi 5 na case oficial, com M.2 HAT+ Compact | https://www.raspberrypi.com/news/m-2-hat-compact-on-sale-now-at-15/ |
| modern-mini-pc.png | ASUS NUC 16 Pro, exemplo de formato de mini-PC moderno | https://www.asus.com/displays-desktops/nucs/nuc-mini-pcs/asus-nuc-16-pro/ |

As antigas fotos `hue-photo.jpg` (Sho Hashimoto, CC BY 2.0), `echo-photo.jpg` (Samuel Wiki, CC0) e `plug-photo.jpg` (TBWABusted, CC BY 2.0) permanecem nos arquivos históricos; não são mais exibidas.

## Planta interativa

`static/img/connected-home-plan.jpg` é uma cópia inalterada da imagem IMG_3211.JPG fornecida pelo usuário. `connected_home.py` registra os 16 polígonos e nomes de ambientes nas coordenadas originais (1136 × 1744). SVG e CSS simulam a iluminação; a imagem original não é redesenhada. São zonas didáticas, sem cálculo luminotécnico. A demonstração não se comunica com dispositivos reais.

Cliques nos cômodos e botões da lista compartilham um único estado. Enter/espaço acionam os marcadores; controles equivalentes de pelo menos 44 px atendem às áreas pequenas no celular. A ampliação é contida na planta. Preferências de luz ficam em `sha-house-lights-v1`, com validação, e persistem em PT/EN. O site continua exibindo conteúdo sem JavaScript, com controles desativados e explicação.

## CasaOS e umbrelOS

Bloco próprio em PT/EN na home e links para CasaOS, seu GitHub, umbrelOS, Umbrel App Store e ZimaOS. Guia `/casaos-umbrel/` revisto: CasaOS é um painel sobre Linux; umbrelOS é um sistema completo com licença PolyForm Noncommercial. A informação de beta 2.0 traz data de consulta. O texto sobre Container agora reconhece os backups do Home Assistant e separa a manutenção dos demais containers.

## Fontes

### Ícones oficiais dos projetos

`static/img/brands/` contém cópias locais, sem redesenho ou recoloração, dos ícones publicados pelos próprios projetos. `sources.json` registra a página oficial, o URL de origem, a data de consulta e o SHA-256 de cada arquivo. São marcas de seus respectivos titulares, usadas para identificar os destinos dos links; não indicam parceria ou endosso.

`brand_icons.py` centraliza a associação entre destinos e marcas. A aplicação acontece durante a geração do HTML, nos 20 cartões de recursos, nos cartões CasaOS/umbrelOS, nos guias e nos links do rodapé, em PT/EN. Links de comparação CasaOS/umbrelOS exibem os dois ícones. GitHub e Wikipedia usam suas próprias marcas, identificando o destino. Links com fotografias ou ícones próprios não recebem imagens duplicadas.

Os arquivos mantêm suas cores e proporções e usam fundo claro para legibilidade no tema escuro. Ícones ao lado de texto são decorativos (`alt=""` e `aria-hidden`); nomes e destinos dos links são preservados. URLs locais incluem hash de conteúdo. Não há dependência de CDN ou de JavaScript para exibir as marcas.

Newsreader 500 para títulos: https://github.com/google/fonts/tree/main/ofl/newsreader — SIL Open Font License, incluída em `static/fonts/newsreader-OFL.txt`. Arquivo obtido pelo CSS oficial Google Fonts. Inter e JetBrains Mono locais já existentes foram preservadas. Nenhuma chamada ao Google Fonts é necessária na navegação.

## Referências de conteúdo e links

Links verificados nas páginas dos projetos, não em preços ou recomendações de varejo:

- https://www.home-assistant.io/ e https://www.home-assistant.io/integrations/
- https://www.home-assistant.io/integrations/matter/ — diferença entre camada Matter e rede Thread/Wi-Fi.
- https://www.home-assistant.io/integrations/zha/ e https://www.zigbee2mqtt.io/ — integração e compatibilidade por modelo.
- https://www.nabucasa.com/ e https://www.home-assistant.io/voice_control/ — Cloud opcional, Alexa e Assist.
- https://esphome.io/ e https://devices.esphome.io/ — sensores, telas e microcontroladores.
- https://kno.wled.ge/ e https://install.wled.me/ — documentação e instalador WLED.
- https://homeassistantbrasil.com.br/, https://community.home-assistant.io/ e https://github.com/home-assistant — comunidades e código-fonte.
- https://en.wikipedia.org/wiki/Home_Assistant — link enciclopédico solicitado pelo autor, não utilizado como base das afirmações técnicas.

## Verificação

Use `python3 build.py` e `python3 scripts/check.py`. A inspeção no navegador deve incluir filtros, cenas, busca por teclado e toque, idiomas, temas, navegação de artigos, imagens e larguras de 320 a 1440 px. A pasta `dist/` é versionada e publicada automaticamente pelo Cloudflare ao enviar `main`. Confira a planta em 320–1440 px, mouse/toque/teclado, PT/EN, recarga, zoom, cenas e os estados sincronizados. A emulação Chromium não substitui testes físicos em iPhone/Safari ou Android.

### Validação da planta (21/09/2026)

Chromium desktop/toque emulado em 1440, 1024, 768, 390 e 320 px, PT/EN e claro/escuro: 16 zonas acionadas separadamente, sincronização bidirecional, Enter/espaço, quatro cenas, zoom sem transbordamento, recarga, idioma, armazenamento inválido, busca, filtros e carregamento das imagens. Conteúdo preservado com JS desligado. Sem erros JavaScript. Testes físicos de VoiceOver, Safari/iPhone e Android não executados.
