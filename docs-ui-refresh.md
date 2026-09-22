# Revisão para iniciantes — 22/09/2026

## Avaliação e mudanças

A página inicial exibia 18 guias, 12 dispositivos e 20 links simultaneamente. Isso dificultava identificar por onde começar. Agora a trilha de três passos vem antes da demonstração, seis guias são destacados e os dispositivos começam por seis exemplos. A biblioteca completa permanece disponível. Diretório e galerias abrem sob demanda.

Títulos e descrições dos 18 guias foram encurtados. Os textos de Comece aqui (PT/EN) e O que é Home Assistant foram reescritos para iniciantes, com a instalação e os conceitos conferidos na documentação oficial. Os demais tutoriais técnicos mantêm seu conteúdo detalhado.

A identidade verde/dourada, a planta interativa, as marcas e as páginas existentes foram preservadas. Ajustados espaçamento, tamanho dos alvos de toque e largura de leitura.

## Imagens

Ferramenta: geração de imagens integrada do Codex. Exportação para WebP/PNG/ICO com Pillow; as imagens originais geradas permanecem no diretório da ferramenta.

- `static/img/home-comfort.webp`: sala acolhedora com luminária, sensor e caixa de som. Prompt: “Use case: photorealistic-natural. Asset type: editorial hero photograph for a beginner smart home website. Wide landscape 3:2. A welcoming contemporary Brazilian living room at dusk, warm floor lamp glowing beside a cream sofa, muted forest-green cushions, natural oak furniture, a discreet small white motion sensor on the wall and a smart speaker on a side table. Warm natural realistic lighting, tasteful lived-in interior, uncluttered composition, no people, no logos, no text, no holographic interfaces. Show everyday comfort, not futuristic technology.”
- `static/img/smart-entry.webp`: fechadura ilustrativa, sem indicação de marca ou modelo. Prompt: “Use case: photorealistic-natural. Asset type: editorial illustration photo for a beginner smart home website. Landscape 3:2 close view of a contemporary oak entrance door with a realistic generic matte black smart lever lock with small keypad, inside a welcoming home, subtle white two-part door contact sensor on frame, a green plant and warm light in background. Soft daylight, restrained editorial architectural photography, realistic proportions. No branding, no text or floating graphics, no people. Focus on the lock and everyday home context.”
- `static/img/favicon-sa.ico`, `favicon-sa-32.png`, `favicon-sa-192.png`, `apple-touch-icon-sa.png`: adaptação da imagem IMG_3207.JPG fornecida pelo usuário. Prompt: “Use case: background-extraction. Edit target: attached SmartHome-AI brand image. Extract ONLY the central SA monogram, retaining its exact green S, gold A, small red roof swoosh and gold window. Remove all surrounding writing, tagline, URL, decorative arc, rays and star. Place the preserved monogram centered and large on a clean pure white square background, with only 5 percent safe margin. This is a browser favicon: crisp recognizable silhouette. No new details, no text beyond the original SA initials. Preserve the original letterforms.” O resultado gerado tem transparência, preservada na exportação. Ícone ICO inclui 16, 32 e 48 pixels; PNG de 32 e 192 pixels; Apple Touch Icon de 180 pixels. URLs recebem hash para atualização do cache; também há `/favicon.ico`.

## Validação

- Gerador Python e verificador de 29 páginas: links internos e templates válidos.
- Sintaxe JavaScript validada.
- Navegador integrado: larguras de 390 e 1440 pixels sem overflow horizontal; inspeção visual da home e guia introdutório.
- Busca por Zigbee, menu móvel, filtro de sensores, expansão dos 12 dispositivos, tema escuro e cena Boa noite exercitados.
- Chrome e Edge não foram executados separadamente; ícones usam os formatos PNG e ICO compatíveis com ambos.

## Referências dos guias revisados

- https://www.home-assistant.io/installation/
- https://www.home-assistant.io/getting-started/concepts-terminology/
- https://www.home-assistant.io/getting-started/automation/
