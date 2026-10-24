# Week 5: C Payload Decoder Project

## Goal
Decode example CAN frames into speed, temperature, RPM and voltage using a
multi-file C project, and flag frames with temperature above 110 C.

## Files
- `decoder.h`: declarations of the decoder functions (with an include guard)
- `decoder.c`: the decoder function code
- `main.c`: three example frames, loops over them, prints a table
- `warmup_frames.c`: 2D array indexing warm-up

## How to Run
    gcc -Wall -Wextra main.c decoder.c -o payload_decoder_project
    ./payload_decoder_project

## Output
    Frame  Speed(km/h)  Temp(C)    RPM  Volt(V)
        0            0       30   1000     12.6
        1           85       90   4000     12.6
        2          200      140   7000     12.6  <-- WARNING: temperature above 110 C

## Concepts Practiced
- 2D array: uint8_t frames[3][8]
- header files, include guards, declaration vs definition
- compiling and linking two .c files
- scale/offset decoding, two-byte values, float return type
- printf field widths (%5d, %7.1f)

## Automotive Relevance
A diagnostic engineer receives many frames, not one. Looping over frames and
decoding each one, with a threshold warning, is the core of any log analyzer.