"""Warm-up: see how the parser treats payloads near the 8-byte boundary."""

from can_parser import EXPECTED_PAYLOAD_BYTES

for byte_count in [7, 8, 9]:
    is_valid = (byte_count == EXPECTED_PAYLOAD_BYTES)
    verdict = "ACCEPTED" if is_valid else "rejected (should raise)"
    print(f"{byte_count} bytes -> {verdict}")