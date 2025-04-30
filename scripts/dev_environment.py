from process_manager import ProcessManager

VS_CODE_PATH = "C:\\Users\\mbaeu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
GITHUB_DESKTOP_PATH = (
    "C:\\Users\\mbaeu\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
)
OBSIDIAN_PATH = "C:\\Users\\mbaeu\\AppData\\Local\\Programs\\Obsidian\\Obsidian.exe"
SPOTIFY_PATH = "C:\\Users\\mbaeu\\AppData\\Roaming\\Spotify\\Spotify.exe"
BRAVE_PATH = [
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "https://www.google.de/?hl=de",
]

manager = ProcessManager()
manager.open_process(
    path=GITHUB_DESKTOP_PATH, title="GitHub Desktop", monitor_index="1", min_mize=True
)
manager.open_process(
    path=VS_CODE_PATH, title="visual studio code", monitor_index="1", max_mize=True
)
manager.open_process(
    path=SPOTIFY_PATH, title="spotify", monitor_index="2", max_mize=True
)
manager.open_process(path=BRAVE_PATH, title="brave", monitor_index="3", max_mize=True)
