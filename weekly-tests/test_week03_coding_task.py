"""Tests for decode_temperature, covering the four checklist categories."""

import pytest

from week03_coding_task import decode_temperature


def test_normal_value():
    # Normal: a typical mid-range byte.
    assert decode_temperature(90) == 50


def test_lower_boundary():
    # Boundary: 0 is the lowest VALID value -> -40 C.
    assert decode_temperature(0) == -40


def test_upper_boundary():
    # Boundary: 255 is the highest VALID value -> 215 C.
    assert decode_temperature(255) == 215


def test_below_range_raises():
    # Error: -1 is just outside the low end -> must raise.
    with pytest.raises(ValueError):
        decode_temperature(-1)


def test_above_range_raises():
    # Error: 256 is just outside the high end -> must raise.
    with pytest.raises(ValueError):
        decode_temperature(256)

def test_normal_value_2():
    # Normal: a typical mid-range byte.
    assert decode_temperature(40) == 0