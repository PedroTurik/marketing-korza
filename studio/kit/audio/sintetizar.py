"""
Korza — áudio próprio do Studio (trilha e efeitos), sintetizado do zero em código.

Tudo aqui é gerado por este script: sem sample, loop ou música de terceiros. Por isso não há licença
de terceiros a cumprir, e a trilha pode ir em anúncio pago, Reels e qualquer canal.

  uv run --with numpy studio/kit/audio/sintetizar.py trilha  <saida.wav> --dur 22 [--entrada 4.6] [--fim 17]
  uv run --with numpy studio/kit/audio/sintetizar.py notif   <saida.wav>
  uv run --with numpy studio/kit/audio/sintetizar.py tick    <saida.wav>
  uv run --with numpy studio/kit/audio/sintetizar.py baque|toque|whoosh <saida.wav>   (M2: pilha, toque na tela, transição)

trilha: Fá maior, 96 BPM, Fmaj9 → Am7 → Dm9 → Bbmaj9 (1 compasso cada). Até --entrada só o pad (tensão do
gancho); de --entrada em diante entram arpejo, baixo e percussão leve; a partir de --fim a percussão sai e o
último acorde (Fmaj9) se resolve e some até --dur.
"""

import argparse
import wave

import numpy as np

SR = 48000
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
rng = np.random.default_rng(7)  # determinístico


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def env_adsr(n, a, r, sr=SR):
    e = np.ones(n)
    na, nr = int(a * sr), int(r * sr)
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):  # one-pole, simples e suave
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def reverb(x, secs=2.2, mix=0.28):
    n = int(secs * SR)
    t = np.arange(n) / SR
    ir = rng.standard_normal(n) * np.exp(-t * 3.2)
    ir = lowpass(ir, 5000)
    ir /= np.sqrt((ir**2).sum())
    size = 1 << int(np.ceil(np.log2(len(x) + n)))
    wet = np.fft.irfft(np.fft.rfft(x, size) * np.fft.rfft(ir, size), size)[: len(x)]
    return (1 - mix) * x + mix * wet * 0.9


def place(buf, sig, t0):
    i = int(t0 * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i]


# Fmaj9, Am7, Dm9, Bbmaj9 (voicings médios)
CHORDS = [
    {"root": 41, "pad": [53, 57, 60, 64, 67]},  # F: F A C E G
    {"root": 45, "pad": [52, 57, 60, 64, 67]},  # Am7: E A C E G
    {"root": 38, "pad": [53, 57, 60, 62, 64]},  # Dm9: F A C D E
    {"root": 46, "pad": [53, 57, 58, 62, 65]},  # Bbmaj9: F A Bb D F
]
ARP = [[65, 69, 72, 76], [64, 69, 72, 76], [62, 65, 69, 74], [62, 65, 70, 74]]


def pad_voice(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for det in (-0.12, 0.0, 0.12):  # chorus leve
        ff = f * 2 ** (det / 12 / 4)
        s += np.sin(2 * np.pi * ff * t) + 0.25 * np.sin(4 * np.pi * ff * t) + 0.08 * np.sin(6 * np.pi * ff * t)
    return s / 3 * env_adsr(n, 0.6, 0.9)


def pluck(f, dur=1.2, bright=0.5):
    # Karplus-Strong
    n = int(dur * SR)
    p = int(SR / f)
    buf = rng.uniform(-1, 1, p)
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = 0.996 * (bright * buf[i % p] + (1 - bright) * buf[(i + 1) % p])
    return out * env_adsr(n, 0.002, 0.3)


def bass(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.15 * np.sin(4 * np.pi * f * t)
    return s * np.exp(-t * 1.6) * env_adsr(n, 0.01, 0.08)


def kick():
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    f = 50 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def hat():
    n = int(0.05 * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    x = x - lowpass(x, 7000)  # passa-alta grosseiro
    return x * np.exp(-t * 90)


def trilha(dur, entrada, fim):
    n = int(dur * SR)
    padb, arpb, bassb, drb = (np.zeros(n) for _ in range(4))
    bars = int(np.ceil(dur / BAR)) + 1
    for b in range(bars):
        t0 = b * BAR
        if t0 >= dur:
            break
        last = t0 >= fim - 0.01 or t0 + BAR > dur
        ch = CHORDS[0] if t0 >= fim else CHORDS[b % 4]
        # pad
        for m in ch["pad"]:
            place(padb, pad_voice(hz(m), (dur - t0 + 0.5) if last else BAR + 0.6), t0)
        if t0 >= fim:
            break
        # arpejo em colcheias, só depois da entrada
        notes = ARP[b % 4]
        for k in range(8):
            tk = t0 + k * BEAT / 2
            if tk >= entrada and tk < fim:
                place(arpb, pluck(hz(notes[k % 4] + (12 if k in (3, 7) else 0)), 1.0, 0.45) * (0.9 if k % 2 == 0 else 0.6), tk)
        # baixo e percussão
        for k in range(4):
            tk = t0 + k * BEAT
            if entrada <= tk < fim:
                if k in (0, 2):
                    place(bassb, bass(hz(ch["root"]), BEAT * 2), tk)
                    place(drb, kick() * 0.9, tk)
                place(drb, hat() * 0.25, tk + BEAT / 2)
    # acorde final resolve (Fmaj9) a partir de "fim"
    pad = lowpass(padb, 1800) * 0.16
    arp = lowpass(arpb, 4200) * 0.22
    mix = pad + arp + bassb * 0.28 + drb * 0.32
    mix = reverb(mix)
    # entrada suave e saída
    e = np.ones(n)
    fi = int(0.4 * SR)
    e[:fi] = np.linspace(0, 1, fi)
    fo = int(min(1.5, dur * 0.2) * SR)
    e[-fo:] *= np.linspace(1, 0, fo) ** 1.5
    return mix * e


def notif():
    # dois toques de sino suaves (Mi6 → Lá6), genérico
    out = np.zeros(int(0.9 * SR))
    for t0, m, g in ((0.0, 88, 0.8), (0.11, 93, 1.0)):
        n = int(0.7 * SR)
        t = np.arange(n) / SR
        f = hz(m)
        s = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 18) + 0.15 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 30))
        s *= np.exp(-t * 7) * env_adsr(n, 0.002, 0.05) * g
        place(out, s, t0)
    return reverb(out, 0.8, 0.18)


def tick():
    n = int(0.12 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 1320 * t) * np.exp(-t * 60) + 0.4 * np.sin(2 * np.pi * 2640 * t) * np.exp(-t * 90)
    return s


def baque():
    # papel/cartão batendo na mesa: thump grave curto + estalo de ruído filtrado
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    f = 95 * np.exp(-t * 18) + 48
    thump = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 16)
    noise = lowpass(rng.standard_normal(n), 2600) * np.exp(-t * 45) * 0.9
    return reverb(thump + noise, 0.5, 0.12)


def toque():
    # toque de dedo na tela: clique suave e curto
    n = int(0.08 * SR)
    t = np.arange(n) / SR
    click = lowpass(rng.standard_normal(n), 5200) * np.exp(-t * 140)
    body = np.sin(2 * np.pi * 620 * t) * np.exp(-t * 90) * 0.5
    return click + body


def whoosh(dur=0.5):
    # sopro de transição: ruído com envelope em sino e filtro abrindo
    n = int(dur * SR)
    t = np.arange(n) / SR
    env = np.sin(np.pi * t / dur) ** 2
    a = lowpass(rng.standard_normal(n), 900)
    b = lowpass(rng.standard_normal(n), 4200)
    mixw = t / dur
    return (a * (1 - mixw) + b * mixw * 0.6) * env


def write(path, x):
    x = x / max(1e-9, np.abs(x).max()) * 0.89  # pico ~ -1 dBFS; loudness final é no mix
    pcm = (np.stack([x, x], 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tipo", choices=["trilha", "notif", "tick", "baque", "toque", "whoosh"])
    ap.add_argument("saida")
    ap.add_argument("--dur", type=float, default=22)
    ap.add_argument("--entrada", type=float, default=4.6)
    ap.add_argument("--fim", type=float, default=17.0)
    a = ap.parse_args()
    x = {"trilha": lambda: trilha(a.dur, a.entrada, a.fim), "notif": notif, "tick": tick, "baque": baque, "toque": toque, "whoosh": whoosh}[a.tipo]()
    write(a.saida, x)
    print(f"✓ {a.saida} ({len(x) / SR:.2f}s)")
