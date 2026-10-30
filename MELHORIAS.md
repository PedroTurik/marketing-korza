# Melhorias

O que enriquece o hub, mas não trava o trabalho. Cada item entra quando houver motivo (uma campanha, um relatório).
Ao fazer, apagar a linha daqui e registrar onde ficou.

## Medição e site

- **`noindex` no `public.korza.app`:** cabeçalho `X-Robots-Tag: noindex` na rota `website-banner/:idOrHostname/rendered`
  (`korza/dev/backend/src/controllers/website-banner.controller.ts`), com quem cuida do backend. A remoção temporária
  no Search Console (pedida em 2026-10-27 para `admin.korza.app` e `public.korza.app`) vale até ~2027-04-27.
- **Sessões de "Paid Search" sem campanha:** o GA4 mostrou 12 sessões, com engajamento zero, nos 28 dias até 2026-10-29,
  e a conta do Google Ads não tem campanha. Provável tráfego automático; olhar quando o relatório semanal for rodar.
- **Guardar a origem na conta:** o admin salva UTMs, `fbclid`/`gclid` e a página de entrada junto da conta criada
  (`estrategia/plano-de-medicao.md`, "UTMs e atribuição").
- **Tag do Google Ads e conversão de cadastro:** pôr `AW-18544776538` no site e importar o `sign_up` do GA4 como
  conversão principal no Google Ads. Antes da primeira campanha no Google, depois do PR do admin.
- **Conversions API pelo backend:** `CompleteRegistration` e `Subscribe` com `event_id` igual ao do Pixel. Depois do
  PR do admin.

## SEO

- **Leva de 11 páginas no Site-Korza** (branch `seo`): 3 páginas de solução, 4 guias e 4 artigos, com o mapa em
  `seo/keywords.md` e as decisões em `seo/estrategia.md`. Sem pré-requisitos pendentes.
  `/precos/` só depois dos planos novos; `/cases/` quando houver mais material por case.

## Dados e rotina

- **Script de métricas + relatório semanal (Fase 4):** Instagram (alcance, views, salvamentos, compartilhamentos,
  seguidores, público) e campanhas da Korza Brasil, pela Graph API com o token (`conexoes/CONEXOES.md`, "Como usar").
  Fazer o primeiro relatório à mão e depois virar script/skill.

- **Acesso Básico na API do Google Ads:** com o acesso Explorer, o Planejador de palavras-chave pela API é bloqueado
  (`DEVELOPER_TOKEN_NOT_APPROVED`, testado em 2026-10-29). Com o Básico, o Claude pesquisa keywords sozinho. O pedido no
  Centro de API da conta falhou em 2026-10-29; tentar de novo depois. Até lá, o Pedro exporta pela interface.

## Canais

- **YouTube:** as APIs já estão ativadas no `korza-marketing`. O cliente OAuth "app de computador" já existe (`conexoes/CONEXOES.md`, Credenciais). Falta
  fazer o login único com a conta dona do canal (escolher o canal da Korza, não a conta pessoal), guardar o token em
  `~/.config/korza-marketing/` e escrever `conexoes/youtube.py` só para leitura. Upload pela API fica de fora: com o app
  não verificado, os vídeos ficam presos como privados até uma auditoria do Google.
- **X:** a conta existe, mas usamos manualmente (reposts de cortes e carrosséis). A API é paga, e o público
  (lojistas Nuvemshop/Shopify) está pouco lá. Só reavaliar se o canal mostrar tração; antes, conferir o preço atual.

## Limpeza

- **Quiz:** excluir o projeto `quiz-korza` no Cloudflare (o `quiz-korza.pages.dev` ainda abre, com o Pixel do quiz) e
  a Edge Function `meta-pageview` no Supabase (mandava os eventos do quiz para a Meta pelo servidor); confirmar que o botão do quiz saiu do app `korza-brownies` (`dev/mobile/tenants/korza-brownies/dynamic/bundle.ts`).
- **Conta de teste do onboarding:** `pedroturik+2026103001@gmail.com` (pedido `QFFnW4`, "Korza Brownies Teste", telefone
  fictício) ficou parada na etapa de notificação, sem criar loja. Apagar quando for conveniente.

O que **trava** a mídia paga (PR do admin, privacidade e banner, case da home) saiu daqui e está em
`estrategia/plano-90-dias.md`, "Portões da mídia paga para o cadastro".
