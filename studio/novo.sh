#!/usr/bin/env bash
# Cria um projeto de vídeo (HyperFrames) a partir de studio/template.
#
#   studio/novo.sh <motion|gravados> <slug> [--format reels|stories|feed|square]
#
#   reels   1080×1920 (padrão) — texto entre y 270 e 1250
#   stories 1080×1920          — texto entre y 270 e 1540
#   feed    1080×1350 (4:5)
#   square  1080×1080
#
# Resultado: studio/<tipo>/AAAA-MM-DD-<slug>/ com index.html, frame.md e assets/brand/ (cópia da marca:
# o preview/render só enxerga arquivos dentro do projeto).
set -euo pipefail

STUDIO="$(cd "$(dirname "$0")" && pwd)"
MARCA="$STUDIO/../contexto/marca"
TIPO="${1:-}"
SLUG="${2:-}"
FORMAT="reels"
shift 2 || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --format) FORMAT="$2"; shift 2 ;;
    --format=*) FORMAT="${1#*=}"; shift ;;
    *) echo "Opção desconhecida: $1" >&2; exit 1 ;;
  esac
done

if [[ "$TIPO" != "motion" && "$TIPO" != "gravados" ]] || [[ -z "$SLUG" || ! "$SLUG" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "Uso: studio/novo.sh <motion|gravados> <slug-em-kebab-case> [--format reels|stories|feed|square]" >&2
  exit 1
fi

case "$FORMAT" in
  reels)   W=1080; H=1920; RES=portrait; SAFE_TOP=270; SAFE_BOTTOM=670 ;;
  stories) W=1080; H=1920; RES=portrait; SAFE_TOP=270; SAFE_BOTTOM=380 ;;
  feed)    W=1080; H=1350; RES=portrait; SAFE_TOP=64;  SAFE_BOTTOM=120 ;;
  square)  W=1080; H=1080; RES=square;   SAFE_TOP=64;  SAFE_BOTTOM=64 ;;
  *) echo "Formato inválido: $FORMAT" >&2; exit 1 ;;
esac

NAME="$(date +%Y-%m-%d)-$SLUG"
DEST="$STUDIO/$TIPO/$NAME"
if [[ -e "$DEST" ]]; then
  echo "Já existe: studio/$TIPO/$NAME" >&2
  exit 1
fi

cp -r "$STUDIO/template" "$DEST"
cp "$STUDIO/frame.md" "$DEST/frame.md"

mkdir -p "$DEST/assets/brand" "$DEST/assets/footage" "$DEST/assets/audio"
cp -r "$MARCA/logo" "$MARCA/fonts" "$MARCA/graphics" "$MARCA/site-assets" "$DEST/assets/brand/"
cp "$STUDIO/kit/korza-video.css" "$DEST/assets/brand/"

f="$DEST/index.html"
sed -i \
  -e "s/data-resolution=\"[a-z]*\"/data-resolution=\"$RES\"/" \
  -e "s/content=\"width=1080, height=1920\"/content=\"width=$W, height=$H\"/" \
  -e "s/data-width=\"1080\"/data-width=\"$W\"/g" \
  -e "s/data-height=\"1920\"/data-height=\"$H\"/g" \
  -e "s/height: 1920px;/height: ${H}px;/" \
  -e "s/--safe-top: 270px;/--safe-top: ${SAFE_TOP}px;/" \
  -e "s/--safe-bottom: 670px;/--safe-bottom: ${SAFE_BOTTOM}px;/" \
  "$f"
sed -i -e "s/data-width=\"1080\"/data-width=\"$W\"/" -e "s/data-height=\"1920\"/data-height=\"$H\"/" "$DEST"/compositions/*.html

python3 - "$DEST" "$NAME" "$TIPO" "$FORMAT" <<'PY'
import json, sys, datetime, pathlib
dest, name, tipo, fmt = pathlib.Path(sys.argv[1]), *sys.argv[2:]
meta = {"id": name, "name": name, "tipo": tipo, "format": fmt,
        "createdAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}
(dest / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
pkg = json.loads((dest / "package.json").read_text())
pkg["name"] = name
(dest / "package.json").write_text(json.dumps(pkg, indent=2) + "\n")
PY

echo "✓ Criado studio/$TIPO/$NAME ($FORMAT, ${W}×${H})"
echo "  Próximo: cd studio/$TIPO/$NAME && npm run check"
