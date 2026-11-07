#!/usr/bin/env bash
# Variantes do M1 v2 a partir do index.html (9:16, gancho A): 9:16 e 4:5. Só o gancho A no v2 (o B ficou no v1).
# O HyperFrames só aceita um HTML raiz por projeto, então cada variante troca o index.html temporariamente
# (o original volta ao fim, mesmo com erro).
#   bash build.sh check                 → npm run check nas 4 variantes
#   bash build.sh snap <tempos>          → snapshots das 4 variantes em ${SNAPDIR:-/tmp/m1-snaps}/<variante>
#   bash build.sh render [--versao v1]   → 4 renders em renders/
set -euo pipefail
cd "$(dirname "$0")"
HF="npx --yes hyperframes@0.9.16"
CMD=${1:-check}; shift || true
V=v2; AT=""
while [[ $# -gt 0 ]]; do case "$1" in --versao) V="$2"; shift 2 ;; *) AT="$1"; shift ;; esac; done

cp index.html .index.orig
rm -rf .comp.orig && cp -r compositions .comp.orig
trap 'mv -f .index.orig index.html; rm -rf compositions && mv .comp.orig compositions' EXIT

variant() { # fmt gancho
  sed -e "s/data-fmt=\"reels\"/data-fmt=\"$1\"/" .index.orig > index.html
  rm -rf compositions && cp -r .comp.orig compositions
  if [[ $1 == feed ]]; then
    sed -i -e 's/data-height="1920"/data-height="1350"/' compositions/*.html
    sed -i -e 's/content="width=1080, height=1920"/content="width=1080, height=1350"/' \
      -e 's/data-height="1920"/data-height="1350"/g' -e 's/height: 1920px;/height: 1350px;/' \
      -e 's/--safe-top: 270px;/--safe-top: 64px;/' -e 's/--safe-bottom: 670px;/--safe-bottom: 64px;/' index.html
  fi
}

for row in "reels A a-9x16" "feed A a-4x5"; do
  read -r fmt g name <<< "$row"
  variant "$fmt" "$g"
  echo "── $name"
  case $CMD in
    check) $HF check 2>&1 | grep -E "⚠|✗|ℹ|error\(s\)|passed|failed" || true ;;
    snap) $HF snapshot --at "$AT" -o "${SNAPDIR:-/tmp/m1-snaps}/$name" 2>&1 | tail -2 ;;
    render)
      out="renders/m1-notificacao-$name-$V.mp4"
      [[ -e $out ]] && { echo "Já existe: $out (use --versao)"; exit 1; }
      mkdir -p renders
      $HF render --quality delivery --fps 30 -o "$out" ;;
  esac
done
