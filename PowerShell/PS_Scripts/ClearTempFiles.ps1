echo "#####  POWERSHELL SCRIPT TO DELETE TEMP FILE ####"
echo "Deleteing Temp Files..."
Get-ChildItem $env:tmp -Recurse | Remove-Item -Recurse -force -ErrorAction SilentlyContinue
Get-ChildItem ([environment]::GetEnvironmentVariable("temp","machine")) -Recurse| Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Read-Host -Prompt "Script Complete! Press Enter to exit"