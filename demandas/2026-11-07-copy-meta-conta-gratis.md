# Demanda: Copy dos anúncios da campanha Meta `2026-11-meta-conta-gratis`

**Status:** `aprovada`
**Criada em:** 2026-11-07
**Especialidade:** copy
**Skill:** nenhuma

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Texto principal e título de 8 anúncios em vídeo da primeira campanha de conversão da Korza na Meta, num arquivo pronto
para colar: `campanhas/2026-11-meta-conta-gratis/COPY.md`.

## Por que

É a primeira campanha paga com o funil novo: o lojista cria a conta grátis, vê o preview do app e assina sozinho
(R$ 399/mês), sem reunião. A campanha otimiza para **conta criada**. Dois conjuntos com o mesmo público frio (donos de
e-commerce que não conhecem a Korza): **Motion** e **Gravados** (sócios falando). O teste compara mensagem e formato; o
texto precisa **reforçar o vídeo, não competir com ele**. Fala com o **dono** (exceto o M3, que fala com o gestor).

Público: donos de e-commerce Nuvemshop/Shopify, R$ 30 mil+/mês, céticos, recebem pitch toda semana.

## Leia antes

- `contexto/voz.md` (fórmula gancho → fato → convite, CTAs, vocabulário)
- `contexto/claims.md` (só números e afirmações aprovados, com as regras de uso de cada um)
- `contexto/produto.md` (oferta, preço, funil)
- `contexto/publico.md` (dores e objeções)
- Motions: o `STORYBOARD.md` de cada projeto em `studio/motion/` (copy e voz de cada vídeo)
- Gravados: os vídeos em `inbox/ads-novos/`. Transcreva para saber o que cada um diz (`npx hyperframes@0.9.16 transcribe`).
  Os vídeos já estão aprovados: não precisa conferir os claims deles. O que vale conferir é o **seu texto**

## Os anúncios

| # | Conjunto | Vídeo | Ângulo / pilar |
| --- | --- | --- | --- |
| 1 | Motion | M1 v2 "A notificação" (`studio/motion/2026-11-05-m1-notificacao/renders/m1-notificacao-a-*-v2.mp4`) | Canal próprio: todo mundo lê a notificação |
| 2 | Motion | M2 v2 "Do zero × Korza" (`.../2026-11-05-m2-do-zero/renders/m2-do-zero-*-v2.mp4`) | Conversão: app do zero custa até R$ 100 mil × Korza |
| 3 | Motion | M2 "busca" (`.../m2-do-zero-busca-*-v1.mp4`) | Mesmo filme do #2, com gancho "Como criar um app do meu e-commerce…?" |
| 4 | Motion | M3 v2 "O painel" (`.../2026-11-05-m3-painel/renders/m3-painel-*-v2.mp4`) | Recompra, fala com o gestor: "Isso é o que você ganha…" |
| 5 | Gravados | Recompra na mesa (`inbox/ads-novos/ads-recompra-na-mesa.mp4`) | Recompra |
| 6 | Gravados | 14 dias (`inbox/ads-novos/ads-14-dias.mp4`) | Recompra / facilidade |
| 7 | Gravados | Como funciona (`inbox/ads-novos/ads-como-funciona.mp4`) | Facilidade: como é lançar o app na Korza |
| 8 | Gravados | Black Friday (`inbox/ads-novos/Korza-Black-Friday-Preview.mp4`) | Vantagens do app em datas de pico. Roda só até 20/11 |

O "Custo de ser amador" também entra no conjunto Gravados, mas usa o post que já está no Instagram, com a legenda dele:
**não precisa de texto**.

## Requisitos

- **Por anúncio:** 1 texto principal e 1 título. **Uma versão de cada**: o teste é do vídeo, e variar o texto confunde a
  leitura.
  - **Texto principal:** a primeira linha é o gancho e precisa funcionar sozinha (~125 caracteres aparecem antes do "mais").
    Total de até ~400 caracteres. Fórmula de `voz.md`: gancho humano → fato → convite.
  - **Título:** até 40 caracteres, fala da oferta (ex.: "Veja seu app grátis").
- **#2 e #3 têm o mesmo texto.** Só o gancho do vídeo muda: se o texto mudar, o teste de gancho se perde.
- **CTA:** "Veja seu app grátis" ou "Crie sua conta grátis". O botão da Meta será "Cadastre-se". O destino é a criação
  de conta; não citar reunião nem especialista.
- **Facilitador em todos os textos** (derruba a objeção, sem virar a mensagem principal): conta grátis com preview e
  `assina-sozinho`. Preço e `sem-setup-comissao` podem entrar; confira a data em `produto.md` (verificado em 2026-11-06).
- **Claims:** só de `claims.md`, com a redação e as ressalvas de cada um ("em até 14 dias úteis", número de case com o
  nome do cliente, meta nunca como resultado). Nada que prometa resultado.
- **#8 (BF):** sem prometer app pronto para esta Black Friday. Fale da vantagem em datas de pico de forma geral.
- Grafia: "e-commerce", "Nuvemshop", "Shopify", "R$ 399/mês". No máximo 1 emoji por texto, e só com função. Sem hashtag.
- **Formato da entrega:** uma seção por anúncio (`## 1 — M1 v2`), com `Texto principal:` e `Título:` em bloco de código
  para copiar e colar.

## Fora do escopo

- Mexer nos vídeos ou nas legendas deles
- Texto do post "Custo de ser amador"
- Subir anúncio, configurar campanha ou publicar

## Critério de pronto

- [x] 8 anúncios com texto principal e título em `campanhas/2026-11-meta-conta-gratis/COPY.md`
- [x] Primeira linha de cada texto funciona sozinha, com até ~125 caracteres
- [x] Títulos com até 40 caracteres
- [x] #2 e #3 com texto idêntico
- [x] Todo número e afirmação existe em `claims.md` e respeita a regra de uso
- [x] O texto conversa com o que o vídeo diz (gravados transcritos)

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

Feita em 2026-11-07: `campanhas/2026-11-meta-conta-gratis/COPY.md`. 8 anúncios, ganchos de 46 a 70 caracteres, textos de
288 a 354, títulos de 19 a 29. #2 e #3 idênticos (conferido por script). Gravados transcritos com
`npx hyperframes@0.9.16 transcribe`.

Diferente do pedido: nada. Pontos para o CMO (fora do escopo, não mexi):

- "Recompra na mesa" e "14 dias" terminam com "Clique em Saiba Mais e eu monto uma estratégia de graça para você": o
  botão será "Cadastre-se" e o destino é a conta grátis, não reunião. O texto puxa para a conta grátis; o vídeo, não.
- "Como funciona" e "Black Friday" fecham com "clica aqui" e "app lançado/gere seu app em duas semanas".
- O BF diz "pode aumentar até 20% as suas vendas", número que não está em `claims.md`. Vídeo já aprovado, só registro.
