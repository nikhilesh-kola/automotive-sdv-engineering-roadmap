# Vehicle Signal Analyzer

## Goal

This project reads vehicle signal CSV files and prints minimum, maximum, and average values for each numeric signal.

## Project Structure

```text
vehicle_signal_analyzer/
├── src/
│   └── signal_parser.py
├── data/
│   ├── vehicle_signals_city.csv
│   ├── vehicle_signals_highway.csv
│   └── vehicle_signals_fault_case.csv
├── tests/
│   └── test_signal_parser.py
├── docs/
│   └── project_notes.md
└── README.md

Example CSV Format
timestamp,speed_kmh,battery_voltage,engine_temp
0,0,12.5,32
1,15,12.4,35

How to Run

From the repository root:
py projects/vehicle_signal_analyzer/src/signal_parser.py projects/vehicle_signal_analyzer/data/vehicle_signals_city.csv

Run with highway data:
py projects/vehicle_signal_analyzer/src/signal_parser.py projects/vehicle_signal_analyzer/data/vehicle_signals_highway.csv

Run with fault-case data:
py projects/vehicle_signal_analyzer/src/signal_parser.py projects/vehicle_signal_analyzer/data/vehicle_signals_fault_case.csv

How to Run the Simple Test
py projects/vehicle_signal_analyzer/tests/test_signal_parser.py

Concepts Practiced
Python project structure
CSV parsing
dictionaries
lists
functions
command-line arguments
simple testing
engineering documentation


Automotive Relevance

Vehicle logs often contain signal values such as:

speed
battery voltage
engine temperature
current
state of charge
diagnostic counters