"""Week 3 coding task: decode a raw CAN temperature byte into Celsius."""


def decode_temperature(raw_byte):
    """Convert a raw temperature byte (0-255) into degrees Celsius.

    Formula: celsius = raw_byte - 40  (raw 0 = -40 C, raw 40 = 0 C).
    Raises ValueError if raw_byte is outside the valid 0-255 range.
    """
    if not (0 <= raw_byte <= 255):
        raise ValueError(
            f"raw_byte must be 0-255, got {raw_byte}"
        )
    celsius = raw_byte - 40
    return celsius