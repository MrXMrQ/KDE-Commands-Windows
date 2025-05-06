@echo off
taskkill /f /im brave.exe
nircmd.exe setdefaultsounddevice "Headphones"
nircmd speak text "starting brave"
taskkill /f /im brave.exe
"C:\Development\KDEConnectCommands\KDE-Commands-Windows\.venv\Scripts\python.exe" "C:\Development\KDEConnectCommands\KDE-Commands-Windows\scripts\move_brave.py"