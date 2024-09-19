from lib import capture, operate_dir
import datetime,time


while True:
    Zoom = capture.find_zoom_window()
    Screenshot = capture.capture_window(Zoom)

    print(f"Caputured: {Screenshot}")

    path = operate_dir.daily_dir()
    date = datetime.datetime.now()

    formatted_date = date.strftime("%Y-%m-%dT%H_%M_%S")


    file_path = f"{path}\\{formatted_date}.png"
    Screenshot.save(file_path)

    print(f"Saved screenshot to: {file_path}")
    time.sleep(10)
