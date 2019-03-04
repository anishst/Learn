# get ip address
Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=TRUE -ComputerName . | Format-Table -Property IPAddress

# Get network adapter settings
Get-WmiObject -Class Win32_NetworkAdapter -ComputerName .

Read-Host -Prompt "Script Complete! Press Enter to exit"