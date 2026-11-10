#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t speed = 85;
    uint16_t rpm = 4000;

    printf("speed: value = %d, address = %p, size = %zu byte(s)\n",
           speed, (void *)&speed, sizeof(speed));
    printf("rpm:   value = %d, address = %p, size = %zu byte(s)\n",
           rpm, (void *)&rpm, sizeof(rpm));

    return 0;
}