---
name: korza-video
description: Criar, editar ou renderizar vídeos da Korza com HyperFrames — motion (ads animados, reels, kinetic type, count-up, logo) e vídeos gravados (cortar fala, legendar, overlays, lower third, reenquadrar). Use para qualquer pedido de vídeo, reels, stories, ad em vídeo, motion, "edita esse vídeo", legenda, corte de vídeo gravado ou render neste hub.
---

# Vídeo da Korza

Camada da marca Korza por cima do HyperFrames. A mecânica (composição, GSAP, lint, render, transcrição)
vem das skills `/hyperframes*`. Aqui ficam o fluxo do hub e as regras da marca. Visão geral e pendências:
`studio/STUDIO.md`.

## 0. Contexto obrigatório

- `studio/frame.md` (spec de vídeo) e `contexto/marca/MARCA.md` (sistema visual).
- `contexto/voz.md` (como escrever, CTAs), `contexto/claims.md` (únicos números permitidos),
  `contexto/posicionamento.md` (pilares: cada vídeo defende **um**).
- `studio/<tipo>/CATALOGO.md`: não repetir conceito/gancho já feito, salvo variação pedida.
- `inbox/`: material novo.
- **`studio/STUDIO.md` → "A definir nas primeiras vezes"**: se o pedido depende de algo ainda não decidido
  (trilha, locução, vinheta, estilo de legenda…), pergunte ao Pedro, proponha um padrão e registre a
  decisão em `STUDIO.md` depois de aprovada.

## 1. Brief

| Item | Padrão |
| --- | --- |
| Objetivo / mensagem | — (pergunte se faltar) |
| Pilar | recompra, conversão, marca ou canal próprio |
| Formato | Reels 9:16, 1080×1920 |
| Duração | 15s (motion); gravados conforme o material |
| Prova | um claim de `claims.md`, com nome do case |
| CTA | "Veja seu app grátis" |
| Áudio | pergunte (ainda não há padrão) |

Número fora de `claims.md`: pergunte. Não invente.

## 2. Criar o projeto

```bash
studio/novo.sh motion <slug> --format reels      # ou gravados; stories | feed | square
```

Não rode `hyperframes init`. Brutos do `inbox/` vão para `assets/footage/` (vídeo não H.264:
`ffmpeg -i in.mov -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac out.mp4`).

## 3. Roteiro

Escreva `BRIEF.md` e `STORYBOARD.md` no projeto: uma linha por cena com tempo, modo (claro/impacto/profundo),
texto na tela, visual e claim usado. Mostre ao Pedro antes de construir.

**Gravados:** rode `npx hyperframes@0.9.16 transcribe` no bruto, escreva `CORTES.md` (trechos mantidos com
timecode, o que sai e por quê, gancho escolhido) e peça aprovação antes de montar.

## 4. Construir

1. Carregue `/hyperframes` e siga o workflow que ele indicar:
   `/general-video` (ad de várias cenas), `/motion-graphics` (peça curta de uma ideia),
   `/talking-head-recut` (gravado + overlays), `/embedded-captions` (gravado + legendas),
   `/music-to-video` (cortes no beat).
2. Convenções do template: uma cena por arquivo em `compositions/sN-<nome>.html`, montada no `index.html`
   com `data-start`/`data-duration`, cortes na lista `CUTS`. Classes de `assets/brand/korza-video.css`.
   Caminhos de assets relativos à raiz do projeto. Elementos que saem do frame:
   `data-layout-allow-overflow="true"`. `&nbsp;` para evitar quebras ruins ("14&nbsp;dias").

## 5. Verificar

```bash
npm run check
npx hyperframes@0.9.16 snapshot --at <1 tempo por cena> -o /tmp/<projeto>-snaps
```

- [ ] Texto/números/logo na zona segura
- [ ] Só cores e fonte da marca; modo de cada cena coerente
- [ ] Números de `claims.md`, com case nomeado e ressalva quando for case
- [ ] Uma ideia e um destaque por cena; gancho legível no frame 0
- [ ] CTA visível ≥ 2,5s no fim
- [ ] Gravados: legenda sincronizada e dentro da zona segura; cortes conforme `CORTES.md`

## 6. Renderizar e entregar

```bash
npx hyperframes@0.9.16 render --quality delivery --fps 30 -o renders/<slug>-<formato>-v1.mp4
```

Confira com `ffprobe` e informe o caminho. Nova versão = novo sufixo. Adicione a linha no `CATALOGO.md`.
