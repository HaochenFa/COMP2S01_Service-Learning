# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in `workshop/`, part of the COMP2S01 monorepo.

## What this is

The team's service-learning workshop, *Taming AI: Learning to Use AI Wisely, Fairly, and for Good*. It is taught to Primary 5–6 learners in the Philippines with UP Diliman partner students, in January 2027. There are 4 teaching days of 3 hours each plus a Day 5 showcase and reflection, and the same plan runs for an AM and a PM group. Learners make four products: AI flashcards, an AI-assisted storybook with audio, an educational web game built with AI, and a before-AI / after-AI reflection essay.

The team is Billy (Computing, the owner of this repo), Yelina (Supply Chain Management and Analytics), Payton (Radiography) and Raiyan (Mechanical Engineering).

## Files

- `docs/guidelines/` holds the course's own documents. Treat them as read-only. Every plan is checked against them:
  - `COMP2S01_261_Taming AI_Project Expectations_Philippines.pdf`: the brief, with learning objectives, theme, tools and the four required outputs and their specs.
  - `COMP2S01_261_Workshop Proposal_TEMPLATE.docx`: the proposal format and workshop objectives A–F.
  - `COMP2S01_Assessment_Rubrics.pdf` and `COMP2S01_Assessment_Components.pdf`: grading. Proposal 10%, teaching materials 15%, individual service performance 40%, reflective journal 30%, class performance 5%.
- `proposal/workshop-proposal.docx` is the proposal itself and the source of truth for the timetable, who leads what, and deadlines (Part 3).
- `proposal/Taming_AI_Proposal_Presentation.pptx` and `proposal/Taming_AI_Day1_Lesson.pptx` are the proposal deck and the Day 1 lesson slides. They were made before the review fixes, so they still describe the old plan (for example, a paper game on Day 4). Bring them in line with the docx before they are used.
- `Taming-AI-team-brief.pdf` is a two-page summary of the proposal for teammates: the products, the week, the rules, the Day 4 web game, who leads what, and deadlines. It was printed from HTML with headless Chrome, and the HTML source isn't kept, so rebuild it from the docx when the plan changes.
- `proposal-review.md` reviews the proposal against the brief, template and rubric, through each member's discipline, and includes an activity bank. Its sources are dated 15 Oct 2026, and its free-tier numbers are unofficial.

## Rules the proposal must keep

From the template and rubric:
- Every activity row has the 7 fields: Topic, Description, Objective, In-charge, Duration, Materials, Evaluation Plan.
- No activity is longer than 30 min, and no session longer than 3 h. Days 1–4 total 180 min each (including one 10-min break) and Day 5 totals 170. Re-add the minutes after any timetable change.
- Objectives A–F must all be covered, including "music" in B.
- The A-band rubric asks for variety (games, hands-on, exercises, quizzes, videos, online interactive tools, props) and for plans that evaluate learning, not just finished products.

From the owner:
- **Only free AI during teaching.** This applies to facilitators and learners alike: free ChatGPT, Gemini and Claude, and Chinese AI such as DeepSeek, Qwen and Kimi, which is recommended alongside them. Materials prepared beforehand may use any tool. Learners never sign in; each group uses a facilitator-signed-in laptop, and no personal information goes into AI tools. Keep Grok away from the children.
- **10 or fewer learners per session.** Free image quotas and the free Kahoot player limit are fine at this size, so don't redesign around them. Revisit them if the class grows.
- **The game is a web game.** The brief's "interactive educational AI game" means learners design it on paper, then build a single-file HTML game by prompting free AI (DeepSeek first). The game must have rules, 3 levels and a score, and run offline from the saved `.html` file.
- **Majors are optional.** A member's discipline may supply an example, but only when it teaches an objective better than a generic example would. Don't add content just so every major appears.
- Work from what the brief explicitly says, and label your own ideas as suggestions.
- Keep activities kid-oriented (ages about 10–12) while still effective: teacher talk of 5 min or less before hands-on, local Philippine examples, short text, and both English and Filipino on instruction cards.

## Editing Office files

- Edit `.docx` and `.pptx` with a proper library (python-docx, python-pptx) so the formatting survives. Never hand-edit the XML with string replacement.
- After changing a `.docx`, export it through Microsoft Word (AppleScript) and look at the result before calling it done. LibreOffice has hidden broken layouts before. Keep table rows together with table-row settings, not chains of "keep with next".
- To read a file quickly: `textutil -convert txt -stdout proposal/workshop-proposal.docx` (docx), `pdftotext -layout <file> -` (pdf).

## Versions

Annotated git tags named `workshop-v<version>`. `workshop-v0` is the first committed version: the proposal with the review's fixes applied, the review, and the Day 1 / proposal decks, which have not been updated yet.
