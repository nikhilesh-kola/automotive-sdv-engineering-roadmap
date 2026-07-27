# Breaking and Fixing the Parser — Week 3 Thursday

## Today's Task
Intentionally break the parser, read the pytest failure, fix it, and record
the episode in a CHANGELOG.

## Key Concepts
- Establish a green baseline before changing anything.
- Predict what a change will do, then check reality against the prediction.
- Read the pytest failure block: which test, the >  line, the E: error line, the source location.
- A passing test only proves the specific thing it checks — not overall correctness.
- A fact should have one home; error messages must read from the same source as the logic.

## Memory-Level Understanding
if len != 7 with 8-byte data -> raise on the FIRST valid row -> valid-log test fails.
The length-check test still passed because 3 != 7 is still True -> it only asks
"did it refuse?", not "did it refuse for the right reason?".
Message said "expected 8" (hardcoded) while the rule checked 7 -> code and message lied to each other.

## Automotive Relevance
In a real diagnostic log, a wrong error message sends an engineer chasing a
phantom fault. The message is the diagnosis; a wrong diagnosis wastes more
time than no message. Keeping the rule and its message in one source prevents this.

## What I Understood Well
How to test the code by wantedly making the tests fail. 

## What Confused Me
Need to also focus on the error messages when wanting to test. For testing I changed the length of expected payload to 7 but forgot to update this number in the error message.

## Next Improvement
Add a test that checks the ERROR MESSAGE text, not just that an error was raised.