"""M2. Gera compositions/legenda.html a partir de assets/audio/vo-words.json (tempos da ElevenLabs).
Rode da pasta do projeto: python3 assets/audio/legenda.py"""
import json, html
VO_AT = 0.15
words = [w for w in json.load(open("assets/audio/vo-words.json")) if not w["w"].startswith("[")]
# grupos de 1–5 palavras (n de palavras da voz), com texto exibido (números em algarismo na tela)
GROUPS = [
    (4, None), (2, None), (4, "até R$ 100 mil."),        # Um app do zero | pode custar | até cem mil reais.
    (3, None), (3, None), (3, None), (3, None),           # Meses de projeto. | Conta na Apple | e no Google. | Aprovação nas lojas.
    (2, None), (4, None), (4, None), (2, None),           # Na Korza, | você conecta sua loja, | escolhe logo e cores… | e pronto.
    (3, None), (4, None), (3, None),                      # A gente constrói | e publica seu app, | iOS e Android,
    (5, "em até 14 dias úteis!"),                         # em até quatorze dias úteis!
]  # o CTA final ("Crie sua conta grátis na Korza.") fica sem legenda: o botão na tela faz esse papel
i = 0; groups = []
for n, disp in GROUPS:
    ws = words[i:i + n]; i += n
    shown = disp.split() if disp else [w["w"] for w in ws]
    assert len(shown) == len(ws), (shown, ws)
    groups.append([(s, round(w["s"] + VO_AT, 3), round(w["e"] + VO_AT, 3)) for s, w in zip(shown, ws)])
for k, g in enumerate(groups):
    nxt = groups[k + 1][0][1] if k + 1 < len(groups) else g[-1][2] + 0.4
    g_end = min(nxt - 0.1, g[-1][2] + 0.6)
    groups[k] = (g, g[0][1] - 0.05, g_end)

items = []
for k, (g, s, e) in enumerate(groups):
    spans = " ".join(f'<span class="w" data-s="{ws}">{html.escape(t)}</span>' for t, ws, we in g)
    items.append(f'<div class="lg-g" id="lg-g{k}" data-s="{s:.3f}" data-e="{e:.3f}"><div class="cap">{spans}</div></div>')
body = "\n          ".join(items)
dur = groups[-1][2]
out = f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <!-- Legenda queimada (padrão Korza). GERADO por assets/audio/legenda.py a partir dos tempos da voz: não edite à mão. -->
  </head>
  <body>
    <template>
      <style>
        #root {{
          position: absolute;
          inset: 0;
          pointer-events: none;
        }}
        .lg-g {{
          position: absolute;
          left: var(--edge-x);
          right: var(--edge-x);
          top: 1480px;
          display: flex;
          justify-content: center;
          opacity: 0;
        }}
      </style>

      <div id="root" data-composition-id="legenda" data-width="1080" data-height="1920">
          {body}
      </div>

      <script>
        const tl = gsap.timeline({{ paused: true }});
        document.querySelectorAll("[data-composition-id='legenda'] .lg-g").forEach((g) => {{
          const s = +g.dataset.s, e = +g.dataset.e;
          tl.fromTo(g, {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.12, ease: "power2.out", immediateRender: false }}, s);
          tl.set(g, {{ opacity: 0 }}, e);
          g.querySelectorAll(".w").forEach((w, i, all) => {{
            const ws = +w.dataset.s;
            tl.set(w, {{ color: "#155DFC" }}, ws);
            const next = all[i + 1];
            if (next) tl.set(w, {{ color: "#10213B" }}, +next.dataset.s);
          }});
        }});
        window.__timelines["legenda"] = tl;
      </script>
    </template>
  </body>
</html>
'''
open("compositions/legenda.html", "w").write(out)
print(f"✓ {len(groups)} grupos, legenda até {dur:.2f}s")
for g, s, e in groups: print(f"  {s:6.2f}–{e:6.2f}  {' '.join(t for t,_,_ in g)}")
