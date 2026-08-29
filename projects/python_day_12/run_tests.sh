#!/bin/bash
# run_tests.sh - runs the Week 3 test suite and saves a timestamped report.

# Create a timestamp like 2026-08-09_1530 for a unique report filename.
TIMESTAMP=$(date +"%Y-%m-%d_%H%M")
REPORT_FILE="reports/test_report_${TIMESTAMP}.txt"

echo "Running CAN parser tests..."
echo "Report will be saved to: ${REPORT_FILE}"

# Run the tests and save output to the report file.
# 'tee' shows output on screen AND writes it to the file at the same time.
py -m pytest ../python_day_09/test_can_parser.py -v | tee "${REPORT_FILE}"

echo "${TIMESTAMP} - Test run completed." >> reports/history.txt
echo "Done. Report saved."
