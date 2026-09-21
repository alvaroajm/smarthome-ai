"""Interactive lighting demo mapped onto the author's unchanged house image."""
from html import escape

# Coordinates follow the 1136 × 1744 source. Areas are lighting zones, not a CAD plan.
# id, PT, EN, polygon, marker x/y. Stable ids preserve state across PT/EN navigation.
ROOMS = [
    ('suite', 'Suíte principal', 'Main bedroom', '375,195 626,234 553,442 303,392', 455,325),
    ('bedroom-2', 'Quarto 2', 'Bedroom 2', '635,234 817,253 757,473 565,431', 687,361),
    ('bedroom-3', 'Quarto 3', 'Bedroom 3', '911,270 1136,316 1136,540 885,493', 1010,418),
    ('bath-1', 'Banheiro da suíte', 'En-suite bathroom', '292,404 510,436 478,537 250,492', 376,475),
    ('bath-2', 'Banheiro central', 'Middle bathroom', '827,259 894,270 844,513 773,490', 829,408),
    ('bath-3', 'Banheiro social', 'Main bathroom', '923,515 1136,545 1090,825 875,778', 1009,674),
    ('living', 'Sala de estar', 'Living room', '336,517 653,567 621,803 275,764', 455,659),
    ('office', 'Escritório', 'Office', '689,546 912,590 873,780 640,743', 779,661),
    ('dining', 'Sala de jantar', 'Dining room', '278,775 606,811 528,1056 208,980', 405,895),
    ('kitchen', 'Cozinha', 'Kitchen', '755,818 1087,843 1036,1214 671,1128 711,988', 871,1029),
    ('laundry', 'Lavanderia', 'Laundry', '610,846 739,879 702,995 571,969', 652,926),
    ('utility', 'Área de serviço', 'Utility room', '190,976 420,1021 411,1238 109,1157', 273,1105),
    ('storage', 'Depósito', 'Storage', '534,1055 661,1090 633,1283 488,1239', 570,1176),
    ('entry', 'Hall de entrada', 'Entrance hall', '493,1270 625,1303 592,1485 364,1431 405,1274', 490,1374),
    ('terrace', 'Varanda', 'Terrace', '131,544 283,581 211,783 163,946 29,916 70,752', 150,777),
    ('pool', 'Piscina', 'Pool', '26,964 102,979 41,1170 0,1145 0,1060', 48,1066),
]


def connected_home(lang):
    en = lang == 'en'
    t = lambda pt, eng: eng if en else pt
    definitions, regions, markers, switches = [], [], [], []
    # A compact, accessible on/off control accompanies every directly clickable zone.
    for n, (key, pt, eng, points, x, y) in enumerate(ROOMS, 1):
        name = escape(eng if en else pt)
        label = escape(t('Luz: ', 'Light: ') + (eng if en else pt))
        definitions.append(f'<clipPath id="clip-{key}"><polygon points="{points}"/></clipPath>')
        regions.append(f'''<g class="plan-zone" data-room-zone="{key}" data-on="true">
          <g class="plan-lit" clip-path="url(#clip-{key})" pointer-events="none">
           <use href="#plan-photo"/><polygon points="{points}" fill="#ffcb68" opacity=".14"/>
          </g>
          <polygon class="plan-zone-hit" data-room-hit="{key}" points="{points}"/>
         </g>''')
        markers.append(f'''<g class="plan-marker" data-room-marker="{key}" data-on="true" transform="translate({x} {y})" role="button" tabindex="-1" aria-disabled="true" aria-pressed="true" aria-label="{label}">
          <title>{name}</title><circle class="marker-target" r="39"/><circle class="marker-disc" r="26"/>
          <text text-anchor="middle" dy=".35em" aria-hidden="true">{n:02}</text>
         </g>''')
        switches.append(f'''<button class="room-toggle" type="button" data-room-toggle="{key}" aria-pressed="true" aria-label="{label}" disabled>
          <span class="room-number" aria-hidden="true">{n:02}</span><span class="room-toggle-copy"><strong>{name}</strong><small data-room-state>{t('Acesa', 'On')}</small></span><span class="room-switch" aria-hidden="true"></span>
         </button>''')
    return f'''<section class="wrap section connected-home" id="casa-interativa" aria-labelledby="house-title" data-house-demo>
      <header class="section-head editorial-head"><div><p class="eyebrow">01 / {t('Experimente a casa conectada', 'Explore the connected home')}</p><h2 id="house-title">{t('Um toque.<br>Um ambiente diferente.', 'One touch.<br>A different atmosphere.')}</h2></div><p id="house-help">{t('Toque em um cômodo da planta ou use os botões para acender e apagar sua luz. Experimente também as cenas prontas.', 'Tap a room on the plan or use the buttons to turn its light on and off. Try the ready-made scenes, too.')}</p></header>
      <div class="house-demo-grid">
       <div class="plan-frame">
        <div class="plan-toolbar"><span class="plan-demo-tag">{t('Demonstração interativa', 'Interactive demo')}</span><button type="button" class="plan-zoom" data-plan-zoom aria-pressed="false" disabled>{t('Ampliar planta', 'Enlarge plan')} <span aria-hidden="true">⤢</span></button></div>
        <div class="plan-viewport" tabindex="0" role="region" aria-label="{t('Planta da casa. Quando ampliada, role para explorar.', 'House plan. Scroll to explore when enlarged.')}">
         <svg class="house-plan" viewBox="0 150 1136 1450" xmlns="http://www.w3.org/2000/svg" role="group" aria-labelledby="plan-title plan-description">
          <title id="plan-title">{t('Planta 3D de uma casa conectada', '3D connected home floor plan')}</title><desc id="plan-description">{t('Dezesseis zonas de iluminação. Use Tab para escolher e Enter ou espaço para alternar. Os mesmos controles estão na lista de ambientes.', 'Sixteen lighting zones. Use Tab to select and Enter or Space to toggle. The same controls are available in the room list.')}</desc>
          <defs><image id="plan-photo" href="/static/img/connected-home-plan.jpg" width="1136" height="1744"/>{''.join(definitions)}</defs>
          <use href="#plan-photo" class="plan-base"/>{''.join(regions)}{''.join(markers)}
         </svg>
        </div>
        <p class="plan-feedback" data-plan-feedback aria-live="polite">{t('Escolha um ambiente para começar.', 'Choose a room to begin.')}</p>
       </div>
       <div class="house-controls">
        <div class="house-controls-title"><h3>{t('Luzes da casa', 'House lights')}</h3><span data-lights-count>16 / 16 {t('acesas', 'on')}</span></div>
        <div class="house-scenes" role="group" aria-label="{t('Cenas de iluminação', 'Lighting scenes')}">
         <button type="button" data-house-scene="all" aria-pressed="true" disabled>{t('Acender todas', 'All on')}</button><button type="button" data-house-scene="off" aria-pressed="false" disabled>{t('Apagar todas', 'All off')}</button><button type="button" data-house-scene="welcome" aria-pressed="false" disabled>{t('Chegar em casa', 'Welcome home')}</button><button type="button" data-house-scene="night" aria-pressed="false" disabled>{t('Boa noite', 'Good night')}</button>
        </div>
        <div class="room-toggle-grid" role="group" aria-label="{t('Iluminação por ambiente', 'Lighting by room')}">{''.join(switches)}</div>
        <p class="house-demo-note">{t('Simulação visual: os cliques mudam apenas a iluminação desta planta. As escolhas ficam salvas neste navegador, inclusive ao trocar PT/EN.', 'Visual simulation: clicks only change this floor plan’s lighting. Your choices are saved in this browser, including when switching PT/EN.')}</p>
        <noscript><p>{t('Ative o JavaScript para experimentar os controles de iluminação.', 'Enable JavaScript to try the lighting controls.')}</p></noscript>
       </div>
      </div>
    </section>'''
