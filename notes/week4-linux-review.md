# Week 4 Linux Review

## Active Recall (answers)
1. Why must `sort` come before `uniq -c` in a pipeline?
Because `uniq -c` only collapses duplicates that are ADJACENT. If identical
lines are scattered through the file, uniq won't catch them — so `sort` must
run first to bring all identical lines next to each other.

2. What does the pipe `|` actually do?
It sends the OUTPUT of the command on its left as the INPUT to the command on
its right, chaining small tools into one operation.

3. Why did `python` fail but `py` work in Week 3 (PATH)?
Windows had a FAKE python — an "app execution alias" (the Microsoft Store
placeholder) — that intercepted the command and redirected to the Store instead
of running real Python. Although my real Python was actually ahead of
WindowsApps on PATH, the Store alias jumped the queue through a separate Windows
mechanism. `py` is a different command (the Python launcher) that resolves
straight to my real install, bypassing all of it.

4. What does a virtual environment isolate, and how (PATH-wise)?
It isolates PACKAGES — each project gets its own private set. Activation
PREPENDS the venv's folder to PATH, so `python`/`pip` find the venv's copies
first (first match wins), and the global packages become invisible inside it.

5. What's the #1 cause of a "file not found" error?
Being in the wrong folder — the command searched relative to my current
location instead of where the file actually lives. Run `pwd` first.

## What I Understood Well
The practical commands — navigation, grep, cut, the counting pipeline. I could
recall what each one does and run them correctly.

## What Confused Me
The two conceptual items were fuzzier than the commands: the exact cause of the
python-vs-py problem (it was a fake executable jumping PATH order, not an empty
folder), and precisely what a venv isolates (packages, via PATH-prepending —
not environment variables broadly). Now corrected.

## My Own Explanation
Small Linux tools each do exactly one job — grep filters, cut slices a column,
sort orders, uniq counts. On their own each is limited, but the pipe lets me
feed one tool's output straight into the next, so I can build a custom analysis
by combining them. This beats one big all-in-one command because I can rearrange
the small pieces for any question. For example, to find which CAN ID dominates a
trace, I chain cut → sort → uniq -c → sort -rn and get a ranked count in one
line — no script needed.