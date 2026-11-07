"""M2, variação "busca". Gera, a partir da voz da pergunta (vo-busca.mp3 + vo-busca-words.json):
  compositions/s0-busca.html       barra de busca digitando (tempo de cada letra)
  compositions/legenda-busca.html  legenda do gancho (mesmo padrão do legenda.py)
  assets/audio/busca/teclas.wav    cliques de tecla + Enter, nos mesmos tempos da tela
Rode da pasta do projeto: python3 assets/audio/busca/gerar.py
O resto do vídeo (o M2 -v2) entra deslocado em H segundos: ver variante.py e mix.sh."""
import html, json, wave
import numpy as np

H = 3.2                         # 96 quadros exatos (quadros do M2 iguais ao -v2); a trilha entra com 1,5 compasso (3,2143s) cortado em 14ms
VO_AT = 0.0                     # a pergunta começa no frame 0
TEXTO = "Como criar um app do meu e-commerce Shopify ou Nuvemshop?"
PREFIXO = "Como criar um app"   # já digitado no frame 0 (legível de cara)
LEAD, PASSO = 0.2, 0.04         # a digitação adianta 0,2s a palavra falada; 40ms por letra
ENTER = 3.08                    # Enter; a busca sai para cima e revela o ato 1 (que começa em H)
SAIDA = 3.22
FIM = 3.65                      # duração da cena s0-busca (fica por cima do ato 1 até aqui)
SR = 48000

words = [w for w in json.load(open("assets/audio/busca/vo-busca-words.json")) if not w["w"].startswith("[")]
assert " ".join(w["w"] for w in words) == TEXTO, [w["w"] for w in words]

# ── tempo de cada letra ──
chars = []  # (char, t ou None se já visível)
n_pref = len(PREFIXO.split())
for k, w in enumerate(words):
    sep = [] if k == 0 else [(" ", None)]
    if k < n_pref:
        chars += sep + [(c, None) for c in w["w"]]
        continue
    t0 = w["s"] + VO_AT - LEAD
    chars += [(" ", t0 - PASSO / 2)] + [(c, round(t0 + i * PASSO, 3)) for i, c in enumerate(w["w"])]
ultimo = max(t for _, t in chars if t is not None)
assert ultimo < ENTER - 0.02, ultimo

# ── HTML da barra: palavras sem quebra interna, letras escondidas no CSS até a hora ──
out, palavra = [], []
def fecha():
    if palavra: out.append('<span class="bz-wd">' + "".join(palavra) + "</span>"); palavra.clear()
for c, t in chars:
    if c == " ":
        fecha()
        out.append(" " if t is None else f'<span class="bz-c" data-t="{t:.3f}"> </span>')
    else:
        palavra.append(html.escape(c) if t is None else f'<span class="bz-c" data-t="{t:.3f}">{html.escape(c)}</span>')
fecha()
texto_html = "".join(out)

cena = f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <!--
      Gancho "busca" (0–{FIM}s, por cima do ato 1, que começa em {H:.4f}s). GERADO por assets/audio/busca/gerar.py: não edite à mão.
      Modo profundo igual ao ato 1. A pergunta é digitada numa barra de busca genérica (sem marca de buscador); no Enter a
      barra sobe e o fundo some, revelando a "resposta": o título e o orçamento do ato 1.
    -->
  </head>
  <body>
    <template>
      <style>
        #root {{
          position: absolute;
          inset: 0;
          overflow: hidden;
        }}
        #bz-bg {{
          position: absolute;
          inset: 0;
          background: radial-gradient(120% 70% at 50% 30%, #1a2f52 0%, #10213b 55%, #0a1628 100%);
        }}
        #bz-grid {{
          position: absolute;
          inset: -120px;
          background-image: linear-gradient(rgba(255, 255, 255, 0.045) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.045) 1px, transparent 1px);
          background-size: 72px 72px;
        }}
        #bz-bar {{
          position: absolute;
          left: var(--edge-x);
          right: var(--edge-x);
          top: 600px;
          display: flex;
          align-items: flex-start;
          gap: 30px;
          padding: 46px 52px 50px 44px;
          background: #fff;
          border-radius: 48px;
          box-shadow: 0 40px 90px rgba(3, 10, 24, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.08);
          color: #10213b;
          transform-origin: 50% 50%;
        }}
        #bz-ico {{
          flex: none;
          width: 64px;
          height: 64px;
          margin-top: 10px;
        }}
        #bz-txt {{
          font-size: 70px;
          font-weight: 600;
          line-height: 1.16;
          letter-spacing: -0.035em;
        }}
        .bz-wd {{
          white-space: nowrap;
        }}
        .bz-c {{
          display: none;
        }}
        #bz-cur {{
          display: inline-block;
          width: 6px;
          height: 0.9em;
          margin-left: 4px;
          vertical-align: -0.1em;
          border-radius: 3px;
          background: #10213b;
        }}
        #bz-load {{
          position: absolute;
          left: 48px;
          right: 48px;
          bottom: 0;
          height: 6px;
          border-radius: 3px;
          background: #10213b;
          opacity: 0;
          transform-origin: left center;
        }}
      </style>

      <div id="root" data-composition-id="s0-busca" data-width="1080" data-height="1920">
        <div id="bz-bg"><div id="bz-grid"></div></div>
        <div id="bz-bar" data-layout-ignore>
          <svg id="bz-ico" viewBox="0 0 64 64" fill="none" stroke="#7d8da1" stroke-width="6" stroke-linecap="round">
            <circle cx="27" cy="27" r="18" />
            <line x1="40.5" y1="40.5" x2="57" y2="57" />
          </svg>
          <div id="bz-txt">{texto_html}<span id="bz-cur"></span></div>
          <div id="bz-load"></div>
        </div>
      </div>

      <script>
        const tl = gsap.timeline({{ paused: true }});
        // câmera: aproximação lenta durante a digitação
        tl.fromTo("#bz-bar", {{ scale: 0.97 }}, {{ scale: 1.02, duration: {ENTER}, ease: "none" }}, 0);
        tl.fromTo("#bz-grid", {{ y: 0 }}, {{ y: 36, duration: {FIM}, ease: "none" }}, 0);
        // letras
        document.querySelectorAll("#bz-txt .bz-c").forEach((c) => tl.set(c, {{ display: "inline" }}, +c.dataset.t));
        // cursor pisca enquanto a voz alcança o texto
        [0.25, 0.75, 3.2].forEach((t) => tl.set("#bz-cur", {{ opacity: 0 }}, t));
        [0.5, {ENTER - 0.3:.2f}].forEach((t) => tl.set("#bz-cur", {{ opacity: 1 }}, t));
        // Enter: a barra afunda, a linha de carregamento corre
        tl.to("#bz-bar", {{ scale: 0.985, duration: 0.07, ease: "power2.out" }}, {ENTER});
        tl.to("#bz-bar", {{ scale: 1.02, duration: 0.12, ease: "power2.out" }}, {ENTER + 0.07:.2f});
        tl.set("#bz-load", {{ opacity: 1 }}, {ENTER});
        tl.fromTo("#bz-load", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.22, ease: "power2.inOut", immediateRender: false }}, {ENTER});
        // resposta: a barra sobe e sai, o fundo some e revela o ato 1
        tl.to("#bz-bar", {{ y: -1100, rotation: -3, duration: 0.4, ease: "power3.in" }}, {SAIDA});
        tl.to("#bz-bg", {{ opacity: 0, duration: 0.3, ease: "power1.inOut" }}, {SAIDA + 0.1:.2f});
        window.__timelines["s0-busca"] = tl;
      </script>
    </template>
  </body>
</html>
'''
open("compositions/s0-busca.html", "w").write(cena)

# ── legenda do gancho (mesmo padrão e posição do legenda.py) ──
GROUPS = [(4, None), (3, None), (3, None)]  # Como criar um app | do meu e-commerce | Shopify ou Nuvemshop?
FIM_LEG = H + 0.239 - 0.05                  # 1º grupo da legenda do M2 entra em H + 0,239
i, groups = 0, []
for n, disp in GROUPS:
    ws = words[i:i + n]; i += n
    groups.append([(w["w"], round(w["s"] + VO_AT, 3)) for w in ws])
items = []
for k, g in enumerate(groups):
    s = max(0.0, g[0][1] - 0.05)
    e = groups[k + 1][0][1] - 0.1 if k + 1 < len(groups) else FIM_LEG
    spans = " ".join(f'<span class="w" data-s="{ws:.3f}">{html.escape(t)}</span>' for t, ws in g)
    items.append(f'<div class="lg-g" id="lb-g{k}" data-s="{s:.3f}" data-e="{e:.3f}"><div class="cap">{spans}</div></div>')
legenda = open("compositions/legenda.html").read()
ini, fim = legenda.index('<div class="lg-g"'), legenda.rindex("</div></div>") + len("</div></div>")
legenda = legenda[:ini] + "\n          ".join(items) + legenda[fim:]
legenda = (legenda.replace('data-composition-id="legenda"', 'data-composition-id="legenda-busca"')
           .replace("[data-composition-id='legenda']", "[data-composition-id='legenda-busca']")
           .replace('window.__timelines["legenda"]', 'window.__timelines["legenda-busca"]')
           .replace("GERADO por assets/audio/legenda.py", "GERADO por assets/audio/busca/gerar.py"))
open("compositions/legenda-busca.html", "w").write(legenda)

# ── cliques de tecla (síntese própria, determinística) ──
rng = np.random.default_rng(7)
def clique(forte=False):
    n = int(SR * (0.05 if forte else 0.03)); t = np.arange(n) / SR
    ruido = rng.standard_normal(n)
    ruido = np.convolve(ruido, np.ones(3) / 3, "same") - np.convolve(ruido, np.ones(24) / 24, "same")  # passa-banda grosso
    corpo = np.sin(2 * np.pi * (180 if forte else 260) * t) * np.exp(-t / (0.012 if forte else 0.006))
    return (ruido * np.exp(-t / (0.006 if forte else 0.003)) * 0.6 + corpo * 0.5) * (1.0 if forte else rng.uniform(0.7, 1.0))
dur = FIM + 0.2
buf = np.zeros(int(SR * dur))
for c, t in chars:
    if t is None or c == " ": continue
    x = clique(); a = int(t * SR); buf[a:a + len(x)] += x
x = clique(True); a = int(ENTER * SR); buf[a:a + len(x)] += x
buf = buf / np.abs(buf).max() * 0.5
pcm = (np.repeat(buf[:, None], 2, 1) * 32767).astype("<i2")
with wave.open("assets/audio/busca/teclas.wav", "wb") as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())

print(f"✓ H={H:.4f}s · letras até {ultimo:.2f}s · Enter {ENTER}s · cena até {FIM}s")
for k, g in enumerate(groups): print("  legenda", items[k].split('data-s="')[1][:6], " ".join(t for t, _ in g))
