#include <stdio.h>
#include <stdint.h>

// Prints one byte's index, hex, and decimal value.
void print_byte(int index, uint8_t value) {
    printf("  byte[%d] = 0x%02X (decimal %3d)\n", index, value, value);
}

int main(void) {
    print_byte(0, 0xA5);
    print_byte(1, 0x0F);
    return 0;
}