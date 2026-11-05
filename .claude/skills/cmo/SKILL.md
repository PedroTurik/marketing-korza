---
name: cmo
description: Análise de marketing da Korza, sob demanda. Puxa dados dos canais, varre o radar de features e marcos, diz o que aprendemos e o que muda. Use quando o Pedro pedir "relatório", "como estamos?", "o que fazemos agora?", "revisão de campanha" ou análise de um canal. Nunca rodar sem pedido.
---

# Análise do CMO

Só roda quando o Pedro pede. Saída: o que aprendemos e o que muda, com uma lista curta do que o Pedro precisa fazer.
Relatório sem decisão não serve. Não há metas: compare com o período anterior e com o que esperávamos ao decidir.

Se o pedido for sobre um canal ou campanha só, rode só a parte que importa.

## 1. Situação

Leia `aprendizados.md`, `conteudo/publicacoes.md`, `estrategia/radar.md` e o último arquivo em `relatorios/`, se houver.

## 2. Dados (só leitura; padrão: 7 dias contra os 7 anteriores, ou o período que o Pedro pedir)

| Fonte | Como |
| --- | --- |
| Instagram, Meta Ads | Graph API, `conexoes/CONEXOES.md`. Por post: alcance, salvamentos, compartilhamentos, cliques |
| GA4 | `mcp__google-analytics__run_report`, propriedade `560905270`, por canal e página |
| Search Console | `uv run conexoes/search_console.py --por query --dias 7` e `--por page` |
| Google Ads | `mcp__google-ads__*`, só se houver campanha |
| HubSpot | `python3 -m outbound status`, rodado em `../crm-automacao`. Nunca `rotina --executar`, `disparar --executar`, `mover`, `importar` ou `setup` |
| Chatwoot | Só em agregado: objeções e perguntas frequentes. Sem nome de pessoa nos arquivos do hub |

Se uma fonte falhar, diga qual e siga com as outras. Com amostra pequena, diga que é pequena.

## 3. Radar

Varra as fontes de `estrategia/radar.md`, classifique o que for novo em A, B ou C e registre a decisão. Confira "Próximos
marcos" e "Datas de verificação".

## 4. Decidir

Para cada frente com dado, uma decisão com o motivo:

- **Conteúdo:** o que rendeu acima ou abaixo da média e o que isso muda nas pautas e nos formatos.
- **Impulsionar:** se algum post merece verba, com valor, público e duração. Sem regra fixa: caso a caso, pelo dado.
- **Campanhas:** manter, cortar ou escalar, e quanto. Verba se ajusta pelo resultado. Mudança real exige OK do Pedro.
- **Apostas:** alguma linha `aposta` de `aprendizados.md` ganhou ou perdeu sustentação?

## 5. Registrar

- `relatorios/AAAA-MM-DD.md`: números, decisões e o que ficou em aberto, em até uma tela.
- Resultados em `conteudo/publicacoes.md`; decisões em `aprendizados.md`; itens novos em `estrategia/radar.md`.
- Trabalho operacional vira arquivo em `demandas/`, a partir de `demandas/_modelo.md`.

## 6. Entregar

Fale com o Pedro nesta ordem, sem jargão:

1. **Em uma frase:** o que os dados dizem.
2. **Até três prioridades**, em ordem, cada uma com o porquê.
3. **Decidi:** o que já foi resolvido.
4. **Preciso do seu OK:** planos com gasto ou publicação, via `AskUserQuestion`.
5. **Com você / comigo:** listas numeradas.
