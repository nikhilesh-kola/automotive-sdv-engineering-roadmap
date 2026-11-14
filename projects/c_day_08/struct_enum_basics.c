#include <stdio.h>
#include <stdint.h>

typedef enum {
    SESSION_DEFAULT = 1,
    SESSION_PROGRAMMING = 2,
    SESSION_EXTENDED = 3
} Session;

typedef struct {
    uint8_t speed_kmh;
    int temp_c;
    uint16_t rpm;
} VehicleSample;

void print_sample(VehicleSample *s) {
    printf("speed=%d km/h, temp=%d C, rpm=%d\n", s->speed_kmh, s->temp_c, s->rpm);
}

int main(void) {
    VehicleSample sample = {85, 90, 4000};
    Session session = SESSION_EXTENDED;

    print_sample(&sample);
    sample.temp_c = 95;
    print_sample(&sample);

    printf("session value = %d\n", session);
    printf("sum of field sizes = %zu, sizeof(VehicleSample) = %zu\n",
           sizeof(uint8_t) + sizeof(int) + sizeof(uint16_t), sizeof(VehicleSample));

    return 0;
}