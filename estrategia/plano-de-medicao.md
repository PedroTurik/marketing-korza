# Plano de medição

O que medir, onde e com qual nome. Sem isso, anúncio roda às cegas e o Meta/Google não conseguem
otimizar para quem cria conta e assina. Criado em 2026-10-26.

## Situação em 2026-10-26

Nenhum rastreamento instalado: **korza.com.br e admin.korza.app não têm GA4, GTM nem Pixel da Meta.**

## Funil e eventos

O funil atravessa dois domínios: o site (`korza.com.br`) e o produto (`admin.korza.app`).
**Atualização 2026-10-27:** o site passa para `korza.app`, o mesmo domínio do admin. Com isso os cookies do GA4 e do
Pixel valem no site e no cadastro sem configuração entre domínios; o repasse do `fbclid` vira redundante.

| Etapa | Onde | Evento GA4 | Evento Meta (Pixel) | Parâmetros |
| --- | --- | --- | --- | --- |
| Visita | site | `page_view` (automático) | `PageView` | — |
| Clique no CTA | site | `cta_click` | — | `cta_text`, `cta_location` (hero, precos, final…) |
| Conta criada | admin | `sign_up` | `CompleteRegistration` | `method`, `platform` (nuvemshop/shopify) |
| Loja conectada | admin | `store_connected` | `ConnectStore` (custom) | `platform` |
| Preview visto | admin | `preview_view` | `ViewPreview` (custom) | `platform` |
| Assinatura | admin/backend | `purchase` | `Subscribe` | `value: 399`, `currency: BRL`, `transaction_id` |
| Falar com especialista | site/admin | `generate_lead` | `Lead` | `cta_location` |

Regras:
- Eventos só disparam quando a ação **aconteceu** (conta criada com sucesso, não clique no botão).
- `Subscribe`/`purchase` de preferência a partir do backend (confirmação do pagamento), não do front.
- Conversão para otimizar anúncios: começar com `CompleteRegistration` (volume) e migrar para `ViewPreview`
  ou `Subscribe` quando houver ~50 eventos/semana.

## Implementação

- **GA4:** uma propriedade "Korza", um fluxo web, com **medição entre domínios** (`korza.com.br` + `admin.korza.app`)
  para a sessão não quebrar no cadastro.
- **Pixel da Meta:** o mesmo pixel nos dois domínios: `1174311258139587` (o da LP antiga, ver `conexoes/CONEXOES.md`).
- **Conversions API (Meta) do backend** para `CompleteRegistration` e `Subscribe`, com `event_id` igual ao do
  pixel (deduplicação). Recupera o que bloqueador de anúncio e iOS escondem. Fase 2b, depois do básico.
- **LGPD:** banner de consentimento + Consent Mode v2 do Google; Pixel só dispara marketing após consentimento.
  Pendente: o Pixel entrou no site em 2026-10-27 sem banner, por decisão do Pedro (ver `conexoes/CONEXOES.md`).
- **Código direto (gtag.js + fbq) em vez de GTM:** o Pedro mantém o código e o Claude edita; um lugar a menos
  para configurar. Rever se a quantidade de tags crescer.

## UTMs e atribuição

Padrão para todo link que a Korza controla:

| Parâmetro | Valores |
| --- | --- |
| `utm_source` | `meta`, `google`, `instagram`, `whatsapp`, `email` |
| `utm_medium` | `paid_social`, `cpc`, `organic_social`, `bio`, `outbound` |
| `utm_campaign` | `AAAA-MM-<slug>` (mesmo nome da pasta em `campanhas/`) |
| `utm_content` | id do criativo / variação (ex.: `reels-recompra-hookA`) |

**Guardar a origem na conta:** no cadastro, o admin salva as UTMs, o `fbclid`/`gclid` e a página de entrada
da primeira visita (first touch) junto da conta criada. Assim dá para saber qual campanha gerou cada
assinatura, inclusive no HubSpot, sem depender só do GA4/Meta.

## Métricas do relatório semanal

Visitas → cliques no CTA → contas criadas → previews vistos → assinaturas, por canal e campanha.
Custo por conta criada e por assinatura. Recompra e receita ficam fora (são resultado do cliente, não do marketing).
