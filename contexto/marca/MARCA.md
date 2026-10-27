# Marca Korza — sistema visual

Vale para tudo: site, posts, carrosséis, reels, stories, ads, thumbnails, OG. Tokens em [tokens.css](tokens.css).
Prévia visual em [preview.html](preview.html). Tom de voz em [../voz.md](../voz.md).

Base: o site ao vivo (korza.app, antes korza.com.br, out/2026), que já é a direção escolhida. A apresentação de identidade
visual (`reference/idv/`, fundos escuros e 3D cromado) virou acento raro, não padrão.

## A ideia

**Premium pelo capricho, simples pelo respiro.** A Korza quer parecer o melhor produto do mercado e o mais
fácil de usar, a um preço acessível. Premium aqui não é fundo escuro nem efeito: é tipografia precisa,
muito espaço em branco, poucas coisas por peça, produto real e movimento bem feito.

Três modos, nesta ordem de frequência:

| Modo | Fundo | Quando | Frequência |
| --- | --- | --- | --- |
| **Claro** (base) | Branco ou `ice` | Explicação, produto, cases, carrosséis, maioria das peças | ~70% |
| **Impacto** | Azul em gradiente (`--k-gradient-impact`) | Gancho, número grande, oferta, fechamento com CTA | ~25% |
| **Profundo** (acento) | Navy, eventualmente com 3D cromado | Peça especial, lançamento, abertura de vídeo | raro |

Uma peça pode alternar claro → impacto (ex.: carrossel com capa azul e miolo claro, reels que fecha no azul).

## Cores

| Token | Hex | Uso |
| --- | --- | --- |
| `blue` | `#155DFC` | A cor da marca. Destaques, CTA, palavra-chave do título, modo impacto |
| `blue-hover` | `#104BD0` | Estado hover/pressionado |
| `blue-deep` | `#0B3CAE` | Fim do gradiente de impacto |
| `navy` | `#10213B` | Títulos e texto forte sobre claro; fundo do modo profundo |
| `slate` | `#42556C` | Texto de corpo sobre claro |
| `gray` | `#7D8DA1` | Segunda parte do título em dois tons; legendas |
| `muted` | `#708096` | Notas, rodapés, ressalvas |
| `line` | `#E5EBF2` | Bordas de cards e divisórias |
| `ice` | `#F5F8FC` | Fundo claro alternativo, cards |
| `white` | `#FFFFFF` | Fundo base; texto sobre azul/navy |

Gradiente de impacto: `linear-gradient(145deg, #236CFB 0%, #155DFC 40%, #0739B0 100%)`.

Navy único: `#10213B` (o `#0B348C` da IDV antiga está aposentado).

Contraste: texto sobre claro = `navy`/`slate`; sobre azul/navy = `white`. Nunca azul sobre navy, nunca
`gray`/`muted` sobre azul.

## Tipografia

Uma família só: **Plus Jakarta Sans** (`fonts/`, variável). Pesos **400** (corpo) e **600** (títulos,
números, botões). Nada de 700+ pesado, nada de outra fonte.

- **Títulos apertados:** tracking negativo forte (`-0.045em` em display, `-0.035em` em títulos), entrelinha 1.05–1.15.
- **Título em dois tons** (assinatura do site): a 1ª parte em `navy`, a 2ª em `blue` ou `gray`.
  Ex.: "Sua marca / **no bolso do seu cliente.**" · "Seu app, em tempo real. / **Você por dentro de tudo.**"
- **Eyebrow:** rótulo pequeno em `blue`, peso 600, acima do título ("Push notifications", "Case Loum").
- Sentence case sempre. Títulos podem terminar com ponto final, como no site.

Escala de referência (px, para 1080 de largura):

| Estilo | Peso | Tamanho | Uso |
| --- | --- | --- | --- |
| display | 600 | 104–128 | Gancho, capa |
| title | 600 | 64–84 | Título de slide/cena |
| stat | 600 | 160–240 | Número grande |
| body | 400 | 34–40 | Texto de apoio |
| eyebrow | 600 | 26–30 | Rótulo acima do título |
| note | 400 | 22–24 | Ressalva, fonte do case |

## Elementos

- **Logo** (`logo/`, `site-assets/korza-logo.png`): símbolo azul + KORZA em navy sobre claro;
  `korza-logo-white.png` sobre azul/navy. Pequeno (~180–220px) num canto; grande só no fechamento.
  Nunca distorcer, recolorir, pôr sombra ou contorno. Ícone de app/avatar: `site-assets/favicon.svg`.
- **Botão / CTA:** fundo `blue`, texto branco 600, seta →. Sobre azul: fundo branco, texto `blue`.
  Cantos discretos (8–14px em peças sociais, 5px no site). Um CTA por peça.
- **Card:** fundo branco ou `ice`, borda 1px `line`, cantos 16–24px, sombra quase invisível.
- **Produto real:** mockups de celular com apps de clientes (`site-assets/*-mockup.png`), cards de push
  e de métrica no estilo do site. Nunca inventar tela de app de cliente.
  Em card de push, o ícone é da loja (cliente real, ex.: LOUM, ONUH), nunca o símbolo da Korza.
- **Prova social:** mosaico de logos de clientes (`site-assets/client-logos.png`).
- **Fita azul:** curva larga em gradiente azul entrando pela borda (hero do site). Grafismo opcional, um por peça.
- **3D cromado** (`graphics/3d/`): só no modo profundo, e no máximo um elemento.
- **Ícones:** traço fino (1.5–2px), arredondados, em `blue` ou `navy`.

## Formatos

| Formato | Tamanho | Área segura |
| --- | --- | --- |
| Post feed / ad feed | 1080×1350 (4:5) | 64px nas bordas |
| Carrossel | 1080×1350 por slide | 64px nas bordas; capa precisa funcionar sozinha |
| Quadrado | 1080×1080 | 64px |
| Reels / ad reels | 1080×1920 | Texto entre y=270 e y=1250, 72px nas laterais (UI do Instagram cobre o resto) |
| Stories | 1080×1920 | Texto entre y=250 e y=1540, 72px nas laterais |
| OG / link | 1200×630 | 60px |

Specs de vídeo (motion e gravados) vão para `studio/` quando a Fase 1 começar, herdando este arquivo.

## Faça / não faça

- ✅ Uma ideia por peça. Muito respiro. Produto real.
- ✅ Um número sempre que possível, de [../claims.md](../claims.md).
- ✅ Título em dois tons; palavra-chave em azul.
- ❌ Verde, roxo, neon, gradientes multicoloridos, sombras pesadas, bordas grossas.
- ❌ Outras fontes. Peso 800 "gritando". CAIXA ALTA em título.
- ❌ Logo "businesstree" e o verde dos slides da IDV (são da agência que fez a identidade).
- ❌ Logos/UI de terceiros como protagonista (Shopify e Nuvemshop só como "conectado a").

## Arquivos

```
MARCA.md          este arquivo
tokens.css        variáveis + componentes base (importar nas peças HTML)
preview.html      prévia visual do sistema
logo/             logos PNG (color, color-on-dark, white, dark, símbolo)
fonts/            Plus Jakarta Sans variável (OFL)
site-assets/      logo, favicon, mockups de apps e mosaico de clientes do site ao vivo (2026-10-26)
cases/            prints de apps de clientes (versão antiga)
graphics/         3D cromado e textura (modo profundo)
reference/        slides da IDV e da apresentação comercial
source/           PDFs originais
```
