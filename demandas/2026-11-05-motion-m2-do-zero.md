# Demanda: Motion M2, "Do zero × Korza"

**Status:** `feita`
**Criada em:** 2026-11-05
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

**Depende do M1** (`demandas/2026-11-05-motion-m1-notificacao.md`). Já entregue: este
motion reaproveita a voz, a legenda, a trilha e a vinheta definidas lá.

## Objetivo

Um motion de cerca de 28s, com voz de IA e legenda, para anúncio na Meta e para o Reels do @korza.br. Ele mostra como é
fácil ter um app de alta qualidade com a Korza: rápido e barato, comparado a fazer do zero.

## Por que

Derruba a objeção "app é caro e demora" e fala com o **dono**. **O foco é a facilidade**, não o preço do concorrente. O
lado "do zero" é pesado e confuso e passa rápido; o lado Korza é leve, bonito e ganha mais tempo de tela. É um dos três
motions da primeira leva, que também servem de teste de criativo.

## Leia antes

- `studio/STUDIO.md` (com o padrão registrado pelo M1) e `studio/frame.md`
- `contexto/voz.md`, `contexto/marca/MARCA.md`
- `contexto/claims.md`: `app-sob-medida-100k`, `prazo-14-dias`, `sem-conta-dev`, `app-nativo`, `plataformas`
- `contexto/produto.md`: preço (R$ 399/mês) e "Funil real"
- `contexto/telas/README.md` e `contexto/telas/onboarding/`

## Design antes de animar (obrigatório)

O M1 ficou bom, mas simplista. Este motion precisa ser **mais dinâmico e mais desenhado**.

1. **Referência de ritmo:** abra o M1 (`studio/motion/2026-11-05-m1-notificacao/`) e o `STORYBOARD.md` dele, e vá além:
   corte ou movimento novo a cada 1–2s, composição em camadas, telas reais em perspectiva e profundidade, tipografia
   cinética, transições com intenção. Use `/hyperframes-animation` e `/hyperframes-registry` antes de desenhar à mão.
2. **Storyboard primeiro:** `STORYBOARD.md` no projeto com a direção visual, os quadros-chave de cada cena (snapshots
   estáticos) e o mapa de tempo. **Mostre ao Pedro e só anime depois do OK.**
3. **Copy e fluxo podem mudar** para servir ao visual: cortar, reordenar, trocar palavras, dividir cenas. **Não mudam:**
   o ângulo da peça, os claims (IDs abaixo, com a redação de `claims.md`), o CTA e a duração de 20–30s. Registre na
   Entrega o que mudou.

## Trilha

Eleven Music (ElevenLabs), por decisão do Pedro, mesmo marcada "For Individual Use Only". Uma faixa instrumental
gerada para este vídeo, no ritmo dos cortes. Mix, ducking e loudness como no padrão do `studio/STUDIO.md`.

## Roteiro (ponto de partida)

**Gancho (0–3s):**

- **A (principal):** "Um app do zero pode custar até R$ 100 mil."
- **B (variação):** "Quanto custa ter o app da sua loja?"

**Voz:**

> "Fazer do zero: até R$ 100 mil, meses de projeto, conta na Apple e no Google, aprovação nas lojas. Na Korza, você
> conecta sua loja, escolhe logo e cores, e pronto. A gente constrói e publica seu app em até 14 dias úteis! Crie sua
> conta grátis na Korza."

**Visual:**

- **Do zero:** acúmulo visual de custo e complicação (orçamento subindo até R$ 100 mil, calendário de meses, contas e
  aprovações empilhando). Tudo rápido e pesado.
- **Korza:** o onboarding real animado, a partir dos prints de `contexto/telas/onboarding/` (plataforma → nome → logo →
  cor → notificação de teste), recriados em HTML ou animados sobre os prints. Termina com um app bonito no celular. Pode
  usar os apps reais dos cases em `contexto/marca/cases/` para mostrar a qualidade final.
- O fechamento fica no modo impacto, com CTA e logo (vinheta do M1).

Pequenos ajustes de palavra para o ritmo estão liberados. Os números não mudam.

## Requisitos

- Dois ganchos × dois formatos: **9:16 (1080×1920)** e **4:5 (1080×1350)**. São 4 renders.
- Duração de 25 a 30s, com a voz e a legenda do padrão M1
- **Sem rodapé de fonte** na tela (decisão do Pedro; a fonte está em `claims.md`)
- Sempre "até R$ 100 mil" e "em até 14 dias úteis". Prazo do "do zero" só como "meses", sem número
- Nos prints, cortar o nome da conta de teste e o domínio de teste

## Fora do escopo

- Citar concorrente ou agência pelo nome
- "Sem comissão" e "sem setup": não entram nesta peça
- Subir anúncio, publicar ou escrever a legenda do post

## Critério de pronto

- [x] Lado Korza com mais tempo de tela que o "do zero"
- [x] Só telas reais do onboarding, sem dado de conta de teste visível
- [x] Claims conferidos com `claims.md`, sem rodapé
- [x] Storyboard aprovado pelo Pedro antes da animação
- [x] Ritmo acima do M1: corte ou movimento novo a cada 1–2s
- [x] Trilha da Eleven Music, com o prompt registrado no projeto
- [x] `npm run check` sem erros e snapshots revisados
- [x] ~~4~~ 2 renders `-v1` em `renders/` (versão única, decisão do Pedro)
- [x] Linha no `studio/motion/CATALOGO.md`

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Resultado (2026-11-05):** `studio/motion/2026-11-05-m2-do-zero/`
- Renders finais: `renders/m2-do-zero-9x16-v2.mp4` (1080×1920) e `renders/m2-do-zero-4x5-v2.mp4` (1080×1350), 25,25s,
  H.264 + AAC, áudio em -14 LUFS. `renders/` fica fora do git. Os `-v1` (27,4s) ficaram como histórico.
- Storyboard aprovado: `STORYBOARD.md` + `storyboard/quadros-chave.jpg`. Prompt da trilha: `assets/audio/trilha-prompt.json`.
- Tempo de tela: "do zero" 9,15s, Korza 16,1s. Corte ou movimento novo a cada 1–1,5s.

**O que mudou em relação ao pedido:**
1. **Uma versão só** (gancho A), por decisão do Pedro: 2 renders em vez de 4.
2. Voz: abre com o gancho A ("Um app do zero pode custar até cem mil reais") no lugar de "Fazer do zero: até R$ 100 mil";
   o "do zero" virou frases curtas, uma por camada da pilha. Entraram "iOS e Android" (`app-nativo`) e "Sem conta de
   desenvolvedor" (`sem-conta-dev`), da lista de claims da demanda; o "sem conta" saiu no v2.
3. CTA na tela igual ao M1 ("Crie sua conta e veja seu app grátis →"); a voz diz "Crie sua conta grátis na Korza".
4. Onboarding recriado em HTML, fiel aos prints, com a loja genérica "Sua Loja" (decisão do Pedro): sem nome, domínio ou
   e-mail da conta de teste. Passos mostrados: plataforma, logo, cor da navegação, notificação de teste. O passo "Nome do
   app" aparece só no preview (nome na tela inicial).
5. Ato 1 em modo profundo por 9s (o `frame.md` pede no máximo uma cena): é o contraste da peça, aprovado no storyboard.
6. Legenda em pílula do início ao CTA, mesmo onde o título já repete a fala (decisão do Pedro).
7. Números sem contagem nem odômetro: um primeiro render mostrava valores como "R$ 421 mil" no giro dos dígitos. O
   "100" e o "14" ficam fixos e só mudam de escala; esse render foi descartado.
8. Trilha: a chave da ElevenLabs ganhou a permissão Music Generation. A primeira faixa morreu em 17s e foi descartada; a
   segunda tem 3 seções e a última veio ~3x mais alta, compensada no `mix.sh`.
9. Kit: `studio/kit/audio/sintetizar.py` ganhou `baque`, `toque` e `whoosh`. `STUDIO.md` (padrão de trilha, efeitos,
   armadilhas do M2) e `conexoes/CONEXOES.md` (Eleven Music liberada) atualizados.
10. **v2, a pedido do Pedro:** legenda desceu para y=1480 (9:16) e 1196 (4:5), para não tapar a tela; "Sem conta de
    desenvolvedor" saiu (voz cortada sem regerar, trilha perde um compasso, vídeo vai de 27,4s para 25,25s);
    selos iOS e Android ganharam os logos da App Store e do Google Play.
