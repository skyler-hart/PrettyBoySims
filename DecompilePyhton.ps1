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
python -m compileall "C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\ghostshell.py"
