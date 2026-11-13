"""Payton's two blocks, rebuilt from her Google Slides deck "Day 1 Ppt".

Stop 2 · Our week (her slides 1-11) and Stop 7 · Monster, Guide or Buddy? (13-35).
The wording is hers. Changes the new Day 1 order forced are marked with "FORCED" comments.

Her three characters and her reaction pictures are placed by their old file names. When
the figures folder holds a new Robi picture for one of them (see SWAPS in figures.py),
the new picture is shown instead; remove that file and her picture is back.
"""
from day1 import WEEK_TOMATO, journey_map
from deckkit import (BODY_FONT, INK, MUTED, NAVY, PURPLE, RED, TEAL, TINT, WHITE, YELLOW)
from layouts import (AMBER_TEXT, GAP, LEFT, WIDTH, accent_text, columns, header, icon_or_figure,
                     text_color_on)
from yelina import TEACHERS

WEEK = 2
ETHICS = 7
TOMATO_TINT = "FFE5DF"

# role -> (colour, small icon, character picture)
ROLES = {
    "Monster": (RED, "p_s17_22.png", "p_s13_02.png"),
    "Guide": (TEAL, "p_s17_25.png", "p_s13_06.png"),
    "Buddy": (YELLOW, "p_s17_28.png", "p_s13_10.png"),
}

RULES = [
    ("p_s06_03.png", "Keep your information private",
     "Never tell AI your full name, address, school, passwords or any other personal information."),
    ("p_s08_03.png", "Always check",
     "AI can make mistakes. Ask a teacher or check the information using trusted sources."),
    ("p_s09_03.png", "Do your own thinking", "AI helps, but YOU do the thinking."),
]

SCENARIO_NOTE = ("Read the scenario aloud. Learners walk to a corner (about 30 sec). Then ask one "
                 "learner per corner to share a reason. Next slide = answer.")
ANSWER_NOTE = ("Reveal the answer, then add one sentence on why. Keep a tally on the board of how "
               "many scenarios the class got right.")
SCENARIO_EXTRA_NOTES = {
    5: (" NOTE: Accept Buddy if a learner argues it supports creativity, but the main answer is "
        "Guide (brainstorm, then think for yourself)."),
}

# scenario, role, the scenario as worded on her answer slide, reasons, extra line, picture
SCENARIOS = [
    ("Ana copies AI's answer for her homework without reading it.", "Monster", None,
     ["No thinking", "AI can make mistakes", "Not her original work"], None, "p_s19_10.gif"),
    ("Juan asks AI to explain a hard word, then checks it in a dictionary.", "Guide", None,
     ["Juan learns with AI, then checks it."], None, None),
    ("Miguel tells AI his home address and phone number.", "Monster", None,
     ["Private info stays private. Never tell AI!"], None, "p_s23_10.gif"),
    ("Maria and her friends use AI to help make a storybook for younger kids.", "Buddy", None,
     ["AI helps them make something good for others."], None, None),
    ("Liza asks AI for story ideas, then writes her own story.", "Guide", None,
     ["AI gives ideas, Liza does the thinking."], None, None),
    ("Carlo uses AI to make an embarrassing picture of a classmate.", "Monster", None,
     ["AI must never be used to hurt others."], "Be a good person!", None),
    ("Mika's group uses AI to build a math game for their classmates.", "Buddy",
     "Mika's group uses AI to help build a math game for their classmates.",
     ["They use AI to help classmates learn."], None, None),
    ("Nico asks AI a science question, then checks his book and his teacher.", "Guide", None,
     ["Nico checks AI's answer with trusted sources."], None, None),
]


# ---- Stop 2 · Our week ---------------------------------------------------------

def week_at_a_glance(kit):
    slide = kit.slide("PAPER", notes="Quickly walk through the schedule (about 2 min): Days 1-4 are "
                                     "3-hour workshop days where we learn and create. Day 5 is "
                                     "Reflection and Showcase day. Today is Day 1.")
    header(kit, slide, WEEK, "LISTEN", "Our week at a glance")
    days = [("Day 1", "3 hours", "Learn + create"), ("Day 2", "3 hours", "Learn + create"),
            ("Day 3", "3 hours", "Learn + create"), ("Day 4", "3 hours", "Learn + create"),
            ("Day 5", "Showcase", "Reflect + share")]
    for index, ((x, w), (day, length, what)) in enumerate(zip(columns(5), days)):
        y = 2.65
        today = index == 0
        kit.card(slide, x, y, w, 3.30)
        if today:
            kit.box(slide, x, y, w, 3.30, None, line=YELLOW, line_width=4)
            kit.pill(slide, x + w / 2 - 0.65, y - 0.50, 1.30, 0.36, YELLOW, "TODAY", 13, NAVY, 100)
        centre = x + w / 2
        if index < 4:
            kit.circle(slide, centre - 0.60, y + 0.35, 1.20, WEEK_TOMATO)
            kit.text(slide, centre - 0.60, y + 0.35, 1.20, 1.20, str(index + 1), 40, WHITE,
                     align="center")
        else:
            kit.icon_circle(slide, centre - 0.60, y + 0.35, 1.20, YELLOW, "p_s01_27.png", NAVY)
        kit.text(slide, x, y + 1.75, w, 0.50, day, 26, INK, align="center")
        kit.text(slide, x, y + 2.25, w, 0.38, length, 16, MUTED, font=BODY_FONT, align="center")
        kit.text(slide, x, y + 2.65, w, 0.38, what, 15, INK, align="center")
    return slide


def _product_card(kit, slide, x, w, y, h, icon_name, color, name, about, day, figure):
    kit.card(slide, x, y, w, h)
    icon_or_figure(kit, slide, figure, x + 0.30, y + 0.30, 1.00, color, icon_name,
                   text_color_on(color))
    kit.text(slide, x + 0.30, y + 1.50, w - 0.60, 0.50, name, 24, INK)
    kit.text(slide, x + 0.30, y + 2.02, w - 0.60, 0.75, about, 15, MUTED, font=BODY_FONT,
             anchor="top")
    kit.pill(slide, x + 0.30, y + h - 0.68, 1.15, 0.40, TOMATO_TINT, day, 14, WEEK_TOMATO)


PRODUCTS = [
    # FORCED: her card said "Day 1-2"; the flashcards now start on Day 2.
    ("p_s02_03.png", WEEK_TOMATO, "Flashcards", "8-10 cards about AI", "Day 2", "obj_flashcards"),
    ("p_s02_08.png", TEAL, "A storybook", "Local story with pictures and sound", "Day 3",
     "obj_storybook"),
    ("p_s02_13.png", YELLOW, "A game", "with rules, levels and scores", "Day 4", "obj_game"),
    ("p_s02_18.png", NAVY, "An essay", "Reflect on the week", "Day 5", "obj_essay"),
]


def four_things(kit):
    slide = kit.slide("PAPER", notes="Preview the four products and the Day 5 showcase.")
    header(kit, slide, WEEK, "LISTEN", "We are going to make 4 things!")
    for (x, w), product in zip(columns(4), PRODUCTS):
        _product_card(kit, slide, x, w, 2.15, 3.55, *product)
    kit.icon_circle(slide, LEFT, 6.05, 0.55, YELLOW, "p_s02_22.png", NAVY)
    kit.text(slide, LEFT + 0.75, 6.05, 10.00, 0.55, "…and show them all at the Day 5 showcase!",
             20, INK)
    return slide


def flashcard_example(kit):
    slide = kit.slide("PAPER", notes="The teachers' intro cards are an example of what a flashcard "
                                     "looks like.")
    header(kit, slide, WEEK, "LISTEN", "We are going to make 4 things!")
    spots = columns(4)
    _product_card(kit, slide, spots[0][0], spots[0][1], 2.15, 3.55, *PRODUCTS[0])
    x = spots[1][0] + 0.15
    kit.text(slide, x, 2.10, 3.00, 0.40, "Example:", 20, INK)
    for (cx, cw), (picture, name, major, about) in zip(
            columns(4, gap=0.18, left=x, width=LEFT + WIDTH - x), TEACHERS):
        kit.card(slide, cx, 2.60, cw, 3.10, radius=0.18)
        picture_width = cw - 0.24
        kit.picture(slide, picture, cx + 0.12, 2.72, picture_width, picture_width * 512 / 938)
        kit.text(slide, cx + 0.15, 3.82, cw - 0.30, 0.34, name, 17, INK)
        kit.text(slide, cx + 0.15, 4.16, cw - 0.30, 0.42, major, 10, WEEK_TOMATO, anchor="top")
        kit.text(slide, cx + 0.15, 4.62, cw - 0.30, 1.00, about, 11, MUTED, font=BODY_FONT,
                 anchor="top")
    return slide


def before_we_start(kit):
    slide = kit.slide("PAPER", notes="Lead-in to the three AI Safety Rules.")
    header(kit, slide, WEEK, "LISTEN", None)
    if kit.figure("robi_rules"):
        # Robi holding the rules stands in for her frog meme, a little larger.
        kit.picture(slide, "p_s05_02.gif", 0.90, 2.20, 3.10, 3.10)
    else:
        kit.picture(slide, "p_s05_02.gif", 1.20, 2.55, 2.40, 2.40)
    kit.text(slide, 4.20, 2.55, 8.30, 2.40, "Before we start to use AI…", 54, INK)
    return slide


def _rule_card(kit, slide, y, h, icon_name, name, body):
    kit.card(slide, LEFT, y, WIDTH, h)
    kit.icon_circle(slide, LEFT + 0.30, y + (h - 0.85) / 2, 0.85, WEEK_TOMATO, icon_name)
    kit.text(slide, LEFT + 1.45, y, 3.40, h, name, 23, INK)
    kit.text(slide, LEFT + 5.05, y, WIDTH - 5.40, h, body, 17, MUTED, font=BODY_FONT)


def rule(kit, number, pictures, cross=False):
    """One safety rule with Payton's reaction pictures below it.
    `pictures` is a list of (file, x, y, width)."""
    icon_name, name, body = RULES[number - 1]
    slide = kit.slide("PAPER", notes=f"AI Safety Rule {number}: {name}.")
    header(kit, slide, WEEK, "LISTEN", f"Rule no.{number}")
    _rule_card(kit, slide, 2.10, 1.35, icon_name, name, body)
    for picture, x, y, width in pictures:
        kit.picture(slide, picture, x, y, w=width)
    if cross:
        kit.picture(slide, "p_s07_09.gif", 2.95, 3.85, w=2.50)
    return slide


def three_rules(kit):
    slide = kit.slide("PAPER", notes="Learners repeat the three rules together.")
    header(kit, slide, WEEK, "SAY", "Our 3 AI Safety Rules")
    kit.picture(slide, "p_s10_17.gif", 9.20, 0.95, w=1.35)
    for index, (icon_name, name, body) in enumerate(RULES):
        _rule_card(kit, slide, 2.10 + index * 1.50, 1.30, icon_name, name, body)
    return slide


def todays_adventure(kit):
    # FORCED: her agenda listed the old eight stops, so the shared day map replaces it.
    slide = kit.slide("PAPER", notes="Show the map so learners know what is coming today. Point at "
                                     "each stop in order; the clocks on the path are the breaks. "
                                     "The stop name is on the top left of every later slide.")
    kit.title(slide, "Today’s adventure")
    journey_map(kit, slide, WEEK)
    return slide


def build_week(kit):
    return [
        week_at_a_glance(kit),
        four_things(kit),
        flashcard_example(kit),
        before_we_start(kit),
        rule(kit, 1, [("p_s06_08.png", 1.40, 4.15, 5.60), ("p_s06_07.gif", 8.30, 3.80, 2.75)]),
        rule(kit, 1, [("p_s06_08.png", 1.40, 4.15, 5.60), ("p_s06_07.gif", 8.30, 3.80, 2.75)],
             cross=True),
        rule(kit, 2, [("p_s08_08.gif", 2.10, 3.80, 2.80), ("p_s08_09.jpg", 6.30, 3.85, 4.10)]),
        # Her two GIFs for rule 3 both show real people; one thinking Robi replaces the pair.
        rule(kit, 3, [("p_s09_09.gif", 5.22, 3.72, 2.90)] if kit.figure("robi_thinking") else
             [("p_s09_07.gif", 3.20, 3.85, 2.70), ("p_s09_09.gif", 7.40, 3.85, 2.70)]),
        three_rules(kit),
        todays_adventure(kit),
    ]


# ---- Stop 7 · Monster, Guide or Buddy? -------------------------------------------

def three_things(kit):
    slide = kit.slide("PAPER", notes="Introduce the three roles before the Corner Game.")
    header(kit, slide, ETHICS, "LISTEN", "AI can be three things…")
    roles = [
        ("Monster", "Monster", "when we use it carelessly or unfairly"),
        ("Guide", "Guide", "when we ask, think and check its answers"),
        ("Buddy", "Learning Buddy", "when we use it to learn, create and help others"),
    ]
    for (x, w), (role, name, body) in zip(columns(3), roles):
        color, _icon, character = ROLES[role]
        kit.card(slide, x, 2.20, w, 3.70, TINT[color])
        kit.picture(slide, character, x + w / 2 - 0.90, 2.35, 1.80, 1.80)
        kit.text(slide, x + 0.20, 4.20, w - 0.40, 0.50, name, 26, accent_text(color), align="center")
        kit.text(slide, x + 0.40, 4.75, w - 0.80, 0.90, body, 17, INK, font=BODY_FONT,
                 align="center", anchor="top")
    kit.text(slide, LEFT, 6.15, WIDTH, 0.60, "It depends on how WE use it!", 28, PURPLE,
             align="center")
    return slide


def role_examples(kit, role, title, question, examples):
    color, _icon, character = ROLES[role]
    slide = kit.slide("PAPER", notes=f"Two everyday examples of AI as a {role}.")
    header(kit, slide, ETHICS, "LISTEN", title)
    kit.picture(slide, character, 0.90, 2.25, 3.70, 3.70)
    x = 5.20
    kit.text(slide, x, 2.15, LEFT + WIDTH - x, 1.00, question, 30, INK)
    for index, ((cx, cw), example) in enumerate(
            zip(columns(2, left=x, width=LEFT + WIDTH - x), examples)):
        kit.card(slide, cx, 3.40, cw, 2.55, TINT[color])
        kit.text(slide, cx + 0.30, 3.62, cw - 0.60, 0.38, f"Example {index + 1}", 16,
                 accent_text(color))
        kit.text(slide, cx + 0.30, 4.10, cw - 0.60, 1.70, example, 21, INK, font=BODY_FONT,
                 anchor="top")
    return slide


def _corner_pills(kit, slide, y):
    """The three answers a learner can walk to."""
    for (x, w), role in zip(columns(3), ROLES):
        color, icon_name, _character = ROLES[role]
        kit.box(slide, x, y, w, 0.95, color, radius=0.475)
        kit.icon(slide, icon_name, x + 0.40, y + 0.20, 0.55, text_color_on(color))
        kit.text(slide, x + 1.15, y, w - 1.40, 0.95, role, 26, text_color_on(color))


def corner_game(kit):
    slide = kit.slide("PAPER", notes="Before starting: point to the 3 corner signs. Explain the 4 "
                                     "steps. Run 6-8 scenarios. Each scenario has a question slide, "
                                     "then an answer slide.")
    header(kit, slide, ETHICS, "MOVE", "Corner Game!")
    steps = [
        ("p_s17_03.png", "Read", "Read the scenario on the slide"),
        ("p_s17_08.png", "Walk", "Go to the corner you choose"),
        ("p_s17_13.png", "Share", "One kid per corner tells why"),
        ("p_s17_18.png", "Reveal", "See the answer together"),
    ]
    for (x, w), (icon_name, heading, body) in zip(columns(4), steps):
        kit.card(slide, x, 2.15, w, 2.55)
        kit.icon_circle(slide, x + w / 2 - 0.50, 2.40, 1.00, PURPLE, icon_name)
        kit.text(slide, x + 0.20, 3.50, w - 0.40, 0.45, heading, 23, INK, align="center")
        kit.text(slide, x + 0.25, 3.98, w - 0.50, 0.60, body, 14, MUTED, font=BODY_FONT,
                 align="center", anchor="top")
    _corner_pills(kit, slide, 5.10)
    return slide


def scenario(kit, number, text):
    slide = kit.slide("PAPER", notes=SCENARIO_NOTE + SCENARIO_EXTRA_NOTES.get(number, ""))
    header(kit, slide, ETHICS, "THINK", f"Scenario {number} of {len(SCENARIOS)}")
    kit.card(slide, LEFT, 2.15, WIDTH, 2.60)
    kit.text(slide, LEFT + 0.55, 2.15, WIDTH - 1.10, 2.60, text, 32, INK)
    _corner_pills(kit, slide, 5.15)
    return slide


def answer(kit, number, role, text, reasons, extra, picture):
    color, icon_name, _character = ROLES[role]
    slide = kit.slide("PAPER", notes=ANSWER_NOTE)
    header(kit, slide, ETHICS, "TALK", f"Scenario {number}: Answer")
    block_width = 3.30
    kit.box(slide, LEFT, 2.15, block_width, 4.20, color, radius=0.30, shadow=True)
    kit.circle(slide, LEFT + block_width / 2 - 0.80, 2.70, 1.60, WHITE)
    kit.icon(slide, icon_name, LEFT + block_width / 2 - 0.45, 3.05, 0.90, accent_text(color))
    kit.text(slide, LEFT, 4.65, block_width, 0.80, role, 36, text_color_on(color), align="center")

    x = LEFT + block_width + GAP
    w = LEFT + WIDTH - x
    kit.card(slide, x, 2.15, w, 4.20)
    kit.text(slide, x + 0.45, 2.45, w - 0.90, 0.70, text, 17, MUTED, font=BODY_FONT, italic=True,
             anchor="top")
    kit.text(slide, x + 0.45, 3.30, 3.00, 0.50, "Why?", 22, accent_text(color))
    text_width = w - 0.90 - (2.00 if picture else 0)
    y = 3.90
    if len(reasons) == 1:
        kit.text(slide, x + 0.45, y, text_width, 1.10, reasons[0], 30, INK, anchor="top")
        y += 1.25 if len(reasons[0]) > 34 else 0.70
    else:
        for reason in reasons:
            kit.circle(slide, x + 0.45, y + 0.22, 0.14, color)
            kit.text(slide, x + 0.80, y, text_width - 0.35, 0.58, reason, 26, INK)
            y += 0.66
    if extra:
        kit.text(slide, x + 0.45, y + 0.10, text_width, 0.60, extra, 26, accent_text(color))
    if picture:
        kit.picture(slide, picture, x + w - 2.10, 4.25, w=1.80)
    return slide


def what_to_learn(kit):
    slide = kit.slide("PAPER", notes="Wrap up (about 2 min). Humans are responsible for how AI is "
                                     "used. Success check: learners should get at least 70% of "
                                     "scenarios right, which is 6 of 8 (or 5 of 6 if you ran 6 "
                                     "scenarios). Celebrate the AI Tamers!")
    header(kit, slide, ETHICS, "SAY", "What to learn?")
    kit.text(slide, LEFT, 2.25, 8.60, 1.40, "AI can be a Monster, a Guide, or a Buddy.", 38, INK)
    kit.text(slide, LEFT, 3.80, 8.60, 0.70, "BUT we can decide its role!", 30, PURPLE)
    for index, role in enumerate(ROLES):
        color, icon_name, _character = ROLES[role]
        kit.icon_circle(slide, LEFT + index * 1.45, 4.95, 1.15, color, icon_name,
                        text_color_on(color))
    kit.picture(slide, "p_s34_10.gif", 9.45, 3.05, w=3.10)
    return slide


def humans_in_charge(kit):
    slide = kit.slide("PAPER", notes="Wrap up (about 2 min). Humans are responsible for how AI is "
                                     "used. Celebrate the AI Tamers!")
    header(kit, slide, ETHICS, "SAY", "Humans are in charge")
    kit.text(slide, LEFT, 2.25, 7.20, 1.60, "Don’t let AI be a monster under your control!", 36,
             INK)
    for index, role in enumerate(["Guide", "Buddy"]):
        color, icon_name, _character = ROLES[role]
        kit.icon_circle(slide, LEFT + index * 1.45, 4.35, 1.15, color, icon_name,
                        text_color_on(color))
    if kit.figure("robi_pompoms"):
        kit.picture(slide, "p_s35_08.gif", 8.75, 2.25, 3.60, 3.60)
    else:
        kit.picture(slide, "p_s35_08.gif", 8.25, 2.45, w=4.30)
    return slide


def build_ethics(kit):
    slides = [
        three_things(kit),
        role_examples(kit, "Monster", "Monster moment!", "When does AI becomes a monster?",
                      ["Copying AI answers without checking and understanding",
                       "Using AI to hurt, trick or exclude others"]),
        role_examples(kit, "Guide", "Guide", "When does AI becomes a guide?",
                      ["Asking AI for help and we check the answer carefully.",
                       "Using AI to brainstorm ideas"]),
        role_examples(kit, "Buddy", "Learning buddy", "When does AI becomes a learning buddy?",
                      ["Creating educational games", "Designing learning flashcards"]),
        corner_game(kit),
    ]
    for number, (text, role, answer_text, reasons, extra, picture) in enumerate(SCENARIOS, start=1):
        slides.append(scenario(kit, number, text))
        slides.append(answer(kit, number, role, answer_text or text, reasons, extra, picture))
    slides.append(what_to_learn(kit))
    slides.append(humans_in_charge(kit))
    return slides
