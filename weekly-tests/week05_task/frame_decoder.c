#include <stdio.h>
#include <stdint.h>

// Oil temperature: 1 byte, raw - 40
int decode_oil_temp(uint8_t raw) {
    return raw - 40;
}

// Oil pressure: 2 bytes, high byte first
uint16_t decode_pressure(uint8_t high_byte, uint8_t low_byte) {
    return ((uint16_t)high_byte << 8) | low_byte;
}

// Torque correction: 1 signed byte
int8_t decode_correction(uint8_t raw) {
    return (int8_t)raw;
}

// Battery voltage: 1 byte, scaled by 0.1
float decode_voltage(uint8_t raw) {
    return raw * 0.1f;
}

int main(void) {

    // Three CAN frames, each containing 8 bytes
    uint8_t frames[3][8] = {
        {0x5A, 0x01, 0x2C, 0xF6, 0x7B, 0x00, 0x00, 0x00},
        {0x28, 0x00, 0xFF, 0x7F, 0x80, 0x00, 0x00, 0x00},
        {0x00, 0x03, 0xE8, 0x80, 0xFF, 0x00, 0x00, 0x00}
    };

    // Print the header with units
    printf("Decoded CAN Signals:\n");
    printf("---------------------------------------------------------------\n");
    printf("%-8s %-14s %-16s %-12s %-12s\n",
           "Frame", "Oil Temp (C)", "Pressure (kPa)",
           "Correction", "Voltage (V)");
    printf("---------------------------------------------------------------\n");

    // Decode all three frames
    for (int i = 0; i < 3; i++) {

        int temp = decode_oil_temp(frames[i][0]);

        uint16_t pressure = decode_pressure(
            frames[i][1], frames[i][2]
        );

        int8_t correction = decode_correction(frames[i][3]);

        float voltage = decode_voltage(frames[i][4]);

        // Print one row per frame
        printf("%-8d %-14d %-16u %-12d %-12.1f\n",
               i, temp, (unsigned int)pressure,
               (int)correction, (double)voltage);
    }

    return 0;
}
