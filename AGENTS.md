# COMP2S01

This repository holds independent coursework projects. Run commands from the project directory that owns them. The repository has no shared build or test tooling.

| Directory | Project and local instructions |
| --- | --- |
| [`hw1-momo/`](hw1-momo/AGENTS.md) | *Momo Learns to Munch*, an educational AI game and its Remotion intro video. |
| [`hw1-math-meteor-defense/`](hw1-math-meteor-defense/AGENTS.md) | *Math Meteor Defense*, a single-file maths game and its preserved MVP for the Assignment 1 live demo. |
| [`workshop/`](workshop/AGENTS.md) | *Taming AI*, a service-learning workshop for Primary 5–6 learners in the Philippines. Teaching materials are organised by day. The shared proposal is maintained in Google Docs, and course requirements are under `workshop/docs/guidelines/`. |

## Repository conventions

- Put new assignments in `hwN-<name>/` and new in-class work in `inclassN-<name>/`. Add a `README.md` and include an `AGENTS.md` when the project needs its own instructions.
- Keep presentation milestones recoverable with annotated tags named `<prefix>-v<version>`. The [root README](README.md) lists existing tags. Momo uses `hw1-v*`. Math Meteor Defense uses `hw1-meteor-v*` and is located at `inclass1-math-meteor-defense/` at those tags.
- Put project-specific ignore rules in the shared root `.gitignore` with the project path in the pattern. Follow existing project-local ignore files for generated outputs.
