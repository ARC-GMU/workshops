---
description: "Navigate, create, edit, copy and delete files from the Ubuntu command line, and install software with apt."
---

# The Ubuntu command line

The terminal shows a **prompt** and waits for a command:

```text
alex@laptop:~$
```

That's `username@computer:current-folder$`. The `~` means your **home folder**, `/home/<username>`. In this workshop, a line starting with `$` is the prompt; don't type the `$` itself.

## Where am I, and what's here?

```bash
pwd        # print working directory: the folder you're in
ls         # list what's in it
ls -la     # list everything, including hidden files, with details
```

Files and folders whose names start with `.` (like `.gitignore`) are hidden. `ls -a` shows them.

## Moving around

```bash
cd Documents      # go into a folder
cd ..             # go up one folder
cd ~              # go home (plain `cd` does the same)
cd -              # go back to the previous folder
```

!!! tip "Two keys that save you hours"
    - ++tab++ completes file and folder names. Type `cd Doc` and press ++tab++.
    - ++arrow-up++ brings back your previous commands.

## Making and editing files

```bash
mkdir robot                 # make a folder
mkdir -p robot/src/drive    # make nested folders in one go
touch notes.txt             # make an empty file
nano notes.txt              # edit a file in the terminal
cat notes.txt               # print a file
less notes.txt              # scroll through a long file (press q to quit)
```

In **nano**, type normally, then press ++ctrl+o++ then ++enter++ to save and ++ctrl+x++ to exit. The shortcuts are listed at the bottom of the screen (`^` means ++ctrl++).

!!! tip "Prefer a graphical editor?"
    [VS Code](https://code.visualstudio.com/) can open folders inside WSL (the **WSL** extension) or Multipass (the **Remote - SSH** extension). From an Ubuntu terminal in WSL, `code .` opens the current folder.

## Copying, moving and deleting

```bash
cp notes.txt backup.txt         # copy a file
cp -r robot robot-old           # copy a folder (-r = recursive)
mv backup.txt old-notes.txt     # rename, or move
mv old-notes.txt robot/         # move into a folder
rm old-notes.txt                # delete a file
rm -r robot-old                 # delete a folder and everything in it
```

!!! danger "There's no recycle bin"
    `rm` deletes immediately and permanently. Double-check before you press ++enter++, especially with `rm -r`.

## Installing software

Ubuntu installs software with **apt**:

```bash
sudo apt update           # refresh the list of available packages
sudo apt install tree     # install a package
tree                      # show the current folder as a tree
```

## Getting help

```bash
ls --help       # quick summary of options
man ls          # the full manual (q to quit)
```

## Stopping things

- ++ctrl+c++ stops the running command.
- ++ctrl+l++ (or `clear`) clears the screen.

## Exercise

Build this layout in your home folder using only the terminal, then check it with `tree ~/practice`:

```text
practice/
├── notes.txt         ← contains one line about yourself
└── robot/
    ├── drive/
    └── sensors/
        └── lidar.txt
```

??? success "One way to do it"

    ```bash
    cd ~
    mkdir -p practice/robot/drive practice/robot/sensors
    cd practice
    nano notes.txt
    touch robot/sensors/lidar.txt
    tree ~/practice
    ```

When you're done, delete it with `rm -r ~/practice`.
