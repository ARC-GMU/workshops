---
description: "Quick reference for Ubuntu, Git and GitHub CLI commands."
---

# Cheat sheet

## Ubuntu command line

| Command | What it does |
|---|---|
| `pwd` | Show the current folder |
| `ls -la` | List files, including hidden ones |
| `cd <folder>` / `cd ..` / `cd ~` | Go into a folder / up one / home |
| `mkdir -p <path>` | Make folders |
| `nano <file>` | Edit a file (++ctrl+o++ save, ++ctrl+x++ exit) |
| `cat <file>` / `less <file>` | Print / scroll through a file |
| `cp <src> <dest>` / `cp -r` | Copy a file / folder |
| `mv <src> <dest>` | Move or rename |
| `rm <file>` / `rm -r <folder>` | Delete, permanently |
| `sudo apt install <pkg>` | Install software |
| ++tab++ / ++arrow-up++ / ++ctrl+c++ | Complete / previous command / stop |

## Git: daily use

| Command | What it does |
|---|---|
| `git status` | What's changed and what's staged |
| `git diff` | Show unstaged changes line by line |
| `git add <file>` / `git add .` | Stage a file / everything |
| `git commit -m "msg"` | Commit staged changes |
| `git log --oneline` | Short history |
| `git pull` | Get new commits from GitHub |
| `git push` | Send your commits to GitHub |

## Git: branches

| Command | What it does |
|---|---|
| `git branch` | List branches |
| `git switch -c <name>` | Create a branch and switch to it |
| `git switch <name>` | Switch branches |
| `git merge <name>` | Merge a branch into the current one |
| `git branch -d <name>` | Delete a merged branch |
| `git push -u origin <name>` | Push a new branch to GitHub |

## Git: setup and remotes

| Command | What it does |
|---|---|
| `git init` | Start a repo in this folder |
| `git clone <url>` | Download a repo |
| `git remote -v` | Show where `origin` (and `upstream`) point |
| `git restore <file>` | Discard unstaged edits to a file |
| `git restore --staged <file>` | Unstage a file |

## GitHub CLI

| Command | What it does |
|---|---|
| `gh auth login` | Log in to GitHub |
| `gh repo create <name> --public --source=. --push` | Create a GitHub repo from this folder |
| `gh repo fork <owner>/<repo> --clone` | Fork and clone |
| `gh pr create` | Open a pull request for this branch |

## Merge conflict markers

```text
<<<<<<< HEAD
your version
=======
their version
>>>>>>> abc1234
```

Edit to the correct text, delete the markers, then `git add <file>` and `git commit`.
