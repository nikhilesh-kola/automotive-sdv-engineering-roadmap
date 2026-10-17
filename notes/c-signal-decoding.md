# C Signal Decoding: Scale, Offset, Multi-byte Values — Week 5 Thursday

## Today's Task
Write C functions that convert raw payload bytes into km/h, rpm, temperature
and voltage.

## Key Concepts
- physical = raw * scale + offset
- One byte holds 0-255 only; larger values are split across bytes.
- Two-byte value = (high * 256) + low. The high byte is worth 256x the low byte.
- Return type must fit the result: int truncates 12.6 to 12, float keeps it.

## Memory-Level Understanding
decode_rpm(0x0F, 0xA0)
  high_byte -> 15, low_byte -> 160
  (15 * 256) + 160 = 4000
  return 4000 -> rpm in main

decode_voltage(126)
  raw -> 126
  126 * 0.1 -> 12.6
  return as float -> printf("%.1f") shows 12.6

## Automotive Relevance
This is what a DBC file describes: for each signal, which bytes, what scale,
what offset. Wrong scale, wrong offset or wrong type gives plausible-looking
but wrong values, which is a typical real defect cause.

## What I Understood Well
- understood the concept of converting raw values to relevant units values 

## What Confused Me
- nothing today

## Next Improvement
Handle signed values and byte order (endianness) in the decoders.