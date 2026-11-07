"""M3. Gera compositions/legenda.html a partir dos tempos da voz (vo-v2-words.ed.json), padrão M1/M2.
v2: gancho novo "Isso é o que você ganha…" (v1 usava vo-a-words.ed.json com GA = 4, 4, 3). Rode da pasta do projeto: python3 assets/audio/legenda.py"""
import json, html
A = json.load(open("assets/audio/vo-v2-words.ed.json"))
GA = [(4, None), (2, None), (4, None), (3, None), (3, None)]  # Isso é o que | você ganha | quando lança o app | da sua loja | com a Korza.
CORPO = [(3, None), (3, None), (2, None),          # Escreva o push, | escolha o destino | e agende.
         (4, None), (3, None),                     # Cupom para a primeira | compra no app.
         (3, None), (4, None),                     # Banner no site | para baixar o app.
         (2, None), (3, None),                     # Boas-vindas automáticas | para quem instala.
         (5, None), (4, None),                     # Vendas do app e do | site, lado a lado.
         (5, "E 1 em cada 3"), (4, None), (5, None),  # E um em cada três | pedidos no app vem | de quem já tinha comprado.
         (4, None), (4, None)]                     # Transforme a sua recompra | e fidelize seu cliente.
def grupos(ws, gs):
    i = 0; out = []
    for n, disp in gs:
        p = ws[i:i + n]; i += n
        shown = disp.split() if disp else [w["w"] for w in p]
        assert len(shown) == len(p), (shown, p)
        out.append([(s, w["s"], w["e"]) for s, w in zip(shown, p)])
    return out, i
ga, na = grupos(A, GA); corpo, nc = grupos(A[na:], CORPO)
def itens(gs, cls, nxt0):
    out = []
    for k, g in enumerate(gs):
        nxt = gs[k + 1][0][1] if k + 1 < len(gs) else nxt0
        s = g[0][1] - 0.05; e = min(nxt - 0.06, g[-1][2] + 0.5)
        spans = " ".join(f'<span class="w" data-s="{ws}">{html.escape(t)}</span>' for t, ws, _ in g)
        out.append(f'<div class="lg-g {cls}" data-s="{max(0,s):.3f}" data-e="{e:.3f}"><div class="cap">{spans}</div></div>')
    return out
body = itens(ga, "", corpo[0][0][1]) + itens(corpo, "", A[na + nc][ "s"] if na + nc < len(A) else 99)
tpl = open("assets/audio/legenda.tpl.html", encoding="utf8").read().replace("{{body}}", "\n          ".join(body))
open("compositions/legenda.html", "w", encoding="utf8").write(tpl)
print(len(body), "grupos · último fim:", body[-1][body[-1].find('data-e="')+8:][:6], "· sobra:", " ".join(w["w"] for w in A[na+nc:]))
