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

def test_seven_byte_payload_raises():
    """Boundary: one byte short must be rejected."""
    with pytest.raises(ValueError):
        parse_can_log(os.path.join(DATA_DIR, "can_log_seven_bytes.csv"))


def test_nine_byte_payload_raises():
    """Boundary: one byte over must be rejected."""
    with pytest.raises(ValueError):
        parse_can_log(os.path.join(DATA_DIR, "can_log_nine_bytes.csv"))

def test_error_message_reports_actual_byte_count():
    """The raised message must state the real byte count, not a hardcoded number."""
    with pytest.raises(ValueError) as exception_info:
        parse_can_log(os.path.join(DATA_DIR, "can_log_seven_bytes.csv"))
    message = str(exception_info.value)
    assert "7" in message          # it must report the ACTUAL count (7)
    assert "expected 8" in message  # and the expected count

def test_single_row_log_returns_one_frame():
    frames = parse_can_log(os.path.join(DATA_DIR, "can_log_valid_1_row.csv"))
    assert len(frames) == 1