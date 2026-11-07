#!/usr/bin/env bash
# Variantes do M2 a partir do index.html (9:16): 9:16 e 4:5 (versão única, gancho A).
# O HyperFrames só aceita um HTML raiz por projeto, então cada variante troca o index.html temporariamente
# (o original volta ao fim, mesmo com erro).
#   bash build.sh check                 → npm run check nas 2 variantes
#   bash build.sh snap <tempos>          → snapshots das 4 variantes em /tmp/m2-snaps/<variante>
#   bash build.sh render [--versao v1]   → 2 renders em renders/
#   --gancho busca                       → variação com o gancho de busca (assets/audio/busca/): o index.html do M2
#                                          deslocado por variante.py; renders m2-do-zero-busca-<formato>-vN.mp4
set -euo pipefail
cd "$(dirname "$0")"
HF="npx --yes hyperframes@0.9.16"
CMD=${1:-check}; shift || true
V=v1; AT=""; GANCHO=""
while [[ $# -gt 0 ]]; do case "$1" in --versao) V="$2"; shift 2 ;; --gancho) GANCHO="$2"; shift 2 ;; *) AT="$1"; shift ;; esac; done

cp index.html .index.orig
if [[ $GANCHO == busca ]]; then python3 assets/audio/busca/variante.py .index.orig > .index.src; else cp .index.orig .index.src; fi
rm -rf .comp.orig && cp -r compositions .comp.orig
trap 'mv -f .index.orig index.html; rm -f .index.src; rm -rf compositions && mv .comp.orig compositions' EXIT

variant() { # fmt gancho
  sed -e "s/data-fmt=\"reels\"/data-fmt=\"$1\"/" .index.src > index.html
  rm -rf compositions && cp -r .comp.orig compositions
  if [[ $1 == feed ]]; then
    sed -i -e 's/data-height="1920"/data-height="1350"/' compositions/*.html
    sed -i -e 's/content="width=1080, height=1920"/content="width=1080, height=1350"/' \
      -e 's/data-height="1920"/data-height="1350"/g' -e 's/height: 1920px;/height: 1350px;/' \
      -e 's/--safe-top: 270px;/--safe-top: 64px;/' -e 's/--safe-bottom: 670px;/--safe-bottom: 64px;/' index.html
  fi
}

for row in "reels A 9x16" "feed A 4x5"; do
  read -r fmt g name <<< "$row"
  variant "$fmt" "$g"
  echo "── $name"
  case $CMD in
    check) $HF check 2>&1 | grep -E "⚠|✗|ℹ|error\(s\)|passed|failed" || true ;;
    snap) $HF snapshot --at "$AT" -o "${SNAPDIR:-/tmp/m2-snaps}/${GANCHO:+$GANCHO-}$name" 2>&1 | tail -2 ;;
    render)
      out="renders/m2-do-zero-${GANCHO:+$GANCHO-}$name-$V.mp4"
      [[ -e $out ]] && { echo "Já existe: $out (use --versao)"; exit 1; }
      mkdir -p renders
      $HF render --quality delivery --fps 30 -o "$out" ;;
  esac
done
