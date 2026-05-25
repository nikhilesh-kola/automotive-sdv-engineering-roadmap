# Git Basics — 19.05.2026

## What is Git?

Git is software on my local computer that tracks file changes over time.

## What is GitHub?

GitHub is a website where Git repositories can be stored online, shared, and used as a portfolio.

## Git vs GitHub

| Git | GitHub |
|---|---|
| Local version control tool | Online hosting platform |
| Tracks changes | Stores repositories online |
| Works on my laptop | Works through browser/cloud |
| Uses commands like status, add, commit | Shows repos, commits, branches, README files |

## What is a repository?

A repository is a project folder that Git is tracking.

## Important Git Commands

### git init

Creates a new Git repository in a folder.

### git status

Shows changed, modified, staged, or untracked files.

### git add .

Prepares all current changes for the next commit.

### git commit -m "message"

Creates a saved snapshot of staged changes with a message describing what changed.

### git log --oneline

Shows commit history in a short one-line format.

### git branch

Shows available branches. The current branch is marked with `*`.

## My Git Workflow

```bash
git status
git add .
git commit -m "Clear message"
git push origin main