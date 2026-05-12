import pyautogui
import time

while True:
    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Move the mouse cursor slightly
    pyautogui.move(30, 30)

    # Perform a mouse click
    pyautogui.click()

    time.sleep(3)

    # Move the mouse cursor back to the original position
    pyautogui.moveTo(current_x, current_y)

    time.sleep(3)
