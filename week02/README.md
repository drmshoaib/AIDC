# Week 2 Student Lab: Problem Framing and Data Suitability

This README is the complete guide for the lab. We will work through it together
in class, in order. Read each section before running its commands.

Week 2 continues the plant-operations scenario from Week 1. In Week 1, the
small baseline rule in `src/model.py` identified one production line to inspect.
This week we step back and ask a more important question: **was that the right
problem to solve with the available data?**

The focus is the decision, the people affected by it, and the evidence required
to support it. **Do not train a new model this week.**

## What you will complete and submit

Week 2 is designed for a 120-minute taught lab. By the end, your Classroom 50
assignment repository must contain:

1. a completed `docs/problem_brief.md`;
2. a completed `docs/ethical_risk_note.md`;
3. a completed `docs/data_choice.md`;
4. a completed `docs/data_suitability_checklist.md`; and
5. an executed and saved `notebooks/week2_problem_framing.ipynb`.

You will commit these files and push the commit to the private repository that
Classroom 50 creates for you. A file left only on your computer is not a
submission.

## Learning outcomes

By the end of the lab, you should be able to:

1. turn a vague technical request into a decision-centred problem brief;
2. distinguish the user, decision owner, affected people, and data owner;
3. define a success measure, guardrail, action window, and constraint;
4. identify initial responsible-use risks; and
5. reach a justified preliminary decision about data suitability.

## Before Week 2: complete Week 1 if you missed it

Many students may not have completed the Week 1 lab. That is the first job.
Week 2 assumes that you have seen the project structure, created a virtual
environment, run a Python script and tests, used a notebook, and made a Git
commit.

Find the Week 1 student folder:

- in the course repository: `Lectures/Week 1/Lab/week01`;
- in your Classroom 50 assignment repository: `week01`.

Open `week01/README.md` and follow it from the beginning. If the tools are not
installed, or you have forgotten the setup, repeat the commands in
`week01/SETUP.md`. Repeating a setup command is better than guessing.

Before starting Week 2, you should be able to run these commands from inside
`week01`:

```bash
python src/check_setup.py
python src/model.py
python -m pytest -q
```

You should see `Setup OK: 73 rows and 8 columns`, a three-line summary naming
`Line_B` as the line to inspect, and `6 passed`. Complete the Week 1 notebook,
`docs/problem_statement.md`, and `docs/readiness_note.md` as instructed there.

If you already completed Week 1 in another local copy, keep that work. Once
your Classroom 50 repository is available, copy only your completed Week 1
documents and notebook into the matching locations in its `week01` folder.
Do **not** copy a `.git` folder or `.venv` environment.

## Your Classroom 50 repository

### What will happen in the next few days

Your instructor already has the GitHub usernames for this cohort and will add
all 50 students to **Classroom 50** over the next few days. Classroom 50 is the
coursework system that creates and records your individual GitHub assignment
repository.

You should expect:

1. an invitation to join the course's GitHub organization; and
2. a Classroom 50 link for the Week 1 and Week 2 assignment.

The invitation may appear by email, on GitHub, or when you open the assignment
link. Accept it using the same GitHub account whose username you gave the
instructor. Do not create a separate personal repository for this lab.

If the invitation has not arrived yet, you may complete Week 1 in your current
course copy and save the files locally. Do not try to push to the course
repository. Transfer the completed output files only after your private
assignment repository has been created.

### Accept the Classroom 50 assignment

When the instructor shares the assignment link:

1. Open the link and sign in to GitHub if asked.
2. Accept the invitation to the course organization if it is still pending.
3. At [classroom50.org](https://classroom50.org), select **Sign in with
   GitHub** and approve the requested access.
4. Check that the page shows your correct GitHub username.
5. Select **Accept assignment** and wait for every setup step to finish.
6. Select **Open repository**.

Accepting the assignment creates an individual repository whose name contains
the classroom, assignment, and your GitHub username. It should be private and
should contain the starter `week01` and `week02` folders. If either folder is
missing, or the repository shows another student's username, stop and tell the
instructor. Do not make a replacement repository.

The current Classroom 50 student instructions are available in its
[Web Student Guide](https://github.com/foundation50/classroom50/wiki/Web-Student-Guide).

### Clone your assignment repository once

On your assignment repository's GitHub page, select **Code**, copy the HTTPS
address, and then run this from the folder where you keep your course projects:

```bash
git clone <your-Classroom-50-repository-URL>
cd <your-Classroom-50-repository-name>
git remote -v
```

Replace the text inside angle brackets with your actual repository URL and
folder name; do not type the angle brackets. Both remote lines must point to
your private assignment repository and must include your GitHub username. They
must not point to the public course repository.

You clone only once. In later labs, open this same local assignment repository
and run `git pull` before starting work.

### Authentication and security

Git may open a browser so that you can sign in when you clone or push. Follow
the browser instructions. GitHub does not accept an account password for Git
operations over HTTPS. If browser sign-in does not work, ask the instructor
before creating a token or changing Git settings.

Never paste a password, personal access token, recovery code, or other secret
into a notebook, document, terminal command saved in a file, or Git commit.

## Understand the `week02` folder

The `week02` folder is a self-contained student project. Open this folder—not
the whole course repository—in VS Code. Run the Week 2 commands from the
terminal while your current folder is `week02`.

```text
week02/
├── README.md
├── requirements.txt
├── .gitignore
├── .vscode/
│   └── extensions.json
├── data/
│   ├── raw/
│   │   └── plant_shift_log.csv
│   └── processed/
│       └── .gitkeep
├── docs/
│   ├── problem_brief.md
│   ├── ethical_risk_note.md
│   ├── data_choice.md
│   └── data_suitability_checklist.md
├── notebooks/
│   └── week2_problem_framing.ipynb
└── src/
    └── profile_data.py
```

| File or folder | Its job | What you do |
|---|---|---|
| `README.md` | The complete lab and submission guide | Follow it in order; do not submit it as an answer sheet |
| `requirements.txt` | Lists the Python packages needed this week | Install it into `week02/.venv`; do not edit it |
| `.gitignore` | Prevents environments, caches, and derived data from entering Git | Leave it unchanged |
| `.vscode/extensions.json` | Recommends the Python and Jupyter extensions | Install the recommendations if VS Code asks |
| `data/raw/plant_shift_log.csv` | The supplied simulated evidence, including deliberate faults | Read it but **never edit or repair it** |
| `data/processed/` | A safe location for any derived data | Use only if needed; its generated contents are not submitted |
| `docs/problem_brief.md` | Part A decision-framing template | Complete every relevant field |
| `docs/ethical_risk_note.md` | Part B stakeholder and risk template | Complete every relevant field and the judgement |
| `docs/data_choice.md` | Part C source, coverage, quality, and decision-fit record | Complete it using notebook evidence |
| `docs/data_suitability_checklist.md` | Part D checklist and preliminary decision | Rate every checklist item and justify the decision |
| `notebooks/week2_problem_framing.ipynb` | Guided inspection of the dataset | Run every cell from top to bottom, inspect the evidence, and save it |
| `src/profile_data.py` | A bounded command-line data profile | Run and read it; do not turn it into a cleaning or modelling script |

The four files in `docs/` and the executed notebook are your Week 2
submission. The raw CSV, profile script, configuration files, and environment
support your work but are not answer sheets.

## Scenario

A plant manager asks the data team to “use AI to predict machine problems.”
The supplied file contains simulated hourly observations for three production
lines across one day. The immediate operational question is whether the data
can help a maintenance supervisor decide which line to inspect first at the
next shift handover.

The raw file contains deliberate quality issues. Identify them, but do not edit
or silently repair the source CSV.

## Create the Week 2 virtual environment

Each week's project has its own virtual environment. A `.venv` keeps the
packages for one project separate from your computer and from other weeks.
Create it inside `week02`; do not reuse or copy the `week01/.venv` folder.

### Step 1: open the correct folder

In VS Code, select **File > Open Folder** and choose `week02` inside your
Classroom 50 assignment repository. Then select **Terminal > New Terminal**.
The terminal prompt should end in `week02`.

### Step 2: create `.venv`

Run:

```bash
python -m venv .venv
```

On Windows, if `python` is not recognised but `py` works, run:

```powershell
py -m venv .venv
```

If `.venv` already exists, do not create it again. Continue to activation.

### Step 3: activate it

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

After activation, the terminal prompt normally starts with `(.venv)`.

### Step 4: install this week's packages

Run these commands after activation, on every operating system:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you are returning to the lab later, activate `.venv` again and rerun the
second command. It checks that the required packages are present and does not
normally reinstall packages that are already correct.

### Step 5: select the same interpreter in VS Code

Press `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS), run **Python: Select
Interpreter**, and choose the Python interpreter inside `week02/.venv`. Use
that interpreter when the notebook asks you to choose a kernel.

If setup fails, copy the exact command and complete error message into a note,
then ask for help. Do not hide the error or install unrelated packages at
random. The Week 1 `SETUP.md` contains troubleshooting for the most common
Python, PowerShell, VS Code, and notebook problems.

## Run the bounded profile

From inside `week02`, with `.venv` active, run:

```bash
python src/profile_data.py
```

The profile should report:

- 73 rows;
- 8 columns;
- 24 distinct hourly periods; and
- three production lines.

It also reports evidence about dates, duplicates, missing values, and simple
plausibility checks. A profile supplies evidence; it does not approve the data
or the project.

## Run the notebook

Open `notebooks/week2_problem_framing.ipynb` in VS Code.

1. Select the interpreter inside `week02/.venv` as the notebook kernel.
2. Select **Restart** and then **Run All** so the notebook executes in order.
3. Read every markdown instruction and inspect every output.
4. Do not edit the raw CSV or add model training.
5. Confirm that the last code cell prints `Notebook checks passed`.
6. Save the notebook after every cell has run.

The final checks confirm that the expected teaching dataset loaded correctly.
They do not prove that the dataset is suitable for deployment.

## Complete the four lab tasks

Work through Parts A to D in order. Each part fills one file in `docs/`.
Short, concrete statements are stronger than long vague paragraphs. Where you
do not know something, write **Unknown** and state what evidence would resolve
it. Do not invent a licence, stakeholder requirement, performance target,
engineering limit, or acceptable error cost.

### Part A: frame the decision — `docs/problem_brief.md`

Rewrite “use AI to predict machine problems” as a decision-ready statement.
Name the user, decision owner, affected people, data owner, operational
decision, action window, available evidence, desired value, technical and
operational success measures, guardrail, baseline, constraint, and condition
for non-use.

Do not name an algorithm. Use your Week 1 `week01/docs/problem_statement.md`
as a starting point, then make the framing more precise.

### Part B: map stakeholders and risks — `docs/ethical_risk_note.md`

Distinguish the person who uses the output from the people who experience its
consequences. Define the event being flagged. Compare a false alarm with a
missed warning, identify who can challenge or stop use, and state one practical
safeguard. Mark unknown costs or permissions as unknown.

### Part C: review the data — `docs/data_choice.md`

Use the notebook's schema, coverage, quality, and decision-fit sections. Record
the dataset name, source, permitted use, data status, unit of observation, time
span, size, relevant variables, missing variables, quality issues, possible
fit, limitations, and further evidence needed. State clearly what one row
represents.

### Part D: make a suitability decision — `docs/data_suitability_checklist.md`

Rate **every checklist item** as **Yes**, **Partly**, **No**, or **Unknown**, and
add evidence or an unresolved question for every rating. Then choose one
provisional outcome:

- **Proceed:** suitable, permitted, and manageable for the stated question.
- **Pilot:** continue cautiously while a named uncertainty is checked.
- **Change question:** use the data for a narrower decision.
- **Stop:** illegal, unsafe, unethical, or infeasible.

Write the requested 150-to-200-word justification. Connect the decision to the
user, operational decision, evidence, risks, and most important unresolved
question. A strong answer may narrow the original request rather than force the
data to support it. Changing the question is an analytical conclusion, not a
failure.

## Commit and submit through Classroom 50

Your work is submitted by committing it and pushing the commit to the private
assignment repository that Classroom 50 created for you. Saving in VS Code is
necessary, but saving alone does not submit anything.

### First: confirm that you are in the correct repository

From inside `week02`, run:

```bash
git remote -v
git status
```

The remote URL must be your Classroom 50 assignment repository, not the public
course repository. `git status` should list the files you completed.

### If you completed missed Week 1 work

Commit and push that checkpoint first. From inside `week01`, run:

```bash
git status
git add docs/problem_statement.md docs/readiness_note.md notebooks/week1_diagnostic.ipynb
git diff --cached --stat
git commit -m "Complete Week 1 diagnostic and problem statement"
git push
```

If Git says there is nothing to commit, use `git status` to check whether the
files were saved and whether they are already part of a commit.

### Commit Week 2

From inside `week02`, run:

```bash
git status
git add docs/ notebooks/week2_problem_framing.ipynb
git diff --cached --stat
git commit -m "Complete Week 2 problem framing and suitability review"
git push
git log -1 --oneline
git status
```

Read the output of each command before running the next one:

- `git add` selects the completed documents and notebook for the commit;
- `git diff --cached --stat` lets you check what will be committed;
- `git commit` records a named checkpoint on your computer;
- `git push` sends that checkpoint to your Classroom 50 repository;
- `git log -1 --oneline` shows the latest commit; and
- the final `git status` should report a clean working tree.

Several honest commits are acceptable. Do not delete history or force-push to
make the work look as though it was completed in one attempt.

### Confirm submission in Classroom 50

After `git push` succeeds:

1. Open the Week 2 assignment at [classroom50.org](https://classroom50.org).
2. Refresh the assignment page.
3. Open **My submission**.
4. Confirm that it shows a submission and the time of your latest push.
5. Open your repository and check that the four completed documents and the
   executed notebook are visible on GitHub.

For this lab, a push to the default branch is the submission. If Classroom 50
does not show the new submission after a successful push, keep the local
commit, copy the complete terminal output, and tell the instructor. Do not
create another repository or paste a token into a file.

## Final submission checklist

Before leaving the lab, confirm all of the following:

- [ ] I completed any missed Week 1 work or recorded exactly what remains.
- [ ] I am working in my private Classroom 50 assignment repository.
- [ ] `python src/profile_data.py` runs successfully in `week02/.venv`.
- [ ] Every notebook cell runs in order and the notebook is saved.
- [ ] All four Week 2 documents are complete.
- [ ] Every suitability checklist item has a rating and evidence.
- [ ] My preliminary decision has a 150-to-200-word justification.
- [ ] I committed the documents and executed notebook.
- [ ] `git push` completed without an error.
- [ ] Classroom 50 shows my latest submission.
- [ ] `git status` reports a clean working tree.

Bring the dataset source, permitted use, provisional suitability decision, and
most important unresolved question to the Week 3 data-approval checkpoint.

## Data and responsible-use note

- **Source:** simulated teaching dataset generated for this course.
- **Permitted use:** free to use for coursework; it is not real operational
  data.
- **Scope:** one day containing 24 hourly periods for three production lines.
- **Decision boundary:** the exercise supports human review at shift handover.
  It does not justify automatic shutdown, maintenance scheduling, or safety
  action.
