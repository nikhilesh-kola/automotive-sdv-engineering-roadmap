# Python Data Structures Flashcards — 29.05.2026

## Flashcard 1

Q: What is a list in Python?

A: A list is an ordered, changeable collection of values.

Example:

```python
ecu_names = ["Engine ECU", "Battery ECU", "Brake ECU"]

List = ordered and changeable

## Flashcard 2

Q: How do I access the first item in a list?

A: Use index 0.

Example:

ecu_names[0]

Python indexes start from 0.

## Flashcard 3

Q: What does .append() do?

A: .append() adds a new value to the end of a list.

Example:

dtc_codes.append("P0420")

## Flashcard 4

Q: What is a tuple?

A: A tuple is an ordered collection that should not be changed.

Example:

dtc_record = ("P0300", "Random misfire detected", "High")

Memory anchor:

Tuple = fixed record

## Flashcard 5

Q: What is a dictionary?

A: A dictionary stores key-value pairs.

Example:

ecu_status = {
    "Engine ECU": "OK",
    "Brake ECU": "FAULT"
}

Memory anchor:

Dictionary = key-value container

## Flashcard 6

Q: How do I access a value from a dictionary?

A: Use the key.

Example:

ecu_status["Engine ECU"]

## Flashcard 7

Q: What does .items() do in a dictionary?

A: .items() gives key-value pairs for looping.

Example:

for ecu_name, status in ecu_status.items():
    print(ecu_name, status)

## Flashcard 8

Q: What is a for loop?

A: A for loop repeats code for every item in a collection.

Example:

for dtc in dtc_codes:
    print(dtc)

Memory anchor:

for loop = for each item

## Flashcard 9

Q: What is a while loop?

A: A while loop repeats while a condition is true.

Example:

retry_count = 0

while retry_count < 3:
    print("Trying request")
    retry_count = retry_count + 1

Memory anchor:

while loop = while condition is true

## Flashcard 10

Q: Why must a while loop change a variable inside the loop?

A: Because the condition must eventually become false. Otherwise, the loop can run forever.

## Flashcard 11

Q: What is a function?

A: A function is a reusable block of code.

Example:

def calculate_stats(values):
    return min(values), max(values), sum(values) / len(values)


## Flashcard 12

Q: What is the difference between parameter and argument?

A: A parameter is the name inside the function definition. An argument is the actual value passed during the function call.

Example:

def calculate_power(voltage, current):
    return voltage * current

calculate_power(12.5, 4.0)

Here, voltage and current are parameters.
12.5 and 4.0 are arguments.

## Flashcard 13

Q: What is the difference between return and print()?

A: return gives a value back to the program. print() only displays a value on the screen.

Memory anchor:

return = gives back
print = shows


## Flashcard 14

Q: What is a module?

A: A module is a Python file that contains reusable code.

Example:

from signal_utils import calculate_stats


## Flashcard 15

Q: What does csv.DictReader do?

A: It reads each CSV row as a dictionary.

Example row:

{
    "timestamp": "0.000",
    "can_id": "0x100",
    "dlc": "8",
    "payload": "11 22 33 44 55 66 77 88"
}


## Flashcard 16

Q: What does csv.DictWriter do?

A: It writes dictionaries into a CSV file.

## Flashcard 17

Q: What is the dictionary counting pattern?

A:

if can_id not in message_counts:
    message_counts[can_id] = 0

message_counts[can_id] = message_counts[can_id] + 1

This counts how many times each CAN ID appears.

## Flashcard 18

Q: What is a list of dictionaries?

A: A list that stores multiple dictionary records.

Example:

filtered_records = [
    {"timestamp": "0.000", "can_id": "0x100"},
    {"timestamp": "0.020", "can_id": "0x100"}
]

Memory anchor:

Dictionary = one row
List of dictionaries = many rows


## Flashcard 19

Q: Why are dictionaries useful for CAN logs?

A: A CAN row has named fields like timestamp, CAN ID, DLC, and payload. A dictionary stores these fields clearly using keys.

Flashcard 20

Q: What is the main Git workflow?

A:

git status → git add . → git commit -m "message" → git push origin main