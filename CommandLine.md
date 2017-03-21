# Command Line Cheat Sheet

## Misc useful commands

### [tab]
  + [command] [tab] / [command] [character] [tab]
  + will present the different options available for the current command; [tab] to move between the options; [enter] to choose the highlighted option

### pwd
  + will tell you which directory (folder) you are currently in

### cd ..
  + will move you up one step within the directory

### cd [folder-name]
  + will move you to the folder [folder-name] - _as long as [folder-name] is located within the directory you are currently in_

### cd [tab] / cd [character] [tab]
  + will present the different navigation options; use [tab] to move between the options && [enter] to choose the highlighted option.

### ls
  + will list all visible files and folders within the current directory

### ls -a
  + will list everything - including hidden files - within the current directory

### touch [file-name]
  + will create a file named [file-name] within the current directory

<!-- ### echo  -->

### atom [file-name]
  + will open the file [file-name] in Atom

### open [file-name]
  + will open the file [file-name] in the program "which makes most sense" depending on the file type

### cat [file-name]
  + will print the content of the file [file-name] to the terminal

### git status
  + ...
  + _it is useful to use this command before & after committing_ and _pushing files to the repo, to ensure that you are adding and removing the correct files_

### git whatchanged
  + will display the most recent commit
    + the commit message
    + the changed files (added, removed, modified, etc)
    + exit through "q"

## Adding to GitHub

### git add --all .
  + will add all changes within the current directory to the commit [pile]; including added, renamed and removed files

#### git add .
  + will add everything within the current directory to the commit [pile]

<!-- #### git add . -p
  +  -->

#### git rm <file-name>
  + will add instructions to the commit [pile] to remove [file-name] from the repo

### git commit -m "[message]"
  + will commit the added changes (additions, removals, updates and renamings of files) to the [pile] to be pushed to GitHub
  + -m "[message]" allows you to include a description of the commit

### git push
  + pushes the committed items to GitHub

## Branches and Collaborating commands

### git checkout -b [branch-name]
  + create & move to a new branch named [branch-name]

### git checkout [branch-name]
  + move to branch [branch-name]

### git branch
  + will list all the branches in the repo && indicate which is the current one

### git push origin [branch-name]
  + will push the new branch to the github
  + 'git push' alone will not make the new branch (& its material) appear on github
    + NOTE: After doing this & having completed the merge onto the 'master' branch, should switch back to the 'master' branch on the computer and use 'git pull', to ensure that the 'master' branch is up to date locally

### git pull origin master
  + To update a local branch with the content on the Master branch (in the terminal):
    + Go to the Master branch > 'git pull'
    + Go to the relevant branch > 'git pull origin Master'

  <!-- ### git log
    + will display the repo log within the terminal
    + exit using command 'q' -->

  <!-- ### To clone single branch, try:   (although cloning the entire repo should clone all different branches as well >> use 'git branch' to check which  branches are available locally)
    +git clone <url> --branch <branch> --single-branch [<folder>] -->

## Other commands

#### python --version
  + will return which version of Python is currently installed
