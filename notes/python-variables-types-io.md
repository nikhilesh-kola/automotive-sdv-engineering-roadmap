# Python Variables, Types, Input/Output — 18.05.2026

## What is a variable?

A variable is a name that stores a value.

Example:

```python
vehicle = "BMW i4"

Main Python types learned today
| Type  | Meaning        | Example |
| ----- | -------------- | ------- |
| str   | text           | "OBD"   |
| int   | whole number   | 5       |
| float | decimal number | 12.5    |
| bool  | true/false     | True    |

What does input() do?

input() takes text from the user.

Important: input is always received as a string first.

What does print() do?

print() displays output on the screen.

What is type conversion?

Type conversion changes a value from one type into another.

Examples:
age = int(input("Enter age: "))
voltage = float(input("Enter voltage: "))

What I learned today
input() always gives a string.
Use int() for whole numbers.
Use float() for decimal numbers.
Use bool for true/false values.
Use f-strings to print readable output.
Choose data types based on meaning.
Engineering output should show correct units.
Automotive connection

Python can be used to:

parse diagnostic logs
calculate signal values
automate diagnostic tests
generate reports
build small tools for CAN/UDS testing

What confused me today?
To use an empty line between variables, calculations and printing lines.

What I understood well?
Defining all variable types and printing them.