# Demanda: leva de SEO com 11 páginas no site

**Status:** `feita`
**Criada em:** 2026-10-30
**Especialidade:** site/SEO
**Skill:** nenhuma. Ao terminar, registre em "Entrega" o que vale virar skill.

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Publicar numa branch do `korza/dev/Site-Korza` um modelo de página e 11 páginas de SEO, com sitemap e links internos, prontas
para o Pedro revisar e fazer o push.

## Por que

O site tem 2 páginas e zero busca fora da marca. O nicho é pequeno (1 a 3 mil buscas relevantes por mês), mas tem intenção
alta, e nenhum concorrente brasileiro tem página forte. O objetivo é capturar quem já procura um app para a loja e levar à
oferta "Veja seu app grátis". Domínio novo: o Google rebaixa conteúdo raso em massa, então **qualidade vale mais que velocidade**.

## Leia antes

1. `seo/estrategia.md` e `seo/keywords.md`: decisões, keywords e intenção de cada página
2. `contexto/voz.md`, `contexto/claims.md`, `contexto/posicionamento.md`, `contexto/produto.md`, `contexto/publico.md`
3. `contexto/concorrentes.md`: base do guia de custos e da seção "por que a Korza"
4. `estrategia/dados-do-painel.md`, seção "Padrões de campanhas": só como referência. O que não está em `claims.md` não vai para a página

## Páginas

Crie todas na mesma branch. Faça primeiro o modelo e a página 1, depois siga a ordem da tabela.

| # | URL | Tipo | Keywords (`seo/keywords.md`) | Autor | Case |
| --- | --- | --- | --- | --- | --- |
| 1 | `/aplicativo-para-nuvemshop/` | Solução | app nuvemshop, aplicativo nuvemshop | Sem autor | Loum |
| 2 | `/aplicativo-para-shopify/` | Solução | app shopify, aplicativo shopify | Sem autor | Belletonn, Pé de Algodão |
| 3 | `/aplicativo-para-loja-virtual/` | Solução | aplicativo para loja virtual, app ecommerce, transformar site em aplicativo | Sem autor | Loum, Belletonn |
| 4 | `/blog/depois-da-black-friday/` | Artigo | pós black friday, black friday e-commerce | Guilhermo | Loum |
| 5 | `/guias/quanto-custa-aplicativo-loja-virtual/` | Guia | quanto custa um aplicativo | Pedro | — |
| 6 | `/guias/push-notification/` | Guia | push notification, push notification significado, push in app | Pedro | Belletonn |
| 7 | `/guias/app-pwa-ou-site-mobile/` | Guia | pwa e-commerce | Pedro | — |
| 8 | `/guias/whatsapp-push-ou-email-custos/` | Guia | preço whatsapp api, custo whatsapp business api, whatsapp para e-commerce, e-mail marketing e-commerce | Guilhermo | — |
| 9 | `/blog/crm-para-e-commerce/` | Artigo | crm para e-commerce | Guilhermo | — |
| 10 | `/blog/taxa-de-recompra/` | Artigo | taxa de recompra | Guilhermo | Loum |
| 11 | `/blog/ltv-e-commerce/` | Artigo | ltv e-commerce | Pedro | — |

## Requisitos

**Conteúdo**
- Uma intenção por página, sem páginas quase iguais trocando a palavra. As 3 de solução precisam ter argumento próprio:
  Nuvemshop com zero trabalho, Shopify com preço fixo em reais, loja virtual com marca e recompra.
- Nuvemshop e Shopify têm intenção mista: parte das buscas quer o app de gestão da plataforma. Deixe claro no título e no
  primeiro parágrafo que é um **app da sua marca para os seus clientes**.
- Artigos e guias têm profundidade real e ângulo da Korza: canal próprio, push, recompra. O produto entra como consequência, no fim.
- Cada página: um pilar, FAQ com perguntas reais e CTA **Veja seu app grátis** para `https://admin.korza.app/create-account`.
  CTA secundário só nas de solução: Fale com um especialista.
- Links internos entre as páginas relacionadas: artigos e guias apontam para a página de solução certa.

**Claims e regras**
- Números só de `contexto/claims.md`, com a redação e as ressalvas de lá. Case sempre com o nome do cliente.
- **Não usar** `push-abertura-30` nem `vendas-16m`. Em vez de abertura de push, use "1 clique até o produto".
- Não vender: carrinho abandonado, Públicos. Não dizer: "a mais barata", "o app é seu", "você é dono". Não prometer resultado.
- Concorrente sem nome. Compare **tipos de solução**. Preço de terceiros de `concorrentes.md` só depois de conferir na fonte.
- Dado de terceiro (WhatsApp, e-mail, Apple, Google) sempre com fonte e data no texto, de fonte primária. Não achou? Não use.
- Sem depoimento, cliente ou tela inventados. Imagens só de `assets/` ou `contexto/telas/`, seguindo `contexto/telas/README.md`.
- Vocabulário de `voz.md`: nada de "retenção" e "churn" nos títulos. "LTV" pode aparecer no artigo 11, explicado.

**Técnico**
- HTML estático, CSS do site. Caminhos absolutos (`/styles.css`, `/assets/...`), como `privacy-policy/index.html`.
- **Não carregue `app.js` direto:** ele espera elementos da home e quebra sem eles. Reaproveite só o que for preciso,
  incluindo o repasse do `fbclid` para o link de cadastro (`app.js`, linha ~242), num script próprio e compartilhado.
- Copie para cada página os mesmos blocos de GA4 e Pixel do `<head>` da home, com o mesmo consent. Sem tags novas.
- Cada página: `title` e `description` únicos, `canonical`, Open Graph, um `h1`.
- Dados estruturados: `Organization` no modelo; `SoftwareApplication` e `FAQPage` nas de solução; `Article` com autor e
  `FAQPage` em guias e artigos.
- Autor com mini-bio: **Pedro**, cofundador e CTO; **Guilhermo**, cofundador e CEO. Não invente trajetória. Peça ao Pedro o
  sobrenome do Guilhermo e o que a bio deve dizer.
- Layout responsivo, sem rolagem horizontal em 390px. Header e footer iguais em todas as páginas.
- Inclua as 11 URLs no `sitemap.xml`.
- Links internos na home: as 3 de solução no footer. Sem mudar o layout da home além disso.

## Fora do escopo

- `/precos/` e `/cases/`
- Política de privacidade, banner de consentimento e `noindex` do admin
- Texto, seções e FAQ atuais da home
- Página de índice do blog e guias, a menos que seja necessária para os links funcionarem. Se criar, avise em "Entrega"
- Push: o Pedro revisa e publica

## Critério de pronto

- [x] Branch `seo-leva-1` criada a partir da `main` atual, com commits por página, sem push
- [x] 11 páginas abrindo num servidor local, com header, footer e fontes corretos, conferidas em 1440px e 390px
- [x] Os CTAs chegam ao cadastro; com `?fbclid=teste` na URL, o link leva o parâmetro
- [x] GA4 e Pixel presentes em todas as páginas; nenhum erro no console
- [x] Dados estruturados com JSON válido em todas as páginas
- [x] Sitemap com 13 URLs, XML válido, e links do footer funcionando
- [x] Todo número conferido contra `claims.md`; todo dado de terceiro com fonte e data
- [x] Nenhum termo proibido: busque por "retenção", "churn", "30%", "16 milhões", "é seu", "mais barata", "carrinho abandonado"
- [x] Atualizar o Status de `seo/` em `MELHORIAS.md` e em `PLANO.md`

## Entrega

Concluída em 2026-10-30. Branch `seo-leva-1` em `korza/dev/Site-Korza`, 11 commits a partir da `main` local (que estava 1 commit à
frente da `origin`), sem push. Fonte das páginas e gerador em `seo/modelo/`: edite `paginas/*.py` e rode `build.py`, sem mexer no HTML.

**Decisões do Pedro:** autores Pedro Turik Firmino e Guilhermo Herter, bio só com cargo e Korza. "Fale com um especialista" vai para
o WhatsApp 55 51 9455-3299, com mensagem preenchida.

**Diferente do pedido:**
- Guia 8: R$ 0,3217 por mensagem de marketing veio do Pedro. Não consegui ler a tabela de tarifas da Meta; só vi o mesmo valor em
  sites de terceiros. A página cita a Meta como fonte: conferir na tabela antes do push.
- Guia 8: as demais tarifas do WhatsApp no Brasil ficaram de fora, sem fonte primária.
- Guia 5: preços de concorrentes conferidos na fonte em 2026-10-30, exceto o da solução com comissão, cuja página não abriu. Por isso
  essa linha não tem percentual. Agência sem valor, por falta de fonte.
- Guia 6: a página da Apple sobre permissão só carregou o título; a afirmação segue a documentação citada, mas vale conferir.
- `cta_click` do GA4 também conta o clique no WhatsApp. É o evento que já existia, sem tag nova.
- Sem índice de blog e guias: os links internos bastam. Guias e artigos entram pelas páginas de solução, os "Leia também" e o sitemap.
- `og:image` é o logo, por falta de arte no formato (em `MELHORIAS.md`).
- Os links do footer da home entraram na coluna "Explore".
- Claims não usados: `push-abertura-30` e `vendas-16m`, como pedido. Os exemplos de conta são marcados como ilustrativos.

**Verificado:** 11 páginas em 1440px e 390px, em navegador sem interface, sem rolagem horizontal nem erro de página; `fbclid` no link de
cadastro ao clicar; GA4 e Pixel carregados; JSON-LD válido; sitemap com 13 URLs; links do footer; termos proibidos sem ocorrência. O
envio ao GA4 e ao Pixel e o link de WhatsApp não foram testados de ponta a ponta.

**Vira skill:** o fluxo de `seo/modelo/` (modelo, página por arquivo, checagem no navegador). Vale criar `/korza-seo` na próxima página.
