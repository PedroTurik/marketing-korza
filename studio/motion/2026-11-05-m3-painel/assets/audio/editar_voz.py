"""M3. Encurta os silêncios da voz sem regerar e monta as versões A e B com o corpo no mesmo tempo.
As janelas vêm de silencedetect (-38 dB): o alinhamento da ElevenLabs erra até 0,3s no início das frases, então os
tempos de cada palavra são reescalados para a janela real da frase.
Saída: vo-a-ed.wav, vo-b-ed.wav, vo-a-words.ed.json, vo-b-words.ed.json (tempos no vídeo). Rode: python3 assets/audio/editar_voz.py"""
import json, subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
VO_AT = 0.15
#          janela no vo-a.mp3   nº palavras  silêncio depois
FRASES = [((0.10, 2.95), 11, 0.30),   # Tudo que o app da sua loja faz, num painel só.
          ((3.51, 6.18), 8, 0.24),    # Escreva o push, escolha o destino e agende.
          ((6.80, 8.58), 7, 0.26),    # Cupom para a primeira compra no app.
          ((9.15, 11.03), 7, 0.26),   # Banner no site para baixar o app.
          ((11.58, 13.79), 5, 0.28),  # Boas-vindas automáticas para quem instala.
          ((14.52, 17.13), 9, 0.22),  # Vendas do app e do site, lado a lado.
          ((17.47, 21.37), 14, 0.36), # E um em cada três pedidos no app vem de quem já tinha comprado.
          ((22.07, 25.24), 8, 0.13),  # Transforme a sua recompra e fidelize seu cliente.
          ((25.37, 27.20), 6, 0.0)]   # Crie sua conta grátis na Korza.
GANCHO_B = (0.15, 3.00)
ws = [w for w in json.load(open("vo-a-words.json")) if not w["w"].startswith("[")]
hb = [w for w in json.load(open("vo-b-gancho-words.json")) if not w["w"].startswith("[")]
assert sum(f[1] for f in FRASES) == len(ws)

def corta(src, a, b, out):
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{a:.3f}","-to",f"{b:.3f}","-i",src,"-ar","48000","-ac","2",
                    "-af","afade=t=in:d=0.008,areverse,afade=t=in:d=0.02,areverse",out],check=True)
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
def reescala(pal, jan, t0, d):
    a0, b0 = pal[0]["s"], pal[-1]["e"]; k = d / (b0 - a0)
    return [{"w": p["w"], "s": round(t0 + (p["s"] - a0) * k, 3), "e": round(t0 + (p["e"] - a0) * k, 3)} for p in pal]

segs = []; i = 0
for jan, n, gap in FRASES:
    segs.append((jan, ws[i:i + n], gap)); i += n
corta("vo-a.mp3", *FRASES[0][0], ".ha.wav"); corta("vo-b-gancho.mp3", *GANCHO_B, ".hb.wav")
T = round(VO_AT + max(dur(".ha.wav"), dur(".hb.wav")) + FRASES[0][2], 3)  # início do corpo, igual em A e B
corpo, t = [], T; partes = []
for k, (jan, pal, gap) in enumerate(segs[1:]):
    f = f".c{k}.wav"; corta("vo-a.mp3", *jan, f); d = dur(f); partes.append((f, t))
    corpo += reescala(pal, jan, t, d); t += d + gap
FIM = t
for nome, g, pal, src_jan in (("a", ".ha.wav", segs[0][1], FRASES[0][0]), ("b", ".hb.wav", hb, GANCHO_B)):
    lista = [(g, VO_AT)] + partes
    inp, flt, mix = [], "", ""
    for j, (f, tt) in enumerate(lista):
        inp += ["-i", f]; ms = int(round(tt * 1000)); flt += f"[{j}:a]adelay={ms}|{ms}[p{j}];"; mix += f"[p{j}]"
    subprocess.run(["ffmpeg","-v","error","-y",*inp,"-filter_complex",flt+mix+f"amix=inputs={len(lista)}:normalize=0[o]","-map","[o]","-ar","48000",f"vo-{nome}-ed.wav"],check=True)
    json.dump(reescala(pal, src_jan, VO_AT, dur(g)) + corpo, open(f"vo-{nome}-words.ed.json","w"), ensure_ascii=False, indent=0)
for f in [".ha.wav", ".hb.wav"] + [p[0] for p in partes]: os.remove(f)
print(f"corpo em {T} · fim da voz {FIM:.2f}")
ini = 0
for (jan, n, gap), _ in zip(FRASES, range(9)):
    pass
for p in corpo: print(f'{p["s"]:6.2f} {p["w"]}')
