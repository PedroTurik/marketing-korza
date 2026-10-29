# Melhorias

O que enriquece o hub, mas não trava o trabalho. Cada item entra quando houver motivo (uma campanha, um relatório).
Ao fazer, apagar a linha daqui e registrar onde ficou.

## Medição e site

- **PR do admin (`korza/dev/admin`, branch `dev`): GA4, Pixel, `sign_up`/`CompleteRegistration` e `noindex`.**
  Fazer antes da primeira campanha paga que leve ao cadastro: sem isso não se mede conta criada e a Meta não otimiza.
  Detalhe em `estrategia/plano-de-medicao.md` ("Admin").
- **`noindex` no `public.korza.app`:** cabeçalho `X-Robots-Tag: noindex` na rota `website-banner/:idOrHostname/rendered`
  (`korza/dev/backend/src/controllers/website-banner.controller.ts`), com quem cuida do backend. A remoção temporária
  no Search Console (pedida em 2026-10-27 para `admin.korza.app` e `public.korza.app`) vale até ~2027-04-27.
- **Banner de consentimento (LGPD):** banner próprio (Aceitar/Recusar) no site e no admin; Pixel e sinais de anúncio
  do Google só após o aceite. Junto, revisar a política de privacidade: a seção 7 nega cookies de marketing, conferir
  os contatos `@korza.app`, falta a seção 11. Hoje o Pixel roda sem banner, por decisão do Pedro (2026-10-27).
- **Guardar a origem na conta:** o admin salva UTMs, `fbclid`/`gclid` e a página de entrada junto da conta criada
  (`estrategia/plano-de-medicao.md`, "UTMs e atribuição").
- **Tag do Google Ads e conversão de cadastro:** pôr `AW-18544776538` no site e importar o `sign_up` do GA4 como
  conversão principal no Google Ads. Antes da primeira campanha no Google, depois do PR do admin.
- **Conversions API pelo backend:** `CompleteRegistration` e `Subscribe` com `event_id` igual ao do Pixel. Depois do
  PR do admin.

## Dados e rotina

- **Script de métricas + relatório semanal (Fase 4):** Instagram (alcance, views, salvamentos, compartilhamentos,
  seguidores, público) e campanhas da Korza Brasil, pela Graph API com o token (`conexoes/CONEXOES.md`, "Como usar").
  Fazer o primeiro relatório à mão e depois virar script/skill.

## Limpeza

- **Quiz:** excluir o projeto `quiz-korza` no Cloudflare (o `quiz-korza.pages.dev` ainda abre, com o Pixel do quiz) e
  a Edge Function `meta-pageview` no Supabase (mandava os eventos do quiz para a Meta pelo servidor); confirmar que o botão do quiz saiu do app `korza-brownies` (`dev/mobile/tenants/korza-brownies/dynamic/bundle.ts`).
- **Token da Meta:** o atual passou pelo chat; trocar quando for conveniente (passo a passo em `conexoes/CONEXOES.md`).
