# Demanda: Motion M3, gancho novo ("Isso é o que você ganha")

**Status:** `feita`
**Criada em:** 2026-11-06
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Um `-v2` do M3 ("O painel") com outro gancho na tela e na voz. Todo o resto do vídeo fica igual.

## Por que

O gancho atual ("Tudo que o app da sua loja faz, num painel só.") descreve a ferramenta. O novo promete ganho: o que vem
depois é o que o lojista recebe ao lançar o app com a Korza. É o mesmo filme com uma abertura melhor.

## Leia antes

- `demandas/2026-11-05-motion-m3-painel.md` (a demanda original e a Entrega)
- `studio/motion/2026-11-05-m3-painel/STORYBOARD.md` (mapa de tempo e voz)
- `studio/STUDIO.md` (padrão de voz, legenda e mix)
- `conexoes/CONEXOES.md` (ElevenLabs: voz Bea, `voice_id`, modelo e speed)

## Requisitos

- **Gancho novo (voz, título e legenda):** "Isso é o que você ganha quando lança o app da sua loja com a Korza."
  Ajuste leve de palavra para o ritmo está liberado, sem mudar o sentido.
- **Animação da abertura não muda.** A pilha de telas em perspectiva, o colapso num plano e o mergulho da câmera ficam como
  estão (decisão do Pedro). Só retime o que for preciso para casar com a voz nova. O mergulho continua terminando antes da
  primeira feature ("Escreva o push…").
- **Voz:** gere só a frase do gancho com a Bea, nas mesmas configurações da voz do M3, e emende no áudio atual. O resto
  da voz não é regerado. Se a emenda soar diferente (timbre ou volume), avise o Pedro antes de regerar a voz inteira.
- Trilha, efeitos, mix e loudness como no v1. Se o gancho novo for mais longo, ajuste a trilha no grid, sem regerar.
- Duração dentro de 20–30s.
- Dois renders: `m3-painel-9x16-v2.mp4` (1080×1920) e `m3-painel-4x5-v2.mp4` (1080×1350). Os `-v1` ficam.

## Fora do escopo

- Mexer nas cenas de feature, na prova `recompra-1-em-3`, no fechamento ou no CTA
- Gancho B
- Subir anúncio, publicar ou escrever a legenda do post

## Critério de pronto

- [x] Gancho novo na voz, no título e na legenda, legível no frame 0
- [x] Animação de abertura igual à do v1 (só retime)
- [x] Emenda da voz sem salto de timbre ou volume
- [x] `npm run check` sem erros e snapshots revisados
- [x] 2 renders `-v2` em `renders/`
- [ ] `STORYBOARD.md` (mapa de tempo e voz) e `studio/motion/CATALOGO.md` atualizados (só o STORYBOARD; ver Entrega, item 5)

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Onde:** `studio/motion/2026-11-05-m3-painel/renders/` → `m3-painel-9x16-v2.mp4` e `m3-painel-4x5-v2.mp4` (27,8s, H.264 30 fps, AAC,
-14 LUFS). Os `-v1` estão intactos. Mapa de tempo e voz do v2 em `STORYBOARD.md`.

**Como ficou:**
1. **Gancho:** "Isso é o que você ganha quando lança o app da sua loja com a Korza." Texto sem mudança nenhuma, igual na voz, no título e na legenda.
   O título cai para 82px no 9:16 e 76px no 4:5 (v1: 100 e 92) para caber em 3 linhas sem bater no celular. A primeira linha, "Isso é o que você ganha",
   fica em branco cheio e o resto em branco 72%, o mesmo recurso do v1.
2. **Abertura:** a mesma animação, só retimada. A pilha abre por 2,85s (v1: 1,85s), colapsa em "com a Korza", e o mergulho termina às 4,38s,
   junto com "Escreva" (4,3s), a mesma relação do v1. Do colapso em diante tudo anda +1,0s (`D` no fim de `compositions/src/mundo.js`).
3. **Voz:** só o gancho foi gerado com a Bea (3 takes, mesma configuração). Usei o take 2, o mais próximo do v1 (-16,2 LUFS e 222 Hz, contra -16,1 e 219 Hz).
   A emenda no corpo do v1 (`assets/audio/gancho_v2.py`) mede -16,3 LUFS no gancho e -16,4 na frase seguinte, sem salto. Não regerei a voz inteira.
4. **Trilha e duração:** o respiro depois do gancho foi para 0,35s (v1: 0,30s), para o corpo andar exatamente 1,0s, que são 2 tempos a 120 BPM.
   A trilha ganha 2 tempos no pulso da abertura, sem regerar, e efeitos e automação andam junto. Total de 27,8s (v1: 26,8s), dentro de 20–30s.

**Diferente do pedido:**
5. **`studio/motion/CATALOGO.md` não foi atualizado:** é arquivo compartilhado e outros agentes estão mexendo nos motions agora (pedido do Pedro). Linha para colar:
   ```
   | `2026-11-05-m3-painel` (v2) | "O painel", gancho novo: "Isso é o que você ganha quando lança o app da sua loja com a Korza." Mesmo filme do v1, abertura retimada | recompra | `recompra-1-em-3`, `push-ilimitado` | Crie sua conta e veja seu app grátis (voz: Crie sua conta grátis na Korza) | 9:16 e 4:5, 27,8s | `renders/m3-painel-<9x16\|4x5>-v2.mp4` | Entregue, aguardando revisão do Pedro | — |
   ```
6. **`npm run check`:** 0 erros. Avisos novos: o título do gancho fica 3,93s na tela, contra o piso de leitura de 3,97s, mas é lido junto com a voz e a legenda. Os
   avisos por palavra na legenda, "Isso", "é" etc., são o falso positivo do karaokê. Os demais avisos são os do v1.
7. **Projeto passa a ser o v2:** `index.html`, `legenda.html`, `mix.sh` e `mundo.js` agora geram o v2. Para voltar ao v1, use `D = 0` em `mundo.js` e `mix.sh` e o texto
   antigo em `mundo.html`. O mix do v1 ficou em `assets/audio/mix-v1.wav`.

**Limite da revisão:** revisei por quadros amostrados e medições de áudio (loudness e tom na emenda). Não dá para ouvir a emenda daqui: vale escutar os
primeiros 5s.

**Pendências (Pedro):** ver e ouvir os 2 renders, principalmente a passagem "com a Korza." → "Escreva o push". Colar a linha do item 5 no `CATALOGO.md`.
