Remove-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.pyc' -Force
Remove-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.ts4script' -Force
#Remove-Item 'C:\Users\skyler\OneDrive - Wandering Stag, LLC\Documents\Electronic Arts\The Sims 4\Mods\GhostShell.ts4script' -Force

Rename-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.cpython-37.pyc' ghostshell.pyc

Compress-Archive -Path 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__' -DestinationPath 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.zip' -CompressionLevel NoCompression -Force
Rename-Item 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.zip' -NewName 'ghostshell.ts4script'

#Copy-Item -Path 'C:\Users\skyler\.GitHub\PrettyBoySims\GhostShell Menu\__pycache__\ghostshell.ts4script' -Destination 'C:\Users\skyler\OneDrive - Wandering Stag, LLC\Documents\Electronic Arts\The Sims 4\Mods' -Force
