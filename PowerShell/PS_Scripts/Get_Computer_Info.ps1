# https://docs.microsoft.com/en-us/powershell/scripting/getting-started/cookbooks/collecting-information-about-computers?view=powershell-5.1

# Get BIOS info
Get-WmiObject -Class Win32_BIOS -ComputerName .

# Listing Processor Information
Get-WmiObject -Class Win32_Processor -ComputerName . | Select-Object -Property [a-z]*

# Listing Computer Manufacturer and Model
Get-WmiObject -Class Win32_ComputerSystem

# List installed hotfixes
Get-WmiObject -Class Win32_QuickFixEngineering -ComputerName .

Read-Host -Prompt "Script Complete! Press Enter to exit"