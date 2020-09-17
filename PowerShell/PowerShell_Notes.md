# PowerShell Guide
PowerShell is a task-based command-line shell and scripting language;

https://docs.microsoft.com/en-us/powershell/

https://docs.microsoft.com/en-us/powershell/?view=powershell-6

## IDE for power shell 

Windows PowerShell Integrated Scripting Environment (ISE)

- https://docs.microsoft.com/en-us/powershell/scripting/getting-started/fundamental/windows-powershell-integrated-scripting-environment--ise-?view=powershell-5.1


## Commands

Everything is an object; use Get-Member to see methods/properties

|Shortcut | Description 
|--------|--------------------|
|$PSVersionTable |version ifo |
|dir get-member||
|**Variable Usage**||
|$a = 1+2||
|$a = "This is a string"||
|$a &#124; get-member| get properties of var|
|$a.length| show len|
|$name="Anish"||
|$a = "my name is $name"| outputs name; double quotes evaluates var; single quote won't|
|$MyCurrentProcess = Get-Process||
|**Cmdlet - Process related Usage**||
|get-process | shows all running processes|
| Get-Proces  &#124; Sort-Object  -Descending WS  &#124; select -first 10| show top 10 memory apps|
|Get-Process &#124; where-object  {$_.ProcessName -eq 'chrome'}|
|get-service | show all services running|
|Get-service &#124; where {$_.Status -eq 'Running'}||
|Stop-Process -Name 'chrome'|stop process|
|**Cmdlet - output**||
|Write-Host "hello world" | write something to shell|
|**Cmdlet - alias**||
| get-alias dir|show alias for dir|
|set-alias howdy Get_Process|set new alias howdy|
|**Misc**||
|Get-WmiObject -Class Win32_Product -ComputerName .|list apps|
|Get-WmiObject -Class Win32_Product -ComputerName . -Filter "Name='Java Auto Updater'"  &#124; Format-List -Property *| apply filters|
|date | prints date|
|help get-childitem -online| Get online help for commands|
| dir &#124; out-null| out-null allows skipping output to console|
|**COPY FIles related**||
|scp "file or dir" user@ipaddr:~/destination|copy files over to another machine|



Send output to file

```Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize > C:\Users\Lori\Documents\InstalledPrograms-PS.txt```

## Working with files

```powershell
# declar var
$files = dir
#  get first item
$files[0]
# get all methods
$files | get-member
# get a certain value
$files[0].name
$files[0].length

# sort by len
$files | sort -property length
$files | sort -property length -desc

# filter using where; show file lengh greater than 20 bytes
$files | where length -gt 20

# find file matching a name
$files | where name -eq 'ansel'

# find file contains name
$files | where name -like 'an*'

# iterate over with filter - $_ refers to current object
$files | where {$_.length -gt 2000}

# iterate mutliple filters
$files | where {($_.length -lt 50) -and  ($_.name -like 'an*')}
```

## Read file recursively

```powershell

# read all files under a dir and sub dirs
$files = Get-ChildItem -recurse

# specify path
 $files = Get-ChildItem -Path 'C:\temp' -recurse
```

## Loops

```powershell
# loop 
1..10 | foreach {$_*2}

# loop with index
1..10 | foreach {"This is loop number $_"}

# multiply
"Hello"*3

1..10 | foreach {"*"*$_}

#  loop conditional logic - print odd numbers
1..10 | foreach {if ($_%2){"$_ is odd"}}
```
- more examples: https://www.howtogeek.com/165293/how-to-get-a-list-of-software-installed-on-your-pc-with-a-single-command/

## Arrays

```powershell
$strComputers = @("server1", "Server2", "Server3")
$strComputers

# get 1st item
$strComputers[0]

# update 1st item
$strComputers[0] = "server1new"

# find length
$strComputers.Length

# concatenate
$strComputers1 = @("server1", "Server2", "Server3")
$strComputers2 = @("server4", "Server5")
$allcomputers = $strComputers1 + $strComputers2

# iterate array
$strComputers | foreach{$_}

# iterate array property
$strComputers | foreach{$_.length}
$strComputers | foreach{$_ + " - " + $_.length}

```

## Hash tables - key value pairs

```powershell
# create new
$serverips = @{"server1" = '10.3.4.1'; "Server2" = '10.3.4.5'}

# get value
$serverips["server1"]

# reassign value
$serverips["server1"] = '10.2.3.1'

# add new value
$serverips["server3"] = '10.3.5.100'

# remove item
$serverips.Remove("server1")
```

## Formatting Output

ways to format output

```powershell

# format wide
$files | format-wide

# list format
$files | format-list

$files | format-list -Property name, length, lastwritetime

$files | format-table

get-process | format-table -property path, name

# group by usage
get-process | format-table -property path, name -groupby company

# sort then group
get-process | sort -property company | format-table -property path, name -groupby company

```

## Saving output

```powershell
# save to txt
Get-Process | Out-file c:\temp\processes.txt

# open in notepad
notepad c:\temp\processes.txt

# ConverT to HTML
Get-Process | ConvertTo-HTML 
Get-Process | ConvertTo-HTML  | Out-file c:\temp\processes.html

# invoke in related app
invoke-expression c:\temp\processes.html

# export to csv
Get-Process | export-csv c:\temp\processes.csv

# open with associated prgram
invoke-expression c:\temp\processes.csv
```

## Import CSV data

```powershell
# store csv in names
$names = Impost-csv c:\temp\processes.csv

# list in column format
$names | format-table

$

```

## Functions

```powershell
# simple
function sayHello
{
    "Hi there"
}
# call
sayHello

# using params

function sayHello
{
    param($name)
    "Hi there $name"
}
# call with param
sayHello("Anish")
sayHello "Anish"
sayHello -name "Anish"

# using return 
function sayHello
{
    param($name)
    return "Hi there $name"
}
$gretting = sayHello -name "Anish"
$gretting

#  another func example

function get-DirInfo($dir)
{
    $results = Get-ChildItem $dir -Recurse |Measure-Object -Property length -Sum
    # return size in GB
    return [math]::Round(($results).sum/1GB,2)


}
# call
get-DirInfo C:\temp
get-DirInfo Y:\
```

## Run Script files


Run below script: ```myscript.ps1 c:\temp```

```powershell
# my_script.ps1

# parameters
param([string]$dir="c:\")

# function
function get-DirInfo($dir)
{
    $results = Get-ChildItem $dir -Recurse |Measure-Object -Property length -Sum
    # return size in GB
    return [math]::Round(($results).sum/1GB,2)


}
# run func using passed in param
get-DirInfo $dir
```

## Sample Scripts

```powershell

#Create a function named DisplayFolderStatistics to display folder statistics for a directory/path that is passed 
#to it. Output should include the name of the folder, number of files in the folder, and total size of all files in 
#that directory.
function Display-FolderStats([string]$path){
 $files = dir $path -Recurse | where {!$_.PSIsContainer}
 $totals = $files | Measure-Object -Property length -sum
 $stats = "" | Select path,count,size
 $stats.path = $path
 $stats.count = $totals.count
 $stats.size = [math]::round($totals.sum/1MB,2)
 return $stats
}


#Create a function named CheckFolder that checks for the existence of a specific directory/folder that is passed 
#to it as a parameter. Also, include a switch parameter named create. If the directory/folder does not exist and 
#the create switch is specified, a new folder should be created using the name of the folder/directory that was 
#passed to the function.
function Check-Folder([string]$path, [switch]$create){
    $exists = Test-Path $path

    if(!$exists -and $create){
        #create the directory because it doesn't exist
        mkdir $path | out-null
        $exists = Test-Path $path
    }
    return $exists
}

```

### Troubleshooting

Script execution issue in VS Code: https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl
