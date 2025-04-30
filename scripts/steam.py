from process_manager import ProcessManager

STEAM_PATH = [
    "C:\Program Files (x86)\Steam\steam.exe",
    "-tenfoot",
]

manager = ProcessManager()
manager.open_process(
    path=STEAM_PATH, title="GitHub Desktop", monitor_index="4", max_mize=True
)
