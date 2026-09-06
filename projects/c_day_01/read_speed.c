#include <stdio.h>

int main(void) {
    int speed_kmh;

    printf("Enter vehicle speed in km/h: ");
    scanf("%d", &speed_kmh);

    printf("You entered: %d km/h\n", speed_kmh);
    return 0;
}