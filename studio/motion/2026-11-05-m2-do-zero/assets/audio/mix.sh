#!/usr/bin/env bash
# Mix final do M2: voz + trilha Eleven Music (ducking pela voz) + efeitos → mix.wav, -14 LUFS / -1 dBTP, 48 kHz.
# Rode da pasta do projeto: bash assets/audio/mix.sh
# Trilha: trilha-eleven.mp3 (Eleven Music, prompt em trilha-prompt.json). A 3ª seção (17s+) veio ~3x mais alta:
# o ganho cai pela metade a partir de 16,8s. Sem a trilha, o mix sai só com voz e efeitos.
set -euo pipefail
cd "$(dirname "$0")"
K=../../../../kit/audio
DUR=25.25
VO_AT=0.15

ms() { python3 -c "print(int(round($1*1000)))"; }

inputs=(-i vo.mp3)
filt="[0:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms $VO_AT)|$(ms $VO_AT),apad=whole_dur=$DUR,asplit=2[vo][vosc];"
mixin="[vo]"; i=1
if [[ -f trilha-eleven.mp3 ]]; then
  inputs+=(-i trilha-eleven.mp3)
  # corta 1 compasso (4 tempos a 112 BPM = 2,1429s) em 20s: o vídeo perdeu 2,15s ("Sem conta de desenvolvedor")
  # e a trilha mantém o acorde final no fim
  filt+="[1:a]atrim=0:20,asetpts=PTS-STARTPTS[m1];[1:a]atrim=start=22.1429,asetpts=PTS-STARTPTS[m2];[m1][m2]acrossfade=d=0.04[mcut];"
  filt+="[mcut]aresample=48000,aformat=channel_layouts=stereo,volume='0.30*(1-0.5*min(max((t-16.8)/0.5\,0)\,1))':eval=frame,apad=whole_dur=$DUR[mus];"
  filt+="[mus][vosc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=350[musd];"
  mixin+="[musd]"; i=2
else
  filt+="[vosc]anullsink;"
fi

# efeito  tempo(s)  volume
SFX=(
  "baque 3.70 0.50"  "baque 5.60 0.50"  "baque 6.25 0.45"                       # calendário, contas
  "baque 7.37 0.28"  "baque 7.61 0.26"  "baque 7.85 0.26"  "baque 8.09 0.24"  "baque 8.33 0.24"  # status
  "whoosh 8.62 0.55"                                                             # pilha cai, cortina branca
  "toque 10.81 0.35" "toque 11.21 0.30" "tick 11.80 0.14" "toque 12.57 0.35"    # onboarding
  "notificacao 13.27 0.40"                                                       # push de teste
  "whoosh 13.80 0.40"                                                            # apps sobem
  "tick 16.21 0.16"  "tick 16.90 0.16"  "tick 18.45 0.20"                        # iOS, Android, 14
  "whoosh 19.65 0.40"                                                            # wipe azul → CTA
)
for row in "${SFX[@]}"; do
  read -r f t v <<< "$row"
  inputs+=(-i "$K/$f.wav")
  filt+="[$i:a]aresample=48000,adelay=$(ms $t)|$(ms $t),volume=$v,apad=whole_dur=$DUR[s$i];"
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
