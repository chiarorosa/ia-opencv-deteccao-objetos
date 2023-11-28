# Aluno: Vitor de Mesquita Lopes
# https://www.agame.com/game/bubble-shooter-classic

import time

import pyautogui
import keyboard
import win32api
import win32con


def click(game_area, game_box, next_ball, ball_center):

    # traverse the screenshot from right to left, bottom to top
    # to get the first line of balls
    for y in reversed(range(game_box.height)):
        for x in reversed(range(game_box.width)):

            # if the current pixel is the same as the pixel of the center of the ball, then click on screen
            if game_area.getpixel((x, y)) == next_ball.getpixel(ball_center):
                pyautogui.click(x+game_box.left, y+game_box.top)
                return


def lets_cheat():
    print("Let's do this! (not veeery smartly)")
    while not keyboard.is_pressed('q'):

        # take screenshot of game area
        game_area = pyautogui.screenshot(region=(310, 175, 630, 550))

        # locate the game area in the screen
        game_box = pyautogui.locateOnScreen(
            game_area, grayscale=False, confidence=0.8)

        # take screenshot of ball to throw
        next_ball = pyautogui.screenshot(region=(595, 745, 40, 40))

        # locate the ball in the screen
        ball_box = pyautogui.locateOnScreen(
            next_ball, grayscale=False, confidence=0.8)

        # get center of the ball to after get the pixel color
        ball_center = (int(ball_box.width/2), int(ball_box.height/2))

        # to check if screenshots are ok
        # game_area.save(
        #     r"path\ia-opencv-deteccao-objetos\game_area.png")
        # game_box.save(
        #     r"path\ia-opencv-deteccao-objetos\game_box.png")
        # break

        click(game_area, game_box, next_ball, ball_center)

        # wait 1s to not break the game
        time.sleep(1)


if __name__ == "__main__":
    lets_cheat()
