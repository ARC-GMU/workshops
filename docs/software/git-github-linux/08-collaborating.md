---
description: "Share a repository with a teammate, and cause and resolve a merge conflict."
---

# Working together & merge conflicts

**Do this lesson in pairs.** One person is the **owner**, the other the **collaborator**.

## 1. Share a repo

**Owner:** on your `my-robot` repo on GitHub, go to **Settings** → **Collaborators** → **Add people**, and add your partner's GitHub username.

**Collaborator:** accept the invite (check your email or <https://github.com/notifications>), then clone the owner's repo:

```bash
cd ~
git clone https://github.com/<owner-username>/my-robot.git partner-robot
cd partner-robot
```

## 2. Take turns

Each of you, one at a time:

1. `git pull`
2. Make a branch, change a file, commit and push.
3. Open a PR. The **other person** reviews and merges it.

Changes to *different files*, or different parts of a file, merge without any trouble.

## 3. Make a conflict on purpose

A **merge conflict** happens when two people change the **same line** differently. Git can't guess which version is right, so it asks you.

1. Both of you: `git switch main && git pull`.
2. Both of you: edit the **first line** of `README.md` to say something different, then commit.

    ```bash
    nano README.md
    git commit -am "Change title"
    ```

3. **Owner:** `git push`. It works.
4. **Collaborator:** `git push`. It's **rejected**:

    ```text
    ! [rejected]        main -> main (fetch first)
    hint: Updates were rejected because the remote contains work that you do not have locally.
    ```

    GitHub has a commit you don't have yet. Pull it:

    ```bash
    git pull
    ```

    ```text
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```

## 4. Resolve the conflict

Open the file:

```bash
nano README.md
```

Git has marked the conflict:

```text
<<<<<<< HEAD
# Collaborator's Robot
=======
# Owner's Robot
>>>>>>> 4c1d2e9...
```

- Between `<<<<<<< HEAD` and `=======` is **your** version.
- Between `=======` and `>>>>>>>` is the version **from GitHub**.

Edit the file so it says what it *should* say: one version, the other, or a mix. **Delete all three marker lines.** For example:

```text
# Our Robot
```

Then tell Git it's resolved, and finish the merge:

```bash
git add README.md
git commit -m "Merge title changes"
git push
```

**Owner:** `git pull` to get the result.

!!! tip "Avoiding conflicts"
    - `git pull` before you start, and push often.
    - Keep branches small and short-lived.
    - Talk to each other: "I'm editing the motor code" saves a lot of trouble.
    - Conflicts are normal and not a sign anyone did something wrong.

## 5. Swap roles

Swap owner and collaborator and do the conflict again, so you've both resolved one.
