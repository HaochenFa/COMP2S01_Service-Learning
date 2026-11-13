"""Print the structure of a .pptx: size, fonts, layouts and each slide's shapes."""
import sys
from collections import Counter

from pptx import Presentation
from pptx.util import Emu


def describe(path, slide_numbers=None, detail=False):
    prs = Presentation(path)
    print(f"== {path}")
    print(f"size: {Emu(prs.slide_width).inches:.2f} x {Emu(prs.slide_height).inches:.2f} in")
    for master in prs.slide_masters:
        print("master:", master.name, "| layouts:", [layout.name for layout in master.slide_layouts])

    fonts = Counter()
    for index, slide in enumerate(prs.slides, start=1):
        wanted = slide_numbers is None or index in slide_numbers
        if wanted:
            print(f"\n--- slide {index} (layout: {slide.slide_layout.name}) shapes: {len(slide.shapes)}")
        for shape in slide.shapes:
            text = ""
            if shape.has_text_frame:
                text = shape.text_frame.text.replace("\n", " / ")[:70]
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if run.font.name:
                            fonts[(run.font.name, run.font.size.pt if run.font.size else None)] += 1
            if wanted and detail:
                print(
                    f"  [{shape.shape_type}] {shape.name!r} "
                    f"x={Emu(shape.left or 0).inches:.2f} y={Emu(shape.top or 0).inches:.2f} "
                    f"w={Emu(shape.width or 0).inches:.2f} h={Emu(shape.height or 0).inches:.2f} "
                    f"{text!r}"
                )
    print("\nfonts (name, pt) -> runs:")
    for (name, size), count in fonts.most_common(25):
        print(f"  {name} {size}: {count}")


if __name__ == "__main__":
    deck = sys.argv[1]
    numbers = {int(n) for n in sys.argv[2].split(",")} if len(sys.argv) > 2 and sys.argv[2] else None
    describe(deck, numbers, detail=len(sys.argv) > 2)
