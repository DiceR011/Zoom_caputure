import pygetwindow as gw
import pyautogui as pag
import time
from datetime import datetime

def find_zoom_window():
    zoom_windows = [win for win in gw.getAllTitles() if 'Zoom ミーティング' in win in win]
    if zoom_windows:
        return gw.getWindowsWithTitle(zoom_windows[0])[0]
    else:
        print("Zoom window not found!")
        exit()

def capture_window(window):
    window.activate()
    time.sleep(0.05)
    screenshot = pag.screenshot(region=(window.left, window.top, window.width, window.height))
    return screenshot