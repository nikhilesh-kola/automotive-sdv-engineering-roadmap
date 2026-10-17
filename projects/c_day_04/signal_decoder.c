#include <stdio.h>
#include <stdint.h>

// Speed: 1 byte, 1 km/h per unit. raw 0..255 -> 0..255 km/h.
int decode_speed(uint8_t raw) {
    return raw;
}

// Temperature: 1 byte, offset -40. raw 0 -> -40C, raw 90 -> 50C.
int decode_temperature(uint8_t raw) {
    return raw - 40;
}

// RPM: 2 bytes combined. High byte is the "big" part (x256), low byte added on.
int decode_rpm(uint8_t high_byte, uint8_t low_byte) {
    return (high_byte * 256) + low_byte;
}

// Voltage: 1 byte, scale 0.1, offset 0.
float decode_voltage(uint8_t raw) {
    return raw * 0.1;
}

int main(void) {
    // A pretend CAN payload: [speed, temp, rpm_high, rpm_low, ...unused...]
    uint8_t payload[8] = {0x55, 0x82, 0x0F, 0xA0, 0x7E, 0x00, 0x00, 0x00};

    int speed = decode_speed(payload[0]);
    int temp  = decode_temperature(payload[1]);
    int rpm   = decode_rpm(payload[2], payload[3]);
    float voltage = decode_voltage(payload[4]);

    printf("Decoded CAN signals:\n");
    printf("  Speed:       %d km/h\n", speed);
    printf("  Temperature: %d C\n", temp);
    printf("  RPM:         %d\n", rpm);
    printf("  Voltage:     %.1f V\n", voltage);

    return 0;
}