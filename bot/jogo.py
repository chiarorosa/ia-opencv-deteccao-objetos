#daniel borba soares
#https://www.agame.com/game/going-balls

import time

import pyautogui
import keyboard
import win32api
import win32con

def clique_e_move(x, y, deslocamento_y):
    # Define a posição do cursor do mouse para as coordenadas (x, y)
    win32api.SetCursorPos((x, y))
    
    # Aguarda um curto período de tempo
    time.sleep(0.01)
    
    # Simula um clique do botão esquerdo do mouse pressionado
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    
    # Aguarda um curto período de tempo antes de mover o mouse
    time.sleep(0.1)
    
    # Mover o mouse para frente (aumenta a coordenada y)
    win32api.SetCursorPos((x, y + deslocamento_y))
    
    # Aguarda um curto período de tempo
    time.sleep(0.1)
    
    # Simula um clique do botão esquerdo do mouse liberado
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Exemplo de uso
if __name__ == "__main__":
    print("Pressione 'q' para sair.")
    
    while not keyboard.is_pressed('q'):
        # Obtenha a largura e altura da tela
        screen_width, screen_height = pyautogui.size()
        
        # Calcule o ponto central da tela
        centro_x, centro_y = screen_width // 2, screen_height // 2
        
        # Chame a função clique_e_move para simular o clique e mover o mouse para frente
        clique_e_move(centro_x, centro_y, deslocamento_y=50)
        
        # Aguarde 1 segundo antes de repetir o processo
        time.sleep(1)
