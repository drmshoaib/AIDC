# AIDC — Applied Industrial Data Science

Course repository for **Applied Industrial Data Science**, BS Data Science and
BS Data Analytics, GC University Faisalabad.

Each week's lab is published here as its own folder. This repository is the
**reference copy**: you read from it, you do not write to it.

---

## Getting the labs

Clone once, near the start of the course. You do not need a GitHub account to
do this.

```bash
git clone https://github.com/drmshoaib/AIDC.git
cd AIDC
```

Each following week, collect the new folder with:

```bash
git pull
```

Run `git pull` from inside the `AIDC` folder. Do not clone again.

---

## What to do in each week's folder

Every week folder is a complete, runnable project. Start with its two
documents, in this order:

1. `SETUP.md` — how to install Python, VS Code, the two VS Code extensions,
   and Git. Only needed once, before Week 1.
2. `README.md` — what you have to produce that week, where every file lives,
   and what each one is for.

| Week | Slides | Lab | Topic |
| --- | --- | --- | --- |
| 1 | [PDF](Week_01_Lecture_slides.pdf) | [`week01/`](week01/) | From models to decision systems: diagnostic, project structure, command line and Git |
| 2 | [PDF](Week_02_Lecture.pdf) | [`week02/`](week02/) | Problem framing, stakeholders and data suitability |
| 3 | [PDF](Week_03_Lecture_Slides.pdf) | Classroom 50 | Data quality and validation |
| 4 | [PDF](Week_04_Lecture_Slides.pdf) | Classroom 50 | Reproducible project architecture and repository hygiene |
| 5 | [PDF](Week_05_Lecture_Slides.pdf) | Classroom 50 | Baseline modelling on validated data |
| 6 | [PDF](Week_06_Lecture_Slides.pdf) | Classroom 50 | Model interpretation, uncertainty and limitations |
| 7 | [PDF](Week_07_Lecture_Slides.pdf) | Classroom 50 | Residual analysis and error diagnosis |
| 8 | [PDF](Week_08_Lecture_Slides.pdf) | Classroom 50 | The capstone projects |
| 9 | [PDF](Week_09_Lecture_Slides.pdf) | Classroom 50 | Testing your code and your data |

From Week 3, each lab is your own Classroom 50 repository, so only the slides
are published here. Later weeks appear here as the course runs.

---

## How you hand work in

**Week 1 — a local commit.** This repository is read-only, so you cannot push
to it. Work inside your clone, then `git add` and `git commit` your files. The
commit stays on your machine, and that is the expected result for Week 1. Your
Week 1 README explains exactly which files to stage.

**Week 2 onward — your own repository.** You will be invited to the course
GitHub organisation and given your own private repository for each assignment,
created from a template. You will push to that repository, not to this one.
Bring a working GitHub account to the Week 2 lab.

If anything about that invitation or your account does not work, record it in
your `docs/readiness_note.md` and raise it in the lab. There is no penalty for
a platform-access problem.

---

## Ground rules

- **Never edit anything in a `data/raw/` folder.** That data is deliberately
  imperfect; finding and documenting the faults is part of the work.
- **Never commit secrets.** No passwords, no personal access tokens, no `.env`
  files, no private data. Run `git status` before every commit and check what
  you are about to record. Each week's `.gitignore` already excludes the usual
  offenders.
- **Keep one local copy** of this repository. Pull it, do not re-clone it.

---

## Getting help

Bring the exact command and the full error message. An honest incomplete
attempt is far more useful than copied output, and it is the only way support
can be targeted at the right thing.

Instructor: Dr. Muhammad Shoaib, Muhammad.shoaib@utopi.co.uk
