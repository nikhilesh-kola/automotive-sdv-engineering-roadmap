# Test Design Thinking — Week 3 Review

## Active Recall (answer in your head first, then check your week)
1. What are the four test categories?
2. Which category did my parser tests miss this week?
3. Why is pytest.raises the tool for the "error case" category?
4. What does a passing test actually prove — and what does it NOT prove?

## What I Understood Well
Got to know the structured 4 categories of the tests
## What Confused Me
Nothing, but the reason behind this 4 categories is to focus every project on what exactly to test rather than just test the happy path and thinking if there is anything to test, which is not efficient. Just definition of 4 test categories confused me.
## My Own Explanation
(In your own words: why does having a fixed four-category checklist make you a
better tester than just "writing some tests"? Write 3-4 sentences.)
A fixed four-category checklist is better because it turns an open-ended question ("what should I test?") into a specific, answerable one ("what's the normal, empty, boundary, and error case for this function?"). Without it, I default to testing only the happy path and skip the cases I don't happen to think of — like the boundary case I missed this week. The checklist guarantees I at least consider every category, so gaps become a deliberate choice rather than an accident.