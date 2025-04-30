from process_manager import ProcessManager

BRAVE_PATH = [
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "https://www.netflix.com/browse",
]

manager = ProcessManager()
manager.open_process(path=BRAVE_PATH, title="brave", monitor_index="4", max_mize=True)
