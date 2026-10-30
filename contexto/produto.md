# Produto e oferta

O que a Korza vende, por quanto e como o lojista compra. Fatos que mudam (preço, planos, prazos) vivem
**só aqui** e nos claims de [claims.md](claims.md). Ao mudar, atualize a data e registre no histórico.

## Em uma frase

A Korza transforma o e-commerce em **aplicativo próprio da marca (iOS e Android)**, conectado à loja
Nuvemshop ou Shopify, com **push ilimitado** e um painel de vendas e recompras. O app vira um canal
próprio de recompra.

## O que vem no plano

- App iOS e Android com a identidade da marca (cores, produtos, jeito), publicado na App Store e no Google Play
- Integração com Nuvemshop e Shopify
- Campanhas de push: criar a mensagem, escolher o destino e agendar. Push ilimitado
- Painel com vendas, recompras, campanhas e clientes
- Construção e publicação em até 14 dias úteis, 100% feitas pela Korza. A implantação é assíncrona e automática: depois do onboarding, o lojista não precisa fazer mais nada

## Funcionalidades — verificado no painel em 2026-10-30

| Área | O que existe |
| --- | --- |
| Início | Faturamento, vendas, ticket e downloads; próxima campanha; próximos passos; últimas campanhas |
| Campanhas | Título, mensagem, destino (página inicial ou outra), envio agora ou agendado, teste no aparelho, preview no iPhone, lista e calendário, exportação, importação por CSV (até 5.000 linhas) |
| Analytics | Abas Resumo, Vendas, Push, Usuários e Pedidos; app × site, participação do app, recompras, ROI, matriz RFM, retenção, CSV |
| App | Banner de cupom, notificação de boas-vindas, banner no site para baixar o app, dynamic config |
| Equipe e cobrança | Convite por e-mail, assinatura e pagamentos |
| Públicos | 11 filtros (compra, gasto, frequência, último acesso, clique e outros). **Ligado em 6 de 75 lojas**; nas demais, "Em breve" |
| Carrinho abandonado | **Em breve.** Não vender como disponível |

Prints em [telas/](telas/README.md). Dados da base em [../estrategia/dados-do-painel.md](../estrategia/dados-do-painel.md).

## Funil real — verificado em 2026-10-30

Cadastro por magic link → plataforma → nome, loja e e-mail → logo → barra de navegação e cor → notificação de teste →
"seu app está sendo construído", com o time entrando em contato. Por enquanto não há pagamento no fluxo; o lojista
passará a pagar a mensalidade pela plataforma, e a comissão que ainda existe no código sai (o PR do admin espera isso).
O preview usa a marca do lojista sobre um esqueleto, sem produtos, e segue como oferta forte; um emulador mais robusto vem depois.
Públicos estão em teste com 6 lojas e entram num plano futuro: ignorar nas peças.

## Preço e condições — verificado em 2026-10-26

| Item | Valor |
| --- | --- |
| Conta | Grátis (inclui o preview do app no onboarding) |
| Plano | **R$ 399/mês** — plano único |
| Setup / implantação | Não tem |
| Comissão sobre vendas | Não tem |
| Fidelidade | Não tem |
| Contas de desenvolvedor | Da Korza. O app é publicado nas contas Apple/Google da Korza; o lojista não paga US$ 99/ano + US$ 25 nem cria conta |
| Cancelamento | O app sai do ar. É assinatura: o app é da marca do lojista (identidade, produtos), mas não é propriedade dele |

**Volátil:** novos planos e features comissionadas estão em preparação. Antes de usar preço ou "sem setup /
sem comissão" numa peça, confira a data acima; se tiver mais de 30 dias, pergunte ao Pedro.

Contexto de mercado (palavra do Pedro, a confirmar em [concorrentes.md](concorrentes.md)): soluções desse
tipo costumam cobrar setup e uma taxa sobre as vendas. Por isso "sem setup e sem comissão" é diferencial,
enquanto durar.

## Como o lojista compra (funil)

1. **Oferta de entrada: "veja seu app gratuitamente".** O lojista cria a conta grátis em
   `https://admin.korza.app/create-account`, conecta a loja e o onboarding mostra um preview do app.
2. **Assinatura self-serve** do plano de R$ 399/mês. É a direção da empresa: vender sem contato humano.
3. **Caminho alternativo: reunião com especialista.** Hoje quase toda venda fecha numa call. Continua
   existindo para quem prefere conversar, mas não é o CTA principal.

Consequências para o marketing:
- CTA principal das peças: preview grátis / criar conta. CTA secundário: falar com um especialista.
- O preview é o que mais converte no outbound ("É do seu interesse ver gratuitamente como ficaria o seu
  aplicativo?", template `follow_features`).
- Métrica de marketing: contas criadas → previews vistos → assinaturas. Reuniões são métrica secundária.

## Links

| O quê | URL |
| --- | --- |
| Criar conta (CTA) | https://admin.korza.app/create-account |
| Login | https://admin.korza.app/login |
| Site | https://korza.app (domínio principal desde 2026-10-27; korza.com.br redireciona). Use sempre korza.app em anúncios e materiais |
| Instagram | https://www.instagram.com/korza.br/ |

## Método AOP (tática, não pilar)

Argumento comercial usado no passado, com certo sucesso. Pode aparecer em peças, mas não é sagrado
nem estrutura a marca.

| Letra | Pilar | O que é |
| --- | --- | --- |
| A | Aplicativo | App da loja nas lojas de apps, integrado ao e-commerce |
| O | Oferta | Incentivo para baixar o app (ex.: cupom exclusivo de primeira compra no app). Sem incentivo, a taxa de download cai muito |
| P | Push | Notificações direto na tela do cliente, com campanhas agendadas no painel |

## Pendências

- [ ] Atualizar quando os novos planos e as features comissionadas forem lançados

## Histórico

- 2026-10-26: criado a partir do site ao vivo ([fontes/site-2026-10-26.md](fontes/site-2026-10-26.md))
  e das respostas do Pedro.
- 2026-10-30: funcionalidades e funil real a partir do painel; prints em `telas/`.
