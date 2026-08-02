# CAN Parser Test Suite v1 — Week 3 Saturday

## Today's Task
Grow the parser suite to 10 meaningful tests, one per checklist category,
including boundary cases and an error-message-content test.

## Key Concepts
- "Meaningful" = each test guards a different category, not more happy paths.
- Boundary tests (7 and 9 bytes) catch off-by-one — the most common byte bug.
- pytest.raises(...) as info lets you inspect the exception message, not just
  confirm it happened.
- Correct test data is a skill: a boundary fixture with the wrong byte count
  proves nothing.

## Memory-Level Understanding
pytest.raises(ValueError) as exception_info
  -> exception_info.value = the ValueError object
  -> str(exception_info.value) = its message text
  -> assert "7" in message checks the message reports the ACTUAL count.

## Automotive Relevance
Testing the message CONTENT (not just that an error occurred) matters because
diagnostics is about producing correct, trustworthy fault information. A wrong
message sends an engineer chasing a phantom.

## What I Understood Well
Understood all the test categories to test and write relevant tests for each category
Understood how to Inspect exception messages content if it raises the error message correctly.

## What Confused Me
Nothing confused but a lot of information to remember and process it accordingly.

## Next Improvement
Consider testing that valid frames preserve their can_id and timestamp values,
not just that the right NUMBER of frames comes back.