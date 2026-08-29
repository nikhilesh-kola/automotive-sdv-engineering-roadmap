# Bash Test-Runner Script — Week 4 Saturday

## Today's Task
Write a shell script that runs the pytest suite and saves a timestamped report
plus a running history file.

## Key Concepts
- A script = commands saved in a file, run all at once (automation).
- #!/bin/bash (shebang) = run this file with bash.
- chmod +x = add execute permission; ./script.sh = run the script here.
- $(date +"%Y-%m-%d_%H%M") = capture formatted date into a variable.
- tee = split output to screen AND file simultaneously.
- >> appends (keeps history); > overwrites (forgets). Proved with 2 timestamped lines.

## Memory-Level Understanding
./run_tests.sh
  shebang -> run with bash
  TIMESTAMP=$(date ...) -> variable holds "2026-08-29_1754"
  REPORT_FILE = reports/test_report_${TIMESTAMP}.txt (unique per run)
  pytest ... | tee "$REPORT_FILE" -> tests run, output to screen + file
  echo "..." >> history.txt -> one summary line appended each run

## Automotive Relevance
Automated test runs with saved, dated evidence are the foundation of CI in
automotive validation. Nobody hand-types 500 tests nightly - a script does it
and a human reads the report.

## What I Understood Well
- understood the shell scripting
- also got to add few more commands to the scripting file

## What Confused Me
- just got to know that I already gave permissions for new file executions

## Next Improvement
Make the script exit with a clear PASS/FAIL status so CI can act on the result.
