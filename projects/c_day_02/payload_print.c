#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t payload[8] = {0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77};

    printf("CAN payload bytes:\n");
    for (int i = 0; i < 8; i++) {
        printf("  byte[%d] = 0x%02X (decimal %d)\n", i, payload[i], payload[i]);
    }

    return 0;
}