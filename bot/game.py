import cv2
import pyautogui
import mss
import time
import numpy as np

t1 = cv2.imread('t1.png',0)
t2 = cv2.imread('t2.png',0)
t3 = cv2.imread('t3.png',0)
t4 = cv2.imread('t4.png',0)
t5 = cv2.imread('t5.png',0)
t6 = cv2.imread('t6.png',0)
threshold = 0.9

def detect_jump(res, img_rgb):
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
          X = pt[0]
          if X <= 220:
            pyautogui.press('space')
            cv2.rectangle(img_rgb, pt, (pt[0]+10, pt[1]+10), (0,0,255), 2)
            return True

        return False


with mss.mss() as sct:
    # Parte da tela para capturar
    monitor = {"top": 275, "left": 185, "width": 480, "height": 110}

    while "Screen capturing":
        last_time = time.time()

        # Pega os pixeis da tela, e salva na numpy array
        img = np.array(sct.grab(monitor))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res1 = cv2.matchTemplate(img_gray, t1, cv2.TM_CCOEFF_NORMED)
        if detect_jump(res1, img) == False:
           res2 = cv2.matchTemplate(img_gray, t2, cv2.TM_CCOEFF_NORMED)
          if detect_jump(res2) == False:
            res4 = cv2.matchTemplate(img_gray, t4, cv2.TM_CCOEFF_NORMED)
            if detect_jump(res4) == False:
              res3 = cv2.matchTemplate(img_gray, t3, cv2.TM_CCOEFF_NORMED)
              if detect_jump(res3) == False:
                res5 = cv2.matchTemplate(img_gray, t5, cv2.TM_CCOEFF_NORMED)
                if detect_jump(res5) == False:
                  res6 = cv2.matchTemplate(img_gray, t6, cv2.TM_CCOEFF_NORMED)
                  detect_jump(res6)
              
        cv2.imshow("OpenCV/Numpy normal", img)

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Pressiona 'q' para sair
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
