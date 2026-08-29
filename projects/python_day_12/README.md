# Week 4 — Automated Test Runner Script

## Goal
A shell script that runs the CAN parser test suite and saves a timestamped
report, plus a running history of all runs. One command -> tests run -> results
saved.

## Files
- `run_tests.sh` — runs pytest on the Week 3 suite, saves a timestamped report
  to reports/, and appends a line to reports/history.txt.
- `hello.sh` — warm-up script (shebang + echo + date).
- `reports/` — timestamped test reports and history.txt.

## How to Run
    chmod +x run_tests.sh    # once, to make it executable
    ./run_tests.sh

## Key Concepts
- Shebang (#!/bin/bash): tells the system to run the file with bash.
- chmod +x: grants execute permission (a script won't run without it).
- ./script.sh: the ./ tells bash the script is in THIS folder (not on PATH).
- $(command): capture a command's output into a variable.
- tee: show output on screen AND write it to a file at once.
- >  overwrites a file; >>  appends to it.

## Automotive Relevance
Diagnostics teams run large test suites automatically and save the results as
evidence. This script is the tiny first version of a CI pipeline: run tests
without human typing, keep a dated record. Scales up to GitHub Actions (Week 41).
