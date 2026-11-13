"""Raiyan's two practice blocks, rebuilt from "Taming AI Day 1 - Quick Draw and Is it AI.pptx".

Stop 4 · Quick, Draw! Race (his slides 2-3) and Stop 6 · Is it AI? (his slides 4-6 and 8).
The wording is his. His deck used emoji as pictures; icons from the shared set and the
new Robi and object pictures stand in for them. Changes the new Day 1 order forced are
marked with "FORCED" comments.
"""
from deckkit import BODY_FONT, GREEN, INK, MUTED, NAVY, PINK, TINT, YELLOW
from layouts import (GAP, LEFT, ROBI_HAPPY, WIDTH, bullets, columns, header, number_circle,
                     subtitle)

QUICK_DRAW = 4
IS_IT_AI = 6

RULES_ICON = "b_s02_13.png"   # a written list: fixed rules
BRAIN_ICON = "b_s08_16.png"   # learning


# ---- Stop 4 · Quick, Draw! Race ---------------------------------------------------

def race_rules(kit):
    slide = kit.slide("PAPER", notes="Groups take turns at the projector while Quick, Draw! guesses.")
    header(kit, slide, QUICK_DRAW, "DO", "Quick, Draw! Relay Race Rules")
    rules = [
        ("b_s15_10.png", "1 Person at a Time",
         "Groups take turns sending 1 player up to draw on the projector!"),
        ("b_s23_16.png", "6 Prompts Total", "Draw as fast as you can before time runs out!"),
        ("b_s26_13.png", "Most Guesses Wins!",
         "The group with the highest AI guesses wins the race!"),
    ]
    # The artist Robi holds a pencil and a drawing, so he needs a little more room.
    cards_width = 9.20 if kit.figure("robi_artist") else 9.50
    for (x, w), (icon_name, heading, body) in zip(columns(3, width=cards_width), rules):
        kit.card(slide, x, 2.25, w, 4.00)
        kit.icon_circle(slide, x + w / 2 - 0.55, 2.65, 1.10, GREEN, icon_name)
        kit.text(slide, x + 0.15, 4.00, w - 0.30, 0.50, heading, 21, INK, align="center")
        kit.text(slide, x + 0.30, 4.60, w - 0.60, 1.30, body, 16, MUTED, font=BODY_FONT,
                 align="center", anchor="top")
    if kit.figure("robi_artist"):
        kit.picture(slide, ROBI_HAPPY, 10.25, 3.00, h=2.90, prefer="robi_artist")
    else:
        kit.picture(slide, ROBI_HAPPY, 10.45, 2.90, h=3.10)
    return slide


def how_ai_guessed(kit):
    slide = kit.slide("PAPER", notes="After the race, open the Quick, Draw! data page and show the "
                                     "drawings the AI learned from: this is its data.")
    header(kit, slide, QUICK_DRAW, "TALK", "How Did the AI Guess Your Drawings?")
    points = [
        ("Millions of Human Examples",
         "Over 50+ million doodles were drawn by real people on the internet to build AI's "
         "memory bank!"),
        ("Stroke & Shape Patterns",
         "AI doesn't \"see\" a picture like humans—it tracks your line direction, curve shapes, "
         "and drawing stroke order."),
        ("Instant Pattern Matching",
         "Draw two ears on top of a circle? AI instantly matches that pattern with thousands of "
         "past bear doodles!"),
    ]
    list_width = 8.05
    for index, (heading, body) in enumerate(points):
        y = 2.15 + index * 1.48
        kit.card(slide, LEFT, y, list_width, 1.30)
        number_circle(kit, slide, LEFT + 0.28, y + 0.35, 0.60, index + 1, GREEN, 22)
        kit.text(slide, LEFT + 1.15, y + 0.14, list_width - 1.40, 0.40, heading, 20, INK)
        kit.text(slide, LEFT + 1.15, y + 0.56, list_width - 1.40, 0.62, body, 13, MUTED,
                 font=BODY_FONT, anchor="top")
    x = LEFT + list_width + GAP
    w = LEFT + WIDTH - x
    kit.card(slide, x, 2.15, w, 4.26, TINT[YELLOW])
    kit.pill(slide, x + w / 2 - 1.45, 2.42, 2.90, 0.38, YELLOW, "DATASET SHOW-AND-TELL", 12, NAVY, 100)
    kit.text(slide, x + 0.30, 2.95, w - 0.60, 1.00, "Let's Look at the Real Data!", 24, INK,
             align="center")
    scene = kit.figure("scene_doodles")
    if scene:
        # Robi studying a wall of doodles: the data the AI learned from.
        kit.picture(slide, kit.rounded(scene, 1.6, radius=0.07), x + 0.20, 4.05, w - 0.40)
    else:
        kit.picture(slide, ROBI_HAPPY, x + w / 2 - 0.85, 4.10, h=2.10)
    return slide


# ---- Stop 6 · Is it AI? -----------------------------------------------------------

def _two_sides(kit, slide, sides, body_size=20):
    """Two cards side by side: Not AI on the left (navy), AI on the right (pink)."""
    for (x, w), (color, icon_name, heading, lines) in zip(columns(2), sides):
        kit.card(slide, x, 2.20, w, 4.10)
        kit.icon_circle(slide, x + 0.40, 2.50, 0.95, color, icon_name)
        kit.text(slide, x + 1.60, 2.50, w - 1.90, 0.95, heading, 25, INK)
        if len(lines) == 1:
            kit.text(slide, x + 0.45, 3.80, w - 0.90, 2.30, lines[0], body_size, INK,
                     font=BODY_FONT, anchor="top", line_spacing=1.15)
        else:
            bullets(kit, slide, x + 0.45, 3.85, w - 0.90,
                    [{"text": line, "lines": 2} for line in lines], body_size, color)


def ai_vs_not_ai(kit):
    slide = kit.slide("PAPER", notes="A simple explanation before the game (about 5 min).")
    header(kit, slide, IS_IT_AI, "THINK", "AI vs. Not AI: What's the Difference?")
    _two_sides(kit, slide, [
        (NAVY, RULES_ICON, "NOT AI (Fixed Rules)",
         ["Follows exact, strict rules written step-by-step by a human.",
          "Does the exact same thing every single time without learning!"]),
        (PINK, BRAIN_ICON, "AI (Learns from Data)",
         ["Finds patterns in data examples to make smart guesses!",
          "Learns and gets smarter when given new drawings or examples."]),
    ])
    return slide


def pick_a_side(kit):
    slide = kit.slide("PAPER", notes="Read each item aloud; learners move to the AI side or the "
                                     "Not AI side. Keep the answers for the discussion.")
    header(kit, slide, IS_IT_AI, "MOVE", "Pick a Side: AI vs. Not AI!")
    subtitle(kit, slide, "Listen to Raiyan read each item, then move to the LEFT (AI) or RIGHT "
                         "(Not AI)!", size=19)
    # His deck showed an emoji for each item; the new object pictures take their place.
    items = [
        ("Pocket Calculator", "Doing 25 × 4", "obj_calculator"),
        ("Phone Face Unlock", "Recognizing your face", "obj_face_unlock"),
        ("Smart Robot Vacuum", "Avoiding new obstacles", "obj_vacuum"),
        ("Microwave Timer", "Counting down 60s", "obj_microwave"),
    ]
    spots = columns(2)
    top, step, height = 2.75, 1.32, 1.12
    for index, (name, detail, figure) in enumerate(items):
        x, w = spots[index % 2]
        y = top + (index // 2) * step
        kit.card(slide, x, y, w, height, radius=0.30)
        number_circle(kit, slide, x + 0.28, y + 0.24, 0.64, index + 1, PINK, 23)
        kit.text(slide, x + 1.20, y + 0.14, w - 2.80, 0.46, name, 22, INK)
        kit.text(slide, x + 1.20, y + 0.60, w - 2.80, 0.38, detail, 15, MUTED, font=BODY_FONT)
        if kit.figure(figure):
            kit.fitted(slide, kit.figure(figure), x + w - 1.50, y + 0.09, 1.20, 0.94)
    keyboard = kit.figure("obj_keyboard")
    w = 9.20 if keyboard else 7.80
    x = LEFT + (WIDTH - w) / 2
    y = top + 2 * step
    kit.card(slide, x, y, w, height, TINT[YELLOW], radius=0.30)
    number_circle(kit, slide, x + 0.28, y + 0.24, 0.64, 5, PINK, 23)
    kit.text(slide, x + 1.20, y + 0.14, 4.70, 0.46, "Auto-Correct & Predictive Text", 22, INK)
    kit.text(slide, x + 1.20, y + 0.60, 4.70, 0.38, "Guessing your next word", 15, MUTED,
             font=BODY_FONT)
    if keyboard:
        kit.fitted(slide, keyboard, x + w - 3.20, y + 0.09, 1.20, 0.94)
    kit.pill(slide, x + w - 1.80, y + 0.34, 1.50, 0.44, YELLOW, "TRICKY!", 15, NAVY, 100)
    return slide


def why_autocorrect(kit):
    slide = kit.slide("PAPER", notes="Discuss the tricky ones: normal machines follow strict rules, "
                                     "while AI learns from data.")
    header(kit, slide, IS_IT_AI, "TALK", "Why is Auto-Correct AI? (The Tricky One!)", title_size=38)
    _two_sides(kit, slide, [
        (NAVY, RULES_ICON, "Basic Spellcheck = NOT AI",
         ["Just looks up words in a fixed dictionary list. If a word isn't in the list, it flags "
          "a mistake. No learning involved!"]),
        (PINK, BRAIN_ICON, "Auto-Correct & Next-Word = AI",
         ["Learns how millions of people type sentences together. It predicts what word you "
          "meant to type based on word context and your typing habits!"]),
    ])
    return slide


def great_job(kit):
    slide = kit.slide("PAPER", notes="Raiyan's conclusion for the two practice blocks.")
    header(kit, slide, IS_IT_AI, "SAY", "Great Job, AI Explorers!")
    points = [
        "AI learns from thousands of human DATA EXAMPLES (like Quick, Draw!).",
        "Not AI follows strict fixed rules, while AI learns smart patterns!",
        # FORCED: his line said "3 Classroom Safety House Rules"; the deck keeps one name
        # for the rules, the one Payton introduces in Stop 2.
        "Always follow our 3 AI Safety Rules!",
    ]
    for index, point in enumerate(points):
        y = 2.20 + index * 1.38
        kit.card(slide, LEFT, y, 8.70, 1.18, radius=0.28)
        kit.icon_circle(slide, LEFT + 0.28, y + 0.29, 0.60, GREEN, "b_s05_32.png")
        kit.text(slide, LEFT + 1.15, y, 7.30, 1.18, point, 19, INK)
    kit.picture(slide, ROBI_HAPPY, 9.95, 2.45, h=3.50, prefer="robi_trophy")
    return slide


def build_quick_draw(kit):
    return [race_rules(kit), how_ai_guessed(kit)]


def build_is_it_ai(kit):
    return [ai_vs_not_ai(kit), pick_a_side(kit), why_autocorrect(kit), great_job(kit)]
