#include <stdio.h>
#include <stdint.h>

#define STATUS_TEST_FAILED  0x01
#define STATUS_PENDING      0x04
#define STATUS_CONFIRMED    0x08
#define STATUS_WARNING_LAMP 0x80

int main(void) {
    uint8_t statuses[3] = {0x00, 0x09, 0x8D};

    printf("Status  Failed  Pending  Confirmed  Lamp\n");

    for (int i = 0; i < 3; i++) {
        uint8_t s = statuses[i];
        printf("0x%02X  %6d  %7d  %9d  %4d\n", s,
               (s & STATUS_TEST_FAILED) != 0,
               (s & STATUS_PENDING) != 0,
               (s & STATUS_CONFIRMED) != 0,
               (s & STATUS_WARNING_LAMP) != 0);
    }

    return 0;
}