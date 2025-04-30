@echo off
taskkill /f /im steam.exe
nircmd.exe setdefaultsounddevice "PHL 323E7"
"C:\Development\KDEConnectCommands\KDE-Commands-Windows\.venv\Scripts\python.exe" "C:\Development\KDEConnectCommands\KDE-Commands-Windows\scripts\steam.py"
