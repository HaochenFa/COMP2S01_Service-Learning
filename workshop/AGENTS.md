# Taming AI workshop

*Taming AI: Learning to Use AI Wisely, Fairly, and for Good* is a January 2027 service-learning workshop for Primary 5–6 learners in the Philippines with UP Diliman partner students. Plan for about 10 learners in two groups of five. There are four teaching days of three hours each and a Day 5 showcase with a 45-minute reflection session. The four products are AI flashcards, an AI-assisted storybook with audio, an educational web game built with AI, and a before-AI / after-AI reflection essay.

The team is Billy (Computing), Yelina (Supply Chain Management and Analytics), Payton (Radiography) and Raiyan (Mechanical Engineering).

## Sources and files

- The shared Drive folder is **Group 12 - Final Workshop Proposal and Teaching Materials**. Find files by title. Keep private document links, IDs and contact information out of the repository.
- **COMP2S01 Workshop Proposal** is the shared Google Doc and the source of truth for the timetable, roles and Part 3 deadlines. Teammates edit it too. Read the current document before editing it.
- **Feedback on Workshop Proposal & Day 1** records the teachers' November 2026 feedback. Billy's individual Day 1 materials are **Taming_AI_Day1_Billy** and **Taming AI Day 1 – Billy: Lesson Plan**.
- See [README.md](README.md) and each day's README for teaching sources, artwork and exports. Billy's Day 2 editable slide deck is the saved presentation in its authoring chat. The editable flashcards are in Canva as **Taming AI — Flashcard Templates (10 cards + 2 examples)**.
- [day1/robi-video/README.md](day1/robi-video/README.md) covers the 75-second “How does a computer learn?” Remotion video (Teach Robi) that opens Billy's Day 1 machine-learning block. Run video commands from `day1/robi-video/` and keep rendered video and generated audio out of Git.
- Treat `docs/guidelines/` as read-only. Check workshop work against the project expectations PDF for the learning objectives, tools and product specs. Use the proposal template for the required format and objectives A–F. The assessment documents give the weights of 10% proposal, 15% teaching materials, 40% individual service performance, 30% reflective journal and 5% class performance.
- Annotated workshop milestones use `workshop-v<version>`. `workshop-v0` preserves the revised local proposal, review and early decks from before the move to Google Docs. Earlier local files including the team brief are also recoverable from `e7f907d`.

## Proposal and timetable

- Include all seven fields in each activity row (Topic, Description, Objective, In-charge, Duration, Materials and Evaluation Plan). Keep activities at 30 minutes or less and sessions at three hours or less. Days 1–4 each total 180 minutes including two 10-minute breaks. Recalculate the totals after changing the timetable.
- Cover objectives A–F, including music in objective B. For the A-band rubric, use varied activities such as games, hands-on practice, quizzes, videos, interactive tools and props. Plan how to assess what learners understood as well as what they made.
- Use one coordinated deck per day, with a shared theme, transitions and a schedule at the start. Assign one member to oversee the whole schedule. Close each teaching day with a Kahoot and a separate recap.
- Use the AI Monster metaphor across the workshop, and include active games to hold attention. Plan the reflection essay for Day 5 and prepare reflection and feedback questions for that session.
- Include one UPD teammate in the logistics plan. The HKD 500 materials budget excludes AI credits and food. Bring an HDMI cable.

### Day 1 plan agreed on 12 November 2026

Check the proposal for the latest activity rows.

| Order | Activity | Lead | Minutes |
| --- | --- | --- | ---: |
| 1 | Welcome, ice-breaking and intro | Yelina, with the full team | 30 |
| 2 | Workshop overview | Payton | 10 |
| 3 | Machine learning, intro video and Teachable Machine | Billy | 30 |
| 4 | ML practice with Quick, Draw! Race | Raiyan | 8 |
| 5 | Break | | 10 |
| 6 | Meet GenAI and the Prompt Recipe | Billy | 20 |
| 7 | GenAI practice with Is it AI? | Raiyan | 12 |
| 8 | Break | | 10 |
| 9 | AI ethics with Monster, Guide or Buddy? | Payton | 20 |
| 10 | Kahoot exit quiz and pre-quiz | Raiyan | 15 |
| 11 | Wrap-up and recap | Yelina | 15 |

- Billy introduces each concept and demonstrates it before hands-on work. Raiyan follows with a practice activity.
- Learners experience data bias when the Teachable Machine model trained on one-sided hand examples fails. Payton links back to this example when teaching AI bias on Day 2.
- Introduce flashcards in Day 2's Flashcard Studio 1. Keep the five pre-quiz questions from Day 1 for reuse in the Day 5 reflection.

## Teaching constraints

- Use free AI tools in class for learners and facilitators. DeepSeek is the general prompting default, with Kimi, Gemini and ChatGPT as complements and backups. Materials prepared ahead of class may use any tool. Groups use facilitator-signed-in laptops. Learners do not sign in, enter personal information into AI tools or use Grok.
- Plan around about 10 learners. Recheck free image quotas and Kahoot capacity if the class grows.
- For Day 4, learners design an educational game on paper, suggest ideas and test the results while facilitators operate the laptops. Use OpenCode with a free model tested before class. Deliver a single HTML file with rules, three levels and a score that runs offline when opened. The Day 4 slide README documents the live demo workflow in the Day 4 materials.
- Use a team member's discipline when it helps teach the objective. Distinguish course requirements from suggestions.
- Use local Philippine examples, short copy for ages 10–12 and English and Filipino on instruction cards. Keep explanations before hands-on work to five minutes or less.

## Editing and checking deliverables

- Edit the existing proposal in place through the Google Docs connector to preserve the shared link. For precise edits, calculate positions programmatically from a current structured read. To reorder existing table rows, rewrite the cell text in a single batch starting from the highest document position.
- Keep proposal table text in Calibri 9 pt, with the Topic cell in bold. Preserve teammates' wording unless the requested edit calls for changing it.
- After editing the proposal, re-read the affected part, recalculate the day's total and inspect a PDF export.
- Use an appropriate library for local Word and PowerPoint artifacts, such as `python-docx` or `python-pptx`. Verify Word layout using Microsoft Word's export when available because LibreOffice has masked layout defects in prior files.
- Keep generated illustrations and final teaching deliverables. Exclude temporary page renders, diagnostic PDFs, caches and duplicate ZIP bundles from Git.
