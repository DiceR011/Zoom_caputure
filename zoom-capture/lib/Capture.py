import pygetwindow as gw
import pyautogui as pag
from datetime import datetime

def find_zoom_window():
    zoom_windows = [win for win in gw.getAllTitles() if 'Zoom ミーティング' in win in win]
    if zoom_windows:
        return gw.getWindowsWithTitle(zoom_windows[0])[0]

def capture_window(window):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.png")
    screenshot = pag.screenshot(region=(window.left, window.top, window.width, window.height))
    screenshot.save(filename)
    return filename