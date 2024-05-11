import pyautogui
import time
# Press Win+Shift+S to capture a screenshot of a region
pyautogui.hotkey('winleft', 'shift', 's')

# Move the mouse to the desired starting position for cropping
# You can adjust the coordinates according to your needs
start_x = 300
start_y = 480
time.sleep(3)
pyautogui.moveTo(start_x, start_y)

# Click and hold the mouse button to start cropping
pyautogui.mouseDown()

# Move the mouse to the desired ending position for cropping
# You can adjust the coordinates according to your needs
end_x = 1200
end_y = 600
pyautogui.moveTo(end_x, end_y)

# Release the mouse button to complete the cropping
pyautogui.mouseUp()
