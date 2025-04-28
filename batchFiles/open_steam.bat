@echo off
taskkill /f /im steam.exe
timeout /t 1
start "" "C:\Program Files (x86)\Steam\steam.exe" -bigpicture -tenfoot
"C:\ToolsNirSoft\nircmd.exe" setdefaultsounddevice "PHL 323E7"
timeout /t 5
"C:\ToolsNirSoft\nircmd.exe" win move ititle "Steam Big Picture" 4480 0 1920 1080
