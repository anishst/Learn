# Git

Git is a free and open source distributed version control system 

Download page: https://git-scm.com/download/win

 # GitHub

GitHub is a web-based hosting service for version control using Git

Videos 
==================================
Crash course on Git/GitHub: https://www.youtube.com/watch?v=SWYqp7iY_Tc

Documentation
=======================
- Git: https://git-scm.com/doc
- GitHub: https://help.github.com/en
- Fork a Repo - https://help.github.com/en/articles/fork-a-repo
- Atlassian Guides - https://www.atlassian.com/git/tutorials/what-is-version-control

GitHub Markdown
=====================
https://guides.github.com/features/mastering-markdown/
Emojis: https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md

# Code Documentation 
Guide on Documenting code: https://guides.github.com/features/wikis/

## Pull Request Steps

1. create a new branch ```git branch feature1``` and checkout ```git checkout feature1```
2. make your code changes; add and commit
3. switch to master: ```git checkout master```
4. check for updates: ```git pull```
5. if there are new items in master merging new updates by:
   - ```git checkout feature1```
   - ```git merge master```
   - resolve conflicts if any
6. once all looks good push: ```git push -set-upstream origin feature1```
7. in GitHub, compare changes and create a pull request

## Merge vs Rebase

git merge --squash feature
git commit -m "feature and master merge"

git rebase master
git log

### Guides
- https://www.atlassian.com/git/tutorials/merging-vs-rebasing

### Videso
- [GITHUB PULL REQUEST, Branching, Merging & Team Workflow](https://www.youtube.com/watch?v=oFYyTZwMyAg)

## Git Commands

Cheat Sheets: https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

### Basics
Command | Description
-------| -------------
git --version | shows versions
logins | contains user login information
git config --list | Configuation Info
git help | shows help


### New Repo Related
Command | Description
-------| -------------
git init | creats a new repo
git status | - lists all new or modified files to be committed
git diff | shows file differences not staged
git add [filename] 	| snapshots the file in prep for versioning
git add . 	| snapshots all eligible file in prep for versioning
git commit -m [filename] | commit changes for given file
git commit -m "msg" . | commit all changed files; -m is for comment
git rm [filename]  | to remove a file
git commit rm "removing [filename]" | remove file
git mv [filename] *source* | move file
git pull | 2 command in one; includes fetch
git fetch | use to get updates from remote
git rm -r --cached *folder* | removes folders already in git
git rm --cached *file*  | removes file already in git
git checkout *file* | allows you to get the latest copy from master branch


### Cloning
Command | Description
-------| -------------
git clone https://github.com/<username>/<repo>.git | clones an existing repo
git clone --branch master --single-branch --depth 1 *repourl* | cline an existing repo but only pull files in latest commit; skip downloading git history

### Historical Data
Command | Description
-------| -------------
git log     | shows changes|
git help log | more info on logs|
git log --oneline --graph --decorate --color  | better graphical view|
| git blame *filename*| who changed what and when in *filename*|

### Setting Usernames globally
Command | Description
-------| -------------
$ git config --global github.user [username] | set username
$ git config --global github.token [token] | set token


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

## Ignoring files
use .gitignore file


## Revert back to previous commit

```git reset --hard <old-commit-id>```

```git push -f <remote-name> <branch-name>```


## Authentication

### Personal Access Token
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

### SSH Auth
```
mkdir ..SSH
ssh-keygen -t rsa -C "<emailaddress> - follow prompts
ssh -T git@github.com
```
To use: go to github and setup ssh keys

[Guide to SSH Key gen]:(https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent )

Pushing to Github Online
====================================
remote add origin <account>
git push -- pushes to Github
git push origin master
git pull origina master
git pull --downloads from Github
git merge

## Generate SSH Key for GitHub Deploy Key

1. open up command: ssh-keygen -t rsa
2. follow prompts
3. a file will get created under: C:\Users\<userid>\.ssh
4. public key is in: id_rsa.pub file
5. copy contents
6. go to github
7. in the repo, go to settings > Deploy Keys > give a name and paste the contents and save
8. clone the repo using ssh 


## Switching remote URLs from HTTPS to SSH
git remote set-url origin git@hostname:USERNAME/REPOSITORY.git

https://help.github.com/en/enterprise/2.20/user/github/using-git/changing-a-remotes-url#switching-remote-urls-from-https-to-ssh

# Tips

to reduce cloning time use below syntax to avoid downloading all history

```git clone --branch <name> --single-branch --depth 1 <repourl>```

# Troubleshooting

Issue: get below error when trying to push

2:15 PM	Update failed
				remote: Password authentication is not available for Git operations.
				remote: You must use a personal access token or SSH key.
				remote: See https://github.company.com/settings/tokens or https://github.company.com/settings/ssh
				unable to access 'https://github.company.com/<org>/AutomationSeleniumPython.git/': The requested URL returned error: 403

Solution: disable credential helper for the current project by executing
```git config credential.helper "" ```

More details:https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000586190-VCS-in-PyCharm-works-with-one-Github-account-but-not-the-other

https://stackoverflow.com/questions/10054318/how-do-i-provide-a-username-and-password-when-running-git-clone-gitremote-git


push to orgs
=============================
close PyCharm
open a terminal in or from terminal navigate to the local project directory.
run your version of: git remote add origin https://github.com/<organization>/<project>.git
open PyChram and push project: "VCS"->'git'->'push'

