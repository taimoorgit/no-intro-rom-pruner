# No-Intro ROM Pruner - a python script to remove junk ROMs for your convenience.

If you downloaded ROMs from any collection e.g. the "No-Intro" SNES/NES/GBA ROMs, there are a ton of junk ROMs that you probably don't want.

```
% cd my-snes-roms           # you can use NES and GBA ROMs and other ROMs too, they just have to be No-Intro or named like them.
% ls
[BIOS] Super NES CD-ROM - Boot ROM (Japan) (En) (v0.95) (Proto).zip         # this is the BIOS for the unreleased SNES CD - really interesting but I don't need it on my handheld.
...
Mega Man X (Europe).zip                                                     # don't want Europe ROMs
Mega Man X (USA).zip                                                        # THIS IS WHAT I ACTUALLY NEED!!!!!!!!!!!!!!!!!!!!!!!!!!
Mega Man X (USA) (Capcom Town).zip                                          # not a real SNES ROM, ripped from somewhere
Mega Man X (USA) (Rev 1).zip                                                # don't want revision ROMs
Mega Man X (World) (Rev 1) (Mega Man X Legacy Collection).zip               # not a real SNES ROM, ripped from PS2 game
...
Super Metroid (Europe) (En,Fr,De).zip                                                             # don't want Europe ROMs
Super Metroid (Japan) (En,Ja) (Virtual Console, Switch Online).zip                                # not a real SNES ROM
Super Metroid (Japan, USA) (En,Ja).zip                                                            # THIS IS THE ONLY ONE I WANT!!!!!!!!!!!
Super Metroid (USA, Europe) (En,Ja) (Virtual Console, Classic Mini, Switch Online).zip            # not a real SNES ROM
...
Street Fighter EX Plus Alpha (USA) (Pirate).zip               # fake ROM, total junk
Street Fighter V (World) (Pirate).zip                         # same
```

This script goes through each ROM and extracts the tags, e.g. `(USA)`, `(Proto)`, `(Rev 1)`. It ignores language tags.

**Any ROM that doesn't have a `(USA)` tag gets moved to the pruned folder.** Revisions get sent to the pruned folder too as do ROMs with the `(Virtual Console)` or `(Pirate)` tag.

Keep in mind that means a game like Star Fox 2 that never actually got released will get moved into the pruned folder, since all the ROMs for Star Fox 2 either have `(Beta)` or some other tag. 

You can just move the ROM file back to the folder after running the script. 

If you know Python you could fork add an `if else` to handle exceptions. 

## Usage

Place the script.py into the parent folder for your ROMs.

By default the script will "dry run" so you can see what it will do before executing. 

```
% cd my-snes-roms
% python3 ../script.py

% # when ready: DRY_RUN=false python3 ../script.py
```

## Background

I made this so I could [transfer ROMs to my SBC handheld](https://old.reddit.com/r/SBCGaming/) without having to wait forever and polluting the microSD card with junk ROMs.

Tested on Windows + wsl.exe, **not tested in Powershell, but it should work...**
