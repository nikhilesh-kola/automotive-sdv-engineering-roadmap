#include <stdio.h>

int main(void) {
    int speed_kmh = 87;
    int rpm = 2450;
    int coolant_temp_c = 90;

    printf("Vehicle speed: %d km/h\n", speed_kmh);
    printf("Engine RPM:    %d\n", rpm);
    printf("Coolant temp:  %d C\n", coolant_temp_c);

    return 0;
}
