# C Integer Types and Overflow: Flashcards

## Flashcard 1
Q: What range does uint8_t hold, and how many bytes is it?
A: 0 to 255, exactly 1 byte (8 bits).

## Flashcard 2
Q: What range does int8_t hold?
A: -128 to 127. Same 8 bits, but the top bit is the sign.

## Flashcard 3
Q: What range does uint16_t hold?
A: 0 to 65535 (2 bytes). Enough for RPM, which a single byte can't hold.

## Flashcard 4
Q: The byte 0xFF is received. What is its value?
A: 255 if read as uint8_t, -1 if read as int8_t. Same bits, different reading.

## Flashcard 5
Q: What does `uint8_t x = 300;` actually store?
A: 44. 300 doesn't fit in 8 bits, so it wraps: 300 - 256 = 44.

## Flashcard 6
Q: What happens when a uint8_t holding 255 gets 1 added and stored back?
A: It wraps to 0.

## Flashcard 7
Q: Why didn't (high_byte * 256) overflow in decode_rpm?
A: C promotes uint8_t to int before arithmetic, so 15 * 256 = 3840 is computed
in a wider type. Overflow only happens when storing into a too-small type.

## Flashcard 8
Q: Why must decode_voltage return float, not int?
A: int truncates 12.6 to 12 and silently loses the decimal.

## Flashcard 9
Q: Why do ECU/CAN programs use uint8_t instead of int or long?
A: uint8_t is exactly 1 byte on every platform. int and long vary (long was
4 bytes on my Windows GCC, 8 on many Linux systems).

## Flashcard 10
Q: Why is a wrong signed/unsigned choice dangerous in a decoder?
A: The output looks plausible but is wrong (for example -1 instead of 255), so
the defect is silent and easy to miss.