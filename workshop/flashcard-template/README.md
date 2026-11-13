# Flashcard templates

Ten blank cards follow the proposal’s suggested balance: three AI knowledge, three applications, and four responsible-use cards. Two additional cards are teaching examples, not part of the learner deck.

## Files

- `assets/`: three image-generated backgrounds, sample illustrations and generation prompts.
- `output/Taming_AI_Flashcard_Templates.pdf`: twelve individual cards; source for the Canva import.
- `output/Taming_AI_Flashcards_A4_Print.pdf`: three A4 sheets, four cards per sheet, with trim marks.
- `output/How_to_use.txt`: editing and printing instructions.
- `output/*_Preview.png`: blank-card and completed-example previews.
- `build/make_templates.py`: PDF generator.

Cards measure 90 × 135 mm. Print at 100% / Actual size. Canva text remains editable; the decorative frame and Robi form the background image. Replace placeholder text and remove the bilingual hints when completing a card.

## Rebuild

Requires Python with ReportLab and Pillow. Install the Fredoka and Lexend variable TTF fonts. The default font folder is `~/Library/Fonts`; set `WORKSHOP_FONT_DIR` to another folder containing `Fredoka[wdth,wght].ttf` and `Lexend[wght].ttf` when needed.

```sh
python3 build/make_templates.py
```

Render both PDFs and inspect every page after rebuilding. Diagnostic renders and the optional ZIP package are excluded from Git. A rebuild does not change the imported Canva design.
