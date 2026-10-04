# C Payload Decoder & Integer Overflow — Week 5 Wednesday

## Today's Task
Build a structured C program that prints an 8-byte payload in hex + decimal
with a highest/lowest summary, using a reusable print function.

## Key Concepts
- void function = acts but returns nothing (print_byte); vs int function = returns a value.
- #define = named constant; single source of truth (like Week 3's EXPECTED_PAYLOAD_BYTES).
- Running max starts at 0; running min starts at UINT8_MAX (255) - mirror images.
- Integer overflow: a uint8_t holds only 0-255. Assigning 300 wraps to 44 (300-256).

## Memory-Level Understanding
uint8_t lowest = 300  ->  does not fit  ->  wraps to 44 silently.
Correct answer by luck here (smallest byte was 0 < 44), but WRONG for a payload
whose smallest byte is 45-255. Fix: lowest = UINT8_MAX (255), which fits and is
guaranteed >= any real byte.

## Why This Matters
The bug was SILENT - right output on this data, wrong on other data. The compiler
WARNING caught it. This is C's compile step acting as a safety net, and the exact
bug class behind real ECU faults (value too big for its type).

## My Own Explanation
300 does NOT fit in a uint8_t. So what happens?
   300 in binary wraps around past 255:
   300 - 256 = 44

## What I Understood Well
Unlike in python, C only accepts values that are in its range. And silently throws an error or warning.

## What Confused Me
Only thing from above about the value ranges in C

## Next Improvement
Add a function that returns the max (instead of computing it inline in main).