Videos 
==================================
Crash course on Git/GitHub: https://www.youtube.com/watch?v=SWYqp7iY_Tc

Documentation
=======================
Git: https://git-scm.com/doc
GitHub: https://help.github.com/en

GitHub Markdown
=====================
https://guides.github.com/features/mastering-markdown/
Emojis: https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

Git Commands
===========================================================

Configuation Info
======================
git config --list

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

[Guide to SSH Key gen]:https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

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

# Troubleshooting
----------------------
Issue: get below error when trying to push

2:15 PM	Update failed
				remote: Password authentication is not available for Git operations.
				remote: You must use a personal access token or SSH key.
				remote: See https://github.company.com/settings/tokens or https://github.company.com/settings/ssh
				unable to access 'https://github.company.com/OTCnet/AutomationSeleniumPython.git/': The requested URL returned error: 403

Solution: disable credential helper for the current project by executing
git config credential.helper ""

More details:https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000586190-VCS-in-PyCharm-works-with-one-Github-account-but-not-the-other

Setting Usernames globally
===============================
$ git config --global github.user defunkt
$ git config --global github.token 6ef8395fecf207165f1a82178ae1b984


push to orgs
=============================
close PyCharm
open a terminal in or from terminal navigate to the local project directory.
run your version of: git remote add origin https://github.com/<organization>/<project>.git
open PyChram and push project: "VCS"->'git'->'push'

Push to GitHub Using Existing Repo
====================================

…or create a new repository on the command line
``` 
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.<server>.com/<project>/test.git
git push -u origin master
```

…or push an existing repository from the command line
```
git remote add origin https://github.<server>.com/<project>/test.git
git push -u origin master
```