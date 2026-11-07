---
version: 2
name: Korza — Frame (vídeo)
description: >
  Spec de vídeo da Korza para HyperFrames. Deriva de contexto/marca/MARCA.md (sistema claro, azul como
  impacto, profundo como acento raro). Unidade = frame vertical 1080×1920 (Reels/Stories); feed 1080×1350
  e quadrado 1080×1080 documentados abaixo. Copiado para a raiz de cada projeto (as skills do HyperFrames leem daqui).
unit: 1080×1920 primary; 1080×1350 and 1080×1080 documented
principle: premium pelo capricho, simples pelo respiro · números só de contexto/claims.md · texto de contexto/voz.md

colors:
  blue: "#155DFC"        # a marca: destaque, CTA, palavra-chave, modo impacto
  blue-deep: "#0B3CAE"   # fim do gradiente de impacto
  navy: "#10213B"        # títulos sobre claro; fundo do modo profundo
  slate: "#42556C"       # corpo sobre claro
  gray: "#7D8DA1"        # segunda parte do título em dois tons
  muted: "#708096"       # notas, ressalvas
  line: "#E5EBF2"        # bordas
  ice: "#F5F8FC"         # fundo claro alternativo
  white: "#FFFFFF"

typography:
  # Única família: Plus Jakarta Sans, pesos 400 e 600. Arquivo: assets/brand/fonts/
  display:  { px: 116, weight: 600, lineHeight: 1.04, tracking: "-0.045em" }
  title:    { px: 80,  weight: 600, lineHeight: 1.08, tracking: "-0.035em" }
  title-sm: { px: 60,  weight: 600, lineHeight: 1.12, tracking: "-0.03em" }
  stat:     { px: 240, weight: 600, lineHeight: 0.9,  tracking: "-0.055em" }
  body:     { px: 38,  weight: 400, lineHeight: 1.38, tracking: "-0.01em" }
  eyebrow:  { px: 30,  weight: 600, lineHeight: 1.2 }
  note:     { px: 24,  weight: 400, lineHeight: 1.4 }
  caption:  { px: 52,  weight: 600, lineHeight: 1.15 }

spacing:
  edge-x: "72px"
  safe-top-reels: "270px"
  safe-bottom-reels: "670px"
  safe-bottom-stories: "380px"

components: "assets/brand/korza-video.css — bg-light/bg-soft/bg-impact/bg-deep, on-light/on-dark, content, display, title, body, eyebrow, note, stat, tone, hl, card, push, phone, cta, logo-sm/lg, shape, caption, lower-third"
---

# Korza — Frame (vídeo)

Leia também `contexto/marca/MARCA.md` (sistema completo) e `contexto/voz.md` (como escrever).

## Modos de cena

| Modo | Classe de fundo | Texto | Uso |
| --- | --- | --- | --- |
| Claro | `bg-light` / `bg-soft` | `on-light` | Explicação, produto, cases. Base da maioria das cenas |
| Impacto | `bg-impact` | `on-dark` | Gancho forte, número grande, oferta, fechamento |
| Profundo | `bg-deep` (+ 1 forma 3D) | `on-dark` | Acento raro: lançamento, abertura especial |

Alternar claro ↔ impacto entre cenas dá ritmo. Profundo no máximo uma cena por vídeo, e só quando pedido.

## Frame 9:16

- Texto, números e logo entre **y=270 e y=1250** (Reels) ou **y=270 e y=1540** (Stories), 72px nas laterais.
  Use `.content`, que já respeita isso.
- Uma ideia por cena. Título ≤ 8 palavras, em dois tons quando couber.
- Um destaque por cena: número **ou** celular **ou** marca-texto.
- Logo pequeno a partir da 2ª cena; logo grande só no fechamento.

## Feed 4:5 e quadrado

Mesmos átomos, tipografia ~15% menor, 64px de margem.

## Composição

- **Gancho (0–2s):** legível no frame 0 (é a thumbnail). Frase de `voz.md` + um elemento visual.
- **Prova:** número de `claims.md` em `stat` com count-up, sempre com o nome do case e, quando for case,
  a ressalva em `note`.
- **Produto:** mockups reais (`assets/brand/site-assets/*-mockup.png`) e cards `push` com nome de loja
  cliente (LOUM, ONUH…), nunca o símbolo da Korza como app da loja.
- **Fechamento (2,5–3s finais):** logo + promessa + `cta` ("Veja seu app grátis").

## Motion

- Entrada de texto: sobe 24–40px + fade, `power3.out`, 0,5–0,7s; stagger 0,06–0,1s por linha.
- Marca-texto: `.hl-bg` scaleX 0→1 logo depois da palavra entrar.
- Números: count-up ~1s, `power2.out`.
- Cards de push: entram de cima, com leve escala (0,96→1) e sombra.
- Transições: wipe azul ou corte seco no beat. Nada de transição "de PowerPoint".
- Movimento calmo e preciso. Premium = controle, não excesso.

## Vídeo gravado

- Legendas: `.caption`, palavra ativa em azul claro, 2–5 palavras por grupo, dentro da zona segura.
- Lower third: `.lower-third` para nome/cargo.
- Abertura e fechamento: cena da marca (impacto) antes/depois da filmagem; CTA no fim.
- Não tratar a imagem com filtros improvisados: use o `/media-use` do HyperFrames.

## Não fazer

- Verde, roxo, neon, gradientes multicoloridos, sombras pesadas.
- Outra fonte, peso 700+, CAIXA ALTA em título.
- Logo/UI de terceiros como protagonista; inventar número, cliente ou tela de app.
