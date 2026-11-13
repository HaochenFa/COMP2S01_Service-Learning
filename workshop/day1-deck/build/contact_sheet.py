"""Tile slide PNGs into numbered contact sheets so many slides can be checked at once.

Usage: contact_sheet.py <png-dir> <prefix> <out-prefix> [columns] [tile-width] [per-sheet]
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw


def build(png_dir, prefix, out_prefix, columns=4, tile_width=480, per_sheet=12):
    files = sorted(Path(png_dir).glob(f"{prefix}-*.png"))
    sheets = []
    for start in range(0, len(files), per_sheet):
        chunk = files[start:start + per_sheet]
        tiles = []
        for path in chunk:
            image = Image.open(path).convert("RGB")
            height = round(image.height * tile_width / image.width)
            tiles.append((path, image.resize((tile_width, height))))
        tile_height = max(tile.height for _, tile in tiles)
        rows = -(-len(tiles) // columns)
        gap = 8
        sheet = Image.new(
            "RGB",
            (columns * (tile_width + gap) + gap, rows * (tile_height + gap) + gap),
            "#888888",
        )
        draw = ImageDraw.Draw(sheet)
        for index, (path, tile) in enumerate(tiles):
            x = gap + (index % columns) * (tile_width + gap)
            y = gap + (index // columns) * (tile_height + gap)
            sheet.paste(tile, (x, y))
            label = path.stem.rsplit("-", 1)[-1]
            draw.rectangle([x, y, x + 34, y + 18], fill="#000000")
            draw.text((x + 5, y + 3), label, fill="#ffffff")
        out = f"{out_prefix}-{start // per_sheet + 1}.png"
        sheet.save(out)
        sheets.append(out)
    return sheets


if __name__ == "__main__":
    args = sys.argv[1:]
    numbers = [int(value) for value in args[3:]]
    for sheet in build(args[0], args[1], args[2], *numbers):
        print(sheet)
