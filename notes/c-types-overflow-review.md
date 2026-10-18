# C Types, Signedness and Overflow: Week 5 Review

## Active Recall
1. What are the ranges of uint8_t, int8_t and uint16_t?
uint8_t: 0 to 255. int8_t: -128 to 127. uint16_t: 0 to 65535.

2. Why can 0xFF mean both 255 and -1?
0xFF is eight 1-bits. Read as unsigned, every bit adds its value:
128+64+32+16+8+4+2+1 = 255. Read as signed, the top bit is worth -128
instead of +128, so -128 + 127 = -1. The bits in memory are identical;
only the way I read them changes.

3. Why did `uint8_t lowest = 300` become 44, and why did my program still give
   the right answer?
A uint8_t holds only 0-255, so 300 wrapped around: 300 - 256 = 44. The program
still printed the right minimum because the smallest byte in the payload was
0x00 = 0, and 0 < 44, so lowest was updated to 0 anyway. With a payload whose
smallest byte was between 45 and 255, lowest would have stayed at 44 and the
answer would have been wrong.

4. Why didn't `high_byte * 256` overflow?
C does the multiplication in int, which is wider than a byte, so 15 * 256 = 3840
fits. Overflow only happens when a result is stored back into a type that is too
small, like putting 300 into a uint8_t.

5. Why must a CAN decoder pick its types deliberately?
If a decoder reads a byte with the wrong type, for example 0xFF as signed, the
output is a plausible but wrong number (-1 instead of 255). There is no error and
no crash, so the defect is silent and easy to miss. The type is part of the
decoding rule, just like scale and offset.

## What Understood Well
The ranges of the types, and the demo results (255, -1, 0).

## What Confused Me
Too many separate rules to memorize. Resolved by reducing them to two ideas:
fixed bits set the range, and the same bits can be read two ways.

## My Own Explanation
Integer types matter in ECU software because every value lives in a fixed number
of bits, and that limits what it can hold. For example, I wrote
`uint8_t lowest = 300` and it silently became 44, and 0xFF is 255 or -1
depending on the type. This is dangerous because C gives no error: the program
runs and prints plausible but wrong numbers. So when I write a decoder, I choose
the type deliberately, check that values fit it, and read compiler warnings.