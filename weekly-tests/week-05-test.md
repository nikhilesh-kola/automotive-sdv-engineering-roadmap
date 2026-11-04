# Week 5 Test: C Basics

## Part 1: Questions
1.  Why does C need a compile step? What does gcc print when compilation
    succeeds with no problems?
    CPU doesn't understand C, so a compiler converts C into machine language. GCC prints nothing when there are no problems
2.  What does `gcc x.c -o x` do, and what does -o mean?
    It signals the GCC compiler, -o means specifies the output file name
3.  Which printf specifier prints a byte as 2-digit, zero-padded, uppercase hex?
    What does %3d do?
    %02X specifier. %3d - prints the number as a decimal integer in a field at least three characters wide, right-aligned by default.
4.  Why does scanf need & before the variable, when printf does not?
    Because printf reads a value, while scanf needs to write a value into a variable.
5.  What range does each type hold: uint8_t, int8_t, uint16_t?
    0 to 255, -128 to 127, 0 to 65535
6.  Why do automotive C programs use uint8_t instead of int or long?
    Automotive protocols use precisely defined signal sizes. uint8_t guarantees an unsigned 8-bit integer, which is useful for representing one data byte.
7.  Convert 0x2A to decimal. Show your working.
    Hexadecimal is base 16.

The hexadecimal digits are:
- 2 = 2
- A = 10
Every position represents a power of 16.
0x2A=(2times16^1)+(10times16^0)

=(2times16)+(10times1)

=32+10={42}

8.  A payload is declared `uint8_t data[8]`. What are its first and last valid
    indices? What happens in C if the code reads data[8]?
    First - 0, last - 7, [8] is outside the array boundaries, it is an undefined behavior.
9.  Explain the three parts of: for (int i = 0; i < 8; i++)
    int i = 0	Initialization: start at zero
    i < 8	Condition: continue while i is less than eight
    i++	Increment: increase i by one after each iteration
10. What does `void` mean as a function's return type? Give an example from
    this week.
    void means the function does not return a value to its caller. Example: 
    void print_payload(const uint8_t data[8]) {
    for (int i = 0; i < 8; i++) {
        printf("%02X ", (unsigned int)data[i]);
    }
    printf("\n");
}
11. A two-byte signal has high_byte = 0x02 and low_byte = 0x10. What is the
    formula to combine them, and what is the result?
    For a signal transmitted in high-byte-first order, the formula is:

{Result}=({High byte}times256)+{Low byte}

Substituting:

=(2times256)+16

=512+16={528}
In hexadecimal, the result is 0x0210.
12. What does `uint8_t x = 300;` actually store, and why?
uint8_t can represent values only from 0 through 255.

When 300 is converted to an unsigned 8-bit integer, it wraps modulo 256.

300mod256={44}

13. What does this print, and why?
        uint8_t c = 250;
        c = c + 10;
        printf("%d\n", c);
        Expected output 4
        During addition, c is promoted to int, so the addition itself produces 260 without overflowing.

But when 260 is assigned back into uint8_t, the value is reduced modulo 256:

260mod256={4}

14. The byte 0xFF is received. What is its value read as uint8_t, and read as
    int8_t? Why are they different?
    For uint8_t, all eight bits contribute to a nonnegative value:

128+64+32+16+8+4+2+1=255

For int8_t, the two's-complement representation interprets the highest bit with a negative weight:

-128+64+32+16+8+4+2+1=-1

The underlying byte pattern is the same; the signedness determines how it is interpreted.
15. What is the difference between a .h file and a .c file? Why does a .h file
    need an include guard (#ifndef / #define / #endif)?
A .h file is a header file, normally used for declarations that multiple source files need.

A .c file is a source file, normally used for function implementations and executable logic.
Suppose two headers both include can_utils.h. Without a guard, its contents could be included twice in the same translation unit, potentially causing duplicate declaration or definition errors.

Include guards prevent repeated processing of the header contents.
## Part 2: Byte-decoding Task
Done code is in frame_decoder.c

## Part 3: Debugging Task
#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t payload[8] = {200, 100, 50, 25, 10, 5, 2, 1};
    uint16_t total = 0;

    for (int i = 0; i < 8; i++) {
        total = total + payload[i];
    }

    printf("Sum of payload bytes: %d\n", total);
    return 0;
}

Hand calculation: not done before running (calculated after, for checking).
Expected values (calculated after running):
frame 0: 50 C, 300 kPa, -10, 12.3 V
frame 1: 0 C, 255 kPa, 127, 12.8 V
frame 2: -40 C, 1000 kPa, -128, 25.5 V
Compile with -Wall -Wextra: no warnings.
### Part 3 — Debugging Task

**Bug 1: Missing semicolon (Syntax Error)**

- **What was wrong:** The statement `total = total + payload[i]` was missing a semicolon (`;`).
- **How I found it:** GCC reported `error: expected ';' before '}' token` during compilation.
- **How I fixed it:** Added the missing semicolon at the end of the statement.

**Bug 2: Incorrect loop condition (Array Out-of-Bounds)**

- **What was wrong:** The loop used `i <= 8`, which accesses `payload[8]`. Since the array contains eight elements, the valid indices are 0–7.
- **How I found it:** I checked the array size and compared it with the loop condition. The loop executes nine times instead of eight.
- **How I fixed it:** Changed the condition to `i < 8`.

**Bug 3: Incorrect data type (Unsigned Integer Wrapping)**

- **What was wrong:** The variable `total` was declared as `uint8_t`, which can store only values from 0 to 255. The actual sum of the payload is 393.
- **How I found it:** I manually calculated the sum and compared it with the result. With the array boundary corrected, an 8-bit total would store `393 % 256 = 137`.
- **How I fixed it:** Changed `total` from `uint8_t` to `uint16_t`, which can store values up to 65,535.

### Most Dangerous Bug

**Bug 2 — Array Out-of-Bounds Access** is the most dangerous.

Accessing `payload[8]` causes undefined behavior because the program reads outside the allocated array. This may lead to incorrect data, unexpected program behavior, or crashes.

In automotive embedded systems, such errors are particularly dangerous because they can potentially affect the reliability of safety-critical software.

Integer wrapping is also a serious problem, but unsigned wrapping is predictable and defined by C. Out-of-bounds access is more dangerous because its behavior is undefined.

### Final Result

After correcting all three bugs, the program successfully compiled without warnings and printed:

`Sum of payload bytes: 393`

## Part 4: Written Explanation (120–180 words)

### What are signed and unsigned mistakes in C, and why are they dangerous in ECU or CAN-decoding code?

Signed and unsigned mistakes happen when we use the wrong data type to store or interpret a value. In C, `uint8_t` stores values from 0 to 255, whereas `int8_t` stores values from -128 to 127.

For example, during this week's CAN frame-decoding task, I had to decode a torque correction value of `0xF6`. If I treated it as unsigned, the value would be 246. But when interpreted as signed, the correct value is -10. This difference could cause an ECU to interpret a negative correction as a large positive value.

Another example was the debugging task, where I used `uint8_t` to calculate the sum of eight payload bytes. The actual sum was 393, but the variable could only store 137 because it exceeded the 8-bit range.

These mistakes are dangerous because the code may compile successfully while producing incorrect results. In automotive software, such errors could affect how an ECU processes sensor information or controls vehicle components.

---

## Part 5: Self-Score

**My provisional self-score: 60/100**

I understood several basic concepts, including hexadecimal conversion, loops, arrays, functions, and unsigned data types.

However, I needed assistance with the more complicated parts. In the frame-decoding task, I initially made mistakes with the pressure and torque correction functions. I also needed help correcting the debugging task and understanding integer overflow.

I should not award myself full marks for solutions I completed with assistance. My main achievement was attempting the exercises and understanding the corrections.

---

## Part 6: Weekly Reflection

**What felt solid:**

I feel more confident with basic C syntax, variables, arrays, loops, and hexadecimal conversions. I also understand how to extract individual bytes from a CAN payload and apply simple formulas.

**What felt shaky:**

I still need practice choosing the correct function parameters and return types. Signed and unsigned conversions, two-byte calculations, and integer overflow are sometimes confusing. I also need to improve my ability to debug code independently.

**What I want to carry into Week 6:**

I want to strengthen my understanding of how variables are stored in memory before learning pointers. I also want to understand how structs organize CAN data and how bitwise operations work, especially shifting, masking, and extracting individual bits.

My goal for Week 6 is to write more code independently, identify my mistakes without immediately checking solutions, and become more confident with automotive C programming.