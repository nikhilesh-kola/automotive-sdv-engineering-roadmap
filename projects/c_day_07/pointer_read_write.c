#include <stdio.h>
#include <stdint.h>

void reset_counter(uint8_t *counter) {
    *counter = 0;
}

int main(void) {
    uint8_t alive_counter = 9;
    uint8_t *p = &alive_counter;

    printf("alive_counter = %d\n", alive_counter);
    printf("read through pointer: %d\n", *p);

    *p = 15;
    printf("after *p = 15: alive_counter = %d\n", alive_counter);

    reset_counter(&alive_counter);
    printf("after reset_counter: alive_counter = %d\n", alive_counter);

    return 0;
}