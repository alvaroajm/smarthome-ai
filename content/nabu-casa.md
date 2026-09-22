---
title: Conheça o Home Assistant Cloud
slug: nabu-casa
description: Entenda o acesso remoto e as conexões com assistentes de voz.
category: Serviços
icon: cloud
order: 11
featured: true
reading: 8 min de leitura
date: 2026-09-21
tags: [Nabu Casa, Home Assistant Cloud, Acesso remoto, Alexa, Google, Backup]
---

O Home Assistant é gratuito e sempre será. A **Nabu Casa** é a empresa criada pelos próprios fundadores do
projeto, e o **Home Assistant Cloud** é a assinatura que financia o desenvolvimento — do Home Assistant, do
ESPHome e do Z-Wave JS. Ela não desbloqueia recursos escondidos: resolve, com dois cliques, três problemas
que dão trabalho de resolver sozinho.

## O que a assinatura entrega

| Recurso | O que resolve |
|---|---|
| **Acesso remoto** | Abrir a sua casa de qualquer lugar, criptografado, **sem abrir portas no roteador** |
| **Alexa e Google Assistant** | Conectar os dois assistentes sem servidor intermediário, certificados nem AWS Lambda |
| **Voz e texto para fala** | Vozes naturais para o *Assist* e para notificações faladas |
| **Backup na nuvem** | Cópia automática fora de casa, criptografada, com restauração ao trocar de hardware |
| **Webhooks** | Endereços públicos para receber eventos de outros serviços |
| **WebRTC melhorado** | Vídeo de câmeras mais fluido fora de casa |

Tudo trafega criptografado e a Nabu Casa declara não ter acesso ao conteúdo.

## Quanto custa (setembro de 2026)

| Região | Mensal | Anual |
|---|---|---|
| Estados Unidos / internacional | US$ 6,50 | US$ 65 |
| União Europeia | € 7,50 (com IVA) | € 75 |
| Reino Unido | £ 6,50 (com IVA) | £ 65 |
| Canadá | CAD 8,70 | CAD 87 |

Há **31 dias de teste** sem cobrança, e a assinatura é cancelável a qualquer momento. Confira sempre os
valores atuais em [nabucasa.com/pricing](https://www.nabucasa.com/pricing/) — preços mudam.

!!! nota "Para quem está no Brasil"
    A cobrança segue a tabela internacional em dólar, no cartão de crédito, com IOF e a conversão do dia.
    Vale comparar com o custo (e o tempo) de manter uma VPN por conta própria.

## Como ativar

1. *Configurações → Home Assistant Cloud*
2. Crie a conta e inicie o período de teste
3. Ligue **Acesso remoto** — você recebe um endereço `https://….ui.nabu.casa` pronto para usar
4. Ligue **Alexa** e/ou **Google Assistant** e escolha, uma a uma, quais entidades quer expor
5. Ative o **backup na nuvem** e defina a frequência

Pronto: o app do Home Assistant no iPhone passa a funcionar dentro e fora de casa sem nenhuma configuração
adicional.

!!! dica "Exponha pouco aos assistentes de voz"
    Mandar 300 entidades para a Alexa é receita para confusão ("Alexa, ligue a luz" e ela liga a errada).
    Exponha luzes, tomadas, cenas e climatização — e renomeie para nomes curtos e falados.

## As alternativas gratuitas (e o que elas custam em trabalho)

| Opção | Custo | Dificuldade | Observações |
|---|---|---|---|
| **Nabu Casa** | ~US$ 6,50/mês | Nenhuma | Acesso remoto + Alexa/Google + backup + TTS, e financia o projeto |
| **Tailscale** | Grátis (uso pessoal) | Baixa | VPN ponto a ponto; ótima no iPhone e no Mac. **Não** resolve Alexa/Google |
| **WireGuard no roteador** | Grátis | Média | Exige IP público ou DDNS e configuração em cada aparelho |
| **Cloudflare Tunnel** | Grátis | Média/alta | Expõe sem abrir porta, mas exige atenção redobrada com autenticação |
| **Abrir a porta 8123** | Grátis | Baixa | **Não faça isso.** É a forma mais comum de ter a casa invadida |

!!! atencao "A comparação honesta"
    O Tailscale resolve o acesso remoto tão bem quanto a Nabu Casa — e de graça. O que ele **não** faz é
    integrar Alexa e Google, gerar vozes naturais nem guardar backups fora de casa. Se você não usa
    assistentes de voz comerciais e já tem backup externo, a VPN é suficiente. Se usa, a assinatura sai mais
    barata que o seu tempo.

## Vale a pena?

**Sim, quase certamente, se você:**

- usa Alexa ou Google e quer que funcionem sem gambiarra
- quer acessar a casa pelo celular sem pensar em rede
- não tem hoje um backup automático fora do servidor
- gosta do projeto e quer que ele continue existindo — esta é a forma direta de financiá-lo

**Talvez não, se você:**

- vive no ecossistema Apple e usa [HomeKit](/apple-homekit/) como interface
- já tem VPN funcionando e um NAS recebendo os backups
- acessa a casa quase sempre de dentro da rede local

Seja qual for a escolha, **backup fora do servidor não é opcional**. Se você dispensar a nuvem, configure
hoje mesmo uma cópia para um NAS, um computador ou um serviço de armazenamento — o
[guia de instalação](/instalacao/) mostra como.
