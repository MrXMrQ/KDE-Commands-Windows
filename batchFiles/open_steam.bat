@echo off
nircmd.exe setdefaultsounddevice "Bed"
nircmd speak text "starting steam"
taskkill /f /im steam.exe
"C:\Development\KDEConnectCommands\KDE-Commands-Windows\.venv\Scripts\python.exe" "C:\Development\KDEConnectCommands\KDE-Commands-Windows\scripts\steam.py"
