# Python CAN ID Filter and CSV Export — 28.05.2026

## Today's Task

Build a function that filters CAN records by CAN ID and exports the filtered data to a new CSV file.

## Input CSV

The input CSV contains:

- timestamp
- can_id
- dlc
- payload

Example:

```csv
timestamp,can_id,dlc,payload
0.000,0x100,8,11 22 33 44 55 66 77 88
0.010,0x200,8,AA BB CC DD EE FF 00 11

Main Idea

The script reads every row from the input CSV.

If the row CAN ID matches the target CAN ID, the row is added to a list called filtered_records.

Then the filtered records are written into a new CSV file.

Important Functions

filter_records_by_can_id()

def filter_records_by_can_id(input_file_path, target_can_id):
    """Return all CSV records that match the target CAN ID."""

This function:

1. Opens the input CSV file.
2. Reads each row using csv.DictReader.
3. Checks row["can_id"].
4. Adds matching rows to filtered_records.
5. Returns the filtered records.

write_records_to_csv()
def write_records_to_csv(output_file_path, records):
    """Write filtered CAN records to a new CSV file."""

This function:

1. Creates a new CSV file.
2. Writes the header row.
3. Writes each filtered record.


DictReader vs DictWriter

csv.DictReader reads CSV rows as dictionaries.

Example:

{
    "timestamp": "0.000",
    "can_id": "0x100",
    "dlc": "8",
    "payload": "11 22 33 44 55 66 77 88"
}

csv.DictWriter writes dictionaries back into a CSV file.

Memory-Level Understanding

A single CAN row in memory:

{
    "timestamp": "0.000",
    "can_id": "0x100",
    "dlc": "8",
    "payload": "11 22 33 44 55 66 77 88"
}

A filtered list in memory:

filtered_records = [
    {
        "timestamp": "0.000",
        "can_id": "0x100",
        "dlc": "8",
        "payload": "11 22 33 44 55 66 77 88"
    },
    {
        "timestamp": "0.020",
        "can_id": "0x100",
        "dlc": "8",
        "payload": "12 23 34 45 56 67 78 89"
    }
]

Memory anchor:

Dictionary = one CAN row
List of dictionaries = many CAN rows
Automotive Relevance

Filtering by CAN ID is useful because CAN logs usually contain messages from many ECUs or functions.

Filtering helps an engineer focus on:

one message ID
one ECU-related message group
one signal source
one suspicious communication pattern


What I Understood Well
The meaning and memory level understanding of both functions filtering and then writing back to a CSV

What Confused Me
Nothing major, just the syntaxes of the functions, but need to practice more to get familiar

Next Improvement

Build a diagnostic-log summarizer that prints message counts, first/last timestamp, and top active CAN IDs.