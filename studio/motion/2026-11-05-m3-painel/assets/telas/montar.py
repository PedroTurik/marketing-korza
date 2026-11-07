"""M3. Monta compositions/s1-mundo.html: src/mundo.html + src/mundo.js + telas extraídas do admin (assets/telas/*.html).
Rode da pasta do projeto: python3 assets/telas/montar.py"""
import math, re
T = "assets/telas"
def tela(n):
    h = open(f"{T}/{n}.html", encoding="utf8").read().replace("__IMG__", f"{T}/img")
    # o CSS de tamanho de tela (min-height: 100svh etc.) já vem resolvido em px
    if n.endswith("-celular"):
        h = h.replace(f"{T}/img/favicon.png", "assets/img/icone-loja.svg")   # push com ícone da loja, nunca o símbolo da Korza
    if n.startswith("boasvindas"):
        h = h.replace("10:41", "9:46")                                       # entrega em 5 minutos, como no print real
    if n == "cupom":
        h = h.replace(f"{T}/img/favicon.png", f"{T}/img/favicon.png")
    h = re.sub(r'<(desc|title)\b[^>]*>.*?</\1>', '', h, flags=re.S)        # <desc> vazio dos gráficos quebra o serializador do HyperFrames
    # tira "Rastreamento" da campanha (texto técnico gerado)
    h = re.sub(r'chegou_a_coleo_nova', '', h)
    return h
def linhas():
    out = []
    for i in range(0, 118):
        x0 = i * 82 - 80; d = f"M{x0} 0"
        for y in range(0, 7001, 140):
            x = x0 + 26 * math.sin(y / 620 + i * .13) + 16 * math.sin(y / 240 + i * .41)
            d += f"L{x:.1f} {y}"
        out.append(f'<path d="{d}"/>')
    return f'<g fill="none" stroke="#c9d9f5" stroke-width="2.4">{"".join(out)}</g>'
src = open("compositions/src/mundo.html", encoding="utf8").read()
for n in ["vendas","boasvindas","site","cupom","campanha","campanha-celular","cupom-celular","site-celular","boasvindas-celular"]:
    src = src.replace("{{%s}}" % n, tela(n))
src = src.replace("{{campanha2}}", "").replace("{{linhas}}", linhas()).replace("{{js}}", open("compositions/src/mundo.js", encoding="utf8").read())
open("compositions/s1-mundo.html", "w", encoding="utf8").write(src)
print("s1-mundo.html", len(src)//1024, "KB")
