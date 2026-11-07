# Plano de medição

O que é medido, onde e com qual nome. Estado em 2026-11-07: site, admin e backend medindo, validado de ponta a ponta
com uma assinatura de teste (GA4 `purchase` e Meta `Subscribe` com `value 399 BRL`).

## Ferramentas

- **GA4:** propriedade `560905270`, fluxo `G-HR907RLPTS`, no site e no admin. Eventos principais: `sign_up` e `purchase`.
  `checkout.stripe.com` é referência indesejada (a compra mantém a origem da campanha).
- **Pixel da Meta:** `1174311258139587` (`Korza - Site`), o mesmo no site, no admin e na Conversions API. Um funil só,
  o que permite deduplicar navegador e servidor.
- **Conversions API (Meta):** o backend envia `CompleteRegistration` e `Subscribe`. A Meta também copia sozinha os
  eventos do navegador como "servidor" (configuração ligada no Pixel); tudo deduplica pelo `event_id`.
- **Código direto (gtag.js + fbq), sem GTM:** um lugar a menos para configurar. Rever se as tags crescerem.
- **Consent Mode:** sinais de anúncio negados por padrão (`ad_storage`, `ad_user_data`, `ad_personalization`),
  `analytics_storage` concedido. Sem banner de consentimento (`MELHORIAS.md`, "Privacidade").

## Funil e eventos

O site (`korza.app`) e o produto (`admin.korza.app`) estão no mesmo domínio: os cookies do GA4 e do Pixel valem nos dois.

| Etapa | Onde dispara | GA4 | Meta | Observação |
| --- | --- | --- | --- | --- |
| Visita | site e admin (a cada rota) | `page_view` | `PageView` | No admin, sem `PageView` em URL com e-mail |
| Clique no CTA | site | `cta_click` | — | `cta_text`, `cta_location` |
| Conta criada | admin + backend | `sign_up` | `CompleteRegistration` | Navegador e servidor com o mesmo `eventId` |
| Onboarding concluído (prévia montada) | admin | `onboarding_complete` | `ViewPreview` (custom) | Uma vez por pedido de onboarding |
| Foi para o Stripe | admin | `begin_checkout` | `InitiateCheckout` | Fim do onboarding ou página Cobrança |
| Assinatura | admin (GA4) + backend (Meta) | `purchase` | `Subscribe` | `value 399`, `BRL`; `Subscribe` só pelo servidor |

Regras:

- Evento só dispara quando a ação **aconteceu** (conta criada com sucesso, assinatura confirmada).
- **Assinatura que conta:** primeira assinatura e volta de quem tinha cancelado. Pagar fatura atrasada não conta. O
  `transaction_id` do GA4 é `<slug>-<subscriberSince>` e o `event_id` da Meta é `subscribe-<transição>`.
- Cadastro pela Shopify App Store e lojas `legacy`/`cortesia` não disparam assinatura (não são o funil dos anúncios).
- O rastreamento do admin só liga no build de produção; o `dev` não manda nada. A Conversions API fica desligada sem
  token.
- **Conversão para otimizar anúncios:** começar com `CompleteRegistration` (volume) e migrar para `ViewPreview` ou
  `Subscribe` quando houver ~50 eventos/semana. Se a campanha otimizar por `ViewPreview`, vale levá-lo também ao
  servidor.

## Origem de cada conta (`signup_attribution`)

- **Site:** guarda `utm_*`, `fbclid` e `gclid` da primeira página da visita (`sessionStorage`) e os repassa no clique para
  criar conta. Sem `fbclid`, usa o clique guardado no cookie `_fbc`.
- **Admin:** na primeira carga com `utm_*`/`fbclid`/`gclid` na URL, guarda a origem como **first touch**
  (`localStorage`, `korza_attribution`), com página de entrada e referrer. Funciona também com anúncio apontando direto
  para o admin. Não sobrescreve uma origem já guardada.
- **Backend:** no cadastro, grava uma linha por usuário na tabela `signup_attribution` (UTMs, `fbclid`, `gclid`, `_fbc`,
  `_fbp`, página de entrada, referrer, IP, navegador, `eventId`). Os campos são cortados em 2048 caracteres e nunca
  bloqueiam o cadastro.
- **Retenção (LGPD, política de privacidade seções 4.5, 9 e 11):** IP, navegador, cookies e ids de clique são apagados
  depois de 180 dias; UTMs, página de entrada e referrer ficam enquanto a conta existir.
- O `Subscribe` reaproveita o IP e o navegador do cadastro (o aviso do Stripe não vem do navegador da pessoa), com
  e-mail, telefone e id do usuário criptografados (SHA-256).

## UTMs

Padrão para todo link que a Korza controla. Nos anúncios da Meta, vão em "Parâmetros de URL" (o `fbclid` a Meta põe
sozinha).

| Parâmetro | Valores |
| --- | --- |
| `utm_source` | `meta`, `google`, `instagram`, `whatsapp`, `email` |
| `utm_medium` | `paid_social`, `cpc`, `organic_social`, `bio`, `outbound` |
| `utm_campaign` | `AAAA-MM-<slug>` (mesmo nome da pasta em `campanhas/`) |
| `utm_content` | id do criativo / variação (ex.: `reels-recompra-hookA`) |

## Como ler

- **Assinatura vale 399 uma vez** para a Meta e o GA4 (primeira mensalidade), mas a receita é recorrente. Ler campanha
  por **custo por assinatura** e **meses para pagar o anúncio** (custo ÷ 399), nunca pelo ROAS da Meta. Mandar
  `predicted_ltv` só quando houver dado de retenção dos clientes self-serve.
- **Contar cadastros pelo banco ou pelo GA4.** No Gerenciador de Eventos e em `ads_get_dataset_stats`, a Meta mostra o
  bruto: cada cadastro chega ~3 vezes (navegador, nosso servidor, cópia automática). 4 contas em 2026-11-07 apareceram
  como 12–13 `CompleteRegistration`. A atribuição dos anúncios usa o número desduplicado.
- **Conversão sem anúncio** aparece no Gerenciador de Eventos, mas não no Gerenciador de Anúncios.
- **Valor e parâmetros** de um evento da Meta: Gerenciador de Eventos → evento → Amostras de atividades.
- **GA4:** filtrar `hostName` em `korza.app` e `admin.korza.app` (o site rodando local manda `localhost`). Funil completo
  em Explorar → Exploração de funil: `cta_click` → `sign_up` → `onboarding_complete` → `begin_checkout` → `purchase`.
- **Qualidade da correspondência** do `CompleteRegistration`: 9,3 em 2026-11-07 (bom é ≥ 6).
- **Teste:** com `APP__META_CAPI__TEST_EVENT_CODE` no backend, todo evento do servidor vai só para Eventos de teste e
  não conta nos anúncios (código em `~/.config/korza-marketing/meta-capi.env`). Em produção a variável fica vazia.
  Para testar o funil, usar `pedroturik+<algo>@gmail.com` com `utm_campaign=teste-<algo>`, estornar e apagar a conta.

## Métricas da análise (`/cmo`)

Visitas → cliques no CTA → contas criadas → onboarding concluído → foi para o Stripe → assinaturas, por canal e
campanha. Custo por conta criada e por assinatura. Recompra e receita da loja ficam fora (são resultado do cliente, não
do marketing).

## Fora por enquanto

Tag do Google Ads (`AW-18544776538`) e importação do `sign_up` como conversão (`MELHORIAS.md`), banner de
consentimento, envio da origem ao HubSpot, versão em português da política.
