# pip install PyAutoGUI      ----> Run in your terminal first

# Importing the pyautogui module for automating GUI interactions
import pyautogui

# Importing the sleep function from the time module
from time import sleep

# Loop to repeat the action 7 times (automatic)
for i in range(0, 7, 1):
    # Typing 'I love you' with an interval of 0.1 seconds between each character
    pyautogui.write('I love you', interval=0.1)
    
    # Pressing the 'enter' key
    pyautogui.press('enter')
