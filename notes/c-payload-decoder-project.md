# C Payload Decoder Project: Week 5 Saturday

## Today's Task
Build a multi-file C project that decodes three CAN frames into speed,
temperature, RPM and voltage, with an overheating warning.

## Key Concepts
- 2D array: frames[row][col], row = which frame, col = which byte.
- .h = declarations (names and types); .c = definitions (the code).
- Include guard (#ifndef/#define/#endif) stops double-declaration errors.
- Compile each .c to an object file, then the linker joins them.
- Adding a function to a multi-file project touches 3 places: .h, .c, main.c.
- printf width: %5d, %7.1f line columns up; put units in the header, not each row.

## Memory-Level Understanding
frames[2][1] = row 2, byte 1 = 0xB4 = 180 -> decode_temperature -> 140 C.
The header lets the compiler check calls; the linker finds the real code.

## Automotive Relevance
Decoding many frames and flagging a signal above a threshold is the shape of
real log analysis.

## My Own Explanation
A .h file (header) contains declarations: the names, parameter types and return
types of functions, with no code inside. A .c file contains the definitions: the
actual code that runs. main.c includes decoder.h so the compiler knows the
signature of each function (what arguments it takes, what it returns) and can
check every call before the real code is attached. The linker then connects each
call to its definition in decoder.o. If I forget the declaration in the .h file,
gcc rejects the call to the new function. If I forget the definition in the .c
file, the linker fails with "undefined reference". Adding decode_voltage meant
touching all three files: decoder.h, decoder.c and main.c.

## What I Understood Well
2D array indexing (frames[row][col]), and how three files fit together as
declaration, definition and caller. My byte-4 test values gave 12.0, 12.6 and
13.2, so each frame is decoded separately.

## What Confused Me
Why a function needs both a declaration and a definition. Resolved: the
declaration lets the compiler check calls, the definition is the code the linker
attaches.

## Next Improvement
Read the frames from a CSV file instead of hard-coding them (file I/O in C).