# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in `workshop/`, part of the COMP2S01 monorepo.

## What this is

The team's service-learning workshop, *Taming AI: Learning to Use AI Wisely, Fairly, and for Good*. It is taught to Primary 5–6 learners in the Philippines with UP Diliman partner students, in January 2027. There are 4 teaching days of 3 hours each, and Day 5 is the showcase day, for which only a 45-minute reflection session is planned. Each session has about 10 learners in two groups of about 5. Learners make four products: AI flashcards, an AI-assisted storybook with audio, an educational web game built with AI, and a before-AI / after-AI reflection essay.

The team is Billy (Computing, the owner of this repo), Yelina (Supply Chain Management and Analytics), Payton (Radiography) and Raiyan (Mechanical Engineering).

## Where things are

The shared proposal and team deliverables live in Google Drive, in "Group 12 - Final Workshop Proposal and Teaching Materials". Find files by title with Drive search. Local teaching sources, artwork and exported deliverables are also versioned here; see `README.md` for the folder guide. Billy's Day 2 editable deck is in the saved presentation in the chat, and the flashcard template is in Canva. Do not write private document IDs or links into this repo: the proposal holds teammates' phone numbers.

- Google Doc "COMP2S01 Workshop Proposal" is the proposal and the source of truth for the timetable, who leads what, and deadlines (Part 3). Teammates edit it too, so read it fresh before every change.
- Google Doc "Feedback on Workshop Proposal & Day 1" is the teachers' feedback on the submitted proposal and the Day 1 materials (November 2026).
- Each member keeps their own Day 1 materials there. Billy's are the Google Slides deck "Taming_AI_Day1_Billy" and the Google Doc "Taming AI Day 1 – Billy: Lesson Plan".

In this repo:

- `docs/guidelines/` holds the course's own documents. Treat them as read-only. Every plan is checked against them:
  - `COMP2S01_261_Taming AI_Project Expectations_Philippines.pdf`: the brief, with learning objectives, theme, tools and the four required outputs and their specs.
  - `COMP2S01_261_Workshop Proposal_TEMPLATE.docx`: the proposal format and workshop objectives A–F.
  - `COMP2S01_Assessment_Rubrics.pdf` and `COMP2S01_Assessment_Components.pdf`: grading. Proposal 10%, teaching materials 15%, individual service performance 40%, reflective journal 30%, class performance 5%.
- `day1/robi-video/` is the Remotion project for the 75-second intro video "How does a computer learn?" (Teach Robi), played at the start of Billy's Machine Learning block on Day 1. Read its `README.md` first; its commands are run from that folder. Its own `.gitignore` keeps the rendered video and generated audio out of git.

The earlier local copies (the proposal `.docx`, the proposal and Day 1 decks, the team brief PDF and `proposal-review.md`) were removed because they no longer matched the Google Doc. They are recoverable from commit `e7f907d`.

## Day 1 order

Agreed by the team on 12 November 2026, after the teachers' feedback. The proposal has the full rows.

1. Welcome, Ice-breaking & Intro: Yelina leads, all join (30 min)
2. Workshop Overview: Payton (10)
3. Machine Learning: How AI Learns, with the intro video and Teachable Machine: Billy (30)
4. ML Practice: Quick, Draw! Race: Raiyan (8)
5. Break (10)
6. Meet GenAI: The Prompt Recipe: Billy (20)
7. GenAI Practice: Is it AI?: Raiyan (12)
8. Break (10)
9. AI ethics: Monster, Guide or Buddy?: Payton (20)
10. Kahoot Quiz: Exit Quiz & Pre-quiz: Raiyan (15)
11. Wrap-up & Recap: Yelina (15)

What the order is built on:

- Billy teaches a concept, then Raiyan runs the practice for it.
- Billy's blocks explain the idea first (the intro video for machine learning), then go hands-on.
- Learners experience data bias on Day 1, when the Teachable Machine model trained on one-sided hand data fails. Payton teaches AI bias formally on Day 2 and links back to that model.
- The flashcards are introduced on Day 2 (in Flashcard Studio 1), because Day 1 was overloaded.
- A quiz is not a recap. The day ends with the Kahoot and then a separate wrap-up.
- The 5 pre-quiz questions in the Day 1 Kahoot return in the Day 5 reflection, so keep them.

## Rules the proposal must keep

From the template and rubric:
- Every activity row has the 7 fields: Topic, Description, Objective, In-charge, Duration, Materials, Evaluation Plan.
- No activity is longer than 30 min, and no session longer than 3 h. Days 1–4 total 180 min each, including two 10-min breaks. Re-add the minutes after any timetable change.
- Objectives A–F must all be covered, including "music" in B.
- The A-band rubric asks for variety (games, hands-on, exercises, quizzes, videos, online interactive tools, props) and for plans that evaluate learning, not just finished products.

From the teachers' feedback (November 2026):
- Each day uses one combined deck with a consistent theme and metaphors, with transitions between sections. One member oversees the whole schedule.
- Show the day's schedule at the start of every day, as Day 1 does.
- End each day with a recap and a Kahoot.
- Learners write the reflection essay on Day 5 only, not every day. Day 5 needs no prepared materials beyond reflective and feedback questions.
- Add some active games to hold attention. They need not be about AI.
- Use the AI Monster metaphor more often.
- Logistics: one UPD teammate joins the team; the budget for materials is HKD 500 (no AI credits, no food); bring an HDMI cable.

From the owner:
- **Only free AI during teaching.** This applies to facilitators and learners alike: DeepSeek first, with Kimi, Gemini and ChatGPT as complements and backups. Materials prepared beforehand may use any tool. Learners never sign in; each group uses a facilitator-signed-in laptop, and no personal information goes into AI tools. Keep Grok away from the children.
- **About 10 learners per session.** Free image quotas and the free Kahoot player limit are fine at this size, so don't redesign around them. Revisit them if the class grows.
- **The game is a web game.** The brief's "interactive educational AI game" means learners design it on paper, then build a single-file HTML game by prompting free AI (DeepSeek first). The game must have rules, 3 levels and a score, and run offline from the saved `.html` file.
- **Majors are optional.** A member's discipline may supply an example, but only when it teaches an objective better than a generic example would. Don't add content just so every major appears.
- Work from what the brief explicitly says, and label your own ideas as suggestions.
- Keep activities kid-oriented (ages about 10–12) while still effective: teacher talk of 5 min or less before hands-on, local Philippine examples, short text, and both English and Filipino on instruction cards.

## Editing the proposal

- Edit the Google Doc in place with the Google Docs connector, so the link the team shares stays the same. Never recreate it.
- A full read of the doc is about 840 KB and is saved to a file. Work out positions from that file with a script, not by eye.
- Table rows can't be moved. To reorder a day, rewrite the text of the cells, from the highest position to the lowest, in one batch.
- Table text is Calibri 9 pt, with the Topic cell in bold. Rows other members wrote keep their wording unless the change is asked for.
- After an edit, read the doc again, re-add the day's minutes, and export it to PDF to look at the pages.
- If a `.docx` or `.pptx` is needed again, edit it with a proper library (python-docx, python-pptx), and export a `.docx` through Microsoft Word to check the layout. LibreOffice has hidden broken layouts before.

## Versions

Annotated git tags named `workshop-v<version>`. `workshop-v0` is the first committed version: the local proposal with the review's fixes applied, the review, and the Day 1 / proposal decks, from before the proposal moved to Google Docs.
