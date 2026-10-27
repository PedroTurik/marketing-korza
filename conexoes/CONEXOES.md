# Conexões

Como o hub lê (e, com OK, escreve) nos canais. Regra: **leitura por padrão; qualquer escrita (subir
campanha, publicar, responder) só depois de mostrar o plano e receber OK para aquele plano.**
Segredos em `.env` (fora do git), nunca em arquivo versionado.

## Status

| Conexão | Método | Status |
| --- | --- | --- |
| Rastreamento (GA4 + Pixel) no site e no admin | Código, ver `estrategia/plano-de-medicao.md` | 🟨 GA4 no ar no site (commit `2d7747e` em `dev/Site-Korza`, publicado 2026-10-26, código direto, sem GTM); falta Pixel, admin e banner de consentimento |
| GA4 | MCP oficial do Google (`google-analytics-mcp`) | 🟨 propriedade criada (`G-HR907RLPTS`); leitura a conectar |
| Search Console | Script próprio (API + conta de serviço) | ⬜ domínio não verificado |
| Meta Ads | MCP oficial da Meta (`https://mcp.facebook.com/ads`, em `.mcp.json`) | 🟨 conectado (2026-10-27); a conta das campanhas, "Korza Brasil" (`1982997825669595`), ainda não tem o MCP liberado (liberação gradual da Meta) |
| Pixel da Meta | Reaproveitar o pixel da LP antiga `1174311258139587` | 🟨 no ar no site desde 2026-10-27 (`PageView` conferido), sem banner por decisão do Pedro; falta admin |
| Instagram @korza.br | Script próprio (Instagram Graph API) | ⬜ a conectar (conta profissional + Página existem) |
| Google Ads | MCP oficial do Google (`googleads/google-ads-mcp`), só leitura | ⬜ conta não existe; developer token leva dias |

Repositórios: site em `korza/dev/Site-Korza` (Amplify, deploy automático no push da `main`).

## Estado em 2026-10-27 (passagem de sessão)

- **GA4:** no ar no site, sem GTM (decisão: código direto). Pedro configurou os domínios
  (`korza.com.br` + `admin.korza.app`) e a retenção de 14 meses. Falta: eventos no admin.
- **Pixel:** o Gerenciador de Eventos já tem 5 conjuntos de dados. Não criar novo e não apagar nenhum.
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
- **Domínio na Meta:** não bloqueia o Pixel (ele não é preso a domínio); vale para a Korza ter o controle oficial
  do domínio no BM. Pedro confere se `korza.com.br` já está verificado (talvez pela LP antiga); se não, TXT no DNS,
  que serve também ao Search Console. `korza.app` é outro domínio e precisa de verificação própria.
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
- **Ainda com o Pedro:** Search Console (TXT), conta MCC do Google Ads + developer token, OK para o primeiro
  commit do hub `marketing/`.

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
   - Google Ads: criar uma **conta de administrador (MCC)** e, dentro dela, a conta da Korza. Na MCC:
     Ferramentas → Central de API → pedir o developer token (aprovação demora; pedir cedo).
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
   - Google Ads: quando o developer token sair.
5. **Conversions API** (Fase 2b) — eventos de cadastro e assinatura enviados pelo backend.

## Configuração de MCP

Os servidores MCP ficam em `marketing/.mcp.json` (sem segredos; credenciais via variáveis de ambiente
ou arquivos fora do git). Precisa da aprovação do Pedro na primeira vez que o Claude Code carregar.
O Claude Code precisa ser aberto dentro de `marketing/` para carregar esse arquivo.

- **Meta Ads:** login OAuth pelo `/mcp`. O servidor não tem modo só leitura: ele tem ferramentas de escrita
  (campanhas, anúncios, regras de evento do pixel). A trava é a regra da casa (plano + OK) e a confirmação
  do Claude Code a cada chamada de escrita; nunca liberar ferramentas de escrita no allowlist.
  Docs: developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/
