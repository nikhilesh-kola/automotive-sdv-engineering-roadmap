# Changelog — CAN Log Parser

## [Fixed] Payload length check and error message drifted apart

**Symptom:** After changing the length rule from 8 to 7, the valid-log test
failed with a confusing message: "payload has 8 bytes, expected 8" — the
numbers looked equal, yet it still raised.

**Root cause:** The number 8 was written in two separate places — the `if`
condition and the error message text. When the condition was changed, the
hardcoded 8 in the message was not, so the message no longer described the
actual rule. The check said "!= 7"; the message still said "expected 8".

**Fix:** Introduced a single constant `EXPECTED_PAYLOAD_BYTES = 8`. Both the
`if` condition and the error message now read from it, so they can never
disagree again.

**Lesson:** A fact should live in one place. An error message must read its
values from the same source the logic uses, never repeat a hardcoded copy.