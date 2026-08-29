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

---

## 26.05.2026 — Theory 2

### Today's Focus
Python functions, return values, docstrings, and simple modules.

### Completed
- Learned why repeated code should become a function
- Practiced writing functions with parameters
- Practiced returning values from functions
- Learned the difference between `return` and `print()`
- Added simple docstrings to functions
- Created reusable functions for power calculation, statistics, DTC count, and threshold checks
- Created a simple module using `signal_utils.py`
- Imported `calculate_stats()` from another Python file

### Exercises Completed
- `exercise_01_power_function.py`
- `exercise_02_stats_function.py`
- `exercise_03_dtc_count_function.py`
- `exercise_04_threshold_function.py`
- `exercise_05_use_module.py`
- `signal_utils.py`

### Problems Faced
- In the stats exercise, I used speed variable names for engine temperature values.
- In the module exercise, I used `kmph`; the better engineering unit notation is `km/h`.

### Corrections Made
- Changed speed-related variable names to temperature-related names where the data was engine temperature.
- Changed `kmph` to `km/h`.
- Improved docstrings to explain the function purpose more clearly.

### What I Learned
- A function is a reusable block of code.
- Parameters are names inside the function definition.
- Arguments are actual values passed during the function call.
- `return` sends a value back to the program.
- `print()` only displays a value on the screen.
- A docstring explains what a function does.
- A module is a Python file containing reusable code.
- Reusable logic can be imported from another file.

### Memory-Level Understanding
- When a function is called, Python maps arguments to parameters.
- Example: in `calculate_power(12.5, 4.0)`, `voltage` points to `12.5` and `current` points to `4.0` inside the function.
- When a function returns a value, that returned value can be stored in another variable.
- Importing from a module makes a function name available in the current script.
- Function parameters can point to the same list object that was passed as an argument.

### Engineering Rule Learned
Correct code runs, but good engineering code also tells the truth through names.

Repeated code should become a function.  
Reusable functions should move into a module.  
Variable names must match the real meaning of the data.

### Confidence Level
Functions: 5/10  
Return values: 5/10  
Docstrings: 6/10  
Modules/imports: 6/10  
Memory-level understanding: 6/10  

### Next Focus
Practical lab: refactor the vehicle signal analyzer using reusable functions and modules.

---

## 27.05.2026 — Practical Lab 1

### Today's Focus
Parse a CSV file with timestamp, CAN ID, DLC, and payload. Count messages per CAN ID.

### Completed
- Created `projects/python_day_06/`
- Created a warm-up script to count repeated CAN IDs from a list
- Created `can_log.csv` with timestamp, CAN ID, DLC, and payload columns
- Created `can_message_counter.py`
- Used `csv.DictReader` to read CSV rows as dictionaries
- Extracted `can_id` from each row
- Counted messages per CAN ID using a dictionary
- Printed a clean CAN message count report

### Files Created
- `projects/python_day_06/exercise_01_count_list.py`
- `projects/python_day_06/can_log.csv`
- `projects/python_day_06/can_message_counter.py`
- `notes/python-can-csv-message-counts.md`

### Output
```text
CAN Message Count Report
------------------------
0x100: 3 messages
0x200: 2 messages
0x300: 2 messages
0x400: 1 message

Problems Faced
- Initially needed step-by-step guidance again.
- Need to keep daily work aligned exactly with the PDF plan.

What I Learned
- A CAN log can be represented as a CSV file.
- Each CSV row can represent one CAN message.
- csv.DictReader converts each row into a dictionary.
- A dictionary can be used to count repeated CAN IDs.
- Counting CAN IDs is an early form of CAN trace analysis.

Memory-Level Understanding
- Each CSV row is read as a dictionary.
- row["can_id"] extracts the CAN ID from the current row.
- message_counts stores each CAN ID as a key and its message count as a value.
- Each time a CAN ID appears, its count increases by 1.


Confidence Level

CSV reading: 5/10
Dictionaries: 5/10
Counting logic: 6/10
CAN log understanding: 6/10

Next Focus

Practical Lab 2: build a function that filters records by CAN ID and exports the filtered data to a new CSV.

---

## 28.05.2026 — Practical Lab 2

### Today's Focus
Build a function that filters CAN records by CAN ID and exports the filtered records to a new CSV file.

### Completed
- Created `exercise_02_filter_list.py`
- Practiced filtering a list of CAN record dictionaries
- Created `can_id_filter.py`
- Built `filter_records_by_can_id()`
- Built `write_records_to_csv()`
- Filtered records for CAN ID `0x100`
- Exported filtered records to `can_log_0x100.csv`
- Modified the script to filter CAN ID `0x300`
- Exported filtered records to `can_log_0x300.csv`

### Files Created
- `projects/python_day_06/exercise_02_filter_list.py`
- `projects/python_day_06/can_id_filter.py`
- `projects/python_day_06/can_log_0x100.csv`
- `projects/python_day_06/can_log_0x300.csv`
- `notes/python-can-id-filter-export.md`

### Output for 0x100
```text
CAN ID Filter Report
--------------------
Input file: projects/python_day_06/can_log.csv
Target CAN ID: 0x100
Filtered records: 3
Output file: projects/python_day_06/can_log_0x100.csv

CAN ID Filter Report
--------------------
Input file: projects/python_day_06/can_log.csv
Target CAN ID: 0x300
Filtered records: 2
Output file: projects/python_day_06/can_log_0x300.csv

Problems Faced
I copied the guided code first, then modified the target CAN ID and output file to confirm understanding.

What I Learned
- csv.DictReader reads CSV rows as dictionaries.
- csv.DictWriter writes dictionaries into a CSV file.
- A list can store multiple matching CAN records.
- A function can make filtering logic reusable.
- Changing target_can_id allows the same function to filter a different CAN ID.

Memory-Level Understanding
- One CSV row becomes one dictionary.
- Multiple filtered rows become a list of dictionaries.
- filtered_records.append(row) stores the matching row in the list.
- The output CSV is created from the dictionaries stored in filtered_records.


Confidence Level

CSV filtering: 5/10
Functions: 5/10
DictReader/DictWriter: 5/10
List of dictionaries: 6/10
CAN log understanding: 6/10

Next Focus

Review: create flashcards for Python data structures and write a short note on where dictionaries help in diagnostics.

---

## 29.05.2026 — Review

### Today's Focus
Create flashcards for Python data structures and write a short note on where dictionaries help in diagnostics.

### Completed
- Created Python data structure flashcards
- Reviewed lists, tuples, dictionaries, for loops, while loops, functions, modules, and CSV handling
- Created a short note explaining where dictionaries help in automotive diagnostics
- Reviewed dictionary counting pattern for CAN message counts
- Reviewed list of dictionaries for filtered CAN records

### Files Created
- `notes/flashcards/python-data-structures-flashcards.md`
- `notes/dictionaries-in-diagnostics.md`

### What I Reviewed
- Lists are ordered and changeable.
- Tuples are ordered and fixed.
- Dictionaries store key-value pairs.
- A `for` loop processes each item in a collection.
- A `while` loop repeats while a condition is true.
- Functions make repeated code reusable.
- Modules store reusable functions in separate Python files.
- `csv.DictReader` reads CSV rows as dictionaries.
- `csv.DictWriter` writes dictionaries to CSV files.

### What I Learned
- Dictionaries make diagnostic data easier to understand because each value has a meaningful key.
- A dictionary can represent one CAN message row.
- A list of dictionaries can represent many CAN message rows.
- A dictionary can count repeated CAN IDs.
- Dictionaries are useful for DTC descriptions, ECU statuses, CAN message counts, and signal values.

### Memory-Level Understanding
- A list stores values by position.
- A tuple stores fixed values by position.
- A dictionary stores values by key.
- In CAN log parsing, one CSV row becomes one dictionary.
- Multiple rows become a list of dictionaries.
- CAN ID counts are stored as key-value pairs.

### Problems Faced
- Need more repetition to remember syntax without looking.
- Need to practice explaining dictionaries in my own words.

### Confidence Level
Lists: 5/10  
Tuples: 5/10  
Dictionaries: 6/10  
for loops: 6/10  
while loops: 5/10  
Functions: 5/10  
CSV DictReader/DictWriter: 5/10  
Git workflow: 7/10  

### Next Focus
Deep project lab: build v1 of a diagnostic-log summarizer that prints message counts, first/last timestamp, and top 5 active IDs.

---

## 30.05.2026 — Deep Project Lab

### Today's Focus
Build v1 of a diagnostic-log summarizer that prints message counts, first/last timestamp, and top active CAN IDs.

### Completed
- Created `exercise_03_first_last_timestamp.py`
- Practiced first and last list item access using `[0]` and `[-1]`
- Created `diagnostic_log_summarizer.py`
- Built `read_can_log()`
- Built `count_messages_by_can_id()`
- Built `get_first_timestamp()`
- Built `get_last_timestamp()`
- Built `get_top_active_ids()`
- Built `print_summary()`
- Printed total messages, first timestamp, last timestamp, CAN ID counts, and top active IDs
- Created README for Python Day 06
- Created diagnostic log summarizer project note

### Files Created or Updated
- `projects/python_day_06/exercise_03_first_last_timestamp.py`
- `projects/python_day_06/diagnostic_log_summarizer.py`
- `projects/python_day_06/README.md`
- `notes/diagnostic-log-summarizer-v1.md`

### Output
```text
Diagnostic Log Summary
----------------------
Input file: projects/python_day_06/can_log.csv
Total messages: 8
First timestamp: 0.000
Last timestamp: 0.070

Message Counts per CAN ID
-------------------------
0x100: 3 messages
0x200: 2 messages
0x300: 2 messages
0x400: 1 message

Top Active CAN IDs
------------------
1. 0x100 - 3 messages
2. 0x200 - 2 messages
3. 0x300 - 2 messages
4. 0x400 - 1 message

What I Learned
- A diagnostic log can be represented as a list of dictionaries.
- Each CAN row is one dictionary.
- records[0] gives the first record.
- records[-1] gives the last record.
- A dictionary can count CAN IDs.
- sorted() can order CAN IDs by message count.
- A summarizer gives quick high-level insight into a CAN trace.

Memory-Level Understanding
- records points to a list containing all CAN message dictionaries.
- Each dictionary contains timestamp, CAN ID, DLC, and payload.
- message_counts maps CAN IDs to how often they appear.
- get_top_active_ids() sorts CAN ID/count pairs by count.
- limit controls how many active IDs are returned.

Problems Faced
- The first version was guided, so I need to practice modifying it independently.
- sorted() with lambda is still new and needs more repetition.

Confidence Level

CSV parsing: 5/10
Functions: 5/10
Lists of dictionaries: 6/10
Message counting: __/10
First/last timestamp logic: 6/10
Sorting with lambda: 5/10
CAN log understanding: 6/10

Next Focus

Sunday weekly test: data-structure questions, parser bug-fix task, 5-minute code explanation, and commit.

Weekly test is also done

---

## Week 3 · Monday — Theory 1

### Today's Focus
Exceptions, assert statements, and why tests matter (Python quality).

### Completed
Read pytest getting-started (first section). Wrote and ran 3 exercises:
exceptions, assert, and a manual test function.

### Files Created
projects/python_day_07/exercise_01_exception_example.py
projects/python_day_07/exercise_02_assert_example.py
projects/python_day_07/exercise_03_test_function_manual.py

### What I Learned
- Exceptions handle expected bad input (catch specific ones, never a catch-all).
- raise is for when MY rule is broken (e.g. CAN frame not 8 bytes).
- assert catches MY logic errors; it can be disabled, so it's not for input validation.
- A test is a known input checked against an expected output.

### Memory-Level Understanding
except ValueError = only catch bad-value errors (safe)
except Exception  = catch everything (hides bugs)
assert            = must-be-true check on my own logic
test              = input X -> expected Y, verified

### Problems Faced
None — the assert crash in exercise 2 was intentional and understood.

### Confidence Level
Exceptions try/except: 8/10
raise your own error: 7/10
assert vs exception: 7/10
why tests matter: 8/10

---

## Week 3 · Tuesday — Theory 2

### Today's Focus
Logging vs print, error messages, and the debugging mindset.

### Completed
Read Python logging tutorial (first two sections). Wrote and ran 2 exercises:
the five log levels with a threshold, and a CAN parser that logs its behaviour.

### Files Created
projects/python_day_08/exercise_01_logging_levels.py
projects/python_day_08/exercise_02_parser_with_logging.py

### What I Learned
- print = show the user a result; logging = the program narrating itself.
- Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL; set one threshold, below it goes silent.
- Never delete debug lines - just lower/raise the threshold dial.
- Good error message = what + where + expected vs actual.
- Hex in source (0x11) is stored as a plain int (17); hex is only notation.

### Memory-Level Understanding
threshold = the dial; below it is silenced
argument outside -> parameter inside; return -> stored in outer variable
result = None -> "if result is not None" refuses to append -> frame skipped

### Problems Faced
None.

### Confidence Level
print vs logging: 7/10
log levels + threshold: 8/10
writing good error messages: 7/10
debugging mindset: 7/10

---

## Week 3 · Wednesday — Practical Lab 1

### Today's Focus
pytest tests for the CAN log parser: valid, empty, bad payload, unknown ID.

### Completed
Installed pytest (via `py`), fixed a "0 items collected" (unsaved file),
wrote a parser + 6 passing tests, added a 5th known CAN ID with its own test.

### Files Created
projects/python_day_09/can_parser.py
projects/python_day_09/test_can_parser.py
projects/python_day_09/test_warmup.py
projects/python_day_09/data/can_log_valid.csv
projects/python_day_09/data/can_log_empty.csv
projects/python_day_09/data/can_log_bad_payload.csv
notes/python-pytest-can-parser.md

### What I Learned
- Use `py`, not `python`, on this machine.
- Save before running — pytest reads from disk.
- pytest.raises: the expected error IS the pass.
- Parser holds the rule; test proves it fires.
- Test names should describe behaviour, not when they were written.

### Problems Faced
"collected 0 items" from an unsaved file; solved by reading timestamps. I actually did not save the file, so it technically has no data in it until I save. So instead of guessing, I checked, saved the file and then re-running it has worked.

### Confidence Level
Writing a pytest test: 6/10
pytest.raises for expected errors: 6/10
Reading a test result / failure: 6/10
Save-before-run discipline: 8/10

---

## Week 3 · Thursday — Practical Lab 2

### Today's Focus
Break the parser on purpose, read the failure, fix it, document in CHANGELOG.

### Completed
Broke the length check (8->7), predicted the failure correctly, read the
pytest failure block, found a code/message drift bug, fixed it with a single
constant EXPECTED_PAYLOAD_BYTES, returned to 6 passed.

### Files Created or Updated
projects/python_day_09/can_parser.py (constant added)
projects/python_day_09/CHANGELOG.md
notes/python-parser-break-fix.md

### What I Learned
- Predict, then verify — my prediction matched the failure.
- A passing test only guards its specific check (the length-check test passed even while broken).
- Code and error messages must share one source of truth, or they drift and lie.

### Problems Faced
Confusing "expected 8, got 8" message caused by a hardcoded 8 in the text
while the rule checked 7.

### Confidence Level
Reading a pytest failure block: 6/10
Predict-then-verify debugging: 6/10
Why a passing test isn't full proof: 6/10
Single-source-of-truth for constants: 6/10

---

## Week 3 · Friday — Review

### Today's Focus
Build a reusable test-design checklist: normal, empty, edge/boundary, error.

### Completed
Created a four-category test checklist and applied it to this week's parser,
which exposed a real gap: I never tested the boundary (7 or 9 bytes), only
"way too short" and "correct".

### Files Created
notes/flashcards/test-design-checklist.md
notes/test-design-thinking.md

### What I Learned
- Four categories every time: normal, empty, edge/boundary, error.
- A checklist turns "what should I test?" into "what's the edge case here?".
- I missed the boundary case this week — off-by-one bugs live exactly there.
- Precise wording matters: "missing test categories", not "missing errors".

### Problems Faced
None — consolidation day.

### Confidence Level
Knowing the four test categories: 7/10
Spotting the boundary/edge case: 7/10
Explaining test design in my own words: 7/10

---

## Week 3 · Saturday — Deep Project Lab

### Today's Focus
Grow the CAN parser suite to 10 meaningful tests using the Friday checklist.

### Completed
Audited existing tests against the four categories, found and filled the
boundary gap (7 and 9 bytes), added an error-message-content test, and a
one-row minimum-input test with a correct 8-byte fixture. 10 passed.

### Files Created or Updated
projects/python_day_09/test_can_parser.py
projects/python_day_09/data/can_log_seven_bytes.csv
projects/python_day_09/data/can_log_nine_bytes.csv
projects/python_day_09/data/can_log_valid_1_row.csv
projects/python_day_09/README.md
notes/can-parser-test-suite-v1.md

### What I Learned
- A test suite is judged by category coverage, not test count.
- Boundary tests catch off-by-one; I'd missed them until the checklist.
- Building correct test data is its own skill (counted bytes to be sure).
- Inspecting the exception message tests HOW it failed, not just THAT it did.

### Problems Faced
None — chose the harder modification (new fixture) and got the byte count right.

### Confidence Level
Boundary testing: 7/10
Inspecting exception messages: 7/10
Building correct test fixtures: 8/10
Designing a suite by category: 7/10

---

## Week 4 · Monday — Theory 1 (+ Week 3 repair)

### Today's Focus
Linux filesystem, paths, and core commands: ls, cd, mkdir, cp, mv, rm, cat, more, Select-String.

### Completed
Repair block: rewrote check_dlc from scratch (fixed the inverted range check
and grafted-variable habits from the Week 3 test). Then: navigated the repo
tree, practiced cp/mv/rm in a sandbox, searched a file with Select-String.

### What I Learned
- Filesystem is a tree; paths are absolute (from root) or relative (from here).
- . = here, .. = up one level; cd needs a space (cd ..\.. not cd..\..).
- cp keeps the original, mv replaces it, rm deletes permanently (no recycle bin).
- Select-String (grep) finds every matching line with line numbers - the key log-hunting tool.
- When a path "doesn't exist", run pwd first - usually I'm in the wrong folder.
- Text files have an encoding; a mismatch turns special chars into garbage (â?").

### Problems Faced
Overshot with cd ..\.. from the sandbox (one level too high) and hit a
"path not found". Diagnosed it with pwd, recovered with an absolute path.

### Confidence Level
Absolute vs relative paths: 7/10
cp / mv / rm distinction: 7/10
Select-String / grep for searching: 7/10
Recovering with pwd when lost: 7/10

---

## Week 4 · Tuesday — Theory 2

### Today's Focus
Environment variables, PATH, pip/packages, virtual environments, permissions.

### Completed
Inspected $env:USERNAME, $env:TEMP, and the full PATH. Listed installed
packages with pip. Explained the Week 3 python-vs-py mystery via PATH.

### What I Learned
- Environment variable = named value the system reads ($env:NAME).
- PATH = ordered folder list; first match wins when I type a command.
- py -m X is bulletproof: runs through real Python, ignores PATH quirks.
- A venv is a private package folder per project, so dependency versions never collide.
- Real machines are messy: I have Python 3.9 on PATH but run 3.14 via py, and
  the Store alias can jump PATH order - the tidy "first match wins" rule has exceptions.

### Problems Faced
None - but discovered my machine has multiple Pythons; py avoids the confusion.

### Confidence Level
What PATH is and how lookup works: 7/10
Why py works and python didn't: 7/10
What a venv is for: 6/10
pip / packages: 6/10

---

## Week 4 · Wednesday — Practical Lab 1

### Today's Focus
Create and use a virtual environment; install pytest inside it; run tests under it.

### Completed
Created .venv in python_day_10, fixed the execution-policy block with the
narrowest scope (RemoteSigned/CurrentUser), activated it, confirmed it started
empty, installed pytest into it, ran the Week 3 suite (10 passed) using the
venv's own python.exe. Verified .venv is gitignored.

### Files Created or Updated
projects/python_day_10/.venv/ (NOT committed - gitignored)
notes/python-virtual-environments.md

### What I Learned
- A venv starts empty and isolated - global pytest was invisible inside it.
- Activation = putting the venv at the front of PATH (ties to Tuesday).
- pytest showed .venv\Scripts\python.exe - one pinned Python, ending the 3.9/3.14 confusion.
- Security errors: check first, then apply the narrowest fix (least privilege).

### Problems Faced
Activation blocked by execution policy; fixed with Set-ExecutionPolicy
RemoteSigned scoped to CurrentUser only.

### Confidence Level
Creating/activating a venv: 8/10
Understanding venv isolation: 7/10
Why activation works (PATH): 7/10
Handling the execution-policy fix safely: 7/10
---

## Week 4 · Thursday — Practical Lab 2

### Today's Focus
Inspect a CAN log with grep, cut, sort, uniq, wc in Git Bash (real Linux tools).

### Completed
Set up Git Bash, created a sample CAN log, and built the classic pipeline to
rank CAN IDs by frequency without Python. Wrote an independent command to count
data rows. Found 0x100 = 5 occurrences (tool beat my eyeball count of 4).

### Files Created or Updated
projects/python_day_11/can_log.csv
notes/linux-log-inspection.md

### What I Learned
- The pipe | chains small single-purpose tools into powerful analysis.
- sort BEFORE uniq -c, because uniq only collapses adjacent duplicates.
- sort -rn ranks by count, biggest first.
- grep -v inverts the match (used to drop the header line).
- Trust the tool over the hand-count - my eyeball said 4, the truth was 5.
- understood and practised all the mentioned linux commands
- Also got to know the logic behind every command, to use them efficiently

### Problems Faced
Finding the pipe key on a Windows/German layout; solved (Shift+\).
- i did not know which key on windows laptop does that, finally learned it is with shift + \
- for wc command the "-l" looks like -1, I thought it is minus 1, but it is actually minus letter l


### Confidence Level
The pipe and chaining tools: 6/10
cut / sort / uniq -c / sort -rn: 6/10
grep and grep -v: 7/10
Working in Git Bash (paths, /c/): 6/10

---

## Week 4 · Friday — Review

### Today's Focus
Build a task-organized Linux cheat sheet for diagnostic logs; consolidate the week.

### Completed
Wrote a 20+ command cheat sheet organized by task, and a review note with
active recall. Corrected two conceptual gaps: what the Store alias actually was
(a fake executable that jumped PATH order, not an empty folder), and that a
venv isolates PACKAGES via PATH-prepending, not environment variables broadly.

### Files Created or Updated
notes/linux-diagnostic-cheatsheet.md
notes/week4-linux-review.md

### What I Learned
- sort ORDERS lines (grouping is a side effect); that's why it must precede uniq -c.
- The python-vs-py cause was an alias jumping PATH order, not an empty folder.
- A venv isolates packages; activation prepends it to PATH so its tools win.
- Cheat sheets organized by TASK are usable under pressure.

### Confidence Level
Recalling command meanings: 6/10
The diagnostic pipeline power move: 6/10
Why python failed / how venv works (precise): 6/10
Organizing knowledge into a reference: 6/10

---

## Week 4 · Saturday — Deep Project Lab

### Today's Focus
Write a shell script that runs the test suite and saves timestamped reports.

### Completed
Built run_tests.sh: runs pytest, saves a timestamped report via tee, and
appends a run summary to history.txt. Practiced shebang, chmod +x, ./ execution,
$(...) capture, and proved >> appends (two timestamped history lines).

### Files Created or Updated
projects/python_day_12/run_tests.sh
projects/python_day_12/hello.sh
projects/python_day_12/README.md
notes/bash-test-runner-script.md

### What I Learned
- A script is just saved, sequenced commands - automation is composition.
- chmod +x grants execute permission; scripts won't run without it (Tue's theory, live).
- ./script.sh runs a script in the current folder (not on PATH).
- tee shows AND saves output; >> appends, > overwrites.

### Problems Faced
Verified the script and append behaviour carefully rather than assuming green.

### Confidence Level
Writing/running a shell script: 6/10
chmod +x and permissions: 6/10
tee and > vs >>: 6/10
Automating a repeatable task: 6/10
