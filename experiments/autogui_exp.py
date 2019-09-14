"""
This is weird, you cannot have permission in pyCharm.
But you can run this on the terminal
"""

import pyautogui

print(pyautogui.position())
'''
Notice that locating the locator requires the size of 
the locator to be consistent. So I would recommend 
to take a new screenshot of locators when moving to a new
platform.
'''
left_loc = pyautogui.locateOnScreen('resources/gui_locator/left_loc.jpg', confidence=.5)

print(left_loc)
