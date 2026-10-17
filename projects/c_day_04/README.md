# Week 5 — C Signal Decoder

## Goal
Convert raw CAN payload bytes into physical values (speed, temperature, RPM,
battery voltage) using one decoder function per signal.

## Files
- `signal_decoder.c` — four decoder functions plus a main that decodes a
  sample 8-byte payload and prints the results.

## How to Run
    gcc signal_decoder.c -o signal_decoder
    ./signal_decoder

## Output
    Speed:       85 km/h
    Temperature: 90 C
    RPM:         4000
    Voltage:     12.6 V

## Key Concepts
- physical_value = (raw * scale) + offset
- Temperature: offset -40, so raw 130 -> 90 C
- RPM needs two bytes: (high_byte * 256) + low_byte, so 0x0F 0xA0 -> 4000
- Voltage: scale 0.1, so raw 126 -> 12.6. It must return float, because int
  would silently truncate it to 12.
- printf("%.1f") rounds the display of a float to one decimal place.

## Automotive Relevance
A CAN frame carries raw bytes, not engineering values. Every diagnostic tool
applies scale and offset (as defined in a DBC file) to turn them into
readable signals. This program is a hand-written version of that step.