from lib import Capture
import os

Zoom = Capture.find_zoom_window()
Screenshot = Capture.capture_window(Zoom)

print(f"Caputured: {Screenshot}")

