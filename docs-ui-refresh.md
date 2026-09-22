# Revisão para iniciantes — 22/09/2026

## Avaliação e mudanças

A página inicial apresentava muitos dispositivos e assuntos técnicos antes de explicar a casa inteligente. A nova sequência começa pelo conceito, compara seis plataformas e destaca o Home Assistant. Depois apresenta HAOS, Zigbee, Thread, Matter, ZBT-2 + ZHA e uma automação pelo editor visual.

A biblioteca e os botões Anterior/Próximo acompanham a mesma trilha. Integrações, Apps, HACS e câmeras entram depois da primeira automação. Alternativas de instalação, Proxmox, Zigbee2MQTT, servidores e IA ficam no aprofundamento. Conteúdos adicionais da home usam elementos details nativos; não foi acrescentado JavaScript.

Guias básicos e FAQ foram reescritos com frases curtas, instruções gráficas e fontes oficiais. Corrigidas generalizações sobre microSD, funcionamento sem internet e compatibilidade Matter. A home, o roteiro e o FAQ em inglês também acompanham a mudança; os tutoriais detalhados continuam identificados como português.

A identidade verde/dourada, o favicon baseado na imagem enviada, a planta interativa e as páginas existentes foram preservados. A demonstração e os dispositivos abrem sob demanda. Ajustados espaçamento, alvos de toque, hierarquia de títulos e largura de leitura.

## Imagens

Ferramenta: geração de imagens integrada do Codex. Exportação para WebP/PNG/ICO com Pillow; as imagens originais geradas permanecem no diretório da ferramenta.

- `static/img/home-comfort.webp`: sala acolhedora com luminária, sensor e caixa de som. Prompt: “Use case: photorealistic-natural. Asset type: editorial hero photograph for a beginner smart home website. Wide landscape 3:2. A welcoming contemporary Brazilian living room at dusk, warm floor lamp glowing beside a cream sofa, muted forest-green cushions, natural oak furniture, a discreet small white motion sensor on the wall and a smart speaker on a side table. Warm natural realistic lighting, tasteful lived-in interior, uncluttered composition, no people, no logos, no text, no holographic interfaces. Show everyday comfort, not futuristic technology.”
- `static/img/smart-entry.webp`: fechadura ilustrativa, sem indicação de marca ou modelo. Prompt: “Use case: photorealistic-natural. Asset type: editorial illustration photo for a beginner smart home website. Landscape 3:2 close view of a contemporary oak entrance door with a realistic generic matte black smart lever lock with small keypad, inside a welcoming home, subtle white two-part door contact sensor on frame, a green plant and warm light in background. Soft daylight, restrained editorial architectural photography, realistic proportions. No branding, no text or floating graphics, no people. Focus on the lock and everyday home context.”
- `static/img/favicon-sa.ico`, `favicon-sa-32.png`, `favicon-sa-192.png`, `apple-touch-icon-sa.png`: adaptação da imagem IMG_3207.JPG fornecida pelo usuário. Prompt: “Use case: background-extraction. Edit target: attached SmartHome-AI brand image. Extract ONLY the central SA monogram, retaining its exact green S, gold A, small red roof swoosh and gold window. Remove all surrounding writing, tagline, URL, decorative arc, rays and star. Place the preserved monogram centered and large on a clean pure white square background, with only 5 percent safe margin. This is a browser favicon: crisp recognizable silhouette. No new details, no text beyond the original SA initials. Preserve the original letterforms.” O resultado gerado tem transparência, preservada na exportação. Ícone ICO inclui 16, 32 e 48 pixels; PNG de 32 e 192 pixels; Apple Touch Icon de 180 pixels. URLs recebem hash para atualização do cache; também há `/favicon.ico`.

## Validação

- Build Python e verificador de 34 páginas HTML aprovados.
- Auditoria de imagens locais, IDs duplicados e links com âncoras aprovada.
- Sintaxe do JavaScript existente válida; nenhum bloco de código na trilha básica.
- Navegador integrado: desktop de 1440 px, celular de 390 px e menu em 320 px, sem overflow nas telas verificadas.
- Busca pelo novo guia de primeira automação, menu móvel, temas e separação da biblioteca conferidos.
- Chrome e Edge não foram executados separadamente; favicon usa PNG e ICO compatíveis com ambos.

## Telas oficiais

Dez imagens da documentação pública do Home Assistant e Nabu Casa ilustram painel, primeiro acesso, Imager, integração ZHA, assistente ZBT-2, automações, integrações e Apps. Cada imagem tem legenda, link para ampliar e fonte. Não contêm dados da instalação particular do autor. Créditos, URLs e licença da documentação Home Assistant estão em `static/img/ha-guide/`.

A captura do Imager usa um quadro estático da animação oficial, reduzindo o arquivo de cerca de 3 MB para 200 KB e evitando movimento contínuo. As telas estão em inglês, com instruções em português e aviso de variação entre versões.

## Referências dos guias revisados

- https://www.home-assistant.io/installation/
- https://www.home-assistant.io/getting-started/concepts-terminology/
- https://www.home-assistant.io/getting-started/automation/
