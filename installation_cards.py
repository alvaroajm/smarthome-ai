"""Three hardware-specific installation entry points; no client-side code."""
def installation_cards(lang='pt'):
 en=lang=='en';t=lambda pt,eng:eng if en else pt
 choices=[
 ('green','Home Assistant Green','/static/img/hardware/green.webp',800,533,t('Pronto para conectar','Ready to connect'),t('Ligue a rede e a energia. Crie sua conta e conecte o ZBT-2, pelas telas.','Connect Ethernet and power. Create your account and add ZBT-2 on screen.')),
 ('raspberry-pi-5','Raspberry Pi 5 + NVMe','/static/img/devices/raspberry-pi-5-case.jpg',800,535,t('Monte sua central','Build your hub'),t('Escolha placa, case e SSD. Prepare o NVMe no Mac ou PC e instale o HAOS.','Choose a board, case and SSD. Prepare NVMe on a Mac or PC and install HAOS.')),
 ('mini-pc','Mini-PC x86-64','/static/img/hardware/n150.webp',800,800,t('Intel ou AMD','Intel or AMD'),t('Prepare o pendrive e grave o HAOS no SSD interno, com um passo a passo visual.','Prepare a USB stick and write HAOS to the internal SSD with visual instructions.')),
 ]
 cards=[]
 for i,(slug,name,img,w,h,tag,desc) in enumerate(choices,1):
  cards.append(f'<a class="install-card" href="/instalar-{slug}/"><img src="{img}" width="{w}" height="{h}" alt="{name}" loading="lazy" decoding="async"><span class="install-card-copy"><span class="eyebrow">0{i} / {tag}</span><h3>{name}</h3><span class="install-card-description">{desc}</span><span class="install-card-cta">{t("Ver instalação passo a passo","Step-by-step installation (PT)")} →</span></span></a>')
 return '<div class="install-card-grid">'+''.join(cards)+'</div>'
