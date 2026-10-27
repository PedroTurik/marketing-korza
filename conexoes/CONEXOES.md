# Conexões

Como o hub lê (e, com OK, escreve) nos canais. Regra: **leitura por padrão; qualquer escrita (subir
campanha, publicar, responder) só depois de mostrar o plano e receber OK para aquele plano.**
Segredos em `.env` ou em `~/.config/korza-marketing/` (fora do git), nunca em arquivo versionado.

## Status

| Conexão | Método | Status |
| --- | --- | --- |
| Rastreamento (GA4 + Pixel) no site e no admin | Código, ver `estrategia/plano-de-medicao.md` | 🟨 GA4 e Pixel no ar no site (código direto, sem GTM); falta admin (ver "PR do admin") e banner de consentimento |
| GA4 | MCP oficial do Google (`analytics-mcp`, servidor `google-analytics` em `.mcp.json`), conta de serviço | ✅ leitura testada em 2026-10-27 (propriedade `properties/560905270`, `G-HR907RLPTS`); sem `--allow-write` |
| Search Console | Script `conexoes/search_console.py` (`uv run`), conta de serviço | ✅ leitura testada em 2026-10-27 (`sc-domain:korza.app`, padrão do script; `sc-domain:korza.com.br` com `--site`) |
| Meta Ads | MCP oficial da Meta (`https://mcp.facebook.com/ads`, em `.mcp.json`) | 🟨 conectado (2026-10-27); a conta das campanhas, "Korza Brasil" (`1982997825669595`), ainda não tem o MCP liberado (liberação gradual da Meta) |
| Pixel da Meta | Reaproveitar o pixel da LP antiga `1174311258139587` | 🟨 no ar no site desde 2026-10-27 (`PageView` conferido), sem banner por decisão do Pedro; falta admin |
| Instagram @korza.br | MCP da Meta (posts) + script próprio (Instagram Graph API, métricas) | 🟨 o MCP já lista os posts com curtidas e comentários (IG `17841473916924433`, Página `637153062822915`, via conta "Korza" `3921782194748691`); token do usuário do sistema funcionando (2026-10-27): insights do Instagram e a conta Korza Brasil pela API; falta o script |
| Google Ads | MCP oficial do Google (`googleads/google-ads-mcp`), só leitura | ⬜ conta não existe; criar só quando houver plano de campanha no Google |

Repositórios: site em `korza/dev/Site-Korza` (Amplify, deploy automático no push da `main`).

## Para retomar (fim da 3ª sessão de 2026-10-27)

**Migração para `korza.app`: concluída** (passos em "Domínio: tudo em korza.app"). Conferido por Claude: conta de
serviço lê `sc-domain:korza.app`; sitemap lido sem erros (2 URLs); fluxo do GA4 em `https://korza.app`; TXT
`facebook-domain-verification` no DNS; padrão do `search_console.py` em `korza.app`. Confirmado pelo Pedro: Alteração
de endereço aceita, `korza.app` verificado na Meta, links antigos trocados.
Achado para a frente de SEO: na propriedade `korza.app` o Google mostra páginas de `admin.korza.app`
(`/create-account`, `/account-deletion/<loja>`) e de `public.korza.app/website-banner/<loja>/rendered`, com o
domínio de lojas clientes na URL. Avaliar `noindex` nesses dois hosts (é código do produto, fora do hub).

**Fila da Fase 2, em ordem** (atualizada em 2026-10-27, 3ª sessão):

1. ✅ Faxina de acesso no portfólio (Pedro).
2. ✅ `Korza - Site` ligado à conta Korza Brasil (Pedro; o MCP não confirma porque ainda não lê a Korza Brasil).
3. ✅ App `Korza Marketing` `1816904082855324` criado pelo MCP `meta-devtools` (contato `pedroturik@gmail.com`),
   vinculado ao portfólio Korza, caso de uso `INSTAGRAM_BUSINESS`. Em modo de desenvolvimento.
4. ✅ Usuário do sistema `leitor-marketing` com token em `~/.config/korza-marketing/meta.env` (testado em 2026-10-27:
   Instagram e Korza Brasil leem; token anterior revogado). **Token com escrita** (`ads_management`,
   `instagram_content_publish`, `instagram_manage_comments`, `instagram_manage_messages`, `pages_manage_ads`), por
   escolha do Pedro: os scripts só leem por padrão; qualquer escrita segue a regra da casa (plano + OK).
5. Script de métricas (Claude): Instagram + campanhas da Korza Brasil.
6. PR do admin na branch `dev` (ver "PR do admin"), quando o Pedro pedir.
7. Conversions API pelo backend (Fase 2b), depois do básico rodando.

**Esperando terceiros / depois:** conta "Korza Brasil" ser liberada no MCP da Meta (testada em 2026-10-27, 3ª sessão: ainda bloqueada);
banner de consentimento (política em `https://korza.app/privacy-policy/`; revisar o texto da seção 7, que nega cookies
de marketing, e os contatos `@korza.app`; falta a seção 11); conta do Google Ads só quando for anunciar no Google; desligar o quiz e
tirar o link do app `korza-brownies`; remoto no GitHub para o hub (hoje sem backup fora da máquina).

**3ª sessão:** migração para `korza.app` fechada; app `Korza Marketing` criado e vinculado.
**1ª sessão:** conjuntos de dados da Meta identificados e renomeados; Pixel `1174…` no ar no site com
repasse do `fbclid`; domínios verificados (Meta e Search Console); GA4 (MCP) e Search Console (script)
conectados com conta de serviço; `korza.com.br` → `www` com 301 e `canonical`; o MCP da Meta lê os posts do
Instagram (curtidas e comentários); primeiro commit do hub.
**2ª sessão:** mapa do portfólio Meta; política de privacidade no site novo; site migrado para `korza.app` com 301 dos
outros três endereços (UTMs e `fbclid` preservados, Pixel e GA4 conferidos); `robots.txt` e `sitemap.xml`.

## Mapa do portfólio Korza na Meta (levantado em 2026-10-27)

Portfólio **Korza** `1444893746669109`. O login do Pedro também enxerga Oryza Labs (3) e Rumy: fora do escopo.

| Ativo | ID | Situação | Decisão |
| --- | --- | --- | --- |
| Conta **Korza Brasil** (BRL) | `1982997825669595` | Principal (Pedro). O MCP ainda não lê (liberação gradual); a API lê pelo token do `leitor-marketing`. ~R$ 3.342,74 gastos na vida da conta; 2 campanhas de leads pausadas (`CBO - Leads`, `ABO - Leads - Testes`) | **Única conta para campanhas novas** |
| Conta **Korza** (USD) | `3921782194748691` | 25 campanhas, todas pausadas, ~US$ 1.466 de jun/2025 a mar/2026 (leads, WhatsApp, engajamento, testes nos EUA). Tem as listas de clientes | Arquivo: não apagar, não anunciar. Listas úteis são compartilhadas com a Korza Brasil |
| Contas **Korza BR** e **Korza - Appza** (BRL) | `1302908798650805` / `907558995677158` | Vistas em 2026-10-27 (3ª sessão): vazias, sem forma de pagamento, **liberadas no MCP** | Não usar (Pedro, 2026-10-27): tudo fica na Korza Brasil e na Korza |
| Página Korza | `637153062822915` | Única Página do portfólio | Usar |
| Instagram @korza.br | `17841473916924433` | Ligado à Página | Usar |
| Conjunto de dados `Korza - Site` | `1174311258139587` | Recebendo `PageView` do site novo | **O pixel oficial** (site e admin) |
| `Korza - Quiz` | `1054973176864468` | Ainda recebe eventos (navegador e servidor) pelo botão do app `korza-brownies` | Desligar quando o Pedro quiser |
| `[inutilizado] Korza` / `[antigo] Korza App` | `1564215361452780` / `1228288975461990` | Parados (dez/2025 / nunca) | Deixar quieto |
| Apps `Korza Chatwoot` e `Chatwoot Outbound WA` | `1145271577493835` / `2227610147973000` | WhatsApp/atendimento (vendas, fora do hub) | Não mexer |

Política de privacidade: `https://korza.app/privacy-policy/` (commit `fe79c76` no site, 2026-10-27; a antiga em
`korza.app` saiu do ar). É o link para o banner e para os apps da Meta. O texto (18/12/2025) diz que não há cookies de
marketing, o que já não vale com o Pixel e o GA4: revisar junto com o banner.

O MCP não mostra quem tem acesso ao portfólio, quem é dono da Korza Brasil, nem os pagamentos. Isso é conferido na
interface (ver "Para retomar").

## Domínio: tudo em korza.app (decidido em 2026-10-27)

Decisão do Pedro: `korza.app` vira o domínio principal do site (sem `www`); `www.korza.app`, `korza.com.br` e
`www.korza.com.br` redirecionam com 301 preservando o caminho. Motivo: site e admin no mesmo domínio (cookies do
Pixel e do GA4 valem no cadastro), um domínio para site, plataforma e e-mail; o histórico do `.com.br` no Google era
pequeno. Nunca deixar o `korza.com.br` expirar (Registro.br) nem sair do Search Console.

Antes da migração, no DNS do `korza.app` (Route 53): raiz sem registro A, `www` inexistente. Continua vivo e **não
pode ser mexido**: `admin.korza.app` (CloudFront), e-mail no Lark (MX `mx1-3.larksuite.com`, SPF, TXT
`verification-code-site-App_lark`) e um TXT `google-site-verification` (a conta de serviço ganhou acesso a
`sc-domain:korza.app` em 2026-10-27). TXT novos entram como valores a mais no mesmo registro.

Passos (status):
1. ✅ Push da política de privacidade (`fe79c76`).
2. ✅ Amplify `site-korza`: domínio `korza.app` (raiz + `www`).
3. ✅ Push da `canonical` em `korza.app` (`7e8ccf4`).
4. ✅ Regras 301 no Amplify (`www.korza.app`, `korza.com.br`, `www.korza.com.br` → `https://korza.app/<*>`). Levaram
   ~5 min para valer depois de salvas. A raiz `https://korza.com.br/` ficou presa no cache da CDN (cópia Brotli de
   quando a regra ainda não valia; `s-maxage` de 1 ano): **depois de mudar regras, reimplantar a `main` para limpar
   a CDN**. Testar com `Accept-Encoding: gzip, deflate, br`, senão o curl pega outra variação e engana.
5. ✅ Search Console: propriedade `korza.app`, conta de serviço como usuário, sitemap, padrão do `search_console.py`.
   Alteração de endereço aceita (Pedro).
6. ✅ GA4: URL do fluxo em `https://korza.app`. ✅ Meta: `korza.app` verificado no portfólio por TXT.
7. ✅ Trocar links antigos: app Korza Chatwoot (URL de privacidade), listagem do app na Shopify, bio do Instagram — Pedro.
8. ✅ Conferido em 2026-10-27: 301 em um salto preservando caminho, UTMs e `fbclid`; `canonical` em `korza.app`;
   admin e MX intactos; Pixel `1174…` (`PageView`) e GA4 (`page_view`) disparam com `dl=https://korza.app/…`.

## Estado em 2026-10-27 (passagem de sessão)

- **GA4:** no ar no site, sem GTM (decisão: código direto). Pedro configurou os domínios
  (`korza.com.br` + `admin.korza.app`) e a retenção de 14 meses. Falta: eventos no admin.
- **Pixel:** o Gerenciador de Eventos já tem 5 conjuntos de dados. Não criar novo e não apagar nenhum. Renomeados pelo Pedro em 2026-10-27.
  Investigado pelo MCP da Meta em 2026-10-27 (todos se chamam "Korza" na API, por isso a confusão):
  - `1174311258139587` = **LP antiga** em `https://www.korza.com.br/`. Criado em 2025-11-24. Só `PageView`
    (~258 em 28 dias). Último evento em 2026-10-20 15:46 (BRT), 3 min antes do deploy do site novo no Amplify
    (commit `c07b241`, 15:49): **parou de receber eventos**, o site novo não tem o pixel. Já teve eventos de
    servidor (último em 2026-06-01). **É o pixel a reaproveitar no site e no admin.**
  - `1054973176864468` = **quiz de qualificação** em `quiz.korza.com.br` (e `quiz-korza.pages.dev`), **ainda no ar**.
    Pixel no HTML (`PageView` com `eventID`), `Lead` com valor ao concluir e Conversions API via Supabase Edge
    Function `meta-pageview`. Também usa GA (`generate_lead`) e PostHog. ~70 `PageView` em 28 dias, nenhum `Lead`.
    A origem do tráfego diário: o app do tenant `korza-brownies` (`dev/mobile/tenants/korza-brownies/dynamic/bundle.ts`)
    tem um botão para `http://quiz.korza.com.br/?utm_source=korzaapp`. Código-fonte do quiz não está em `korza/`.
  - `1564215361452780` (Korza): último evento em 2025-12-15. `1228288975461990` (Korza App): nunca recebeu evento.
    `2227610147973000` (Chatwoot Outbound WA) e o oculto não aparecem na listagem do BM pelo MCP (devem pertencer a
    outro dono ou estar só compartilhados).
  - Públicos: nas contas legíveis pelo MCP não há público de site baseado em pixel. A conta "Korza" (USD) tem
    listas de clientes (SHOPIFY BRASIL ~6 mil, NUVEM SHOP BR ~13 mil, SHOPIFY UNITED STATES ~140 mil) e lookalikes
    inativos. A conta "Korza Brasil" (BRL) não pode ser lida pelo MCP (liberação gradual da Meta).
  - Renomear no Gerenciador de Eventos (`Korza – Site` para o `1174…`, `Korza – Quiz` para o `1054…`,
    `[antigo] …` para os outros): aprovado pelo Pedro; o MCP não renomeia, é feito na interface.
  - Quiz: segundo o Pedro, está no ar mas não é mais usado. Ainda recebe visitas pelo botão do app
    `korza-brownies`. Tirar o link do app e desligar o quiz fica para quando o Pedro quiser.
- **Banner de consentimento: depois.** Em 2026-10-27 o Pedro decidiu ligar o Pixel no site **sem banner** e
  colocar o banner depois, ciente do risco de LGPD (coleta para anúncio sem consentimento). Quando entrar:
  banner próprio (Aceitar/Recusar); o Pixel e os sinais de anúncio do Google (`gtag('consent','update',…)`)
  passam a ligar só após o aceite. O banner aponta para uma política de privacidade, que **o site não tem**.
  A Korza tem política de privacidade (Pedro, 2026-10-27); pegar o link quando o banner for retomado.
- **Domínios verificados (2026-10-27):** `korza.com.br` no BM da Meta e no Search Console, por TXT no DNS
  (Route 53, AWS; o DNS do `korza.app` também está lá). O Pedro informou `korza.app` também verificado; no DNS
  dele não há TXT da Meta, então foi por outro método ou ainda falta. Os registros SPF e Lark dos dois domínios
  ficam intactos ao editar o TXT (no Route 53 é um registro TXT só por nome, com vários valores).
- **Site (`dev/Site-Korza`), commits `6b285e0` (Pixel `PageView`) e `6a11094` (repasse do `fbclid` no link
  "Criar conta", da URL ou do cookie `_fbc`; testado em Chromium):** Pedro faz o push. Depois, conferir pelo MCP
  (`ads_get_dataset_stats` do `1174…`, agregação `host`) se `www.korza.com.br` voltou a mandar eventos.
  **Push feito e conferido em 2026-10-27:** o site no ar carrega o Pixel e o `adClickId`; uma visita de teste
  (`?utm_source=claude-teste`) enviou `PageView` para o `1174…`. Obs.: o Pixel não dispara em navegador
  automatizado padrão; para testar, desligar `AutomationControlled` no Chromium.
- **Dois domínios:** um pixel só serve para `korza.com.br` e `admin.korza.app`, sem configuração por domínio na Meta.
  O cookie não atravessa os domínios, por isso o repasse do `fbclid`. Discutido levar tudo para um domínio só
  (`app.korza.com.br` ou o site em `korza.app`): resolveria os cookies, mas é decisão de marca e infraestrutura;
  por ora, mantido `.com.br` + `.app`.
- **GA4 entre domínios:** confirmado na tag publicada do `G-HR907RLPTS` (regra `korza.com.br` + `admin.korza.app`).
  Só vale quando o admin tiver a tag também.
- **Hub `marketing/`:** primeiro commit `d813e8c` (2026-10-27), na branch `master`. Sem remoto ainda
  (sem backup fora da máquina); sugerido criar um repo privado no GitHub.
- **Google Ads API mudou (verificado na doc do Google em 2026-10-27, página de 2026-10-19):** o developer token foi
  extinto em 2026-09-09 e a MCC não é mais necessária para começar. O acesso à API pertence ao **projeto do Google
  Cloud** (o mesmo "korza-marketing"): ativar a Google Ads API dá acesso de teste; para contas reais, pedir
  **Explorer** na página Google Ads API → Visão geral do Cloud console (revisão automática, até 2.880 operações/dia,
  o bastante para leitura). Projeto em teste gratuito ou sem faturamento pode ser recusado. Não pedir pela
  Central de API do Google Ads (não é mais processado). Conferir se o `google-ads-mcp` já aceita rodar sem token.
- **Conta do Google Ads:** só quando for anunciar no Google (ao criar, usar o modo especialista e "criar conta sem
  campanha"). O projeto "korza-marketing" no Google Cloud já existe (ver abaixo).

## Google Cloud e conta de serviço

- Projeto `korza-marketing` (número `419588201628`), sem faturamento por enquanto. APIs ativas: Google Analytics
  Admin, Google Analytics Data, Google Search Console.
- Conta de serviço `leitor-marketing@korza-marketing.iam.gserviceaccount.com`, sem papéis no projeto. Chave JSON em
  `~/.config/korza-marketing/google-sa.json` (permissão 600, fora do git). Se vazar: Cloud console → Contas de
  serviço → Chaves → excluir e gerar outra.
- O Pedro deu a ela permissões acima de leitura no GA4 e no Search Console (para editar se preciso). As ferramentas
  do hub continuam só lendo: o MCP do GA4 roda sem `--allow-write` e o script pede o escopo `webmasters.readonly`.
  Qualquer escrita segue a regra da casa (plano + OK).
- Para ligar o MCP do GA4: abrir o Claude Code dentro de `marketing/` e aprovar o servidor `google-analytics`
  na primeira vez (precisa de `pipx`).

## Primeiras observações dos dados (2026-10-27, para a frente de SEO)

- Search Console, 28 dias: a busca "korza" teve 17 cliques em 99 impressões, posição média 3,8 (a própria marca
  fora do 1º lugar; site novo de 2026-10-20). "korza ai" aparece com 19 impressões, posição 6,5.
- `korza.com.br` (sem www) e `www.korza.com.br` respondem 200 com o mesmo conteúdo, sem redirecionamento nem
  `canonical`: conteúdo duplicado para o Google e o GA4 registra os dois hosts. **Resolvido em 2026-10-27:**
  `<link rel="canonical" href="https://www.korza.com.br/">` (commit `304b27f`) e redirecionamento no Amplify de
  `korza.com.br/<*>` para `www.korza.com.br/<*>` (preserva `fbclid`/UTMs). Conferido: o redirecionamento saiu
  como 302 e foi ajustado pelo Pedro para **301** (permanente), conferido em 2026-10-27.
- O Google ainda mostra `quiz.korza.com.br` (19 impressões) e `www.korza.com.br/formulário` (página antiga, hoje 404).

## Instagram: app e token (em andamento)

O MCP da Meta já lista os posts (curtidas, comentários). Para métricas (passo a passo dado em 2026-10-27):

1. ✅ **App** `Korza Marketing` `1816904082855324`, criado pelo MCP `meta-devtools` em 2026-10-27, no portfólio
   **Korza** (app e ativos no mesmo BM: não deve precisar de revisão de app), caso de uso `INSTAGRAM_BUSINESS`.
   As permissões do token são opcionais nesse caso de uso: se o token não as oferecer, adicioná-las em
   developers.facebook.com/apps/1816904082855324 → Casos de uso → Personalizar.
2. **Usuário do sistema** em business.facebook.com/settings → Usuários → Usuários do sistema → `leitor-marketing`,
   função Funcionário → atribuir ativos: app `Korza Marketing`, Página `Korza` e Instagram `korza.br` (visualização /
   insights) e conta de anúncios **Korza Brasil** (só visualizar desempenho) → gerar token com validade "Nunca" e só
   `instagram_basic`, `instagram_manage_insights`, `pages_show_list`, `pages_read_engagement`, `business_management`,
   `ads_read`.
3. **Token** guardado pelo Pedro num terminal fora do Claude (não colar no chat), em
   `~/.config/korza-marketing/meta.env` como `META_IG_TOKEN=…`, permissão 600.

IDs: Instagram `17841473916924433` (@korza.br), Página `637153062822915`, BM `1444893746669109`.

## PR do admin (pendente)

Repositório `korza/dev/admin` (React + Vite) = `admin.korza.app`. Um PR só, para a branch `dev`, quando o Pedro
pedir. Conteúdo:

1. **GA4** `G-HR907RLPTS` no `index.html`, com o mesmo Consent Mode do site (sinais de anúncio negados por padrão).
   Com isso a medição entre domínios passa a valer (o admin lê o `_gl` que o site já acrescenta).
2. **Pixel** `1174311258139587` no `index.html` + `PageView` a cada troca de rota (é SPA; o `PageView` do código
   base só dispara no primeiro carregamento). O Pixel lê o `fbclid` da URL sozinho e grava o `_fbc` no `korza.app`.
3. **`sign_up` (GA4) + `CompleteRegistration` (Pixel)** só após a conta ser criada com sucesso
   (`src/pages/create-account.page.tsx`), com `method` e `platform`. Pixel com correspondência avançada
   (e-mail da conta, enviado criptografado pelo próprio Pixel) e `eventID` guardado para a deduplicação com a
   Conversions API (Fase 2b).
4. **Depois, no mesmo padrão:** `store_connected`/`ConnectStore`, `preview_view`/`ViewPreview`. `Subscribe` fica
   para o backend.
5. **Banner de consentimento:** quando entrar no site, entra igual no admin.

Eventos e nomes em `estrategia/plano-de-medicao.md`.

## Ordem

1. **Google: criar as contas** (Pedro, ~30 min)
   - GA4: analytics.google.com → criar conta "Korza" → propriedade "Korza" (fuso São Paulo, BRL) →
     fluxo web `korza.com.br`. Anotar o **ID de medição** (`G-XXXXXXX`).
     Em Administrador → Fluxos → Configurar tag → Configurar domínios: incluir `korza.com.br` e `admin.korza.app`.
   - Search Console: search.google.com/search-console → propriedade de **Domínio** `korza.com.br` → registro
     TXT no DNS.
   - Google Ads: ~~MCC + developer token~~ (extinto em 2026-09-09; ver "Google Ads API mudou" acima).
2. **Meta: Pixel** (Pedro, ~10 min) — Gerenciador de Eventos → Conectar fontes de dados → Web → criar o
   dataset/pixel "Korza". Anotar o **ID do pixel**.
3. **Instalar o rastreamento** (Pedro + Claude) — Pedro clona o site; Claude implementa no site e no
   `admin.korza.app` conforme o plano de medição (eventos, entre domínios, consentimento, UTMs na conta).
   Validar com o DebugView do GA4 e o Test Events da Meta.
4. **Conectar as leituras** (Claude, com credenciais do Pedro)
   - Meta Ads: conector oficial (confirmar URL e procedimento na documentação da Meta na hora).
   - GA4: `google-analytics-mcp` com credencial do Google Cloud (projeto "korza-marketing", API Analytics Data ativa).
   - Search Console: conta de serviço do mesmo projeto, adicionada como usuário no Search Console; script em `conexoes/`.
   - Instagram: app "Korza Marketing" no Meta for Developers, usuário do sistema do BM com
     `instagram_basic`, `instagram_manage_insights`, `pages_read_engagement`, `pages_show_list`; script em `conexoes/`.
   - Google Ads: Google Ads API no projeto "korza-marketing" + acesso Explorer, quando a conta de anúncios existir.
5. **Conversions API** (Fase 2b) — eventos de cadastro e assinatura enviados pelo backend.

## Configuração de MCP

Os servidores MCP ficam em `marketing/.mcp.json` (sem segredos; credenciais via variáveis de ambiente
ou arquivos fora do git). Precisa da aprovação do Pedro na primeira vez que o Claude Code carregar.
O Claude Code precisa ser aberto dentro de `marketing/` para carregar esse arquivo.

- **Meta Ads:** login OAuth pelo `/mcp`. O servidor não tem modo só leitura: ele tem ferramentas de escrita
  (campanhas, anúncios, regras de evento do pixel). A trava é a regra da casa (plano + OK) e a confirmação
  do Claude Code a cada chamada de escrita; nunca liberar ferramentas de escrita no allowlist.
  Docs: developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/
- **Meta devtools** (`meta-devtools`, `https://mcp.facebook.com/devtools`): lê configuração de apps, status de revisão
  e documentação da API; não cria app. Login OAuth pelo `/mcp` (pendente). Beta, liberação gradual.
- **Google Analytics** (`google-analytics`): `pipx run analytics-mcp` com a conta de serviço; sem `--allow-write`.
