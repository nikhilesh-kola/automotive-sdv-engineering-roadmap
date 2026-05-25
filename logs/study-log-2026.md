# Automotive SDV Engineering Study Log

---

# 15.05.2026 — Bridge Day 1

## Today's Focus
Engineering workspace setup

---

## Completed Tasks

- Installed VS Code
- Installed Python
- Installed Git
- Created GitHub repository
- Created README.md
- Set up engineering workspace folders
- Created first Python file
- Created study log

---

## What I Learned Today

- How Git commits work
- Difference between local commit and remote push
- Basic engineering workspace structure
- Importance of GitHub for engineering portfolio

---

## Problems Faced

- GitHub authentication failed during push
- Needed to understand GitHub login/token authentication

---

## How I Solved Them

- Signed into GitHub via VS Code/browser authentication
- Re-ran:
  ```bash
  git push origin main
  ```

---

## Questions for Later

- How does Git authentication work internally?
- What is the difference between HTTPS and SSH authentication?
- How do professional teams structure repositories?

---

## Confidence Level

6/10

---

## Next Session Focus

- What is SDV?
- What is an ECU?
- Python basics refresh
- C basics refresh
- CAN introduction

---

## Notes to Future Me

Today was the real beginning of becoming an automotive software engineer.

---

## 16.05.2026 — Bridge Day 2

### Today's Focus
Baseline: Python, C, and diagnostic-domain knowledge.

### Completed
- Created a tiny Python baseline script
- Created a tiny C baseline program
- Wrote diagnostic-domain baseline note
- Reflected on current strengths and weaknesses

### Problems Faced
- GCC was not recognised, will do tomorrow.

### What I Learned
- VS Code is enough to write and run python & C codes, I thought I need to open Python separately to do this.

### Confidence Level
Programming: 1/10  
Diagnostics: 0/10  
Engineering mindset: 4/10  

### Next Focus
Bridge Day 3: baseline test and reflection.
---

## 18.05.2026 — Theory 1

### Today's Focus
Python variables, types, input/output, and script execution.

### Completed
- Learned variables and data types
- Learned `str`, `int`, `float`, and `bool`
- Practiced `input()` and `print()`
- Practiced type conversion
- Wrote 10 tiny Python scripts
- Connected Python basics to automotive diagnostics examples

### Problems Faced
- Understanding when type conversion is necessary
- Remembering that `input()` always returns a string

### What I Learned
- A variable stores a value.
- Data types give meaning to values.
- Engineering scripts should use clear variable names and correct units.
- Python can be used for diagnostic summaries and simple calculations.

### Confidence Level
Python basics: 3/10  
Terminal execution: 5/10  
Engineering consistency: 5/10  

### Next Focus
C compiler setup and C basics.

---

## 19.05.2026 — Theory 2

### Today's Focus
Git basics: init, status, add, commit, log, branch.

### Completed
- Learned the difference between Git and GitHub
- Learned what a repository is
- Learned `git init`
- Learned `git status`
- Learned `git add .`
- Learned `git commit -m`
- Learned `git log --oneline`
- Learned `git branch`
- Added Git basics note
- Updated README with 12-month engineering goal

### Problems Faced
- commit is a saved snapshot and commit message will explain what has changed.
- message is actually description of that snapshot

### What I Learned
- Git tracks changes locally.
- GitHub stores repositories online.
- A commit is a saved snapshot of staged changes.
- `git status` should be checked before adding and committing.
- Clear commit messages help future review.

### Confidence Level
Git basics: 5/10  
GitHub workflow: 7/10  
Repository navigation: 7/10  

### Next Focus
Practical Git workflow and first small repo organization cleanup.

---

## 20.05.2026 — Practical Lab 1

### Today's Focus
Python CSV vehicle signal analysis.

### Completed
- Created a small vehicle signal CSV file
- Read CSV data using Python
- Used `csv.DictReader`
- Stored signal values in lists
- Calculated min, max, and average values
- Printed a vehicle signal analysis report

### Problems Faced
- Understood the CSV concept well 

### What I Learned
- CSV files are text-based tables.
- Python reads CSV values as strings first.
- Lists store multiple values in memory.
- `append()` adds values into a list.
- `min()`, `max()`, `sum()`, and `len()` are useful for signal analysis.
- Average is calculated as `sum(values) / len(values)`.

### Memory-Level Understanding
- A variable name points to a value or object in memory.
- A list is an object that contains multiple values.
- CSV values move from disk text into Python memory as list values.

### Confidence Level
CSV reading: 5/10  
Lists: 5/10  
Signal statistics: 8/10  
Memory-level understanding: 7/10  

### Next Focus
Create a reusable Python function for repeated signal calculations.