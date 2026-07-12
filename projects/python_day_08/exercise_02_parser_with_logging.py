"""Week 3 - Tuesday - Exercise 2: add logging to a CAN frame parser."""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s | %(message)s",
)


def parse_frame(line_number, payload):
    """Validate a CAN payload. Log what happens; return the payload or None."""
    logging.debug(f"Line {line_number}: checking payload {payload}")

    if len(payload) != 8:
        logging.warning(
            f"Line {line_number}: payload has {len(payload)} bytes, expected 8 - skipping"
        )
        return None

    logging.info(f"Line {line_number}: valid frame accepted")
    return payload


# Synthetic log: some good frames, one broken one.
lines = [
    [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77],  # good
    [0x01, 0x02, 0x03],                                 # too short
    [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, 0x00, 0x11],  # good
]

accepted = []
for number, payload in enumerate(lines, start=1):
    result = parse_frame(number, payload)
    if result is not None:
        accepted.append(result)

logging.info(f"Done. Accepted {len(accepted)} of {len(lines)} frames.")