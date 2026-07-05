"""Week 3 - Monday - Exercise 2: assert for catching logic errors."""


def scale_speed(raw):
    """Convert a raw CAN value into km/h using a 0.01 scale factor."""
    speed = raw * 0.01
    assert 0 <= speed <= 300, f"Speed out of range: {speed} km/h"
    return speed


print(scale_speed(2500))    # normal: 25.0 km/h
print(scale_speed(50000))   # impossible: SHOULD crash on purpose