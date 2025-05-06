from process_manager import ProcessManager

BRAVE_PATH = [
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "https://www.youtube.com/feed/subscriptions",
]

manager = ProcessManager()
manager.open_process(path=BRAVE_PATH, title="brave", monitor_index="1", max_mize=True)
