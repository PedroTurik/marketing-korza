# M1 v2 — "A notificação" (storyboard)

Demanda: `demandas/2026-11-06-motion-m1-revamp.md` (revamp visual do v1). Pilar: canal próprio. Fala com o dono.
Quadros-chave: `storyboard/quadros-chave.jpg` (e `storyboard/qNN.jpg`): poses estáticas da fase de storyboard, geradas por
`storyboard/quadros.py` com o mesmo CSS da animação (`assets/v2/m1v2.css`).

**Status:** storyboard aprovado pelo Pedro em 2026-11-06, com um ajuste: logos da Nuvemshop e da Shopify nos cartões do tópico 1.
Animado e renderizado: `renders/m1-notificacao-a-9x16-v2.mp4` e `renders/m1-notificacao-a-4x5-v2.mp4`.

Copy, voz e claims iguais ao v1. Voz `assets/audio/vo.mp3` (Bea), sem regerar, entrando em 1,0s. Só o gancho A ("Amor").
Duração 22,5s, como o v1.

## Direção visual

**Um celular de verdade e a câmera reagindo a ele.** O v1 era um celular chapado e uma lista. O v2 é filmado: um celular com
volume (espessura em camadas 3D, aro metálico, reflexo correndo no vidro, luz da tela no ambiente) e uma câmera que se mexe a
cada fala.

- **Gancho, no escuro (0–2,9s, modo profundo).** Quarto à noite: o celular inclinado brilha no navy e ilumina o entorno. A
  notificação "Amor ❤ / Precisamos conversar..." bate de cima com o sino, e a câmera dá um tranco (camera shake do registry
  do HyperFrames, perfil handheld leve). Legível em 0,4s. Depois a câmera chega perto, o reflexo corre no vidro e, no "né?",
  um traço azul sublinha "Precisamos conversar..." como quem acabou de ler.
- **A virada, causa e efeito sem corte (2,9–4,6s).** É o mesmo cartão: em "Seu cliente", remetente e texto rolam para
  "Sua Loja / Novidade pra você. Vem ver.", o balão vira a sacola da loja e o papel de parede passa de noite para o azul da
  marca. O fundo clareia de navy para claro e, em "também lê", a câmera recua de uma vez: o celular é um entre vários, e cada
  um acende com o mesmo push, em cascata (sinos curtos).
- **Miolo claro (4,6–17s).** Fundo `ice` com luz azul, como o M3. Títulos em dois tons, entrada por máscara, trocando no
  mesmo lugar. Um celular herói em perspectiva atravessa as cenas, sempre em movimento, e as transições são de câmera
  (chicote com motion blur e mergulho), não wipes.
- **Os 3 tópicos viram cenas**, cada uma com eyebrow e progresso em 3 traços (padrão M3):
  1. **Plataformas:** os cartões grandes trazem os logos da Nuvemshop e da Shopify (pedido do Pedro no OK; arquivos oficiais
     do site, `assets/v2/logo-*`), e uma linha pontilhada liga os dois à loja no celular.
  2. **Prazo:** "14" gigante entra crescendo e uma régua de 14 dias úteis enche de azul; no fim, o selo "App no ar" carimba
     abaixo da régua. Sem contagem: nenhum número além do 14 passa pela tela.
  3. **Push:** pushes da loja chovem sobre o celular, cada vez mais rápido, e viram um túnel infinito em perspectiva em
     "ilimitadas".
- **Fechamento no nível do M3 (17–22,5s).** O primeiro push do túnel voa contra a câmera e o branco dele vira o azul de
  impacto, sem wipe. "Sua loja na tela / do seu cliente." com o celular aceso em perspectiva no meio e o botão na posição da
  vinheta. A vinheta do kit entra com o logo; o botão não pula.

## Mapa de tempo (travado na voz; voz entra em 1,0s)

| Tempo | Quadro | Câmera / movimento | Na tela | Voz | Claim |
| --- | --- | --- | --- | --- | --- |
| 0–0,45 | 01 | Notificação bate de cima, tranco de câmera, luz da tela acende o quarto | Celular, 21:47, "Amor ❤ / Precisamos conversar..." | (sino) | — |
| 0,45–1,26 | 01→02 | Câmera avança devagar; celular gira para frente | idem | — | — |
| 1,26–2,49 | 02 | Push-in contínuo; reflexo corre no vidro | idem | "Você leu essa notificação," | — |
| 2,49–2,92 | 03 | Close extremo, micro-tranco; traço azul sublinha a mensagem | idem | "né?" | — |
| 2,92–3,78 | 04 | Remetente e texto rolam para a loja; papel de parede e fundo clareiam | "Seu cliente" | "Seu cliente" | — |
| 3,78–4,62 | 05 | Recuo rápido: campo de celulares acendendo em cascata | "Seu cliente / também lê." | "também lê." | — |
| 4,62–5,84 | 06 | Chicote (motion blur) para um celular herói no claro; logo entra | "Com a Korza," | "Com a Korza," | — |
| 5,84–7,3 | 07 | Celular gira para frente; tela inicial; ícone da loja cai na grade e brilha em "app" | "Sua loja ganha / um app próprio." | "sua loja ganha um app próprio" | — |
| 7,3–8,95 | 08 | Push da loja desce na tela e salta para fora, rumo à câmera | "E fala direto / na tela dele." | "e fala direto na tela dele." | — |
| 8,95–10,6 | 09 | Mergulho para o tópico 1; "Nuvemshop" bate como cartão | "Para lojas" + cartão | "Para lojas Nuvemshop" | `plataformas` |
| 10,6–11,6 | 10 | "Shopify" se encaixa; linha liga os dois à loja no celular | "Para lojas / Nuvemshop e Shopify." | "e Shopify." | `plataformas` |
| 11,6–13,9 | 11 | "14" cresce no "quatorze"; régua de dias úteis enche | "App no ar em até / 14 dias úteis." | "App no ar em até quatorze dias úteis." | `prazo-14-dias` |
| 13,9–14,42 | 12 | Régua completa; selo "App no ar" carimba | idem | — | `prazo-14-dias` |
| 14,45–15,9 | 13 | Pushes chovem e empilham, acelerando | "Notificações push" | "Notificações push" | `push-ilimitado` |
| 15,9–17,0 | 14 | Pilha vira túnel infinito; câmera atravessa | "Push / ilimitado." | "ilimitadas." | `push-ilimitado` |
| 17,0–20,3 | 15 | Push voa na câmera e vira o azul; celular aceso em perspectiva; botão entra em 17,6 | "Sua loja na tela / do seu cliente." + botão | "Crie sua conta e veja seu app grátis." | — |
| 20,3–22,5 | 16 | Vinheta do kit: logo grande, botão parado | logo + botão | — | — |

Ritmo: o maior intervalo sem corte nem movimento novo é ~1,2s. CTA na tela de 17,6s a 22,5s (4,9s).
Legenda: pílula padrão em y=1480 (9:16) e y=1196 (4:5), de 1,2s até 17s, gerada de `vo-words.json` por `legenda.py`; sai no
CTA (o botão faz o papel). Na tela, "14" em algarismo.

## Som

- **Trilha nova, Eleven Music, instrumental, ~120 BPM** (cortes caem na batida), prompt em `assets/audio/trilha-prompt.json`:
  1. 0–2,9s, noite: pulso grave e íntimo, poucas notas, tensão leve.
  2. 2,9–4,6s, virada: riser curto que abre no "Com a Korza".
  3. 4,6–17s, claro: groove leve e confiante, plucks brilhantes, acentos nos chicotes.
  4. 17–22,5s, fechamento: sobe um degrau e termina num acorde resolvido na vinheta.
- **Efeitos do kit** (sem som da Apple): sino na notificação (0,05s), sinos curtos em cascata no campo de celulares, `whoosh`
  nos chicotes e mergulhos, `tick` na entrada de cada tópico e no "14", `baque` leve nos cartões.
- Mix padrão: trilha ~0,30 com ducking pela voz, -14 LUFS / -1 dBTP.

## Formatos

9:16 (1080×1920) e 4:5 (1080×1350), pelo `build.sh` (2 variantes, só gancho A). No 4:5, o palco 3D sobe e encolhe ~15% e os
títulos ficam em 84px.

## O que mudou do storyboard para a animação

- Logos da Nuvemshop e da Shopify nos cartões (pedido do Pedro).
- Quadro 12: o selo "App no ar" carimba sob a régua, sem o celular subindo. A janela (0,5s antes do corte) era curta demais
  para trazer o celular sem atropelar.
- Trilha sem regerar: a Eleven Music entregou intro até 8s e groove até 18s. O `mix.sh` lê a faixa a partir de 3,38s (o
  groove cai no "Com a Korza") e repete 3 compassos, no grid de 120 BPM, para o groove ir até a vinheta.
- Tempos das frases corrigidos por `silencedetect` (o alinhamento da ElevenLabs errava até 0,3s): "Com" em 4,84s,
  "Para" em 9,12s, "App" em 11,71s, "Notificações" em 14,47s. A legenda usa esses tempos (`legenda.py`, `FIX`).
- O check avisa que três títulos ficam menos de 1s na tela ("um app próprio.", "na tela dele.", "Nuvemshop e Shopify."):
  eles repetem a fala e a pílula da legenda, no ritmo do M2/M3.

## Construção

- `assets/v2/m1v2.css`: celular com volume (`.ph3`, 20 camadas de espessura criadas por `m1Edges`), notificação, push
  grande, títulos. `assets/v2/m1v2.js`: helpers (`m1Edges`, `m1In`/`m1Out` dos títulos, `m1Jolt` do tranco).
- `assets/v2/camera-shake.js`: componente `camera-shake` do registry do HyperFrames (só o helper), perfil handheld leve no
  gancho. Também consultei `parallax-device-dive`, `notification-cascade` e `shimmer-sweep`; a câmera, a chuva de pushes e o
  reflexo ficaram à mão porque precisam seguir o tempo da voz.
- 4:5: tudo que não é título mora num `.stg` (1080×1920), que no 4:5 sobe 210px e encolhe para 0,78 (`index.html`).
- Sem motion blur por quadro (o M3 usa): os chicotes já têm borrão em CSS.

## O que muda em relação ao v1

- Celular com volume e luz, câmera viva, troca da notificação pessoal pela da loja no mesmo cartão.
- Gancho em modo profundo (o `frame.md` pede profundo como acento raro: aqui é uma cena só, de 2,9s, e é o que faz a
  notificação brilhar).
- Os 3 tópicos são três cenas. Títulos novos na tela, todos tirados da voz: "Seu cliente também lê.", "E fala direto na tela
  dele.", "Push ilimitado." (o v1 tinha "Push ilimitado" também).
- Trilha da Eleven Music no lugar da trilha sintetizada.
- Fonte do v1 guardada em `v1-fonte.tar.gz` (o `-v1` renderizado continua em `renders/`).

Reproduzir (depois da animação): `bash assets/audio/mix.sh` (áudio) · `python3 assets/audio/legenda.py` (legenda) ·
`bash build.sh check|snap|render`.
