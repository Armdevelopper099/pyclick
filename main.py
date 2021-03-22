from pynput.mouse import Button, Controller
import time
import pyautogui

mouse = Controller()

# Move pointer relative to current position

def everysecond():
    import time
    
    while True:
        #pyautogui.moveTo(262, 21, 2)
        pyautogui.moveTo(100, 21, 2)
        time.sleep(2)
        mouse.click(Button.left)
        time.sleep(1)
        #pyautogui.moveTo(470, 21, 2)
        pyautogui.moveTo(200, 21, 2)
        time.sleep(1)
        mouse.click(Button.left)
        time.sleep(5)

everysecond()
