---
description: "Put a local Git repository on GitHub, then clone, push and pull."
---

# Pushing to GitHub

Your repo exists only on your laptop. Now you'll put it on GitHub.

## Create an empty repo on GitHub

1. Go to <https://github.com/new>.
2. **Repository name:** `my-robot`.
3. Leave **Add a README**, **.gitignore** and **license** turned **off**. Your local repo already has a history, and GitHub's repo must start empty.
4. Click **Create repository**.

## Connect and push

GitHub shows you the commands. From inside `~/my-robot`:

```bash
git remote add origin https://github.com/<your-username>/my-robot.git
git push -u origin main
```

- `git remote add origin <url>` tells your repo where its GitHub copy lives. `origin` is the standard name for it.
- `git push -u origin main` uploads your `main` branch. The `-u` remembers the connection, so afterwards plain `git push` is enough.

Refresh the GitHub page: your files and commit history are there.

!!! tip "The shortcut"
    `gh` can create the GitHub repo and push in one step:

    ```bash
    gh repo create my-robot --public --source=. --push
    ```

## The everyday loop

From now on, after you commit, push:

```bash
git add .
git commit -m "Describe the change"
git push
```

## Getting a repo onto another computer: clone

To download a repo from GitHub, **clone** it. Try it with your own repo in a different folder:

```bash
cd ~
git clone https://github.com/<your-username>/my-robot.git my-robot-copy
cd my-robot-copy
git log --oneline
```

The clone has the full history and is already connected to `origin`.

## Getting new changes: pull

Change something on GitHub's website: open `README.md`, click the pencil icon, edit, and **Commit changes**. Then back in your original folder:

```bash
cd ~/my-robot
git pull
```

`git pull` downloads new commits from GitHub and merges them into your branch.

!!! tip "Pull before you start working"
    Make `git pull` the first thing you do when you sit down to work on a shared repo.

Clean up the copy when you're done:

```bash
rm -rf ~/my-robot-copy
```
