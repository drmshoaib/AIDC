# Week 1 Student Lab — Plant Operations

Student project for **Applied Industrial Data Science** at GC University
Faisalabad. It introduces the reproducible project structure you will use for
the rest of the semester.

**New here? Read [SETUP.md](SETUP.md) first** and install your tools before the
lab. This file assumes Python, VS Code and Git are already working.

---

## What you have to produce

Four things. All four live in this folder and are handed in by committing them.

| # | Output | Where it goes |
| --- | --- | --- |
| 1 | Diagnostic attempt | `notebooks/week1_diagnostic.ipynb` |
| 2 | Labelled plot | inside the notebook, Task 4 |
| 3 | Problem statement | `docs/problem_statement.md` |
| 4 | Commit and readiness note | `docs/readiness_note.md`, plus your first commit |

The diagnostic is **ungraded**. It exists to show where you need help, not to
catch you out. An honest incomplete attempt is worth more than copied output.

---

## What to do, in order

1. **Set up.** Follow [SETUP.md](SETUP.md). Finish with
   `python src/check_setup.py` reporting 73 rows and 8 columns.
2. **Look around.** Read the file table below so you know what each folder is
   for before you touch anything.
3. **Run the project.** The three commands under "Running the project".
4. **Do the diagnostic.** Open `notebooks/week1_diagnostic.ipynb` in VS Code
   and work through Tasks 1 to 6: load and inspect, select and summarise,
   derive a measure, plot, interpret, and check data quality.
5. **Frame the decision.** Notebook Task 7 sends you to
   `docs/problem_statement.md`. Name the user, the decision, the evidence and
   the consequence, in those words.
6. **Record and commit.** Fill in `docs/readiness_note.md`, then follow the Git
   task below. Notebook Task 8 asks you to paste the commit hash.

If your setup broke at any point, write the exact command and the full error
into `docs/readiness_note.md` and carry on with what you can. That note is one
of the four outputs, not an admission of failure.

---

## Every file, and what it is for

| Path | What it is | What you do with it |
| --- | --- | --- |
| `README.md` | this file | read first |
| `SETUP.md` | how to install Python, VS Code, the extensions and Git | follow before the lab |
| `requirements.txt` | the exact package versions the course uses | install once; do not edit |
| `.gitignore` | the list of things Git must never record | do not edit |
| `.vscode/extensions.json` | tells VS Code to recommend the Python and Jupyter extensions | accept the prompt |
| `config/settings.yaml` | data paths and the named alert thresholds | read it; change nothing in Week 1 |
| `data/raw/plant_shift_log.csv` | 73 rows of simulated shift data, with deliberate faults | read only; **never edit** |
| `data/processed/.gitkeep` | keeps the folder in Git while its contents stay out | write any derived data into this folder |
| `src/loading.py` | one tested function that loads the data, plus the rejection-rate helper | import it; do not re-read the CSV by hand |
| `src/check_setup.py` | proves your environment and data path work | run it first |
| `src/model.py` | a transparent baseline rule that flags a line to inspect | run it and read it |
| `tests/test_data.py` | six pytest checks on loading and the derived measure | run them; do not edit |
| `notebooks/week1_diagnostic.ipynb` | the eight-task diagnostic | complete and commit |
| `docs/problem_statement.md` | the framing template | complete and commit |
| `docs/readiness_note.md` | where setup problems and your Git evidence go | complete and commit |

```text
week01/
├── README.md                   # you are here
├── SETUP.md                    # install guide, read this first
├── requirements.txt            # pinned package versions
├── .gitignore                  # what Git must never track
├── .vscode/
│   └── extensions.json         # recommends the two VS Code extensions
├── config/
│   └── settings.yaml           # data paths and named thresholds
├── data/
│   ├── raw/                    # immutable teaching data; do not edit
│   └── processed/              # your derived outputs; contents ignored by Git
├── src/
│   ├── check_setup.py          # verifies the environment and data path
│   ├── loading.py              # configured, reusable data loading
│   └── model.py                # transparent Week 1 baseline preview
├── tests/
│   └── test_data.py            # introductory pytest checks
├── docs/
│   ├── problem_statement.md    # output 3, complete during the lab
│   └── readiness_note.md       # output 4, setup problems and Git evidence
└── notebooks/
    └── week1_diagnostic.ipynb  # outputs 1 and 2, the diagnostic
```

The model, the configuration and the tests are **previews** of practices taught
later in the course. In Week 1 you only need to run them and understand what
they are for. You are not expected to redesign them.

---

## Running the project

Open the `week01` folder in VS Code and use its integrated terminal, from the
project root:

```bash
python src/check_setup.py
python src/model.py
python -m pytest -q
```

Expect `Setup OK: 73 rows and 8 columns`, a three-line table naming Line_B as
the line to inspect, and `6 passed`.

Then open `notebooks/week1_diagnostic.ipynb` and choose the `.venv` interpreter
if VS Code asks. There is no separate Jupyter server to start.

The baseline in `src/model.py` is a deliberately simple decision-support
example, not a validated production rule.

---

## The Git task

In Week 1 you clone the public course repository. It is **read-only**, so your
commit this week stays on your own machine. That local commit is the
deliverable. You will push for the first time in Week 2, when you receive your
own repository.

When the notebook and both documents are done:

```bash
git status
git add docs/problem_statement.md docs/readiness_note.md notebooks/week1_diagnostic.ipynb
git commit -m "Complete Week 1 diagnostic and problem statement"
```

Confirm it:

```bash
git log -1 --oneline
git status
```

Copy that commit hash into `docs/readiness_note.md`.

`git push` is the fifth command in the working loop, and it is what shares a
commit with a remote. Do not run it this week. You do not have write access to
the course repository, so it will be refused, and that is expected rather than
a fault. From Week 2 it becomes part of your routine.

Never paste passwords or personal access tokens into the notebook or any file
in this repository.

---

## Data source and assumptions

- **Source:** simulated teaching dataset generated for this course.
- **Licence:** free to use for coursework; it is not real operational data.
- **Assumptions:** readings are hourly and nominally comparable across lines.
- **Important:** the data contains deliberate quality issues. Find them,
  document them in Task 6, and do not silently repair the raw file.

## Responsible-use note

This is a decision-support exercise, not an automated controller. A false alarm
wastes maintenance time; a missed warning can allow disruption or quality loss.
Any flag should support a human decision at shift handover rather than replace
it.
