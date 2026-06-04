# Vehicle Signal Analyzer Project Notes

Date: 23.05.2026

## What I Built

I created a small Python project that reads CSV files containing vehicle signals and calculates min, max, and average values.

## Why This Matters

Automotive engineers often work with measurement logs and diagnostic data. These logs must be parsed, analyzed, and reported clearly.

## Memory-Level Understanding

The CSV file exists on disk as text.

When Python reads the CSV:

1. `csv.DictReader` reads each row as a dictionary.
2. Each column name becomes a key.
3. Numeric values are converted from string to float.
4. Values are stored in lists inside a dictionary.

Example:

```python
signals = {
    "speed_kmh": [0.0, 15.0, 28.0],
    "battery_voltage": [12.5, 12.4, 12.3]
}

Memory model:
signals
  ├── "speed_kmh" → [0.0, 15.0, 28.0]
  └── "battery_voltage" → [12.5, 12.4, 12.3]

Important Functions
read_numeric_signals()

Reads the CSV file and returns a dictionary of signal lists.

calculate_stats()

Calculates minimum, maximum, and average for one list of values.

print_signal_report()

Prints a readable report for all signals.

main()

Controls command-line input, calls the parser, and handles errors.

What I Understood Well
What is a project structure and all its essential files

What Confused Me
All the not yet learned functions and its logics confused me, but I could still read the code

Next Improvements
Add units for each signal.
Skip non-numeric columns automatically.
Detect abnormal values.
Export the report to a text file.
Add proper pytest-based tests.