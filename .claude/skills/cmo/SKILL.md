---
name: cmo
description: Ritual semanal do CMO da Korza. Puxa dados de todos os canais, varre o radar de features e marcos, confere a cadência, decide as prioridades da semana e o que impulsionar. Use para "relatório da semana", "o que fazemos agora?", "como estamos?", "revisão de campanha" ou no início da semana.
---

# Ritual do CMO

Saída: uma decisão por frente e uma lista curta do que o Pedro precisa fazer. Relatório sem decisão não serve.

## 1. Situação

Leia `estrategia/plano-90-dias.md`, `conteudo/calendario.md`, `estrategia/radar.md`, `aprendizados.md` e o último arquivo em
`relatorios/`.

## 2. Dados (só leitura, 7 dias contra os 7 anteriores)

| Fonte | Como |
| --- | --- |
| Instagram, Meta Ads | Graph API, `conexoes/CONEXOES.md`. Por post: alcance, salvamentos, compartilhamentos, cliques |
| GA4 | `mcp__google-analytics__run_report`, propriedade `560905270`, por canal e página |
| Search Console | `uv run conexoes/search_console.py --por query --dias 7` e `--por page` |
| Google Ads | `mcp__google-ads__*`, só se houver campanha |
| HubSpot | `python3 -m outbound status`, rodado em `../crm-automacao`. Nunca `rotina --executar`, `disparar --executar`, `mover`, `importar` ou `setup` |
| Chatwoot | Só em agregado: objeções e perguntas frequentes. Sem nome de pessoa nos arquivos do hub |

Se uma fonte falhar, diga qual e siga com as outras.

## 3. Radar

Varra as fontes de `estrategia/radar.md`, classifique o que for novo em A, B ou C e registre a decisão. Confira "Próximos
marcos" e "Datas de verificação".

## 4. Decidir

Para cada frente, uma decisão com o motivo:

- **Cadência:** quantos posts saíram contra o plano. Abaixo de 4 por semana, ache a causa e ajuste a grade.
- **Pauta-mãe da semana** e o desdobramento por canal.
- **Impulsionar:** quais posts passam na regra de `plano-90-dias.md`, com valor, público e duração.
- **Campanhas:** manter, cortar ou escalar. Mudança real exige OK do Pedro.
- **Metas:** no caminho ou não. Se não, o que muda.

## 5. Registrar

- `relatorios/AAAA-MM-DD.md`: números, decisões e o que ficou em aberto, em até uma tela.
- Atualize `conteudo/calendario.md`, `estrategia/radar.md` e `aprendizados.md`.

## 6. Entregar

Fale com o Pedro nesta ordem, sem jargão:

1. **Em uma frase:** como foi a semana.
2. **Três prioridades**, em ordem, cada uma com o porquê.
3. **Decidi:** o que já foi resolvido.
4. **Preciso do seu OK:** planos com gasto ou publicação, via `AskUserQuestion`.
5. **Com você / comigo:** listas numeradas.
