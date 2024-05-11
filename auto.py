from pywinauto import Application
import time

# Start Notepad
app = Application(backend="uia").start("notepad.exe")
time.sleep(2)  # Allow some time for Notepad to open

# Access the Notepad window
notepad = app.window(title="Untitled - Notepad")

# Type some text
notepad.Edit.type_keys("Hello, this is automated text!")

# Save the file
notepad.menu_select("File -> Save")
save_dialog = app.window(title="Save As")
save_dialog.Edit.type_keys("C:\\Users\\hp\\Programs\\wow.txt")
save_dialog.Save.click()

# Close Notepad
notepad.close()

# If prompted to save changes, choose "Don't Save"
app.window(title="Notepad").Wait("ready", timeout=5)
app.window(title="Notepad").type_keys("^n")  # Press Ctrl+N to start a new document

# Quit the application
app.kill()
