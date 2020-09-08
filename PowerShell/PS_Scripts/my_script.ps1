param([string]$dir = "c:\temp")

# function
function get-DirInfo($dir) {
    Write-Output "Getting size of dir $dir..."
    $results = Get-ChildItem $dir -Recurse | Measure-Object -Property length -Sum
    # return size in GB
    return [math]::Round(($results).sum / 1GB, 2)


}
# run func using passed in param
get-DirInfo $dir