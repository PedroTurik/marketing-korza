# Plano de medição

O que medir, onde e com qual nome. Sem isso, anúncio roda às cegas e o Meta/Google não conseguem
otimizar para quem cria conta e assina. Criado em 2026-10-26.

## Situação em 2026-10-27

- **Site (`korza.app`):** GA4 `G-HR907RLPTS` e Pixel `1174311258139587` no ar (`page_view`/`PageView`), código direto,
  sem banner de consentimento. O link "Criar conta" repassa o `fbclid`.
- **Admin (`admin.korza.app`):** nada instalado ainda. É a próxima melhoria (seção "Admin" abaixo; `MELHORIAS.md`).

## Funil e eventos

O funil vai do site (`korza.app`) ao produto (`admin.korza.app`). Os dois estão no mesmo domínio, então os cookies do
GA4 e do Pixel valem no site e no cadastro sem configuração entre domínios.

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

- **GA4:** uma propriedade "Korza", um fluxo web (`G-HR907RLPTS`) no site e no admin.
- **Pixel da Meta:** o mesmo pixel no site e no admin: `1174311258139587` (`Korza - Site`, ver `conexoes/CONEXOES.md`).
- **Conversions API (Meta) do backend** para `CompleteRegistration` e `Subscribe`, com `event_id` igual ao do
  pixel (deduplicação). Recupera o que bloqueador de anúncio e iOS escondem. Melhoria, depois do admin (`MELHORIAS.md`).
- **LGPD:** banner de consentimento + Consent Mode v2 do Google; Pixel só dispara marketing após consentimento.
  Pendente: o Pixel entrou no site em 2026-10-27 sem banner, por decisão do Pedro (ver `MELHORIAS.md`).
- **Código direto (gtag.js + fbq) em vez de GTM:** o Pedro mantém o código e o Claude edita; um lugar a menos
  para configurar. Rever se a quantidade de tags crescer.

## Admin (melhoria pendente)

Repositório `korza/dev/admin` (React + Vite). Um PR só, para a branch `dev`, quando o Pedro pedir:

1. **GA4** `G-HR907RLPTS` no `index.html`, com o mesmo Consent Mode do site (sinais de anúncio negados por padrão).
2. **Pixel** `1174311258139587` no `index.html` + `PageView` a cada troca de rota (é SPA; o código base só dispara no
   primeiro carregamento). O Pixel lê o `fbclid` da URL e grava o `_fbc`.
3. **`sign_up` (GA4) + `CompleteRegistration` (Pixel)** só após a conta ser criada com sucesso
   (`src/pages/create-account.page.tsx`), com `method` e `platform`. Pixel com correspondência avançada (e-mail da
   conta, criptografado pelo próprio Pixel) e `eventID` guardado para deduplicar com a Conversions API.
4. **`noindex`:** `<meta name="robots" content="noindex">` no `index.html` (o Google indexou `/create-account` e
   `/account-deletion/<loja>`; a página de exclusão continua acessível para as lojas de apps).
5. **Depois, no mesmo padrão:** `store_connected`/`ConnectStore`, `preview_view`/`ViewPreview`. `Subscribe` fica para
   o backend. Quando o banner entrar no site, entra igual no admin.

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
