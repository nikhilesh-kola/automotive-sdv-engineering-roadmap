"""Week 3 debug task — this code has bugs. Find and fix them."""

import logging

logging.basicConfig(level=logging.INFO)


def count_valid_frames(payloads):
    """Count how many payloads have exactly 8 bytes."""
    valid_count = 0
    for payload in payloads:
        if len(payload) == 8:
            valid_count = valid_count + 1
            logging.info("Valid frame found")
    return valid_count

test_payloads = [
    [0, 1, 2, 3, 4, 5, 6, 7],   # 8 bytes - valid
    [0, 1, 2],                   # 3 bytes - invalid
    [0, 1, 2, 3, 4, 5, 6, 7],   # 8 bytes - valid
]

result = count_valid_frames(test_payloads)
print(f"Valid frames: {result}")