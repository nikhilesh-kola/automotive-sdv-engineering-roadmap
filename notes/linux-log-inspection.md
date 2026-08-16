# Inspecting Logs with grep, cut, sort, uniq, wc — Week 4 Thursday

## Today's Task
Analyze a CAN log using only shell tools (no Python): count lines, extract
the CAN ID column, find unique IDs, and rank them by frequency.

## The Core Pipeline
    grep -v "can_id" can_log.csv | cut -d',' -f2 | sort | uniq -c | sort -rn

## What Each Tool Does
- wc -l          count lines ("how big is this?")
- grep PATTERN   show lines that match
- grep -v PATTERN  show lines that do NOT match (used to drop the header)
- cut -d',' -f2  extract field 2, comma-delimited (one column)
- sort           group identical lines together (REQUIRED before uniq)
- uniq -c        collapse adjacent duplicates and count each group
- sort -rn       sort reverse (-r) numeric (-n): biggest count first

## The Pipe |
The pipe sends the OUTPUT of one command as the INPUT of the next.
Small tools, each doing one job, chained into something powerful.

## Memory-Level Understanding
cut -f2   -> stream of CAN IDs
| sort    -> identical IDs now adjacent
| uniq -c -> "5 0x100", "3 0x200", ... (counts)
| sort -rn -> ranked, busiest ID first

## Automotive Relevance
On a remote Linux ECU/test box where I can't run a script, this pipeline
triages a CAN trace instantly: which ID dominates the bus, how many frames,
which IDs are rare. The tool's count beats any eyeball estimate - I counted
0x100 as 4 by eye; the pipeline correctly found 5.

## Bash vs PowerShell notes
- Paths use forward slashes; C: drive is /c/Users/...
- Pipe | : Shift+\ (US layout) or AltGr+< (German layout)

## What I Understood Well
- understood and practised all the mentioned linux commands
- Also got to know the logic behind every command, to use them efficiently

## What Confused Me
- for wc command the "-l" looks like -1, I thought it is minus 1, but it is actually minus letter l
- also the pipe character, i did not know which key on windows laptop does that, finally learned it is with shift + \

## Next Improvement
Learn awk, which can filter AND compute in one tool.
