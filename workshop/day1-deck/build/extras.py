"""Slides that belong to the whole day, not to one member: the map before each stop,
the breaks, and the placeholders for the two stops that have no slides yet."""
from day1 import BREAKS, journey_map, stop
from deckkit import BODY_FONT, INK, MUTED, NAVY, ORANGE, PATH_TAN, TINT, WHITE, YELLOW
from layouts import LEFT, ROBI_HAPPY, WIDTH, accent_text, header, photo, stop_color

KAHOOT = 8
WRAP_UP = 9
KAHOOT_LINK = "https://create.kahoot.it/share/day-1-lesson/112aa49f-9e2e-46ef-9452-a83c18c87a85"


def next_stop_map(kit, number):
    """Shown before a stop starts: where we are in the day, and who leads next."""
    _number, name, leader, minutes, color, _icon = stop(number)
    slide = kit.slide("PAPER", notes=f"Transition. Stop {number}: {name}, led by {leader} "
                                     f"({minutes} min).")
    kit.title(slide, [[("Next stop: ", INK), (name, accent_text(color))]])
    journey_map(kit, slide, number)
    return slide


def break_slide(kit, after):
    """The break that follows stop `after`."""
    minutes = BREAKS[after]
    _number, next_name, _leader, _minutes, next_color, _icon = stop(after + 1)
    slide = kit.slide("PAPER", notes=f"Break: {minutes} minutes. Then {next_name}.")
    scene = kit.figure("scene_break")
    if scene:
        # Robi resting on the beach fills the right half; the words sit on the left.
        kit.icon_circle(slide, LEFT + 0.05, 1.55, 1.05, YELLOW, "p_s12_02.png", NAVY, 0.5)
        kit.text(slide, LEFT, 2.75, 5.60, 1.20, "Break time!", 66, INK)
        kit.text(slide, LEFT + 0.05, 3.95, 5.60, 0.70, f"Back in {minutes} minutes", 30, MUTED,
                 font=BODY_FONT)
        # A smaller pill than usual, so the longest stop name still ends before the picture.
        label = f"Next: {next_name}"
        kit.pill(slide, LEFT + 0.05, 5.05, 0.165 * len(label) + 0.55, 0.62, next_color, label, 20,
                 NAVY if next_color == YELLOW else WHITE)
        photo(kit, slide, scene, 6.70, 1.70, 6.03)
        return slide
    kit.icon_circle(slide, LEFT + 0.20, 2.35, 2.30, YELLOW, "p_s12_02.png", NAVY, 0.5)
    kit.text(slide, LEFT + 3.00, 2.20, 6.50, 1.40, "Break time!", 72, INK)
    kit.text(slide, LEFT + 3.05, 3.70, 6.50, 0.70, f"Back in {minutes} minutes", 30, MUTED,
             font=BODY_FONT)
    kit.next_pill(slide, f"Next: {next_name}", next_color, x=LEFT + 3.05, y=4.85)
    kit.picture(slide, ROBI_HAPPY, 10.05, 2.20, h=3.50)
    return slide


def placeholder(kit, number, title, owner, covers, extra=None):
    """A clearly marked slide for a stop whose owner has not made slides yet."""
    slide = kit.slide("PAPER", notes=f"PLACEHOLDER. {owner} has not made slides for this stop yet. "
                                     "The list on the slide is copied from the proposal's Day 1 "
                                     "table, as a reminder of what the stop covers.")
    header(kit, slide, number, None, title)
    kit.box(slide, LEFT, 2.15, WIDTH, 4.30, WHITE, radius=0.30, line=PATH_TAN, line_width=2.5,
            dashed=True)
    kit.pill(slide, LEFT + 0.40, 2.45, 4.60, 0.44, TINT[YELLOW],
             f"PLACEHOLDER · {owner.upper()} TO ADD SLIDES", 13, NAVY, 100)
    kit.text(slide, LEFT + 0.45, 3.05, 8.00, 0.40, "The proposal says this stop covers:", 16, MUTED,
             font=BODY_FONT)
    y = 3.55
    for line in covers:
        rows = 2 if len(line) > 95 else 1
        kit.circle(slide, LEFT + 0.50, y + 0.17, 0.13, stop_color(number))
        kit.text(slide, LEFT + 0.85, y, WIDTH - 1.40, 0.36 * rows, line, 18, INK, font=BODY_FONT,
                 anchor="top")
        y += 0.36 * rows + 0.22
    if extra:
        kit.text(slide, LEFT + 0.45, y + 0.12, WIDTH - 0.90, 0.40, extra, 13, MUTED,
                 font=BODY_FONT)
    return slide


def kahoot_placeholder(kit):
    return placeholder(
        kit, KAHOOT, "Kahoot quiz", "Raiyan",
        ["Kahoot: 5 questions on today and 5 pre-quiz questions that return on Day 5.",
         "Review any of today’s questions most learners missed."],
        extra=f"Link from Raiyan’s deck: {KAHOOT_LINK}")


def wrap_up_placeholder(kit):
    return placeholder(
        kit, WRAP_UP, "Wrap-up & Recap", "Yelina",
        ["Recap today’s big ideas together: AI learns from data, GenAI makes new things from "
         "prompts, and AI can be a Monster, a Guide or a Buddy.",
         "Each learner writes “One thing I learned” on a sticky note.",
         "Preview Day 2: AI becomes our Guide, and we start making our flashcards."])
