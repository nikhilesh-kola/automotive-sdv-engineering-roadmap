"""Week 3 - Wednesday - pytest tests for the CAN log parser."""

import os

import pytest

from can_parser import parse_can_log, is_known_can_id

# Build the path to the data folder relative to THIS test file,
# so the tests work no matter which folder you run pytest from.
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def test_parse_valid_log():
    frames = parse_can_log(os.path.join(DATA_DIR, "can_log_valid.csv"))
    assert len(frames) == 3


def test_empty_file_returns_no_frames():
    frames = parse_can_log(os.path.join(DATA_DIR, "can_log_empty.csv"))
    assert frames == []


def test_invalid_payload_length_raises():
    with pytest.raises(ValueError):
        parse_can_log(os.path.join(DATA_DIR, "can_log_bad_payload.csv"))


def test_known_can_id():
    assert is_known_can_id("0x100") is True


def test_unknown_can_id():
    assert is_known_can_id("0x999") is False

def test_known_can_id_0x400():
    assert is_known_can_id("0x400") is True