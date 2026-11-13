"""Build the combined Day 1 deck.

Usage: build_day1.py <billy.pptx> <assets-dir> <cache-dir> <out.pptx> [figures-dir]

Billy's exported deck is the base: its 26 slides are kept and everyone else's
slides are rebuilt around them in the same style, in the order of the proposal.
With a figures folder (see figures.py), the new Robi pictures replace the old ones.
"""
import sys

from pptx import Presentation

import billy
import payton
import raiyan
import yelina
from deckkit import Kit
from extras import break_slide, kahoot_placeholder, next_stop_map, wrap_up_placeholder


def build(base, assets_dir, cache_dir, out, figures_dir=None):
    presentation = Presentation(base)
    kit = Kit(presentation, assets_dir, cache_dir, figures_dir)
    kit.flatten_backgrounds()

    billy_slides = list(presentation.slides)
    billy.restyle(kit, billy_slides)
    swapped = kit.swap_pictures(billy_slides)
    print(f"new figures on Billy's own slides: {swapped}")
    teach_a_computer, make_with_ai = billy_slides[:15], billy_slides[15:]

    sections = [
        ("Stop 1 · Hello! (Yelina)", yelina.build(kit)),
        ("Stop 2 · Our week (Payton)", payton.build_week(kit)),
        ("Break", [break_slide(kit, 2)]),
        ("Stop 3 · Teach a computer (Billy)", [next_stop_map(kit, 3)] + teach_a_computer),
        ("Stop 4 · Quick, Draw! Race (Raiyan)", [next_stop_map(kit, 4)] + raiyan.build_quick_draw(kit)),
        ("Break", [break_slide(kit, 4)]),
        ("Stop 5 · Make with AI (Billy)", [next_stop_map(kit, 5)] + make_with_ai),
        ("Stop 6 · Is it AI? (Raiyan)", [next_stop_map(kit, 6)] + raiyan.build_is_it_ai(kit)),
        ("Break", [break_slide(kit, 6)]),
        ("Stop 7 · Monster, Guide or Buddy? (Payton)", [next_stop_map(kit, 7)] + payton.build_ethics(kit)),
        ("Stop 8 · Kahoot quiz (Raiyan)", [next_stop_map(kit, 8), kahoot_placeholder(kit)]),
        ("Stop 9 · Wrap-up (Yelina)", [next_stop_map(kit, 9), wrap_up_placeholder(kit)]),
    ]
    kit.reorder([slide for _name, slides in sections for slide in slides])
    presentation.save(out)

    first = 1
    for name, slides in sections:
        last = first + len(slides) - 1
        print(f"{first:3d}-{last:3d}  {name}  ({len(slides)} slides)")
        first = last + 1
    print(f"total: {first - 1} slides")


if __name__ == "__main__":
    build(*sys.argv[1:6])
