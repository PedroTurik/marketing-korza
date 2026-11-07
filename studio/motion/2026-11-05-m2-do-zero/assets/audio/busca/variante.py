"""M2, variação "busca": monta o index.html da variante a partir do index.html do M2 (-v2), sem mudar nada dele.
Tudo do M2 é deslocado em H segundos; entram a cena s0-busca (por cima do ato 1) e a legenda do gancho; o áudio vira
mix-busca.wav. Uso (o build.sh chama): python3 assets/audio/busca/variante.py index.html > <saída>"""
import re, sys

H = 3.2  # igual a gerar.py
FIM_S0 = 3.65
src = open(sys.argv[1]).read()

def num(x): return f"{x:.4f}".rstrip("0").rstrip(".")

# 1. desloca data-start (> 0 ou não) de toda clip/áudio do M2 e estende as durações de 25.25
dur_m2 = float(re.search(r'id="root"[^>]*data-duration="([\d.]+)"', src).group(1))
src = re.sub(r'(<(?:div|audio) id="(?!root)[^"]+"[^>]*?data-start=")([\d.]+)"',
             lambda m: f'{m.group(1)}{num(float(m.group(2)) + H)}"', src)
src = src.replace(f'data-composition-id="main" data-start="0" data-duration="{num(dur_m2)}"',
                  f'data-composition-id="main" data-start="0" data-duration="{num(dur_m2 + H)}"', 1)
# o áudio é um mix próprio, que já começa no zero
src = re.sub(r'<audio id="mix" src="assets/audio/mix.wav" data-start="[\d.]+" data-duration="[\d.]+"',
             f'<audio id="mix" src="assets/audio/busca/mix-busca.wav" data-start="0" data-duration="{num(dur_m2 + H)}"', src)
assert "mix-busca.wav" in src
# 2. cortes do timeline principal
src = re.sub(r"const CUTS = \[([^\]]*)\]",
             lambda m: "const CUTS = [" + ", ".join(num(float(x) + H) for x in m.group(1).split(",")) + "]", src)
# 3. cena do gancho e legenda do gancho
novas = (f'<div id="s0-busca" class="clip" data-composition-id="s0-busca" data-composition-src="compositions/s0-busca.html" '
         f'data-start="0" data-duration="{FIM_S0}" data-track-index="3" data-width="1080" data-height="1920"></div>\n      '
         f'<div id="legenda-busca" class="clip" data-composition-id="legenda-busca" data-composition-src="compositions/legenda-busca.html" '
         f'data-start="0" data-duration="{num(H + 0.19)}" data-track-index="4" data-width="1080" data-height="1920"></div>\n      ')
src = src.replace('<div id="legenda" class="clip"', novas + '<div id="legenda" class="clip"', 1)
css = """      #s0-busca { z-index: 30; }
      #legenda-busca { z-index: 40; }
      [data-fmt="feed"] #bz-bar { top: 400px !important; }
      [data-fmt="feed"] #bz-txt { font-size: 64px !important; }
      #legenda {"""
src = src.replace("      #legenda {", css, 1)
src = src.replace("<title>Korza — M2 Do zero × Korza</title>", "<title>Korza — M2 Do zero × Korza (gancho busca)</title>")
sys.stdout.write(src)
