# Billy’s Day 2 slides

`Taming_AI_Day2_Billy.pptx` is the local PowerPoint export of the current 14-slide presentation:

- Slides 1–8: Prompt Power-up, 20 minutes. Clear tasks, context, output format, example-based prompting and follow-up conversations.
- Slides 9–14: Flashcard Studio 2, 20 minutes. Pictures, readable design, assembly and handover to Yelina.

These blocks occur at different points in the full Day 2 schedule.

`assets/` holds six generated illustrations and their generation prompts. `build/slides.mjs` contains the original slide builders. `build/revise-prompting.mjs` applies the approved teaching-content revision to that original 12-slide draft. It is a guarded, one-time migration; do not rerun it on the revised deck.

The modules run inside a connected presentation Artifact Session. They are not standalone PowerPoint exporters. The first draft’s cover was authored directly in the session. The saved presentation is the authoritative editable deck; export PowerPoint from its viewer when needed.

For an original draft, apply `reviseCore`, `addExample`, `addConversation`, and `orderAndCheck` in that order, each in a separate session call. Review all rendered pages after changes. Robi cutouts are reused from `../../day1/slides/build/figures/`.

`build/export-pptx.mjs` exports a saved presentation snapshot from the ignored `build/export-cache/presentation.json`, embedding local artwork. The snapshot must come from the current saved presentation. Run with the bundled Artifact Tool runtime, then validate the candidate before replacing the final PPTX.
