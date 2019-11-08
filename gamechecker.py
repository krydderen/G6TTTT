import cv2
import numpy as np
import time

# Fetch the video captured by the camera
cap = cv2.VideoCapture(1)

# Reduce the camera resolution to 640x480
cap.set(3, 640)
cap.set(4, 480)

# Create the lower and upper boundaries of the color blue
lower_blue = np.array([93, 54, 51])
upper_blue = np.array([135, 216, 255])

# Create the lower and upper boundaries of the color red
lower_red = np.array([0, 165, 4])
upper_red = np.array([80, 255, 255])

# Noise cancelling something
kernel = np.ones((5, 5), np.uint8)

# Create a list of all possible win combinations
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

while True:
    # Start a timer for debugging ( Finding out how long it will take for the program to do one cycle )
    startT = time.time()

    # Read the video captured from the camera and set a Region Of Interest
    ret, frame = cap.read()
    roi = frame[170:330, 275:438]

    # Set up 9 Region Of Interests with the 9 tiles of TTT in mind
    tiles = [roi[0:45, 0:48],
             roi[0:45, 60:105],
             roi[0:45, 120:160],
             roi[55:100, 0:48],
             roi[55:100, 60:105],
             roi[55:100, 120:160],
             roi[115:155, 0:48],
             roi[115:155, 60:105],
             roi[115:155, 120:160]]

    index = 0

    # Reset the gamestate for each cycle
    game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    # Now check for BLUE or RED in each of the tiles in the list of ROIs
    for tile in tiles:

        # Convert RGB to HSV
        hsv = cv2.cvtColor(tile, cv2.COLOR_BGR2HSV)
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)

        # Some magic bamboozling
        dilation_blue = cv2.dilate(blue_mask, kernel)
        dilation_red = cv2.dilate(red_mask, kernel)

        # Checking more magic numbers
        contours_blue, hierarchy = cv2.findContours(dilation_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_red, hierarchy = cv2.findContours(dilation_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # For each magic blue wizard, place "O" where he belongs
        if len(contours_blue) > 0:
            game_state[index] = "O"

        # For each magic red wizard, place "X" where he belongs
        if len(contours_red) > 0:
            game_state[index] = "X"
        index += 1

    # Print the current gamestate, used for debugging
    # print(game_state)

    # Check if the current gamestate gives out any winners or a tie
    for comb in win_combinations:
        # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue scanning
        if "-" not in game_state:
            print("Nobody wins, game ends in a tie")

        elif game_state[comb[0]] == "X" and game_state[comb[1]] == "X" and game_state[comb[2]] == "X":
            print("Player 1 Wins")

        elif game_state[comb[0]] == "O" and game_state[comb[1]] == "O" and game_state[comb[2]] == "O":
            print("Player 2 Wins")

        else:
            continue

    # Shows the picture captured and used for calculating winners, tie or scan again
    cv2.imshow("frame", roi)

    stopT = time.time()

    print(stopT-startT)

    # An escape key to close the program, button assigned is "ESC
    key = cv2.waitKey(1)
    if key == 27:
        break

# When ESC is pressed, close the program
cap.release()
cv2.destroyAllWindows()
