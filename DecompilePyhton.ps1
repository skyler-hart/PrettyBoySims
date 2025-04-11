Get-ChildItem -Path "D:\Apps\Sims\GAME\WickedWhims\TURBODRIVER_WickedWhims_Scripts" -Recurse -Filter *.pyc | ForEach-Object {
    $outputPath = $_.DirectoryName
    uncompyle6 -o "$outputPath" $_.FullName
    if ($?) { Remove-Item $_.FullName -Force }
}




Get-ChildItem -Path "D:\Apps\Sims\GAME\GhostShell_Populated\mc_ghostshell" -Recurse -Filter *.pyc | ForEach-Object {
    $outputPath = $_.DirectoryName
    uncompyle6 -o "$outputPath" $_.FullName
    if ($?) { Remove-Item $_.FullName -Force }
}



######################
# To compile
cd D:\VENV\Sims
.\Scripts\Activate.ps1

python -m compileall "C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\ghostshell.py"
python -m compileall -b "C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu"


# Only compile recently modified .py files
$sourcePath = "C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu"

Get-ChildItem -Path $sourcePath -Recurse -Filter *.py | ForEach-Object {
    $pyFile = $_.FullName
    $pycFile = [System.IO.Path]::ChangeExtension($pyFile, ".pyc")

    if (!(Test-Path $pycFile) -or (Get-Item $pyFile).LastWriteTime -gt (Get-Item $pycFile).LastWriteTime) {
        python -m py_compile $pyFile
    }
}
