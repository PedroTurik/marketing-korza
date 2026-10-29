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
| Rastreamento no admin | `korza/dev/admin` | ⬜ melhoria (ver `estrategia/plano-de-medicao.md`) |
| Google Ads | MCP `google-ads` (oficial do Google), conta de serviço | ✅ lê a conta `717-714-5646` (o MCP só tem leitura) |
| YouTube | YouTube Data + Analytics, OAuth do dono do canal (a conta de serviço não serve) | ⬜ APIs ativadas no projeto `korza-marketing`; falta a credencial OAuth (melhoria) |
| X | API paga | ⬜ fora por ora: uso manual (melhoria) |

## Como usar

- **GA4:** ferramentas `mcp__google-analytics__*`, propriedade `560905270`. Os relatórios têm de 24 a 48 h de atraso;
  para conferir na hora, `run_realtime_report`.
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

## Credenciais

| O quê | Onde | Observação |
| --- | --- | --- |
| Conta de serviço Google `leitor-marketing@korza-marketing.iam.gserviceaccount.com` | `~/.config/korza-marketing/google-sa.json` (600) | Projeto Cloud `korza-marketing` (`419588201628`), sem faturamento; APIs: Analytics Admin, Analytics Data, Search Console, Google Ads (acesso Explorer, até 2.880 operações/dia), YouTube (ativadas pelo Pedro em 2026-10-29, ainda sem credencial). Tem permissão acima de leitura no GA4 e no Search Console e é usuária **Padrão** no Google Ads; as ferramentas pedem só leitura. Se vazar: Cloud console → Contas de serviço → Chaves → excluir e gerar outra |
| Cliente OAuth "app de computador" do projeto `korza-marketing` | `~/.config/korza-marketing/google-oauth-client.json` (600) | Criado em 2026-10-29. Tela de consentimento **Externa**, modo **Em teste** (sem logo, sem verificação). Serve para o login do YouTube; com "Em teste" o token expira em 7 dias, então ao ligar o YouTube mudar para "Em produção" sem verificar. O segredo passou pelo chat: para app de computador o Google não o trata como confidencial, mas trocar se quiser (Credenciais → cliente → Redefinir secret) |
| Token Meta do usuário do sistema `leitor-marketing` (`122094640929536394`) | `~/.config/korza-marketing/meta.env` como `META_IG_TOKEN` (600) | Não expira. App `Korza Marketing`. Permissões de leitura e de escrita (`ads_management`, `instagram_content_publish`, `instagram_manage_comments`, `instagram_manage_messages`, `pages_manage_ads`…), por escolha do Pedro. Trocar: business.facebook.com/settings → Usuários do sistema → `leitor-marketing` → Revogar tokens → gerar outro e salvar com `read -rs T && printf 'META_IG_TOKEN=%s\n' "$T" > ~/.config/korza-marketing/meta.env` num terminal fora do Claude |
| Meta Ads e Meta devtools (MCP) | Login OAuth pelo `/mcp` | Sem modo só leitura: a trava é a regra da casa e a confirmação a cada chamada de escrita. Exceção liberada pelo Pedro no `.claude/settings.local.json`: `devtools_app_use_cases_manage` |

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
