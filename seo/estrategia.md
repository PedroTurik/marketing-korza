# Estratégia de SEO

Aprovada com o Pedro em 2026-10-29. Base: [../contexto/posicionamento.md](../contexto/posicionamento.md),
[../contexto/publico.md](../contexto/publico.md), [../contexto/concorrentes.md](../contexto/concorrentes.md).

## Ponto de partida (2026-10-29)

- Site `korza.app` (HTML estático em `korza/dev/Site-Korza`): 2 páginas (home e privacidade). Sem blog.
- Search Console: **zero buscas fora da marca**. Em 90 dias, o `korza.com.br` teve 81 cliques, todos em "korza"
  (posição média 5,7: a marca disputa o nome com outras "Korza", como importadoras).
- Domínio novo (migrado em 2026-10-27). SEO de domínio novo leva de 3 a 6 meses para trazer tráfego relevante.

## O que as buscas mostram (2026-10-29)

- **Comercial** ("aplicativo para loja Nuvemshop/Shopify", "transformar loja virtual em app"): o Google mostra
  documentação de desenvolvedor da Nuvemshop, a loja de apps dela e ferramentas gringas. Nenhum brasileiro tem
  página forte. **É onde entramos primeiro.**
- **Educativa ampla** ("como aumentar recompra", "taxa de recompra"): Nuvemshop, Tray, Stone e Shopify dominam.
  Domínio novo não vence isso cedo. Entramos pela cauda longa com o nosso ângulo (push, app, canal próprio).
- **Lojas de apps** (Loja de Aplicativos Nuvem, Shopify App Store): concorrentes listados lá. Para o nosso público
  é um segundo Google.

## Como produzimos

**Uma leva só**, guiada pelos volumes do Planejador ([keywords.md](keywords.md)): modelo de página, 3 páginas de solução,
4 guias e 4 artigos (11 páginas), numa branch do Site-Korza. O mapa página → keywords está em `keywords.md`. Depois, novos artigos entram quando a pauta pedir (Instagram, Search Console), sem cota semanal.
Ajustamos pelos dados do Search Console a partir de 4 a 8 semanas.

Cuidados da leva: cada página atende uma intenção distinta (nada de páginas quase iguais trocando a palavra), texto com
substância própria (o Google rebaixa conteúdo em massa raso, ainda mais em domínio novo) e números só de `claims.md`.

**Lojas de apps:** a Korza ainda não está na Loja de Aplicativos Nuvem nem na Shopify App Store; vai estar. Quando
entrar, a listagem vira frente de SEO (título, descrição, prints, avaliações).

## Três camadas

### 1. Páginas de solução (fundo de funil)

Uma página por intenção de compra, com CTA "veja seu app grátis".

| Página | Busca-alvo | Pilar |
| --- | --- | --- |
| `/aplicativo-para-nuvemshop/` | aplicativo para loja Nuvemshop, app Nuvemshop iOS Android | Todos + zero trabalho |
| `/aplicativo-para-shopify/` | aplicativo para loja Shopify, app Shopify Brasil | Todos + preço fixo em reais |
| `/aplicativo-para-loja-virtual/` | aplicativo para loja virtual, app para loja virtual, aplicativo para e-commerce | Marca, recompra |
| `/precos/` | quanto custa aplicativo para loja virtual | **Espera os planos novos** (decisão de 2026-10-29) |

### 2. Guias comparativos (meio de funil)

Comparam **tipos de solução**, nunca concorrentes pelo nome (regra do `posicionamento.md` e CONAR).

- App próprio x site mobile (PWA)
- Push x WhatsApp x e-mail para e-commerce
- App próprio x construtor "faça você mesmo" x agência sob medida
- Quanto custa um aplicativo de loja (setup, comissão, contas de desenvolvedor)

### 3. Blog (topo de funil, ligado ao Instagram)

Mesmos territórios de [../estrategia/linha-editorial.md](../estrategia/linha-editorial.md): a pauta da semana vira
post no Instagram **e** artigo. Cauda longa com o nosso ângulo, por exemplo:

- O que fazer com os clientes novos depois da Black Friday
- Push notification para e-commerce: exemplos e frequência
- Como calcular a taxa de recompra (e o que é bom para moda, cosméticos, calçados)
- Quanto custa o WhatsApp para e-commerce em 2026
- Como marcas como [marca conhecida] usam o app para recompra (análise de marca)

**Cases:** sem página `/cases/` nesta leva (sem busca; a home já tem a seção). Cada página e guia traz o case que combina,
só com os claims aprovados. Página própria quando houver mais material por case.

**Autoria:** guias e artigos assinados por **Pedro** (cofundador e CTO) ou **Guilhermo** (cofundador e CEO), com mini-bio
e dados estruturados de autor.

## Técnico (junto com a primeira leva de páginas)

- Modelo de página e de artigo no Site-Korza (HTML estático, mesmo CSS), com `title`, `description`, `canonical`,
  Open Graph e dados estruturados (`Organization`, `SoftwareApplication`, `FAQPage`, `Article`).
- Sitemap atualizado a cada página; links internos da home para as páginas de solução.
- Marca: garantir a korza.app em 1º para "korza" e "korza app" (dados estruturados de organização e perfis sociais).

## Como medimos

| Métrica | Fonte | Meta de 90 dias (até 2027-01-27) |
| --- | --- | --- |
| Páginas indexadas | Search Console | Todas as publicadas |
| Impressões fora da marca | Search Console | Sair do zero; crescer mês a mês |
| Posição das páginas de solução | Search Console | Top 10 nas buscas-alvo |
| Sessões orgânicas e contas criadas vindas do orgânico | GA4 (contas depois do PR do admin) | Linha de base |
