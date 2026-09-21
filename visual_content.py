"""Bilingual editorial components for the SmartHome-AI visual guide."""
from html import escape as esc
from pathlib import Path

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

def photo_gallery(lang):
 en=lang=='en';out=[]
 photos=[('hue-photo.jpg','Philips Hue · '+('hub & bulbs' if en else 'ponte e lâmpadas'),'Sho Hashimoto','https://commons.wikimedia.org/wiki/File:Philips_Hue_hub_and_2_bulbs.jpg','CC BY 2.0','https://creativecommons.org/licenses/by/2.0/','800','503'),('echo-photo.jpg','Amazon Echo Dot · '+('3rd generation' if en else '3ª geração'),'Samuel Wiki','https://commons.wikimedia.org/wiki/File:Echo_Dot_(3rd_Gen)_02.jpg','CC0','https://creativecommons.org/publicdomain/zero/1.0/','3740','2805'),('plug-photo.jpg','Smart plug · '+('remote switching' if en else 'acionamento remoto'),'TBWABusted','https://commons.wikimedia.org/wiki/File:Smart-plug.jpg','CC BY 2.0','https://creativecommons.org/licenses/by/2.0/','2627','2255')]
 for file,name,author,url,license,licurl,w,h in photos:
  out.append(f'''<figure class="photo-card"><a href="{url}"{ext(url)} aria-label="{'View original photo' if en else 'Ver foto original'}: {esc(name)}"><img src="/static/img/devices/{file}" width="{w}" height="{h}" alt="{esc(name)}" loading="lazy"></a><figcaption><strong>{esc(name)}</strong><small><a href="{url}"{ext(url)}>{author}</a> · <a href="{licurl}"{ext(licurl)}>{license}</a></small></figcaption></figure>''')
 return '\n'.join(out)

def home_visual_context(lang):
 return {'device_cards':device_cards(lang),'resource_cards':resource_cards(lang),'photo_gallery':photo_gallery(lang),'smart_room':(Path(__file__).parent/'static/img/smart-room.svg').read_text()}
