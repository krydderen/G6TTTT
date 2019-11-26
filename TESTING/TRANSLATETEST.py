from XOto012 import translate
from gamechecker import GameChecker
import cv2

cap = cv2.VideoCapture(0)

game = GameChecker(capture=cap,watch=False)

old = game.getGamestateXO()
print(old)

new = game.getGamestate12()
print(str(new))