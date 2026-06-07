# Python Data Structures and Loops — 25.05.2026

## Topics

- lists
- tuples
- dictionaries
- for loops
- while loops

## List

A list stores multiple values in order and can be changed.

```python
ecu_names = ["Engine ECU", "Battery ECU", "Brake ECU"]

Memory model:

ecu_names → ["Engine ECU", "Battery ECU", "Brake ECU"]
              0             1              2

Tuple

A tuple stores multiple values in order but should not be changed.

dtc_record = ("P0300", "Random misfire detected", "High")

Use tuples for fixed records.

Dictionary

A dictionary stores key-value pairs.

dtc_info = {
    "P0300": "Random misfire detected",
    "U0100": "Lost communication with ECM"
}

Memory model:

dtc_info
  ├── "P0300" → "Random misfire detected"
  └── "U0100" → "Lost communication with ECM"
for Loop

A for loop repeats for every item in a collection.

for ecu in ecu_names:
    print(ecu)

Memory-level idea:

Loop round 1: ecu → first item
Loop round 2: ecu → second item
Loop round 3: ecu → third item
while Loop

A while loop repeats while a condition is true.

retry_count = 0

while retry_count < 3:
    print("Trying request")
    retry_count = retry_count + 1

Important:

A while loop must move toward stopping, otherwise it can become infinite.

Automotive Examples
ECU names can be stored in a list.
One DTC record can be stored in a tuple.
DTC code-description pairs can be stored in a dictionary.
Signal values can be processed with loops.
Diagnostic retry logic can be modeled with a while loop.

What I Understood Well
Differences between List, dictionary and for loop , while loop. All their syntax. Understood all the practice scripts

What Confused Me
While loop needs a failure message to show the failure message.

Next Focus

Use loops and dictionaries to process multiple diagnostic signals more cleanly.              