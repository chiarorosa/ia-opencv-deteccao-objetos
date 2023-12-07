from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import numpy

jogarNovamente= (1434, 489)
dinossauro = (1174,508)

def restart():
    pyautogui.click(jogarNovamente)

def pegar_imagem():
    box = (dinossauro[0]+55, dinossauro[1], dinossauro[0]+145, dinossauro[1]+5) # cria uma tupla com as coordenadas da caixa que vou ficar de olho para ver se altera a cor
    imagem = ImageGrab.grab(box) # cria a imagem
    cinza = ImageOps.grayscale(imagem) # transforma a imagem em escala de cinza
    a = numpy.array(cinza.getcolors()) # cria um array com os valores da imagem
    return a.sum() # retorna a soma dos valores da imagem


time.sleep(4)
restart()

while True:
    pegar_imagem()
    if pegar_imagem() != 697: # se a soma dos valores da imagem for diferente de 697, significa que a minha caixa mudou de cor
        time.sleep(0.1)
        pyautogui.keyDown('space')
        time.sleep(0.1)