@echo off
nircmd.exe setdefaultsounddevice "Headphones"
nircmd speak text "starting dev environment"
"C:\Development\KDEConnectCommands\KDE-Commands-Windows\.venv\Scripts\python.exe" "C:\Development\KDEConnectCommands\KDE-Commands-Windows\scripts\dev_environment.py" 
pause
