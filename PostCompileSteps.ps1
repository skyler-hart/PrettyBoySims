#Remove-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.pyc' -Force
#Remove-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.ts4script' -Force
#Remove-Item 'C:\Users\skyler\OneDrive - Wandering Stag, LLC\Documents\Electronic Arts\The Sims 4\Mods\GhostShell.ts4script' -Force
# Rename-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.cpython-37.pyc' ghostshell.pyc

Remove-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\ghostshell.ts4script' -Force

#Compress-Archive -Path 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\' -DestinationPath 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\\ghostshell.zip' -CompressionLevel NoCompression -Force
$source = "C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu"
$dest   = "$source\ghostshell.ts4script"

# Remove any existing zip
if (Test-Path $dest) { Remove-Item $dest }

# Create new zip archive
Add-Type -AssemblyName 'System.IO.Compression.FileSystem'
$zip = [System.IO.Compression.ZipFile]::Open($dest, 'Create')

# Add only .pyc files to the archive, preserving folder structure
Get-ChildItem -Path $source -Recurse -Include *.pyc | ForEach-Object {
    $entryPath = $_.FullName.Substring($source.Length + 1)
    [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $_.FullName, $entryPath, [System.IO.Compression.CompressionLevel]::NoCompression)
}

$zip.Dispose()


# Rename-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\ghostshell.zip' -NewName 'ghostshell.ts4script'

#Copy-Item -Path 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.ts4script' -Destination 'C:\Users\skyler\OneDrive - Wandering Stag, LLC\Documents\Electronic Arts\The Sims 4\Mods' -Force
