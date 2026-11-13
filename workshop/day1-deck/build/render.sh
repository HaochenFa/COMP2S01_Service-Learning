#!/bin/zsh
# Render a .pptx to PDF with LibreOffice (headless), then to one PNG per slide.
# PowerPoint can't be scripted from here: macOS blocks access to its sandbox folder.
# Usage: render.sh <deck.pptx> <out-dir> [dpi]
set -euo pipefail

deck="${1:A}"
out="${2:A}"
dpi="${3:-60}"
name="${deck:t:r}"
profile="${out:h}/lo-profile"

mkdir -p "$out"
rm -f "$out/$name.pdf" "$out/$name"-*.png(N)
/Applications/LibreOffice.app/Contents/MacOS/soffice \
  -env:UserInstallation="file://$profile" \
  --headless --convert-to pdf --outdir "$out" "$deck" >/dev/null 2>&1
pdftoppm -r "$dpi" -png "$out/$name.pdf" "$out/$name"
ls "$out" | grep -c "^$name-.*png$"
