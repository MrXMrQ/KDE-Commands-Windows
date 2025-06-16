@echo off
nircmd speak text "ending steam"
taskkill /f /im steam.exe
nircmd.exe setprimarydisplay 1