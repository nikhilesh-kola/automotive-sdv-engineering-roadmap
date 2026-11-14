#include <stdio.h>
#include <stdint.h>

// Prints a byte as 8 bits, with a space between the two nibbles.
void print_bits(uint8_t value) {
    for (int bit = 7; bit >= 0; bit--) {
        putchar(((value >> bit) & 1) ? '1' : '0');
        if (bit == 4) {
            putchar(' ');
        }
    }
}

void show(const char *label, uint8_t value) {
    printf("%-8s = 0x%02X = ", label, value);
    print_bits(value);
    printf("\n");
}

int main(void) {
    uint8_t a = 0xB4;
    uint8_t b = 0x0F;

    show("a", a);
    show("b", b);
    show("a & b", a & b);
    show("a | b", a | b);
    show("a ^ b", a ^ b);
    show("a >> 4", a >> 4);
    show("a << 1", a << 1);
    show("~a", ~a);

    return 0;
}