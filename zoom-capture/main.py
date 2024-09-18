from lib import Capture

Zoom = Capture.find_zoom_window()
print(Zoom)

Screenshot = Capture.capture_window(Zoom)

print(f"Caputured: {Screenshot}")