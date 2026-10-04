# Week 5 — C Payload Decoder

## Goal
Print an 8-byte CAN payload in hex and decimal, with a summary (byte count,
highest and lowest byte value). Built with a reusable print function.

## Files
- `warmup_print_byte.c` — a void function that prints one byte (index, hex, decimal).
- `payload_decoder.c` — loops over an 8-byte payload, prints each byte, and
  reports the highest and lowest values.

## How to Run
    gcc payload_decoder.c -o payload_decoder
    ./payload_decoder

## Key Concepts
- `#define PAYLOAD_SIZE 8` — one home for the size (array, loop, summary).
- `void` return type — a function that acts (prints) but returns nothing.
- Running max/min: `highest` starts at 0, `lowest` starts at UINT8_MAX (255).
- A value must fit its type: `uint8_t lowest = 300` silently wraps to 44
  (300 - 256). The compiler WARNING caught it; the fix was UINT8_MAX.
- %02X = zero-padded 2-digit hex; %3d = space-padded width-3 decimal.

## Automotive Relevance
A CAN payload is uint8_t[8]. Decoding and summarizing raw bytes is the core of
diagnostic log work. The overflow bug mirrors a real ECU fault class: a value
too large for its type wraps silently and corrupts data.