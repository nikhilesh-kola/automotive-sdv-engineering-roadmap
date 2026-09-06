#include <stdio.h>

int main(void) {
    int rpm = 2450;              // whole number
    float voltage = 12.6;        // decimal number
    char gear = 'D';             // a single character

    printf("RPM:     %d\n", rpm);
    printf("Voltage: %.1f V\n", voltage);
    printf("Gear:    %c\n", gear);

    return 0;
}