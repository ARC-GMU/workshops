---
description: "Get an Ubuntu terminal on Windows (WSL), macOS (Multipass) or Ubuntu, install Git and log in to GitHub."
---

# Install & set up

By the end of this lesson you'll have an Ubuntu terminal with Git installed and connected to your GitHub account.

!!! tip "Do this before the workshop"
    Installing Ubuntu can take 20–30 minutes and, on Windows, a restart.

## 1. Get an Ubuntu terminal

!!! note "TODO: pick the club's Ubuntu version"
    These steps install the current Ubuntu LTS. Use the same version as the ROS 2 workshop so people only install it once.

=== "Windows"

    Use **WSL** (Windows Subsystem for Linux), which runs Ubuntu inside Windows.

    1. Right-click **Start** → **Terminal (Admin)** or **PowerShell (Admin)**.
    2. Run:

        ```powershell
        wsl --install
        ```

        This installs WSL with Ubuntu.

    3. Restart your computer when asked.
    4. Open **Ubuntu** from the Start menu. The first launch asks you to create a Linux username and password. The password doesn't show while you type; that's normal.

=== "macOS"

    Use **Multipass**, which runs a lightweight Ubuntu virtual machine.

    1. Download and install [Multipass](https://canonical.com/multipass/install).
    2. Open **Terminal** and run:

        ```bash
        multipass launch --name ubuntu
        multipass shell ubuntu
        ```

    3. Your prompt changes to `ubuntu@ubuntu:~$`. You're now inside Ubuntu. Next time, open Terminal and run `multipass shell ubuntu` to get back.

=== "Ubuntu"

    You're all set. Open **Terminal** with ++ctrl+alt+t++.

From here on, **every command goes in your Ubuntu terminal**.

## 2. Install Git and the GitHub CLI

```bash
sudo apt update
sudo apt install -y git gh
```

`sudo` runs a command as administrator, so it asks for your Ubuntu password. `gh` is the GitHub command-line tool, which handles logging in to GitHub.

Check that both installed:

```bash
git --version
gh --version
```

## 3. Tell Git who you are

Every commit is labelled with a name and email. Use the email address on your GitHub account.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Set a few sensible defaults:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor nano
```

| Setting | What it does |
|---|---|
| `init.defaultBranch main` | New repos start on a branch called `main`, matching GitHub |
| `pull.rebase false` | `git pull` merges changes in (we'll cover this in lesson 8) |
| `core.editor nano` | Git opens the simple `nano` editor when it needs you to type a message |

## 4. Log in to GitHub

```bash
gh auth login
```

Answer the prompts:

1. **Where do you use GitHub?** → `GitHub.com`
2. **Preferred protocol?** → `HTTPS`
3. **Authenticate Git with your GitHub credentials?** → `Yes`
4. **How would you like to authenticate?** → `Login with a web browser`

Copy the one-time code it shows, press ++enter++, and paste the code into the browser page. On WSL or Multipass the browser may not open by itself; go to <https://github.com/login/device> yourself.

Check that it worked:

```bash
gh auth status
```

!!! info "Why not just use my GitHub password?"
    GitHub doesn't accept account passwords for `git push`. `gh auth login` sets up a secure token for Git so you never have to deal with one.

## Checklist

- [ ] `git --version` prints a version
- [ ] `git config --global user.email` prints your GitHub email
- [ ] `gh auth status` says you're logged in
