import time
import pyautogui
import keyboard
import random

def click(x, y):
    pyautogui.click(x, y)
    time.sleep(0.1)

while not keyboard.is_pressed('q'):
    random_x = random.randint(500, 700)
    random_y = random.randint(300, 500)

    if pyautogui.pixel(random_x, random_y) == (0, 0, 255):
        click(random_x, random_y)
