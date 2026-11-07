# Studio — vídeo da Korza

Tudo que é vídeo: motion (100% animado) e gravados (filmagem editada). Uma ferramenta só,
[HyperFrames](https://hyperframes.heygen.com): vídeo = HTML + GSAP, renderizado em MP4.
Skill do fluxo: `/korza-video`. Spec visual: [frame.md](frame.md), que deriva de `contexto/marca/MARCA.md`.

**Status: em produção desde 2026-11-05** (M1, "A notificação"). O padrão de motion está em "Padrão de motion" abaixo;
o que ainda não foi decidido fica em "A definir".

## Estrutura

```
studio/
  STUDIO.md            este arquivo
  frame.md             spec de vídeo (copiado para cada projeto)
  novo.sh              cria um projeto: studio/novo.sh <motion|gravados> <slug> [--format reels|stories|feed|square]
  kit/korza-video.css  componentes de vídeo da marca (copiado para cada projeto): fundos, tipo, celular de
                       bloqueio (.lock), notificação (.notif), legenda (.cap), CTA, logo
  kit/vinheta.html     vinheta de fechamento (logo + CTA, 2,2s), copie para compositions/
  kit/audio/           trilha e efeitos próprios: sintetizar.py gera trilha-korza-01, notificacao e tick (.wav fora do git)
  template/            projeto HyperFrames base (1 cena, modo claro)
  motion/              um projeto por vídeo animado + CATALOGO.md
  gravados/            um projeto por vídeo gravado + CATALOGO.md
```

Cada projeto: `AAAA-MM-DD-<slug>/` com `index.html`, `compositions/sN-*.html`, `frame.md`,
`assets/brand/` (cópia da marca), `assets/footage/`, `assets/audio/`, `renders/` (fora do git).

## Fluxos

**Motion** (ad animado, número, kinetic type, logo sting): brief → `novo.sh motion` → roteiro por cena →
`/hyperframes` (`/general-video` ou `/motion-graphics`) → `npm run check` → snapshots → render.

**Gravados** (vídeo de fala: você explicando, depoimento, tutorial, corte de live):
bruto em `inbox/` → `novo.sh gravados` → `hyperframes transcribe` → proposta de corte (silêncios, erros,
takes repetidos, gancho) → aprovação → `/talking-head-recut` (overlays: títulos, lower thirds, números,
telas do produto) ou `/embedded-captions` (só legendas) → abertura/fechamento da marca → check → render.

Limite: o Claude trabalha pela transcrição e por frames amostrados, não assiste ao vídeo. Ótimo para
vídeos de fala; para edição de ritmo visual, primeiro corte aqui e refino num editor.

## Comandos

```bash
studio/novo.sh motion <slug> --format reels
cd studio/motion/<projeto>
npm run check                                           # rode SEMPRE após editar
npx hyperframes@0.9.16 snapshot --at 1,4,8 -o /tmp/snaps
npx hyperframes@0.9.16 preview                         # Studio no navegador
npx hyperframes@0.9.16 render --quality delivery --fps 30 -o renders/<slug>-v1.mp4
```

## Padrão de motion (definido no M1, 2026-11-05; vale para M2, M3…)

Referência pronta: `motion/2026-11-05-m3-painel/` (a mais desenhada: plano-sequência 3D, telas extraídas do admin, motion blur) e
`motion/2026-11-05-m2-do-zero/` (dois atos, onboarding recriado em HTML; copie `assets/audio/mix.sh`, `assets/audio/legenda.py` e `build.sh`). O M1 (`motion/2026-11-05-m1-notificacao/`) é o
primeiro, mais simples.

- **Planejamento de design antes de animar** (aprendido no M1, que ficou simplista): antes de qualquer cena,
  o executor faz um `STORYBOARD.md` com direção visual, quadros-chave e ritmo de cortes, e pode ajustar copy e
  fluxo para servir ao visual. O Pedro aprova o storyboard antes da animação. Alvo: corte ou movimento novo a cada
  1–2s, composições com camadas, telas reais em perspectiva, tipografia cinética.
- **Estrutura:** gancho (0–3s, legível no frame 0) → virada (a frase que liga o gancho à Korza) → prova/benefício
  (claims, um por vez, no ritmo da voz) → CTA (modo impacto, ≥ 2,5s na tela) → vinheta (logo). 20–30s.
- **Voz:** ElevenLabs, voz **Bea** (`cabLxBh81HurPAAJfEHo`), `eleven_v3`, `speed` 1.05, tags `[curious]`/`[confident]`.
  Configuração e chamada em `conexoes/CONEXOES.md`. Gere com `/with-timestamps` e guarde `vo.mp3` + `vo-words.json`
  no projeto (o mp3 vai para o git: regenerar custa crédito e muda a leitura). Números por extenso no texto da voz.
  A voz entra em ~1,0s, depois do som do gancho.
- **Legenda:** queimada, pílula branca (`.cap`), Plus Jakarta 600 58px, navy com a palavra falada em azul, 1–5
  palavras por grupo, gerada dos tempos da voz por `legenda.py` (não editar à mão). Posição: topo em y=1480 no 9:16 e
  y=1196 no 4:5, abaixo do conteúdo, para não tapar a tela (pedido do Pedro no M2; o M1 usava 1090/1166). Na tela, números em algarismo ("14 dias úteis") mesmo com a
  voz por extenso. Quando o texto falado já está na tela como CTA, a legenda sai. A pílula fica mesmo quando o título
  cinético repete a fala (decisão do Pedro no M2).
- **Trilha:** **Eleven Music (ElevenLabs)**, por decisão do Pedro em 2026-11-05, mesmo marcada "For Individual Use
  Only" no plano atual: risco de licença aceito por ele (anúncio pago pode ser contestado ou silenciado). Gere uma
  faixa por vídeo, instrumental, combinando com o ritmo das cenas, e registre o prompt no projeto. Fica baixa: ganho
  ~0,30 + ducking pela voz (`sidechaincompress`). Reserva sem risco: trilha própria de `kit/audio/sintetizar.py`
  (`trilha-korza-01`, usada no M1). Biblioteca do Instagram não serve. Chamada: `POST /v1/music` com `composition_plan`
  (uma seção por ato, `duration_ms` somando a duração do vídeo; exemplo em `motion/2026-11-05-m2-do-zero/assets/audio/
  trilha-prompt.json`). A chave precisa da permissão Music Generation. Confira o RMS por segundo antes de mixar: no M2 a
  primeira faixa morreu em 17s e a segunda subiu ~3x na última seção (o `mix.sh` compensa com automação de ganho).
- **Efeitos:** `notificacao.wav` (sino genérico de dois toques, sem som da Apple), `tick.wav` (entrada de tópico),
  `baque.wav` (cartão batendo), `toque.wav` (toque na tela) e `whoosh.wav` (transição), todos de `sintetizar.py`.
- **Vinheta:** `kit/vinheta.html`, modo impacto, logo branco grande + CTA, 2,2s; o CTA fica na mesma posição (base da
  zona segura) na cena de CTA e na vinheta, então ele não "pula" e soma ≥ 2,5s na tela.
- **Transição:** wipe azul do template nos cortes de cena; corte seco entre CTA e vinheta (mesmo fundo).
- **Loudness de entrega:** mix único `mix.wav` por `mix.sh`: **-14 LUFS integrado, -1 dBTP** (loudnorm em 2 passadas),
  48 kHz. Um `<audio id="mix">` só na composição.
- **Formatos e variações:** um projeto, um `index.html` (9:16, gancho A). `build.sh check|snap|render` gera 9:16 e 4:5
  (1080×1350) × gancho A/B trocando `data-fmt`/`data-gancho` no `#root`. Regras de variante ficam no `<style>` do
  `index.html` (o CSS das cenas é isolado e não enxerga o `#root`). Renders: `renders/<slug>-<gancho>-<9x16|4x5>-vN.mp4`.
- **Armadilhas do HyperFrames vistas no M1:** id de elemento interno igual ao id do host da cena move a cena inteira;
  só um HTML raiz por projeto (por isso o `build.sh` troca o `index.html`); sub-composição precisa de `data-height`
  do formato (o `build.sh` ajusta).
- **Armadilhas vistas no M2:** estado inicial escondido vai no CSS (`opacity: 0`), não em `tl.set(..., 0)`, que não
  aparece no frame 0; transform do GSAP apaga o `transform` do CSS (escala fixa num elemento, câmera num wrapper);
  `[data-composition-id='x']` acha primeiro o host no `index.html`, então variável CSS animada mora num elemento com id
  próprio dentro da cena; `left`/`top` animados dão erro no check (use `x`/`y`); camadas que se sobrepõem de propósito
  (pilha de papéis, UI dentro do celular) levam `data-layout-ignore` para o check passar sem esconder erro real.

- **Telas do painel (M3):** não redesenhe nem use print. `assets/telas/extrair.spec.ts.txt` roda numa **cópia** do admin (`git archive` no
  scratchpad, mocks do e2e, nenhum dado real) e gera HTML vetorial com estilos computados: fiel ao produto e nítido em qualquer zoom. Os fixtures
  aceitam o texto que a peça precisa, então o app real renderiza a copy aprovada. Públicos e domínio de teste saem lá. `assets/telas/montar.py` monta a cena.
- **Motion blur (M3):** `build.sh` roda o filme 4x mais lento a 240 fps (`assets/telas/lento.py`; 240 é o máximo do HyperFrames) e funde 16 amostras por
  quadro de 30 fps (`tmix`), obturador de 1/60s. Com só 4 amostras os voos ficam estroboscópicos. Cerca de 5 min por formato. Áudio volta no ffmpeg; `loudnorm` com
  TP -1,5 porque o AAC sobe o pico.
- **Armadilhas vistas no M3:** `document.querySelector` dentro de cena não enxerga o `#root` do `index.html` (variante vai por constante, trocada no `build.sh`);
  `<desc>`/`<title>` vazios em SVG quebram o serializador do HyperFrames e aninham o resto da cena; `<p>` com `<div>` ou botão dentro de botão também (gere tudo como
  `div`); timeline aninhada precisa de `tl.paused(false)`, senão a render sai congelada. **Sempre confira quadros e tamanho do arquivo**: 2 MB em 27s era o congelamento;
  o tempo do alinhamento da ElevenLabs erra até 0,3s no início das frases, então cheque com `silencedetect` (`assets/audio/editar_voz.py`).
- **Trilha sem regerar (M3):** rode `hyperframes beats`; a Eleven Music costuma errar a duração das seções, mas o grid é exato, e dá para repetir ou cortar compassos no `mix.sh`.

## A definir nas primeiras vezes

Decidir com o Pedro quando o primeiro vídeo de cada tipo for feito, e registrar aqui:

**Geral**
- [x] Peças de abertura e fechamento padrão: vinheta de fechamento `kit/vinheta.html` (2,2s). Abertura: não há; o vídeo abre no gancho
- [x] Trilha e efeitos sonoros: própria, sintetizada (`kit/audio/`); entrega em -14 LUFS / -1 dBTP
- [x] Locução: voz gerada na ElevenLabs (Bea), com legenda queimada
- [ ] Ritmo e duração padrão por formato (motion com voz: 20–30s, definido no M1; Stories e peças sem voz em aberto)
- [x] Transição padrão: wipe azul entre cenas; corte seco entre CTA e vinheta
- [x] HyperFrames atualizado para 0.9.16 (template e M1, 2026-11-05)

**Motion**
- [x] Estrutura: gancho → virada → prova → CTA → logo; variação de gancho por `data-gancho` (A/B) no mesmo projeto
- [ ] Biblioteca de cenas reaproveitáveis no `kit/` (já há celular de bloqueio, notificação, legenda e CTA no CSS; falta count-up)
- [ ] Assinatura de movimento da marca (como o logo entra, como os cards entram). Candidato: o plano-sequência do M3, se o Pedro aprovar

**Gravados**
- [ ] Quem aparece e onde grava (luz, enquadramento, celular ou câmera, 9:16 nativo ou reenquadrar)
- [x] Estilo de legenda: o mesmo do motion (pílula `.cap`, ver "Padrão de motion")
- [ ] Lower third: quando e com qual texto
- [ ] Nível de corte: só silêncios e erros, ou edição dinâmica (zoom, B-roll)
- [ ] B-roll: telas do produto, gravações de tela do painel, mockups
- [ ] Fluxo de revisão: o Pedro aprova o roteiro de corte antes de montar?
- [ ] Ferramenta de refino (DaVinci/Premiere/CapCut) e formato de exportação da lista de cortes

## Regras

- Marca de `frame.md` / `MARCA.md`; texto de `contexto/voz.md`; números só de `contexto/claims.md`.
- Nunca inventar número, cliente, depoimento ou tela de app. Push com nome de loja cliente, nunca o símbolo da Korza.
- `npm run check` sem erros + revisão visual dos snapshots antes de renderizar.
- Renders versionados: `-v1`, `-v2`… nunca sobrescrever um render entregue.
- Ao entregar: uma linha no `CATALOGO.md` da pasta (motion ou gravados).
