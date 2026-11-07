# Radar — marcos e features

Tudo que pode virar conteúdo nasce aqui. Quando o Pedro pede, o `/cmo` varre as fontes e registra a decisão (os níveis
abaixo são ponto de partida, não regra): **vira conteúdo? como?
impulsiona? qual criativo?** Só anunciar o que já está em produção; commit em `dev` é sinal, não lançamento.

## Fontes

| Fonte | Como ler |
| --- | --- |
| Produto | `git -C ../dev/<repo> log --all --since='7 days ago' --no-merges` em `admin`, `backend`, `backoffice`, `mobile`. Só `feat`; ignorar teste e correção interna |
| Lojas novas | Commits `feat: add <loja> tenant` em `mobile`. Citar cliente só com OK |
| Números | API do admin (`conexoes/CONEXOES.md`, "Painel da Korza"), comparando com "Próximos marcos" |
| Pedro | Prêmios, eventos, parcerias e lançamentos que não passam pelo git |

## Níveis

| Nível | Quando | O que acontece |
| --- | --- | --- |
| **A** | Muda a oferta ou destrava objeção | Pauta prioritária em todos os canais, avaliar impulsionar, avisar o outbound |
| **B** | Feature útil ou marco redondo | 1 post e 1 story; avaliar impulsionar se render acima da média |
| **C** | Melhoria pequena | Só bastidor, ou nada |

## Na fila

| Item | Nível | Quando | Decisão |
| --- | --- | --- | --- |
| Pagamento na plataforma (self-serve) | A | **No ar desde 2026-11-06** | Vira "assine sem falar com ninguém" (`assina-sozinho`). Medição de conta criada e assinatura no ar desde 2026-11-07 (`plano-de-medicao.md`): a mídia paga está destravada |
| Novos planos | A | Sem data | Revisar preço, claims, `/precos/` e `sem-setup-comissao` antes de qualquer peça |
| Listagem na Loja de Aplicativos Nuvem e Shopify App Store | A | Sem data | Lançamento + frente de SEO (`seo/estrategia.md`) |
| Carrinho abandonado | A | "Em breve" | Não vender antes de sair. Ao sair: pauta prioritária, tema de maior dor |
| Públicos | B | Plano futuro | Ignorar nas peças até o plano sair |
| Logo opcional no onboarding (2026-10-30, em `dev`) | C | Ao entrar em produção | Sem peça |

## Próximos marcos

Base: painel em 2026-10-30. Ao bater, conferir, aprovar em `claims.md` e decidir a peça.

| Marco | Hoje | Próximo |
| --- | --- | --- |
| Notificações enviadas | 9,56 milhões | **10 milhões** (nível B, é o mais próximo) |
| Downloads | 206.953 | 250 mil |
| Clientes com push ativo | 71.365 | 100 mil |
| Pedidos pelos apps | 36.463 | 50 mil |
| Vendas pelos apps | R$ 16,36 mi | R$ 20 mi |
| Vendas atribuídas ao push | R$ 2,39 mi | R$ 3 mi |

## Datas de verificação

| Item | Vence | Ação |
| --- | --- | --- |
| Preço e `sem-setup-comissao` | 2026-12-06 | Confirmar com o Pedro |
| Preços de `concorrentes.md` | Antes de qualquer comparação | Conferir na fonte |
| Remoção temporária no Search Console | ~2027-04-27 | Resolver o `noindex` antes |
