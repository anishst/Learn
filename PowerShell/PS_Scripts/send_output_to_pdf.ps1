# https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/sending-powershell-results-to-pdf-part-1

$printer = Get-Printer -Name "Microsoft Print to PDF" -ErrorAction SilentlyContinue
if (!$?) {
    Write-Warning "Your PDF Printer is not yet available!"
}
else {
    Write-Warning "PDF printer is ready for use."
}

# simple test that sends services to pdf; this one prompts for filename

# Get-Service | Out-Printer -Name "Microsoft Print to PDF"

# specify the path to the file you want to create
# (adjust if you want)
$OutPath = "$home\desktop\result.pdf"

# this is the file the print driver always prints to
$TempPDF = "$env:temp\PDFResultFile.pdf"

# make sure old print results are removed
$exists = Test-Path -Path $TempPDF
if ($exists) { Remove-Item -Path $TempPDF -Force }

# send PowerShell results to PDF
# Get-Service | Out-Printer -Name "PrintPDFUnattended"
(Invoke-WebRequest -Uri "http://www.google.com").Links.Href | Out-Printer -Name "PrintPDFUnattended"

# wait for the print job to be completed, then move file
$ok = $false
do { 
    Start-Sleep -Milliseconds 500 
    Write-Host '.' -NoNewline
                
    $fileExists = Test-Path -Path $TempPDF
    if ($fileExists) {
        try {
            Move-Item -Path $TempPDF -Destination $OutPath -Force -ErrorAction Stop
            $ok = $true
        }
        catch {
            # file is still in use, cannot move
            # try again
        }
    }
} until ( $ok )
Write-Host

# show new PDF file in explorer
explorer "/select,$OutPath"