# Demanda: Motion M1, "A notificação" (e o padrão de motion da Korza)

**Status:** `aprovada`
**Criada em:** 2026-11-05
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

## Objetivo

Um motion de cerca de 25s, com voz de IA e legenda, para anúncio na Meta e para o Reels do @korza.br. É o **primeiro motion
produzido no Studio**: além do vídeo, ele define o padrão (voz, legenda, trilha, vinheta) que o M2 e o M3 vão reaproveitar.

## Por que

Pilar **canal próprio**, falando com o **dono** de e-commerce. O gancho usa um reflexo: todo mundo lê uma notificação que
chega. A voz vira o jogo ("você leu, seu cliente também lê") e mostra que, com o app, a loja fala direto na tela do
cliente. É um dos três motions da primeira leva (M2: do zero × Korza; M3: o painel), que também servem de teste de criativo.

## Leia antes

- `studio/STUDIO.md` e `studio/frame.md`
- `contexto/voz.md`, `contexto/marca/MARCA.md`
- `contexto/claims.md`: `plataformas`, `prazo-14-dias`, `push-ilimitado`

## Pré-requisito: voz (ElevenLabs)

- O Pedro cria a conta na ElevenLabs (plano pago, com uso comercial) e salva a chave num terminal fora do Claude:
  `read -rs T && printf 'ELEVENLABS_API_KEY=%s\n' "$T" > ~/.config/korza-marketing/elevenlabs.env && chmod 600 ~/.config/korza-marketing/elevenlabs.env`
- Gere a frase "Você leu essa notificação, né? Seu cliente também lê." em **3 a 4 vozes femininas, calmas e próximas, em
  PT-BR** (tom de conversa, nada de locutora de varejo). O Pedro escolhe uma, e ela vira a voz padrão da Korza.
- Documente a conexão em `conexoes/CONEXOES.md` (status, credencial, como usar e o `voice_id` escolhido).

## Roteiro

**Cena 1 (gancho, 0–3s).** Um celular grande na tela, em mockup, e uma notificação bem chamativa chegando de cima, com
som de notificação. Precisa ser lida em menos de 1 segundo.

- **Gancho A (principal):** remetente **"Amor ❤️"**, texto **"Precisamos conversar..."**
- **Gancho B (variação):** remetente **"Mãe ❤️"**, texto **"Me liga quando puder."**

Ícone de mensagem genérico (balão), **sem logo do WhatsApp, do iMessage ou da Apple**, e sem o som de notificação da
Apple: use um som genérico livre.

**Voz** (o mesmo texto depois de qualquer gancho):

> "Você leu essa notificação, né? Seu cliente também lê. Com a Korza, sua loja ganha um app próprio e fala direto na tela
> dele. Para lojas Nuvemshop e Shopify. App no ar em até 14 dias úteis. Notificações push ilimitadas. Crie sua conta e
> veja seu app grátis."

- Os três pontos (Nuvemshop e Shopify · em até 14 dias úteis · push ilimitado) aparecem como tópicos animados, um por vez,
  sincronizados com a voz.
- O fechamento fica no modo impacto (azul), com o CTA na tela e o logo.
- Pequenos ajustes de palavra para caber no ritmo da voz estão liberados. Os claims não mudam: sempre "em até 14 dias
  úteis", nunca "2 semanas".

## Padrão a definir e registrar (vale para o M2 e o M3)

Decida, aplique e registre em `studio/STUDIO.md`, marcando os itens da seção "A definir":

- **Legenda:** queimada no vídeo, com o estilo da marca (Plus Jakarta 600, palavra ativa em azul, poucas palavras por
  vez), dentro da zona segura do Reels
- **Trilha:** livre de direitos e liberada para anúncio. A biblioteca do Instagram não serve. Registre a fonte e a
  licença. A trilha fica baixa sob a voz
- **Vinheta de fechamento:** logo e CTA, com cerca de 1 a 2 segundos, no `studio/kit/`, para ser reaproveitada
- **Estrutura:** gancho → virada → prova ou benefício → CTA → logo
- **Loudness de entrega**

## Requisitos

- Dois renders por gancho: **9:16 (1080×1920)**, para Reels, Stories e anúncio, e **4:5 (1080×1350)**, para o feed do
  anúncio. São 4 arquivos.
- Duração de 20 a 30s
- Só os claims `plataformas`, `prazo-14-dias` e `push-ilimitado`
- CTA: "Crie sua conta e veja seu app grátis"

## Fora do escopo

- Subir anúncio, publicar ou escrever a legenda do post
- Inventar cliente: a notificação é pessoal (Amor/Mãe), não de loja
- Mudar o site ou o `contexto/`

## Critério de pronto

- [x] ElevenLabs conectada, voz escolhida pelo Pedro e registrada em `conexoes/CONEXOES.md`
- [x] A notificação é legível em menos de 1s, no celular, nas duas versões de gancho
- [x] Voz e legenda sincronizadas; nenhuma palavra fora da zona segura
- [x] Nenhum logo de terceiro (Apple, WhatsApp) nem som da Apple
- [x] `npm run check` sem erros e snapshots revisados
- [x] 4 renders `-v1` em `renders/`
- [x] Padrão registrado em `studio/STUDIO.md` e vinheta no `kit/`
- [x] Linha no `studio/motion/CATALOGO.md`

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Onde:** `studio/motion/2026-11-05-m1-notificacao/renders/` →
`m1-notificacao-a-9x16-v1.mp4`, `m1-notificacao-b-9x16-v1.mp4`, `m1-notificacao-a-4x5-v1.mp4`,
`m1-notificacao-b-4x5-v1.mp4` (22,5s, H.264 30fps, -14 LUFS / -1 dBTP). Storyboard em `STORYBOARD.md` do projeto.

**Feito:**
- ElevenLabs no plano Starter (o Pedro assinou durante a execução). Voz padrão: **Bea** (`cabLxBh81HurPAAJfEHo`),
  `eleven_v3`, speed 1.05, escolhida pelo Pedro após 3 rodadas de ajuste. Registrada em `conexoes/CONEXOES.md`.
- Padrão de motion registrado em `studio/STUDIO.md` ("Padrão de motion"); itens de "A definir" marcados.
- Kit: `studio/kit/vinheta.html`, `studio/kit/audio/sintetizar.py` (trilha + som de notificação + tick) e
  componentes novos no `korza-video.css` (celular de bloqueio, notificação, legenda).
- HyperFrames atualizado de 0.8.158 para 0.9.16 (template, skill e M1).

**Diferente do pedido:**
- **Trilha:** não é de banco de músicas. A Eleven Music é "For Individual Use Only" nos planos Starter a Pro (a Korza é
  empresa), e não consegui confirmar a licença do Mixkit para anúncio. Saída: trilha **própria, sintetizada em
  código** (fonte: o hub; licença: nossa, sem restrição de canal). Se a qualidade não agradar, dá para trocar por uma
  faixa licenciada sem mexer no resto (só o `mix.sh`).
- **Duração 22,5s** e vinheta de 2,2s (pedido: 1–2s), para o CTA ficar ≥ 2,5s na tela.
- **CTA sem legenda:** nos últimos segundos, a voz fala o CTA e o botão na tela mostra o mesmo texto; a legenda sai para não duplicar.
- Na tela, "14 dias úteis" em algarismo; a voz fala "quatorze" (por extenso para a pronúncia sair certa).
- Cena 2 mostra um push genérico "Sua loja: Novidade pra você. Vem ver." (ícone de sacola), sem cliente inventado.
- Ícone de mensagem azul genérico e coração em SVG (sem emoji de sistema, sem logo de terceiros).

**Pendências (Pedro):** ouvir/ver os 4 renders; trocar a chave da ElevenLabs, que passou pelo chat.
