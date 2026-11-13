"""Day 1 facts shared by every slide: the stops, their colours and the journey map.

The order and leaders follow the Day 1 table in the Google Doc
"COMP2S01 Workshop Proposal" as read on 13 November 2026.
"""
from deckkit import (BLUE, BODY_FONT, GREEN, INK, MUTED, NAVY, ORANGE, PATH_TAN, PINK, PURPLE,
                     WHITE, YELLOW)

WELCOME_TEAL = "0E9F8E"
WEEK_TOMATO = "E4572E"

# number, short name for learners, leader, minutes, colour, icon
STOPS = [
    (1, "Hello!", "Yelina", 30, WELCOME_TEAL, "b_s07_18.png"),
    (2, "Our week", "Payton", 15, WEEK_TOMATO, "p_s01_27.png"),
    (3, "Teach a computer", "Billy", 25, NAVY, "b_s08_16.png"),
    (4, "Quick, Draw! Race", "Raiyan", 8, GREEN, "b_s23_16.png"),
    (5, "Make with AI", "Billy", 20, ORANGE, "b_s21_26.png"),
    (6, "Is it AI?", "Raiyan", 12, PINK, "p_s11_11.png"),
    (7, "Monster, Guide or Buddy?", "Payton", 20, PURPLE, "p_s17_22.png"),
    (8, "Kahoot quiz", "Raiyan", 15, BLUE, "p_s11_40.png"),
    (9, "Wrap-up", "Yelina", 15, YELLOW, "b_s09_18.png"),
]

# Breaks come after these stops: stop number -> minutes.
BREAKS = {2: 5, 4: 5, 6: 10}

# The map is a grid: five columns, two rows, read left to right like a book.
COLUMN_X = [1.75, 4.20, 6.65, 9.10, 11.55]
ROW_Y = [3.15, 5.50]
ROBI_WAVE = "b_s01_05.png"


def stop(number):
    return next(entry for entry in STOPS if entry[0] == number)


def stop_label(number):
    """Text of the pill shown top left on every slide of a stop."""
    return f"STOP {number} · {stop(number)[1].upper()}"


def stop_spot(number):
    """Centre of a stop's circle on the map."""
    return COLUMN_X[(number - 1) % 5], ROW_Y[(number - 1) // 5]


def journey_map(kit, slide, current):
    """Draw the day's nine stops in two rows. Stops before `current` get a tick,
    and the current stop gets a yellow ring."""
    kit.dashed_line(slide, COLUMN_X[0], ROW_Y[0], COLUMN_X[4], ROW_Y[0])
    kit.dashed_line(slide, COLUMN_X[0], ROW_Y[1], COLUMN_X[4] - 0.75, ROW_Y[1])
    # Robi waits at the end of the path.
    kit.picture(slide, ROBI_WAVE, COLUMN_X[4] - 0.68, ROW_Y[1] - 0.95, h=1.75)

    for after in BREAKS:
        x, y = stop_spot(after)
        x += (COLUMN_X[1] - COLUMN_X[0]) / 2
        kit.circle(slide, x - 0.26, y - 0.26, 0.52, WHITE, line=PATH_TAN, line_width=1.5)
        kit.icon(slide, "p_s12_02.png", x - 0.16, y - 0.16, 0.32, ORANGE)
        kit.text(slide, x - 0.50, y + 0.30, 1.00, 0.26, "break", 11, MUTED, font=BODY_FONT,
                 align="center")

    for number, name, _leader, _minutes, color, icon_name in STOPS:
        x, y = stop_spot(number)
        if number == current:
            kit.circle(slide, x - 0.72, y - 0.72, 1.44, None, line=YELLOW, line_width=6)
            kit.pill(slide, x - 0.78, y - 1.14, 1.56, 0.34, YELLOW, "WE ARE HERE", 12, NAVY, 100)
        icon_color = NAVY if color == YELLOW else WHITE
        kit.icon_circle(slide, x - 0.575, y - 0.575, 1.15, color, icon_name, icon_color)
        kit.circle(slide, x - 0.70, y - 0.70, 0.40, WHITE, line=PATH_TAN, line_width=1.25)
        kit.text(slide, x - 0.70, y - 0.70, 0.40, 0.40, str(number), 14, INK, align="center")
        if number < current:
            kit.icon_circle(slide, x + 0.26, y + 0.26, 0.40, GREEN, "b_s05_32.png", WHITE, 0.6)
        lines = 2 if len(name) > 17 else 1
        kit.text(slide, x - 1.10, y + 0.80, 2.20, 0.31 * lines, name, 17, INK, align="center",
                 anchor="top")
