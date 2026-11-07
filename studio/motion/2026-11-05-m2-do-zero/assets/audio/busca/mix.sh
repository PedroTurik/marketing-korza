#!/usr/bin/env bash
# Mix da variação "busca": o mix do M2 (-v2, ../mix.sh) deslocado em H, com o gancho na frente → mix-busca.wav.
# Mesmo padrão: ducking pela voz, -14 LUFS / -1 dBTP, 48 kHz. Rode da pasta do projeto: bash assets/audio/busca/mix.sh
#   voz:    pergunta (vo-busca.mp3, Bea, mesmas configurações, -1 dB para casar com o início do vo.mp3) em 0s,
#           cortada em 3,30s; depois o vo.mp3 do M2 inteiro em H + 0,15 (sem regerar)
#   trilha: a mesma faixa, sem regerar. Antes dela entra 1,5 compasso do 1º compasso (meio + inteiro), no grid de
#           112 BPM, e a faixa do M2 segue no mesmo ponto do compasso, com a mesma edição e automação deslocadas em H
#   efeitos: os do M2 deslocados em H, + teclas.wav (gerar.py) + whoosh na saída da busca
set -euo pipefail
cd "$(dirname "$0")"
K=../../../../../kit/audio
B=2.142857        # 1 compasso
H=3.2             # gancho: 96 quadros (igual a gerar.py); a trilha usa 1,5 compasso = 3,2143s, cortado no início
DUR=$(python3 -c "print(round(25.25+$H,4))")
VO_AT=0.15        # do M2, relativo ao início do M2

ms() { python3 -c "print(str(int(round(($1)*48000)))+'S')"; }  # atraso em amostras (48 kHz): ms arredondado desalinha do M2
add() { python3 -c "print(round($1+$2,4))"; }

inputs=(-i vo-busca.mp3 -i ../vo.mp3 -i ../trilha-eleven.mp3)
# voz: pergunta + resposta numa faixa só (o sidechain vê as duas)
filt="[0:a]atrim=0:3.30,afade=t=out:st=3.24:d=0.06,volume=0.89,aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=$DUR[q];"
filt+="[1:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms "$H+$VO_AT")|$(ms "$H+$VO_AT"),apad=whole_dur=$DUR[a];"
filt+="[q][a]amix=inputs=2:normalize=0,asplit=2[vo][vosc];"
# trilha: [meio compasso 1][compasso 1] + trilha do M2 (mesmo corte de 1 compasso em 20s do ../mix.sh)
filt+="[2:a]asplit=4[t1][t2][t3][t4];"
# cada pedaço avança 0,03s além do fim do compasso: é o trecho que o acrossfade sobrepõe, então o grid não anda
filt+="[t1]atrim=start=$(python3 -c "print($B/2+1.5*$B-$H)"):end=$(add $B 0.03),asetpts=PTS-STARTPTS[i1];"
filt+="[t2]atrim=0:$(add $B 0.03),asetpts=PTS-STARTPTS[i2];"
filt+="[t3]atrim=0:20,asetpts=PTS-STARTPTS[m1];[t4]atrim=start=22.1429,asetpts=PTS-STARTPTS[m2];"
filt+="[i1][i2]acrossfade=d=0.03:c1=tri:c2=tri[i12];[i12][m1]acrossfade=d=0.03:c1=tri:c2=tri[im];[im][m2]acrossfade=d=0.04[mcut];"
filt+="[mcut]aresample=48000,aformat=channel_layouts=stereo,volume='0.30*(1-0.5*min(max((t-$(add 16.8 $H))/0.5\,0)\,1))':eval=frame,apad=whole_dur=$DUR[mus];"
filt+="[mus][vosc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=350[musd];"
mixin="[vo][musd]"; i=3

# efeitos: os do ../mix.sh (tempo do M2) + os do gancho (tempo absoluto, prefixo @)
SFX=(
  "baque 3.70 0.50"  "baque 5.60 0.50"  "baque 6.25 0.45"
  "baque 7.37 0.28"  "baque 7.61 0.26"  "baque 7.85 0.26"  "baque 8.09 0.24"  "baque 8.33 0.24"
  "whoosh 8.62 0.55"
  "toque 10.81 0.35" "toque 11.21 0.30" "tick 11.80 0.14" "toque 12.57 0.35"
  "notificacao 13.27 0.40"
  "whoosh 13.80 0.40"
  "tick 16.21 0.16"  "tick 16.90 0.16"  "tick 18.45 0.20"
  "whoosh 19.65 0.40"
  "@teclas 0 0.35"                                                               # digitação + Enter (3,08s)
  "@whoosh 3.18 0.35"                                                            # a busca sobe e revela o ato 1
)
for row in "${SFX[@]}"; do
  read -r f t v <<< "$row"
  if [[ $f == @* ]]; then f=${f#@}; else t=$(add "$t" "$H"); fi
  [[ $f == teclas ]] && inputs+=(-i teclas.wav) || inputs+=(-i "$K/$f.wav")
  filt+="[$i:a]aresample=48000,aformat=channel_layouts=stereo,adelay=$(ms "$t")|$(ms "$t"),volume=$v,apad=whole_dur=$DUR[s$i];"
  mixin+="[s$i]"; i=$((i + 1))
done
n=$(grep -o "\[" <<< "$mixin" | wc -l)
filt+="${mixin}amix=inputs=$n:normalize=0,atrim=0:$DUR,afade=t=out:st=$(python3 -c "print($DUR-0.8)"):d=0.8[pre]"

ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" -map "[pre]" -ar 48000 pre.wav

read -r I TP LRA THR OFF < <(ffmpeg -hide_banner -i pre.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 |
  python3 -c 'import sys,json,re; d=json.loads(re.search(r"\{.*\}", sys.stdin.read(), re.S).group()); print(d["input_i"], d["input_tp"], d["input_lra"], d["input_thresh"], d["target_offset"])')
ffmpeg -v error -y -i pre.wav -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$THR:offset=$OFF:linear=true" -ar 48000 mix-busca.wav
rm pre.wav
ffmpeg -hide_banner -i mix-busca.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | tr -s ' '
