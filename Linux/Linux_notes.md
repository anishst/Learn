# Linux

LINUX is an open source software development and free operating system developed by Linus Torvalds in 1991

- runs on many hardware platforms
- small footprint
- great for servers
- stable/reliable, secure

BASH (Bourne Again Shell) is the Linux default shell i.e. text mode interface which supports multiple command interpreters.

Basic Components: 
- Kernel
- System Library
- System Utility

*root account* - system administrator account which gives you the ability to fully control the system

Linux Distro examples:
- Ubuntu
- Linux Mint
- Debian
- Fedora
- Red Hat Enterprise (RHEL)
- CentOS - same as REHEL - branding/logos

## Connecting over the network

- SSH - replaced telnet as the way to connect over network
- PuTTy - terminal emulator

## Common Directories

like a tree
 - / - "root" top of file system
 - /bin - binary files and exe files
 - /etc - config files
 - /home - home directories; separates user data
 - /opt - optional or third party software
 - /tmp - temp space; typically cleared on reboot
 - /usr - user related programs
 - /var - variable data; ex. log files

## Shell
- default intfc to linux
- command line 
- shell prompts 
    - $ indicate normal user
    - '#' super user or root
## Tilde expansion
- ~username = /home/username
- ~root = /root
- ~ftp = /srv/ftp
Cron - Cron allows the user to schedule tasks to be executed every minute.

Grep -  stands for ‘global regular expression print’. This command is used for matching a regular expression against text in a file.

## Working with Directories
- . current directory
- .. parent dir
- pwd - current work dir
- cd .. - go to parent
- cd username/

## Wildcards

- a char or string used for pattern matching
- wildcards be used with many commands
- '*' - matches zero or more
- '?' - matches exactly one character
- [] - character class
    - maches any of the chars included between the brackets; matches exactly one char
    - to exculde use ! ; [!aeiou]*
    - to find a rang use hyphen; [a-g]*
 - named char classes; ex. [[:alpha:]]

## Input, Output, and Redirection

- standard input - stdin 
- std output - stdout
- std errror - stderr
- '>' rediects to a file. new file
- '>>' appends to a file
- '<' redirects input from a file  to a command
- ```>/dev/nulll``` redirect output to nowhere

## Comparing contents of files

- diff file1 file2 - compares two files
- sdiff file1 file2 - side-by-side compare
- vimdiff file1 file2 - hightlight diff in vim

## Searching files
- grep displays line matching pattern
- grep pattern file
- grep -i searchterm file - ignores case
- grep -c shows count of occurences
- file <filename - displays file type
- pipe sysmbol ; cmd-out | cmd-input
- cat file | grep pattern
- grep bob /etc/passwd | cut -d: -f1,5 | sort - get username and password and sort it

## Customize shell

- PS1="<\t \u@\h \w>\$ " - display time username@direcotryname
- to make permanent, add to vi .bash_profile
    - export PS1="[mycustomterminal \u@\h \w>\$ "
## Linux Commands
|Command | Description 
|--------|--------------------|
|ls|list directory contents|
|ls -l|long listing dir contents|
|pwd|display current work dir|
|echo| display env vars; echo $PATH|
|cd| changed directory; cd without args takes you to home dir|
|cat| concatenates and display files|
|man| displays online manual|
|exit|exit cmd prompt|
|which *programname*| display location of program; ```which python3```|
|mv old_dirname/ new_dirname| rename folder|
|**Directory ops**||
|mkdir *dirname*|create dir|
|mkdir -p *dirname*|create dir and parent dirs| 
|rmdir *dirname*|remove empty dir|
|rm -rf *dirname*|remove dir and files recursively|
|**Listing Files**||
|ls -l|detailed dir outpu|
|```ls -l -a``` OR ```ls -al```|show hidden files|
|ls -F|to reveal file types; / = dir @ =link * =exe|
|ls -t|list files by time|
|ls -r|reverse order|
|ls -latr|long list include all files reverse sorted by time|
|ls -R|list files recursively
|tree -d|visual dir list|
|tree -C|visual colorize outpu|
|ls --color|colour output|
|**Display contents of Files**||
|cat *file*|display contents of file|
|more *file*|browser thru txt file|
|less *file*|more features than more|
|head *file*|output beginning or top portion of file; by deault only 10 lines; change this by adding -<numofline>; example: head -15 file.txt|
|tail *file*|output ending or bottom portion of file; by deault only 10 lines; change this by adding -<numofline>; example: tail -15 file.txt|
| tail -f *file*| display data as it is being written to the file|
|**Finding File and Directories**||
|find [path..] [pattern]|find files; ex. ```find *.log```|
|find /bin -name *v|find file ending with v|
|find . -mtime +3 |find files modified|
|find . -size +1M|find files 1MB or greater|
|locate *pattern*|faster than find; queries and index; delay due to index|

https://www.marquette.edu/mathematical-and-statistical-sciences/basic-vi-editor-commands.php

## Text Editors
### Nano Editor
- simple text editor
- easier than vi or emac
- if nano is not availble , look for pico

### Vi Editor
- more harder to learn;
- vi [file] - edit file
- vim [file] - same as vi but more features

## Graphical Editors

- emacs
- gedit
- gvim
- kedit

### Vi command mode and navigation 

|Command | Description 
|--------|-----------|
|i|insert mode at cursor position|
|I|insert beginning of line|
|a|append after cursor position|
|A|append at then end of line|
| k| up one line|
| j | down one line|
|h| left one char|
|l|right one char|
|w|right one word|
|b|left one word|
|^|go to the begining of line|
|$|go to end of line|
|:n| position cursor at line n|
|$|position at last line|
|:set nu | turn on line numbering|
|:set nonu | turn off line numbering|
| 5k|move up line 5 times|
| 80i<text><ESC>| insert <text> 80 times|
|**Deleting Text**||
|x|delete a char|
|dw|delete a wor|
|dd|delete a line|
|D|delete from the current position|
|**File save related**||
|:w|writes file|
|:w!|forces file to be saved|
|:q|quit|
|:q!|quick w/o saving|
|:wq!|write and quit|
|:x|same as :wq|


vi commands: https://www.guru99.com/the-vi-editor.html#3

## Permissions

<1char =type><next 3 chars =user permisions><next3=group permissions><next 3 = all user permissions>
ls -l 

```-rw-rw-r-- 1 adminuser adminuser  9 May 26 14:02 'my notes.txt'```

```drwxr-xr-x 2 adminuser adminuser  6 May 22 18:27  Pictures```

 - '-' = regular file
- d = dir
- | symbolic link

3 main types of permissions: r=read w=write x=execute

Groups
- every user in at least group
- use ```groups``` command to display users group; or ```id -Gn```
- use ```groups <userid>``` to show their groups

## Changing Permissions

- ```chmode``` = changing mode

http://linuxcommand.org/lc3_lts0090.php





## Debian OS

https://www.debian.org/doc/manuals/debian-reference/pr01.en.html
- add user to sudo: https://devconnected.com/how-to-add-a-user-to-sudoers-on-debian-10-buster/
- https://unix.stackexchange.com/questions/179954/username-is-not-in-the-sudoers-file-this-incident-will-be-reported

## Resources
- centOS vdi download https://www.linuxtrainingacademy.com/vdi/
- https://distrowatch.com/ - keep on new distros