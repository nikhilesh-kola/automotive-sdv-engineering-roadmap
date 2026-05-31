# CSV Vehicle Signal Analyzer V2

## Goal

This script reads a CSV file containing vehicle signal data and prints the minimum, maximum, and average values for selected signals.

## Signals Analyzed

- Speed in km/h
- Battery voltage in V
- Engine temperature in °C

## Required CSV Columns

The CSV file must contain these columns:

```csv
timestamp,speed_kmh,battery_voltage,engine_temp

Example CSV
timestamp,speed_kmh,battery_voltage,engine_temp
0,0,12.4,35
1,10,12.3,36
2,25,12.2,38
3,40,12.1,42
4,55,12.0,45