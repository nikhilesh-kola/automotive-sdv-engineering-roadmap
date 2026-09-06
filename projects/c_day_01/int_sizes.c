#include <stdio.h>
#include <stdint.h>

int main(void) {
    printf("Size of char:     %zu byte(s)\n", sizeof(char));
    printf("Size of int:      %zu byte(s)\n", sizeof(int));
    printf("Size of long:     %zu byte(s)\n", sizeof(long));
    printf("Size of uint8_t:  %zu byte(s)\n", sizeof(uint8_t));
    printf("Size of uint16_t: %zu byte(s)\n", sizeof(uint16_t));
    printf("Size of uint32_t: %zu byte(s)\n", sizeof(uint32_t));

    return 0;
}