# Combined Day 1 deck

`Taming_AI_Day1_Combined.pptx` is the combined teaching deck.

`build/` contains its source, the original Billy deck in `base/`, extracted teaching assets in `assets/`, and prepared Robi cutouts in `figures/`. Keep those inputs: the Day 2 slides also reference the Robi cutouts. Shared original artwork lives in `../../assets/`.

Build from this folder with Python, `python-pptx`, Pillow, NumPy and lxml:

```sh
python3 build/build_day1.py build/base/billy.pptx build/assets build/cache Taming_AI_Day1_Combined.pptx build/figures
```

Inspect the result after rebuilding. Overview images and caches are generated previews and are not tracked.
