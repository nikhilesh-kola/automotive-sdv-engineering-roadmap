# pytest for a CAN Log Parser — Week 3 Wednesday

## Today's Task
Write automated pytest tests for a CAN log parser: valid log, empty file,
invalid payload length, and known/unknown CAN IDs.

## Key Concepts
- pytest finds functions named test_* in files named test_*.
- A test = known input checked against an expected output via assert.
- pytest.raises(ValueError) EXPECTS an error; the error is the success.
- The parser holds the rule (if len != 8: raise); the test proves the rule fires.
- Save before running — pytest reads the file from disk, not the editor.

## Code Pattern
    with pytest.raises(ValueError):
        parse_can_log(bad_file)   # passes only if a ValueError is raised

## Memory-Level Understanding
test calls parser -> parser hits bad payload -> if 3 != 8 True -> raise
-> ValueError travels up -> pytest.raises catches it -> test PASSES.
raise = end the function loudly; return = end it quietly.

## Automotive Relevance
A diagnostic parser that silently accepts a malformed frame reports wrong
data downstream. Tests guard the parser so a future change cannot make it
go soft on bad input without a test turning red.

## What I Understood Well
- Why pytest.raises treats the error as a pass.
- The parser-holds-rule / test-proves-rule separation.

## What Confused Me
The test file actually runs the functions from the original parser file and checks if the error is correctly raised or not. I thought this pytest file is independent of the parser code file.
Pytest file has simple code to check if the error is raised correctly or not.

## Next Improvement
Break the parser on purpose next time and watch a test go from PASS to FAIL.