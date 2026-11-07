# Campanha `2026-11-meta-conta-gratis`

Primeira campanha de conversão na Meta com o funil self-serve (conta grátis → preview → assinatura de R$ 399/mês).
Decidida com o Pedro em 2026-11-07. Hipótese, não regra: muda com o dado.

## O que testa

1. **Formato:** motion × sócio em vídeo (custo por conta, por conjunto)
2. **Mensagem:** qual vídeo traz conta mais barata dentro de cada conjunto
3. **Gancho do M2:** "R$ 100 mil" (v2) × "busca"
4. **O funil:** primeira vez que tráfego pago passa por conta → preview → assinatura

## Configuração

| Item | Valor |
| --- | --- |
| Conta | Korza Brasil `1982997825669595` (pela Graph API: o MCP não chega nela) |
| Objetivo | Leads, conversão no site, evento `CompleteRegistration`, Pixel `1174311258139587` |
| Orçamento | Por conjunto (ABO), R$ 200/dia no total, ~R$ 4,2 mil |
| Lance | Maior volume, sem teto |
| Atribuição | 7 dias clique, 1 dia visualização |
| Período | 2026-11-07 (17h09) a 2026-11-29 |
| Público | Brasil, 22+, Advantage+ com sugestões (Shopify, comércio eletrônico, empreendedorismo, pequenas e médias empresas, marketing digital). Não existe interesse "Nuvemshop" na Meta |
| Exclusão | Pixel `CompleteRegistration` nos últimos 180 dias |
| Posicionamentos | Instagram (feed, stories, reels, explorar home, perfil) e Facebook (feed, stories, reels). Sem Audience Network nem Threads. O Explorar do Instagram está obsoleto na API v23 |
| Destino | `https://admin.korza.app/create-account`, botão "Cadastre-se" |
| UTMs | `utm_source=meta&utm_medium=paid_social&utm_campaign=2026-11-meta-conta-gratis&utm_content=<id>` |
| Melhorias automáticas de criativo | Desligadas |
| Listas de clientes da conta USD | Não usar (decisão do Pedro) |

## Conjuntos e anúncios

| Conjunto | Verba | Anúncios (`utm_content`) |
| --- | --- | --- |
| Motion | R$ 100/dia | `m1-notificacao-v2`, `m2-do-zero-v2`, `m2-do-zero-busca`, `m3-painel-v2` (9:16 + 4:5) |
| Gravados | R$ 100/dia | `gravado-recompra-mesa`, `gravado-14-dias`, `gravado-como-funciona`, `gravado-custo-amador` (post existente do IG, 94s), `gravado-bf` (só até 2026-11-20) (9:16) |
| Remarketing | R$ 30/dia | **Só a partir de ~2026-11-16, se o público morno passar de ~5 mil.** Vídeo 50%+, engajados do IG 90d, site 30d; exclui contas criadas |

Em 2026-11-07, o público morno tinha ~2–3 mil pessoas (site ~100 em 30 dias, IG 88 engajados em 28 dias, vídeo 50%+ das
campanhas de julho e do ThruPlay). Pouco para R$ 40/dia. O ThruPlay `2026-11-reel-custo-amador` termina em 2026-11-12 e
alimenta esse público.

Copy: `COPY.md` (demanda `demandas/2026-11-07-copy-meta-conta-gratis.md`).

## Regras de decisão

| Métrica | Regra |
| --- | --- |
| Taxa de gancho (views de 3s ÷ impressões) | < 20% após 2 mil impressões → trocar o gancho |
| Custo por conta criada | Criativo com R$ 150 gastos e nenhuma conta → pausar |
| Conta → preview concluído | < 30% → o público está errado; mexer no público antes do criativo |
| Custo por assinatura (self-serve + comercial) | Teto de R$ 800 (2 mensalidades). O teste é bom com 5+ assinaturas |
| Trava | R$ 1.600 sem nenhuma assinatura → pausar e revisar o funil |
| Semana da BF (23–29/11) | Custo por conta +50% → baixar para R$ 100/dia |
| Otimização | Com ~50 previews/semana, trocar o evento para `ViewPreview` |

Contas são contadas pelo banco ou pelo GA4, nunca pelo bruto da Meta (`estrategia/plano-de-medicao.md`). O comercial
chama toda conta nova em até 24h; assinatura fechada pelo comercial conta para a campanha (`signup_attribution`).

## Pontos de atenção

- `gravado-recompra-mesa` e `gravado-14-dias` terminam com "Saiba Mais, eu monto uma estratégia de graça"; o anúncio leva ao
  cadastro. O Pedro decidiu rodar assim. Se tiverem CTR alto e poucas contas, o descompasso é a primeira suspeita.

- Gravados **com Stories**, mesmo com o botão CTA cobrindo a legenda dos sócios (decisão do Pedro, 2026-11-07). Se o
  Stories converter mal nesse conjunto, tirar o posicionamento ou reeditar com a legenda mais alta.

## Status

- [x] Copy aprovada (`COPY.md`)
- [x] Vídeos enviados, público de exclusão, campanha, conjuntos e anúncios criados **pausados** (2026-11-07; IDs em `ids.tsv` e `videos.tsv`)
- [x] Ativada em 2026-11-07 às 17h09, com OK do Pedro (anúncios entram depois da revisão da Meta)
- [ ] 2026-11-20: pausar `gravado-bf` (anúncio não tem data de fim; o conjunto tem)
