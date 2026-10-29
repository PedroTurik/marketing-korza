# Hub de marketing da Korza — plano

Criado em 2026-10-26. Hub único onde o Pedro, junto com o Claude, cuida de todo o marketing da Korza
(korza.app; antes korza.com.br): ads pagos, copy, SEO, conteúdo orgânico, edição de vídeo e motion.

## Princípio

O hub não é um repositório de código, é um **cérebro com receitas**. Tudo depende das mesmas perguntas:
quem é a Korza, com quem fala, o que pode afirmar e como soa. Isso fica escrito num lugar só (`contexto/`)
e toda tarefa lê de lá.

| Camada | O que é | Onde |
| --- | --- | --- |
| 1. Contexto | Marca, voz, claims, produto, público, concorrentes, posicionamento | `contexto/` |
| 2. Playbooks | Skills do Claude, uma por tarefa recorrente | `.claude/skills/` |
| 3. Conexões | Meta Ads, Instagram, Google Ads, GA4, Search Console | `.mcp.json` / scripts |
| 4. Produção | Uma pasta por frente | `campanhas/`, `conteudo/`, `seo/`, `studio/` |
| 5. Memória | Catálogo do que foi feito, resultados, aprendizados | `aprendizados.md`, catálogos por frente |

## Estrutura

```
marketing/
  CLAUDE.md               regras da casa e mapa do hub
  PLANO.md                este arquivo
  MELHORIAS.md            o que enriquece o hub sem travar o trabalho (fila de melhorias)
  contexto/               FONTE DA VERDADE (lida antes de qualquer tarefa)
    marca/                visual: tokens, logo, fontes, 3D, referências, specs por formato
    voz.md                tom, vocabulário, o que nunca dizer
    claims.md             ÚNICA lista de números/afirmações aprovados
    produto.md            Método AOP, planos, preço, integrações, prazos
    publico.md            lojista: segmentos, dores, objeções, nível de consciência
    concorrentes.md
    posicionamento.md     mensagem-mãe ("você aluga seu cliente" → canal próprio de recompra)
  conexoes/               CONEXOES.md (como ler cada canal, IDs, credenciais) + scripts
  estrategia/             plano do trimestre, metas, calendário mestre, plano de medição
  campanhas/              ads pagos: AAAA-MM-<slug>/ (brief, copies, criativos, públicos, resultados)
  conteudo/               orgânico: calendário + uma pasta por post/carrossel/reels
  seo/                    keywords, auditorias/, blog/ (pautas e artigos)
  studio/
    kit/                  peças de marca reutilizáveis: abertura, encerramento, lower third, legenda, CTA
    motion/               ads 100% animados (HyperFrames)
    gravados/             vídeos com filmagem: brutos → transcrição → roteiro de corte → render
  relatorios/             semanais/mensais a partir dos dados reais
  aprendizados.md         o que funcionou e o que não, com números
  inbox/                  material bruto
  .claude/skills/         playbooks
```

## Decisões

- **Ponto de partida: não existe marketing hoje.** A Korza só faz outbound (WhatsApp). O hub constrói do zero.
- **Funil self-serve.** Oferta de entrada "veja seu app gratuitamente" (conta grátis + preview no onboarding),
  assinatura sem contato humano. Reunião com especialista é caminho secundário. Detalhes em `contexto/produto.md`.
- **Tudo de marketing fica dentro de `marketing/`.** Nada na raiz `korza/`.
- **video-edit é absorvido** em `studio/motion/`. Foi um experimento; aproveitamos o que funcionou
  (fonte única de marca, skill dedicada, catálogo, regras de claims) sem obrigação de manter o formato.
  A marca deixa de ser específica de vídeo: `frame.md` vira uma das specs de formato (vídeo, post estático,
  carrossel, OG).
- **Site:** a pasta `korza/site` NÃO é o site atual. O site real será clonado depois (pedir ao Pedro
  quando precisar). O hub cuida de estratégia, copy e SEO; mudanças de código acontecem no repo do site.
- **Vendas fora do escopo:** `crm-automacao` e `korza-leads` continuam separados.
- **Git** para histórico de copies e campanhas, mesmo trabalhando sozinho. Mídia pesada e renders fora do git.
- **Conexões leem por padrão; escrever (subir campanha, publicar post, responder comentário) só com OK
  explícito para aquele plano.**
- **Sem LinkedIn.**

## Canais e conexões

| Conexão | Para quê | Esforço |
| --- | --- | --- |
| GA4 | Tráfego, conversões do site | Baixo (conta de serviço) |
| Search Console | Buscas, posições, páginas, indexação | Baixo (conta de serviço) |
| Meta Ads | Ler performance; depois criar/ajustar campanhas com aprovação | Médio (app no Meta for Developers) |
| Instagram (@korza.br) | Métricas por post, público, horários, comentários, benchmark de concorrentes; depois publicar com aprovação | Mesmo app do Meta Ads. Exige conta profissional ligada a uma Página do Facebook |
| Google Ads | Ler performance; depois campanhas com aprovação | Feito em 2026-10-29 (conta de serviço, acesso Explorer) |

Instagram começa só em leitura. Publicação vem quando o fluxo de conteúdo estiver rodando.
Limitações: a API não agenda posts de Instagram nativamente; DMs exigem permissões e revisão extras.

## Studio: vídeo gravado

Fluxo: bruto em `inbox/` → transcrição local (Whisper) + frames amostrados → proposta de corte (silêncios,
gaguejos, takes repetidos, gancho) → legendas animadas na marca, lower thirds, B-roll (telas do produto
ou motion), abertura/CTA do `kit/`, reenquadramento 16:9 → 9:16 → render → revisão.

Limite: o Claude trabalha por transcrição e frames, não assiste ao vídeo. Ótimo para vídeos de fala
(explicação, depoimento, tutorial, corte de live). Para edição de ritmo visual, primeiro corte aqui e
refinamento num editor (ou exportar lista de cortes para DaVinci/Premiere).

## Rotina de uso

- **Segunda:** `/relatorio` puxa Meta, Instagram, GA4 e Search Console, compara com a semana anterior e sugere ações.
- **Semana:** pedidos em linguagem natural ("carrossel sobre recompra", "campanha de fundo de funil",
  "audita o SEO da home", "edita esse vídeo") → o playbook certo é usado.
- **Ao fechar algo:** registra no catálogo da frente e o aprendizado em `aprendizados.md`.

## Fases

0. **Fundação** — `CLAUDE.md`, migrar a marca para `contexto/marca/`, escrever `contexto/` (em conversa:
   o Claude pergunta e escreve).
   - [x] Snapshot do site ao vivo (`contexto/fontes/site-2026-10-26.md`)
   - [x] `claims.md` reconciliado com o Pedro
   - [x] `produto.md` (preço, oferta, funil self-serve)
   - [x] Migrar a marca (`contexto/marca/`): direção C — base clara, azul como impacto, escuro/3D como acento raro
   - [x] `voz.md`: calorosa no gancho, concreta na prova
   - [x] `publico.md` (definição do Pedro: Nuvemshop/Shopify, R$ 30 mil+/mês, dono ou gestor)
   - [x] `concorrentes.md` (levantamento de 2026-10-26)
   - [x] `posicionamento.md` (4 pilares: recompra, conversão, marca, canal próprio + 3 facilitadores)
1. **Studio** — estrutura pronta em 2026-10-26 (template testado, skill `/korza-video`, `studio/STUDIO.md`).
   Muita coisa será definida nas primeiras produções: ver "A definir nas primeiras vezes" em `studio/STUDIO.md`.
2. **Conexões** — concluída em 2026-10-27: GA4, Search Console, Meta Ads (MCP e API), Instagram, Pixel e GA4 no site,
   site migrado para `korza.app`. Como usar em `conexoes/CONEXOES.md`; o que medir em `estrategia/plano-de-medicao.md`.
   Google Ads conectado em 2026-10-29. O que ficou de fora (admin, Conversions API, banner, tag do Google Ads, script de relatório) está em `MELHORIAS.md`.
3. **Playbooks** — uma skill por frente, criada quando a tarefa for feita pela primeira vez à mão
   (primeiro fazemos juntos, depois vira receita).
4. **Ritmo** — relatório semanal, calendário editorial, ciclo de aprendizados.

## Status

- [x] Plano
- [x] Esqueleto de pastas + git
- [x] Fase 0 — Fundação
- [x] Fase 1 — Studio (estrutura; decisões pendentes para as primeiras produções)
- [x] Fase 2 — Conexões (melhorias em `MELHORIAS.md`)
- [ ] Fase 3 — Playbooks ← **próximo:** a primeira peça real (campanha ou conteúdo), feita junto e depois virando receita
- [ ] Fase 4 — Ritmo
