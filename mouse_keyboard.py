import pyautogui
import time

# Start Notepad
pyautogui.hotkey('win', 'r')  # Open Run dialog
time.sleep(1)
pyautogui.write('notepad.exe')
pyautogui.press('enter')
time.sleep(1)

# Type some text
pyautogui.write("Hello, this is automated text!")

# Save the file
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write("C:\\Users\\hp\\Programs\\wow.txt")
pyautogui.press('enter')

# Close Notepad
#pyautogui.hotkey('alt', 'f4')

# If prompted to save changes, choose "Don't Save"
#pyautogui.press('n')

# Close Run dialog
#pyautogui.hotkey('alt', 'f4')
