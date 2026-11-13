"""The pictures made with ChatGPT in the new Robi look, and which old picture each replaces.

ChatGPT drew several figures on one transparent sheet. This cuts each sheet into
single figures named as in SHEETS, and copies the two scenes:

    python3 -E figures.py <folder-with-the-chatgpt-pictures> <out-folder>
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# Words in the downloaded file's name -> (rows, columns) and the figures in reading order.
SHEETS = {
    "Waving": ((1, 1), ["robi_wave"]),
    "Excitement": ((1, 2), ["robi_cheer", "robi_question"]),
    "Progress": ((1, 3), ["robi_explain", "robi_unsure", "robi_loading"]),
    "Chef and Monster": ((1, 2), ["robi_chef_wave", "robi_monster"]),
    "Guide": ((1, 2), ["robi_guide", "robi_buddy"]),
    "in Action": ((1, 3), ["robi_megaphone", "robi_artist", "robi_trophy"]),
    "Smart Device": ((1, 5), ["obj_calculator", "obj_face_unlock", "obj_vacuum", "obj_microwave",
                              "obj_keyboard"]),
    "Rules": ((2, 3), ["robi_rules", "robi_privacy", "robi_detective", "robi_thinking", "robi_no",
                       "robi_pompoms"]),
    "Filipino": ((2, 4), ["obj_flashcards", "obj_storybook", "obj_game", "obj_essay", "food_rice",
                          "food_meat", "food_fruits", "food_sweets"]),
    "Chef Sticker Trio": ((1, 3), ["robi_results", "robi_chef_explain", "robi_chef_stars"]),
}
SCENES = {"Hammock": "scene_break", "Doodle": "scene_doodles"}

# Old picture -> the new figures that can take its place, best first. A figure that has
# not been made is skipped, so the old picture stays until one of them exists.
SWAPS = {
    "b_s01_05.png": ["robi_wave"],
    "b_s07_26.png": ["robi_cheer"],
    "b_s03_06.png": ["robi_question"],
    "b_s05_29.png": ["robi_loading"],
    "b_s06_07.png": ["robi_explain"],
    "b_s11_27.png": ["robi_unsure"],
    "b_s17_08.png": ["robi_results", "robi_question"],
    "b_s16_12.png": ["robi_chef_wave"],
    "b_s18_13.png": ["robi_chef_explain", "robi_chef_wave"],
    "b_s19_12.png": ["robi_chef_stars", "robi_chef_wave"],
    "b_s10_07.png": ["robi_monster"],
    # Payton's three characters become Robi in three roles.
    "p_s13_02.png": ["robi_monster"],
    "p_s13_06.png": ["robi_guide"],
    "p_s13_10.png": ["robi_buddy"],
    # Payton's reaction pictures (a frog meme and GIFs of real people).
    "p_s05_02.gif": ["robi_rules"],
    "p_s06_07.gif": ["robi_privacy"],
    "p_s08_08.gif": ["robi_detective"],
    "p_s09_09.gif": ["robi_thinking"],
    "p_s19_10.gif": ["robi_no"],
    "p_s23_10.gif": ["robi_no"],
    "p_s35_08.gif": ["robi_pompoms"],
}

SCALE = 4          # the sheet is searched at a quarter of its size
SOLID = 40         # alpha above this counts as part of a figure
GLOW_SHARE = 0.04  # a sheet with more half-transparent pixels than this has a glow to remove
TALLEST = 1000     # a cut figure is saved at most this many pixels tall


def _regions(mask):
    """Label the connected regions of a small boolean mask. Returns (labels, count)."""
    height, width = mask.shape
    labels = np.zeros(mask.shape, dtype=np.int32)
    count = 0
    for y, x in zip(*np.nonzero(mask)):
        if labels[y, x]:
            continue
        count += 1
        labels[y, x] = count
        stack = [(y, x)]
        while stack:
            cy, cx = stack.pop()
            for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                if 0 <= ny < height and 0 <= nx < width and mask[ny, nx] and not labels[ny, nx]:
                    labels[ny, nx] = count
                    stack.append((ny, nx))
    return labels, count


def _reading_order(boxes, rows, columns):
    """Indexes of `boxes` (x0, y0, x1, y1) sorted row by row, left to right."""
    by_height = sorted(range(len(boxes)), key=lambda i: boxes[i][1] + boxes[i][3])
    order = []
    for row in range(rows):
        band = by_height[row * columns:(row + 1) * columns]
        order += sorted(band, key=lambda i: boxes[i][0] + boxes[i][2])
    return order


def _spread(owner, steps):
    """Let every figure claim the empty pixels next to it, `steps` pixels deep."""
    for _ in range(steps):
        grown = owner.copy()
        for shifted in (np.roll(owner, 1, 0), np.roll(owner, -1, 0),
                        np.roll(owner, 1, 1), np.roll(owner, -1, 1)):
            empty = grown == 0
            grown[empty] = shifted[empty]
        owner = grown
    return owner


def _shrink(mask):
    """Take one pixel off the edge of every region."""
    inner = mask.copy()
    inner[1:, :] &= mask[:-1, :]
    inner[:-1, :] &= mask[1:, :]
    inner[:, 1:] &= mask[:, :-1]
    inner[:, :-1] &= mask[:, 1:]
    inner[0, :] = inner[-1, :] = inner[:, 0] = inner[:, -1] = False
    return inner


def _cores(mask, wanted, name):
    """Find one core region per figure. Stickers whose borders touch count as one region,
    so the mask is shrunk until `wanted` regions of similar size stand apart.
    Returns (labels, boxes), with the figures labelled 1..wanted."""
    for _ in range(40):
        labels, count = _regions(mask)
        sizes = [(int((labels == label).sum()), label) for label in range(1, count + 1)]
        sizes.sort(reverse=True)
        if count >= wanted and sizes[wanted - 1][0] * 4 >= sizes[0][0]:
            cores = np.zeros_like(labels)
            boxes = []
            for number, (_size, label) in enumerate(sizes[:wanted], start=1):
                ys, xs = np.nonzero(labels == label)
                cores[labels == label] = number
                boxes.append((xs.min(), ys.min(), xs.max(), ys.max()))
            return cores, boxes
        mask = _shrink(mask)
    raise ValueError(f"{name}: could not tell {wanted} figures apart")


def cut_sheet(path, rows, columns):
    """Split one transparent sheet into rows x columns figures, in reading order.

    The biggest regions are the figures; smaller loose bits (sparks, a question mark,
    a light bulb) join the figure they are closest to."""
    sheet = Image.open(path).convert("RGBA")
    pixels = np.asarray(sheet).copy()
    alpha = pixels[..., 3].astype(np.float32)
    if ((alpha > 10) & (alpha < 200)).mean() > GLOW_SHARE:
        # A soft glow around the stickers: keep only the solid part, with a short ramp.
        alpha = np.clip((alpha - 120) * 255 / 90, 0, 255)
        pixels[..., 3] = alpha.astype(np.uint8)

    height, width = alpha.shape
    small_h, small_w = -(-height // SCALE), -(-width // SCALE)
    padded = np.zeros((small_h * SCALE, small_w * SCALE), dtype=bool)
    padded[:height, :width] = alpha > SOLID
    small = padded.reshape(small_h, SCALE, small_w, SCALE).any(axis=(1, 3))

    wanted = rows * columns
    cores, core_boxes = _cores(small, wanted, path.name)
    order = _reading_order(core_boxes, rows, columns)
    owner = np.zeros(small.shape, dtype=np.int32)
    for number, index in enumerate(order, start=1):
        owner[cores == index + 1] = number
    # Each core grows back to its full figure, stopping where it meets a neighbour.
    while True:
        grown = np.where(small, _spread(owner, 1), 0)
        if (grown == owner).all():
            break
        owner = grown

    # Loose bits the figures did not reach join the figure they are closest to.
    figure_boxes = []
    for number in range(1, wanted + 1):
        ys, xs = np.nonzero(owner == number)
        figure_boxes.append((xs.min(), ys.min(), xs.max(), ys.max()))
    loose, count = _regions(small & (owner == 0))
    for label in range(1, count + 1):
        ys, xs = np.nonzero(loose == label)
        cx, cy = xs.mean(), ys.mean()

        def distance(box):
            x0, y0, x1, y1 = box
            return max(x0 - cx, 0, cx - x1) ** 2 + max(y0 - cy, 0, cy - y1) ** 2

        owner[loose == label] = 1 + min(range(wanted), key=lambda n: distance(figure_boxes[n]))
    owner = _spread(owner, 3)
    owner = np.repeat(np.repeat(owner, SCALE, axis=0), SCALE, axis=1)[:height, :width]

    cut = []
    for number in range(1, wanted + 1):
        part = pixels.copy()
        part[..., 3] = np.where(owner == number, part[..., 3], 0)
        image = Image.fromarray(part, "RGBA")
        cut.append(image.crop(image.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()))
    return cut


def _find(folder, words):
    matches = [path for path in sorted(folder.iterdir())
               if words in path.name and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    return matches[0] if matches else None


def cut_all(source, out):
    source, out = Path(source), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    for words, ((rows, columns), names) in SHEETS.items():
        path = _find(source, words)
        if path is None:
            print(f"missing: a sheet with {words!r} in its name ({', '.join(names)})")
            continue
        for name, image in zip(names, cut_sheet(path, rows, columns)):
            if image.height > TALLEST:
                # More than a slide can show; a smaller file keeps the deck light.
                image = image.resize((round(image.width * TALLEST / image.height), TALLEST),
                                     Image.LANCZOS)
            image.save(out / f"{name}.png", optimize=True)
            print(f"{name}: {image.width}x{image.height}  from {path.name}")
    for words, name in SCENES.items():
        path = _find(source, words)
        if path is None:
            print(f"missing: a scene with {words!r} in its name ({name})")
            continue
        Image.open(path).convert("RGB").save(out / f"{name}.png")
        print(f"{name}: scene from {path.name}")


if __name__ == "__main__":
    cut_all(*sys.argv[1:3])
