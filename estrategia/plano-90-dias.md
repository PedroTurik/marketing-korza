# Plano de 90 dias

De 2026-11-02 a 2027-01-31. Escrito pelo CMO (Claude) em 2026-10-30. Revisar a cada ritual `/cmo`; as metas são a
primeira aposta e mudam com os dados.

## Onde estamos (2026-10-30)

| Frente | Hoje |
| --- | --- |
| Vendas | Quase tudo vem do outbound. Funil no HubSpot: 544 negócios, 418 contatados, 10 reuniões realizadas ou além, 3 ganhos, 13 quentes, 176 parados em "Ligar" |
| Site | 76 sessões em 28 dias (GA4), sem busca fora da marca |
| Instagram | 608 seguidores, alcance de 738 em 28 dias, 28 posts em 16 meses |
| Mídia paga | Parada. Meta com 2 campanhas pausadas, Google sem campanha |
| Hub | Configurado, ainda sem nenhuma peça real produzida aqui |

**Leitura:** o gargalo não é convencer, é ser visto. Com 76 sessões por mês, nenhuma otimização de site muda o negócio.
O trabalho dos próximos 90 dias é criar demanda e aquecer quem o outbound já alcança.

## Metas

**Métrica-mãe: assinaturas originadas pelo marketing.** Até o PR do admin não dá para medir conta criada, então novembro
é medido por sinais antecedentes.

| Métrica | Hoje | Meta em 2027-01-31 |
| --- | --- | --- |
| Posts publicados por semana | ~0,4 | 5 (mínimo aceitável: 4) |
| Alcance do Instagram em 28 dias | 738 | 5.000 |
| Seguidores | 608 | 1.000 |
| Cliques no site vindos do Instagram (28 dias) | 6 | 60 |
| Sessões no site (28 dias) | 76 | 500 |
| Páginas de SEO no ar | 0 de 11 | 11 |
| Contas criadas por mês (após o PR) | sem medição | 30, a ~R$ 100 por conta (hipótese a calibrar em 4 semanas) |
| Assinaturas originadas pelo marketing | 0 | 5 |

## Verba

Faixa aprovada: **R$ 1.500 a R$ 5.000/mês**, a partir do PR do admin. Plano-base de R$ 3.000/mês. Cada campanha ainda
passa por OK do Pedro.

| Fase | Quando | Verba | Onde |
| --- | --- | --- | --- |
| Antes do PR | Novembro | Até R$ 500/mês | Só impulsionar post que já rendeu acima da média, para engajamento e audiência, sem levar ao cadastro |
| Depois do PR | Quando entrar | R$ 3.000/mês | 40% remarketing (engajados, visitantes, base de outbound), 40% prospecção na Meta, 20% Google em poucas keywords de fundo de funil |

**Regra de impulsionamento:** post orgânico com salvamentos + compartilhamentos acima de 2× a média dos últimos 10 posts é
candidato. Criativo pago nasce do que já provou no orgânico.

## Portões da mídia paga para o cadastro

Nenhuma campanha que leve ao cadastro sobe antes de:

1. **PR do admin:** GA4, Pixel, `sign_up` e pagamento na plataforma (`plano-de-medicao.md`, `dados-do-painel.md`). Previsto
   para a semana de 2026-11-02, segundo o Pedro.
2. **Privacidade:** a seção 7 da política diz que não há cookies de marketing, mas o Pixel roda no site. Corrigir a política
   (conferir também os contatos `@korza.app` e a seção 11, que falta) e pôr um banner próprio (Aceitar/Recusar) no site e no
   admin, com Pixel e sinais de anúncio do Google só após o aceite.
3. **Site com o case certo:** a home ainda mostra Loum 42%; o claim aprovado é 88,6% em 90 dias. A Loum deu OK (2026-10-30).

## Calendário comercial

O prazo de até 14 dias úteis muda a campanha de fim de ano:

- **Black Friday (27/11):** quem assina depois de ~3/11 pode não estar no ar a tempo (feriados de 2/11 e 20/11).
  **Não vendemos "app para a Black Friday".**
- **Natal:** quem assina até ~30/11 pode estar no ar até ~18/12.
- **Mensagem da temporada:** *"Na Black Friday você paga para ganhar cliente. E depois, como ele volta?"* O lojista sente o
  custo de mídia em novembro; o app é a resposta para dezembro e janeiro. Vale para Instagram, SEO e outbound.

## Multicanal

**Uma pauta-mãe por semana, desdobrada em todos os canais.** Assim 5 posts não viram 5 ideias do zero.

| Canal | Papel | Como entra | Mede |
| --- | --- | --- | --- |
| Instagram | Canal central: audiência e prova | 5 posts por semana, gravados pelos fundadores ou produzidos no hub | API do Instagram |
| YouTube Shorts | Alcance sem custo novo | Repostar os reels. Sem produção própria nesta fase | Manual até o OAuth (`MELHORIAS.md`) |
| X | Reposição manual | Cortes e carrosséis, sem esforço extra | Não mede |
| Site / SEO | Captura de intenção | Pauta boa vira artigo; 11 páginas na primeira leva | Search Console, GA4 |
| Outbound (WhatsApp) | Canal que vende hoje | Case e conteúdo da semana viram material para o follow-up. O envio segue no `crm-automacao` | HubSpot |
| Meta Ads | Amplificar o que provou | Boost; campanhas após os portões | Graph API |
| Google Ads | Capturar intenção | Só após os portões | MCP |

**Fora por 90 dias:** TikTok (o decisor está no Instagram e não há como produzir para mais um canal), newsletter e LinkedIn.

## Fontes de dados

| Fonte | Responde | Frequência |
| --- | --- | --- |
| Instagram e Meta Ads (Graph API) | O que rende, o que impulsionar | Semanal |
| GA4 | Quem chega e por onde | Semanal |
| Search Console | O que buscam, se as páginas indexam | Semanal |
| Google Ads | Custo e intenção | Quando houver campanha |
| HubSpot / Chatwoot (só leitura, `crm-automacao`) | O que vira venda, objeções reais | Semanal; conversas só em agregado |
| Painel da Korza (API do admin) | Marcos e claims novos | Mensal; exige login do Pedro |
| Repositórios de produto | Features novas | Semanal (`radar.md`) |

## Apostas que não dependem do PR

1. **Instagram a 5 por semana**, começando em 3/11 (`conteudo/calendario.md`).
2. **Leva de SEO**, com o artigo de pós-Black Friday no ar até 16/11, para dar tempo de indexar.
3. **Aquecer o outbound:** 13 quentes e 176 em "Ligar" recebem conteúdo e prova. Quem tem contato feito e não comprou é o
   melhor público de remarketing, assim que a base legal da lista for checada.
4. **Dois cases novos** com OK dos clientes (candidatos em `dados-do-painel.md`). Prova nova rende em todos os canais.

## Claims: cuidados do CMO

- **`push-abertura-30`:** evitar em peça nova. Não há fonte conferível, e o CTR que medimos é de ~0,9%. Usar "1 clique até o
  produto". Dá para voltar quando houver fonte.
- **`sem-setup-comissao` e preço:** verificados em 2026-10-26, vencem em **2026-11-25**, na véspera da Black Friday.
  Confirmar antes (`radar.md`).
- **Dados da Black Friday 2025:** ainda não são claims. Se quisermos usá-los em novembro, precisam de aprovação.
