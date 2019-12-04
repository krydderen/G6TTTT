import numpy as np
import operator
"""            X  O     """
currentWins = [0, 0]
while 1:
    win = input(" X OR O")
    if win == "x":
        currentWins[0] = currentWins[0].__add__(1)
    if win == "o":
        currentWins[1] = currentWins[1].__add__(1)

    if currentWins[1] == 5 or currentWins[0] == 5:
        break
    print(currentWins.__str__())

print("#1: " + str(currentWins[0]) + "   #2: " + str(currentWins[1]))
