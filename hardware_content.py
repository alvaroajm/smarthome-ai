"""Beginner hardware comparison, with dated Brazilian price references."""
from html import escape

GREEN = 'https://www.home-assistant.io/green/'
PI = 'https://www.raspberrypi.com/products/raspberry-pi-5/'
INTEL = 'https://www.intel.com/content/www/us/en/products/sku/241636/intel-processor-n150-6m-cache-up-to-3-60-ghz/specifications.html'
ML_GREEN = 'https://lista.mercadolivre.com.br/home-assistant-green'
ML_PI = 'https://lista.mercadolivre.com.br/raspberry-pi-5-nvme'
ML_RYZEN = 'https://lista.mercadolivre.com.br/mini-pc-ryzen-16gb'
N150_PRICE = 'https://www.kabum.com.br/produto/1066967/mini-pc-ntc-14n150-1103-intel-processor-n150-intel-graphics-16gb-ddr4-512gb-ssd-s-fans-linux'
R7_PRICE = 'https://www.eletrowix.com.br/mini-pc-nucbox-gmktec-k8-plus-amd-ryzen-7-8845hs32gb-ddr51tbw11-pro'
R7_PRICE2 = 'https://www.eletrowix.com.br/mini-pc-nucbox-gmktec-k6-amd-ryzen-7-7840hs16gb-ddr51tbw11-pro'

def hardware_section(lang='pt'):
    en = lang == 'en'
    def t(pt, eng): return eng if en else pt
    def a(url, label): return f'<a class="ext" href="{escape(url, quote=True)}" target="_blank" rel="noopener">{label}</a>'
    cards = [
        dict(id='green', name='Home Assistant Green', tag=t('Mais simples para começar', 'Easiest first step'),
             image='/static/img/hardware/green.webp', width=800, height=533,
             photo=a(GREEN, t('Foto oficial · Home Assistant Green', 'Official photo · Home Assistant Green')),
             specs='4 GB RAM · 32 GB eMMC',
             pro=t('HAOS já instalado, silencioso e econômico. Basta conectar a energia e o cabo de rede.', 'HAOS preinstalled, silent and energy efficient. Just connect power and Ethernet.'),
             con=t('Memória e armazenamento internos fixos. Menos indicado para gravação de câmeras e tarefas pesadas.', 'Fixed internal memory and storage. Less suited to camera recording and demanding tasks.'),
             price='1.950', basis=t('Faixa: R$ 1.750–2.300 · anúncios de importação', 'Range: R$ 1,750–2,300 · import listings')),
        dict(id='pi5', name='Raspberry Pi 5', tag=t('Para quem gosta de montar', 'For hands-on beginners'),
             image='/static/img/devices/raspberry-pi-5-case.jpg', width=800, height=535,
             photo=a('https://www.raspberrypi.com/news/m-2-hat-compact-on-sale-now-at-15/', t('Foto oficial · Pi 5 com case e M.2 HAT', 'Official photo · Pi 5 with case and M.2 HAT')),
             specs='8 GB RAM · SSD NVMe 500 GB / 1 TB',
             pro=t('Compacto, com boa comunidade e desempenho para automações. O SSD oferece mais espaço e resistência a gravações que um cartão comum.', 'Compact, well documented and capable of home automation. An SSD provides more space and write endurance than a basic memory card.'),
             con=t('Some fonte adequada, cooler, case e adaptador M.2 HAT. Montagem e inicialização pelo NVMe exigem preparação; o kit pode custar tanto quanto um mini-PC.', 'Add a suitable power supply, cooling, case and M.2 HAT adapter. Assembly and NVMe boot need preparation; a full kit can cost as much as a mini PC.'),
             price='3.750', basis=t('Faixa: R$ 3.465–4.020 · kit completo, 500 GB / 1 TB', 'Range: R$ 3,465–4,020 · complete 500 GB / 1 TB kit')),
        dict(id='n150', name='Mini-PC Intel N150', tag=t('Equilíbrio para o HAOS', 'A balanced HAOS choice'),
             image='/static/img/hardware/n150.webp', width=800, height=800,
             photo=a('https://www.gmktec.com/products/nucbox-g3-plus-enhanced-performance-mini-pc-with-intel-n150-processor', t('Exemplo da categoria · GMKtec G3 Plus', 'Category example · GMKtec G3 Plus')),
             specs=t('16 GB RAM · SSD/NVMe 500 GB ou 1 TB', '16 GB RAM · 500 GB or 1 TB SSD/NVMe'),
             pro=t('Bom equilíbrio entre desempenho, tamanho e consumo. Tem folga para HAOS, ZHA e vários Apps.', 'Balances performance, size and power use. Has room for HAOS, ZHA and several Apps.'),
             con=t('Exige instalar o HAOS. Para 32 GB, compre apenas um modelo com suporte confirmado pelo fabricante: a especificação da Intel é de até 16 GB.', 'Requires HAOS installation. Choose 32 GB only when the PC manufacturer confirms support: Intel specifies up to 16 GB.'),
             price='3.500', basis=t('Referência: 16 GB + NVMe 512 GB · uma oferta nacional', 'Reference: 16 GB + 512 GB NVMe · one Brazilian offer')),
        dict(id='ryzen5', name='Mini-PC Ryzen 5', tag=t('Mais espaço para crescer', 'Room to grow'),
             image='/static/img/hardware/ryzen5.webp', width=800, height=800,
             photo=a('https://www.bee-link.com/products/beelink-eqr5', t('Exemplo da categoria · Beelink EQR5', 'Category example · Beelink EQR5')),
             specs=t('16 ou 32 GB RAM · SSD/NVMe 500 GB ou 1 TB', '16 or 32 GB RAM · 500 GB or 1 TB SSD/NVMe'),
             pro=t('Boa margem para mais Apps e tarefas simultâneas. Muitos modelos permitem ampliar RAM e SSD.', 'Headroom for more Apps and simultaneous tasks. Many models allow RAM and SSD upgrades.'),
             con=t('Pode consumir mais e ter ventoinha audível. A geração do Ryzen importa: nem todo Ryzen 5 é recente ou permite expansão.', 'May use more power and have an audible fan. CPU generation matters: not every Ryzen 5 is recent or upgradeable.'),
             price='3.500', basis=t('Faixa: R$ 2.988–3.999 · amostra com 16 GB + 512 GB', 'Range: R$ 2,988–3,999 · sample with 16 GB + 512 GB')),
        dict(id='ryzen7', name='Mini-PC Ryzen 7', tag=t('Para planos mais exigentes', 'For more demanding plans'),
             image='/static/img/hardware/ryzen7.webp', width=800, height=800,
             photo=a('https://www.bee-link.com/products/beelink-eqr7', t('Exemplo da categoria · Beelink EQR7', 'Category example · Beelink EQR7')),
             specs=t('16 ou 32 GB RAM · SSD/NVMe 500 GB ou 1 TB', '16 or 32 GB RAM · 500 GB or 1 TB SSD/NVMe'),
             pro=t('Modelos recentes oferecem bastante desempenho para crescer. Faz sentido se já houver planos concretos para tarefas mais pesadas.', 'Recent models offer plenty of performance to grow into. Makes sense when you already have specific plans for demanding workloads.'),
             con=t('Custo maior e potência desnecessária para começar com ZHA. Consumo, calor e ruído variam muito entre modelos.', 'Higher cost and more performance than basic ZHA needs. Power use, heat and noise vary widely by model.'),
             price='5.250', basis=t('Faixa: R$ 3.879–6.910 · amostra com 16/32 GB e 512 GB/1 TB', 'Range: R$ 3,879–6,910 · sample with 16/32 GB and 512 GB/1 TB')),
    ]
    out = [f'''<section class="wrap section lesson-divider" aria-labelledby="hardware-haos">
<header class="section-head"><p class="eyebrow">04 / {t('Um passo de cada vez','One step at a time')}</p>
<h2 id="hardware-haos">{t('Escolha a central da sua casa.','Choose your home’s hub.')}</h2>
<p>{t('O HAOS precisa de um computador ligado em casa. Estas são as opções: do Green pronto para usar aos mini-PCs com mais capacidade.','HAOS needs an always-on computer at home. Choose from the ready-to-use Green to more capable mini PCs.')}</p></header>
<p class="hardware-intro">{t('Para começar sem complicação, escolha o Green. Para ter mais folga, considere um N150 com 16 GB.','For an easy start, choose Green. For more headroom, consider an N150 with 16 GB.')}</p>
<div class="ha-hardware-grid">''']
    for c in cards:
        out.append(f'''<article class="ha-hardware-card hardware-{c['id']}">
<figure><div class="hardware-photo"><img src="{c['image']}" width="{c['width']}" height="{c['height']}" alt="{escape(c['name'])}: {t('foto do equipamento','device photo')}" loading="lazy" decoding="async"></div><figcaption>{c['photo']}</figcaption></figure>
<div class="hardware-copy"><p class="eyebrow">{c['tag']}</p><h3>{c['name']}</h3><p class="hardware-specs">{c['specs']}</p>
<dl><dt>{t('Vantagens','Advantages')}</dt><dd>{c['pro']}</dd><dt>{t('Desvantagens','Trade-offs')}</dt><dd>{c['con']}</dd></dl>
<div class="hardware-price"><span>{t('Preço de referência no Brasil','Brazilian reference price') if c['id']=='n150' else t('Média de referência no Brasil','Brazilian reference average')}</span><strong>≈ R$ {c['price']}</strong><small>{c['basis']}</small></div></div></article>''')
    out.append(f'''<aside class="hardware-decision"><p class="eyebrow">{t('Escolha sem exagerar','Keep it simple')}</p><h3>{t('Você não precisa do mais potente.','You don’t need the fastest one.')}</h3>
<p>{t('16 GB e 500/512 GB já dão bastante margem para começar em um mini-PC. 32 GB e 1 TB são opções para expansão, não requisitos do HAOS.','16 GB and 500/512 GB provide plenty of room for a first mini PC. 32 GB and 1 TB are expansion options, not HAOS requirements.')}</p>
<p>{t('Em todos eles, reserve o ZBT-2 à parte para nossa rede Zigbee. Use cabo de rede e mantenha backups fora da central.','For all these options, budget separately for ZBT-2 for our Zigbee network. Use Ethernet and keep backups outside the hub.')}</p>
<p>{t('Nos mini-PCs, confira suporte a UEFI e compatibilidade da rede. Instalar HAOS diretamente no disco apaga o sistema anterior.','For mini PCs, check UEFI and network compatibility. Installing HAOS directly on the disk erases the existing system.')}</p>
{a('https://www.home-assistant.io/installation/generic-x86-64/',t('Instalação oficial para mini-PC','Official mini PC installation'))}</aside></div>
<details class="hardware-references"><summary>{t('Preços, configurações e fontes da comparação','Prices, configurations and comparison sources')} · 22/09/2026</summary>
<p>{t('Valores aproximados, em reais, para planejar a compra. As médias arredondadas vêm da pequena amostra abaixo; não representam todo o mercado. No N150, há uma única oferta de referência. Anúncios indexados podem mudar de preço ou sair do ar.','Approximate Brazilian real values for budgeting. Rounded averages come from the small sample below, not the entire market. N150 has a single reference offer. Indexed listings may change price or disappear.')}</p>
<ul>
<li><strong>Green:</strong> R$ 1.749, R$ 1.786, R$ 2.297 — {a(ML_GREEN,'Mercado Livre')}. {t('Anúncios internacionais; confirme impostos no fechamento.','International listings; confirm taxes at checkout.')}</li>
<li><strong>Pi 5 8 GB:</strong> R$ 3.465 (500 GB), R$ 4.019 (1 TB) — {a(ML_PI,'Mercado Livre')}. {t('Kits Argon One V3 com NVMe, case e fonte; a foto mostra outro case.','Argon One V3 kits with NVMe, case and power supply; the photo shows a different case.')}</li>
<li><strong>N150:</strong> R$ 3.513,01 (16 GB / 512 GB, Pix) — {a(N150_PRICE,'KaBuM! / Gigantec')}. {t('Modelo NTC 14N150-1103; a foto é do GMKtec.','NTC 14N150-1103 model; the photo shows GMKtec.')}</li>
<li><strong>Ryzen 5:</strong> R$ 2.988 (7430U), R$ 3.599 e R$ 3.999 (3550H), {t('todos com','all with')} 16 GB / 512 GB — {a(ML_RYZEN,'Mercado Livre')}.</li>
<li><strong>Ryzen 7:</strong> R$ 3.879 (7730U, 16 GB / 512 GB) — {a(ML_RYZEN,'Mercado Livre')}; R$ 4.971,65 (7840HS, 16 GB / 1 TB, Pix) — {a(R7_PRICE2,'Eletrowix K6')}; R$ 6.909,65 (8845HS, 32 GB / 1 TB, Pix) — {a(R7_PRICE,'Eletrowix K8 Plus')}.</li></ul>
<p>{t('Compare o valor final com frete, tributos, garantia e forma de pagamento. Os preços não incluem o ZBT-2. Variantes de 32 GB/1 TB fora da amostra exigem cotação própria. As fotos dos mini-PCs ilustram a categoria, não todos os anúncios citados; confirme RAM, tipo de SSD e possibilidade de expansão no modelo exato.','Compare the final total including shipping, taxes, warranty and payment method. Prices exclude ZBT-2. Unlisted 32 GB/1 TB variants need their own quote. Mini PC photos illustrate the category, not every listed offer; confirm RAM, SSD type and upgrade options on the exact model.')}</p>
<p>{t('Especificações','Specifications')}: {a(GREEN,'Green')} · {a(PI,'Raspberry Pi 5')} · {a(INTEL,'Intel N150')}. <a href="/static/img/hardware/README.md">{t('Créditos das fotos','Photo credits')}</a>.</p></details></section>''')
    return '\n'.join(out)
