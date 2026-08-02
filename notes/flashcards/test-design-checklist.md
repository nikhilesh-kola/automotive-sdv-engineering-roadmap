# Test Design Checklist

For every function I write, before I say "done", I check these four categories.
For each one I ask: "what is an example of this case for THIS function?"

## 1. Normal case (happy path)
- Typical valid input.
- Q: What is the most ordinary correct input, and what should it return?

## 2. Empty / zero case
- Nothing, or the smallest legal input.
- Q: What happens with an empty file, empty list, zero, or "" ?
- It should NOT crash — it should return an empty/neutral result.

## 3. Edge / boundary case
- The limits: just inside and just outside every rule.
- Q: If a rule is "must be 8", have I tested 7, 8, and 9?
- Off-by-one bugs hide here.

## 4. Error case
- Input that must be rejected.
- Q: What bad input should make this raise? Have I tested that it DOES raise?
- Use pytest.raises to prove the refusal.

---

## Applied to this week's CAN parser

| Category | Test I wrote | Did I cover it? |
|---|---|---|
| Normal | test_parse_valid_log (3 frames) | yes |
| Empty | test_empty_file_returns_no_frames | yes |
| Edge/boundary | (7 or 9 bytes) | NO — gap to fix |
| Error | test_invalid_payload_length_raises | yes |

## The one I missed
I never tested a payload that is off by ONE (7 or 9 bytes). I only tested
3 bytes (obviously wrong) and 8 bytes (correct). The boundary is where
off-by-one bugs live — exactly the 8-vs-7 mistake I made on Thursday.