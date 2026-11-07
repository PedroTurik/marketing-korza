#!/usr/bin/env bash
# Mix final do M3: voz + trilha Eleven Music reconstruída (ducking pela voz) + efeitos → mix.wav, -14 LUFS / -1 dBTP, 48 kHz.
# Rode da pasta do projeto: bash assets/audio/mix.sh
# v2 (gancho novo): voz vo-v2-ed.wav, 1,0s mais longa no gancho. A trilha ganha 2 tempos no começo (repete [0,035–1,035], pulso
# estável da abertura) e todo efeito e automação a partir do colapso (1,87s no v1) anda D = 1,0s. v1: D=0 e vo-a-ed.wav.
# Trilha (120 BPM exatos, grid em 0,035+0,5n): a seção forte veio em 16s e morre em 24s. Reconstrução no grid:
#   [0–8,035] + repete [4,035–8,035] (2 compassos) + [8,035–22,035] + [23,035–fim] → clímax em 19,97s (com início -0,065s), acorde final na vinheta.
set -euo pipefail
cd "$(dirname "$0")"
K=../../../../kit/audio
D=1.0
VO=vo-v2-ed.wav
DUR=$(python3 -c "print(26.8+$D)")
ms() { python3 -c "print(int(round($1*1000)))"; }

# 1. Trilha reconstruída
ffmpeg -v error -y -i trilha-eleven.mp3 -filter_complex "
[0:a]aresample=48000,asplit=5[ax][a0][a1][a2][a3];
[ax]atrim=0:1.035,asetpts=PTS-STARTPTS,afade=t=out:st=1.03:d=0.005[sx];
[a0]atrim=0.035:8.035,asetpts=PTS-STARTPTS,afade=t=in:d=0.005,asetpts=PTS-STARTPTS,afade=t=out:st=8.03:d=0.005[s0];
[a1]atrim=4.035:8.035,asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st=3.995:d=0.005[s1];
[a2]atrim=8.035:22.035,asetpts=PTS-STARTPTS,afade=t=in:d=0.005,afade=t=out:st=13.995:d=0.005[s2];
[a3]atrim=23.035,asetpts=PTS-STARTPTS,afade=t=in:d=0.005[s3];
[sx][s0][s1][s2][s3]concat=n=5:v=0:a=1,atrim=0.065,asetpts=PTS-STARTPTS[o]" -map "[o]" trilha-montada.wav

# 2. Ganho: 0–20s é baixo no original (RMS 0,08), 20s+ é alto (0,26)
G0=$(python3 -c "print(19.92+$D)")
GAN="if(lt(t,$G0),0.62,if(lt(t,$G0+0.1),0.62-(t-$G0)*4.4,0.18))"

# 3. Efeitos: tempo, arquivo, volume
FX=(
  "1.87 baque 0.28" "2.72 whoosh 0.34"
  "3.38 tick 0.10" "3.7 tick 0.08" "4.03 tick 0.08"
  "4.8 toque 0.5" "5.38 toque 0.5"
  "5.54 whoosh 0.22" "5.74 notificacao 0.42"
  "6.42 whoosh 0.3" "7.34 toque 0.5" "7.42 tick 0.2"
  "8.18 whoosh 0.3" "9.5 toque 0.5"
  "9.92 whoosh 0.34" "10.72 tick 0.2" "11.76 notificacao 0.42"
  "12.56 whoosh 0.32" "14.14 whoosh 0.18" "14.5 tick 0.2" "14.72 tick 0.2"
  "15.5 whoosh 0.24" "15.72 baque 0.22" "16.57 tick 0.22"
  "19.62 whoosh 0.36" "24.6 baque 0.34"
)
inputs=(-i $VO -i trilha-montada.wav)
filt="[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=$DUR,asplit=2[vo][vosc];"
filt+="[1:a]aformat=channel_layouts=stereo,volume='$GAN':eval=frame,apad=whole_dur=$DUR[mus];"
filt+="[mus][vosc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[musd];"
mixin="[vo][musd]"; i=2
for row in "${FX[@]}"; do
  read -r t f v <<< "$row"
  t=$(python3 -c "print($t+$D if $t>=1.85 else $t)")
  inputs+=(-i "$K/$f.wav")
  filt+="[$i:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms $t)|$(ms $t),volume=$v,apad=whole_dur=$DUR[x$i];"
  mixin+="[x$i]"; i=$((i + 1))
done
filt+="${mixin}amix=inputs=$i:normalize=0,atrim=0:$DUR,afade=t=out:st=$(python3 -c "print($DUR-0.35)"):d=0.35[pre]"
ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" -map "[pre]" -ar 48000 pre.wav

# 4. loudnorm em duas passadas
read -r I TP LRA THR OFF < <(ffmpeg -hide_banner -i pre.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 |
  python3 -c 'import sys,json,re; d=json.loads(re.search(r"\{.*\}", sys.stdin.read(), re.S).group()); print(d["input_i"], d["input_tp"], d["input_lra"], d["input_thresh"], d["target_offset"])')
ffmpeg -v error -y -i pre.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$THR:offset=$OFF:linear=true" -ar 48000 mix.wav
rm pre.wav trilha-montada.wav
ffmpeg -hide_banner -i mix.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' '
python3 - <<'P'
import subprocess, struct, math
raw=subprocess.check_output(['ffmpeg','-v','error','-i','mix.wav','-ac','1','-ar','8000','-f','s16le','-'])
n=len(raw)//2; s=struct.unpack(f'<{n}h',raw)
print('RMS/s:',' '.join(f"{math.sqrt(sum(x*x for x in s[i:i+8000])/max(1,len(s[i:i+8000])))/32768:.2f}" for i in range(0,n,8000)))
P
