# Week 3 Test — Python Quality: Testing, Logging, Debugging

## Part 1 — Theory Questions
1. What is the difference between an EXCEPTION and an ASSERT?
   Give one automotive example of when you'd use each.
   EXCEPTION is python's way of saying it cannot continue.
   Example: value = int("can ID count", 16)
   Assert - checks a condition, that we believe to be true
   assert len(frames) == 1

2. Why is `except Exception:` (catch-everything) dangerous in a diagnostic tool?
It is dangerous in a diagnostic tool because it catches everything and stops the parsing, which has a huge data to parse.

3. Name the five logging levels in order, least to most severe.
DEBUG
INFO
WARNING
ERROR
CRITICAL

4. What does pytest.raises(ValueError) do, and why does a raised error make the test PASS instead of fail?
It raises the error, whenever it finds it. Raised error make the test PASS instead of fail because it raised correctly that there is a value error and it caught the error correctly, so the test is passed in the catching the error.

5. This week a passing test (the length-check test) stayed green even though the parser was broken. In one sentence: what does this tell you about what a passing test actually proves?
This proves that the test passes when it correctly catches the error. It does not mean, that when a test is passed it is always positive.
## Part 2 — Coding Task
Completed the task with some help, added an additional test to confirm my learning.

## Part 3 — Debugging Task
The first but is syntax error, found it after running the code in error description. It has only 1 = instead of ==.
The second bug is about the valid frames found, but it prints the incorrect valid frames number. This is because of the wrong calculation of valid frames. It directly has (valid_count + 1). It should have valid_count = valid_count + 1.

## Part 4 — Written Explanation
Why does test automation matter in automotive software? Connect it to real diagnostics — malformed CAN frames, regressions, and why an engineer can't just "eyeball" a 50,000-line trace.
The test automation is very important in Automotive software, because each ECU sends hundreds or thousands of CAN frames within each second or minute. And a car has around 100 ECUs, so the data we get is really huge and an enginner cannot check manually each CAN row.

## Part 5 — Self-Score
I felt it difficult for the coding task, 65/100

## Part 6 — Reflection
It was really good week for me. Learned alot on testing and de-bugging. Need to improve on wrting the code without any help.


Corrected sections and evaluation
Part 1 — Theory quiz (25 points)

Q1 — Exception vs assert (partial). You gave correct examples but didn't state the difference, which is what the question asked. You defined what an exception is, but never said what distinguishes it from an assert. The key distinction you missed: exceptions handle expected bad input (a malformed log line — normal operation), while asserts catch your own logic errors (a decoded speed of 500 km/h — something that should be impossible). Also, your assert example assert len(frames) == 1 is a test assert; a better in-code example is assert 0 <= speed <= 300. 3/5

Q2 — catch-everything danger (partial, and the reason given is wrong). You said it's dangerous because "it stops the parsing." That's backwards — the real danger is the opposite: except Exception: hides bugs by swallowing errors that should surface, so a broken decoder silently reports wrong values instead of crashing. It doesn't stop too much; it stops too little from being noticed. 2/5

Q3 — logging levels. Perfect. All five, correct order. 5/5

Q4 — pytest.raises (partial, wording muddled). You've got the intuition — "it caught the error correctly so the test passes" — but the wording is circular and slightly wrong. pytest.raises(ValueError) doesn't raise the error; it expects and catches one. The test passes because the error you wanted to happen did happen. Cleaner: "It sets a trap expecting a ValueError. If the code raises one, the trap catches it and the test passes; if no error is raised, the test fails." 3/5

Q5 — what a passing test proves. Good. Your second sentence is exactly right: "a passing test does not always mean positive." The precise version: a passing test only proves the specific thing it checks still holds — not that the code is correct overall. You got the core idea. 4/5

Part 1 total: 17/25

Part 2 — Coding task (35 points)

I have to score this fairly: you got stuck and I walked you through the function and the test structure. You did write the sixth test independently and it was correct, and you ran everything to green. But the core function and four tests were guided, so I can't award full marks as if it were solo work — that would make the grade a lie, and you'd rather know the truth.

What you demonstrated on your own: running the suite, reading the pass output, and writing a correct additional boundary/normal test. What you needed help with: structuring the function (validate-then-compute) and not grafting the CSV template on. 20/35

Part 3 — Debugging task (20 points)

Both bugs found, both correct. The syntax error (= vs ==) — found by running and reading the error, exactly the right method. The silent bug (valid_count + 1 computes then throws away the result, instead of valid_count = valid_count + 1) — this is the harder one and you nailed both the what and the why.

One thing you skipped: the question asked which bug was more dangerous and why. The answer — the silent one, because the syntax error stops the program loudly (you can't miss it), while the silent bug lets the program run and produce a wrong count that looks fine. In diagnostics, a wrong-but-plausible number is far more dangerous than a crash. Add that and it'd be full marks. 16/20

Part 4 — Written explanation (part of 20)

Good core point — the scale argument (100 ECUs, thousands of frames/second, impossible to eyeball) is exactly right and well put. But it's ~60 words, not 200, and it only covers the volume angle. You didn't touch regressions (a change silently breaking something that worked — the thing you literally experienced Thursday) or malformed frames (why a parser must reject bad data reliably). Those were named in the prompt. The idea is sound; it's incomplete. 11/20 for documentation+reflection combined (see below).

Part 6 reflection is honest and self-aware — "need to improve writing code without help" is precisely the right thing to notice, and naming it is how you fix it. That candour earns its share of the documentation points.

Final score
text
Part 1 — Theory quiz          17 / 25
Part 2 — Coding task          20 / 35
Part 3 — Debugging            16 / 20
Part 4/6 — Docs + reflection  11 / 20
                              ---------
TOTAL                         64 / 100