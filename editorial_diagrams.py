"""Original, bilingual schematics replacing third-party editorial images.

No UI screenshots or product likenesses are reproduced. Keep source links for
technical reference; the diagram does not establish product compatibility.
"""
from html import escape
from pathlib import Path
import re

# source path: (diagram name, Portuguese / English title, three conceptual steps)
DIAGRAMS = {}
def add(folder, names, title, steps):
    for name in names.split():
        DIAGRAMS[f'/static/img/{folder}/{name}'] = (f'{folder}-{Path(name).stem}', title, steps)

add('ha-guide', 'dashboard.png', ('Controles em um painel', 'Controls on a dashboard'), [('Dispositivos','Devices'),('Painel','Dashboard'),('Controle','Control')])
add('ha-guide', 'onboarding.png', ('Primeiro acesso', 'First connection'), [('Abrir endereço','Open address'),('Criar conta','Create account'),('Adicionar dispositivo','Add device')])
add('ha-guide', 'imager.png', ('Preparar o HAOS', 'Prepare HAOS'), [('Escolher equipamento','Choose hardware'),('Gravar o sistema','Write the system'),('Iniciar a central','Start the hub')])
add('ha-guide', 'automation.png action.png', ('Uma automação', 'An automation'), [('Quando: gatilho','When: trigger'),('E se: condição','And if: condition'),('Então: ação','Then: action')])
add('ha-guide', 'integrations.png', ('Conectar uma integração', 'Connect an integration'), [('Dispositivo ou serviço','Device or service'),('Integração','Integration'),('Entidades no painel','Dashboard entities')])
add('ha-guide', 'apps.png', ('Serviços no HAOS', 'Services in HAOS'), [('HAOS','HAOS'),('App adicional','Additional app'),('Serviço configurado','Configured service')])
add('ha-guide', 'zbt-discovery.png zbt-zigbee.png zha-add.png', ('Começar com Zigbee', 'Start with Zigbee'), [('Adaptador USB','USB adapter'),('ZHA: criar a rede','ZHA: create network'),('Parear dispositivo','Pair device')])
add('ha-features', 'esp32.webp atom-s3.webp esphome-builder.webp', ('Um dispositivo ESPHome', 'An ESPHome device'), [('Placa e componentes','Board and parts'),('Configuração ESPHome','ESPHome configuration'),('Home Assistant','Home Assistant')])
add('ha-features', 'voice-pe.webp', ('Uma conversa com a casa', 'A conversation with home'), [('Entrada de voz','Voice input'),('Agente de conversação','Conversation agent'),('Resposta ou ação','Response or action')])
add('ha-features', 'frigate-live.webp frigate-review.webp reolink.webp', ('Vídeo na casa conectada', 'Connected home video'), [('Câmera compatível','Compatible camera'),('Integração ou NVR','Integration or NVR'),('Visualização / eventos','Live view / events')])
add('hardware', 'green.webp n150.webp ryzen5.webp ryzen7.webp', ('Uma central para o HAOS', 'A hub for HAOS'), [('Computador e disco','Computer and storage'),('Home Assistant OS','Home Assistant OS'),('Rede e dispositivos','Network and devices')])
add('zigbee-guide', 'zbt-2.webp contact.avif motion.avif button.png switch.avif', ('A rede Zigbee', 'The Zigbee network'), [('Home Assistant / ZHA','Home Assistant / ZHA'),('Coordenador USB','USB coordinator'),('Dispositivos Zigbee','Zigbee devices')])
add('devices', 'hue-liane-2026.jpg', ('Iluminação conectada', 'Connected lighting'), [('Comando ou rotina','Command or routine'),('Integração compatível','Compatible integration'),('Luz ou cena','Light or scene')])
add('devices', 'echo-dot-max-2025.jpg', ('Controle por voz', 'Voice control'), [('Pedido por voz','Voice request'),('Assistente e integração','Assistant and integration'),('Dispositivo compatível','Compatible device')])
add('devices', 'shelly-plug-gen4.png', ('Uma tomada conectada', 'A connected plug'), [('Comando','Command'),('Tomada compatível','Compatible plug'),('Equipamento','Appliance')])
add('devices', 'raspberry-pi-5-case.jpg modern-mini-pc.png', ('Uma central doméstica', 'A home hub'), [('Energia e Ethernet','Power and Ethernet'),('Computador com HAOS','Computer with HAOS'),('Rede de dispositivos','Device network')])


add('install', 'disks-image.png disks-progress.png disks-restore.png etcher-file.png', ('Gravar o sistema no disco', 'Write the system to storage'), [('Selecionar imagem HAOS','Select HAOS image'),('Conferir o disco de destino','Check target storage'),('Gravar e iniciar a central','Write and start the hub')])
add('install', 'green-power.webp green-zbt.png', ('Preparar a central', 'Prepare the hub'), [('Conectar a rede e energia','Connect Ethernet and power'),('Abrir o Home Assistant','Open Home Assistant'),('Configurar dispositivos','Set up devices')])
add('install', 'pi-ribbon.png', ('Armazenamento no Raspberry Pi', 'Raspberry Pi storage'), [('Placa e adaptador compatíveis','Compatible board and adapter'),('Conectar o SSD','Connect SSD storage'),('Gravar e iniciar o HAOS','Write and boot HAOS')])
add('install', 'secure-boot.jpg uefi.jpg', ('Preparar o boot do mini-PC', 'Prepare mini PC boot'), [('Consultar o manual do modelo','Read the model manual'),('Conferir os requisitos HAOS','Check HAOS requirements'),('Selecionar a mídia de boot','Select boot media')])


def diagram_url(source):
    return '/static/img/diagrams/' + DIAGRAMS[source][0] + '.svg'


def write_diagrams(root):
    folder = Path(root) / 'static/img/diagrams'
    folder.mkdir(parents=True, exist_ok=True)
    for name, title, steps in DIAGRAMS.values():
        blocks = []
        for i, (pt, en) in enumerate(steps):
            y = 145 + i * 108
            blocks.append(f'<rect x="48" y="{y}" width="504" height="80" rx="16" fill="#fffdf6" stroke="#315744" stroke-width="2"/><text x="300" y="{y+33}" text-anchor="middle" font-size="25" font-weight="600">{escape(pt)}</text><text x="300" y="{y+59}" text-anchor="middle" font-size="21" fill="#4a6254">{escape(en)}</text>')
            if i < 2:
                blocks.append(f'<path d="M300 {y+84}v18m-7-7 7 7 7-7" fill="none" stroke="#315744" stroke-width="3"/>')
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="520" viewBox="0 0 600 520" role="img" aria-labelledby="title desc"><title id="title">{escape(title[0])} / {escape(title[1])}</title><desc id="desc">Diagrama original conceitual. Não é captura de interface nem desenho de um produto. Original conceptual diagram; not a screenshot or product drawing.</desc><rect width="600" height="520" rx="24" fill="#edf1e8"/><g fill="#213e30" font-family="Arial, sans-serif"><text x="300" y="52" text-anchor="middle" font-size="15" letter-spacing="3">SMARTHOME-AI · DIAGRAMA / DIAGRAM</text><text x="300" y="91" text-anchor="middle" font-size="27" font-weight="600">{escape(title[0])}</text><text x="300" y="119" text-anchor="middle" font-size="22">{escape(title[1])}</text>{''.join(blocks)}<text x="300" y="493" text-anchor="middle" font-size="16">Esquema conceitual · Conceptual overview</text></g></svg>'''
        (folder / (name + '.svg')).write_text(svg, encoding='utf-8')


IMAGE = re.compile(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>', re.I)
FIGURE = re.compile(r'<figure\b[^>]*>.*?</figure>', re.S | re.I)


def replace_editorial_images(content, lang):
    en = lang == 'en'
    def image(match):
        source = match[1].split('?')[0]
        if source not in DIAGRAMS:
            return match[0]
        label = ('Original conceptual diagram: ' if en else 'Diagrama original conceitual: ') + DIAGRAMS[source][1][en]
        tag = match[0].replace(match[1], diagram_url(source))
        for attr, value in [('alt', escape(label, quote=True)), ('width', '600'), ('height', '520')]:
            if re.search(rf'\b{attr}="[^"]*"', tag):
                tag = re.sub(rf'\b{attr}="[^"]*"', f'{attr}="{value}"', tag)
            else:
                tag = tag[:-1] + f' {attr}="{value}">'
        return tag
    def figure(match):
        original = match[0]
        sources = [m[1].split('?')[0] for m in IMAGE.finditer(original) if m[1].split('?')[0] in DIAGRAMS]
        if not sources:
            return original
        result = IMAGE.sub(image, original)
        for source in sources:
            result = result.replace(f'href="{source}"', f'href="{diagram_url(source)}"')
        if any('/ha-guide/' in s or '/install/' in s for s in sources):
            refs = re.findall(r'<a\b[^>]*href="https://[^\"]+"[^>]*>.*?</a>', original, re.S)
            refs = [re.sub(r'>[^<]*(?:Official screenshot|Tela oficial)[^<]*<', '>' + ('Official instructions' if en else 'Instruções oficiais') + '<', ref) for ref in refs]
            result = re.sub(r'aria-label="[^"]*"', 'aria-label="' + ('Enlarge original diagram' if en else 'Ampliar diagrama original') + '"', result)
            caption = ('Original conceptual diagram, not a screenshot. Follow the linked instructions for the current interface.' if en else 'Diagrama conceitual original, não uma captura de tela. Consulte as instruções vinculadas para a interface atual.')
            return re.sub(r'<figcaption>.*?</figcaption>', '<figcaption>' + caption + ' ' + ' '.join(refs) + '</figcaption>', result, flags=re.S)
        note = ('Original conceptual diagram; not a photo of the named model.' if en else 'Diagrama conceitual original; não é foto do modelo citado.')
        result = result.replace('<figcaption>', '<figcaption><span>' + note + '</span> ', 1)
        for old, new in [('Official photo and product','Product reference'),('Foto e produto oficiais','Referência do produto'),('Official photo','Product reference'),('Foto oficial','Referência do produto'),('Official screenshot','Official documentation'),('Tela oficial','Documentação oficial')]:
            result = result.replace(old, new)
        return result
    content = FIGURE.sub(figure, content)
    return IMAGE.sub(image, content)
