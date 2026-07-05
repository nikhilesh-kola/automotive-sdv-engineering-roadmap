"""Week 3 - Monday - Exercise 1: Exceptions in diagnostic parsing."""


def parse_hex_byte(text):
    """Convert a hex string like '1A' into an integer. Return None if invalid."""
    try:
        return int(text, 16)
    except ValueError:
        print(f"Bad byte value: {text!r} is not valid hex")
        return None


def decode_frame(data):
    """A CAN classic frame must have exactly 8 data bytes."""
    if len(data) != 8:
        raise ValueError(f"CAN payload must be 8 bytes, got {len(data)}")
    return "Frame OK"


# --- Try the parser on good and bad input ---
print(parse_hex_byte("1A"))     # valid hex
print(parse_hex_byte("ZZ"))     # invalid -> caught, prints message, returns None

# --- Try the frame check ---
good_frame = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77]
short_frame = [0x00, 0x11, 0x22]

print(decode_frame(good_frame))

try:
    print(decode_frame(short_frame))
except ValueError as error:
    print(f"Rejected frame: {error}")