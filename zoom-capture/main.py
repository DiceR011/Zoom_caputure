from lib import capture, operate_dir
import os

Zoom = capture.find_zoom_window()
Screenshot = capture.capture_window(Zoom)

print(f"Caputured: {Screenshot}")
path = operate_dir.daily_dir()

Screenshot.save()

