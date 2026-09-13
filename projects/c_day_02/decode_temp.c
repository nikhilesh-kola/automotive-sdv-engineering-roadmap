#include <stdio.h>
#include <stdint.h>

// Converts a raw temperature byte into degrees Celsius (offset -40).
int decode_temperature(uint8_t raw_byte) {
    int celsius = raw_byte - 40;
    return celsius;
}

int main(void) {
    uint8_t raw_values[4] = {40, 90, 130, 0};

    for (int i = 0; i < 4; i++) {
        int temp = decode_temperature(raw_values[i]);
        printf("raw %3d -> %d C\n", raw_values[i], temp);
    }

    return 0;
}