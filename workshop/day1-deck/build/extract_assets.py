"""Save every picture in a .pptx as its own file, named by slide and position.

Usage: extract_assets.py <deck.pptx> <out-dir> <prefix>
Prints one line per picture: file, slide, position and size in inches, pixel size.
Identical pictures are saved once and reported with the first file's name.
"""
import hashlib
import io
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Emu


def walk(shapes):
    for shape in shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(shape.shapes)
        else:
            yield shape


def extract(deck, out_dir, prefix):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    seen = {}
    prs = Presentation(deck)
    for number, slide in enumerate(prs.slides, start=1):
        for index, shape in enumerate(walk(slide.shapes)):
            if shape.shape_type != MSO_SHAPE_TYPE.PICTURE:
                continue
            blob = shape.image.blob
            digest = hashlib.sha1(blob).hexdigest()
            if digest not in seen:
                name = f"{prefix}_s{number:02d}_{index:02d}.{shape.image.ext}"
                (out / name).write_bytes(blob)
                seen[digest] = name
            try:
                pixels = Image.open(io.BytesIO(blob)).size
            except Exception:
                pixels = ("?", "?")
            print(
                f"{seen[digest]:28s} slide {number:2d} "
                f"x={Emu(shape.left).inches:5.2f} y={Emu(shape.top).inches:5.2f} "
                f"w={Emu(shape.width).inches:5.2f} h={Emu(shape.height).inches:5.2f} "
                f"px={pixels[0]}x{pixels[1]}"
            )


if __name__ == "__main__":
    extract(*sys.argv[1:4])
