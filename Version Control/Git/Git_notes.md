reVideos 
==================================
Crash course on Git/GitHub: https://www.youtube.com/watch?v=SWYqp7iY_Tc

SublimeText Related
+++++++++++++++++++++++++++++++++++++++++
packages: GitSavvy
 
Git Commands
Download page: https://git-scm.com/download/win
++++++++++++++++++++++++++++++++++++++++++
git --vesion - shows versions
git clone <URL> -- this downloads the repository from Github
git init
git status -- what is different between local and Github

git add <filename> - add changes

**** MAKE CHANGES **********
============================
git status  	- lists all new or modified files to be committed
git diff 		-shows file differences not staged
git add [file] 	- snapshots the file in prep for versioning
git commit  -m "added new file" - -m is for comment

Removing/Moving files
=====================================
git rm <filename>  - to remove a file
git commit -m "removing <filename>"
You can also remove using GUI or command line outside git

git mv <filename> <source>

Get Historical Data
=========================
git log     - shows changes
git help log - more info on logs
git log --oneline --graph --decorate --color        - better graphical view

Ignoring files
==================================
use .gitignore file

SSH Auth
=====================
mkdir ..SSH
ssh-keygen -t rsa -C "<emailaddress> - follow prompts
ssh -T git@github.com
To use: go to github and setup ssh keys

Pushing to Github Online
====================================
remote add origin <account>
git push -- pushes to Github
git push origin master
git pull origina master
git pull --downloads from Github
git merge

**** HELP **********
============================
git help -shows help

escape /wq