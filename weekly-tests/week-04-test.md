# Week 4 Test — Linux Command Line and Developer Environment

## Part 1 — Theory Questions
1. What is the difference between an ABSOLUTE path and a RELATIVE path?
   Give one example of each.
ABSOLUTE path: It is the full path of a file or folder in a repository from the root
Example: /c/Users/Nikhilesh Kola/automotive-sdv-engineering-roadmap/logs/study-log-2026.md
RELATIVE path: It is partial path of a file or folder within a folder or project or repository from where you are now
Example: notes\flashcards

2. What does the pipe | do? Explain using a two-command example.
pipe | takes the output of its left side command and uses it as the input for its right side command
Example: sort | uniq -c
"sort outputs ordered lines, the pipe hands them to uniq -c, which counts the now-adjacent duplicates."

3. Why must `sort` come BEFORE `uniq -c` in a pipeline?
Because uniq -c eliminates the duplicates only which are next to it, so sort arranges these similar items next to each other and uniq -c can remove all the duplicates correctly.

4. What does a virtual environment isolate, and how does activation make it work (think PATH)?
It isolates the packages. python -m venv .venv activation prepends the venv to PATH so its python/pip win the first-match lookup.

5. What does `chmod +x script.sh` do, and why do you need it?
Modifies permissions to enable execution/adds the execute (x) permission specifically,; without it, it errors and stops.

## Part 2 — Terminal Task
Q1. How many total lines are in dtc_log.csv?
wc -l dtc_log.csv
11 dtc_log.csv

Q2. How many DATA rows are there (excluding the header)?
grep -v "ecu" dtc_log.csv | wc -l
10

Q3. How many DTCs did the "engine" ECU report? (count lines mentioning engine)
grep "engine" dtc_log.csv | wc -l
6

Q4. List every UNIQUE dtc code and how many times each occurred, ranked most-frequent first, WITHOUT the header polluting the result.(This is the power-move pipeline.)
 grep -v "dtc" dtc_log.csv | cut -d',' -f3 | sort | uniq -c | sort -rn
      4 P0301
      2 P0A80
      2 P0420
      2 C0035

Q5. Which ECU appears most often in the log? Build a pipeline that answers it.
    (Hint: same pattern as Q4, but on the ecu column instead of the dtc column.)
grep -v "ecu" dtc_log.csv | cut -d',' -f2 | sort | uniq -c | sort -rn
      6 engine
      2 brake
      2 battery


## Part 3 — Debugging / Reasoning
1. A colleague runs this and gets an EMPTY result, even though the log
   definitely has engine entries:

       cut -d',' -f2 dtc_log.csv | uniq -c

   The counts are all wrong/scattered. What did they forget, and what's the fix?
First before uniq sort should be written, so sort can place all the similar entries one after other in order
cut -d',' -f2 dtc_log.csv | sort | uniq -c

2. Someone types `python -m venv .venv` then `pip install pytest`, but pytest
   ends up in their GLOBAL Python, not the venv. What step did they skip?
They did not change the path to venv, they are still in the master path. They need to cd to new venv
Also it's activating the venv (source .venv/Scripts/activate). Without activation, pip still points at global Python no matter which folder you're in

3. A script `backup.sh` gives "Permission denied" when they run `./backup.sh`.
   What's the fix, and why is it needed?
The permissions are missing, they need to enable the permissions.
chmod +x ./backup.sh

4. Someone is in `projects/python_day_09` and runs
   `git add .` then commits, but their edited `notes/foo.md` (at the repo
   root) is NOT included. Why? What should they do differently?
It is because they are inside a sub folder and only the files inside this are considered for git add. Always while writing git add, first we need to change directory to main and then write git add

## Part 4 — Written Explanation
Why does a diagnostics engineer need Linux command-line skills? Connect it to real work — triaging a large CAN/DTC log on a remote machine, reproducible environments, and automation. Why isn't "just open it in Excel" enough?
A diagnostics engineer need Linux command-line skills because CAN data has very large number of rows which cannot be analysed on a excel file. And that too it would be on a remote environment, which is even more difficult. Also reproducible environments (venvs — why the same analysis runs identically everywhere) and automation (scripts running tests/analysis without a human). To make the analysis faster and more efficient engineers use Linux commands for CAN/DTC logs.

## Part 5 — Self-Score
I would rate myself 65/100

## Part 6 — Reflection
Got a good idea of linux and its commands. Will practice one more time sometime later so that I do not forget the commands. But I understood well.