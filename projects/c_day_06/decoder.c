#include "decoder.h"

int decode_speed(uint8_t raw) {
    return raw;
}

int decode_temperature(uint8_t raw) {
    return raw - 40;
}

int decode_rpm(uint8_t high_byte, uint8_t low_byte) {
    return (high_byte * 256) + low_byte;
}
float decode_voltage(uint8_t raw) {
    return raw * 0.1;
}    
