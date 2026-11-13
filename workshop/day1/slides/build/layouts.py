"""Layout helpers shared by every section, so all slides sit on the same grid.

Content lives between LEFT and RIGHT. Cards are white on the cream page; colour
is kept for small things (icon circles, numbers, pills) unless it carries meaning.
"""
from day1 import stop, stop_label
from deckkit import BODY_FONT, INK, MUTED, WHITE, YELLOW, NAVY

LEFT = 0.60
RIGHT = 12.73
WIDTH = RIGHT - LEFT
GAP = 0.25

ROBI_HAPPY = "b_s07_26.png"
ROBI_WAVE = "b_s01_05.png"
AMBER_TEXT = "B26A00"


def stop_color(number):
    return stop(number)[4]


def text_color_on(color):
    """Readable text colour for a label placed on `color`."""
    return NAVY if color == YELLOW else WHITE


def accent_text(color):
    """Version of a stop colour that is readable as text on the cream page."""
    return AMBER_TEXT if color == YELLOW else color


def header(kit, slide, number, tag, title, title_size=40):
    """Stop pill, action tag and title: the same three things on every content slide."""
    kit.stop_pill(slide, stop_label(number), stop_color(number))
    if tag:
        kit.tag(slide, tag)
    if title:
        kit.title(slide, title, size=title_size)


def columns(count, gap=GAP, left=LEFT, width=WIDTH):
    """Left edge and width of `count` equal columns across the content area."""
    column_width = (width - gap * (count - 1)) / count
    return [(left + index * (column_width + gap), column_width) for index in range(count)]


def subtitle(kit, slide, content, y=1.90, size=22):
    return kit.text(slide, LEFT, y, WIDTH, 0.50, content, size, MUTED, font=BODY_FONT)


def hint(kit, slide, content, y=6.50):
    return kit.text(slide, LEFT + 0.05, y, WIDTH, 0.40, content, 15, MUTED, font=BODY_FONT,
                    italic=True)


def number_circle(kit, slide, x, y, d, number, fill, size=None):
    kit.circle(slide, x, y, d, fill)
    kit.text(slide, x, y, d, d, str(number), size or round(d * 36), text_color_on(fill),
             align="center")


def icon_or_figure(kit, slide, figure, x, y, d, fill, icon_name, icon_color=WHITE, grow=1.25):
    """An icon in a coloured circle, or the new picture of the same thing when one has
    been made. The picture is a little larger than the circle and starts at its left edge."""
    new = kit.figure(figure)
    if new is None:
        return kit.icon_circle(slide, x, y, d, fill, icon_name, icon_color)
    size = d * grow
    return kit.fitted(slide, new, x - 0.05, y - (size - d) / 2, size, size, align="left")


def photo(kit, slide, path, x, y, w, ratio=1.5, frame=0.12):
    """A scene picture with round corners in a white frame, like the other cards."""
    h = w / ratio
    kit.card(slide, x, y, w, h, radius=0.28)
    inner_w, inner_h = w - 2 * frame, h - 2 * frame
    rounded = kit.rounded(path, inner_w / inner_h, radius=0.18 / inner_h)
    return kit.picture(slide, rounded, x + frame, y + frame, inner_w, inner_h)


def bullets(kit, slide, x, y, w, items, size, dot_color, color=INK, line_height=None,
            font=BODY_FONT):
    """Bulleted lines with a small coloured dot each. Returns the y after the last one."""
    line_height = line_height or size / 72 * 1.35
    for item in items:
        lines = item["lines"] if isinstance(item, dict) else 1
        content = item["text"] if isinstance(item, dict) else item
        kit.circle(slide, x, y + line_height / 2 - 0.06, 0.12, dot_color)
        kit.text(slide, x + 0.30, y, w - 0.30, line_height * lines, content, size, color,
                 font=font, anchor="top")
        y += line_height * lines + 0.14
    return y
