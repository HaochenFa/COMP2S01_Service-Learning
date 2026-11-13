"""Building blocks of the shared Day 1 slide style.

The style is the one already used in "Taming_AI_Day1_Billy": every measurement and
colour here was read from that deck, so slides built with this module sit next to
its slides without a visible seam. All positions and sizes are in inches.
"""
import hashlib
from copy import deepcopy
from pathlib import Path

from lxml import etree
from PIL import Image, ImageDraw
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE, MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.opc.packuri import PackURI
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

from figures import SWAPS

HEADING_FONT = "Fredoka"
BODY_FONT = "Lexend"

INK = "1C2440"
NAVY = "17213D"
MUTED = "4B5470"
MUTED_ON_DARK = "C9D2E8"
FAINT_ON_DARK = "8F9BBE"
WHITE = "FFFFFF"
YELLOW = "FFC83A"
BLUE = "2F6BFF"
RED = "D93A25"
GREEN = "178A50"
TEAL = "0F766E"
PURPLE = "7B4DFF"
ORANGE = "C9530A"
PINK = "C93D82"
PATH_TAN = "D8C6A6"

# Pale card fills that pair with the strong colours above.
TINT = {
    RED: "FFE5DF",
    PURPLE: "ECE5FF",
    BLUE: "E3ECFF",
    ORANGE: "FFE9D6",
    GREEN: "DFF3E6",
    TEAL: "DDF3F0",
    PINK: "FBE3EE",
    YELLOW: "FFF1C7",
}

DARK_LAYOUTS = {"NAVY", "PURPLE"}

# Plain background colour of each layout. The source deck used dotted pictures;
# these are the base colours of those pictures.
LAYOUT_FILL = {"PAPER": "FEF6E9", "PAPER_WARM": "FFF0DD", "NAVY": "17203D", "PURPLE": "281A58"}

# Action tag shown top right: label -> (fill, icon file in Billy's deck, text colour).
TAGS = {
    "DO": (GREEN, "b_s02_03.png", WHITE),
    "LISTEN": (TEAL, "b_s03_03.png", WHITE),
    "WATCH": (PURPLE, "b_s04_03.png", WHITE),
    "SAY": (RED, "b_s05_03.png", WHITE),
    "PREDICT": (YELLOW, "b_s09_03.png", NAVY),
    "TALK": (ORANGE, "b_s12_03.png", WHITE),
    "MOVE": (PINK, "b_s15_03.png", WHITE),
    "THINK": (BLUE, "b_s08_16.png", WHITE),
}

SHADOW_XML = (
    '<a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
    '<a:outerShdw blurRad="101600" rotWithShape="0" algn="bl" dir="5400000" dist="38100">'
    '<a:srgbClr val="5A4632"><a:alpha val="21961"/></a:srgbClr>'
    "</a:outerShdw></a:effectLst>"
)


class Kit:
    """Adds styled slides to one presentation, using pictures from an assets folder."""

    def __init__(self, presentation, assets_dir, cache_dir, figures_dir=None):
        self.prs = presentation
        self.assets = Path(assets_dir)
        self.figures = Path(figures_dir) if figures_dir else None
        self.cache = Path(cache_dir)
        self.cache.mkdir(parents=True, exist_ok=True)
        self.layouts = {layout.name: layout for layout in presentation.slide_layouts}
        self._slide_number = self._find_slide_number_placeholder()

    # ---- slides -------------------------------------------------------------

    def _find_slide_number_placeholder(self):
        for slide in self.prs.slides:
            for shape in slide.placeholders:
                if shape.placeholder_format.type is not None and "SLIDE_NUMBER" in str(
                    shape.placeholder_format.type
                ):
                    return deepcopy(shape._element)
        return None

    def flatten_backgrounds(self):
        """Replace each layout's dotted background picture with its plain base colour."""
        for name, color in LAYOUT_FILL.items():
            layout = self.layouts[name]
            properties = layout._element.cSld.find(qn("p:bg")).find(qn("p:bgPr"))
            blip = properties.find(".//" + qn("a:blip"))
            for child in list(properties):
                properties.remove(child)
            fill = etree.SubElement(properties, qn("a:solidFill"))
            etree.SubElement(fill, qn("a:srgbClr")).set("val", color)
            etree.SubElement(properties, qn("a:effectLst"))
            if blip is not None:
                layout.part.drop_rel(blip.get(qn("r:embed")))

    @staticmethod
    def set_background(slide, color):
        """Give one slide its own plain background, overriding its layout's."""
        c_sld = slide._element.cSld
        existing = c_sld.find(qn("p:bg"))
        if existing is not None:
            c_sld.remove(existing)
        background = etree.Element(qn("p:bg"))
        properties = etree.SubElement(background, qn("p:bgPr"))
        fill = etree.SubElement(properties, qn("a:solidFill"))
        etree.SubElement(fill, qn("a:srgbClr")).set("val", color)
        etree.SubElement(properties, qn("a:effectLst"))
        c_sld.insert(0, background)

    def remove_slides(self, keep=()):
        """Drop every existing slide except the 1-based numbers in `keep`.
        Returns the kept slides in their original order."""
        id_list = self.prs.slides._sldIdLst
        kept = []
        for number, slide_id in enumerate(list(id_list), start=1):
            if number in keep:
                kept.append(self.prs.slides.get(int(slide_id.get("id"))))
                continue
            self.prs.part.drop_rel(slide_id.rId)
            id_list.remove(slide_id)
        # python-pptx names a new slide file by counting slides, so the kept files are
        # renumbered from 1 to stop a new slide reusing a kept slide's file name.
        for index, slide in enumerate(kept, start=1):
            slide.part.partname = PackURI(f"/ppt/slides/slide{index}.xml")
        return kept

    def reorder(self, slides):
        """Put the deck's slides in the given order (every slide must be listed)."""
        id_list = self.prs.slides._sldIdLst
        by_id = {int(element.get("id")): element for element in id_list}
        ordered = [by_id[slide.slide_id] for slide in slides]
        if len(ordered) != len(by_id):
            raise ValueError("reorder() needs every slide of the deck exactly once")
        for element in list(id_list):
            id_list.remove(element)
        for element in ordered:
            id_list.append(element)

    @staticmethod
    def _drop_theme_style(shape):
        """New shapes inherit a theme shadow and outline; the source deck's shapes don't."""
        style = shape._element.find(qn("p:style"))
        if style is not None:
            shape._element.remove(style)

    def slide(self, layout="PAPER", notes=None):
        slide = self.prs.slides.add_slide(self.layouts[layout])
        slide.dark = layout in DARK_LAYOUTS
        slide.layout_name = layout
        if self._slide_number is not None:
            number = deepcopy(self._slide_number)
            slide.shapes._spTree.append(number)
            number.find(".//" + qn("p:cNvPr")).set("id", str(self._next_id(slide)))
        if notes:
            slide.notes_slide.notes_text_frame.text = notes
        return slide

    @staticmethod
    def _next_id(slide):
        ids = [int(el.get("id")) for el in slide.shapes._spTree.iter(qn("p:cNvPr"))]
        return max(ids, default=1) + 1

    # ---- text ---------------------------------------------------------------

    def text(self, slide, x, y, w, h, content, size, color=INK, font=HEADING_FONT,
             bold=None, align="left", anchor="middle", spacing=None, italic=False,
             line_spacing=None, gap=None):
        """Add a text box. `content` is a string, or a list of paragraphs, where a
        paragraph is a string or a list of (text, colour) / (text, colour, font) runs.
        `gap` is the space after each paragraph, in points."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        self._fill_text(box.text_frame, content, size, color, font, bold, align, anchor,
                        spacing, italic, line_spacing, gap)
        return box

    def _fill_text(self, frame, content, size, color, font, bold, align, anchor,
                   spacing=None, italic=False, line_spacing=None, gap=None):
        if bold is None:
            bold = font == HEADING_FONT
        frame.word_wrap = True
        frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
        frame.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE,
                                 "bottom": MSO_ANCHOR.BOTTOM}[anchor]
        paragraphs = content if isinstance(content, list) else [content]
        for index, paragraph_content in enumerate(paragraphs):
            paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            paragraph.alignment = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER,
                                   "right": PP_ALIGN.RIGHT}[align]
            if line_spacing:
                paragraph.line_spacing = line_spacing
            if gap:
                paragraph.space_after = Pt(gap)
            runs = paragraph_content if isinstance(paragraph_content, list) else [(paragraph_content, color)]
            for run_spec in runs:
                run_text, run_color = run_spec[0], run_spec[1]
                run_font = run_spec[2] if len(run_spec) > 2 else font
                run = paragraph.add_run()
                run.text = run_text
                run.font.name = run_font
                run.font.size = Pt(size)
                run.font.bold = bold if run_font == font else run_font == HEADING_FONT
                run.font.italic = italic
                run.font.color.rgb = RGBColor.from_string(run_color)
                properties = run._r.get_or_add_rPr()
                properties.set("lang", "en-US")
                if spacing:
                    properties.set("spc", str(spacing))
                # Name the font for every script slot, as Google Slides exports do.
                for slot in ("a:ea", "a:cs", "a:sym"):
                    element = etree.SubElement(properties, qn(slot))
                    element.set("typeface", run_font)

    def title(self, slide, content, color=None, size=40):
        color = color or (WHITE if slide.dark else INK)
        placeholder = slide.shapes.title
        self._fill_text(placeholder.text_frame, content, size, color, HEADING_FONT, True,
                        "left", "middle")
        return placeholder

    # ---- shapes -------------------------------------------------------------

    def box(self, slide, x, y, w, h, fill, radius=0.22, shadow=False, line=None,
            line_width=1.0, shape=MSO_SHAPE.ROUNDED_RECTANGLE, dashed=False):
        item = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
        self._drop_theme_style(item)
        if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
            item.adjustments[0] = min(0.5, radius / min(w, h))
        if fill is None:
            item.fill.background()
        else:
            item.fill.solid()
            item.fill.fore_color.rgb = RGBColor.from_string(fill)
        if line:
            item.line.color.rgb = RGBColor.from_string(line)
            item.line.width = Pt(line_width)
            if dashed:
                etree.SubElement(item.line._get_or_add_ln(), qn("a:prstDash")).set("val", "dash")
        else:
            item.line.fill.background()
        if shadow:
            item._element.spPr.append(etree.fromstring(SHADOW_XML))
        # Shapes carry no text of their own; labels are separate boxes, as in the source deck.
        item.text_frame.text = ""
        return item

    def card(self, slide, x, y, w, h, fill=WHITE, radius=0.22):
        return self.box(slide, x, y, w, h, fill, radius=radius, shadow=True)

    def circle(self, slide, x, y, d, fill, line=None, line_width=1.0):
        return self.box(slide, x, y, d, d, fill, shape=MSO_SHAPE.OVAL, line=line,
                        line_width=line_width)

    def pill(self, slide, x, y, w, h, fill, label, size, color=WHITE, spacing=None):
        item = self.box(slide, x, y, w, h, fill, radius=h / 2)
        self._fill_text(item.text_frame, label, size, color, HEADING_FONT, True, "center",
                        "middle", spacing)
        return item

    def dashed_line(self, slide, x1, y1, x2, y2, color=PATH_TAN, width=4.5):
        line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
                                          Inches(x2), Inches(y2))
        self._drop_theme_style(line)
        line.line.color.rgb = RGBColor.from_string(color)
        line.line.width = Pt(width)
        properties = line.line._get_or_add_ln()
        dash = etree.SubElement(properties, qn("a:prstDash"))
        dash.set("val", "dash")
        properties.set("cap", "rnd")
        return line

    # ---- pictures -----------------------------------------------------------

    def figure(self, *names):
        """Path of the first of these new figures that has been made, or None."""
        for name in names:
            if name and self.figures and (self.figures / f"{name}.png").exists():
                return self.figures / f"{name}.png"
        return None

    def picture(self, slide, name, x, y, w=None, h=None, prefer=None):
        """Place a picture from the assets folder.

        If a new figure exists for it (`prefer`, or the ones SWAPS lists for this
        picture), the new figure is placed instead, as tall as the old picture
        would have been and centred on the same spot."""
        path = Path(name) if Path(name).is_absolute() else self.assets / name
        new = self.figure(prefer, *SWAPS.get(path.name, []))
        if new is None:
            return slide.shapes.add_picture(str(path), Inches(x), Inches(y),
                                            Inches(w) if w else None, Inches(h) if h else None)
        with Image.open(path) as old:
            ratio = old.width / old.height
        if w is None:
            w = h * ratio
        elif h is None:
            h = w / ratio
        return self.fitted(slide, new, x, y, w, h)

    def fitted(self, slide, path, x, y, w, h, widest=1.35, align="center"):
        """Place a picture as tall as the box and centred in it (or on its left edge).
        A picture much wider than the box is made smaller, so it is never wider than
        `widest` boxes."""
        with Image.open(path) as image:
            ratio = image.width / image.height
        height = min(h, w * widest / ratio)
        width = height * ratio
        left = x if align == "left" else x + (w - width) / 2
        return slide.shapes.add_picture(str(path), Inches(left), Inches(y + (h - height) / 2),
                                        Inches(width), Inches(height))

    def rounded(self, path, ratio, radius=0.05, width=1100):
        """Return a copy of a photo cropped to `ratio` (width / height) with round corners."""
        target = self.cache / f"{Path(path).stem}_round_{ratio:.3f}.png"
        if not target.exists():
            photo = Image.open(path).convert("RGB")
            crop_w = min(photo.width, round(photo.height * ratio))
            crop_h = round(crop_w / ratio)
            left, top = (photo.width - crop_w) // 2, (photo.height - crop_h) // 2
            photo = photo.crop((left, top, left + crop_w, top + crop_h))
            photo = photo.resize((width, round(width / ratio)), Image.LANCZOS)
            # The corner mask is drawn four times larger, then reduced, for a smooth edge.
            mask = Image.new("L", (photo.width * 4, photo.height * 4), 0)
            ImageDraw.Draw(mask).rounded_rectangle(
                (0, 0, mask.width - 1, mask.height - 1), radius=round(radius * mask.height), fill=255)
            photo.putalpha(mask.resize(photo.size, Image.LANCZOS))
            photo.save(target, optimize=True)
        return target

    def swap_pictures(self, slides):
        """On slides that came with the base deck, replace every picture that has a new
        figure in SWAPS. The new figure keeps the old one's height and centre."""
        old_names = {}
        for name in SWAPS:
            if (self.assets / name).exists():
                old_names[hashlib.sha1((self.assets / name).read_bytes()).hexdigest()] = name
        swapped = 0
        for slide in slides:
            for shape in slide.shapes:
                if shape.shape_type != MSO_SHAPE_TYPE.PICTURE:
                    continue
                name = old_names.get(hashlib.sha1(shape.image.blob).hexdigest())
                new = self.figure(*SWAPS[name]) if name else None
                if new is None:
                    continue
                with Image.open(new) as image:
                    ratio = image.width / image.height
                blip = shape._element.blipFill.blip
                old_id = blip.rEmbed
                _part, blip.rEmbed = slide.part.get_or_add_image_part(str(new))
                slide.part.drop_rel(old_id)
                crop = shape._element.blipFill.find(qn("a:srcRect"))
                if crop is not None:
                    shape._element.blipFill.remove(crop)
                centre = shape.left + shape.width // 2
                height = min(shape.height, round(shape.width * 1.35 / ratio))
                shape.top += (shape.height - height) // 2
                shape.height = height
                shape.width = round(height * ratio)
                shape.left = centre - shape.width // 2
                swapped += 1
        return swapped

    def tinted(self, name, color):
        """Return a copy of a one-colour icon repainted in `color` (transparency kept)."""
        target = self.cache / f"{Path(name).stem}_{color}.png"
        if not target.exists():
            icon = Image.open(self.assets / name).convert("RGBA")
            red, green, blue = (int(color[i:i + 2], 16) for i in (0, 2, 4))
            painted = Image.new("RGBA", icon.size, (red, green, blue, 0))
            painted.putalpha(icon.getchannel("A"))
            painted.save(target)
        return target

    def icon(self, slide, name, x, y, size, color=WHITE):
        return self.picture(slide, self.tinted(name, color), x, y, size, size)

    def icon_circle(self, slide, x, y, d, fill, icon_name, icon_color=WHITE, ratio=0.56):
        self.circle(slide, x, y, d, fill)
        inset = d * (1 - ratio) / 2
        return self.icon(slide, icon_name, x + inset, y + inset, d * ratio, icon_color)

    # ---- recurring header parts ----------------------------------------------

    def stop_pill(self, slide, label, color):
        """The "STOP n · NAME" pill, top left. On dark layouts it turns yellow."""
        width = 0.12 * len(label) + 0.48
        if slide.dark:
            text_color = PURPLE if slide.layout_name == "PURPLE" else NAVY
            return self.pill(slide, 0.55, 0.38, width, 0.42, YELLOW, label, 14, text_color, 100)
        text_color = NAVY if color == YELLOW else WHITE
        return self.pill(slide, 0.55, 0.38, width, 0.42, color, label, 14, text_color, 100)

    def tag(self, slide, label):
        """The action tag, top right: what the class does on this slide."""
        fill, icon_name, text_color = TAGS[label]
        width = 0.80 + 0.16 * len(label)
        x = 12.79 - width
        self.box(slide, x, 0.36, width, 0.48, fill, radius=0.24)
        self.circle(slide, x + 0.06, 0.42, 0.36, WHITE)
        self.picture(slide, icon_name, x + 0.10, 0.47, 0.27, 0.27)
        self.text(slide, x + 0.47, 0.36, width - 0.52, 0.48, label, 15, text_color, spacing=150)

    def next_pill(self, slide, label, color, x=0.60, y=5.75):
        width = 0.2 * len(label) + 0.6
        text_color = NAVY if color == YELLOW else WHITE
        return self.pill(slide, x, y, width, 0.70, color, label, 24, text_color)
