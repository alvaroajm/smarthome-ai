"""Cenas de iluminação RGBCCT, home cinema e Music Assistant (galeria interativa bilíngue).

A galeria mostra posters gerados por IA; o vídeo correspondente (sem áudio) é carregado
apenas quando o leitor passa o mouse ou toca no cartão. Clicar alterna a "cena" aplicada
sobre imagem e vídeo (RGB, branco dia, leitura, manhã, pôr do sol, luz noturna) via CSS.
"""
from html import escape

VIDEO = '/static/video/scenes/'
IMG = '/static/img/scenes/'

# (arquivo, largura, altura, título pt, título en, legenda pt, legenda en)
CARDS = [
    ('game-neon', 1280, 720,
     'Modo game', 'Game mode',
     'Fitas RGB no rebaixo do teto e atrás da TV; a sanca vira moldura de luz.',
     'RGB strips in the ceiling cove and behind the TV; the cove becomes a frame of light.'),
    ('corrida', 1280, 720,
     'Sanca em degradê', 'Gradient cove',
     'Magenta de um lado, azul do outro: fitas endereçáveis pintam a parede inteira.',
     'Magenta on one side, blue on the other: addressable strips paint the whole wall.'),
    ('quatro-ambientes', 1280, 1280,
     'Quatro cenas, uma sala', 'Four scenes, one room',
     'Dia, entardecer, festa e noite: os mesmos móveis, decorações diferentes.',
     'Day, dusk, party and night: the same furniture, four different rooms.'),
    ('cidade-noite', 1280, 1280,
     'Noite de cinema', 'Movie night',
     'Luz de contorno atrás da TV e rodapé do sofá iluminado: guia os passos sem ofuscar.',
     'Bias light behind the TV and a lit sofa plinth: guides your steps without glare.'),
    ('dia-tarde-noite', 1280, 720,
     'Manhã, pôr do sol e noite', 'Morning, sunset and night',
     'Do branco frio ao azul profundo, a mesma sala acompanha o dia lá fora.',
     'From cool white to deep blue, the same room follows the day outside.'),
    ('lounge', 1184, 768,
     'Lounge', 'Lounge',
     'Cortina banhada de luz e abajures coloridos: cada luminária entra na cena.',
     'A light-washed curtain and colored lamps: every fixture joins the scene.'),
]

# (id, rótulo pt, rótulo en, ajuste típico exibido no selo)
MODES = [
    ('rgb', 'RGB festa', 'RGB party', 'RGB · 100%'),
    ('dia', 'Branco dia', 'Daylight', '5.500 K · 100%'),
    ('leitura', 'Leitura', 'Reading', '4.000 K · 80%'),
    ('manha', 'Manhã', 'Morning', '3.000 K · 60%'),
    ('por-do-sol', 'Pôr do sol', 'Sunset', '2.200 K · 35%'),
    ('noturna', 'Luz noturna', 'Night light', '1.800 K · 3%'),
]


def _ext(url, label):
    return f'<a class="ext" href="{escape(url, quote=True)}" target="_blank" rel="noopener">{label}</a>'


def scene_gallery(lang='pt'):
    en = lang == 'en'
    t = lambda pt, eng: eng if en else pt
    cards = []
    for i, (name, w, h, title_pt, title_en, cap_pt, cap_en) in enumerate(CARDS, 1):
        title = title_en if en else title_pt
        cap = cap_en if en else cap_pt
        alt = escape(f'{title}: {cap}', quote=True)
        chips = ''.join(
            f'<button type="button" data-mode="{mid}" data-k="{k}" aria-pressed="{"true" if mid == "rgb" else "false"}">{eng if en else pt}</button>'
            for mid, pt, eng, k in MODES)
        cards.append(
            f'<figure class="scene-card" data-mode="rgb" style="--ar:{w}/{h}">'
            f'<button class="scene-stage" type="button" aria-label="{escape(t("Cena " + str(i) + ": trocar a iluminação de " + title, "Scene " + str(i) + ": change the lighting of " + title), quote=True)}">'
            f'<span class="scene-media"><img src="{IMG}{name}.webp" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">'
            f'<video muted playsinline loop preload="none" data-src="{VIDEO}{name}.mp4" width="{w}" height="{h}" tabindex="-1" aria-hidden="true"></video>'
            f'<span class="scene-tint" aria-hidden="true"></span></span>'
            f'<span class="scene-badge" aria-live="polite"><strong>{MODES[0][2] if en else MODES[0][1]}</strong><span>{MODES[0][3]}</span></span>'
            f'<span class="scene-hint" aria-hidden="true">▶ {t("Passe o mouse ou toque", "Hover or tap")}</span>'
            f'</button>'
            f'<figcaption><h4>{title}</h4><p>{cap}</p>'
            f'<span class="scene-modes" role="group" aria-label="{t("Escolher cena", "Choose a scene")}">{chips}</span></figcaption>'
            f'</figure>')
    return (f'<div class="scene-gallery" data-scene-gallery aria-label="{t("Galeria de cenas de iluminação", "Lighting scene gallery")}">'
            + ''.join(cards) + '</div>')


def scenes_showcase(lang='pt', heading_id='ha-cenas', in_article=False):
    en = lang == 'en'
    t = lambda pt, eng: eng if en else pt
    h = 'h2' if in_article else 'h3'
    sub = 'h3' if in_article else 'h4'
    ha_scene = 'https://www.home-assistant.io/integrations/scene/'
    ha_light = 'https://www.home-assistant.io/integrations/light/'
    adaptive = 'https://adaptive-lighting.nijho.lt/'
    ma = 'https://www.music-assistant.io/'
    ma_ha = 'https://www.home-assistant.io/integrations/music_assistant/'
    hue_sync = 'https://www.philips-hue.com/en-us/explore-hue/propositions/entertainment'
    wled = 'https://kno.wled.ge/'
    # No artigo, o título vem do Markdown (entra no sumário); na home, é gerado aqui.
    head = '' if in_article else f'''<p class="eyebrow">{t('Iluminação RGBCCT', 'RGBCCT lighting')}</p><{h} id="{heading_id}">{t('A mesma sala. Seis climas diferentes.', 'The same room. Six different moods.')}</{h}>
'''
    return f'''<div class="feature-block scene-section{' scene-section-article' if in_article else ''}">{head}<p>{t('<strong>RGBCCT</strong> junta duas coisas em uma lâmpada ou fita de LED: <strong>RGB</strong>, os LEDs coloridos, e <strong>CCT</strong> (temperatura de cor correlata), os LEDs brancos que vão do branco quente, parecido com vela, ao branco frio, parecido com o céu de meio-dia. A medida é em kelvin (K): 2.200 K é âmbar, 2.700 K é a lâmpada incandescente de antigamente, 4.000 K é neutro e 6.500 K é o branco azulado. Cor muda o clima; temperatura do branco muda o quanto o ambiente parece manhã ou noite.', '<strong>RGBCCT</strong> puts two things into one bulb or LED strip: <strong>RGB</strong>, the colored LEDs, and <strong>CCT</strong> (correlated color temperature), white LEDs that range from candle-like warm white to midday-sky cool white. It is measured in kelvin (K): 2,200 K is amber, 2,700 K is the classic incandescent bulb, 4,000 K is neutral and 6,500 K is bluish white. Color changes the mood; white temperature changes how much the room feels like morning or night.')}</p>
<p>{t('Uma <strong>cena</strong> é um conjunto de estados salvos com nome: quais luzes acendem, em que cor, brilho e temperatura. É ela que transforma decoração fixa em decoração que muda ao longo do dia. Passe o mouse (ou toque, no celular) para ver cada ambiente em movimento; clique na imagem ou nos botões para trocar a cena aplicada. A simulação usa filtros de cor sobre imagens geradas por IA: a ideia é mostrar o efeito, não reproduzir um produto.', 'A <strong>scene</strong> is a named set of saved states: which lights turn on, in which color, brightness and temperature. It is what turns fixed decor into decor that changes through the day. Hover (or tap, on a phone) to see each room in motion; click the image or the buttons to switch the applied scene. The simulation uses color filters over AI-generated images: the point is to show the effect, not to reproduce a product.')}</p>
{scene_gallery(lang)}
<p class="feature-small">{t('Imagens e vídeos gerados por IA para o SmartHome-AI; cenas simuladas. Cores, brilho e transições reais dependem do produto e da integração.', 'AI-generated images and videos for SmartHome-AI; simulated scenes. Real colors, brightness and transitions depend on the product and integration.')}</p>
<{sub}>{t('Cinco cenas que valem a pena criar', 'Five scenes worth creating')}</{sub}>
<div class="ha-control-grid scene-recipes"><article><h4>{t('Amanhecer', 'Sunrise')}</h4><p>{t('Começa em 1% e 2.200 K e sobe devagar até 60% e 4.000 K em 20 minutos, antes do alarme. Use <em>transition</em> na ação de luz ou a integração Adaptive Lighting, que segue o sol sozinha.', 'Starts at 1% and 2,200 K and slowly rises to 60% and 4,000 K over 20 minutes before the alarm. Use <em>transition</em> in the light action or the Adaptive Lighting integration, which follows the sun by itself.')}</p></article>
<article><h4>{t('Branco dia e leitura', 'Daylight and reading')}</h4><p>{t('Branco neutro a frio (4.000–5.500 K) com brilho alto para trabalhar e ler. Fitas atrás de prateleiras e sob armários dão luz uniforme, sem sombras duras.', 'Neutral to cool white (4,000–5,500 K) at high brightness for work and reading. Strips behind shelves and under cabinets give even light without harsh shadows.')}</p></article>
<article><h4>{t('Pôr do sol', 'Sunset')}</h4><p>{t('Ao entardecer, tons âmbar (2.200–2.700 K) a 30–40%, com um toque de laranja na sanca. Um gatilho de <em>sunset</em> na automação faz a casa acompanhar o horário do ano.', 'At dusk, amber tones (2,200–2,700 K) at 30–40%, with a hint of orange in the cove. A <em>sunset</em> trigger in the automation keeps the home in step with the season.')}</p></article>
<article><h4>{t('Home cinema', 'Home cinema')}</h4><p>{t('TV ou projetor ligado, cortinas fechadas, luz de contorno atrás da tela e um filete de luz no chão. Quando o filme pausa, as luzes sobem um pouco; quando volta, descem de novo.', 'TV or projector on, curtains closed, bias light behind the screen and a strip of light along the floor. When the movie pauses, the lights come up a little; when it resumes, they dim again.')}</p></article>
<article><h4>{t('Luz noturna', 'Night light')}</h4><p>{t('Entre 1% e 5% em 1.800–2.200 K, acesa por sensor de presença de madrugada e apagada depois de dois minutos. Ilumina o caminho sem acordar ninguém.', 'Between 1% and 5% at 1,800–2,200 K, turned on by a presence sensor in the small hours and off after two minutes. Lights the way without waking anyone.')}</p></article></div>
<p class="feature-small">{t('No Home Assistant, crie cenas no editor visual e chame-as em automações, botões ou por voz.', 'In Home Assistant, create scenes in the visual editor and call them from automations, buttons or voice.')} {_ext(ha_scene, t('Cenas no Home Assistant', 'Scenes in Home Assistant'))} · {_ext(ha_light, t('Ações de luz e transição', 'Light actions and transition'))} · {_ext(adaptive, 'Adaptive Lighting')}</p>
<div class="feature-pair scene-pair"><div><p class="eyebrow">{t('Home cinema', 'Home cinema')}</p><{sub}>{t('O ritual em um toque.', 'The ritual in one tap.')}</{sub}><p>{t('A cena de cinema é o exemplo clássico porque envolve vários aparelhos ao mesmo tempo: o <em>media player</em> (TV, Apple TV, projetor) liga e escolhe a entrada, a cortina fecha, o ar-condicionado ajusta e as luzes assumem o tom da noite. No Home Assistant, isso vira um <strong>script</strong> ou uma cena com transição de alguns segundos, disparado por um botão físico, pelo painel, pela Siri ou por uma frase no Assist.', 'The movie scene is the classic example because it involves several devices at once: the <em>media player</em> (TV, Apple TV, projector) turns on and picks the input, the blind closes, the air conditioner adjusts and the lights take on the evening tone. In Home Assistant this becomes a <strong>script</strong> or a scene with a few seconds of transition, triggered by a physical button, the dashboard, Siri or a phrase in Assist.')}</p><p>{t('A <strong>luz de contorno</strong> (bias light) atrás da TV reduz o contraste entre a tela brilhante e a parede escura, o que cansa menos os olhos. A referência de cinema é um branco neutro de 6.500 K em brilho baixo; para efeito de ambiente, muita gente prefere cor. Sistemas como Hue Play HDMI Sync ou fitas endereçáveis com WLED podem acompanhar as cores do filme; o Home Assistant ainda cuida do resto da cena.', '<strong>Bias light</strong> behind the TV reduces the contrast between the bright screen and the dark wall, which is easier on the eyes. The cinema reference is neutral 6,500 K white at low brightness; for ambience, many people prefer color. Systems such as Hue Play HDMI Sync or addressable strips running WLED can follow the movie’s colors; Home Assistant still handles the rest of the scene.')}</p><p>{t('Uma automação simples fecha o ciclo: quando o estado do <em>media player</em> muda para <em>pausado</em>, as luzes sobem para 30% em dois segundos; quando volta a <em>tocando</em>, descem de novo. Ao desligar a TV, a cena “Noite” assume.', 'A simple automation closes the loop: when the <em>media player</em> state changes to <em>paused</em>, the lights rise to 30% over two seconds; when it returns to <em>playing</em>, they dim again. When the TV turns off, the “Night” scene takes over.')}</p><p class="feature-small">{_ext(hue_sync, 'Philips Hue Entertainment')} · {_ext(wled, 'WLED')}</p></div>
<div class="scene-ma"><p class="eyebrow">Music Assistant</p><{sub}>{t('A trilha sonora da casa.', 'The soundtrack of your home.')}</{sub}><p>{t('<strong>Music Assistant</strong> é um projeto da Open Home Foundation que funciona como uma biblioteca musical única para a casa. Instala-se como App no HAOS (ou em Docker) e reúne serviços como Spotify, Apple Music, YouTube Music, Tidal, Deezer, Qobuz, rádios, podcasts e arquivos locais em uma só interface.', '<strong>Music Assistant</strong> is an Open Home Foundation project that works as a single music library for the home. It installs as an App in HAOS (or in Docker) and brings services such as Spotify, Apple Music, YouTube Music, Tidal, Deezer, Qobuz, radio, podcasts and local files into one interface.')}</p><p>{t('Do outro lado, ele toca em quase qualquer caixa: Sonos, Google Cast, AirPlay (HomePod e Apple TV), DLNA, Squeezelite e até um ESP32 com ESPHome, com grupos multi-room sincronizados. A integração oficial do Home Assistant expõe cada player como <em>media player</em>, permite transferir a fila entre cômodos e pausa a música para avisos de voz.', 'On the other side, it plays on almost any speaker: Sonos, Google Cast, AirPlay (HomePod and Apple TV), DLNA, Squeezelite and even an ESP32 running ESPHome, with synchronized multi-room groups. The official Home Assistant integration exposes every player as a <em>media player</em>, lets you move the queue between rooms and pauses music for voice announcements.')}</p><p>{t('É o que fecha a cena: “Pôr do sol” pode acender a sanca em âmbar <em>e</em> iniciar uma playlist tranquila a 20% de volume na sala; “Home cinema” silencia as caixas da cozinha antes do filme começar. Com o Assist, dá para pedir uma música por voz e o pedido cai no player do cômodo onde você está.', 'It completes the scene: “Sunset” can light the cove in amber <em>and</em> start a mellow playlist at 20% volume in the living room; “Home cinema” mutes the kitchen speakers before the movie starts. With Assist, you can ask for a song by voice and it lands on the player in the room you are in.')}</p><p class="feature-small">{_ext(ma, 'music-assistant.io')} · {_ext(ma_ha, t('Integração no Home Assistant', 'Home Assistant integration'))}</p></div></div></div>'''
