#!/usr/bin/env bash
# Variantes do M3 a partir do index.html: 9:16 e 4:5 (versão única, gancho A, decisão do Pedro).
# O HyperFrames só aceita um HTML raiz por projeto: cada variante troca index.html e compositions/ temporariamente
# (o original volta ao fim, mesmo com erro). As cenas recebem a variante pela linha "VARIANTE" do s1-mundo.
#   bash build.sh check                  → npm run check nas 2 variantes
#   bash build.sh snap <tempos>           → snapshots em ${SNAPDIR:-/tmp/m3-snaps}/<variante>
#   bash build.sh render [--versao v2]    → 2 renders em renders/ (v2: gancho novo; os -v1 ficam)
set -euo pipefail
cd "$(dirname "$0")"
HF="npx --yes hyperframes@0.9.16"
CMD=${1:-check}; shift || true
V=v1; AT=""; SO="${SO:-}"
while [[ $# -gt 0 ]]; do case "$1" in --versao) V="$2"; shift 2 ;; *) AT="$1"; shift ;; esac; done
python3 assets/telas/montar.py >/dev/null
cp index.html .index.orig
rm -rf .comp.orig && cp -r compositions .comp.orig
trap 'mv -f .index.orig index.html; rm -rf compositions && mv .comp.orig compositions' EXIT

variant() { # fmt gancho(a|b)
  sed -e "s/data-fmt=\"reels\"/data-fmt=\"$1\"/" -e "s/data-gancho=\"a\"/data-gancho=\"$2\"/" .index.orig > index.html
  rm -rf compositions && cp -r .comp.orig compositions
  sed -i -e "s/const FMT = \"reels\", G = \"a\";/const FMT = \"$1\", G = \"$2\";/" compositions/s1-mundo.html
  if [[ $1 == feed ]]; then
    sed -i -e 's/data-height="1920"/data-height="1350"/' compositions/*.html
    sed -i -e 's/content="width=1080, height=1920"/content="width=1080, height=1350"/' \
      -e 's/data-height="1920"/data-height="1350"/g' -e 's/height: 1920px;/height: 1350px;/' \
      -e 's/--safe-top: 270px;/--safe-top: 64px;/' -e 's/--safe-bottom: 670px;/--safe-bottom: 64px;/' index.html
  fi
}

for row in "reels a 9x16" "feed a 4x5"; do
  read -r fmt g name <<< "$row"
  [[ -n $SO && $SO != *"$name"* ]] && continue
  variant "$fmt" "$g"
  echo "── $name"
  case $CMD in
    check) $HF check 2>&1 | grep -E "⚠|✗|ℹ|error\(s\)|passed|failed" | cut -c1-200 || true ;;
    snap) $HF snapshot --at "$AT" --no-end --describe false -o "${SNAPDIR:-/tmp/m3-snaps}/$name" 2>&1 | tail -1 | cut -c1-120 ;;
    render)
      out="renders/m3-painel-$name-$V.mp4"
      [[ -e $out ]] && { echo "Já existe: $out (use --versao)"; exit 1; }
      mkdir -p renders
      # Motion blur real: o filme roda 4x mais lento a 240 fps (= 960 amostras por segundo real) e cada quadro de 30 fps
      # funde 16 amostras (obturador de 1/60s). Com menos amostras os voos ficam estroboscópicos. O áudio volta aqui.
      # O intermediário fica fora do projeto, em ${TMPDIR:-/tmp}.
      python3 assets/telas/lento.py 4
      tmp="${TMPDIR:-/tmp}/m3-painel-$name-lento.mp4"
      $HF render --quality delivery --fps 240 -o "$tmp"
      ffmpeg -v error -y -i "$tmp" -i assets/audio/mix.wav -map 0:v -map 1:a -vf "tmix=frames=16,setpts=PTS/4,fps=30,format=yuv420p" -c:v libx264 -preset slow -crf 16 -profile:v high -movflags +faststart -c:a aac -b:a 192k -shortest "$out" ;;
  esac
done
