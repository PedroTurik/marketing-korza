# Demanda: Motion M2, variação com gancho de busca ("Como criar um app…")

**Status:** `feita`
**Criada em:** 2026-11-06
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Uma variação do M2 ("Do zero × Korza") que abre com um gancho novo em forma de pergunta de busca. Depois dele, o vídeo
segue igual ao `-v2`. O `-v2` atual continua como está: são duas versões para testar o gancho.

## Por que

O gancho atual ("Um app do zero pode custar até R$ 100 mil") abre pela dor do preço. O novo fala a pergunta que o dono de
loja digita quando começa a pensar em app, e se identifica na hora com Shopify e Nuvemshop. Rodando os dois, o anúncio
mostra qual abertura segura mais.

## Leia antes

- `demandas/2026-11-05-motion-m2-do-zero.md` (a demanda original e a Entrega)
- `studio/motion/2026-11-05-m2-do-zero/STORYBOARD.md` (mapa de tempo, voz, som)
- `studio/STUDIO.md` (padrão de voz, legenda e mix)
- `conexoes/CONEXOES.md` (ElevenLabs: voz Bea, `voice_id`, modelo e speed)
- `contexto/claims.md`: `plataformas`

## Requisitos

- **Gancho novo, 0–~2,5s (voz, tela e legenda):** "Como criar um app do meu e-commerce Shopify ou Nuvemshop?"
  - Na tela, a pergunta é digitada numa barra de busca genérica (sem logo do Google ou de outro buscador), com cursor e
    som leve de tecla. Precisa ser legível no frame 0 ou logo depois: comece já com parte do texto digitado.
  - Grafia: "Nuvemshop", "Shopify", "e-commerce".
  - Em seguida entra o M2 atual, a partir de "Um app do zero pode custar até cem mil reais", sem outras mudanças. A
    transição da busca para o ato 1 precisa ter intenção (a busca "responde" com a pilha de custo, por exemplo), sem corte seco.
- **Voz:** gere só a pergunta com a Bea, nas mesmas configurações do M2, e emende antes da voz atual. O resto não é
  regerado. Se a emenda soar diferente, avise o Pedro antes de regerar.
- **Trilha:** estenda a abertura da faixa atual no grid (repetir ou adaptar a introdução), sem regerar. Mix e loudness
  como no `-v2`.
- Duração total até 30s (estimativa: ~28s).
- Dois renders, no mesmo projeto: `m2-do-zero-busca-9x16-v1.mp4` (1080×1920) e `m2-do-zero-busca-4x5-v1.mp4`
  (1080×1350). Os renders `m2-do-zero-*-v2` não são alterados.
- Organize no projeto de um jeito que as duas versões continuem renderizáveis (variável de gancho ou composição separada).

## Fora do escopo

- Mudar qualquer coisa do M2 depois do gancho
- Citar concorrente, agência ou buscador pelo nome
- Subir anúncio, publicar ou escrever a legenda do post

## Critério de pronto

- [x] Gancho de busca na voz, na tela e na legenda, legível em menos de 1s
- [x] Resto do vídeo idêntico ao `-v2`
- [x] Versão original (`-v2`) continua renderizando igual
- [x] Emenda da voz e da trilha sem salto
- [x] `npm run check` sem erros e snapshots revisados
- [x] 2 renders `m2-do-zero-busca-*-v1` em `renders/`
- [x] `STORYBOARD.md` atualizado; ~~`studio/motion/CATALOGO.md`~~ pendente (arquivo compartilhado, ver Entrega)

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Resultado (2026-11-06):** `studio/motion/2026-11-05-m2-do-zero/`
- Renders: `renders/m2-do-zero-busca-9x16-v1.mp4` (1080×1920) e `renders/m2-do-zero-busca-4x5-v1.mp4` (1080×1350),
  28,47s, H.264 + AAC, -14,4 LUFS (o `-v2` sai com -14,5). Os `-v2` não foram tocados.
- Gancho: 3,2s (96 quadros). Barra de busca genérica no modo profundo do ato 1, com "Como criar um app" já digitado no
  frame 0, digitação à frente da voz, cursor e clique de tecla. No Enter, a barra sobe e o fundo some, revelando o título
  "até R$ 100 mil" e o orçamento (a "resposta" da busca), com whoosh. Legenda em pílula com a pergunta desde 0,03s.
- Resto idêntico: quadros do pós-gancho comparados pixel a pixel com o `-v2` (diferença só de antialias, máx. 12/255 em
  3 pixels); áudio depois do gancho com correlação 1,000 e -0,07 dB em relação ao `mix.wav` do M2.
- Organização: tudo em `assets/audio/busca/` (`gerar.py`, `variante.py`, `mix.sh`, `gerar_voz.py`, voz e tempos) +
  `compositions/s0-busca.html` e `legenda-busca.html` (gerados). `bash build.sh check|snap|render --gancho busca`; sem
  `--gancho`, o `build.sh` faz o mesmo de antes. Explicado no `STORYBOARD.md`.

**O que ficou diferente do pedido:**
1. Gancho de 3,2s, não ~2,5s: a pergunta falada pela Bea dura ~3,1s. Total 28,47s (limite de 30s).
2. Voz: 3 takes da pergunta, nas configurações do M2; ficou o mais limpo na transcrição. Pausa de ~0,35s antes de
   "Um app do zero". Não dá para ouvir daqui: pelos números, o volume foi casado com o começo do `vo.mp3` (-1 dB) e o
   timbre é o mesmo modelo e voz. **Ouça a emenda em ~3,2s**; se soar diferente, regero.
3. Trilha: a abertura repete o 1º compasso (meio + inteiro, no grid de 112 BPM) e emenda na faixa do M2 no mesmo ponto do
   compasso.
4. `studio/motion/CATALOGO.md` **não foi alterado**: outros agentes estão mexendo nos arquivos compartilhados. Linha
   sugerida, para incluir depois:
   `| 2026-11-05-m2-do-zero (busca) | Variação do M2 com gancho de busca: "Como criar um app do meu e-commerce Shopify ou Nuvemshop?" digitado numa barra genérica, que "responde" com a pilha de custo; depois, igual ao -v2 | conversão | app-sob-medida-100k, plataformas, app-nativo, prazo-14-dias | Crie sua conta e veja seu app grátis | 9:16 + 4:5, 28,47s | renders/m2-do-zero-busca-{9x16,4x5}-v1.mp4 | pronto, não publicado | — |`

