# https://docs.microsoft.com/en-us/powershell/scripting/getting-started/cookbooks/working-with-software-installations?view=powershell-5.1
cls
New-PSDrive -Name Uninstall2 -PSProvider Registry -Root HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
$UninstallableApplications = Get-ChildItem -Path Uninstall:
Get-ChildItem -Path Uninstall: | ForEach-Object -Process { $_.GetValue("DisplayName") }