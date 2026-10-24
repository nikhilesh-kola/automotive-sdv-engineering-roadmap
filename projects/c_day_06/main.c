#include <stdio.h>
#include <stdint.h>
#include "decoder.h"

#define FRAME_COUNT 3
#define PAYLOAD_SIZE 8
#define TEMP_WARNING_C 110

int main(void) {
    uint8_t frames[FRAME_COUNT][PAYLOAD_SIZE] = {
        {0x00, 0x46, 0x03, 0xE8, 0x78, 0x00, 0x00, 0x00},
        {0x55, 0x82, 0x0F, 0xA0, 0x7E, 0x00, 0x00, 0x00},
        {0xC8, 0xB4, 0x1B, 0x58, 0x84, 0x00, 0x00, 0x00}
    };

    printf("Frame  Speed(km/h)  Temp(C)    RPM  Volt(V)\n");

    for (int i = 0; i < FRAME_COUNT; i++) {
        int speed = decode_speed(frames[i][0]);
        int temp  = decode_temperature(frames[i][1]);
        int rpm   = decode_rpm(frames[i][2], frames[i][3]);
        float voltage = decode_voltage(frames[i][4]);

        printf("%5d  %11d  %7d  %5d %7.1f", i, speed, temp, rpm, voltage);
        if (temp > TEMP_WARNING_C) {
            printf("  <-- WARNING: temperature above %d C", TEMP_WARNING_C);
        }
        printf("\n");
    }

    return 0;
}