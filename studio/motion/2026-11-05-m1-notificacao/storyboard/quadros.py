"""Quadros-chave estáticos do M1 v2 (fase de storyboard). Rodar num projeto HyperFrames temporário com link para assets/: python3 quadros.py && hyperframes snapshot --at 0.5,1.5,...,15.5"""
HEART = '<svg viewBox="0 0 24 24" fill="#E8414E"><path d="M12 21s-7.5-4.6-9.6-9.2C1 8.6 3 5 6.6 5c2.1 0 3.6 1.1 5.4 3 1.8-1.9 3.3-3 5.4-3C21 5 23 8.6 21.6 11.8 19.5 16.4 12 21 12 21z"/></svg>'
MSG = '<div class="ic-msg"><svg viewBox="0 0 24 24" fill="#fff"><path d="M12 3C6.9 3 3 6.5 3 10.8c0 2.4 1.2 4.5 3.1 5.9-.2 1.4-.9 2.7-1.9 3.6 2 0 3.8-.7 5.1-1.8.9.2 1.8.3 2.7.3 5.1 0 9-3.5 9-7.9S17.1 3 12 3z"/></svg></div>'
LOJA = '<img src="assets/v2/icone-loja.svg" alt="">'

def notif(kind="amor", mid=None):
    if kind == "amor":
        ic, t, x = MSG, f"Amor {HEART}", "Precisamos conversar..."
    else:
        ic, t, x = LOJA, "Sua Loja", "Novidade pra você. Vem ver."
    if mid is not None:  # rolando: mostra metade de cada
        return (f'<div class="nt"><div class="nt-ic">{LOJA}<div style="clip-path:inset(0 0 {100-mid}% 0)">{MSG}</div></div><div class="nt-body">'
                f'<div class="nt-head"><div class="nt-title roll"><span style="transform:translateY(-{mid}%)">Amor {HEART}</span><span style="transform:translateY(-{mid}%)">Sua Loja</span></div><span class="nt-when">agora</span></div>'
                f'<div class="nt-text roll"><span style="transform:translateY(-{mid}%)">Precisamos conversar...</span><span style="transform:translateY(-{mid}%)">Novidade pra você. Vem ver.</span></div></div></div>')
    return f'<div class="nt"><div class="nt-ic">{ic}</div><div class="nt-body"><div class="nt-head"><div class="nt-title">{t}</div><span class="nt-when">agora</span></div><div class="nt-text">{x}</div></div></div>'

def phone(tf, wp="wp-noite", inner="", glare="100%", layers=20):
    edges = "".join(f'<div class="ph3-e" style="transform:translateZ(-{(k+1)*1.9:.1f}px)"></div>' for k in range(layers))
    return (f'<div class="ph3" style="transform:{tf}">{edges}<div class="ph3-body"><div class="ph3-screen"><div class="wp {wp}"></div>{inner}'
            f'<div class="ph3-cam"></div><div class="ph3-glare" style="background-position:{glare} 0"></div></div></div></div>')

def lock(n="amor", time="21:47", mid=None, nt=True):
    return f'<div class="lk-time">{time}</div><div class="lk-date">quinta-feira, 5 de novembro</div>' + (notif(n, mid) if nt else "")

def mini(x, y, z, ry, lit=True):
    n = f'<div class="n">{LOJA}<div><b>Sua Loja</b><span>Novidade pra você.</span></div></div>' if lit else ""
    return f'<div class="mp" style="transform:translate3d({x}px,{y}px,{z}px) rotateY({ry}deg)"><div class="scr"><div class="wp wp-loja"></div><div class="t">21:47</div>{n}</div></div>'

def ttl(lines, dk=False, top=270, eb=None, size=None):
    ebh = f'<div class="eb">{eb[0]}<s>' + "".join(f'<b class="{"on" if i < eb[1] else ""}"></b>' for i in range(3)) + "</s></div>" if eb else ""
    st = f"top:{top}px;" + (f"font-size:{size}px;" if size else "")
    return f'<div class="ttl{" dk" if dk else ""}" style="{st}">{ebh}' + "".join(f'<span class="mk"><span class="in">{l}</span></span>' for l in lines) + "</div>"

def cap(words, on):
    return '<div style="position:absolute;left:72px;right:72px;top:1480px;display:flex;justify-content:center"><div class="cap">' + " ".join(
        f'<span class="w" style="color:{"#155DFC" if i == on else "#10213B"}">{w}</span>' for i, w in enumerate(words)) + "</div></div>"

BG_NOITE = '<div style="position:absolute;inset:0;background:radial-gradient(900px 1100px at 50% 46%, #17336f 0%, #0b1730 55%, #060d1c 100%)"></div>'
BG_ICE = '<div style="position:absolute;inset:0;background:radial-gradient(1100px 900px at 70% 60%, #dbe7ff 0%, rgba(219,231,255,0) 70%), radial-gradient(900px 800px at 18% 28%, #e6eeff 0%, rgba(230,238,255,0) 70%), #f5f8fc"></div>'
SCRIM = '<div style="position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(#f5f8fc 0%, #f5f8fc 70%, rgba(245,248,252,0) 100%)"></div>'
BG_IMP = '<div class="bg-impact"></div>'
def glow(x, y, w, h, c="rgba(80,140,255,.55)"):
    return f'<div class="glow" style="left:{x-w/2}px;top:{y-h/2}px;width:{w}px;height:{h}px;background:radial-gradient(closest-side, {c}, rgba(0,0,0,0))"></div>'
def stage(inner, po="540px 900px"):
    return f'<div class="st3" style="perspective-origin:{po}"><div class="cam3">{inner}</div></div>'

F = []  # (rótulo, html)

# 1 — 0,3s: chega a notificação; celular inclinado no escuro, luz da tela
F.append(("0,3s gancho", BG_NOITE + glow(540, 860, 1300, 1500) + stage(phone("translate3d(0,140px,260px) rotateX(16deg) rotateY(-24deg) rotateZ(5deg)", inner=lock())) ))
# 2 — 1,4s: câmera chega perto, reflexo corre no vidro
F.append(("1,4s Você leu", BG_NOITE + glow(540, 760, 1400, 1300, "rgba(90,150,255,.6)") + stage(phone("translate3d(0,330px,420px) rotateX(6deg) rotateY(-7deg) rotateZ(1deg)", inner=lock(), glare="55%")) + cap(["Você", "leu", "essa", "notificação,"], 1)))
# 3 — 2,5s: "né?" — close extremo, marca-texto lendo a frase
F.append(("2,5s né?", BG_NOITE + stage(phone("translate3d(40px,330px,900px) rotateX(2deg) rotateY(-3deg)", inner=lock() + '<div style="position:absolute;left:148px;top:600px;width:420px;height:10px;border-radius:5px;background:#155dfc"></div>', glare="40%")) + cap(["né?"], 0)))
# 4 — 3,4s: virada — a mesma notificação troca de remetente rolando; fundo clareia
F.append(("3,4s Seu cliente", '<div style="position:absolute;inset:0;background:linear-gradient(#0b1730,#24407e)"></div>' + glow(540, 900, 1400, 1400, "rgba(120,170,255,.6)") + stage(phone("translate3d(0,420px,600px) rotateX(4deg) rotateY(-4deg)", wp="wp-loja", inner=lock("loja"), glare="20%")) + ttl(["Seu cliente"], dk=True) + cap(["Seu", "cliente", "também", "lê."], 1)))
# 5 — 4,2s: câmera recua: campo de celulares, todos com o push da loja
minis = "".join(mini(x, y, z, ry) for x, y, z, ry in [(-560, -700, -500, 14), (-150, -740, -500, 4), (260, -700, -500, -8), (-760, -200, -200, 18), (440, -220, -200, -14), (-560, 520, -260, 14), (300, 540, -260, -10)])
F.append(("4,2s também lê", BG_ICE + stage(minis + phone("translate3d(0,220px,40px) rotateX(10deg) rotateY(-10deg) scale(.62)", wp="wp-loja", inner=lock("loja")), "540px 640px") + SCRIM + ttl(["Seu cliente", "<em>também lê.</em>"]) + cap(["Seu", "cliente", "também", "lê."], 3)))
# 6 — 5,1s: "Com a Korza," — chicote para o claro, logo entra; celular sobe de lado
F.append(("5,1s Com a Korza", BG_ICE + f'<img src="assets/brand/logo/korza-logo-color.png" style="position:absolute;left:72px;top:270px;width:300px">' + ttl(["Com a Korza,"], top=360) + stage(phone("translate3d(80px,420px,-100px) rotateX(18deg) rotateY(-26deg) rotateZ(8deg) scale(.86)", wp="wp-loja", inner=lock(nt=False))) + cap(["Com", "a", "Korza,"], 2)))
# 7 — 6,7s: ícone da loja cai na tela inicial
grid = '<div style="position:absolute;left:62px;right:62px;top:420px;display:grid;grid-template-columns:repeat(4,1fr);gap:46px 38px">' + "".join('<div style="width:112px;height:112px;border-radius:28px;background:rgba(255,255,255,.22)"></div>' for _ in range(12)) + "</div>"
icon = '<img src="assets/v2/icone-loja.svg" style="position:absolute;left:224px;top:700px;width:232px;height:232px;border-radius:54px;box-shadow:0 30px 60px rgba(4,12,30,.45), 0 0 0 10px rgba(255,255,255,.35)"><div style="position:absolute;left:0;right:0;top:950px;text-align:center;color:#fff;font-size:38px;font-weight:600">Sua Loja</div>'
F.append(("6,7s app próprio", BG_ICE + glow(540, 1050, 1100, 1100, "rgba(21,93,252,.18)") + stage(phone("translate3d(0,240px,0) rotateX(8deg) rotateY(-12deg) scale(.82)", wp="wp-loja", inner=grid + icon, glare="45%")) + ttl(["Sua loja ganha", "<em>um app próprio.</em>"]) + cap(["um", "app", "próprio"], 2)))
# 8 — 8,3s: push da loja desce e salta para fora da tela
pz = '<div class="pz" style="left:160px;top:860px;transform:rotate(-3deg)"><img src="assets/v2/icone-loja.svg"><div><b>Sua Loja</b><span>Novidade pra você. Vem ver.</span></div><i>agora</i></div>'
F.append(("8,3s na tela dele", BG_ICE + glow(540, 1050, 1100, 1100, "rgba(21,93,252,.18)") + stage(phone("translate3d(-60px,420px,-260px) rotateX(10deg) rotateY(14deg) scale(.82)", wp="wp-loja", inner=lock(nt=False), glare="70%")) + pz + ttl(["E fala direto", "<em>na tela dele.</em>"]) + cap(["na", "tela", "dele."], 1)))
# 9 — 9,9s: tópico 1 — Nuvemshop entra como cartão grande
F.append(("9,9s Nuvemshop", BG_ICE + ttl(["Para lojas"], eb=("Plataformas", 1)) + '<div class="wc" style="left:110px;top:720px;transform:rotate(-4deg)"><span class="dot"></span>Nuvemshop</div>' + stage(phone("translate3d(260px,560px,-500px) rotateX(16deg) rotateY(-24deg) scale(.7)", wp="wp-loja", inner=lock("loja"))) + cap(["Para", "lojas", "Nuvemshop"], 2)))
# 10 — 11,0s: Shopify se encaixa; linha liga as duas ao celular
F.append(("11,0s e Shopify", BG_ICE + ttl(["Para lojas", "<em>Nuvemshop e Shopify.</em>"], eb=("Plataformas", 1), size=88) + '<svg style="position:absolute;inset:0" viewBox="0 0 1080 1920"><path d="M470 780 C 700 800, 720 980, 800 1050 M 420 1000 C 640 1010, 700 1050, 800 1070" fill="none" stroke="#155dfc" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/></svg><div class="wc" style="left:72px;top:700px;transform:rotate(-3deg) scale(.86)"><span class="dot"></span>Nuvemshop</div><div class="wc" style="left:120px;top:930px;transform:rotate(2deg) scale(.86)"><span class="dot"></span>Shopify</div>' + stage(phone("translate3d(300px,540px,-500px) rotateX(14deg) rotateY(-26deg) scale(.68)", wp="wp-loja", inner=lock("loja"))) + cap(["e", "Shopify."], 1)))
# 11 — 13,3s: "14" gigante + régua de dias úteis enchendo
rg = '<div class="rg" style="left:72px;top:1100px">' + "".join('<i class="on"></i>' if i < 9 else "<i></i>" for i in range(5)) + '<i class="we"></i>' + "".join('<i class="on"></i>' if i < 4 else "<i></i>" for i in range(5)) + '<i class="we"></i>' + "".join("<i></i>" for _ in range(4)) + "</div>"
rg = '<div class="rg" style="left:72px;top:1130px;flex-wrap:wrap;width:940px;row-gap:16px">' + "".join(f'<i class="{"on" if i < 9 else ""}"></i>' for i in range(14)) + "</div>"
F.append(("13,3s 14 dias", BG_ICE + ttl(["App no ar em até"], eb=("Prazo", 2), size=72) + '<div style="position:absolute;left:60px;top:440px;font-size:560px;font-weight:600;letter-spacing:-.07em;line-height:.9;color:#155dfc">14</div><div style="position:absolute;left:640px;top:720px;font-size:96px;font-weight:600;letter-spacing:-.045em;line-height:1;color:#10213b">dias<br>úteis.</div>' + rg + cap(["até", "14", "dias", "úteis."], 1)))
# 12 — 14,2s: régua completa, a tela acende "No ar"
F.append(("14,2s no ar", BG_ICE + ttl(["App no ar", "<em>em até 14 dias úteis.</em>"], eb=("Prazo", 2), size=84) + '<div class="rg" style="left:72px;top:520px;flex-wrap:wrap;width:940px;row-gap:12px;transform:scale(.6);transform-origin:0 0">' + "".join('<i class="on"></i>' for _ in range(14)) + "</div>" + stage(phone("translate3d(-40px,330px,-200px) rotateX(10deg) rotateY(-8deg) scale(.6)", wp="wp-loja", inner=grid + icon)) + '<div class="pill" style="left:560px;top:700px;transform:rotate(-4deg)">App no ar</div>' + cap(["dias", "úteis."], 1)))
# 13 — 15,2s: pushes chovem no celular
pushes = "".join(f'<div class="pz" style="left:{160 + dx}px;top:{y}px;transform:scale({s}) rotate({r}deg);opacity:{o}"><img src="assets/v2/icone-loja.svg"><div><b>Sua Loja</b><span>{t}</span></div><i>agora</i></div>' for dx, y, s, r, o, t in [(0, 640, .9, -2, 1, "Novidade pra você. Vem ver."), (10, 860, .86, 1.5, 1, "Seu cupom chegou."), (-10, 1070, .82, -1, 1, "Chegou a coleção nova."), (0, 1260, .78, 2, .55, "Só no app, hoje.")])
F.append(("15,2s push", BG_ICE + stage(phone("translate3d(0,520px,-700px) rotateX(18deg) scale(.8)", wp="wp-loja", inner=lock(nt=False))) + pushes + ttl(["Notificações push"], eb=("Push", 3)) + cap(["Notificações", "push"], 1)))
# 14 — 16,2s: ilimitadas — túnel de pushes sumindo no fundo
tun = "".join(f'<div class="pz" style="left:160px;top:960px;transform:translate3d(0,{-i*40}px,{-i*520}px) rotateX(8deg);opacity:{max(0.15, 1 - i*0.12)}"><img src="assets/v2/icone-loja.svg"><div><b>Sua Loja</b><span>Novidade pra você.</span></div><i>agora</i></div>' for i in range(9, -1, -1))
F.append(("16,2s ilimitadas", BG_ICE + f'<div class="st3" style="perspective-origin:540px 760px">{tun}</div>' + ttl(["Push", "<em>ilimitado.</em>"], eb=("Push", 3), size=120) + cap(["ilimitadas."], 0)))
# 15 — 18,2s: impacto, CTA; celular brilhando no azul com o push da loja
F.append(("18,2s CTA", BG_IMP + glow(540, 1100, 1200, 1200, "rgba(255,255,255,.18)") + stage(phone("translate3d(0,-40px,-300px) rotateX(16deg) rotateY(-16deg) rotateZ(6deg) scale(.44)", wp="wp-loja", inner=lock("loja"), glare="50%")) + ttl(["Sua loja na tela", "<em>do seu cliente.</em>"], dk=True) + '<div class="cta" style="position:absolute;left:50%;bottom:670px;transform:translateX(-50%);font-size:36px;padding:26px 38px;white-space:nowrap">Crie sua conta e veja seu app grátis <span>→</span></div>'))
# 16 — 21,0s: vinheta (kit)
F.append(("21,0s vinheta", BG_IMP + '<img class="logo-lg" src="assets/brand/logo/korza-logo-white.png" style="position:absolute;left:230px;top:820px">' + '<div class="cta" style="position:absolute;left:50%;bottom:670px;transform:translateX(-50%);font-size:36px;padding:26px 38px;white-space:nowrap">Crie sua conta e veja seu app grátis <span>→</span></div>'))

clips = "\n".join(f'<div id="q{i+1:02d}" class="clip q on-dark" data-start="{i}" data-duration="1" data-track-index="0" style="z-index:{i}">{h}</div>' for i, (lab, h) in enumerate(F))
html = f'''<!doctype html><html lang="pt-BR" data-resolution="portrait"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/brand/korza-video.css"><link rel="stylesheet" href="assets/v2/m1v2.css">
<style>@font-face{{font-family:"Plus Jakarta Sans";src:url("assets/brand/fonts/PlusJakartaSans-VariableFont_wght.ttf") format("truetype");font-weight:200 800}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;overflow:hidden;background:#fff}}
#root{{position:relative;width:100%;height:100%;overflow:hidden;font-family:"Plus Jakarta Sans",sans-serif}} .q{{position:absolute;inset:0;overflow:hidden}}</style></head>
<body><div id="root" data-composition-id="main" data-start="0" data-duration="{len(F)}" data-width="1080" data-height="1920">
{clips}
</div><script>const tl=gsap.timeline({{paused:true}});tl.set({{}},{{}},{len(F)});window.__timelines["main"]=tl;</script></body></html>'''
open("index.html", "w").write(html)
open("rotulos.txt", "w").write("\n".join(l for l, _ in F))
print(len(F), "quadros")
