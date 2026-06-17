# Where Dictionaries Help in Diagnostics — 29.05.2026

## Short Note

Dictionaries are very useful in automotive diagnostics because diagnostic data usually has named information.

For example, a CAN message is not just one value. It has multiple fields:

- timestamp
- CAN ID
- DLC
- payload

A dictionary can store one CAN message clearly:

```python
can_message = {
    "timestamp": "0.000",
    "can_id": "0x100",
    "dlc": "8",
    "payload": "11 22 33 44 55 66 77 88"
}

This is easier to understand than using a list like:

["0.000", "0x100", "8", "11 22 33 44 55 66 77 88"]

With a list, I must remember that index 0 means timestamp and index 1 means CAN ID. With a dictionary, the key explains the meaning.

Dictionaries also help with counting repeated diagnostic data.

Example:

message_counts = {
    "0x100": 3,
    "0x200": 2,
    "0x300": 2
}

This tells me how many times each CAN ID appeared in a trace.

Dictionaries help in diagnostics for:

CAN message rows
DTC code descriptions
ECU status information
signal name to signal values
CAN ID message counts
filtering and report generation
Memory-Level Understanding

One CAN row:

{
    "timestamp": "0.000",
    "can_id": "0x100",
    "dlc": "8",
    "payload": "11 22 33 44 55 66 77 88"
}

Many CAN rows:

records = [
    {"timestamp": "0.000", "can_id": "0x100"},
    {"timestamp": "0.010", "can_id": "0x200"},
    {"timestamp": "0.020", "can_id": "0x100"}
]

Message counts:

message_counts = {
    "0x100": 2,
    "0x200": 1
}