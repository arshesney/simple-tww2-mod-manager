# simple-tww2-mod-manager

Simple mod manager to add some degree of profiles using the official CA launcher.

The launcher stores the mod list in a plain JSON file in %APPDATA%\The Creative Assembly\Launcher\20190104-moddata.dat (that date seems hardcoded in the launcher), and it is shared between all supported games.

The goal is to provide a simple frontend written in Python and Qt in order to read and edit the modlist, storing profiles elsewhere.

Uses the SteamworkPy library by Gramps: https://github.com/Gramps/SteamworksPy

Python modules: PyQt5, pandas
