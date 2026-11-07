# Conexões

Como o hub lê (e, com OK, escreve) nos canais. Regra: **leitura por padrão; qualquer escrita (subir
campanha, publicar, responder) só depois de mostrar o plano e receber OK para aquele plano.**
Segredos em `~/.config/korza-marketing/` (fora do git), nunca em arquivo versionado nem colados no chat.

Fase 2 concluída em 2026-10-27. O que falta enriquecer está em [../MELHORIAS.md](../MELHORIAS.md).

## Status

| Conexão | Como | Status |
| --- | --- | --- |
| GA4 | MCP `google-analytics` (`.mcp.json`), conta de serviço | ✅ lê (sem `--allow-write`) |
| Search Console | `uv run conexoes/search_console.py`, conta de serviço | ✅ lê `sc-domain:korza.app` (padrão) e `sc-domain:korza.com.br` (`--site`) |
| Meta Ads | MCP `meta-ads` (`https://mcp.facebook.com/ads`) | 🟨 lê e escreve na conta **Korza** (USD); a **Korza Brasil** ainda não foi liberada no MCP pela Meta: usar a API (abaixo) |
| Meta Ads + Instagram pela API | Graph API com o token do usuário do sistema `leitor-marketing` | ✅ lê a Korza Brasil e os insights do @korza.br; o token também escreve |
| Meta devtools | MCP `meta-devtools` (`https://mcp.facebook.com/devtools`) | ✅ lê e configura apps da Meta (criou o app `Korza Marketing`) |
| Rastreamento no site | GA4 + Pixel em código direto no `korza/dev/Site-Korza` | ✅ no ar em `korza.app` (`page_view`/`PageView`), sem banner de consentimento |
| Rastreamento no admin e Conversions API | `korza/dev/admin` + `korza/dev/backend` | ✅ no ar desde 2026-11-07 (`estrategia/plano-de-medicao.md`) |
| Google Ads | MCP `google-ads` (oficial do Google), conta de serviço | ✅ lê a conta `717-714-5646` (o MCP só tem leitura) |
| YouTube | YouTube Data + Analytics, OAuth do dono do canal (a conta de serviço não serve) | ⬜ APIs ativadas e cliente OAuth criado; falta o login do dono do canal (melhoria) |
| X | API paga | ⬜ fora por ora: uso manual (melhoria) |
| HubSpot e Chatwoot | `python3 -m outbound status`, em `korza/crm-automacao` | ✅ lê o funil por etapa. Somente leitura para o hub: nunca `--executar`, `mover`, `importar` ou `setup` |
| ElevenLabs (voz) | API REST `api.elevenlabs.io`, chave em `elevenlabs.env` | ✅ gera locução (plano Starter, uso comercial). Voz padrão da Korza: **Bea**. Música: Eleven Music liberada pelo Pedro (ver abaixo) |

## Como usar

- **GA4:** ferramentas `mcp__google-analytics__*`, propriedade `560905270`. Os relatórios têm de 24 a 48 h de atraso;
  para conferir na hora, `run_realtime_report`. Toda leitura filtra `hostName` em `korza.app` e `admin.korza.app`:
  o site rodando local manda eventos de `localhost`/`127.0.0.1` para a mesma propriedade.
- **Pixel `Korza - Site`:** `ads_get_dataset_stats` e a Visão geral do Gerenciador de Eventos contam o bruto recebido.
  Cada cadastro chega ~3 vezes (navegador, nosso servidor e a cópia automática da Meta), desduplicadas pelo `eventId`:
  4 contas em 2026-11-07 apareceram como 12–13 `CompleteRegistration`. Contar cadastros pelo banco ou pelo GA4.
- **Search Console:** `uv run conexoes/search_console.py --por query|page|date --dias 28` (ver o cabeçalho do script).
  Cerca de 2 dias de atraso.
- **Meta Ads (MCP):** usar o `ad_account_id` sem `act_`. Se `is_ads_mcp_enabled` for `false` (hoje, Korza Brasil),
  ler pela API.
- **Google Ads:** ferramentas `mcp__google-ads__*`, `customer_id` `7177145646` (sem hífens), sem `login_customer_id`.
  Antes de montar uma consulta no `search`, ver os campos com `get_resource_metadata`.
- **Graph API (Korza Brasil, Instagram):**
  ```
  set -a; . ~/.config/korza-marketing/meta.env; set +a   # define META_IG_TOKEN
  curl -s -G https://graph.facebook.com/v23.0/act_1982997825669595/campaigns \
    --data-urlencode fields=name,status,objective --data-urlencode access_token=$META_IG_TOKEN
  curl -s -G https://graph.facebook.com/v23.0/17841473916924433/insights --data-urlencode metric=reach,views \
    --data-urlencode metric_type=total_value --data-urlencode period=day --data-urlencode access_token=$META_IG_TOKEN
  ```
  Nunca imprimir o token. `amount_spent` da conta vem em centavos.

- **ElevenLabs (voz padrão da Korza):** voz **Bea – Calm & Friendly** (`voice_id` `cabLxBh81HurPAAJfEHo`, biblioteca,
  PT-BR), escolhida pelo Pedro em 2026-11-05. Configuração aprovada: modelo `eleven_v3`, `language_code` `pt`,
  `stability` 0.5, `speed` 1.05, tags de tom no texto (`[curious]` na pergunta, `[confident]` na afirmação). Números por
  extenso ("quatorze dias úteis"). Use o endpoint `/with-timestamps` para ter o tempo de cada palavra (legenda):
  ```
  set -a; . ~/.config/korza-marketing/elevenlabs.env; set +a   # define ELEVENLABS_API_KEY
  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/cabLxBh81HurPAAJfEHo/with-timestamps?output_format=mp3_44100_128" \
    -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
    -d '{"text":"[curious] ... [confident] ...","model_id":"eleven_v3","language_code":"pt","voice_settings":{"stability":0.5,"speed":1.05}}'
  ```
  Resposta: `audio_base64` + `alignment` por caractere (exemplo de conversão em palavras: `studio/motion/2026-11-05-m1-notificacao/assets/audio/vo-words.json`).
  O Starter só sai em até 128 kbps (192 é do Creator). **Trilha:** Eleven Music (`POST /v1/music`), por decisão do Pedro em
  2026-11-05, mesmo com os planos Starter a Pro marcados "For Individual Use Only" (risco de licença aceito por ele). A
  chave ganhou a permissão Music Generation em 2026-11-05. Reserva sem risco: trilha própria de `studio/kit/audio/`.

## Credenciais

| O quê | Onde | Observação |
| --- | --- | --- |
| Conta de serviço Google `leitor-marketing@korza-marketing.iam.gserviceaccount.com` | `~/.config/korza-marketing/google-sa.json` (600) | Projeto Cloud `korza-marketing` (`419588201628`), sem faturamento; APIs: Analytics Admin, Analytics Data, Search Console, Google Ads (acesso Explorer, até 2.880 operações/dia), YouTube (ativadas pelo Pedro em 2026-10-29; usam o cliente OAuth abaixo). Tem permissão acima de leitura no GA4 e no Search Console e é usuária **Padrão** no Google Ads; as ferramentas pedem só leitura. Se vazar: Cloud console → Contas de serviço → Chaves → excluir e gerar outra |
| Cliente OAuth "app de computador" do projeto `korza-marketing` | `~/.config/korza-marketing/google-oauth-client.json` (600) | Criado em 2026-10-29. Tela de consentimento **Externa**, modo **Em teste** (sem logo, sem verificação). Serve para o login do YouTube; com "Em teste" o token expira em 7 dias, então ao ligar o YouTube mudar para "Em produção" sem verificar. O segredo passou pelo chat: para app de computador o Google não o trata como confidencial, mas trocar se quiser (Credenciais → cliente → Redefinir secret) |
| Token Meta do usuário do sistema `leitor-marketing` (`122094640929536394`) | `~/.config/korza-marketing/meta.env` como `META_IG_TOKEN` (600) | Não expira. App `Korza Marketing`. Permissões de leitura e de escrita (`ads_management`, `instagram_content_publish`, `instagram_manage_comments`, `instagram_manage_messages`, `pages_manage_ads`…), por escolha do Pedro. Trocar: business.facebook.com/settings → Usuários do sistema → `leitor-marketing` → Revogar tokens → gerar outro e salvar com `read -rs T && printf 'META_IG_TOKEN=%s\n' "$T" > ~/.config/korza-marketing/meta.env` num terminal fora do Claude |
| Token da Conversions API (Pixel `Korza - Site`) | `~/.config/korza-marketing/meta-capi.env` (600): `META_CAPI_PIXEL_ID`, `META_CAPI_ACCESS_TOKEN`, `META_CAPI_TEST_EVENT_CODE` | Gerado pelo Pedro no Gerenciador de Eventos em 2026-11-06. Usuário de sistema da "Conversions API Application", não expira, só envia eventos ao Pixel. Vai para `APP__META_CAPI__ACCESS_TOKEN` no backend de produção (`estrategia/plano-de-medicao.md`). Passou pelo chat com OK do Pedro. Trocar: Gerenciador de Eventos → Pixel → Configurações → API de Conversões → gerar outro |
| Meta Ads e Meta devtools (MCP) | Login OAuth pelo `/mcp` | Sem modo só leitura: a trava é a regra da casa e a confirmação a cada chamada de escrita. Exceção liberada pelo Pedro no `.claude/settings.local.json`: `devtools_app_use_cases_manage` |
| Chave da API ElevenLabs | `~/.config/korza-marketing/elevenlabs.env` como `ELEVENLABS_API_KEY` (600) | Plano **Starter** (pago, uso comercial), assinado pelo Pedro em 2026-11-05. Chave com permissão restrita: texto em fala e Voices: Read (sem User: Read). A chave passou pelo chat na criação: trocar em elevenlabs.io → Developers → API Keys e salvar a nova com `read -rs T && printf 'ELEVENLABS_API_KEY=%s\n' "$T" > ~/.config/korza-marketing/elevenlabs.env` num terminal fora do Claude |

## Ativos

**Google:** GA4 propriedade `560905270`, fluxo `Korza - Site` `G-HR907RLPTS` (`https://korza.app`, retenção de 14 meses).
Search Console: `sc-domain:korza.app` (sitemap `https://korza.app/sitemap.xml`) e `sc-domain:korza.com.br`
(Alteração de endereço para `korza.app` aceita em 2026-10-27).

**Meta**, portfólio **Korza** `1444893746669109` (o login do Pedro também enxerga Oryza Labs e Rumy: fora do escopo):

| Ativo | ID | Uso |
| --- | --- | --- |
| Conta **Korza Brasil** (BRL) | `1982997825669595` | **Única conta para campanhas novas.** Tem pagamento. Até 2026-10-27: ~R$ 3.342,74 gastos, 2 campanhas de leads pausadas |
| Conta **Korza** (USD) | `3921782194748691` | Arquivo: 25 campanhas pausadas (jun/2025 a mar/2026). Tem as listas de clientes (Shopify BR ~6 mil, Nuvemshop BR ~13 mil, Shopify US ~140 mil); compartilhar com a Korza Brasil quando precisar. Não apagar, não anunciar |
| Contas Korza BR / Korza - Appza (BRL) | `1302908798650805` / `907558995677158` | Vazias, sem pagamento. Não usar |
| Página Korza | `637153062822915` | Única Página |
| Instagram @korza.br | `17841473916924433` | Ligado à Página |
| Conjunto de dados `Korza - Site` | `1174311258139587` | **O pixel oficial** (site e admin). Ligado à Korza Brasil |
| `Korza - Quiz` | `1054973176864468` | Quiz desligado em 2026-10-27; para de receber sozinho |
| `[inutilizado] Korza` / `[antigo] Korza App` | `1564215361452780` / `1228288975461990` | Parados. Não criar conjunto novo nem apagar nenhum |
| App `Korza Marketing` | `1816904082855324` | Do hub. Caso de uso `INSTAGRAM_BUSINESS`, modo de desenvolvimento, contato `pedroturik@gmail.com` |
| Apps `Korza Chatwoot` / `Chatwoot Outbound WA` | `1145271577493835` / `2227610147973000` | Atendimento (vendas): não mexer |

O MCP não mostra quem tem acesso ao portfólio nem os pagamentos: isso é conferido na interface.

## Domínio e site

- **`korza.app` é o domínio principal** (sem `www`), desde 2026-10-27. `www.korza.app`, `korza.com.br` e
  `www.korza.com.br` redirecionam com 301 em um salto, preservando caminho, UTMs e `fbclid`. Motivo: site e admin no
  mesmo domínio (os cookies do Pixel e do GA4 valem no cadastro). Nunca deixar o `korza.com.br` expirar (Registro.br)
  nem sair do Search Console.
- Site: `korza/dev/Site-Korza`, Amplify `site-korza`, deploy automático no push da `main` (o Pedro faz o push).
  Política de privacidade: `https://korza.app/privacy-policy/`. `robots.txt` e `sitemap.xml` no ar.
- **Amplify:** depois de mudar regras de redirecionamento, esperar ~5 min e **reimplantar a `main` para limpar a CDN**
  (`s-maxage` de 1 ano). Testar com `curl -H 'Accept-Encoding: gzip, deflate, br'`, senão o curl pega outra variação
  do cache e engana.
- **DNS no Route 53 (AWS).** No `korza.app`, não mexer: `admin.korza.app` (CloudFront), e-mail no Lark (MX
  `mx1-3.larksuite.com`, SPF, TXT `verification-code-site-App_lark`), TXT `google-site-verification` e
  `facebook-domain-verification`. TXT novo entra como valor a mais no mesmo registro.
- O Pixel não dispara em navegador automatizado padrão; para testar, desligar `AutomationControlled` no Chromium.

**Google Ads:** conta **Korza** `717-714-5646` (BRL, `America/Sao_Paulo`, autotagging ligado), criada em 2026-10-29
pelo fluxo guiado (o modo especialista não apareceu), sem campanha e sem pagamento. Tag `AW-18544776538`, **ainda fora
do site**: entra como uma linha `gtag('config', 'AW-18544776538')` no gtag que já carrega o GA4, não como bloco novo.
Vinculada ao GA4 (`560905270`); as conversões importadas do GA4 (`purchase`, `qualify_lead`, `close_convert_lead`)
estão ocultas e sem uso.

## Configuração de MCP

Servidores em `marketing/.mcp.json`, sem segredos. O Claude Code precisa ser aberto dentro de `marketing/`.
O MCP do GA4 roda com `pipx run analytics-mcp`; o do Google Ads, com `pipx run --spec git+https://github.com/googleads/google-ads-mcp.git google-ads-mcp`,
sem developer token (o acesso à API é do projeto do Cloud desde 2026-09-09). Docs do MCP da Meta:
developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/

## Painel da Korza (admin.korza.app)

Leitura pela API `https://api.korza.app`, com a sessão da conta de administrador. Rotas no cliente gerado
`dev/admin/src/generated/korza-api-client/`. Login por magic link: pedir no formulário e o Pedro cola o endereço do botão, sem clicar.
Para telas, usar Playwright com viewport próprio (1440×900 e iPhone 390×844) e `locale: pt-BR`.

- Só leitura nas lojas reais. Korza Brownies pode ser alterada e pode receber push.
- Só rotas agregadas (`analytics/metrics/*`, `analytics/roi`, `campaigns`, `feature-flags`, `tenant-engagement`). Evitar
  `app-users`, `members` e os `drilldown`, que trazem dados de consumidores.
- Concluir o onboarding cria uma loja real "em construção"; não fazer em teste.
- Dados por loja ficam em `inbox/`, fora do git.
