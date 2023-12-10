#Marcos Miguel S.Cardoso
#https://www.classicgame.com/game/Whack+a+Mole

#pip install opencv-python
#pip install pyautogui

#imports
from re import template
import cv2
import pyautogui
from time import sleep


pyautogui.PAUSE = 0


template = cv2.imread("imgs/nose.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]


x, y, w, h = 523, 247, 875, 679


sleep(3)



while True:

  
    pyautogui.screenshot("imgs/image.png", (x, y, w, h))
    image = cv2.imread("imgs/image.png")

    while True:

        
        image_mini = cv2.resize(
            src = image,
            dsize = (450,350) 
        )
        cv2.imshow("vision", image_mini)
        cv2.waitKey(10)

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(
            image = image_gray,
            templ = template_gray,
            method = cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        
        if max_val >= 0.8:
            #pyautogui.click(
            #    x = max_loc[0] + x, #screen x
            #    y = max_loc[1] + y  #screen y
            #)

            image = cv2.rectangle(
                img = image,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + template_w, # = pt2 x 
                    max_loc[1] + template_h # = pt2 y
                ),
                color = (0,0,255),
                thickness = -1 
            )
        
        else:
            break