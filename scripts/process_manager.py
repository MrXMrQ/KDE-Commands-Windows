import subprocess
import pygetwindow
import time
import screeninfo


class ProcessManager:
    def __init__(self) -> None:
        self._monitors = self._list_monitors()
        self._active_processes = []
        pass

    def _list_monitors(self) -> list:
        """Returns a list of connected monitors."""
        return screeninfo.get_monitors()

    def open_process(
        self,
        path: str,
        title: str,
        monitor_index: str = "1",
        max_mize: bool = True,
        min_mize: bool = False,
        width: int = 1920,
        height: int = 1080,
    ) -> None:
        """Opens a process and moves the window to the specified monitor."""
        try:
            process = subprocess.Popen(path)
        except Exception as e:
            raise ValueError(f"'{path}' is not valid! Error: {e}")

        time.sleep(1)

        target_monitor = None
        for i, monitor in enumerate(self._monitors):
            if monitor_index in monitor.name:
                print(monitor.name)
                target_monitor = monitor

        if target_monitor is None:
            raise KeyError(f"Monitor index {monitor_index} not found")

        target_x, target_y = target_monitor.x, target_monitor.y
        print(target_x, target_y)

        windows = pygetwindow.getWindowsWithTitle(title)

        if windows:
            window = windows[0]
            window.moveTo(target_x, target_y)
            window.restore()

            if max_mize:
                window.maximize()
                return
            elif min_mize:
                window.minimize()
                return

            window.resizeTo(width, height)
        else:
            raise ValueError(f"Window for process at '{path}' not found.")

    def __str__(self) -> str:
        """Returns a string representation of the connected monitors."""
        if not self._monitors:
            return "No monitors connected."

        monitor_str = ""
        for i, monitor in enumerate(self._monitors):
            monitor_str += f"Monitor {i+1}: \nName: {monitor.name} \nResolution: {monitor.width}x{monitor.height} \nPosition: ({monitor.x}, {monitor.y}) \n----------------------\n"
        return monitor_str

    @property
    def monitors(self) -> list:
        """Returns the list of monitors."""
        return self._monitors
