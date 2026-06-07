# Python Functions, Return Values, Docstrings, and Modules — 26.05.2026

## Function

A function is a reusable block of code.

```python
def calculate_power(voltage, current):
    power = voltage * current
    return power

Parameter vs Argument

Parameter = variable name inside function definition.
Argument = actual value passed during function call.

Example:

def calculate_power(voltage, current):
    return voltage * current

calculate_power(12.5, 4.0)

Here:

voltage and current are parameters
12.5 and 4.0 are arguments
return vs print

return gives a value back to the program.
print() only displays a value on the screen.

Docstring

A docstring explains what a function does.

def is_over_limit(value, limit):
    """Return True if value is greater than limit."""
    return value > limit
Module

A module is a Python file containing reusable code.

Example:

from signal_utils import calculate_stats

This imports the function from another file.

Memory-Level Understanding

When a function is called, Python maps arguments to parameters.

calculate_power(12.5, 4.0)

Inside the function:

voltage → 12.5
current → 4.0

When a function returns a value:

power_result = calculate_power(12.5, 4.0)

Memory:

power_result → 50.0
Engineering Rule

Repeated code should become a function.
Reusable functions should move into a module.
Variable names must match the real meaning of the data.    