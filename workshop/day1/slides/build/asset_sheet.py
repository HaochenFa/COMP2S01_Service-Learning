"""Tile every image in a folder onto labelled sheets (grey backing shows white icons).

Usage: asset_sheet.py <image-dir> <out-prefix> [columns] [cell] [per-sheet]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw


def build(image_dir, out_prefix, columns=8, cell=150, per_sheet=48):
    files = sorted(
        path for path in Path(image_dir).iterdir()
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif"}
    )
    label_height = 16
    for start in range(0, len(files), per_sheet):
        chunk = files[start:start + per_sheet]
        rows = -(-len(chunk) // columns)
        sheet = Image.new("RGB", (columns * cell, rows * (cell + label_height)), "#7a8794")
        draw = ImageDraw.Draw(sheet)
        for index, path in enumerate(chunk):
            image = Image.open(path)
            image = image.convert("RGBA")
            image.thumbnail((cell - 8, cell - 8))
            x = (index % columns) * cell + (cell - image.width) // 2
            y = (index // columns) * (cell + label_height) + (cell - image.height) // 2
            sheet.paste(image, (x, y), image)
            draw.text(
                ((index % columns) * cell + 3, (index // columns) * (cell + label_height) + cell),
                path.stem,
                fill="#ffffff",
            )
        out = f"{out_prefix}-{start // per_sheet + 1}.png"
        sheet.save(out)
        print(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    build(args[0], args[1], *[int(value) for value in args[2:]])
