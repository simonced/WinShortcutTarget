param([string]$link="")

# how to use that script:
# powershell -ExecutionPolicy Bypass -file link_target.ps1 -link Vortex.lnk
# the last file name is the link file which we want the targetPath of

$shell = New-Object -ComObject Wscript.Shell
$target = $shell.CreateShortcut($link).targetpath

Write-Output $target
