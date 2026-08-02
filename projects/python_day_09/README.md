# Week 3 — CAN Log Parser with pytest

## Goal
A small CAN log parser that reads a CSV of frames and validates payload
length, backed by a pytest suite covering every test-design category.

## Files
- `can_parser.py` — the parser: reads CSV rows, validates 8-byte payloads,
  raises ValueError on bad length. Also `is_known_can_id`.
- `test_can_parser.py` — 10 pytest tests (see coverage below).
- `data/` — CSV fixtures: valid, empty, 1-row, bad payload, 7-byte, 9-byte.
- `CHANGELOG.md` — record of the payload-length / message-drift fix.

## How to Run
    py -m pytest projects/python_day_09/test_can_parser.py -v

Expected: 10 passed.

## Test Coverage (by category)
| Category        | Test |
|-----------------|------|
| Normal          | test_parse_valid_log (3 frames) |
| Normal (minimum)| test_parse_valid_log_1_row |
| Empty           | test_empty_file_returns_no_frames |
| Edge / boundary | test_seven_byte_payload_raises, test_nine_byte_payload_raises |
| Error (raises)  | test_invalid_payload_length_raises |
| Error (message) | test_error_message_reports_actual_byte_count |
| CAN ID lookup   | known, unknown, 0x400 |

## Concepts Practiced
Exceptions, raise, assert, pytest, pytest.raises, inspecting the exception
message, boundary testing, single-source-of-truth constants.

## Automotive Relevance
A diagnostic engineer receives large CAN traces that are often malformed. A
parser that silently accepts a bad frame reports wrong data downstream. This
suite guards the parser so a future change can't make it go soft on bad input
without a test turning red — the foundation of diagnostic test automation.