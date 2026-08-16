# Linux Command Cheat Sheet for Diagnostic Logs — Week 4

Organized by TASK, because under pressure you think "what do I need to do?",
not "what's the alphabetical command?".

## 1. Where am I / what's here (navigation)
| Command | What it does |
|---------|--------------|
| `pwd` | Prints the working directory I am currently in |
| `ls` | Lists the files and folders inside the current directory |
| `ls -l` | Long listing: permissions, size, date |
| `cd folder` | Moves into the named folder |
| `cd ..` | Go up one level |
| `cd` (bash, alone) | Jump to home folder |

## 2. Looking at file contents
| Command | What it does |
|---------|--------------|
| `cat file` | Dumps the whole file to the screen |
| `less file` | Page through a file (q to quit) — better for big logs |
| `head file` | First 10 lines (great for checking a log's format) |
| `tail file` | Last 10 lines |
| `tail -f file` | Follow a file LIVE as it grows (watching a log in real time) |

## 3. Searching inside files
| Command | What it does |
|---------|--------------|
| `grep "0x100" log` | Prints every line in the file that contains the pattern |
| `grep -v "header" log` | -v inverts the match: prints lines that do NOT contain the pattern |
| `grep -c "0x100" log` | Count matching lines directly |
| `grep -i "error" log` | Case-insensitive match |

## 4. Extracting and counting (the pipeline tools)
| Command | What it does |
|---------|--------------|
| `cut -d',' -f2 log` | -d sets the delimiter (here a comma), -f2 selects field/column 2 |
| `sort` | Orders lines alphabetically/numerically, which puts identical lines next to each other |
| `uniq -c` | Collapses ADJACENT duplicate lines and counts each group. Needs `sort` first, because it only catches duplicates that are already next to each other |
| `sort -rn` | -r reverse (biggest first), -n numeric (treat as numbers, not text) |
| `wc -l file` | Counts the number of lines in the file |

## 5. Files and folders
| Command | What it does |
|---------|--------------|
| `mkdir name` | Make a folder (`mkdir -p a/b` makes nested) |
| `cp a b` | Copies a to b — the original STAYS |
| `mv a b` | Move or rename — the original GOES |
| `rm file` | Removes the file. Danger: permanent, no recycle bin, cannot undo |
| `rm -r folder` | Remove a folder and everything in it |

## 6. Environment & Python (from Wed/Tue)
| Command | What it does |
|---------|--------------|
| `echo $PATH` | Show the PATH (bash) / `$env:PATH` (PowerShell) |
| `python -m venv .venv` | Create a virtual environment |
| `source .venv/Scripts/activate` | Activate venv (bash) |
| `deactivate` | Leave the venv |

## THE ONE TO MEMORIZE — the diagnostic power move
    grep -v "header" log.csv | cut -d',' -f2 | sort | uniq -c | sort -rn
Ranks every value in a column by frequency. "Which CAN ID dominates the bus?"
answered in one line.

## Bash gotchas (from this week)
- Paths: forward slashes; C: drive is /c/Users/...
- Pipe | : Shift+\ (US) or AltGr+< (German)
- "File not found" usually means WRONG FOLDER — run pwd first.
- Commit from the REPO ROOT so `git add .` catches everything.