"""M2 busca. Gera a voz (Bea, padrão M1) com tempos por palavra. Custa crédito e muda a leitura: só rode para regerar.
Uso: set -a; . ~/.config/korza-marketing/elevenlabs.env; set +a; python3 assets/audio/gerar_voz.py <nome> "<texto>"
Saída: <nome>.mp3 e <nome>-words.json nesta pasta."""
import base64, json, os, sys, urllib.request
nome, texto = sys.argv[1], sys.argv[2]
aqui = os.path.dirname(os.path.abspath(__file__))
req = urllib.request.Request(
    "https://api.elevenlabs.io/v1/text-to-speech/cabLxBh81HurPAAJfEHo/with-timestamps?output_format=mp3_44100_128",
    data=json.dumps({"text": texto, "model_id": "eleven_v3", "language_code": "pt",
                     "voice_settings": {"stability": 0.5, "speed": 1.05}}).encode(),
    headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
d = json.load(urllib.request.urlopen(req, timeout=120))
open(f"{aqui}/{nome}.mp3", "wb").write(base64.b64decode(d["audio_base64"]))
a = d.get("normalized_alignment") or d["alignment"]
words, cur = [], None
for c, s, e in zip(a["characters"], a["character_start_times_seconds"], a["character_end_times_seconds"]):
    if c.isspace():
        if cur: words.append(cur); cur = None
    elif cur is None: cur = {"w": c, "s": s, "e": e}
    else: cur["w"] += c; cur["e"] = e
if cur: words.append(cur)
json.dump(words, open(f"{aqui}/{nome}-words.json", "w"), ensure_ascii=False, indent=0)
print(nome, "palavras:", len(words), "fim:", words[-1]["e"])
for w in words: print(f'{w["s"]:6.2f} {w["w"]}')
