import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

lower_blue = np.array([93, 54, 51])
upper_blue = np.array([135, 216, 255])

lower_red = np.array([0, 165, 4])
upper_red = np.array([80, 255, 255])

# Enlarge the mask
kernel = np.ones((5, 5), np.uint8)

win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

while True:
    startT = time.time()
    ret, frame = cap.read()
    roi = frame[76:386, 168:484]

    tiles = [roi[0:80, 0:80],
             roi[0:80, 100:180],
             roi[0:80, 205:285],
             roi[100:180, 0:100],
             roi[100:180, 100:180],
             roi[100:180, 205:285],
             roi[200:275, 0:100],
             roi[200:275, 100:180],
             roi[200:275, 205:285]]

    index = 0
    game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    for tile in tiles:

        # Convert RGB to HSV
        hsv = cv2.cvtColor(tile, cv2.COLOR_BGR2HSV)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)

        dilation_blue = cv2.dilate(blue_mask, kernel)
        dilation_red = cv2.dilate(red_mask, kernel)

        contours_blue, hierarchy = cv2.findContours(dilation_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_red, hierarchy = cv2.findContours(dilation_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours_blue) > 0:
            game_state[index] = "O"

        if len(contours_red) > 0:
            game_state[index] = "X"
        index += 1

    print(game_state)

    for comb in win_combinations:
        if game_state[comb[0]] == "X" and game_state[comb[1]] == "X" and game_state[comb[2]] == "X":
            print("Player 1 Wins")

        elif game_state[comb[0]] == "O" and game_state[comb[1]] == "O" and game_state[comb[2]] == "O":
            print("Player 2 Wins")
        else:
            continue

    cv2.imshow("frame", roi)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
