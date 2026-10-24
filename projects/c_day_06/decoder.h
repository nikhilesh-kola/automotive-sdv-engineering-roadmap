#ifndef DECODER_H
#define DECODER_H

#include <stdint.h>

int decode_speed(uint8_t raw);
int decode_temperature(uint8_t raw);
int decode_rpm(uint8_t high_byte, uint8_t low_byte);
float decode_voltage(uint8_t raw);

#endif