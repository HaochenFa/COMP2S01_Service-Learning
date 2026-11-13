"""Stop 1 · Hello! Yelina's welcome and ice-breaking (30 min).

Rebuilt from "Day1_Welcome_Yelina.pdf" (8 pages). The wording is hers; the pictures
are the ones in her PDF, except the teacher cards, which are the sharper copies of
the same four pictures in Payton's deck.
"""
from day1 import WELCOME_TEAL
from deckkit import (BLUE, BODY_FONT, INK, MUTED, NAVY, ORANGE, PATH_TAN, PURPLE, RED, TEAL,
                     TINT, WHITE, YELLOW)
from layouts import (GAP, LEFT, ROBI_HAPPY, WIDTH, columns, header, hint, icon_or_figure,
                     number_circle, subtitle)

STOP = 1
TEACHERS = [
    ("p_s03_08.jpg", "Yelina", "Supply Chain Management and Analytics",
     "I study how food and toys travel to you. AI helps plan the trip."),
    ("p_s03_14.jpg", "Billy", "Computer Science", "I teach computers to learn from examples."),
    ("p_s03_20.jpg", "Payton", "Radiography", "I take X-ray images. AI can help doctors read them."),
    ("p_s03_26.jpg", "Raiyan", "Mechanical Engineering", "I design machines and robots that move."),
]


def title_slide(kit):
    slide = kit.slide("PAPER", notes="Yelina opens the day. Source: Yelina's welcome PDF, page 1.")
    kit.pill(slide, 0.60, 0.60, 5.60, 0.42, YELLOW, "DAY 1 · WHAT IS AI AND HOW DOES IT LEARN?",
             14, NAVY, 100)
    kit.text(slide, 0.60, 1.60, 6.60, 2.40, [[("Welcome to", INK)], [("Taming AI!", BLUE)]], 66)
    kit.text(slide, 0.65, 4.15, 6.40, 0.50, "Learning to use AI wisely, fairly, and for good",
             20, MUTED, font=BODY_FONT)
    kit.text(slide, 0.65, 5.15, 2.40, 0.70, "Tuloy ka!", 34, WELCOME_TEAL)
    kit.text(slide, 3.05, 5.27, 3.00, 0.50, "welcome, come in", 16, MUTED, font=BODY_FONT)
    kit.text(slide, 0.65, 6.45, 6.40, 0.40, "University of the Philippines Diliman · January 2027",
             14, MUTED, font=BODY_FONT)
    # Yelina's woven sun was drawn for a night sky, so it keeps one: a navy window.
    kit.box(slide, 7.45, 0.60, 5.28, 6.30, "17203D", radius=0.45)
    kit.picture(slide, "y_p1_01.png", 7.59, 1.25, 5.00, 5.00)
    return slide


def meet_your_teachers(kit):
    slide = kit.slide("PAPER", notes="Each teacher says one line. Source: Yelina's welcome PDF, page 2.")
    header(kit, slide, STOP, "LISTEN", "Meet your teachers!")
    for (x, w), (picture, name, major, about) in zip(columns(4), TEACHERS):
        kit.card(slide, x, 2.10, w, 3.80)
        picture_width = w - 0.40
        kit.picture(slide, picture, x + 0.20, 2.30, picture_width, picture_width * 512 / 938)
        kit.text(slide, x + 0.25, 3.85, w - 0.50, 0.45, name, 24, INK)
        kit.text(slide, x + 0.25, 4.30, w - 0.50, 0.50, major, 13, WELCOME_TEAL, anchor="top")
        kit.text(slide, x + 0.25, 4.85, w - 0.50, 0.95, about, 13, MUTED, font=BODY_FONT,
                 anchor="top")
    kit.icon_circle(slide, LEFT, 6.18, 0.50, WELCOME_TEAL, "y_p2_06.png")
    kit.text(slide, LEFT + 0.68, 6.18, 10.00, 0.50,
             "+ our friends from UP Diliman will teach with us every day!", 18, WELCOME_TEAL)
    return slide


def first_30_minutes(kit):
    slide = kit.slide("PAPER", notes="Walk through the five steps. Source: Yelina's welcome PDF, page 3.")
    header(kit, slide, STOP, "LISTEN", "Our first 30 minutes")
    subtitle(kit, slide, "Fun first, then new friends, then a new team!")
    steps = [
        ("y_p3_02.png", "Meet your teachers", "5 min"),
        ("y_p3_03.png", "Name sticker", "5 min"),
        ("y_p3_04.png", "Find a Match", "8 min"),
        ("y_p3_05.png", "Meet your team", "6 min"),
        ("y_p3_06.png", "Team name & shout-out", "6 min"),
    ]
    spots = columns(5, gap=0)
    y = 3.95
    kit.dashed_line(slide, spots[0][0] + spots[0][1] / 2, y, spots[4][0] + spots[4][1] / 2, y)
    for (x, w), (icon_name, label, minutes) in zip(spots, steps):
        centre = x + w / 2
        kit.icon_circle(slide, centre - 0.65, y - 0.65, 1.30, WELCOME_TEAL, icon_name)
        kit.text(slide, x + 0.10, y + 0.85, w - 0.20, 0.70, label, 19, INK, align="center",
                 anchor="top")
        kit.pill(slide, centre - 0.55, y + 1.65, 1.10, 0.40, TINT[YELLOW], minutes, 14, NAVY)
    return slide


def name_sticker(kit):
    slide = kit.slide("PAPER", notes="Hand out stickers and markers. Source: Yelina's welcome PDF, page 4.")
    header(kit, slide, STOP, "DO", "Make your name sticker")
    # The sticker: a red label with a white writing area.
    kit.box(slide, LEFT, 2.15, 4.90, 4.25, RED, radius=0.30, shadow=True)
    kit.text(slide, LEFT, 2.25, 4.90, 0.70, "HELLO", 40, WHITE, align="center", spacing=300)
    kit.text(slide, LEFT, 2.90, 4.90, 0.35, "my name is", 16, WHITE, font=BODY_FONT, align="center")
    kit.box(slide, LEFT + 0.15, 3.40, 4.60, 2.85, WHITE, radius=0.20)
    kit.text(slide, LEFT + 0.40, 3.50, 4.10, 0.60, "your name here", 22, PATH_TAN, font=BODY_FONT,
             align="center", italic=True)
    kit.box(slide, LEFT + 0.45, 4.12, 4.00, 0.03, INK, radius=0.01)
    kit.text(slide, LEFT + 0.45, 4.30, 4.00, 0.35, "My favourite food:", 14, INK)
    kit.box(slide, LEFT + 0.45, 4.72, 4.00, 1.35, TINT[TEAL], radius=0.15, line=WELCOME_TEAL,
            line_width=1.5, dashed=True)
    kit.text(slide, LEFT + 0.45, 4.72, 4.00, 1.35, "draw or write it here!", 14, MUTED,
             font=BODY_FONT, align="center")

    x = 6.00
    w = LEFT + WIDTH - x
    steps = [
        ("y_p4_03.png", "Write your first name or nickname"),
        ("y_p4_05.png", "Draw or write your favourite food"),
        ("y_p3_03.png", "Stick it on your shirt"),
    ]
    for index, (icon_name, label) in enumerate(steps):
        y = 2.15 + index * 1.08
        kit.card(slide, x, y, w, 0.90, radius=0.25)
        kit.icon_circle(slide, x + 0.20, y + 0.15, 0.60, WELCOME_TEAL, icon_name)
        kit.text(slide, x + 1.00, y, w - 1.20, 0.90, label, 19, INK)
    kit.card(slide, x, 5.45, w, 0.95, TINT[YELLOW], radius=0.25)
    kit.icon_circle(slide, x + 0.20, 5.625, 0.60, YELLOW, "y_p4_08.png", NAVY)
    kit.text(slide, x + 1.00, 5.45, w - 1.20, 0.95,
             "First name only! No surname, school or address.", 17, INK)
    return slide


def find_a_match(kit):
    slide = kit.slide("PAPER", notes="Learners walk around and group by favourite food. "
                                     "Source: Yelina's welcome PDF, page 5.")
    header(kit, slide, STOP, "MOVE", "Find a Match!")
    subtitle(kit, slide, [[("Walk around and ask: ", MUTED),
                           ("“What’s your favourite food?”", INK, "Fredoka")]])
    foods = [
        (RED, "y_p4_05.png", "food_rice", "Rice & noodles", "pancit, fried rice, spaghetti"),
        (TEAL, "y_p5_03.png", "food_meat", "Meat & fish", "adobo, fried chicken, sisig"),
        (ORANGE, "y_p5_04.png", "food_fruits", "Fruits", "mango, banana, pineapple"),
        (PURPLE, "y_p5_05.png", "food_sweets", "Sweets & snacks", "halo-halo, ube cake, chips"),
    ]
    spots = columns(4)
    for (x, w), (color, icon_name, figure, name, examples) in zip(spots, foods):
        kit.card(slide, x, 2.70, w, 2.15)
        icon_or_figure(kit, slide, figure, x + 0.28, 2.95, 0.85, color, icon_name, grow=1.2)
        kit.text(slide, x + 0.28, 3.92, w - 0.45, 0.40, name, 21, INK)
        kit.text(slide, x + 0.28, 4.32, w - 0.45, 0.34, examples, 13, MUTED, font=BODY_FONT)

    # The four steps share one band; the numbers give the order. U+2060 keeps "3–4" together.
    kit.card(slide, LEFT, 5.15, WIDTH, 0.95, radius=0.30)
    steps = ["Walk around", "Ask a friend", "Find a similar food", "Form a group of 3⁠–⁠4"]
    for (x, w), (index, label) in zip(spots, enumerate(steps)):
        number_circle(kit, slide, x + 0.28, 5.40, 0.45, index + 1, YELLOW, 16)
        kit.text(slide, x + 0.86, 5.15, w - 0.70, 0.95, label, 15, INK)
    hint(kit, slide, "No match yet? Ask a teacher: we’ll help you find a team!", y=6.35)
    return slide


def meet_your_team(kit):
    slide = kit.slide("PAPER", notes="Groups introduce themselves in turn. "
                                     "Source: Yelina's welcome PDF, page 6.")
    header(kit, slide, STOP, "TALK", "Meet your team!")
    left_width = 7.20
    kit.card(slide, LEFT, 2.10, left_width, 2.85)
    kit.text(slide, LEFT + 0.35, 2.22, 4.00, 0.35, "SAY IT LIKE THIS", 12, WELCOME_TEAL, spacing=150)
    lines = ["Hello, I’m ______.", "My favourite food is ________.",
             "One fun fact about me: ________."]
    for index, line in enumerate(lines):
        y = 2.68 + index * 0.72
        number_circle(kit, slide, LEFT + 0.35, y, 0.50, index + 1, WELCOME_TEAL, 18)
        kit.text(slide, LEFT + 1.10, y - 0.05, left_width - 1.40, 0.60, line, 23, INK)

    x = LEFT + left_width + GAP
    w = LEFT + WIDTH - x
    kit.card(slide, x, 2.10, w, 2.85, TINT[TEAL])
    kit.text(slide, x + 0.35, 2.25, w - 0.70, 0.50, "Listen like a pro", 22, TEAL)
    tips = [("y_p6_03.png", "Look at the speaker"), ("y_p6_04.png", "Take turns"),
            ("y_p6_05.png", "Clap for your friends")]
    for index, (icon_name, tip) in enumerate(tips):
        y = 2.90 + index * 0.64
        kit.icon_circle(slide, x + 0.35, y, 0.48, TEAL, icon_name)
        kit.text(slide, x + 1.02, y, w - 1.30, 0.48, tip, 17, INK)

    kit.text(slide, LEFT + 0.05, 5.20, 5.00, 0.35, "NEED A FUN FACT IDEA?", 12, WELCOME_TEAL,
             spacing=150)
    ideas = ["I have a pet cat", "I love basketball", "I can sing and dance"]
    for (ix, iw), idea in zip(columns(3), ideas):
        kit.box(slide, ix, 5.62, iw, 0.62, WHITE, radius=0.31, line=WELCOME_TEAL, line_width=1.5)
        kit.text(slide, ix, 5.62, iw, 0.62, idea, 17, INK, align="center")
    hint(kit, slide, "Remember: no surname, school or address!", y=6.42)
    return slide


def pick_a_team_name(kit):
    slide = kit.slide("PAPER", notes="Each group agrees on a name. Source: Yelina's welcome PDF, page 7.")
    header(kit, slide, STOP, "TALK", "Pick a team name!")
    part_width = 3.55
    y, h = 2.10, 1.90
    parts = [
        (LEFT, "ADJECTIVE", "Brave · Speedy · Clever · Happy"),
        (LEFT + part_width + 0.75, "PHILIPPINE ANIMAL", "Tarsier · Carabao · Eagle · Pawikan · Tamaraw"),
    ]
    for x, label, words in parts:
        kit.card(slide, x, y, part_width, h)
        kit.text(slide, x + 0.30, y + 0.22, part_width - 0.60, 0.32, label, 12, WELCOME_TEAL,
                 spacing=150)
        kit.text(slide, x + 0.30, y + 0.62, part_width - 0.60, 1.05, words, 17, INK, anchor="top")
    kit.text(slide, LEFT + part_width, y, 0.75, h, "+", 40, INK, align="center")
    kit.text(slide, LEFT + 2 * part_width + 0.75, y, 0.75, h, "=", 40, INK, align="center")
    result_x = LEFT + 2 * part_width + 1.50
    result_width = LEFT + WIDTH - result_x
    kit.card(slide, result_x, y, result_width, h, TINT[YELLOW])
    kit.text(slide, result_x + 0.30, y + 0.22, result_width - 0.60, 0.32, "YOUR TEAM NAME", 12,
             "B26A00", spacing=150)
    kit.text(slide, result_x + 0.30, y + 0.62, result_width - 0.60, 1.05, "Brave Tarsiers!", 30, INK,
             anchor="top")

    steps = [
        ("y_p7_05.png", "Share ideas", "Everyone says one idea"),
        ("y_p7_06.png", "Vote", "Hands up for your favourite"),
        ("y_p7_07.png", "Shout it loud!", "Tell the class your name"),
    ]
    for (x, w), (icon_name, heading, body) in zip(columns(3), steps):
        kit.card(slide, x, 4.35, w, 1.45)
        kit.icon_circle(slide, x + 0.28, 4.675, 0.80, WELCOME_TEAL, icon_name)
        kit.text(slide, x + 1.30, 4.60, w - 1.50, 0.45, heading, 21, INK)
        kit.text(slide, x + 1.30, 5.05, w - 1.50, 0.45, body, 14, MUTED, font=BODY_FONT)
    hint(kit, slide, "Kind names only: and have fun!", y=6.15)
    return slide


def team_shout_out(kit):
    slide = kit.slide("PAPER", notes="Every team stands and shouts its name. "
                                     "Source: Yelina's welcome PDF, page 8.")
    header(kit, slide, STOP, "MOVE", "Team shout-out!")
    steps = [("y_p8_02.png", "Stand up as a team"), ("y_p8_03.png", "Shout your team name"),
             ("y_p8_04.png", "Say your name and wave!")]
    for index, (icon_name, label) in enumerate(steps):
        y = 2.15 + index * 1.18
        kit.card(slide, LEFT, y, 8.40, 1.00, radius=0.28)
        number_circle(kit, slide, LEFT + 0.25, y + 0.20, 0.60, index + 1, WELCOME_TEAL, 22)
        kit.text(slide, LEFT + 1.15, y, 6.00, 1.00, label, 25, INK)
        kit.icon(slide, icon_name, LEFT + 7.45, y + 0.225, 0.55, WELCOME_TEAL)
    kit.picture(slide, ROBI_HAPPY, 9.60, 2.15, h=3.45, prefer="robi_megaphone")
    kit.next_pill(slide, "Next: let’s see our week ahead!", WELCOME_TEAL, x=LEFT, y=5.85)
    return slide


def build(kit):
    """All of Stop 1, in order, starting with the deck's title slide."""
    return [
        title_slide(kit),
        meet_your_teachers(kit),
        first_30_minutes(kit),
        name_sticker(kit),
        find_a_match(kit),
        meet_your_team(kit),
        pick_a_team_name(kit),
        team_shout_out(kit),
    ]
