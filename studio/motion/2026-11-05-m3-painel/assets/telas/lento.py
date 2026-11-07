"""M3. Dilata o filme para a captura do motion blur: o HyperFrames captura até 240 fps, então o filme roda N vezes mais lento
(N=4 equivale a 960 amostras por segundo real). Só o build.sh chama, sobre as cópias temporárias de index.html e compositions/.
O áudio sai daqui: o mix.wav volta no ffmpeg, depois de voltar à velocidade normal.
Uso: python3 assets/telas/lento.py 4"""
import glob, re, sys

N = int(sys.argv[1])

s = open("index.html", encoding="utf8").read()
s = re.sub(r'\s*<audio id="mix"[^>]*></audio>', "", s)
s = re.sub(r'data-(start|duration)="([\d.]+)"', lambda m: f'data-{m[1]}="{float(m[2]) * N:g}"', s)
open("index.html", "w", encoding="utf8").write(s)

for f in glob.glob("compositions/*.html"):
    h = open(f, encoding="utf8").read()
    h2 = re.sub(
        r'window\.__timelines\["([\w-]+)"\]\s*=\s*tl;',
        lambda m: f'{{ const m = gsap.timeline({{ paused: true }}); tl.paused(false); tl.timeScale({1 / N}); m.add(tl, 0); window.__timelines["{m[1]}"] = m; }}',
        h,
    )
    assert h2 != h, f"timeline não encontrada em {f}"
    open(f, "w", encoding="utf8").write(h2)
print(f"filme dilatado {N}x")
