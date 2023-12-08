import pyautogui
import keyboard
import win32api,win32con
import time


def Click(x,y):
      win32api.SetCursorPos((x,y))
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


time.sleep(2)
while keyboard.is_pressed('c') == False:
    sc = pyautogui.screenshot(region=(201,315,580,530))
    width,height = sc.size
    
    for x in range(0,width,12):
            achou = 0
            for y in range(0,height,12):
                  r,g,b = sc.getpixel((x,y))
                  print(r,g,b)
                  if r == 255 and g == 219 and b == 195:
                        achou = 1
                        Click(201+x,315+y)
                        time.sleep(0.1)
                        break
            if achou ==1:
                  break



