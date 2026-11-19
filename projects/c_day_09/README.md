# Week 6: CAN_Frame Struct

## Goal
Model a CAN frame as a C struct (id, dlc, data[8]), print frames clearly,
and reject invalid frames before reading their data.

## Files
- `warmup_frame.c`: a two-field struct (id, dlc), printed in hex and decimal
- `can_frame.c`: CAN_Frame struct, print_frame, is_valid_frame, four test frames

## How to Run
    gcc -Wall -Wextra can_frame.c -o can_frame && ./can_frame

## Output
    valid    ID 0x100  DLC 8  Data: 00 11 22 33 44 55 66 77
    valid    ID 0x7E8  DLC 3  Data: 62 F1 90
    valid    ID 0x200  DLC 0  Data:
    INVALID  ID 0x300  DLC 9  (data not printed)
    sizeof(CAN_Frame) = 12

## Key Concepts
- id is uint16_t because a standard CAN ID has 11 bits (up to 0x7FF).
- Print only the first dlc bytes; the rest are not part of the message.
- print_frame takes `const CAN_Frame *`: a pointer (no copy) that only reads.
- is_valid_frame returns bool: dlc <= 8 && id <= 0x7FF.
- Validate before looping over data, or a dlc of 9 reads past data[8].
- sizeof is 12: 2 + 1 + 8 = 11 bytes, rounded up to a multiple of 2.

## Automotive Relevance
Log parsers and diagnostic tools keep id, length and payload together as a
frame. Malformed frames (impossible DLC or ID) must be rejected before their
bytes are used, or the tool reads memory it does not own.