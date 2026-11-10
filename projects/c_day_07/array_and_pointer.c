#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t payload[4] = {0x10, 0x20, 0x30, 0x40};
    uint8_t *p = payload;

    for (int i = 0; i < 4; i++) {
        printf("i=%d  payload[i]=0x%02X  *(p+i)=0x%02X  address=%p\n",
               i, payload[i], *(p + i), (void *)(p + i));
    }

    uint16_t rpm_values[3] = {1000, 4000, 7000};
    uint16_t *q = rpm_values;

    for (int i = 0; i < 3; i++) {
        printf("rpm_values[%d] = %d  address=%p\n", i, *(q + i), (void *)(q + i));
    }

    return 0;
}