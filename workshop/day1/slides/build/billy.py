"""Changes made to the slides that come straight from "Taming_AI_Day1_Billy".

Those slides keep their layout and wording. This module only turns the dark
(navy) ones into bright ones and repaints their text so it stays readable.
"""
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches

from deckkit import BLUE, GREEN, INK, LAYOUT_FILL, MUTED, NAVY, ORANGE, WHITE, YELLOW

FAINT = "7A829C"


def _run_colors(shape):
    """Every colour element set directly on a text run of this shape."""
    for properties in shape._element.iter(qn("a:rPr")):
        fill = properties.find(qn("a:solidFill"))
        if fill is not None and fill.find(qn("a:srgbClr")) is not None:
            yield fill.find(qn("a:srgbClr"))


def _shape_fill(shape):
    properties = shape._element.find(qn("p:spPr"))
    if properties is None:
        return None
    fill = properties.find(qn("a:solidFill"))
    return None if fill is None else fill.find(qn("a:srgbClr"))


def lighten(kit, slide, pill_color, accent, background="PAPER"):
    """Turn a navy slide into a bright one.

    The stop pill goes back to its section colour, white text becomes ink, and the
    yellow highlight becomes `accent`. Text that sits on a coloured shape (the
    action tag, pills) is left alone.
    """
    kit.set_background(slide, LAYOUT_FILL[background])
    swaps = {WHITE: INK, YELLOW: accent, "C9D2E8": MUTED, "8F9BBE": FAINT}
    for index, shape in enumerate(slide.shapes):
        if not shape.has_text_frame:
            continue
        fill = _shape_fill(shape)
        if index == 0 and fill is not None and fill.get("val") == YELLOW:
            fill.set("val", pill_color)
            for color in _run_colors(shape):
                color.set("val", WHITE)
            continue
        on_action_tag = Emu(shape.top).inches < 0.9 and Emu(shape.left).inches > 10
        if fill is not None or on_action_tag:
            continue
        for color in _run_colors(shape):
            if color.get("val") in swaps:
                color.set("val", swaps[color.get("val")])


def _shape_with_text(slide, text):
    for shape in slide.shapes:
        if shape.has_text_frame and shape.text_frame.text.strip() == text:
            return shape
    raise LookupError(f"no shape with the text {text!r}")


def _set_text(shape, text):
    """Change a one-run label's words and keep its formatting."""
    runs = shape.text_frame.paragraphs[0].runs
    runs[0].text = text
    for extra in runs[1:]:
        extra.text = ""


def restyle(kit, slides):
    """Apply the merge's changes to Billy's 26 slides (passed in their original order).

    Bright instead of navy: slide 4 (the intro video), 14 and 26. Slide 10, the Monster
    moment, stays dark on purpose. Two "Next:" labels and one rule name follow the new
    Day 1 order and the single set of safety rules.
    """
    video, statement, shake_out, boss = slides[3], slides[13], slides[14], slides[25]

    lighten(kit, video, pill_color=NAVY, accent=BLUE)
    # The video's poster is cream, so on a bright page it sits in a navy screen frame.
    poster = max((shape for shape in video.shapes if shape.shape_type == MSO_SHAPE_TYPE.PICTURE),
                 key=lambda shape: shape.width)
    # The poster filled the page up to the title; a little smaller, it leaves air above
    # and below the frame.
    ratio = poster.width / poster.height
    y, h = 2.12, 4.70
    w = h * ratio
    x = (Emu(kit.prs.slide_width).inches - w) / 2
    poster.left, poster.top = Inches(x), Inches(y)
    poster.width, poster.height = Inches(w), Inches(h)
    frame = kit.box(video, x - 0.12, y - 0.12, w + 0.24, h + 0.24, NAVY, radius=0.20, shadow=True)
    poster._element.addprevious(frame._element)

    lighten(kit, statement, pill_color=NAVY, accent=BLUE)

    # The stop after "Teach a computer" is now Raiyan's Quick, Draw! Race.
    next_label = _shape_with_text(shake_out, "Next: Make with AI!")
    _set_text(next_label, "Next: Quick, Draw! Race")
    next_label.width = Inches(5.30)
    _shape_fill(next_label).set("val", GREEN)

    lighten(kit, boss, pill_color=ORANGE, accent=ORANGE, background="PAPER_WARM")
    # The stop after "Make with AI" is now Raiyan's Is it AI?
    _set_text(_shape_with_text(boss, "Next: Monster, Guide or Buddy?"), "Next: Is it AI?")
    # Rule 3 is "Do your own thinking" everywhere, as in the proposal and Payton's slides.
    _set_text(_shape_with_text(boss, "You are the boss"), "Do your own thinking")
    crown = min((shape for shape in boss.shapes if shape.shape_type == MSO_SHAPE_TYPE.PICTURE
                 and Emu(shape.left).inches > 6 and Emu(shape.left).inches < 7),
                key=lambda shape: shape.width)
    x, y, size = Emu(crown.left).inches, Emu(crown.top).inches, Emu(crown.width).inches
    crown._element.getparent().remove(crown._element)
    kit.icon(boss, "b_s08_16.png", x, y, size, NAVY)
