# M3, "O painel" (storyboard)

Demanda: `demandas/2026-11-05-motion-m3-painel.md`. Pilar: recompra. Fala com o gestor de e-commerce.
Quadros-chave: `storyboard/quadros-chave.jpg` (e `storyboard/qNN.jpg`): poses estáticas da fase de storyboard; na prancha ainda aparece o gancho B, que saiu depois.

**Status:** storyboard aprovado pelo Pedro em 2026-11-05 e animado. Versão única: gancho A, 2 renders (decisão do Pedro no OK do storyboard).

**v2 (2026-11-06, `demandas/2026-11-06-motion-m3-gancho-novo.md`):** gancho novo, "Isso é o que você ganha quando lança o app da sua loja com a Korza.",
na voz, no título e na legenda. Mesma animação de abertura, só retimada: a pilha abre por 2,85s (v1: 1,85s), e o colapso, o mergulho e todo o
resto andam 1,0s (`D` no fim de `compositions/src/mundo.js`). Total de 27,8s. O mapa abaixo é o do v2; os renders `-v1` seguem em `renders/`.

## Direção visual

**Um painel só, filmado em plano-sequência.** As cinco telas formam um único mural no espaço, e a câmera voa de uma área para
a outra sem corte. O ritmo vem do movimento, não de wipes: a cada 1–2s a câmera muda de pose ou uma peça se solta do plano.

- **Abertura (azul):** as telas empilhadas em perspectiva sobre o azul de impacto. Em "num painel só", a pilha colapsa num plano.
  A câmera mergulha nele, o azul sai, e estamos dentro do painel.
- **Miolo (`ice` com luz azul):** telas reais em perspectiva, fundo com as linhas onduladas do próprio Studio do painel e
  profundidade de campo. Celulares e peças flutuam acima do plano com sombra longa.
- **A prova:** o card real "Composição dos pedidos" se solta do Analytics, e o donut preenche exatamente 1/3.
- **Fechamento (azul) sem wipe:** o arco azul do donut cresce até tomar o quadro, e o card continua na cena. Mesmo botão e mesma
  posição da vinheta, com o logo entrando no "Korza" falado.
- **Tipografia:** eyebrow com o nome da área do menu e progresso em 4 traços, mais o título em dois tons, sempre em resultado.
  Entrada por máscara, com troca no mesmo lugar para não pular.
- **Assinatura do filme:** a sequência causa e efeito fica contínua. O clique em BAIXAR lança o ícone do app para a cena de
  boas-vindas, onde ele vira a instalação ("Instalou 9:41 → Chega 9:46").

## Mapa de tempo (v2, travado na voz; voz entra em 0,15s)

| Tempo | Quadro | Câmera / movimento | Título na tela | Voz | Claim |
| --- | --- | --- | --- | --- | --- |
| 0–3,0 | 1 | Pilha em perspectiva, abrindo devagar; camadas respiram (2,85s) | "Isso é o que você ganha quando lança o app da sua loja com a Korza." | gancho | — |
| 3,0–4,3 | 2 | Pilha colapsa em "com a Korza" e a câmera mergulha; o azul sai | idem | "…com a Korza." | — |
| 4,3–5,45 | 3 | Câmera próxima no Título; digitação caractere a caractere com contador, depois Mensagem | "Sua oferta, na hora certa." | "Escreva o push," | — |
| 5,45–6,3 | 4 | Desliza até "Ao tocar"; cursor clica em Página inicial | idem | "escolha o destino" | — |
| 6,3–6,75 | 5 | Desliza até "Quando enviar"; clique em Amanhã | idem | "e agende." | — |
| 6,75–7,2 | 6 | Câmera vira para o celular; o push se solta e vem à frente, com som | idem | (fim da frase) | — |
| 7,2–9,25 | 7 | Voo até App; banner desce no celular; COPIAR; o cupom BEMVINDO se solta | "Do site para o app." | "Cupom para a primeira compra no app." | — |
| 9,25–11,4 | 8 | Voo até o site; banner entra; clique em BAIXAR; ícone do app parte para baixo | idem | "Banner no site para baixar o app." | — |
| 11,4–13,9 | 9 | Câmera desce; ícone pousa; 9:41 → 9:46 com a seta desenhando; push de boas-vindas chega | "Quem instala é recebido." | "Boas-vindas automáticas para quem instala." | — |
| 13,9–15,2 | 10 | Voo aberto sobre o Analytics; gráficos desenham em sequência | "Você vê o que o app vende." | "Vendas do app e do site," | — |
| 15,2–16,7 | 11 | Mergulho no gráfico; rótulos App e Site entram nas linhas | idem | "lado a lado." | — |
| 16,7–20,97 | 12 | Card sai do plano, fundo desfoca; donut preenche 1/3 no "três" | "1 em cada 3 pedidos no app vem de quem já tinha comprado" | "E um em cada três pedidos no app vem de quem já tinha comprado." | `recompra-1-em-3` |
| 20,97–24,27 | 13 | Arco do donut cresce até virar o fundo azul; card fica em cena | "Transforme a sua recompra e fidelize seu cliente." | idem | — |
| 24,27–25,6 | 14 | Botão entra (legenda sai) | idem + "Crie sua conta e veja seu app grátis →" | "Crie sua conta grátis na Korza." | — |
| 25,6–27,8 | 15 | Logo grande no "Korza"; botão não pula | logo + CTA | — | — |

Duração total: **27,8s** (v1: 26,8s). CTA na tela por 3,6s. Legenda (pílula) de 0 a 24,2s em y=1480 (9:16) e y=1196 (4:5).
`push-ilimitado` entra como selo na cena do push (6,96s), sem voz (decisão do Pedro).

## Voz (Bea, padrão M1)

> [confident] Isso é o que você ganha quando lança o app da sua loja com a Korza. Escreva o push, escolha o destino e agende. Cupom para a primeira
> compra no app. Banner no site para baixar o app. Boas-vindas automáticas para quem instala. Vendas do app e do site, lado a
> lado. E um em cada três pedidos no app vem de quem já tinha comprado. [warm] Transforme a sua recompra e fidelize seu cliente.
> Crie sua conta grátis na Korza.

**v2:** só o gancho foi gerado (3 takes, `vo-v2-gancho-{1,2,3}.mp3`, mesma configuração; usado o take 2, mais próximo do v1 em volume, tom e ritmo:
-16,2 LUFS e F0 222 Hz contra -16,1 LUFS e 219 Hz). `assets/audio/gancho_v2.py` emenda o gancho no corpo do `vo-a-ed.wav` sem regerar, com 0,35s de
respiro, para o corpo andar exatamente 1,0s (2 tempos a 120 BPM). Na emenda: gancho -16,3 LUFS, frase seguinte -16,4 LUFS.

O gancho B foi gerado (`vo-b-gancho.mp3`), mas saiu da peça; a voz fica no projeto caso o teste volte. Silêncios encurtados sem regerar
(`assets/audio/editar_voz.py`): 27,2s viraram 25,1s.

## Som

Eleven Music, instrumental, eletrônica precisa, ~120 BPM (decisão do Pedro), com acentos nos voos e abertura no fechamento.
Prompt em `assets/audio/trilha-prompt.json`. Efeitos do kit: toque nos cliques, `whoosh` nos voos, sino no push, baque leve no
card. Mix em -14 LUFS / -1 dBTP, ducking pela voz. **v2:** a trilha ganha 2 tempos no começo (repete o pulso da abertura) e todo efeito
e automação a partir do colapso anda 1,0s (`D` no `mix.sh`); o clímax cai em 20,97s ("Transforme"). O mix do v1 fica em `assets/audio/mix-v1.wav`.

## Telas

Extraídas do **admin real rodando numa cópia, com os mocks do e2e** (`assets/telas/extrair.spec.ts.txt`), em HTML vetorial com
estilos computados: mesmo layout, fonte e cores, nítido em qualquer zoom. Nenhum dado real de cliente entra. Sem Públicos, sem
carrinho abandonado, sem domínio ou nome de teste. Loja genérica "Sua Loja", com ícone de sacola (padrão M2).
Banner do site: o editor mostra um exemplo fixo no iframe, então o banner é recriado com o texto de exemplo do próprio painel.
Registry do HyperFrames: consultei `filmed-screen`, `ui-3d-reveal` e `cursor-zoom-follow`, mas a câmera e o cursor ficam à mão,
porque precisam atravessar o mural inteiro numa timeline só.

## O que mudou em relação à demanda

- **Cena 2 dividida:** "Banner de cupom para o cliente baixar o app" estava incorreto (o cupom fica dentro do app; quem leva a
  baixar é o banner do site). Agora são duas frases e duas telas, por decisão do Pedro.
- **Prova falada:** a demanda só pedia o card na tela. Decisão do Pedro.
- **Títulos como resultado** ("Sua oferta, na hora certa." etc.), e a voz fica com a ação. Decisão do Pedro.
- **Uma versão só** (gancho A): 2 renders, não 4. Decisão do Pedro.
- **Selo "Push ilimitado"** na cena do push. Decisão do Pedro.
- **Duração 26,8s** (pedido: cerca de 25s, limite 20–30s), por causa da prova falada.
- **Números de interface:** horários de UI seguem legíveis ("Amanhã, 10:00", 9:41, "Instalou 9:41 → Chega 9:46"). Todo número de
  resultado fica borrado, e o único legível é `recompra-1-em-3`.
- **Boas-vindas:** além da notificação no celular, um push grande igual ao da campanha, para ler no celular de quem assiste.
- **Card da prova:** sem valores, descrições e selo "Beta"; o donut mostra 1/3 em vez do número de exemplo.

## Trilha e render

Trilha reconstruída no grid (120 BPM exatos) sem regerar: a seção forte veio em 16s e morria em 24s; com 2 compassos a mais e 2 tempos a
menos, o clímax caía em 19,97s no v1 ("Transforme"; 20,97s no v2) e o acorde final na vinheta (detalhes em `assets/audio/mix.sh`). Motion blur real: filme 4x mais
lento a 240 fps (960 amostras por segundo), 16 amostras fundidas em cada quadro de 30 fps, obturador de 1/60s (`build.sh`, `assets/telas/lento.py`).

Reproduzir: `python3 assets/telas/montar.py` (cena) · `bash assets/audio/mix.sh` (áudio) · `python3 assets/audio/legenda.py` (legenda) ·
`bash build.sh check|snap|render`.
