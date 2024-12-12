import time
import pyautogui

while True:
    # Wait for 15 seconds
    print("Waiting for 15 seconds...")
    time.sleep(15)

    # Press the down arrow key
    print("Pressing the download arrow key...")
    pyautogui.press("down")
