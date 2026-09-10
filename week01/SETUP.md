# Setting up your tools

Do this **before** the Week 1 lab if you can. If anything fails, do not spend
the evening fighting it: write the exact command and the full error message
into `docs/readiness_note.md` and bring it to the lab. There is no penalty for
a setup or platform problem.

You need four things: Python, VS Code, two VS Code extensions, and Git.

---

## Do I need Anaconda?

**No. Anaconda is not required for this course, and it is not the recommended
route.**

This course installs its packages with `pip` from `requirements.txt`, and
creates a small virtual environment inside each week's project folder. That
keeps every student on identical package versions, keeps each week isolated,
and keeps the download to a few tens of megabytes rather than several hundred.
Mixing `conda` and `pip` in one environment is also the single most common
cause of a broken Python setup, and it is not worth the risk in a course where
reproducibility is the point.

So: install plain Python from python.org and follow Step 1 below.

### If you already have Anaconda installed

You do **not** need to uninstall it. Create a clean environment for the course
and install the course packages into it with pip:

```bash
conda create -n aids python=3.12
conda activate aids
python -m pip install -r requirements.txt
```

Then point VS Code at that environment (Step 6 below) instead of at `.venv`.
Install from `requirements.txt` rather than with `conda install`, so your
package versions match everyone else's.

### If you decide you want Anaconda anyway

Download it from <https://www.anaconda.com/download>. On Windows, run the
installer and accept the defaults; when asked, **do not** add Anaconda to your
PATH, and use the "Anaconda Prompt" application instead. On macOS and Linux,
run the graphical or shell installer and accept the defaults. Check it worked:

```bash
conda --version
```

---

## Step 1 — Install Python

Use **Python 3.10 or newer**. Versions 3.11 and 3.12 are the safest choices.

**Windows.** Download from <https://www.python.org/downloads/>. In the
installer, tick **"Add python.exe to PATH"** on the first screen before
clicking Install. This one checkbox prevents most later problems.

**macOS.** Download the installer from <https://www.python.org/downloads/>, or
use Homebrew: `brew install python@3.12`.

**Linux (Debian or Ubuntu).**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Check it worked. You should see a version number of 3.10 or higher:

```bash
python --version
```

If Windows says `python` is not recognised, try `py --version`. If that works,
use `py` in place of `python` everywhere below.

---

## Step 2 — Install VS Code

VS Code is the only editor used on this course. It gives you the notebook, a
terminal, and your Git changes in one window, so you are never switching tools
part-way through a task.

Download it from <https://code.visualstudio.com/download>.

**Windows.** Run the installer. On the "Select Additional Tasks" screen, tick
**"Add to PATH"** and both **"Open with Code"** options. They make it easy to
open a project folder later.

**macOS.** Unzip and drag `Visual Studio Code.app` into Applications. Then open
VS Code, press `Cmd+Shift+P`, and run
**Shell Command: Install 'code' command in PATH**.

**Linux.** Install the `.deb` or `.rpm` package from the download page, or use
your distribution's software centre.

---

## Step 3 — Install the two VS Code extensions

You need **Python** (`ms-python.python`) and **Jupyter**
(`ms-toolsai.jupyter`).

The easy way: open the `week01` folder in VS Code (**File > Open Folder**).
VS Code will show a notification saying the workspace has extension
recommendations. Click **Install**. This project ships that recommendation in
`.vscode/extensions.json`, so the right two are chosen for you.

The manual way: press `Ctrl+Shift+X` (`Cmd+Shift+X` on macOS), search for each
name above, and click Install.

---

## Step 4 — Install Git

Download from <https://git-scm.com/downloads>. On Windows, accept the default
options; the installer also gives you Git Bash, which is a useful fallback
terminal.

Tell Git who you are. Use the same email as your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check it worked:

```bash
git --version
```

---

## Step 5 — Create a GitHub account

Sign up at <https://github.com> if you do not already have an account. Use an
email address you will keep after graduation.

---

## Step 6 — Open the project and create its environment

Open the `week01` folder in VS Code, then open a terminal inside VS Code with
**Terminal > New Terminal**. Run these from the project root, which is the
folder containing `README.md`.

Create the environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

Install the course packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Now tell VS Code to use it. Press `Ctrl+Shift+P`, run
**Python: Select Interpreter**, and choose the one inside `.venv`. Do this
once; VS Code remembers it for this folder.

---

## Step 7 — Check that everything works

```bash
python src/check_setup.py
python -m pytest -q
```

You should see `Setup OK: 73 rows and 8 columns` and then `6 passed`. If you
see both, you are ready for the lab.

---

## Common problems

**PowerShell refuses to run `Activate.ps1`** and mentions an execution policy.
Run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Alternatively, open a Git Bash terminal in VS Code and use
`source .venv/Scripts/activate` instead.

**`python` is not recognised (Windows).** Python was installed without being
added to PATH. Either reinstall and tick "Add python.exe to PATH", or use `py`
instead of `python`.

**VS Code runs the wrong Python.** Run **Python: Select Interpreter** again and
pick the one inside `.venv`. The chosen interpreter is shown in the bottom
status bar.

**The notebook offers to install ipykernel.** That package is already in
`requirements.txt`. It usually means the `.venv` interpreter is not selected;
fix Step 6 and reopen the notebook.

**`pip install` fails behind a slow or filtered connection.** Retry once, then
record the failure in `docs/readiness_note.md` and raise it in the lab.
