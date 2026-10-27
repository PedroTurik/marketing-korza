# Studio — vídeo da Korza

Tudo que é vídeo: motion (100% animado) e gravados (filmagem editada). Uma ferramenta só,
[HyperFrames](https://hyperframes.heygen.com): vídeo = HTML + GSAP, renderizado em MP4.
Skill do fluxo: `/korza-video`. Spec visual: [frame.md](frame.md), que deriva de `contexto/marca/MARCA.md`.

**Status: estrutura pronta, nunca usada em produção.** Template testado (check sem erros, frame renderizado
em 2026-10-26). Muita coisa só será decidida nas primeiras vezes; ver "A definir" abaixo.

## Estrutura

```
studio/
  STUDIO.md            este arquivo
  frame.md             spec de vídeo (copiado para cada projeto)
  novo.sh              cria um projeto: studio/novo.sh <motion|gravados> <slug> [--format reels|stories|feed|square]
  kit/korza-video.css  componentes de vídeo da marca (copiado para cada projeto)
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
npx hyperframes@0.8.158 snapshot --at 1,4,8 -o /tmp/snaps
npx hyperframes@0.8.158 preview                         # Studio no navegador
npx hyperframes@0.8.158 render --quality delivery --fps 30 -o renders/<slug>-v1.mp4
```

## A definir nas primeiras vezes

Decidir com o Pedro quando o primeiro vídeo de cada tipo for feito, e registrar aqui:

**Geral**
- [ ] Peças de abertura e fechamento padrão (`kit/`): existe uma vinheta? quanto dura? sempre igual?
- [ ] Trilha e efeitos sonoros: banco de músicas, trilha gerada, sem som? Volume/loudness de entrega
- [ ] Locução: voz do Pedro, voz gerada (`hyperframes tts`), ou só texto na tela?
- [ ] Ritmo e duração padrão por formato (Reels 15s? 30s? Stories?)
- [ ] Transição padrão (wipe azul do template ou corte seco)
- [ ] Atualizar o HyperFrames fixado (0.8.158; havia 0.8.206 em 2026-10-26) e testar

**Motion**
- [ ] Estrutura padrão de um ad (gancho → prova → CTA?) e variações A/B de gancho
- [ ] Biblioteca de cenas reaproveitáveis no `kit/` (count-up, push caindo, celular, CTA)
- [ ] Assinatura de movimento da marca (como o logo entra, como os cards entram)

**Gravados**
- [ ] Quem aparece e onde grava (luz, enquadramento, celular ou câmera, 9:16 nativo ou reenquadrar)
- [ ] Estilo de legenda (tamanho, posição, cor da palavra ativa, quantas palavras por vez)
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
