#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t raw = 0xFF;
    int8_t as_signed = (int8_t)raw;

    uint8_t counter = 255;
    counter = counter + 1;

    printf("0xFF read as uint8_t: %d\n", raw);
    printf("0xFF read as int8_t:  %d\n", as_signed);
    printf("255 + 1 stored back into uint8_t: %d\n", counter);

    return 0;
}