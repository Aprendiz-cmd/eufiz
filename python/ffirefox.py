
import pyautogui
import time

def open_firefox():

    # Printing basic message
    print(1,'Opening Firefox...')

    # Location the start button
    _start_button_=pyautogui.locateOnScreen('images/start_button.png')
    _location_=pyautogui.center(_start_button_)

    # Clicking the start button
    if not  pyautogui.click(_location_):
        msg(1,'Opened start menu successfully!')
    else:
        msg(3,'Failed to open start menu!')
        ext()

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    
    # Print message
    print(1,'Firefox is now open and running.')

