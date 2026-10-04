#include <stdio.h>
#include <stdint.h>

#define PAYLOAD_SIZE 8

// Prints one byte's index, hex, and decimal value.
void print_byte(int index, uint8_t value) {
    printf("  byte[%d] = 0x%02X (decimal %3d)\n", index, value, value);
}

int main(void) {
    uint8_t payload[PAYLOAD_SIZE] = {0x00, 0x11, 0x22, 0xFF, 0x44, 0x55, 0x66, 0x77};

    printf("CAN payload (%d bytes):\n", PAYLOAD_SIZE);

    uint8_t highest = 0;
    uint8_t lowest = 255;
    for (int i = 0; i < PAYLOAD_SIZE; i++) {
        print_byte(i, payload[i]);
        if (payload[i] > highest) {
            highest = payload[i];
        }
        if (payload[i] < lowest) {
            lowest = payload[i];
        }
    }

    printf("Summary: %d bytes, highest = 0x%02X (%d), lowest = 0x%02X (%d)\n",
       PAYLOAD_SIZE, highest, highest, lowest, lowest);

    return 0;
}