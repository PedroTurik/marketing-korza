# Dados do painel — leitura de 2026-10-30

Fonte: API do admin, 75 lojas com app no ar (sem as contas com "teste" no nome e sem a Green Is Good, ver "Qualidade").
Podem restar contas de teste com outro nome, o que pesa pouco nos totais.
O que foi aprovado está em `contexto/claims.md`; o restante daqui **não vale em peça**. Números por loja ficam em
`inbox/admin-2026-10-30/raw/` (fora do git).

## Como ler as métricas

- **Conversão de campanha** = pedidos pagos ÷ cliques. **CTR** = cliques ÷ notificações entregues.
- **Recompra** = pedidos no app de quem já tinha comprado, no app (`inApp`) ou só no site (`channelMigration`).
- `firstPurchases` é a primeira compra **no app** e inclui `channelMigration`; por isso a composição soma mais que o total.
- Cliques não eram medidos em novembro de 2025: a Black Friday passada tem pedidos e receita, mas não CTR.

## Conferência dos claims atuais

| Claim | Status | O painel mostra |
| --- | --- | --- |
| `clientes-60` (+60 e-commerces) | Mantido | 97 cadastros, 75 com app no ar, dos quais alguns são de teste (Pedro) |
| `belletonn-push-266` (26,6%) | Confirmado | 26,4% histórico, 26,2% em 90 dias |
| `loum-recompra-886` (era 42%) | Atualizado | 65,1% histórico, 88,6% em 90 dias (Loum é Nuvemshop) |
| `pda-faturamento-498` (+4,98%) | Mantido pelo Pedro | Campanhas sobre o faturamento da loja: 2,44% histórico, 3,39% em 90 dias |
| `sem-setup-comissao` | Mantido | Vale pela decisão do Pedro; o código está sendo ajustado |
| `preview-gratis` | Mantido | Oferta forte; emulador melhor no futuro |
| `push-abertura-30`, `app-conversao-25` | Sem como conferir | O painel não compara canais |

## Divergências com o código (decididas pelo Pedro em 2026-10-30)

`contexto/` segue valendo. O código está sendo ajustado para ficar igual, e o PR do admin espera essas mudanças.

- **Comissão:** não existe mais. O código ainda tem 1% em planos antigos e no onboarding novo; isso sai.
- **Pagamento:** o lojista paga a mensalidade pela plataforma. Hoje o onboarding termina em "nosso time vai entrar em contato", sem pagamento.
- **Preview:** continua sendo a oferta forte, mesmo mostrando só a marca sobre um esqueleto. Um emulador mais robusto vem depois.
- **Públicos:** entra num plano futuro; hoje 6 lojas testam. Ignorar nas peças.
- **Carrinho abandonado:** "Em breve" no painel. Não vender como disponível.

Até o PR entrar, um anúncio que leve ao cadastro promete o que o fluxo ainda não entrega. Por isso a campanha paga espera o PR.

## Base dos claims agregados (aprovados em 2026-10-30)

| Número | Base |
| --- | --- |
| +200 mil downloads | 206.953 acumulados |
| +70 mil clientes com push ativo | 71.365 |
| +9,5 milhões de notificações enviadas | 9.559.847, em 6.877 campanhas |
| +36 mil pedidos pelo app | 36.463 |
| R$ 16 milhões vendidos pelo app | R$ 16,36 mi. Conferir antes: inclui lojas com ticket muito alto |
| R$ 2,3 milhões atribuídos a campanhas de push | R$ 2,39 mi, 8.157 pedidos |
| Ticket médio no app ~10% maior que no site | Mediana +10,4%; maior em 18 de 23 lojas com 50+ pedidos em 90 dias |
| 1 em cada 3 pedidos no app é recompra | 36,1% em 90 dias |

## Candidatos a case (precisam de OK do cliente)

Pelo volume e pela recompra em 90 dias: Ohana Kameala (65% de recompra, ticket +20%), Alto Calçados (ticket +12%),
Dom Perfumes, Tabs Perfumes (63%). Entre os já citáveis, ONUH tem 50,6% de recompra e Hiven, ticket 66% acima do site.
Plataformas: Loum é Nuvemshop; Belletonn, Pé de Algodão, Hiven e ONUH são Shopify.

## Black Friday 2025 (matéria-prima para novembro)

Mês de novembro: 361 campanhas, 296 mil notificações, 581 pedidos e R$ 174,7 mil atribuídos ao push.
Semana da Black Friday: 152 campanhas, 322 pedidos, R$ 78,8 mil. A base era bem menor que a de hoje.

## Padrões de 3.248 campanhas (30 lojas, 200+ entregas, com clique)

Correlação, não causa, e poucas lojas pesam muito. Servem de pauta com essa ressalva.

- **CTR agregado perto de 0,9%**, muito abaixo do que costuma circular sobre push. Cuidado ao falar em "abertura".
- **Título longo:** 45+ caracteres teve CTR de 1,39% e R$ 449 por mil entregas, contra 0,88% e R$ 236 nos de 15–29 (n=120).
- **Emoji não ajudou:** R$ 219 por mil com emoji no título, R$ 312 sem.
- **Urgência ajudou** ("hoje", "acaba", "últim…"): R$ 291 contra R$ 219.
- **Falar de desconto não ajudou:** R$ 209 contra R$ 256.
- **Horário:** sem vencedor claro. 9h, 10h e 18h lideram em receita por mil; 20h e 8h ficam atrás.
- **Dia:** terça e sábado à frente; segunda atrás. Diferença pequena.

## Uso da base (interno, nunca em peça)

Das 77 lojas em `tenant-engagement`: 29 ativas ou com envio agendado, 28 pararam, 20 nunca enviaram.
Quase dois terços não usam o push hoje: risco de churn e assunto para o time de sucesso do cliente.

## Qualidade dos dados

- **Green Is Good** foi excluída: 18 pedidos com ticket de R$ 67 mil em 90 dias, somando R$ 1,2 mi. Parece erro de valor.
- **ONUH:** app com 94% do faturamento da loja, o que sugere venda do site incompleta. Não usar participação do app dela.
- Comparar app e site também tem viés: quem baixa o app tende a já ser cliente melhor.
