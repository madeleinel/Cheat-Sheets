# Git Cheat Sheet

## Misc useful commands

### pwd
  + will tell you which directory (folder) you are currently in

### cd ..
  + will move you up one step within the directory

### cd [folder-name]
  + will move you to the folder [folder-name] - _as long as [folder-name] is located within the directory you are currently in_

### ls
  + will list everything within the current folder

### git status
  + ...
  + _it is useful to use this command before & after committing_ and _pushing files to the repo, to ensure that you are adding and removing the correct files_

## Adding to GitHub

### git add .
  + will add everything within the current directory to the commit [pile]

### git rm <file-name>
  + will add instructions to the commit [pile] to remove [file-name] from the repo

### git commit -m "[message]"
  + will commit the added changes (additions, removals, updates and renamings of files) to the [pile] to be pushed to GitHub
  + -m "[message]" allows you to include a description of the commit

### git push
  + pushes the committed items to GitHub
