"""Week 3 - Monday - Exercise 3: a manual test, the idea behind pytest."""


def scale_speed(raw):
    return raw * 0.01


def test_scale_speed():
    expected = 25.0
    actual = scale_speed(2500)
    if actual == expected:
        print("PASS: scale_speed(2500) == 25.0")
    else:
        print(f"FAIL: expected {expected}, got {actual}")


test_scale_speed()