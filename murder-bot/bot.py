import pygetwindow as gw
import pyautogui
import time

# Função para verificar se a janela do jogo está ativa
def verificar_janela_do_jogo_ativa(nome_da_janela):
    try:
        return gw.getWindowsWithTitle(nome_da_janela)[0].isActive
    except IndexError:
        return False

# Função para manter a barra de espaço pressionada
def pressionar_barra_espaco_continuamente():
    pyautogui.keyDown('space')

# Função para soltar a barra de espaço
def soltar_barra_espaco():
    pyautogui.keyUp('space')

jogo_em_execucao = False
nome_da_janela_do_jogo = "Jogo Murder no Jogos 360"

try:
    while True:
        if verificar_janela_do_jogo_ativa(nome_da_janela_do_jogo):
            if not jogo_em_execucao:
                print("Janela do jogo ativa. Pressionando a barra de espaço.")
                pressionar_barra_espaco_continuamente()
                jogo_em_execucao = True
        else:
            if jogo_em_execucao:
                print("Janela do jogo não está ativa. Soltando a barra de espaço.")
                soltar_barra_espaco()
                jogo_em_execucao = False
        time.sleep(1)
except KeyboardInterrupt:
    soltar_barra_espaco()
    print("Script interrompido pelo usuário.")
