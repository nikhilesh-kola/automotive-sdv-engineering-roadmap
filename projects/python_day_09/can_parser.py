"""A small CAN log parser to be tested with pytest."""

import csv

KNOWN_CAN_IDS = {"0x100", "0x200", "0x300", "0x400"}


def parse_can_log(path):
    """Read a CAN log CSV and return a list of frame dictionaries.

    Raises ValueError if any payload does not have exactly 8 bytes.
    """
    frames = []
    with open(path, newline="") as file_handle:
        reader = csv.DictReader(file_handle)
        for line_number, row in enumerate(reader, start=1):
            payload_bytes = row["payload"].split()
            if len(payload_bytes) != 8:
                raise ValueError(
                    f"Line {line_number}: payload has {len(payload_bytes)} bytes, expected 8"
                )
            frames.append(row)
    return frames


def is_known_can_id(can_id):
    """Return True if the CAN ID is one we recognise."""
    return can_id in KNOWN_CAN_IDS