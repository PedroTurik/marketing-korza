# M2 — "Do zero × Korza" (storyboard)

Demanda: `demandas/2026-11-05-motion-m2-do-zero.md`. Pilar: conversão (derrubar "app é caro e demora"). Fala com o dono.
Quadros-chave aprovados pelo Pedro em 2026-11-05: `storyboard/quadros-chave.jpg` (e `storyboard/qNN.jpg`). Poses estáticas da fase de storyboard.

## Direção visual

**Dois mundos, uma virada.**

- **Ato 1, "Do zero" (0–8s, ~30% do tempo).** Modo profundo (navy com grade fina), **monocromático**: o azul da marca fica
  guardado para a Korza. A ideia é o **acúmulo**: cada fala joga uma camada de papel em cima da anterior (orçamento →
  calendário → contas de desenvolvedor → status de aprovação) e a pilha fica pesada e confusa. Cortes secos no título a
  cada batida, câmera recuando conforme a pilha cresce, tremor leve no fim. Termina com a pilha caindo e uma cortina branca
  subindo.
- **Ato 2, "Korza" (8–25,4s, ~70%).** Claro, arejado, azul. **Um celular só, em perspectiva**, com o onboarding real
  recriado em HTML (fiel aos prints; loja genérica "Sua Loja", sem dado de conta de teste). A câmera acompanha cada passo e
  um toque (dedo) aciona a tela: plataforma → logo → cor (a barra de navegação muda de cor ao vivo) → push de teste chega.
  Depois, apps reais de clientes em leque 3D (Hiven, Loum, Belletonn, Pé de Algodão), o prazo como resposta direta ao
  calendário riscado do ato 1 (14 quadradinhos enchendo de azul) e o CTA no modo impacto.
- **Tipografia cinética:** títulos grandes (96–112px) trocam a cada fala, com entrada por máscara; números grandes
  fixos com escala (sem contagem nem odômetro: nenhum valor fora dos claims pode passar pela tela).
- **Ritmo:** corte ou movimento novo a cada 1–1,5s (M1 tinha cenas de 4–8s paradas).

## Mapa de tempo (final, travado na voz; voz entra em 0,15s)

| Tempo | Cena | Quadro | Na tela | Voz | Claim |
| --- | --- | --- | --- | --- | --- |
| 0–3,63 | `s1-do-zero` | 1 | "Um app do zero pode custar **até R$ 100 mil**" (legível no frame 0). O "100" (fixo desde o frame 0) infla a cada item e dá um soco no "cem mil"; itens do orçamento entram um a um (sem valores) | "Um app do zero pode custar até cem mil reais." | `app-sob-medida-100k` |
| 3,63–5,48 | `s1-do-zero` | 2 | "Meses de projeto." Calendário cai por cima; meses viram, dias riscados | "Meses de projeto." | — (sem número) |
| 5,48–7,27 | `s1-do-zero` | 3 | "Conta na Apple e no Google." Dois formulários batem tortos na pilha | "Conta na Apple e no Google." | — |
| 7,27–9,15 | `s1-do-zero` | 4 | "Aprovação nas lojas." Status chovem; pilha treme e cai; cortina branca | "Aprovação nas lojas." | — |
| 9,15–10,0 | `s2-korza` | 5 | Logo Korza no branco; o celular sobe em perspectiva | "Na Korza," | — |
| 10,0–11,3 | `s2-korza` | 6 | "Conecte sua loja." Toque em Nuvemshop (Shopify ao lado), Continuar | "você conecta sua loja," | `plataformas` |
| 11,3–12,1 | `s2-korza` | 7 | "Escolha a logo." Ícone cai no lugar; preview na tela inicial | "escolhe logo" | — |
| 12,1–13,0 | `s2-korza` | 8 | "E as cores." Toque no laranja; a barra de navegação muda de cor | "e cores…" | — |
| 13,0–13,85 | `s2-korza` | 9 | "E pronto." Push de teste da "Sua Loja" chega (som); passo vira ✓ | "e pronto." | — |
| 13,85–17,55 | `s3-apps` | 10 | "A gente constrói e publica." Hiven sobe, Loum, Belletonn e Pé de Algodão abrem em leque 3D; selos com os logos da App Store (iOS) e do Google Play (Android) | "A gente constrói e publica seu app, iOS e Android," | `app-nativo` |
| 17,55–19,85 | `s4-prazo` | 11 | "Seu app no ar em até **14** dias úteis." "14" entra crescendo e 14 dias úteis enchem de azul | "em até quatorze dias úteis!" | `prazo-14-dias` |
| 19,85–23,05 | `s5-cta` | 13 | Wipe azul. "~~Do zero, até R$ 100 mil.~~" → "Seu app pronto, sem complicação." + botão | "Crie sua conta grátis na Korza." | — |
| 23,05–25,25 | `vinheta` | 14 | Logo grande + CTA (mesma posição) | — | — |

Tempo de tela: "do zero" 9,15s, Korza 16,1s. Legenda (pílula) de 0 a 19,85s em y=1480 (9:16) / 1196 (4:5); sai no CTA.

**v2 (pedido do Pedro após o v1):** legenda mais baixa, sem "Sem conta de desenvolvedor" (voz cortada, sem regerar;
trilha perde um compasso), logos da App Store e do Google Play nos selos iOS/Android.

## Variação "busca" (2026-11-06)

Demanda: `demandas/2026-11-06-motion-m2-gancho-busca.md`. Mesmo vídeo com um gancho novo de 3,2s na frente; o `-v2` segue
igual e renderizável. Total 28,45s. Tudo em `assets/audio/busca/`.

| Tempo | Cena | Na tela | Voz |
| --- | --- | --- | --- |
| 0–3,08 | `s0-busca` | Modo profundo do ato 1. Barra de busca genérica (lupa, sem marca de buscador) com "Como criar um app" já digitado no frame 0; o resto é digitado à frente da voz, com cursor e clique de tecla. Legenda em pílula com a pergunta | "[curious] Como criar um app do meu e-commerce Shopify ou Nuvemshop?" |
| 3,08–3,65 | `s0-busca` → `s1-do-zero` | Enter: a barra afunda, linha de carregamento corre, a busca sobe e sai (whoosh) e o fundo some, revelando a "resposta": o título "até R$ 100 mil" e o orçamento do ato 1 | — |
| 3,2–28,45 | M2 `-v2` | Idêntico, deslocado 3,2s (96 quadros exatos) | Voz do M2 sem regerar |

- **Montagem:** `variante.py` gera o `index.html` da variante a partir do `index.html` do M2 (desloca as cenas, entra
  `s0-busca` por cima do ato 1 e `legenda-busca`). `bash build.sh check|snap|render --gancho busca`.
- **Voz:** pergunta gerada com a Bea nas configurações do M2 (`gerar_voz.py`, 3 takes; ficou o mais limpo na transcrição),
  -1 dB para casar com o começo do `vo.mp3`. Pausa de ~0,35s antes de "Um app do zero".
- **Trilha:** a mesma faixa, sem regerar. Abre com 1,5 compasso do 1º compasso (112 BPM; meio compasso + compasso
  inteiro, mesmo nível de tensão do início) e emenda no ponto do grid em que a faixa do M2 começa.
- **Áudio:** `mix.sh` desta pasta = o `../mix.sh` deslocado (mesmos efeitos, ducking, automação e -14 LUFS / -1 dBTP) +
  `teclas.wav` (gerado por `gerar.py` nos mesmos tempos das letras). Depois do gancho, correlação 1,000 com o `mix.wav`
  do M2 e -0,07 dB de diferença.
- **Gerar de novo:** `python3 assets/audio/busca/gerar.py` (cena, legenda e teclas) → `bash assets/audio/busca/mix.sh`.

## Voz (Bea, padrão M1)

> [confident] Um app do zero pode custar até cem mil reais. Meses de projeto. Conta na Apple e no Google. Aprovação nas
> lojas. [warm] Na Korza, você conecta sua loja, escolhe logo e cores… e pronto. A gente constrói e publica seu app, iOS e
> Android, em até quatorze dias úteis! Crie sua conta grátis na Korza.

## Som

Trilha Eleven Music instrumental (prompt em `assets/audio/trilha-prompt.json`, 3 seções): tensa no ato 1, abre na
virada (9,15s) para algo leve e confiante. Efeitos: baque seco a cada camada da pilha, toque suave nos taps, sino de notificação (kit) no push de
teste, tick no "14".

## O que mudou em relação à demanda

- **Uma versão só** (gancho A), por decisão do Pedro: 2 renders (9:16 e 4:5), não 4.
- Voz: a abertura usa o gancho A ("Um app do zero pode custar até cem mil reais") no lugar de "Fazer do zero: até R$ 100
  mil", para não repetir. O "do zero" vira frases curtas, uma por camada.
- Entra "iOS e Android" (`app-nativo`). "Sem conta de desenvolvedor" (`sem-conta-dev`) entrou no v1 e saiu no v2.
- CTA na tela igual ao M1 ("Crie sua conta e veja seu app grátis →"); a voz diz "Crie sua conta grátis na Korza".
- Loja do onboarding: "Sua Loja" genérica, com sacola no ícone (decisão do Pedro).
- Modo profundo por 8s no ato 1 (o `frame.md` pede no máximo uma cena e só quando pedido): é o contraste que faz a peça.

Reproduzir: `bash assets/audio/mix.sh` (áudio) · `python3 assets/audio/legenda.py` (legenda) · `bash build.sh check|snap|render`.
