import pyautogui
import time 
from datetime import datetime
import random
from random import randint

time.sleep(5)
start_time = time.time()
max_duration = 60

while time.time() - start_time < max_duration:
    if (pyautogui.locateCenterOnScreen('aim.png', confidence=0.9)):
        aim = pyautogui.locateCenterOnScreen('aim.png', confidence=0.9)
        pyautogui.moveTo(aim.x, aim.y)
        pyautogui.click(aim.x, aim.y)