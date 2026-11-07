#!/usr/bin/env bash
# Mix final do M1 v2: voz (v1, sem regerar) + trilha Eleven Music (ducking pela voz) + efeitos do kit → mix.wav,
# -14 LUFS / -1 dBTP, 48 kHz. Rode da pasta do projeto: bash assets/audio/mix.sh
# Trilha: trilha-eleven.mp3 (prompt em trilha-prompt.json), 120 BPM exatos. A faixa veio com intro de 0–8s, groove de 8–18s
# e decaimento de 18–20s. Sem regerar: lê a partir de 3,38s (o groove cai em 4,62s, no "Com a Korza") e, em 18s da faixa,
# volta para 12s (3 compassos repetidos, emenda no compasso): o groove termina em 20,6s, na vinheta, e soa até o fim.
set -euo pipefail
cd "$(dirname "$0")"
K=../../../../kit/audio
DUR=22.5
VO_AT=1.0

ms() { python3 -c "print(int(round($1*1000)))"; }

inputs=(-i vo.mp3 -i trilha-eleven.mp3)
filt="[0:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms $VO_AT)|$(ms $VO_AT),apad=whole_dur=$DUR,asplit=2[vo][vosc];"
filt+="[1:a]atrim=start=3.38:end=18,asetpts=PTS-STARTPTS[m1];[1:a]atrim=start=12,asetpts=PTS-STARTPTS[m2];[m1][m2]acrossfade=d=0.03[mcut];"
filt+="[mcut]aresample=48000,aformat=channel_layouts=stereo,volume=0.30,apad=whole_dur=$DUR[mus];"
filt+="[mus][vosc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=350[musd];"
mixin="[vo][musd]"; i=2

# efeito  tempo(s)  volume  (tempos = cenas em compositions/)
SFX=(
  "notificacao 0.03 0.55"                                                         # gancho: "Amor" chega
  "tick 2.52 0.10"                                                                # "né?": sublinhado
  "whoosh 3.18 0.28"                                                              # virada: o cartão troca
  "notificacao 4.00 0.18" "notificacao 4.14 0.15" "notificacao 4.28 0.13"         # campo de celulares acende
  "whoosh 4.47 0.50"                                                              # chicote → cena 2
  "baque 6.80 0.30"                                                               # ícone da loja cai
  "notificacao 7.70 0.35"                                                         # push da loja chega
  "whoosh 7.98 0.28"                                                              # push salta para fora
  "whoosh 8.74 0.42"                                                              # mergulho → plataformas
  "baque 9.88 0.45" "baque 10.74 0.45"                                            # Nuvemshop, Shopify
  "whoosh 11.40 0.45"                                                             # chicote → prazo
  "tick 13.06 0.22" "baque 14.03 0.32"                                            # "14", selo "App no ar"
  "whoosh 14.22 0.40"                                                             # chicote para cima → push
  "notificacao 14.56 0.28" "notificacao 14.92 0.24" "notificacao 15.20 0.20"      # chuva de pushes
  "tick 15.40 0.12" "tick 15.56 0.11" "tick 15.68 0.10" "tick 15.78 0.09" "tick 15.86 0.08"
  "whoosh 15.95 0.32"                                                             # túnel
  "whoosh 16.66 0.50"                                                             # push voa na câmera
)
for row in "${SFX[@]}"; do
  read -r f t v <<< "$row"
  inputs+=(-i "$K/$f.wav")
  filt+="[$i:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms $t)|$(ms $t),volume=$v,apad=whole_dur=$DUR[s$i];"
  mixin+="[s$i]"; i=$((i + 1))
done
n=$(grep -o "\[" <<< "$mixin" | wc -l)
filt+="${mixin}amix=inputs=$n:normalize=0,atrim=0:$DUR,afade=t=out:st=$(python3 -c "print($DUR-0.8)"):d=0.8[pre]"

ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" -map "[pre]" -ar 48000 pre.wav

# loudnorm em duas passadas
read -r I TP LRA THR OFF < <(ffmpeg -hide_banner -i pre.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 |
  python3 -c 'import sys,json,re; d=json.loads(re.search(r"\{.*\}", sys.stdin.read(), re.S).group()); print(d["input_i"], d["input_tp"], d["input_lra"], d["input_thresh"], d["target_offset"])')
ffmpeg -v error -y -i pre.wav -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$THR:offset=$OFF:linear=true" -ar 48000 mix.wav
rm pre.wav
ffmpeg -hide_banner -i mix.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' '
