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

- **Acesso Básico na API do Google Ads:** com o acesso Explorer, o Planejador de palavras-chave pela API é bloqueado
  (`DEVELOPER_TOKEN_NOT_APPROVED`, testado em 2026-10-29). Com o Básico, o Claude pesquisa keywords sozinho. Pedido no
  Centro de API da conta (formulário; o Google responde em alguns dias). Até lá, o Pedro exporta pela interface.

## Canais

- **YouTube:** as APIs já estão ativadas no `korza-marketing`. Falta criar uma credencial OAuth "app de computador",
  fazer o login único com a conta dona do canal (escolher o canal da Korza, não a conta pessoal), guardar o token em
  `~/.config/korza-marketing/` e escrever `conexoes/youtube.py` só para leitura. Upload pela API fica de fora: com o app
  não verificado, os vídeos ficam presos como privados até uma auditoria do Google.
- **X:** a conta existe, mas usamos manualmente (reposts de cortes e carrosséis). A API é paga, e o público
  (lojistas Nuvemshop/Shopify) está pouco lá. Só reavaliar se o canal mostrar tração; antes, conferir o preço atual.

- **Ações diárias coordenadas entre canais:** a mesma pauta desdobrada no dia em Instagram, X, YouTube (Shorts e
  vídeos) e outros, com cortes e adaptações por canal. Entra depois que o Instagram estiver rodando com a grade de
  `estrategia/linha-editorial.md` (e o YouTube com OAuth, se for ler métricas).

## Limpeza

- **Quiz:** excluir o projeto `quiz-korza` no Cloudflare (o `quiz-korza.pages.dev` ainda abre, com o Pixel do quiz) e
  a Edge Function `meta-pageview` no Supabase (mandava os eventos do quiz para a Meta pelo servidor); confirmar que o botão do quiz saiu do app `korza-brownies` (`dev/mobile/tenants/korza-brownies/dynamic/bundle.ts`).
- **Token da Meta:** o atual passou pelo chat; trocar quando for conveniente (passo a passo em `conexoes/CONEXOES.md`).
