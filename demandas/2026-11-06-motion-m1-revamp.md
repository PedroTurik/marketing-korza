# Demanda: Motion M1, revamp visual ("A notificação" v2)

**Status:** `feita`
**Criada em:** 2026-11-06
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Um `-v2` do M1 com animação e estética refeitas. A copy e a voz ficam como estão. O vídeo precisa chegar ao nível de
acabamento do M2 e do M3.

## Por que

A copy do M1 é ótima, mas ele foi o primeiro motion do Studio e ficou visualmente básico, com cara de "mal feito": cenas
de 4 a 8s paradas, tópicos em lista e pouca profundidade. Para rodar como anúncio ao lado do M2 e do M3, ele precisa do
mesmo padrão visual. Pilar **canal próprio**, falando com o **dono**.

## Leia antes

- `demandas/2026-11-05-motion-m1-notificacao.md` (a demanda original e a Entrega)
- `studio/motion/2026-11-05-m1-notificacao/STORYBOARD.md`
- `studio/STUDIO.md` e `studio/frame.md`
- **Referência de nível:** `studio/motion/2026-11-05-m2-do-zero/` e `studio/motion/2026-11-05-m3-painel/` (o
  `STORYBOARD.md` de cada um e os renders `-v2`/`-v1`)
- `contexto/marca/MARCA.md`
- `contexto/claims.md`: `plataformas`, `prazo-14-dias`, `push-ilimitado`

## Design antes de animar (obrigatório)

1. **Vá além do M2 e do M3, não só do M1:** corte ou movimento novo a cada 1–2s, composição em camadas, celular em
   perspectiva e profundidade, tipografia cinética, transições com intenção. Use `/hyperframes-animation` e
   `/hyperframes-registry` antes de desenhar à mão.
2. **Storyboard primeiro:** reescreva o `STORYBOARD.md` do projeto com a direção visual, os quadros-chave de cada cena
   (snapshots estáticos, em `storyboard/`) e o mapa de tempo. **Mostre ao Pedro e só anime depois do OK.**
3. Pontos que pedem mais atenção:
   - **Gancho:** a notificação "Amor ❤ / Precisamos conversar..." continua legível em menos de 1s, mas com chegada mais
     cinematográfica (celular com volume e luz, câmera reagindo à notificação).
   - **A virada ("Seu cliente também lê"):** transição visual da notificação pessoal para o push da loja, como causa e
     efeito, sem corte seco.
   - **Os 3 tópicos:** hoje são uma lista. Cada um vira uma cena própria (Nuvemshop e Shopify, em até 14 dias úteis, push
     ilimitado).
   - **Fechamento:** impacto azul, CTA e vinheta, no nível do fechamento do M3.

## Requisitos

- **Copy e voz não mudam.** Reaproveite o áudio da voz atual (gancho A) sem regerar. O vídeo segue o tempo da voz, então a
  duração fica perto dos 22,5s do v1.
- **Só o gancho A** ("Amor"). O gancho B não entra (decisão do Pedro).
- **Trilha nova da Eleven Music,** instrumental, no ritmo dos cortes, no lugar da trilha sintetizada do v1. Prompt
  registrado no projeto. Mix, ducking e loudness como no padrão do `studio/STUDIO.md`.
- Legenda no padrão atual (pílula, na altura usada no M2/M3 v2).
- Só os claims `plataformas`, `prazo-14-dias` e `push-ilimitado`, com a redação de `claims.md`. Sempre "em até 14 dias
  úteis".
- Nenhum logo de terceiro (Apple, WhatsApp) nem som da Apple, como no v1.
- Dois renders: `m1-notificacao-a-9x16-v2.mp4` (1080×1920) e `m1-notificacao-a-4x5-v2.mp4` (1080×1350). Os `-v1` ficam.
- Componentes novos ficam no projeto do M1. Se mexer em algo do `studio/kit/` (CSS, vinheta), confira que o M2 e o M3
  continuam iguais.

## Fora do escopo

- Mudar copy, voz ou claims
- Gancho B
- Subir anúncio, publicar ou escrever a legenda do post

## Critério de pronto

- [x] Storyboard aprovado pelo Pedro antes da animação
- [x] Ritmo no nível do M2/M3: corte ou movimento novo a cada 1–2s, nenhuma cena parada
- [x] Notificação legível em menos de 1s
- [x] Voz do v1 intacta; legenda sincronizada e dentro da zona segura
- [x] Trilha da Eleven Music, com o prompt registrado no projeto
- [x] `npm run check` sem erros e snapshots revisados
- [x] 2 renders `-v2` em `renders/`
- [ ] `studio/motion/CATALOGO.md` atualizado

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Onde:** `studio/motion/2026-11-05-m1-notificacao/renders/m1-notificacao-a-9x16-v2.mp4` e `m1-notificacao-a-4x5-v2.mp4`
(22,5s, H.264 30 fps, -14 LUFS / -1 dBTP). Os `-v1` continuam lá. Storyboard, decisões e como reproduzir em `STORYBOARD.md` do
projeto; quadros-chave aprovados em `storyboard/quadros-chave.jpg`.

**Feito:**
- Storyboard com 16 quadros-chave, aprovado pelo Pedro em 2026-11-06 antes da animação.
- 6 cenas novas, com transições de câmera (chicote, mergulho, o push que voa e vira o azul) no lugar do wipe. Gancho em modo
  profundo: celular com volume, luz da tela, tranco de câmera (`camera-shake` do registry) e "Amor" legível em 0,4s. Na
  virada, o mesmo cartão vira o push da "Sua Loja" e a câmera recua para um campo de celulares. Os 3 tópicos viraram cenas:
  cartões com logos, "14" com régua de dias úteis e chuva de pushes que vira túnel. Fechamento azul com CTA (4,9s na tela) e
  a vinheta do kit.
- Voz do v1 sem regerar (`vo.mp3`). Legenda em pílula em y=1480 (9:16) e y=1196 (4:5), com início das frases corrigido por
  `silencedetect`.
- Trilha nova da Eleven Music (prompt em `assets/audio/trilha-prompt.json`), mix pelo padrão do `STUDIO.md`.
- Nada em `studio/kit/` foi alterado: os componentes novos estão em `assets/v2/` do projeto. A fonte do v1 está guardada em
  `v1-fonte.tar.gz`.

**Diferente do pedido:**
- **Logos da Nuvemshop e da Shopify** nos cartões do tópico 1: pedido do Pedro no OK do storyboard. São os arquivos oficiais
  do site. Apple e WhatsApp continuam fora.
- **Trilha sem regerar:** a faixa veio com intro até 8s e o groove morria em 18s. O `mix.sh` corta e repete compassos no
  grid de 120 BPM: o groove entra no "Com a Korza" (4,62s) e vai até a vinheta.
- **Quadro 12:** o selo "App no ar" carimba sob a régua. O celular subindo não coube nos 0,5s antes do corte.
- O check avisa que 3 títulos ficam menos de 1s na tela. Eles repetem a fala, que já está na legenda, no ritmo do M2/M3.
- **`studio/motion/CATALOGO.md` não foi atualizado:** é um arquivo compartilhado, e outros agentes estavam mexendo nos outros
  motions ao mesmo tempo (instrução do Pedro). Linha a trocar na do M1:
  `| 2026-11-05-m1-notificacao | "A notificação": todo mundo lê a notificação que chega; o mesmo cartão vira o push da loja e a câmera recua para um campo de celulares. v2: celular 3D, câmera viva, 3 tópicos em cenas (logos Nuvemshop/Shopify, "14" com régua, túnel de pushes). Gancho A (Amor); B só no v1 | canal próprio | plataformas, prazo-14-dias, push-ilimitado | Crie sua conta e veja seu app grátis | 9:16 + 4:5, 22,5s, voz Bea + legenda, trilha Eleven Music | renders/m1-notificacao-a-{9x16,4x5}-v2.mp4 (v1 mantidos) | pronto, não publicado | — |`

**Pendências (Pedro):** ver e ouvir os 2 renders; atualizar o `CATALOGO.md` quando os outros motions fecharem (ou me pedir).
