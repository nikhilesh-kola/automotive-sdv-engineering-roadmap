#include <stdio.h>
#include <stdint.h>

typedef struct {
    uint16_t id;
    uint8_t dlc;
} MiniFrame;

int main(void) {
    MiniFrame f = {0x7E8, 8};

    printf("id  = 0x%03X\n", f.id);
    printf("dlc = %d\n", f.dlc);

    return 0;
}