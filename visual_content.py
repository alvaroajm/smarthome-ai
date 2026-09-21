"""Bilingual editorial components for the SmartHome-AI visual guide."""
from html import escape as esc
from connected_home import connected_home

# name, group, protocol, PT description, EN description, PT check, EN check, guide
DEVICES = [
 ('bulb','Lâmpadas RGBCCT','RGBCCT bulbs','light','Zigbee',
  'Cores para criar ambientes. Branco quente ou frio para cada momento.',
  'Color for atmosphere. Warm or cool white for every moment.',
  'RGBCCT combina RGB e temperatura de cor ajustável. Confira as funções expostas pelo modelo no ZHA ou Zigbee2MQTT.',
  'RGBCCT combines RGB with adjustable white color temperature. Check the features exposed by the model in ZHA or Zigbee2MQTT.','/zigbee/'),
 ('led','Fitas de LED','LED strips','light','WLED · ESPHome',
  'Luz indireta, cores e cenas que acompanham o ritmo da casa.',
  'Indirect light, color and scenes that follow your day.',
  'Fitas endereçáveis e analógicas usam controladores diferentes. Combine tipo de fita, tensão, fonte e controlador.',
  'Addressable and analog strips need different controllers. Match strip type, voltage, power supply and controller.','https://kno.wled.ge/'),
 ('relay','Relés inteligentes','Smart relays','control','Zigbee · Wi-Fi',
  'Automação discreta, mantendo o interruptor que você já usa.',
  'Discreet automation that keeps your existing wall switch.',
  'Verifique neutro, tensão, carga e espaço na caixa. A instalação elétrica deve ser feita por profissional qualificado.',
  'Check neutral, voltage, load rating and wall-box space. Mains installation requires a qualified electrician.','/esphome-esp32/'),
 ('plug','Tomadas inteligentes','Smart plugs','control','Zigbee · Wi-Fi · Matter',
  'Controle aparelhos e, nos modelos compatíveis, acompanhe o consumo.',
  'Control appliances and, with supported models, track energy use.',
  'Confirme padrão do plugue, corrente admissível e medição de energia. Matter não garante todos os recursos do app do fabricante.',
  'Check plug type, current rating and energy metering. Matter does not guarantee every feature of the vendor app.','/matter-thread/'),
 ('presence','Sensores de presença','Presence sensors','sensor','mmWave · PIR',
  'A luz acompanha a ocupação do ambiente, sem depender de um botão.',
  'Light follows room occupancy without a button press.',
  'PIR responde a movimento; radar mmWave pode detectar pequenos movimentos. Posicionamento, zonas e sensibilidade precisam de ajuste.',
  'PIR responds to motion; mmWave radar can detect smaller movements. Position, zones and sensitivity need tuning.','/esphome-esp32/'),
 ('contact','Portas e janelas','Door & window sensors','sensor','Zigbee · Thread',
  'Saiba o que ficou aberto e use esse estado nas suas automações.',
  'Know what is open and use that state in your automations.',
  'Alinhe as duas partes dentro da distância indicada pelo fabricante. Um contato informa abertura; não confirma se a porta está trancada.',
  'Align both parts within the manufacturer’s specified gap. A contact detects opening; it does not confirm the door is locked.','/zigbee/'),
 ('temperature','Temperatura e umidade','Temperature & humidity','sensor','Zigbee · ESPHome',
  'Entenda o conforto de cada cômodo com medições ao longo do dia.',
  'Understand each room’s comfort with measurements throughout the day.',
  'Evite sol direto e fontes de calor. Confira precisão, intervalo de atualização e possibilidade de calibração.',
  'Avoid direct sunlight and heat sources. Check accuracy, update interval and calibration support.','/esphome-esp32/'),
 ('panel','Painéis de controle','Smart panels','control','Dashboard · ESP32',
  'Luzes, clima e cenas em uma tela ao alcance de todos.',
  'Lights, climate and scenes on a screen everyone can reach.',
  'Um tablet pode mostrar o dashboard do Home Assistant. Painéis ESP32 usam interfaces próprias, por exemplo com ESPHome e LVGL.',
  'A tablet can display a Home Assistant dashboard. ESP32 panels use their own interfaces, for example ESPHome with LVGL.','https://www.home-assistant.io/dashboards/'),
 ('tv','Smart TVs','Smart TVs','media','Wi-Fi · Ethernet',
  'Integre a TV às cenas de cinema e aos controles da sala.',
  'Bring your TV into movie scenes and living-room controls.',
  'A integração depende do fabricante e do modelo. Ligar a TV pela rede pode exigir Wake-on-LAN ou uma configuração de espera.',
  'Integration depends on the manufacturer and model. Network power-on may need Wake-on-LAN or a standby setting.','https://www.home-assistant.io/integrations/#media-player'),
 ('echo','Alexa e voz','Alexa & voice','media','Echo · Assist',
  'Comandos de voz para acionar cenas e facilitar pequenas tarefas.',
  'Voice commands for scenes and everyday tasks.',
  'Alexa depende de serviços online. Nabu Casa facilita a conexão com o Home Assistant; o Assist oferece outras opções, inclusive locais.',
  'Alexa relies on online services. Nabu Casa simplifies Home Assistant integration; Assist offers alternatives, including local options.','/nabu-casa/'),
 ('lock','Fechaduras inteligentes','Smart locks','media','Zigbee · Matter · Wi-Fi',
  'Consulte o estado da fechadura e organize o acesso à casa.',
  'Check lock status and organize access to your home.',
  'Confirme encaixe na porta, acesso de emergência, bateria e integração do modelo. O funcionamento local varia por produto.',
  'Check door fit, emergency access, batteries and model integration. Local operation varies by product.','https://www.home-assistant.io/integrations/#lock'),
 ('esp32','ESP32 e projetos DIY','ESP32 & DIY projects','control','ESPHome · Wi-Fi',
  'Crie sensores, controles e dispositivos que atendem à sua ideia.',
  'Build sensors, controls and devices around your own ideas.',
  'Escolha a placa e os componentes suportados. Comece por um projeto de baixa tensão e use a documentação do ESPHome.',
  'Choose a supported board and components. Start with a low-voltage project and follow the ESPHome documentation.','/esphome-esp32/'),
]

RESOURCES = [
 ('CasaOS','https://casaos.zimaspace.com/','base','Um painel para arquivos e aplicativos Docker no seu servidor.','A dashboard for files and Docker apps on your server.','C'),
 ('umbrelOS','https://umbrel.com/umbrelos','base','Sistema para criar sua nuvem pessoal em casa.','An operating system for your own home cloud.','u'),
 ('Umbrel App Store','https://apps.umbrel.com/','build','Explore os aplicativos para instalar no umbrelOS.','Explore apps to install on umbrelOS.','u+'),
 ('ZimaOS','https://www.zimaspace.com/zimaos','build','Conheça a evolução do ecossistema CasaOS, com foco em NAS.','Explore the CasaOS ecosystem’s evolution, focused on NAS.','Z'),
 ('Home Assistant','https://www.home-assistant.io/','base','O ponto de partida: plataforma, documentação e novidades.','The starting point: platform, documentation and news.','HA'),
 ('Nabu Casa','https://www.nabucasa.com/','base','Cloud opcional, acesso remoto e integração com Alexa.','Optional Cloud, remote access and Alexa integration.','NC'),
 ('ESPHome','https://esphome.io/','build','Crie sensores, controles e telas com microcontroladores.','Build sensors, controls and displays with microcontrollers.','ESP'),
 ('Zigbee2MQTT','https://www.zigbee2mqtt.io/','build','Documentação e catálogo de dispositivos Zigbee compatíveis.','Documentation and compatible Zigbee device catalog.','Z2M'),
 ('Instalador WLED','https://install.wled.me/','build','Instale WLED em uma placa compatível pelo navegador.','Install WLED on a supported board through your browser.','W'),
 ('Documentação WLED','https://kno.wled.ge/','build','Controladores, fitas de LED, efeitos e integrações.','Controllers, LED strips, effects and integrations.','W'),
 ('Home Assistant Brasil','https://homeassistantbrasil.com.br/','community','Projetos, dúvidas e troca de experiências em português.','Projects, questions and discussions in Portuguese.','BR'),
 ('Home Assistant Community','https://community.home-assistant.io/','community','Fórum internacional com tutoriais e projetos da comunidade.','International forum with tutorials and community projects.','HA'),
 ('Home Assistant no GitHub','https://github.com/home-assistant','community','Código-fonte, repositórios e acompanhamento do projeto.','Source code, repositories and project development.','GH'),
 ('Home Assistant · Wikipedia','https://en.wikipedia.org/wiki/Home_Assistant','community','Uma visão geral da história e do ecossistema, em inglês.','An overview of the history and ecosystem, in English.','Wk'),
 ('Integrações do Home Assistant','https://www.home-assistant.io/integrations/','base','Confira como conectar cada marca, serviço e dispositivo.','Check how to connect brands, services and devices.','+'),
 ('Assist','https://www.home-assistant.io/voice_control/','base','Conheça as opções de voz do Home Assistant.','Explore Home Assistant’s voice options.','A'),
 ('Dispositivos ESPHome','https://devices.esphome.io/','build','Receitas e configurações para diferentes equipamentos.','Recipes and configurations for different devices.','DIY'),
 ('Matter no Home Assistant','https://www.home-assistant.io/integrations/matter/','base','Entenda requisitos, Thread, Wi-Fi e compatibilidade.','Understand requirements, Thread, Wi-Fi and compatibility.','M'),
 ('Scrypted','https://www.scrypted.app/','build','Integração de câmeras e vídeo para a casa inteligente.','Camera and video integration for the smart home.','S'),
 ('Open Home Foundation','https://www.openhomefoundation.org/','community','Privacidade, escolha e sustentabilidade para o lar conectado.','Privacy, choice and sustainability for the connected home.','OH'),
]

def ext(url):
 return ' target="_blank" rel="noopener noreferrer"' if url.startswith('https://') else ''

def device_cards(lang):
 en=lang=='en';out=[]
 for key,pt,name,group,protocol,desc,desc_en,check,check_en,url in DEVICES:
  out.append(f'''<article class="device-card" data-device-category="{group}" id="device-{key}">
  <div class="device-art"><img src="/static/img/devices/{key}.svg" alt="" width="320" height="220" loading="lazy"><span>{esc(protocol)}</span></div>
  <div class="device-copy"><h3>{esc(name if en else pt)}</h3><p>{esc(desc_en if en else desc)}</p>
  <details><summary>{'What to check' if en else 'O que observar'}</summary><p>{esc(check_en if en else check)}</p><a href="{url}"{ext(url)}>{'Read the guide' if en else 'Consultar guia'} ↗</a></details></div></article>''')
 return '\n'.join(out)

def resource_cards(lang):
 en=lang=='en';out=[]
 for name,url,group,pt,eng,mark in RESOURCES:
  translations={'Instalador WLED':'WLED installer','Documentação WLED':'WLED documentation','Home Assistant no GitHub':'Home Assistant on GitHub','Integrações do Home Assistant':'Home Assistant integrations','Dispositivos ESPHome':'ESPHome devices','Matter no Home Assistant':'Matter in Home Assistant'}
  out.append(f'''<a class="resource-card" data-resource-category="{group}" href="{url}"{ext(url)}><span class="resource-mark" aria-hidden="true">{mark}</span><span><strong>{esc(translations.get(name,name) if en else name)}</strong><small>{esc(eng if en else pt)}</small></span><span class="resource-arrow" aria-hidden="true">↗</span></a>''')
 return '\n'.join(out)

def photo_gallery(lang, hardware=False):
 en=lang=='en';out=[]
 photos=[
 ('hue-liane-2026.jpg','Philips Hue Liane 360°','Signify / Philips Hue','https://www.signify.com/global/our-company/news/press-releases/2026/20260903-philips-hue-expands-on-smart-lighting-with-ai-immersive-entertainment-and-design',800,450,'Lançamento de setembro de 2026. Iluminação contínua em 360°; disponibilidade por região.','September 2026 release. Continuous 360° lighting; availability varies by region.'),
 ('echo-dot-max-2025.jpg','Echo Dot Max','Amazon','https://www.aboutamazon.com.br/noticias/dispositivos/echo-dot-max-chega-ao-brasil-com-novo-design-e-audio-premium',1176,751,'Geração lançada em 2025, com áudio de duas vias e Alexa.','Released in 2025, with two-way audio and Alexa.'),
 ('shelly-plug-gen4.png','Shelly Plug US Gen4','Shelly','https://us.shelly.com/products/shelly-plug-us-gen4-black',800,800,'Geração 4 com medição de energia. A foto mostra o padrão dos EUA, 120 V; confira o padrão elétrico local.','Generation 4 with energy metering. Photo shows the US 120 V model; check local electrical standards.'),
 ] if not hardware else [
 ('raspberry-pi-5-case.jpg','Raspberry Pi 5 · '+('official case' if en else 'case oficial'),'Raspberry Pi','https://www.raspberrypi.com/news/m-2-hat-compact-on-sale-now-at-15/',800,535,'Raspberry Pi 5 no gabinete oficial, com o acessório M.2 HAT+ Compact visível na foto. Uma base compacta para projetos de automação.','Raspberry Pi 5 in its official case, with the M.2 HAT+ Compact accessory shown. A compact foundation for automation projects.'),
 ('modern-mini-pc.png','Mini-PC · ASUS NUC 16 Pro','ASUS','https://www.asus.com/displays-desktops/nucs/nuc-mini-pcs/asus-nuc-16-pro/',800,800,'Exemplo real de mini-PC moderno. O formato compacto pode abrigar um servidor doméstico; dimensione CPU, RAM e SSD para seu projeto.','A real example of a modern mini PC. This compact format can host a home server; size CPU, RAM and SSD for your project.'),
 ]
 for file,name,author,url,w,h,pt,eng in photos:
  out.append(f'''<figure class="photo-card"><a href="{url}"{ext(url)} aria-label="{'Official source' if en else 'Fonte oficial'}: {esc(name)}"><img src="/static/img/devices/{file}" width="{w}" height="{h}" alt="{esc(name)}" loading="lazy" decoding="async"></a><figcaption><strong>{esc(name)}</strong><p>{esc(eng if en else pt)}</p><small>{'Photo' if en else 'Imagem'}: <a href="{url}"{ext(url)}>{author} ↗</a></small></figcaption></figure>''')
 return '\n'.join(out)

def server_section(lang):
 en=lang=='en'
 t=lambda pt,eng: eng if en else pt
 return f'''<section class="server-section" id="servidor-em-casa" aria-labelledby="server-title"><div class="wrap section">
 <header class="section-head editorial-head"><div><p class="eyebrow">04 / {t('Seu servidor, suas possibilidades', 'Your server, your possibilities')}</p><h2 id="server-title">{t('Uma nuvem com<br>endereço de casa.', 'A cloud with<br>a home address.')}</h2></div><p>{t('Fotos, arquivos, mídia e aplicativos no seu próprio equipamento. CasaOS e umbrelOS simplificam o dia a dia de um servidor doméstico.', 'Photos, files, media and apps on your own hardware. CasaOS and umbrelOS simplify everyday home-server tasks.')}</p></header>
 <div class="server-platforms">
  <article class="server-platform"><span class="server-monogram" aria-hidden="true">C</span><h3>CasaOS</h3><p>{t('Um painel web instalado sobre um Linux compatível. Reúne arquivos, discos e aplicativos Docker em uma interface simples — uma boa porta de entrada para reaproveitar um PC ou Raspberry Pi.', 'A web dashboard installed on a compatible Linux system. It brings files, disks and Docker apps into a simple interface — a useful starting point for repurposing a PC or Raspberry Pi.')}</p><p class="platform-detail">{t('O site oficial também apresenta o ZimaOS, evolução do ecossistema com foco em NAS.', 'The official site also introduces ZimaOS, the ecosystem’s evolution focused on NAS.')}</p><div class="platform-links"><a href="https://casaos.zimaspace.com/"{ext('https://')}>{t('Conhecer CasaOS', 'Explore CasaOS')} ↗</a><a href="https://github.com/IceWhaleTech/CasaOS"{ext('https://')}>GitHub ↗</a></div></article>
  <article class="server-platform"><span class="server-monogram" aria-hidden="true">u</span><h3>umbrelOS</h3><p>{t('Um sistema completo para sua nuvem pessoal, administrado pelo navegador. Sua loja facilita a instalação de aplicativos de arquivos, fotos, mídia e outros serviços no hardware compatível.', 'A complete operating system for your personal cloud, managed in a browser. Its app store makes it easy to install file, photo, media and other services on compatible hardware.')}</p><p class="platform-detail">{t('Disponível para equipamentos Umbrel, PCs Intel/AMD, Raspberry Pi 5 e máquinas virtuais compatíveis.', 'Available for Umbrel devices, Intel/AMD PCs, Raspberry Pi 5 and compatible virtual machines.')}</p><div class="platform-links"><a href="https://umbrel.com/umbrelos"{ext('https://')}>{t('Conhecer umbrelOS', 'Explore umbrelOS')} ↗</a><a href="https://apps.umbrel.com/"{ext('https://')}>App Store ↗</a></div></article>
 </div>
 <div class="server-ha-note"><strong>{t('E o Home Assistant?', 'And Home Assistant?')}</strong><p>{t('Ele coordena a automação da casa. CasaOS e umbrelOS organizam os serviços do servidor. Se o Home Assistant rodar em container, os apps complementares são administrados separadamente.', 'It coordinates home automation. CasaOS and umbrelOS organize server services. When Home Assistant runs in a container, companion apps are managed separately.')}</p><a href="/casaos-umbrel/">{t('Comparar e escolher a instalação', 'Compare installation options (PT)')} →</a></div>
 <header class="hardware-heading"><h3>{t('O hardware por trás das ideias', 'The hardware behind your ideas')}</h3><p>{t('Do Raspberry Pi ao mini-PC: dois formatos para explorar.', 'From Raspberry Pi to mini PC: two formats to explore.')}</p></header><div class="photo-grid hardware-gallery">{photo_gallery(lang,True)}</div>
 </div></section>'''

def home_visual_context(lang):
 return {'device_cards':device_cards(lang),'resource_cards':resource_cards(lang),'photo_gallery':photo_gallery(lang),'connected_home':connected_home(lang),'server_section':server_section(lang),'resource_total':str(len(RESOURCES))}
