# PowerShell Guide
PowerShell is a task-based command-line shell and scripting language;

https://docs.microsoft.com/en-us/powershell/


## IDE for power shell 

Windows PowerShell Integrated Scripting Environment (ISE)

- https://docs.microsoft.com/en-us/powershell/scripting/getting-started/fundamental/windows-powershell-integrated-scripting-environment--ise-?view=powershell-5.1


## Commands

cls - clear s
creen
ls - list directories
cd - change dirs
help
help ls

get-process - shows all running processes
Get-Process | where-object  {$_.ProcessName -eq 'chrome'}

get-service - show all services running
Get-service | where {$_.Status -eq 'Running'}

Stop-Process -Name 'chrome'


## Listing Windows Installer Applications

Get-WmiObject -Class Win32_Product -ComputerName .

## Apply filters
Get-WmiObject -Class Win32_Product -ComputerName . -Filter "Name='Java Auto Updater'"| Format-List -Property *

Write-Host "hello world" - write something to shell
date - prints date

## Using Variables
$MyCurrentProcess = Get-Process
Get-Process

Using double quotes evaluates the variable in the string
$name = "anish"
"My name is $name"

## Get list of installed apps
```Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize```

Send output to file

```Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize > C:\Users\Lori\Documents\InstalledPrograms-PS.txt```

- more examples: https://www.howtogeek.com/165293/how-to-get-a-list-of-software-installed-on-your-pc-with-a-single-command/
