""""      1  2  3  4  5  6  7  8  9"""
from gamechecker import GameChecker
import cv2
import numpy

cap = cv2.VideoCapture(1)
game =GameChecker(capture=cap,watch=False)

fields=game.getGamestate12()

index = 0
left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fields)
for element in fields:
    print(left)
    if int(element) != 0:
        left.pop(index)
    else:
        index += 1

if str(numpy.array(left)) == "[]":
    left = 0

print(left)
