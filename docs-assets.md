# Imagens, tipografia e fontes — redesign SmartHome-AI

Atualização de 21/09/2026. A apresentação está nas homes PT/EN; tipografia, navegação e busca são compartilhadas com os guias. O gerador continua em `build.py`, com os componentes editoriais em `visual_content.py`. Gere `dist/` antes de publicar.

## Imagens fornecidas pelo autor

Arquivos copiados sem alteração dos anexos: `author-original.jpg` (IMG_2923), `author-seal.jpg` (IMG_2992), `radapps-brand.jpg` (IMG_3128), `smarthome-brand.jpg` (IMG_3207) e `smarthome-banner.jpg` (IMG_3209). IMG_3208 é uma alternativa de marca equivalente; foi usada a IMG_3207. As proporções e os recortes de apresentação são controlados por CSS. Links dos brasões: alvaro-menezes.com e radapps.app.

## Ilustrações originais

- `static/img/smart-room.svg`: sala em perspectiva, com luminária, sofá, TV, painel, fechadura e sensor. As três cenas são demonstrações visuais; não se conectam a uma instalação de Home Assistant.
- `static/img/devices/*.svg`: 12 ilustrações genéricas. Fonte editável em `scripts/draw-devices.py`. Não são imagens de modelos comerciais específicos, nem desenhos de instalação elétrica.

## Fotografias licenciadas

Arquivos originais preservados; enquadramento responsivo com CSS, sem retoque. Autoria, link da fonte e licença estão junto a cada foto no site.

| Arquivo | Fotógrafo | Fonte | Licença |
|---|---|---|---|
| hue-photo.jpg | Sho Hashimoto | https://commons.wikimedia.org/wiki/File:Philips_Hue_hub_and_2_bulbs.jpg | https://creativecommons.org/licenses/by/2.0/ |
| echo-photo.jpg | Samuel Wiki | https://commons.wikimedia.org/wiki/File:Echo_Dot_(3rd_Gen)_02.jpg | https://creativecommons.org/publicdomain/zero/1.0/ |
| plug-photo.jpg | TBWABusted | https://commons.wikimedia.org/wiki/File:Smart-plug.jpg | https://creativecommons.org/licenses/by/2.0/ |

São exemplos visuais de gerações distintas, sem recomendação de compra, patrocínio ou garantia de compatibilidade. As imagens são hospedadas no próprio site e carregadas sob demanda.

## Fontes

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

Use `python3 build.py` e `python3 scripts/check.py`. A inspeção no navegador deve incluir filtros, cenas, busca por teclado e toque, idiomas, temas, navegação de artigos, imagens e larguras de 320 a 1440 px. A pasta `dist/` é versionada e publicada automaticamente pelo Cloudflare ao enviar `main`; esta alteração deve ser revisada antes desse envio.
