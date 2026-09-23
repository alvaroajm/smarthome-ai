# Cenas de iluminação (galeria interativa)

Imagens (`static/img/scenes/*.webp`) e vídeos (`static/video/scenes/*.mp4`, sem áudio, 15 s, H.264)
gerados por IA em 2026 para o SmartHome-AI, a pedido do autor, e usados na seção
"Cenas de luz" da página inicial e do guia `/home-assistant/`. Não retratam produtos
reais nem a casa do autor; as cenas (RGB, branco dia, leitura, manhã, pôr do sol, luz noturna)
são simuladas no navegador com filtros CSS sobre a imagem e o vídeo.

| arquivo | vídeo | dimensões |
|---|---|---|
| game-neon.webp | game-neon.mp4 | 1280×720 |
| corrida.webp | corrida.mp4 | 1280×720 |
| quatro-ambientes.webp | quatro-ambientes.mp4 | 1280×1280 / 944×944 |
| cidade-noite.webp | cidade-noite.mp4 | 1280×1280 / 944×944 |
| dia-tarde-noite.webp | dia-tarde-noite.mp4 | 1280×720 |
| lounge.webp | lounge.mp4 | 1184×768 |

Os vídeos são carregados só quando o leitor passa o mouse ou toca no cartão
(`preload="none"`, `muted`, `playsinline`, `loop`).
