#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

typedef struct {
    uint8_t speed_kmh;
    int temp_c;
    uint16_t rpm;
} VehicleSample;

int main(void) {
    printf("speed_kmh offset = %zu\n", offsetof(VehicleSample, speed_kmh));
    printf("temp_c    offset = %zu\n", offsetof(VehicleSample, temp_c));
    printf("rpm       offset = %zu\n", offsetof(VehicleSample, rpm));
    printf("total size       = %zu\n", sizeof(VehicleSample));
    return 0;
}