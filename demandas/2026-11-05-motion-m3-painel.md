# Demanda: Motion M3, "O painel"

**Status:** `feita`
**Criada em:** 2026-11-05
**Especialidade:** motion
**Skill:** `/korza-video`

Execute fora do Modo CMO. Este arquivo é o escopo inteiro.

**Depende do M1** (`demandas/2026-11-05-motion-m1-notificacao.md`). Já entregue: este
motion reaproveita a voz, a legenda, a trilha e a vinheta definidas lá. Pode rodar em paralelo com o M2.

## Objetivo

Um motion dinâmico, de cerca de 25s, com voz de IA e legenda, para anúncio na Meta e para o Reels do @korza.br. Ele mostra,
animado, o que dá para fazer no painel da Korza, e cada feature aparece como resultado para a loja.

## Por que

Fala com o **gestor de e-commerce**, enquanto o M1 e o M2 falam com o dono. Pilar **recompra**. O lojista não compra
função, compra resultado: cada cena diz o que ele ganha, sobre a tela real. O fechamento puxa a melhor prova de recompra.

## Leia antes

- `studio/STUDIO.md` (com o padrão registrado pelo M1) e `studio/frame.md`
- `contexto/voz.md`, `contexto/marca/MARCA.md`
- `contexto/claims.md`: `recompra-1-em-3`, `push-ilimitado`
- `contexto/produto.md`: "Funcionalidades"
- `contexto/telas/README.md` e `contexto/telas/painel/`

## Design antes de animar (obrigatório)

O M1 ficou bom, mas simplista. Este motion precisa ser **mais dinâmico e mais desenhado**.

1. **Referência de ritmo:** abra o M1 (`studio/motion/2026-11-05-m1-notificacao/`) e o `STORYBOARD.md` dele, e vá além:
   corte ou movimento novo a cada 1–2s, composição em camadas, telas reais em perspectiva e profundidade, tipografia
   cinética, transições com intenção. Use `/hyperframes-animation` e `/hyperframes-registry` antes de desenhar à mão.
2. **Storyboard primeiro:** `STORYBOARD.md` no projeto com a direção visual, os quadros-chave de cada cena (snapshots
   estáticos) e o mapa de tempo. **Mostre ao Pedro e só anime depois do OK.**
3. **Copy e fluxo podem mudar** para servir ao visual: cortar, reordenar, trocar palavras, dividir cenas. **Não mudam:**
   o ângulo da peça, os claims (IDs abaixo, com a redação de `claims.md`), o CTA e a duração de 20–30s. Registre na
   Entrega o que mudou.

## Trilha

Eleven Music (ElevenLabs), por decisão do Pedro, mesmo marcada "For Individual Use Only". Uma faixa instrumental
gerada para este vídeo, no ritmo dos cortes. Mix, ducking e loudness como no padrão do `studio/STUDIO.md`.

## Roteiro (ponto de partida)

**Gancho (0–3s):**

- **A (principal):** "Tudo que o app da sua loja faz, num painel só."
- **B (variação):** "Quanto o app da sua loja vendeu este mês?"

**Uma feature por cena**, com a frase na voz e a tela real animada (zoom, cursor, destaque):

1. "Escreva o push, escolha o destino e agende." → `painel/campaign_preenchida.png` ou `iphone-campaigns_create.png`.
   Troque a oferta fictícia do exemplo por uma neutra.
2. "Banner de cupom para o cliente baixar o app." → `painel/customization_coupon-banner.png`
3. "Boas-vindas automáticas para quem instala." → `painel/customization_welcome-notification.png`
4. "Vendas do app e do site, lado a lado." → não há print do analytics. Recrie a tela em HTML a partir do código de
   `korza/dev/admin` (só leitura, não altere o repositório). Números da tela ilustrativos e ilegíveis. Nessa cena,
   o único número legível é o card **"1 em cada 3 pedidos no app vem de quem já tinha comprado"** (`recompra-1-em-3`).

**Fechamento (voz + tela, modo impacto):**

> "Transforme a sua recompra e fidelize seu cliente. Crie sua conta grátis na Korza."

Pequenos ajustes de palavra para o ritmo estão liberados.

## Requisitos

- Dois ganchos × dois formatos: **9:16 (1080×1920)** e **4:5 (1080×1350)**. São 4 renders.
- Duração de 20 a 30s, com a voz e a legenda do padrão M1
- Só telas reais ou recriadas fielmente a partir do código do admin; nada inventado
- Nos prints, cortar o nome da conta de teste e o domínio de teste

## Fora do escopo

- **Públicos** (liberado para poucas lojas) e **carrinho abandonado** ("em breve"): não aparecem, nem em segundo plano.
  No `customization.png`, o card "Em breve" é cortado
- Dados reais de clientes (`inbox/admin-2026-10-30/` não sai de lá)
- Subir anúncio, publicar ou escrever a legenda do post

## Critério de pronto

- [x] 4 features + fechamento, cada uma sobre tela real
- [x] Públicos e carrinho abandonado ausentes
- [x] Único número legível: `recompra-1-em-3`
- [x] Storyboard aprovado pelo Pedro antes da animação
- [x] Ritmo acima do M1: corte ou movimento novo a cada 1–2s
- [x] Trilha da Eleven Music, com o prompt registrado no projeto
- [x] `npm run check` sem erros e snapshots revisados
- [x] Renders `-v1` em `renders/` (2, não 4: gancho A só, decisão do Pedro)
- [x] Linha no `studio/motion/CATALOGO.md`

## Entrega

Preenchido por quem executou: onde está o resultado e o que ficou diferente do pedido.

**Onde:** `studio/motion/2026-11-05-m3-painel/renders/` → `m3-painel-9x16-v1.mp4` e `m3-painel-4x5-v1.mp4` (26,8s, H.264 30 fps, AAC, -14 LUFS).
Storyboard e mapa de tempo em `STORYBOARD.md`; quadros em `storyboard/`.

**Diferente do pedido (decisões do Pedro):**
1. **2 renders, não 4:** só o gancho A. A voz do gancho B está no projeto (`assets/audio/vo-b-gancho.mp3`).
2. **Plano-sequência 3D** sem wipes: o conceito escolhido troca os cortes por voos de câmera num mural de telas.
3. **Cupom e banner do site em duas frases e duas telas:** "Banner de cupom para o cliente baixar o app" estava incorreto; o cupom fica dentro do app, e quem leva a baixar é o banner do site.
4. **Prova falada:** a demanda só pedia o card na tela.
5. **Títulos como resultado** ("Sua oferta, na hora certa.") e a voz com a ação.
6. **Selo "Push ilimitado"** na cena do push (`push-ilimitado`), sem voz.

**Diferente do pedido (decisões de execução):**
7. **Telas:** extraídas do admin real numa cópia, com os mocks do e2e, em vez de prints; o acesso à conta real não foi usado, e nenhum dado de cliente entrou. Textos de exemplo aprovados pelo Pedro, loja genérica "Sua Loja".
8. **Banner do site:** o editor mostra um exemplo fixo no iframe, então esse banner é recriado com o texto de exemplo do próprio painel.
9. **Duração 26,8s** (pedido: cerca de 25s, dentro de 20–30s), por causa da prova falada. CTA na tela por 3,6s.
10. **Números:** todo número de resultado fica borrado ou escondido, e o único legível é `recompra-1-em-3`. Horários de interface seguem legíveis ("Amanhã, 10:00", "Hoje, 19:00", 9:41, 9:46), como também "1 em 3" no donut.
11. **Card da prova:** é o card real "Composição dos pedidos", sem valores nem descrições; o donut mostra 1/3 no lugar do número fictício do fixture.
12. **Trilha:** faixa da Eleven Music remontada no grid, sem regerar, para o clímax cair no fechamento.
13. **`npm run check`:** 0 erros. Sobram avisos: tamanho da composição e imagens repetidas, consequência das telas em HTML, e o CTA "lido em 1,3s", falso positivo porque ele continua igual na vinheta. A interface do painel está marcada com `data-layout-ignore`, fora das regras de texto de cena.

**Limite da revisão:** revisei por quadros amostrados e medições de áudio. Não dá para assistir nem ouvir daqui: ritmo real e mix pedem o seu olho e ouvido.

**Pendências (Pedro):** ver e ouvir os 2 renders. Risco de licença da Eleven Music segue aceito por você, conforme `STUDIO.md`.
