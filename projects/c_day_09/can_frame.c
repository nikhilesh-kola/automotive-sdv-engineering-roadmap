#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

#define MAX_DATA_BYTES 8
#define FRAME_COUNT 4

typedef struct {
    uint16_t id;
    uint8_t dlc;
    uint8_t data[MAX_DATA_BYTES];
} CAN_Frame;

void print_frame(const CAN_Frame *frame) {
    printf("ID 0x%03X  DLC %d  Data:", frame->id, frame->dlc);
    for (int i = 0; i < frame->dlc; i++) {
        printf(" %02X", frame->data[i]);
    }
    printf("\n");
}

bool is_valid_frame(const CAN_Frame *frame) {
    return frame->dlc <= 8 && frame->id <= 0x7FF;
}

int main(void) {
    CAN_Frame frames[FRAME_COUNT] = {
        {0x100, 8, {0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77}},
        {0x7E8, 3, {0x62, 0xF1, 0x90}},
        {0x200, 0, {0}},
        {0x300, 9, {0x88, 0x99, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07}}
    };

    for (int i = 0; i < FRAME_COUNT; i++) {
        if (is_valid_frame(&frames[i])) {
            printf("valid    ");
            print_frame(&frames[i]);
        } else {
            printf("INVALID  ID 0x%03X  DLC %d  (data not printed)\n",
                   frames[i].id, frames[i].dlc);
        }
    }

    printf("sizeof(CAN_Frame) = %zu\n", sizeof(CAN_Frame));

    return 0;
}