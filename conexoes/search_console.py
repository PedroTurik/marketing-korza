# /// script
# requires-python = ">=3.11"
# dependencies = ["google-auth", "requests"]
# ///
"""Leitura do Search Console da Korza (só leitura).

Uso:
  uv run conexoes/search_console.py                      # top buscas dos últimos 28 dias
  uv run conexoes/search_console.py --por page --dias 7  # top páginas da última semana
  uv run conexoes/search_console.py --por date           # série diária
  uv run conexoes/search_console.py --por query,page --limite 50 --csv > buscas.csv

Credencial: conta de serviço em ~/.config/korza-marketing/google-sa.json (fora do git),
ou o caminho em GOOGLE_APPLICATION_CREDENTIALS. Ver conexoes/CONEXOES.md.
"""
import argparse
import csv
import datetime as dt
import os
import sys
from urllib.parse import quote

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

SITE = "sc-domain:korza.com.br"
CHAVE = os.environ.get(
    "GOOGLE_APPLICATION_CREDENTIALS",
    os.path.expanduser("~/.config/korza-marketing/google-sa.json"),
)
ESCOPO = "https://www.googleapis.com/auth/webmasters.readonly"
DIMENSOES = {"query", "page", "date", "device", "country", "searchAppearance"}


def consultar(dimensoes, inicio, fim, limite, site):
    creds = service_account.Credentials.from_service_account_file(CHAVE, scopes=[ESCOPO])
    url = f"https://www.googleapis.com/webmasters/v3/sites/{quote(site, safe='')}/searchAnalytics/query"
    corpo = {"startDate": inicio.isoformat(), "endDate": fim.isoformat(),
             "dimensions": dimensoes, "rowLimit": limite}
    resposta = AuthorizedSession(creds).post(url, json=corpo)
    if resposta.status_code != 200:
        sys.exit(f"Erro {resposta.status_code}: {resposta.text}")
    return resposta.json().get("rows", [])


def main():
    p = argparse.ArgumentParser(description="Desempenho de busca da Korza no Google.")
    p.add_argument("--por", default="query", help="dimensões separadas por vírgula: " + ", ".join(sorted(DIMENSOES)))
    p.add_argument("--dias", type=int, default=28, help="janela até hoje (padrão 28)")
    p.add_argument("--limite", type=int, default=25)
    p.add_argument("--site", default=SITE)
    p.add_argument("--csv", action="store_true", help="saída em CSV")
    a = p.parse_args()

    dimensoes = a.por.split(",")
    if not set(dimensoes) <= DIMENSOES:
        p.error(f"dimensão inválida: {set(dimensoes) - DIMENSOES}")
    fim = dt.date.today()
    linhas = consultar(dimensoes, fim - dt.timedelta(days=a.dias), fim, a.limite, a.site)

    cabecalho = dimensoes + ["cliques", "impressoes", "ctr", "posicao"]
    tabela = [r["keys"] + [r["clicks"], r["impressions"], f"{r['ctr']:.1%}", f"{r['position']:.1f}"] for r in linhas]
    if a.csv:
        w = csv.writer(sys.stdout)
        w.writerow(cabecalho)
        w.writerows(tabela)
        return
    if not tabela:
        print("Sem dados no período (o Search Console tem ~2 dias de atraso).")
        return
    larguras = [max(len(str(x)) for x in col) for col in zip(cabecalho, *tabela)]
    for linha in [cabecalho, *tabela]:
        print("  ".join(str(x).ljust(w) for x, w in zip(linha, larguras)))


if __name__ == "__main__":
    main()
