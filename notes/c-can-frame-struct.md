# CAN_Frame Struct: Week 6 Wednesday

## Today's Task
Define a CAN_Frame struct with id, dlc and data[8], print frames, and add an
is_valid_frame check.

## Key Concepts
- printf decides the display: %X shows hex, %d shows decimal. Same stored number.
- Struct initializer fills fields in declaration order; missing data bytes become 0.
- Loop bound i < frame->dlc: only valid bytes are printed.
- * makes a parameter a pointer; const makes it read-only.
- bool return for a yes/no question; && needs both conditions true.
- A dlc field can CLAIM 9 bytes, but data[8] only has 8 slots.

## Memory-Level Understanding
INVALID frame: frame -> address of frames[3]
  frame->dlc <= 8  -> 9 <= 8 -> false
  && stops early -> return false
  main prints INVALID and never calls print_frame, so data[8] is never read.

## Debugging Lessons
- Missing comma between struct initializers: "expected '}' before '{'".
- A failed compile leaves the OLD .exe; running it shows stale output.
  Fix: gcc ... && ./program

## Automotive Relevance
Rejecting malformed frames before using their bytes prevents out-of-bounds reads,
which in ECU software can mean wrong values or crashes.

## What I Understood Well
Understood the CAN frame prints

## What Confused Me
Still sometimes confuses with the struct and pointer, need to practice here.

## Next Improvement
Add a check that dlc matches the number of meaningful bytes, and support CAN FD
lengths (up to 64 bytes).