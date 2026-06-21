# Python Day 06 — CAN Log Parsing and Diagnostic Summaries

## Goal

This folder contains Python practice scripts for reading CAN-style CSV logs and performing basic diagnostic analysis.

## Files

| File | Purpose |
|---|---|
| `can_log.csv` | Input CAN log with timestamp, CAN ID, DLC, and payload |
| `exercise_01_count_list.py` | Warm-up for counting repeated CAN IDs from a list |
| `can_message_counter.py` | Counts messages per CAN ID from a CSV file |
| `exercise_02_filter_list.py` | Warm-up for filtering dictionaries from a list |
| `can_id_filter.py` | Filters CAN records by CAN ID and exports a new CSV |
| `exercise_03_first_last_timestamp.py` | Warm-up for first and last timestamp logic |
| `diagnostic_log_summarizer.py` | v1 diagnostic log summarizer |

## How to Run

From the repository root:

```powershell
python projects/python_day_06/can_message_counter.py
python projects/python_day_06/can_id_filter.py
python projects/python_day_06/diagnostic_log_summarizer.py


Diagnostic Log Summarizer Output

The summarizer prints:

- total messages
- first timestamp
- last timestamp
- message counts per CAN ID
- top active CAN IDs


Concepts Practiced

- CSV reading with csv.DictReader
- dictionaries
- lists of dictionaries
- functions
- return values
- sorting dictionary items
- CAN log analysis basics