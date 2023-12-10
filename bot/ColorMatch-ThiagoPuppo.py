import cv2
import numpy as np
import pyautogui
import time

# Função para capturar a tela do jogo
def capture_screen(region=None):
    screen = pyautogui.screenshot(region=region)
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    return screen

# Função para encontrar blocos da mesma cor
def find_color_blocks(screen):
    hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Encontrar contornos dos blocos
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    block_centers = []
    for cnt in contours:
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            block_centers.append((cx, cy))
    
    return block_centers

# Função para interagir com o jogo
def click_blocks(blocks):
    for x, y in blocks:
        pyautogui.click(x, y)
        time.sleep(0.1)

# Configuração inicial
game_region = (0, 0, 800, 600)  

# Loop principal
while True:
    screen = capture_screen(region=game_region)
    blocks_to_click = find_color_blocks(screen)
    click_blocks(blocks_to_click)
    time.sleep(1)  
