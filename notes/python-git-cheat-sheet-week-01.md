# Python and Git Cheat Sheet — Week 01

Date: 22.05.2026

## 1. Python Variables

A variable is a name that points to a value or object in memory.

Example:

```python
vehicle = "BMW i4"
dtc_count = 3
battery_voltage = 12.4
dtc_present = True
```

Memory-level idea:

```text
vehicle         → "BMW i4"
dtc_count       → 3
battery_voltage → 12.4
dtc_present     → True
```

## 2. Basic Python Types

| Type    | Meaning        | Example |
| ------- | -------------- | ------- |
| `str`   | Text           | `"UDS"` |
| `int`   | Whole number   | `3`     |
| `float` | Decimal number | `12.4`  |
| `bool`  | True/False     | `True`  |

Rule:

```text
Choose data type based on meaning.
```

Examples:

```python
dtc_code = "P0300"      # string, because it contains a letter
dtc_count = 3           # integer, because it is a count
voltage = 12.4          # float, because it is a measured value
dtc_present = True      # boolean, because it is yes/no
```

## 3. Input and Output

`print()` displays output.

```python
print("Hello")
print(f"Voltage: {voltage:.2f} V")
```

`input()` reads user input as text.

```python
name = input("Enter your name: ")
```

Important:

```text
input() always returns a string first.
```

So convert when needed:

```python
age = int(input("Enter age: "))
voltage = float(input("Enter voltage: "))
```

## 4. Lists

A list stores multiple values.

```python
speed_values = [0, 10, 25, 40, 55]
```

Memory-level idea:

```text
speed_values → [0, 10, 25, 40, 55]
```

Index positions start at 0:

```python
speed_values[0]  # 0
speed_values[1]  # 10
```

Useful list functions:

```python
min(speed_values)
max(speed_values)
sum(speed_values)
len(speed_values)
```

Average formula:

```python
average = sum(values) / len(values)
```

## 5. CSV Reading

CSV means comma-separated values.

Example:

```csv
timestamp,speed_kmh,battery_voltage,engine_temp
0,0,12.4,35
1,10,12.3,36
```

Python CSV reading pattern:

```python
import csv

with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        speed_values.append(float(row["speed_kmh"]))
```

Important:

```text
CSV values are read as strings first.
```

So numeric values must be converted:

```python
float(row["speed_kmh"])
```

## 6. Functions

A function stores reusable logic.

```python
def calculate_stats(values):
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    return minimum, maximum, average
```

Calling the function:

```python
speed_min, speed_max, speed_avg = calculate_stats(speed_values)
```

Memory-level idea:

```text
values → same list object passed into the function
```

A list passed into a function is not automatically copied.

## 7. Command-Line Arguments

Python stores command-line arguments in:

```python
sys.argv
```

Example command:

```powershell
python script.py data.csv
```

Memory-level view:

```text
sys.argv → ["script.py", "data.csv"]
              0          1
```

Usage:

```python
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <csv_file_path>")
    sys.exit(1)

csv_file_path = sys.argv[1]
```

## 8. Error Handling

Use `try` and `except` to handle expected errors.

```python
try:
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)

except FileNotFoundError:
    print("Error: File not found.")
```

Common errors:

| Error               | Meaning                             |
| ------------------- | ----------------------------------- |
| `FileNotFoundError` | File path does not exist            |
| `KeyError`          | Expected CSV column is missing      |
| `ValueError`        | Value cannot be converted to number |

## 9. Git Basics

Git tracks changes locally.

GitHub stores Git repositories online.

Basic workflow:

```powershell
git status
git add .
git commit -m "Clear commit message"
git push origin main
```

## 10. Git Commands

| Command                   | Meaning                                    |
| ------------------------- | ------------------------------------------ |
| `git status`              | Shows changed, staged, and untracked files |
| `git add .`               | Stages all changes                         |
| `git commit -m "message"` | Saves a snapshot with a message            |
| `git log --oneline`       | Shows short commit history                 |
| `git branch`              | Shows available branches                   |
| `git push origin main`    | Uploads local commits to GitHub            |

## 11. My Weekly Learning Pattern

```text
Small script first
Understand memory model
Run and test
Improve with functions/error handling
Write notes
Commit to GitHub
```

## 12. Five Questions

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



## 13. Week 01 Summary

This week I learned the basics of Python variables, types, input/output, lists, CSV reading, functions, command-line arguments, error handling, and Git workflow.

My first practical engineering tool is a CSV vehicle signal analyzer that reads vehicle signal data and prints min, max, and average values.
