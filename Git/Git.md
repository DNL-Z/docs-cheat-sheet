# ⛓️ GIT

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Git is lightning fast and has a huge ecosystem of GUIs, hosting services, and command-line tools.

## 📑 Table of Contents
- [📥 Installation](#installation)
- [⚙️ Configuration](#configuration)
- [🔑 SSH Keys](#ssh-keys)
- [🌐 Remote Repository](#remote-repository)
- [📝 Basic Commands](#basic-commands)
- [🌿 Branches](#branches)
- [📦 Staging and Committing](#staging-and-committing)
- [💾 Stash](#stash)
- [👁️ Viewing Changes](#viewing-changes)
- [🔧 Advanced Operations](#advanced-operations)

---

## 📥 Installation

### macOS

```bash
  brew install git
```

### Linux (Ubuntu/Debian)

```bash
  sudo apt update
  sudo apt install git
```

### Linux (Fedora)

```bash
  sudo dnf install git
```

### Windows

Download from [git-scm.com](https://git-scm.com/download/win) or use:

```bash
  winget install --id Git.Git -e --source winget
```

### Verify installation

```bash
  git --version
```

---

## ⚙️ Configuration

### Configuration file

**.gitconfig**

```ini
[user]
    name = Your Name
    email = your.email@example.com

[core]
    autocrlf = input

[pull]
    ff = only
    rebase = true
```

### Use different email for a specific directory

Add this to your main **~/.gitconfig** file:

```ini
[includeIf "gitdir:~/Specific-Folder/Dev/"]
    path = ~/.gitconfig-specific-folder
```

Then create a **~/.gitconfig-specific-folder** file with:

```ini
[user]
    email = your.work@email.com
```

---

## 🔑 SSH Keys

### Generate SSH keys (id_rsa and id_rsa.pub) in the ~/.ssh directory

```bash
  ssh-keygen -t rsa
```

The public key **~/.ssh/id_rsa.pub** must be registered on your **Git** account.

---

## 🌐 Remote Repository

### Check if the project is connected to a remote (like GitHub)

```bash
  git remote -v
```

### Clone a repository locally

```bash
  git clone <SSH_or_HTTPS_address>
```

### Set up GitHub Token

```bash
  git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git
```

### Push a local project to a repository

```bash
  git init --initial-branch=main
```

```bash
  git remote add origin <ssh_url_repository_project>
  git add .
  git commit -m "Initial commit"
  git push -u origin main
```

---

## 📝 Basic Commands

### Show the status of files: modified, added, deleted

```bash
  git status
```

### View changes made to a file

```bash
  git diff <file_name>
```

### Pull the latest commits on the current branch

```bash
  git pull
```

Note: `git pull` = `git fetch` + `git merge`

### Pull changes from the main branch while on another branch

```bash
  git pull origin main
```

### Fetch remote branches and their commits (before merging)

```bash
  git fetch
```

---

## 🌿 Branches

### List all branches

```bash
  git branch -a
```

### Show the current branch

```bash
  git branch
```

### Create a new branch

```bash
  git branch <branch_name>
```

### Switch to another branch

```bash
  git switch <branch_name>
```

Or using the older syntax:

```bash
  git checkout <branch_name>
```

### Create and switch to a new branch

```bash
  git switch -c <branch_name>
```

Or using the older syntax:

```bash
  git checkout -b <branch_name>
```

### Delete a branch

```bash
  git branch -d <branch_name>
```

### Delete a remote branch

```bash
  git push origin --delete <branch_name>
```

---

## 📦 Staging and Committing

### Stage a file for commit

```bash
  git add <file_name>
```

### Stage all changes

```bash
  git add .
```

### Interactive staging (select specific lines to commit)

```bash
  git add -i
```

This allows you to select the exact lines you want to commit, not necessarily the entire file.

### Unstage a file

```bash
  git restore --staged <file_name>
```

Or using the older syntax:

```bash
  git reset <file_name>
```

### Discard changes in a file

```bash
  git restore <file_name>
```

Or using the older syntax:

```bash
  git checkout <file_name>
```

### Remove a file and stage the deletion

If you delete a file manually, but it's already in the git repository, it won't automatically be deleted from the repository.

```bash
  git rm <file_name>
```

### Commit changes

```bash
  git commit -m "commit message"
```

### Push changes online

```bash
  git add <file_name>  # or use . for all files
  git commit -m "commit message"
  git push
```

### Amend the last local commit

```bash
  git commit --amend
```

### Undo the last commit (keeping changes)

```bash
  git reset HEAD^
```

⚠️ **Warning**: Use with caution. This removes the commit but keeps the changes in your working directory.

### Undo the last commit (discarding changes)

```bash
  git reset --hard HEAD^
```

⚠️ **Warning**: This is destructive and will permanently delete your changes.

---

## 💾 Stash

### Stash locally modified files to work on other tasks

```bash
  git stash
```

### List stashed files

```bash
  git stash list
```

### Show stashed changes

```bash
  git stash show
```

### Apply stashed changes

```bash
  git stash pop
```

### Clear all stashed files

```bash
  git stash clear
```

---

## 👁️ Viewing Changes

### Show commit history

```bash
  git log
```

### Show a pretty formatted commit history

```bash
  git log --oneline --graph --decorate
```

### Show a specific commit

```bash
  git show <commit_hash>
```

### Show the last commit

```bash
  git show
```

---

## 🔧 Advanced Operations

### Merge branches

```bash
  git switch main
  git pull origin main
  git merge <branch_name>
  git push origin main
```

### Merge branches with conflicts

1. Switch to the branch you want to merge:

```bash
  git switch <branch_name_to_merge>
```

2. Pull changes from the main:

```bash
  git pull origin main
```

3. At this point there are conflicts - resolve them and test that everything works (!)

4. Commit the merge:

```bash
  git add .
  git commit -m "merge main"
  git push
```

5. Now `<branch_name_to_merge>` is up to date with main
6. Validate the PR and merge

### Rebase local commits on top of origin/dev (keeping local commits)

```bash
  git rebase origin/dev
```

### Interactive rebase (reorder, squash, edit commits)

```bash
  git rebase -i HEAD~<number_of_commits>
```

### Completely reset the local branch to match origin/dev (removing local commits)

```bash
  git reset --hard origin/dev
```

⚠️ **Warning**: This is destructive and will permanently delete your local commits.

### Cherry-pick a specific commit

```bash
  git cherry-pick <commit_hash>
```

### Force push (use with extreme caution)

```bash
  git push --force
```

⚠️ **Warning**: Never force push to shared branches (main/master) as it rewrites history and can cause issues for other developers.
