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

---

## 21.05.2026 — Practical Lab 2

### Today's Focus
Add error handling, command-line arguments, and README documentation to the CSV analyzer.

### Completed
- Learned `sys.argv`
- Added command-line file input
- Added error handling with `try` and `except`
- Added reusable functions
- Created README for the script
- Tested successful run
- Tested missing argument error
- Tested wrong file path error

### Problems Faced
- nothing major, my VS Terminal uses "py" command instead of "python"
- 

### What I Learned
- Command-line arguments make scripts more flexible.
- `sys.argv` stores arguments as a list.
- `try/except` prevents ugly crashes and gives useful messages.
- Functions reduce repeated code.
- README files explain how to use a tool.

### Memory-Level Understanding
- `sys.argv` is a list stored in memory.
- Function parameters point to the objects passed as arguments.
- A list passed to a function is not automatically copied.

### Confidence Level
Command-line arguments: 5/10  
Error handling: 5/10  
Functions: 6/10  
README writing: 5/10  

### Next Focus
Review, error log, and cheat sheet.

---

## 22.05.2026 — Review

### Today's Focus
Rewrite messy notes into a one-page Python/Git cheat sheet.

### Completed
- Reviewed Python variables, types, input/output
- Reviewed lists and memory-level basics
- Reviewed CSV reading
- Reviewed functions
- Reviewed command-line arguments
- Reviewed error handling
- Reviewed Git workflow
- Created one-page Python/Git cheat sheet
- Wrote 5 open questions

### Five Questions
1. What exactly happens in memory when I assign one list variable to another?
Python does not create a new list for b. Instead, both a and b point to the same list object in memory.

2. How does Python know whether a CSV value should be a string, integer, or float?
Python does not automatically know the correct numeric type when reading CSV data. CSV files are plain text files, so values are read as strings first.

3. What is the difference between a function parameter and an argument?
A parameter is the variable name written in the function definition.
def calculate_stats(values):
    ...
An argument is the real value passed into the function when calling it.
calculate_stats(speed_values)    

4. What is the difference between staged changes and committed changes in Git?
Staged changes are changes prepared for the next commit. Committed changes are changes saved as a snapshot in Git history.

5. How can I make the CSV analyzer automatically analyze all numeric columns?
the script can read the CSV headers automatically and try to convert each column value to float.
for column_name in reader.fieldnames:
    signal_values[column_name] = []
    for column_name in reader.fieldnames:
    try:
        value = float(row[column_name])
        signal_values[column_name].append(value)
    except ValueError:
        pass
        
If a column can be converted to a number, analyze it.
If it contains text, skip it.        

### What I Learned
- Review is where scattered learning becomes structured knowledge.
- A cheat sheet helps me quickly recall important patterns.
- Git commits should capture clean learning milestones.

### Confidence Level
Python basics: 4/10  
CSV analysis: 4/10  
Git workflow: 6/10  
Memory-level understanding: 5/10  

### Next Focus
Saturday deep project lab: improve or extend the vehicle signal analyzer.

---

## 23.05.2026 — Deep Project Lab

### Today's Focus
Create a clean project structure with src, tests, data, docs, example CSV files, and a working parser.

### Completed
- Created `vehicle_signal_analyzer` project
- Added `src`, `tests`, `data`, and `docs` folders
- Added 3 example CSV files
- Created a working CSV signal parser
- Used dictionaries to store signal columns
- Added a simple function test
- Added project README
- Added project notes

### Problems Faced
- All the not yet learned functions and its logics confused me, but I could still read the code

### What I Learned
- A clean project structure makes code easier to maintain.
- `src` contains source code.
- `data` contains input files.
- `tests` contains checks for code behavior.
- `docs` contains engineering explanations.
- A dictionary can store signal names as keys and signal values as lists.
- A parser converts CSV text data into Python memory objects.

### Memory-Level Understanding
- A dictionary maps keys to values.
- In this project, each CSV column name maps to a list of numeric values.
- Function calls pass object references, not automatic deep copies.

### Confidence Level
Project structure: 5/10  
Dictionaries: 4/10  
CSV parsing: 4/10  
Testing basics: 4/10  

### Next Focus
Sunday weekly test and review.

---

## 24.05.2026 — Weekly Test 1

### Today's Focus
Weekly test for Python basics, Git workflow, CSV parsing, and memory-level understanding.

### Completed
- Answered 15 Python/Git questions
- Completed 20-minute coding task
- Ran the coding task from terminal
- Created weekly test file
- Wrote 150-word reflection
- Made Git commit from terminal

### Test Result
Python/Git questions: 12.5/15  
Coding task: PASS  
Git commit: PASS  

### Problems Faced
- Need more practice for remembering Git related definitions
- Writing scripts from scratch

### What I Learned
- Tested my knowledge on Git & Python basics
- Written a script from scratch
- Running the code, saving and commiting the changes

### Top Weak Areas
1. Exact definitions of Git related words
2. writing scripts from scratch
3. Writing scripts for Reading csv files
4. Not much practice for error handling scripts
5. Python functions & dictionaries

### Next Focus
Week 2: C compiler setup, C basics, memory model, and comparison with Python.

---

## 25.05.2026 — Theory 1

### Today's Focus
Lists, tuples, dictionaries, for loops, and while loops using ECU, DTC, and signal examples.

### Completed
- Practiced lists with ECU names
- Practiced tuples with one DTC record
- Practiced dictionaries with DTC descriptions
- Practiced for loops over lists and dictionaries
- Practiced signal statistics using a dictionary of lists
- Practiced while loop retry logic

### Problems Faced
- Needed to add final failure message after while loop
- Need more practice with exact loop stopping conditions

### What I Learned
- Lists are ordered and changeable.
- Tuples are ordered and fixed.
- Dictionaries store key-value pairs.
- for loops process each item in a collection.
- while loops repeat while a condition remains true.
- Diagnostic retry logic can be modeled with a while loop.

### Memory-Level Understanding
- A list variable points to a list object.
- A dictionary maps keys to values.
- In a for loop, the loop variable temporarily points to the current item.
- In a while loop, variables must change so that the condition eventually becomes false.

### Confidence Level
Lists: 6/10  
Tuples: 6/10  
Dictionaries: 6/10  
for loops: 6/10  
while loops: 5/10  

### Next Focus
Practical loop-based diagnostic signal processing.