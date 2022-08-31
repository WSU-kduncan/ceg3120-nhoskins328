## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Gets a copy of a repo of choice and creates a clone of it in another location
    - shows what you're cloning into
    - shows how many files or folders are in the repo
  - git clone <url of repo>
- add
  - Adds a file to the tracked index and adds it to a space where it waits to be commited and pushed to the github repo
  - git add <file>
- rm
  - Removes a file from the tracked index 
    - can also remove from space where added files have gone before commiting
  - git rm <file>
- commit
  - Commit saves the state of the tree as it is when the command is ran 
    - brings you to a screen where you can add a optional message to clarify what was changed
  - git commit --a
- push
  - pushes the local repository to the cloned repo
    - tells you how many files are being pushed 
    - gives a brief summary of what happened to said files
  - git push
- fetch
  - allows to see wether changes went through to the remote repository or not
    - shows the repository and points out wether any new files or branches were added
  - git fetch <repository>
- merge
  - merges a branch that has 'split' back into the 'main' branch  
    - shows any changes made as a reslut of the merge
  - git merge <split branch>
- pull
  - gets the latest snapshot of what is in the local repository and updates the local repository using said snapshot
    - shows where the pull is coming from
    - shows how many files are being added to the local repo
  - git pull 
- branch
  - can either add, delete, or list all branches in the local repo
    - git branch list branches, can also be achieved with git branch --list
    - git branch <branch> creates a new branch 
    - git branch -d <branch> deletes the specified branch
- checkout
  - allows you to move between any branch you have
    - normally used with git branch
  - git checkout <branch>
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - contains a history of commits and remote repository addresses 
- .gitignore file
  - contains a series of patterns that git uses to decide wether or not to ignore a file for tracking or not
- ~~.git/hooks~~

## GitHub

- Pull requests
  - brings up a page of changes made between the local branch and the remote repository branch
  - allows you and others to view said page and make comments all while being able to push more stuff
- SSH authentication to repositories
  - a user generates a private and public key 
  - the user uploads the public key to github which allows their device to act as a local repository
  - the private key is meant to be kept private, no need to upload it anywhere.
- ~~Actions~~
