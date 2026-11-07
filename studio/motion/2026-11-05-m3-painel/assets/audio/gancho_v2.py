"""M3 v2. Emenda o gancho novo ("Isso é o que você ganha quando lança o app da sua loja com a Korza.", Bea, take 2 de
vo-v2-gancho-{1,2,3}.mp3) no corpo da voz do v1 (vo-a-ed.wav), sem regerar o corpo.
O gancho novo dura 3,80s contra 2,85s do v1; com 0,35s de respiro (v1: 0,30s) o corpo anda exatamente D = 1,0s
(2 tempos da trilha a 120 BPM), então a trilha só ganha 2 tempos na abertura.
Saída: vo-v2-ed.wav e vo-v2-words.ed.json (tempos no vídeo). Rode: python3 assets/audio/gancho_v2.py"""
import json, subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
VO_AT, D = 0.15, 1.0
TAKE, JAN = "vo-v2-gancho-2", (0.12, 3.92)   # janela da fala (silencedetect -38 dB; o fim é o fim do arquivo)
CORPO_DE = 3.15                               # no vo-a-ed.wav: silêncio entre o gancho do v1 (fim 3,0) e "Escreva" (3,3)

def run(*a): subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)
run("-ss", f"{JAN[0]}", "-to", f"{JAN[1]}", "-i", f"{TAKE}.mp3", "-ar", "48000", "-ac", "2",
    "-af", "afade=t=in:d=0.008,areverse,afade=t=in:d=0.04,areverse", ".g.wav")
run("-ss", f"{CORPO_DE}", "-i", "vo-a-ed.wav", "-ar", "48000", "-ac", "2", ".c.wav")
a, c = int(VO_AT * 1000), int((CORPO_DE + D) * 1000)
run("-i", ".g.wav", "-i", ".c.wav", "-filter_complex",
    f"[0:a]adelay={a}|{a}[g];[1:a]adelay={c}|{c}[c];[g][c]amix=inputs=2:normalize=0[o]", "-map", "[o]", "-ar", "48000", "vo-v2-ed.wav")
os.remove(".g.wav"); os.remove(".c.wav")

g = [w for w in json.load(open(f"{TAKE}-words.json")) if not w["w"].startswith("[")]
a0, b0 = g[0]["s"], g[-1]["e"]; k = (JAN[1] - JAN[0]) / (b0 - a0)
hook = [{"w": w["w"], "s": round(VO_AT + (w["s"] - a0) * k, 3), "e": round(VO_AT + (w["e"] - a0) * k, 3)} for w in g]
corpo = [{"w": w["w"], "s": round(w["s"] + D, 3), "e": round(w["e"] + D, 3)} for w in json.load(open("vo-a-words.ed.json"))[11:]]
assert corpo[0]["w"] == "Escreva"
json.dump(hook + corpo, open("vo-v2-words.ed.json", "w"), ensure_ascii=False, indent=0)
print(f"gancho {hook[0]['s']}–{hook[-1]['e']} · corpo em {corpo[0]['s']} · fim da voz {corpo[-1]['e']}")
